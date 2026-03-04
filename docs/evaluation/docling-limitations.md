# Docling Extraction Limitations and Solutions

> Engineering solutions to four Docling extraction limitations discovered during
> pipeline evaluation. Each section documents the discovery, root cause analysis,
> implemented solution, and measured results.

> **Quick links:** [Extraction Evaluation](./extraction-evaluation.md) |
> [Pipeline Test Set](./pipeline-test-set.md) |
> [Image Catalog](../image-catalog.md)

<br><br>

## Summary

| ID | Limitation | Formats affected | Solution | Measured impact |
|----|-----------|-----------------|----------|-----------------|
| L1 | Office formats use inferior extraction pipeline | DOCX, PPTX, XLSX | `--office-to-pdf` (LibreOffice pre-conversion) | XLSX 0% -> ~100% recall, DOCX 67% -> ~100% recall |
| L2 | Decorative images not filtered | DOCX, PPTX | `--filter-decorative` (dimension + variance heuristics) | DOCX 7/7 caught, 0 FP |
| L3 | DOCX image provenance is empty | DOCX | Page-0 fallback with pixel dimensions | 0 -> 15 crops recovered |
| L4 | GPU acceleration not auto-detected | All formats | AUTO device detection with graceful fallback | 6-10x speedup (3 min T4 vs 20-30 min CPU) |

<br><br>

## L1: Office Formats Use Inferior Extraction Pipeline

### Discovery

Extraction evaluation across 10 documents revealed a stark quality gap between
PDF and Office format results:

| Format | Pipeline | Content recall | Noise rate |
|--------|----------|---------------|------------|
| PDF (digital) | HERON | 98.4% | ~3% (2 FP in 62 images) |
| PPTX | SimplePipeline | 100% | 35% (9 decorative FP) |
| DOCX | SimplePipeline | 67% | 53% (8 decorative FP) |
| XLSX | SimplePipeline | 0% | N/A (0 crops extracted) |

PDF extraction through HERON (neural layout model) delivered near-perfect
recall with implicit decorative filtering. Office formats through
SimplePipeline showed three distinct problems: missing vector content (DOCX),
missing XML charts (XLSX), and decorative noise (DOCX, PPTX).

### Root cause

Docling uses two fundamentally different extraction architectures:

- **HERON** (PDF only): Renders each page at configurable DPI, runs neural
  object detection to identify `PictureItem` regions, and crops them. Layout
  detection inherently ignores decorative elements too small or thin to register
  as picture regions.

- **SimplePipeline** (DOCX, PPTX, XLSX): Extracts embedded images directly
  from the document's media folder (e.g., `ppt/media/`, `word/media/`). No
  layout detection, no page rendering, no filtering.

SimplePipeline cannot extract:
- EMF/WMF vector objects (DOCX charts, diagrams)
- OLE chart objects (DOCX embedded Excel charts)
- XML-defined `<c:chart>` elements (XLSX charts)

These content types exist in the document model but have no raster
representation in the media folder.

### Solution

The `--office-to-pdf` flag converts Office documents to PDF via LibreOffice
headless before Docling extraction, routing all formats through HERON:

```bash
python3 run_docling.py input.xlsx out/ --image-capture --office-to-pdf
```

Internally, the pipeline calls `libreoffice --headless --convert-to pdf` on the
input document, then passes the resulting PDF to Docling's `DocumentConverter`.
HERON processes the converted PDF identically to a native PDF.

### Results

| Document | Format | SimplePipeline | LibreOffice + HERON | Change |
|----------|--------|---------------|---------------------|--------|
| doc20 (workforce dashboard) | XLSX | 0 crops, 0% recall | 17 crops, ~100% recall | Charts now extractable |
| doc19 (energy report) | DOCX | 15 crops, 67% recall, 53% noise | 17 crops, ~100% recall, ~12% noise | Vector charts recovered, noise reduced |
| doc11 (RL lecture) | PPTX | 26 crops, 100% recall, 35% noise | Incomplete (CPU constraint) | Noise reduction expected |

### Trade-offs

- **LibreOffice dependency:** ~200-400 MB (`libreoffice-writer`,
  `libreoffice-calc`, `libreoffice-impress`)
- **Conversion overhead:** 2-10 seconds per document
- **Fidelity loss:** Font substitution and layout reflow may occur. Charts
  placed near page edges can be clipped (observed on 2 of 17 doc20 crops where
  chart titles extended past the printable area)
- **Recommended architecture:** PDF direct to HERON, Office via LibreOffice to
  HERON, standalone images via PIL to HERON -- one extraction pipeline for all
  formats

<br><br>

## L2: Decorative Images Not Filtered

### Discovery

SimplePipeline extraction of Office documents produced significant decorative
noise:

| Document | Format | Total crops | Decorative FP | Noise rate |
|----------|--------|-------------|---------------|------------|
| doc11 (RL lecture) | PPTX | 26 | 9 blank white bars | 35% |
| doc19 (energy report) | DOCX | 15 | 7 line separators + 1 CC badge | 53% |

### Root cause

Investigation of all available Docling configuration options found no built-in
mechanism to filter decorative images:

| Docling feature | Helps? | Why not |
|----------------|--------|---------|
| `do_picture_classification` | Partial | 26-class model has no "decorative" label; blank bars classify as `other` |
| `picture_area_threshold` | No | Only gates the annotation step, not extraction |
| `classification_allow/deny` | No | Same -- only gates annotation, not extraction |
| PPTX backend filtering | No | Extracts all `MSO_SHAPE_TYPE.PICTURE` shapes unconditionally |

SimplePipeline extracts every image from the media folder indiscriminately.
There is no filtering stage between extraction and output.

### Solution

The `--filter-decorative` flag applies a post-extraction filter using combined
heuristics:

```bash
python3 run_docling.py input.docx out/ --image-capture --filter-decorative
```

Three filter rules, applied in order:
1. **Min dimension < 10px:** Catches line separators (e.g., 623x2 pixel bars)
2. **Both dimensions < 50px:** Catches tiny icons and badges
3. **Pixel variance < threshold:** Catches solid-color rectangles

### Results

| Format | Decorative images | Caught | Missed | False positives |
|--------|-------------------|--------|--------|-----------------|
| DOCX (doc19) | 7 line separators | 7 | 0 | 0 |
| PPTX (doc11) | 9 white bars | 0 | 9 | 0 |

The filter is effective for DOCX decorative elements (low-variance, thin line
separators). It is not effective for PPTX decorative bars because slide
background colors give pixel variance of 2700-7400, well above any threshold
that would avoid false positives on real content.

### Relationship to L1

The L1 solution (LibreOffice pre-conversion to HERON) handles PPTX decorative
noise implicitly -- HERON's layout detection ignores elements too small or thin
to register as picture regions. The decorative filter serves as a secondary
safety net for edge cases HERON misses (logos, badges, very small icons) and
for runs that use SimplePipeline directly.

<br><br>

## L3: DOCX Image Provenance Is Empty

### Discovery

DOCX extraction produced `PictureItem` objects in Docling's document model but
zero crops in the output. The pipeline's image capture step requires provenance
data (page number and bounding box) to locate and crop images from page renders.

### Root cause

Docling's DOCX backend does not populate `PictureItem.prov` -- the provenance
list that maps each image to its page location and bounding box. The PPTX
backend sets slide numbers and EMU coordinates correctly, but the DOCX backend
leaves `prov` empty for all `PictureItem` entries.

This means the pipeline's crop extraction code receives valid `PictureItem`
objects (with correct image data) but has no coordinates to determine where on
which page the image appears.

### Solution

A fallback in the image capture step handles empty provenance:

1. If `PictureItem.prov` is empty, assign the image to page 0
2. Use the image's pixel dimensions (from the embedded raster data) as the
   bounding box
3. Log a warning indicating the fallback was used

This produces crops from the embedded image data directly rather than from page
renders, preserving the original resolution. The page-0 assignment means
manifest entries show `page: 0` instead of the actual page number -- acceptable
for evaluation purposes and annotation workflow, where the crop content matters
more than its page location.

### Results

| Document | Before fix | After fix | Notes |
|----------|-----------|-----------|-------|
| doc19 (energy report) | 0 crops | 15 crops | All `PictureItem` entries recovered |

Every DOCX document with embedded images benefits from this fix. The 15 crops
from doc19 include both content images and decorative elements (the decorative
filter from L2 then removes the 8 false positives).

<br><br>

## L4: GPU Acceleration Not Auto-Detected

### Discovery

Initial pipeline runs on Colab GPU runtimes took 20-30 minutes per document --
the same speed as local CPU Docker runs. The GPU was available but not being
used by Docling's HERON model.

### Root cause

Docling's `AcceleratorOptions` defaults to CPU unless explicitly configured.
The HERON layout model and OCR engine support CUDA acceleration, but the
pipeline script was not setting up `AcceleratorOptions` at all, leaving Docling
in its CPU-only default mode.

### Solution

AUTO device detection configures `AcceleratorOptions` to detect CUDA
availability at startup and fall back to CPU gracefully:

```python
AcceleratorOptions(
    num_threads=4,
    device=AcceleratorDevice.AUTO,
)
```

The detected device is logged in the `docling_object_created` event for
verification in run output.

### Results

| Environment | Before | After | Speedup |
|-------------|--------|-------|---------|
| Colab T4 GPU | 20-30 min/doc | ~3 min/doc | 6-10x |
| Local Docker (CPU) | 20-30 min/doc | 20-30 min/doc | No change (no GPU) |

The fix is transparent -- CPU-only environments continue to work without
configuration changes. GPU environments get automatic acceleration.

<br><br>

## Open Issues

### Composite figure grouping

HERON merges adjacent images on the same page into a single `PictureItem`.
Doc02 had 18 catalog images in 10 crops (1.8:1 merging ratio), doc06 had 22
images in 6 crops (3.7:1). No content is lost -- merged crops contain all
visual information -- but the merging is not controllable and there is no
mechanism to express figure-level grouping in the output contract.

This affects annotation quality: a merged crop containing three related photos
should receive a figure-level annotation describing the composite, not three
independent per-image annotations. See
[`notes/design-findings.md`](../../notes/design-findings.md) DF-01 for the
full design analysis.

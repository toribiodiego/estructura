# Pass 2 Workflow: Ground Truth Recording

Step-by-step workflow for recording per-image ground truth during the second
evaluation pass. Covers how to obtain verified reference images independently
of the pipeline under test, and how to fill the analysis template for each
eval subset image.

> **Related:** [Analysis Template](./analysis-template.md) |
> [Annotation Test Set](./annotation-test-set.md) |
> [Image Catalog](../image-catalog.md) |
> [Evaluation README](./README.md)

<br><br>

## Why Independent Image Extraction

The pipeline's image extraction is part of what we evaluate. Using
pipeline-produced crops as reference images would build ground truth around
whatever the pipeline happened to extract -- including any missed images, bad
crop boundaries, or false positives. Ground truth must be independent of the
system under test.

Each eval subset image is extracted and verified outside of the pipeline before
ground truth recording begins.

<br><br>

## Overview

For each eval subset image:

1. **Extract** the image from the source document using format-appropriate
   tools (not the pipeline)
2. **Verify** the extracted image matches the catalog entry (content type,
   figure reference, expected content)
3. **Record** ground truth by viewing the verified image and filling every
   section of the [analysis template](./analysis-template.md)

Steps 1 and 2 produce verified reference crops. Step 3 produces the written
ground truth that scorers use during annotation evaluation.

<br><br>

## Step 1: Image Extraction by Format

Each document format requires a different extraction approach. The image
catalog provides the expected image count, content types, and figure
references for every document.

### Standalone images (WebP, PNG, JPG)

**Documents:** 13, 14, 15, 29

No extraction needed. The fixture file is the image. View it directly.

```text
fixtures/downloaded/table-image/13_artpro_table.webp
fixtures/downloaded/table-image/14_simple_table.png
fixtures/downloaded/table-image/15_timetable.jpg
fixtures/downloaded/table-image/29_nasa_helio_fleet_dec2025.jpg
```

### DOCX

**Documents:** 16, 19

Embedded images are stored inside the DOCX ZIP archive under `word/media/`.
List and extract them:

```bash
# List embedded media files
unzip -l fixtures/downloaded/multi-image/16_cambridge_mitoball_biology.docx | grep word/media/

# Extract all media to a working directory
unzip -j fixtures/downloaded/multi-image/16_cambridge_mitoball_biology.docx \
    "word/media/*" -d /tmp/doc16-crops/
```

Match each extracted file against the catalog entry by viewing the image and
comparing to the figure reference and description.

### PPTX

**Documents:** 11, 12

Embedded images are stored under `ppt/media/` in the PPTX ZIP archive:

```bash
# List embedded media
unzip -l fixtures/downloaded/multi-image/11_policy_gradient_rl_lecture.pptx | grep ppt/media/

# Extract all media
unzip -j fixtures/downloaded/multi-image/11_policy_gradient_rl_lecture.pptx \
    "ppt/media/*" -d /tmp/doc11-crops/
```

PPTX media files include both content images and decorative elements (logos,
bars, backgrounds). Use the catalog's decorative count and descriptions to
identify which extracted files are content vs decorative.

### PDF (digital)

**Documents:** 00, 01, 02, 04, 05, 06

PDF images are embedded in the document stream. Two extraction approaches:

**Option A -- `pdfimages` (poppler-utils):**
Extracts embedded image objects directly from the PDF. Fast, preserves
original resolution. Best for raster images.

```bash
# Extract all images from the PDF
pdfimages -png fixtures/downloaded/vector-heavy/04_anthropic_economic_index.pdf \
    /tmp/doc04-crops/img

# Or extract from a specific page range
pdfimages -png -f 8 -l 8 fixtures/downloaded/vector-heavy/04_anthropic_economic_index.pdf \
    /tmp/doc04-crops/img
```

**Option B -- Page rendering + manual crop:**
Render the page at high resolution and crop the figure region. Required for
vector figures that `pdfimages` cannot extract as single images.

```python
import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("fixtures/downloaded/vector-heavy/04_anthropic_economic_index.pdf")
page = pdf[7]  # 0-indexed, so page 8 = index 7
bitmap = page.render(scale=3)  # 3x for high resolution
image = bitmap.to_pil()
image.save("/tmp/doc04-crops/page8.png")
```

For vector figures (IDs starting with `V`), Option B with manual cropping is
usually necessary since vector content is drawn from PDF path operators rather
than stored as discrete image objects.

### XLSX

**Documents:** 20, 21, 28

Charts in XLSX files are XML-defined objects, not raster images. They must be
rendered to produce a viewable image. Options:

- Open the file in a spreadsheet application and screenshot each chart
- Use a rendering library that can produce chart images from the XML
  definitions

The catalog lists the sheet name and chart type for each chart object. Use
this to locate charts within the file.

### HTML

**Documents:** 22, 23, 24

Images in HTML files are referenced by `<img>` tags with `src` attributes.
Download the image URLs directly:

```bash
# Extract image URLs from the HTML file
grep -oP 'src="[^"]+\.(png|jpg|jpeg|gif|svg|webp)"' \
    fixtures/downloaded/multi-image/22_nasa_global_warming.html

# Download a specific image
curl -fSL -o /tmp/doc22-crops/image01.png "https://example.com/image.png"
```

For HTML files with relative image paths (Docs 23, 24), reconstruct the full
URL from the document's source domain.

<br><br>

## Step 2: Verification

After extracting images for a document, verify each one against the catalog
entry before recording ground truth.

**Verification checklist per image:**

- [ ] Image count matches catalog expectation for this document
- [ ] Each image can be matched to a specific catalog entry (image ID, figure
      reference, content type)
- [ ] Content matches the catalog description (e.g., "line chart showing usage
      share trends" -- does the extracted image actually show that?)
- [ ] Decorative elements are identified and excluded from the eval subset
- [ ] Image is viewable at sufficient resolution for ground truth recording
      (text, labels, and values must be readable)

**Common issues to watch for:**

- **Composite figures:** A single catalog entry may correspond to a multi-panel
  figure. The extraction may produce one image (the full composite) or
  multiple images (individual panels). Match to the catalog's description.
- **Vector vs raster mismatch:** Some PDFs embed a raster preview alongside
  vector content. Ensure the extracted image captures the full figure, not
  just the low-resolution preview.
- **PPTX/DOCX decorative media:** ZIP extraction pulls everything including
  logos, backgrounds, and separator bars. Use the catalog's decorative
  annotations to filter.

<br><br>

## Step 3: Ground Truth Recording

With verified images in hand, fill the analysis template for each eval subset
image. Open the image and the corresponding stub file in
`image-analysis/doc{NN}.md`.

### What to record

For each image, fill every section of the
[analysis template](./analysis-template.md):

| Section | What to write | Rubric dimension |
|---------|---------------|------------------|
| Visual inventory | Every significant visual element, using the content-type-specific format | Completeness (25%) |
| Verifiable facts | Specific, falsifiable statements observable in the image | Accuracy (30%) |
| Hallucination risks | Plausible claims a model might fabricate, with the actual reality | Accuracy (30%) |
| Detail inventory | All concrete details a high-quality annotation would reference | Specificity (25%) |
| Domain context | Background knowledge, document context, technical terminology | Usefulness (20%) |
| Search keywords | Terms that should surface this image in a search system | Usefulness (20%) |
| Quality anchors | Concrete examples of score 40, 70, and 95 for each dimension | All dimensions |

### Recording principles

- **Write only what is directly observable.** Every fact and detail must be
  verifiable by looking at the image. Do not infer from document context
  unless explicitly captured in the "domain context" section.
- **Be exhaustive in the visual inventory.** If a reviewer could say "you
  missed X," the inventory is incomplete. List every significant element.
- **Be specific in verifiable facts.** Not "the chart shows a trend" but "the
  blue line rises from 0.3 at x=100 to 0.7 at x=1000." If a value is not
  readable from the image, do not include it as a fact.
- **Think adversarially for hallucination risks.** Consider what a model would
  plausibly fabricate for this content type: inventing exact values from
  approximate visual positions, adding components not present, misidentifying
  elements.
- **Quality anchors are the most important section.** These calibrate the
  rubric to this specific image. A scorer reading "Score 70: mentions 4 of 6
  data series by color, states the correct trend direction, but misses the
  confidence band annotation" knows exactly what "good" means for this image.

<br><br>

## Ordering: Format-First Approach

Work through one format group at a time. This catches format-specific
extraction issues early and resolves them as a batch before moving to the next
format. Within each format group, process one document at a time -- extract
all crops, verify against the catalog, then record ground truth before starting
the next document.

The `image-analysis/` directory is organized into 6 format subdirectories.
Complete all documents in one subdirectory before moving to the next.

| Order | Format | Directory | Documents | Images | Extraction method |
|-------|--------|-----------|-----------|--------|-------------------|
| 1 | Standalone | `standalone/` | 13, 14, 15, 29 | 4 | View directly (no extraction) |
| 2 | DOCX | `docx/` | 16, 19, 25 | 32 | Unzip `word/media/` |
| 3 | PPTX | `pptx/` | 11, 12, 26, 27 | 79 | Unzip `ppt/media/` |
| 4 | XLSX | `xlsx/` | 20, 21, 28 | 38 | Render charts (screenshot or library) |
| 5 | HTML | `html/` | 22, 23, 24 | 32 | Download `<img>` src URLs |
| 6 | PDF (digital) | `pdf-digital/` | 00, 01, 02, 04, 05, 06, 18 | 153 | `pdfimages` or page render + crop |

**Why this order:**
- Standalone images need zero extraction work -- fast wins to calibrate the
  recording workflow
- DOCX and PPTX use the same ZIP-based extraction pattern
- XLSX charts require rendering (harder tooling), grouped to solve once
- HTML requires network access for remote images
- PDF is last because it has the most images (153) and the most complex
  extraction (vector figures, page rendering, manual cropping)

<br><br>

## Output

When pass 2 is complete:

- 24 filled analysis files across 6 format subdirectories in `image-analysis/`
- Each file has ground truth for every taggable image from that document
- Every section of the analysis template is filled (no blank sections)
- The rubric can be applied with per-image anchors instead of generic scoring
  band descriptions

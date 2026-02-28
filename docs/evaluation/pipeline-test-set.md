# Pipeline Test Set

Document-level test index for end-to-end pipeline extraction testing. Each
row represents one document from the evaluation fixture set. Difficulty is
classified by how challenging it is for the pipeline to **find, isolate, and
crop every image** in the document -- independent of how hard those images are
to annotate.

> **Related:** [Image Catalog](../image-catalog.md) (master reference) |
> [Annotation Test Set](./annotation-test-set.md) (image-level annotation
> evaluation)

<br><br>

## What Pipeline Testing Measures

- **Image detection completeness** -- did the pipeline find all images in the
  document? Compare extracted crop count against the catalog's expected count.
- **Crop boundary accuracy** -- are crops correctly bounded around the image
  content, without clipping or excess whitespace?
- **False positive filtering** -- did the pipeline exclude decorative elements
  (logos, separator bars, gradient strips) while retaining content images?
- **Format handling** -- does the pipeline produce correct output across PDF,
  DOCX, PPTX, XLSX, and standalone image formats?

<br><br>

## Extraction Difficulty Criteria

Extraction difficulty describes how hard it is for the pipeline to correctly
detect and crop all images in a document. It is independent of annotation
difficulty (a document can be easy to extract but contain hard-to-annotate
images).

| Level | Criteria | Typical characteristics |
|-------|----------|------------------------|
| Easy | Simple layout, few images, single format challenge | 0-1 content images, minimal decorative filtering, straightforward format |
| Medium | Mixed content types, moderate image count, some filtering needed | 5-25 images, raster + vector mix, screenshot-heavy, scanned pages |
| Hard | Dense layouts, high image count, vector/raster mix, non-trivial filtering | 20+ images with vector figures, multi-column scans, equation detection, large page counts |

<br><br>

## Test Documents

| Doc | Filename | Format | Pages | Images | Extraction Difficulty | Challenges |
|-----|----------|--------|-------|--------|-----------------------|------------|
| 00 | `00_gemini3_pro_model_card.pdf` | PDF | 9 | 1 | Easy | 2 decorative elements to filter; 1 content image |
| 01 | `01_gpt4_system_card.pdf` | PDF | 60 | 13 | Hard | 12 vector figures requiring PATH/FORM extraction; 1 raster; heavy decorative filtering |
| 02 | `02_icml2019_importance_sampling.pdf` | PDF | 19 | 18 | Medium | 16 raster charts + 2 vector diagrams; dense multi-panel figures on pages 6-7 |
| 03 | `03_imf_economic_impacts_ai.pdf` | PDF | 69 | 0 | Easy | 2 decorative covers to filter; no content images |
| 04 | `04_anthropic_economic_index.pdf` | PDF | 47 | 22 | Hard | 22 vector figures; 2 decorative gradient bars to filter; choropleth maps and multi-panel grids |
| 05 | `05_gemini_multimodal_report.pdf` | PDF | 90 | 31 | Hard | 28 raster + 8 vector; 5 decorative elements; 26 MB file; mixed photos, charts, diagrams |
| 06 | `06_arxiv_2206_01062.pdf` | PDF | 9 | 22 | Medium | 20 near-identical screenshots; 8 decorative separator bars; vector chart + line chart |
| 07 | `07_epa_sample_letter.pdf` | PDF | 3 | 0 | Medium | 3 full-page scans; pipeline must detect scanned pages and handle OCR-only content |
| 08 | `08_xerox_mfp_scan_forestburg.pdf` | PDF | 5 | 0 | Medium | 5 full-page scans; form layout with checkboxes and tables; no separable image content |
| 09 | `09_archive_newspaper_1948.pdf` | PDF | 6 | 0 | Hard | 6 high-resolution scans; photos and illustrations embedded in page images; multi-column layout; no individually extractable crops |
| 10 | `10_medrxiv_llama4_benchmark.docx` | DOCX | -- | 0 | Easy | Text-only DOCX; pipeline must handle gracefully with zero images |
| 11 | `11_policy_gradient_rl_lecture.pptx` | PPTX | 80 | 14 | Medium | 10 algorithm screenshots + 4 equations; 12 blank decorative bars to filter |
| 12 | `12_minnstate_fy2025_budget.pptx` | PPTX | 17 | 1 | Easy | 3 decorative logos to filter; 1 content table image |
| 13 | `13_artpro_table.webp` | WebP | 1 | 1 | Easy | Standalone image; tests WebP format support |
| 14 | `14_simple_table.png` | PNG | 1 | 1 | Easy | Standalone image; tests PNG format support |
| 15 | `15_timetable.jpg` | JPG | 1 | 1 | Easy | Standalone image; tests JPG format support |
| 16 | `16_cambridge_mitoball_biology.docx` | DOCX | -- | 8 | Medium | 6.8 MB DOCX; 1 decorative logo; 8 multi-sub-panel composite photos; TIFF handling |
| 17 | `17_arxiv_fractional_brownian_sde.pdf` | PDF | 24 | 0 | Hard | 63 native LaTeX equations; pipeline must detect and crop equation regions from rendered pages |
| 18 | `18_ibm_microservices_redbook.pdf` | PDF | 170 | 46 | Hard | 170 pages; ~52 taggable figures; diagrams, screenshots, infographics; largest document in corpus |
| 19 | `19_cris_electronic_screens_2023.docx` | DOCX | -- | 10 | Medium | 10 mixed images (charts, photos, infographics); 8 decorative elements to filter |
| 20 | `20_illinois_workforce_dashboard.xlsx` | XLSX | 3 | 5 | Medium | 5 XML-defined chart objects (bar, pie); duplicated across 2 sheets; no raster images |
| 21 | `21_praxie_project_portfolio.xlsx` | XLSX | 1 | 4 | Easy | 4 simple bar chart objects; 1 decorative logo to filter |
| 22 | `22_nasa_global_warming.html` | HTML | -- | 20 | Hard | 20 content images in `<figure>` tags; ~35 navigation thumbnails to filter; remote-hosted images (NASA CDN) |
| 23 | `23_nvie_git_branching_model.html` | HTML | -- | 6 | Easy | 6 inline diagrams; 2 decorative to filter; relative image paths; clean layout |
| 24 | `24_fowler_microservices.html` | HTML | -- | 6 | Medium | 6 architecture diagrams; 8 decorative elements to filter; relative image paths |
| 25 | `25_va_tiu_clinical_manual.docx` | DOCX | -- | 14 | Hard | 14 content screenshots + 5 decorative icons; mixed sizes; clinical software UI |
| 26 | `26_concordia_coen6501_digital_logic.pptx` | PPTX | 62 | 22 | Medium | 22 circuit diagrams (15 raster + 8 WMF); dense slide 13 (7 images); no decorative filtering; mixed sizes |
| 27 | `27_era_annual_report_2023.pptx` | PPTX | 32 | 42 | Hard | 42 content images (maps, charts, paired comparisons); 4 decorative in slide layouts; near-duplicate halves (bilingual); 31 of 32 slides have images |
| 28 | `28_eurostat_climate_driving_forces_2022.xlsx` | XLSX | 49 | 29 | Hard | 29 XML-defined charts across 24 figure sheets; 6 chart types (line, bar, area, pie, scatter, combo); 2 decorative logos; 20 backing data sheets |
| 29 | `29_nasa_helio_fleet_dec2025.jpg` | JPG | 1 | 1 | Medium | Standalone high-res image (10800x7186, 14 MB); tests large raster handling and memory management |

**Notes:**
- "Images" column counts taggable content images (decorative excluded). Compare
  pipeline output against this number to measure detection completeness.
- Standalone images (13, 14, 15) are trivial for extraction (1 image = 1 crop)
  but test format support for WebP, PNG, and JPG.
- Scanned documents (07, 08, 09) have zero individually extractable images but
  test the pipeline's scan detection and OCR routing.

<br><br>

## Coverage Matrix

### By format

| Format | Easy | Medium | Hard | Total |
|--------|------|--------|------|-------|
| PDF (digital) | 2 | 2 | 4 | 8 |
| PDF (scanned) | 0 | 2 | 1 | 3 |
| DOCX | 1 | 2 | 1 | 4 |
| PPTX | 1 | 2 | 1 | 4 |
| Standalone image | 3 | 1 | 0 | 4 |
| XLSX | 1 | 1 | 1 | 3 |
| HTML | 1 | 1 | 1 | 3 |
| **Total** | **9** | **11** | **9** | **29** |

**Documents per cell:**
- PDF (digital) -- Easy: 00, 03 | Medium: 02, 06 | Hard: 01, 04, 05, 17
- PDF (scanned) -- Medium: 07, 08 | Hard: 09
- DOCX -- Easy: 10 | Medium: 16, 19 | Hard: 25
- PPTX -- Easy: 12 | Medium: 11, 26 | Hard: 27
- Standalone -- Easy: 13, 14, 15 | Medium: 29
- XLSX -- Easy: 21 | Medium: 20 | Hard: 28
- HTML -- Easy: 23 | Medium: 24 | Hard: 22

Note: The XLSX file in `fixtures/other/` (medrxiv supplementary data) is
excluded from the active evaluation set.

### By extraction challenge type

| Challenge | Documents | Count |
|-----------|-----------|-------|
| Vector figure extraction | 01, 04, 05 | 3 |
| High image density (20+) | 04, 05, 06, 18, 22, 26, 27, 28 | 8 |
| Decorative filtering | 00, 03, 05, 06, 11, 12, 19, 22, 24, 25, 27, 28 | 12 |
| Scanned pages | 07, 08, 09 | 3 |
| Equation region detection | 17 | 1 |
| Large file size (25+ MB) | 05 | 1 |
| Large page count (100+) | 18 | 1 |
| Multi-sub-panel composites | 16 | 1 |
| High-resolution standalone (10K+ px) | 29 | 1 |
| Non-PDF format | 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 | 18 |

<br><br>

## Coverage Gaps

| Format / Area | Gap | Impact | Priority |
|---------------|-----|--------|----------|
| ~~DOCX~~ | ~~No hard-difficulty documents~~ | Addressed: Doc 25 (VA clinical manual, 19 images, hard) fills DOCX hard gap | -- |
| ~~PPTX~~ | ~~No hard difficulty~~ | Addressed: Doc 27 (ERA annual report, 42 images, hard) fills PPTX hard gap. 4 decorative elements in slide layouts. Docs 11, 26 cover medium. | -- |
| ~~XLSX~~ | ~~Zero evaluation coverage~~ | Addressed: Docs 20 (medium), 21 (easy), 28 (hard) provide XML-defined chart objects across all difficulty levels. Doc 28 adds 29 charts with 6 types including combos. | -- |
| ~~HTML~~ | ~~Zero files~~ | Addressed: Docs 22 (hard), 23 (easy), 24 (medium) cover all difficulty levels | -- |
| Scanned + images | 3 scanned PDFs but all are text-only pages | Tests OCR routing but not image extraction from scans | Medium |
| Standalone (hard) | 3 easy + 1 medium standalone images; no hard | No test of complex single-image extraction (SVG, multi-page TIFF) | Low |

<br><br>

## How to Run

### Extract a single document

```bash
docker compose exec dev python3 \
    src/estructura-java/src/main/resources/scripts/run_docling.py \
    fixtures/downloaded/00_gemini3_pro_model_card.pdf \
    out/pipeline-test/doc00 --image-capture --progress
```

### Verify extraction completeness

After extraction, compare the number of crop files in the output directory
against the "Images" count in the test documents table above:

```bash
ls out/pipeline-test/doc00/crops/ | wc -l
# Expected: 1 content image (+ any decorative that were not filtered)
```

### Run all documents

```bash
for doc in fixtures/downloaded/*; do
    name=$(basename "$doc" | sed 's/\.[^.]*$//')
    docker compose exec dev python3 \
        src/estructura-java/src/main/resources/scripts/run_docling.py \
        "$doc" "out/pipeline-test/$name" --image-capture --progress
done
```

### Evaluate results

For each document, check:

1. **Completeness:** crop count matches expected image count from the catalog
2. **Precision:** no decorative elements appear as content crops
3. **Boundaries:** spot-check crop files for correct bounding (no clipping,
   minimal excess whitespace)
4. **Format:** output structure matches the
   [Output Contract](../output-contract.md)

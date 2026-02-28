# Test Fixtures

This directory contains representative input documents for testing the
estructura image-aware document processing pipeline. Fixtures cover all
supported formats (PDF, DOCX, PPTX) and document categories (multi-image,
vector-heavy, text-heavy, scanned, text-only).

Downloaded files are organized by category in `fixtures/downloaded/` and
are gitignored. Run `scripts/download-fixtures.sh` to fetch them.

<br><br>

## Directory Structure

```text
fixtures/
  downloaded/
    multi-image/           02, 05, 06, 11, 12, 16, 20-27 -- documents with images or chart objects
    vector-heavy/          01, 04 -- figures drawn with vector graphics
    text-heavy/            00, 03, 17 -- mostly prose, few or no images
    scanned/               07, 08, 09 -- scanned documents (image-only or OCR'd)
    text-only/             10 -- no images at all
    table-image/           13, 14, 15 -- standalone table-as-image files
  eval-subset/
    easy/                  easy-difficulty crops (populated after pipeline extraction)
    medium/                medium-difficulty crops
    hard/                  hard-difficulty crops
  other/                   files not part of the evaluation
  ../docs/image-catalog.md               master catalog (images, difficulty, eval subset, gaps)
  ../docs/standards/pdf-image-inspection.md  methodology for PDF structural inspection
```

<br><br>

## Download

```bash
# Full set (28 fixtures, ~90 MB)
./scripts/download-fixtures.sh

# Baseline only (4 documents, ~5 MB)
./scripts/download-fixtures.sh --quick
```

The `--quick` flag downloads only the baseline set for fast iteration.
The full set adds 3 scanned/OCR documents and 6 additional PDFs from
the KVision test catalog.

<br><br>

## Fixture Catalog

### multi-image (raster images across pages)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 02 | `02_icml2019_importance_sampling.pdf` | PDF | 19 | 16 raster, 2 vector | 2.7 MB |
| 05 | `05_gemini_multimodal_report.pdf` | PDF | 90 | 28 raster, 8 vector | 26 MB |
| 06 | `06_arxiv_2206_01062.pdf` | PDF | 9 | 22 raster, 2 vector | ~1 MB |
| 11 | `11_policy_gradient_rl_lecture.pptx` | PPTX | 80 | 14 content, 12 decorative | 1.9 MB |
| 12 | `12_minnstate_fy2025_budget.pptx` | PPTX | 17 | 1 table-image, 3 decorative | 351 KB |
| 16 | `16_cambridge_mitoball_biology.docx` | DOCX | n/a | 8 scientific composites, 1 decorative | 6.8 MB |
| 18 | `18_ibm_microservices_redbook.pdf` | PDF | 170 | ~27 architecture diagrams, ~20 screenshots, ~5 infographics | 7.0 MB |
| 19 | `19_cris_electronic_screens_2023.docx` | DOCX | n/a | 3 chart-simple, 3 chart-complex, 2 photos, 2 infographics | 1.3 MB |
| 20 | `20_illinois_workforce_dashboard.xlsx` | XLSX | 3 sheets | 5 chart objects (3 bar, 2 pie; duplicated across 2 sheets) | 99 KB |
| 21 | `21_praxie_project_portfolio.xlsx` | XLSX | 1 sheet | 4 chart objects (all bar), 1 decorative logo | 58 KB |
| 22 | `22_nasa_global_warming.html` | HTML | -- | 11 charts, 9 photos, ~35 navigation thumbnails | 351 KB |
| 23 | `23_nvie_git_branching_model.html` | HTML | -- | 6 git flow diagrams, 2 decorative | 31 KB |
| 24 | `24_fowler_microservices.html` | HTML | -- | 6 architecture diagrams, 8 decorative | 84 KB |
| 25 | `25_va_tiu_clinical_manual.docx` | DOCX | n/a | 14 screenshots, 5 decorative icons | 1.8 MB |
| 26 | `26_concordia_coen6501_digital_logic.pptx` | PPTX | 62 | 22 circuit diagrams (15 raster, 8 WMF) | 1.5 MB |
| 27 | `27_era_annual_report_2023.pptx` | PPTX | 32 | 42 images (maps, charts, paired comparisons), 4 decorative | 1.9 MB |

### vector-heavy (figures drawn with PATH/FORM/TEXT, no raster)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 01 | `01_gpt4_system_card.pdf` | PDF | 60 | 1 raster, 12 vector | 991 KB |
| 04 | `04_anthropic_economic_index.pdf` | PDF | 47 | 2 decorative, 22 vector | 13 MB |

### text-heavy (mostly prose, sparse visual content)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 00 | `00_gemini3_pro_model_card.pdf` | PDF | 9 | 1 table-image, 2 decorative | 849 KB |
| 03 | `03_imf_economic_impacts_ai.pdf` | PDF | 69 | 2 decorative covers | 1.3 MB |
| 17 | `17_arxiv_fractional_brownian_sde.pdf` | PDF | 24 | 0 (63 native LaTeX equations) | 248 KB |

### scanned (image-only or OCR'd full-page scans)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 07 | `07_epa_sample_letter.pdf` | PDF | 3 | 3 full-page scans | 1.93 MB |
| 08 | `08_xerox_mfp_scan_forestburg.pdf` | PDF | 5 | 5 full-page scans | 1.5 MB |
| 09 | `09_archive_newspaper_1948.pdf` | PDF | 6 | 6 high-res OCR'd scans | 23 MB |

### table-image (standalone table screenshots)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 13 | `13_artpro_table.webp` | WebP | 1 | 1 table | 43 KB |
| 14 | `14_simple_table.png` | PNG | 1 | 1 table | 35 KB |
| 15 | `15_timetable.jpg` | JPG | 1 | 1 table | 34 KB |

### text-only (no images)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 10 | `10_medrxiv_llama4_benchmark.docx` | DOCX | n/a | 0 | 11 KB |

<br><br>

## Evaluation Corpus Summary

From [image catalog](../docs/image-catalog.md) (cataloging complete):

| Category | Docs | Content images | Decorative | Vector figures | Tables |
|----------|------|---------------|------------|----------------|--------|
| multi-image | 02, 05, 06, 11, 12, 16, 18, 19, 20-27 | 240 | 90 | 12 | 24 |
| vector-heavy | 01, 04 | 1 | 2 | 34 | 3 |
| text-heavy | 00, 03, 17 | 1 | 4 | 0 | 4 |
| scanned | 07, 08, 09 | 8 | 0 | 0 | 0 |
| text-only | 10 | 0 | 0 | 0 | 4 |
| table-image | 13, 14, 15 | 3 | 0 | 0 | 0 |
| **Total** | **28** | **259** | **96** | **46** | **35** |

See [image catalog](../docs/image-catalog.md) for per-image difficulty
ratings and the selected 64-image evaluation subset.

<br><br>

## Known Gaps

From [image catalog](../docs/image-catalog.md) gap analysis. These need
additional fixtures:

| Gap | Issue | Recommendation |
|-----|-------|----------------|
| ~~table-as-image~~ | ~~Only 1 example~~ | Addressed: 5 examples across 5 docs (Docs 00, 12-15) |
| ~~equation diversity~~ | ~~4 from one source~~ | Addressed: Doc 17 adds 63 native LaTeX equations |
| infographics | 16 total, concentrated in 3 docs | Low priority; partially improved by Docs 18, 19 |
| ~~diagrams~~ | ~~9 total, no complex architecture/UML~~ | Addressed: Doc 18 adds ~27 architecture diagrams |
| ~~photo variety~~ | ~~All from one doc~~ | Improved: Docs 16, 19 add scientific + environmental photos |
| ~~DOCX with images~~ | ~~Text-only~~ | Addressed: Doc 16 (photos), Doc 19 (charts + photos + infographics) |

<br><br>

## Fixture Details

### 00_gemini3_pro_model_card.pdf

- **Source:** https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf
- **Format:** PDF, 9 pages
- **Category:** text-heavy
- **Content:** Google DeepMind Gemini 3 Pro model card. Mostly prose with
  2 native text tables and 1 benchmark table rendered as a raster image.

### 01_gpt4_system_card.pdf

- **Source:** https://cdn.openai.com/papers/gpt-4-system-card.pdf
- **Format:** PDF, 60 pages
- **Category:** vector-heavy
- **SHA-256:** `ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004`
- **Content:** OpenAI GPT-4 system card. 12 vector-drawn figures
  (infographics, bar charts) and 1 raster heatmap. All prompt/response
  examples are rendered as vector graphics, not images.

### 02_icml2019_importance_sampling.pdf

- **Source:** https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/ICML2019-Hanna.pdf
- **Format:** PDF, 19 pages
- **Category:** multi-image
- **SHA-256:** `8160f6e88d54944e9c99571ff6dc759744d33ba9d47178ff7979ac53f5c8b9a3`
- **Content:** Academic RL paper. 16 raster charts (line and bar) plus
  2 vector MDP diagrams. Two-column layout with inline math.

### 03_imf_economic_impacts_ai.pdf

- **Source:** https://www.imf.org/-/media/Files/Publications/WP/2024/English/wpiea2024065-print-pdf.ashx
- **Format:** PDF, 69 pages
- **Category:** text-heavy
- **SHA-256:** `324b4e2c519940ac69c25061597d6b3828b748570025cb966a3d39bd62350948`
- **Content:** IMF working paper. 69 pages of prose with 2 decorative
  cover images and 2 native text tables. Zero content images.

### 04_anthropic_economic_index.pdf

- **Source:** https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf
- **Format:** PDF, 47 pages
- **Category:** vector-heavy
- **SHA-256:** `42c34a517e9184ff06d5e3ab084e8a70c013c6fda60db4c97407bfbd582fde42`
- **Content:** Anthropic economic index report. 22 vector-drawn figures
  (choropleth maps, scatter plots, bar charts, infographic panels).
  Only 2 tiny raster gradient bars. Highest vector complexity in corpus.

### 05_gemini_multimodal_report.pdf

- **Source:** https://arxiv.org/pdf/2312.11805v5.pdf
- **Format:** PDF, 90 pages
- **Category:** multi-image
- **SHA-256:** `8ca95b27851b09c335fa2abe9b84cec5848195a5914eec7fb0b635ba2d8fe4fe`
- **Content:** Google Gemini technical report. Most diverse fixture: 28
  raster images (photos, screenshots, diagrams, charts, memes, video
  frames), 8 vector figures, 18 tables. Largest by page count.

### 06_arxiv_2206_01062.pdf

- **Source:** https://arxiv.org/pdf/2206.01062.pdf
- **Format:** PDF, 9 pages
- **Category:** multi-image
- **Content:** DocLayNet dataset paper. 30 embedded images (mostly
  1025x1025 document page screenshots), 2 vector charts, 5 tables.
  High image density for its page count.

### 07_epa_sample_letter.pdf

- **Source:** https://19january2021snapshot.epa.gov/sites/static/files/2016-02/documents/epa_sample_letter_sent_to_commissioners_dated_february_29_2015.pdf
- **Format:** PDF, 3 pages (scanned)
- **Category:** scanned
- **Content:** Scanned EPA letter. Each page is a single full-page raster
  image (1275x1650 px, ~150 DPI). No native text except 1 TEXT object
  on page 1. Tests OCR quality on typed government correspondence.

### 08_xerox_mfp_scan_forestburg.pdf

- **Source:** https://files.gabbart.com/1605/scanned_from_a_xerox_multifunction_printer.pdf
- **Format:** PDF, 5 pages (scanned)
- **Category:** scanned
- **Content:** Scanned employment application from Forestburg ISD. Pure
  image-only pages (2208x1728 px, ~200 DPI). Contains structured form
  layouts with fields, tables, checkboxes within the scans.

### 09_archive_newspaper_1948.pdf

- **Source:** https://archive.org/download/cupl_003575/cupl_003575_access.pdf
- **Format:** PDF, 6 pages (scanned with OCR)
- **Category:** scanned
- **Content:** 1948 California newspaper. Very high resolution scans
  (~5500x6800 px, ~300 DPI) with OCR text overlay. Contains photos,
  ads, comic strips, crossword, and dense multi-column layouts within
  the scans.

### 10_medrxiv_llama4_benchmark.docx

- **Source:** https://www.medrxiv.org/content/medrxiv/early/2025/10/07/2025.10.05.25337350/DC1/embed/media-1.docx?download=true
- **Format:** DOCX
- **Category:** text-only
- **Content:** Supplementary material with 4 data tables. Zero images.
  Tests DOCX table extraction only.

### 11_policy_gradient_rl_lecture.pptx

- **Source:** https://www.cs.princeton.edu/courses/archive/spring17/cos598F/lectures/RL.pptx
- **Format:** PPTX, 80 slides
- **Category:** multi-image
- **Content:** RL lecture slides. 10 algorithm pseudocode screenshots,
  4 rendered equations, 12 blank decorative bars. 56 of 80 slides are
  text-only.

### 16_cambridge_mitoball_biology.docx

- **Source:** https://www.repository.cam.ac.uk/bitstreams/a5e95699-d0d4-49e1-a471-e7dc381cdbac/download
- **Format:** DOCX (6.8 MB)
- **Category:** multi-image
- **Content:** Cell biology research paper on mitochondrial dynamics during
  insect spermatogenesis. 8 high-resolution scientific composite figures
  (JPEG, 666 KB - 1.1 MB each) containing fluorescence microscopy,
  electron micrographs, bar charts, diagrams, and time-lapse sequences.
  All figures are multi-panel composites (A-I sub-panels). First DOCX
  with content images in the corpus; also addresses photo variety and
  hard-difficulty photo gaps.

### 17_arxiv_fractional_brownian_sde.pdf

- **Source:** https://arxiv.org/pdf/2306.08324.pdf
- **Format:** PDF, 24 pages (248 KB)
- **Category:** text-heavy (equation-dense)
- **Content:** Pure mathematics paper on stochastic differential equations
  driven by fractional Brownian motion. 63 numbered LaTeX equations,
  15 theorems, 9 lemmas, 6 definitions, 7 proofs. Zero embedded images.
  Tests equation region detection in born-digital PDFs and annotation
  of formal mathematical notation.

### 18_ibm_microservices_redbook.pdf

- **Source:** https://www.redbooks.ibm.com/redbooks/pdfs/sg248275.pdf
- **Format:** PDF, 170 pages (7.0 MB)
- **Category:** multi-image
- **Content:** IBM Redbook on microservices architecture patterns. 206 raster
  images across 72 pages containing ~27 architecture diagrams (component,
  sequence, deployment, topology), ~8 process/framework diagrams, ~20 UI
  screenshots (IBM Bluemix console), and ~5 infographics. Addresses the
  architecture/system diagrams gap with diverse diagram types spanning
  easy-to-hard difficulty.

### 19_cris_electronic_screens_2023.docx

- **Source:** https://www.energyrating.gov.au/sites/default/files/2023-06/Cost%20Recovery%20Impact%20Statement%20-%20Electronic%20Screens%20-%202023.docx
- **Format:** DOCX (1.3 MB)
- **Category:** multi-image
- **Content:** Cost Recovery Impact Statement for electronic screen energy
  labelling. 18 media files, all raster PNG/JPEG: 3 simple charts (pie,
  stacked area, bar), 3 complex charts (scatter, multi-line), 2 photos
  (airport scenes), 2 infographics (energy rating labels), 4 decorative
  logos, 3 spacers. First DOCX with mixed raster chart content; addresses
  the DOCX format gap for annotation evaluation.

### 20_illinois_workforce_dashboard.xlsx

- **Source:** https://www.illinoisworknet.com/WIOA/Resources/Documents/6.%20Dashboard%20for%20the%20Local%20Workforce%20Board%20-%20TEMPLATE.xlsx
- **Format:** XLSX, 3 worksheets (99 KB)
- **Category:** multi-image
- **Content:** WIOA workforce board dashboard template from Illinois WorkNet.
  5 unique XML-defined chart objects (3 grouped bar charts, 1 pie chart,
  1 training bar chart) duplicated across Sheets 2 and 3 (10 chart objects
  total). No raster images. Charts cover budget obligations, grant allocation,
  direct training expenditures, and youth workforce learning metrics.

### 21_praxie_project_portfolio.xlsx

- **Source:** https://praxie.com/wp-content/uploads/2021/08/Project-Portfolio-Management-Template.xlsx
- **Format:** XLSX, 1 worksheet (58 KB)
- **Category:** multi-image
- **Content:** Project portfolio management template. 4 single-series bar
  charts summarizing projects by Priority, Status, Risk, and Budget. 1
  decorative Praxie logo (8.5 KB JPEG). Charts are simple aggregation
  summaries with 2-3 categories each.

### 22_nasa_global_warming.html

- **Source:** https://science.nasa.gov/earth/climate-change/global-warming/
- **Format:** HTML (351 KB)
- **Category:** multi-image
- **Content:** NASA science article on global warming evidence and impacts.
  20 content images in `<figure>` elements: 11 charts (temperature anomaly,
  greenhouse gas trends, EPICA reconstruction, IPCC scenarios, sea level
  rise, etc.) and 9 photos (Earth from space, ice cores, glaciers, storms,
  satellite imagery). ~35 navigation thumbnails for unrelated articles in
  header/sidebar that the pipeline must filter. Images are remote-hosted
  (NASA CDN URLs, not embedded). First HTML fixture in the corpus.

### 23_nvie_git_branching_model.html

- **Source:** https://nvie.com/posts/a-successful-git-branching-model/
- **Format:** HTML (31 KB)
- **Category:** multi-image
- **Content:** Vincent Driessen's git-flow branching model blog post. 6 inline
  diagrams showing the complete branching strategy: overall model, centralized
  vs decentralized repos, main branches, feature branches, merge strategies,
  and hotfix workflow. 2 decorative elements (author avatar, PDF icon). Clean
  layout with minimal navigation noise.

### 24_fowler_microservices.html

- **Source:** https://martinfowler.com/articles/microservices.html
- **Format:** HTML (84 KB)
- **Category:** multi-image
- **Content:** Martin Fowler and James Lewis article defining microservice
  architecture. 6 technical diagrams: monolith vs microservices comparison,
  Conway's Law mapping, team organization, decentralized data, deployment
  pipeline, and infrastructure comparison. 8 decorative elements (site logo,
  author photos, book cover, thumbnails, footer branding).

### 25_va_tiu_clinical_manual.docx

- **Source:** https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiutm.docx
- **Format:** DOCX (1.8 MB)
- **Category:** multi-image
- **Content:** VA CPRS Text Integration Utility technical manual. 19 raster
  images: 14 content screenshots of the clinical software interface (dialog
  boxes, data entry forms, record displays, toolbar captures) and 5 small
  decorative icons/buttons. First hard-difficulty DOCX in the corpus; high
  image count with mixed sizes requiring decorative filtering.

### 27_era_annual_report_2023.pptx

- **Source:** https://www.era-online.org/wp-content/uploads/2026/01/Slides-summarizing-AR2023_website.pptx
- **Format:** PPTX, 32 slides (1.9 MB)
- **Category:** multi-image
- **Content:** European Union Agency for Railways (ERA) 2023 annual report
  summary. 42 content images across 31 of 32 slides: European rail network
  maps, horizontal bar/timeline charts, and paired comparison panels. 4
  decorative ERA branding images in slide layouts. Document structure mirrors
  across two halves (slides 2-13 and 14-28), suggesting bilingual or
  year-over-year presentation with near-duplicate charts. First
  hard-difficulty PPTX in the corpus.

### 26_concordia_coen6501_digital_logic.pptx

- **Source:** https://users.encs.concordia.ca/~asim/COEN_6501/Lecture_Notes/Lecture_1_Slides.pptx
- **Format:** PPTX, 62 slides (1.5 MB)
- **Category:** multi-image
- **Content:** Concordia University digital logic design lecture (COEN 6501).
  22 circuit diagrams across 15 slides: full adders, ripple-carry adders,
  half adders, inverters, and assorted logic schematics. 15 raster (PNG/JPEG)
  plus 8 WMF vector metafiles. Slide 13 has 7 images (densest slide). No
  decorative elements in slide masters. Second medium-difficulty PPTX with
  different content type (engineering diagrams vs RL algorithms in Doc 11).

### 12_minnstate_fy2025_budget.pptx

- **Source:** https://www.minnstate.edu/system/finance/budget/docs/fy2025-operating-budget-second-reading-june-2024-final.pptx
- **Format:** PPTX, 17 slides
- **Category:** multi-image
- **Content:** Government budget presentation. 1 financial data table
  rendered as a raster image (North Star Promise Program awards), 3
  decorative Minnesota State logos. Addresses table-as-image gap.

### 13_artpro_table.webp

- **Source:** https://standupsurfshop.com.au/wp-content/uploads/2023/09/ARTPRO-Table.webp
- **Format:** WebP (standalone image)
- **Category:** table-image
- **Content:** Aircraft wing specification table with 6 wing models and
  7 numeric columns. Clean tabular layout with alternating row shading
  and mixed metric/imperial units.

### 14_simple_table.png

- **Source:** https://raw.githubusercontent.com/eihli/image-table-ocr/master/resources/test_data/simple.png
- **Format:** PNG (standalone image)
- **Category:** table-image
- **Content:** Simple spreadsheet cell/format/formula reference table.
  3 columns (Cell, Format, Formula), 5 rows. Clean OCR-friendly layout.

### 15_timetable.jpg

- **Source:** https://courses.washington.edu/fish340/Images/timetable.jpg
- **Format:** JPG (standalone image)
- **Category:** table-image
- **Content:** Color-coded university course timetable ("SWORD Deadlines").
  9-week schedule with 4 assignment types, staggered submission pattern.
  Tests annotation of color-coded tabular layouts.

<br><br>

## Checksum Verification

Five extended-set PDFs have SHA-256 checksums verified during download.
The download script checks these automatically and re-downloads on mismatch.

| Fixture | SHA-256 |
|---------|---------|
| `01_gpt4_system_card.pdf` | `ca3677e1...7b7004` |
| `02_icml2019_importance_sampling.pdf` | `8160f6e8...c8b9a3` |
| `03_imf_economic_impacts_ai.pdf` | `324b4e2c...350948` |
| `04_anthropic_economic_index.pdf` | `42c34a51...2fde42` |
| `05_gemini_multimodal_report.pdf` | `8ca95b27...8fe4fe` |

Baseline set documents do not have published checksums. The download
script skips verification for these files.

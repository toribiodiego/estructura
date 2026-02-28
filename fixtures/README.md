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
    multi-image/           02, 05, 06, 11 -- documents with raster images
    vector-heavy/          01, 04 -- figures drawn with vector graphics
    text-heavy/            00, 03 -- mostly prose, few or no images
    scanned/               07, 08, 09 -- scanned documents (image-only or OCR'd)
    text-only/             10 -- no images at all
  eval-subset/
    easy/                  easy-difficulty crops (populated after pipeline extraction)
    medium/                medium-difficulty crops
    hard/                  hard-difficulty crops
  other/                   files not part of the evaluation (XLSX, etc.)
  image-catalog.md         master catalog of all images, figures, tables per document
  difficulty-tags.md       difficulty ratings, eval subset selection, gap analysis
  pdf-image-inspection-guide.md   methodology for PDF structural inspection
```

<br><br>

## Download

```bash
# Full set (12 documents, ~75 MB)
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

### scanned (image-only or OCR'd full-page scans)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 07 | `07_epa_sample_letter.pdf` | PDF | 3 | 3 full-page scans | 1.93 MB |
| 08 | `08_xerox_mfp_scan_forestburg.pdf` | PDF | 5 | 5 full-page scans | 1.5 MB |
| 09 | `09_archive_newspaper_1948.pdf` | PDF | 6 | 6 high-res OCR'd scans | 23 MB |

### text-only (no images)

| ID | Filename | Format | Pages | Images | Size |
|----|----------|--------|------:|-------:|-----:|
| 10 | `10_medrxiv_llama4_benchmark.docx` | DOCX | n/a | 0 | 11 KB |

<br><br>

## Evaluation Corpus Summary

From image-catalog.md (cataloging complete):

| Category | Docs | Content images | Decorative | Vector figures | Tables |
|----------|------|---------------|------------|----------------|--------|
| multi-image | 02, 05, 06, 11 | 74 | 24 | 12 | 24 |
| vector-heavy | 01, 04 | 1 | 2 | 34 | 3 |
| text-heavy | 00, 03 | 1 | 4 | 0 | 4 |
| scanned | 07, 08, 09 | 8 | 0 | 0 | 0 |
| text-only | 10 | 0 | 0 | 0 | 4 |
| **Total** | **12** | **90** | **30** | **46** | **35** |

See `difficulty-tags.md` for per-image difficulty ratings and the
selected 46-image evaluation subset.

<br><br>

## Known Gaps

From difficulty-tags.md gap analysis. These need additional fixtures:

| Gap | Issue | Recommendation |
|-----|-------|----------------|
| table-as-image | Only 1 example in corpus | Add financial/government report with table screenshots |
| equation diversity | 4 equations, all from one source | Add paper with diverse LaTeX/handwritten equations |
| infographics | 9 total, concentrated in 2 docs | Add consulting slides or data-rich reports |
| diagrams | 9 total, no complex architecture/UML | Add technical documentation with architecture diagrams |
| photo variety | 17 photos, all from one document | Add scientific paper with domain-specific photos |
| DOCX with images | Current DOCX is text-only | Add DOCX with embedded figures |

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

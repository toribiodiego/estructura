# Test Fixtures

This directory contains representative input documents for testing the
estructura image-aware document processing pipeline. Fixtures cover all
supported formats (PDF, DOCX, PPTX, XLSX) and image-aware categories
(text-only, multi-image, scanned, tabular).

Downloaded files live in `fixtures/downloaded/` and are gitignored.
Run `scripts/download-fixtures.sh` to fetch them.

<br><br>

## Download

```bash
# Full set (13 documents, ~77 MB)
./scripts/download-fixtures.sh

# Baseline only (5 documents, ~5 MB)
./scripts/download-fixtures.sh --quick
```

The `--quick` flag downloads only the baseline set for fast iteration.
The full set adds 2 OCR/mixed-content PDFs and 6 additional PDFs from
the KVision test catalog.

<br><br>

## Fixture Catalog

### Baseline Set

| Filename | Format | Pages | Expected Images | Category | Size |
|----------|--------|------:|----------------:|----------|-----:|
| `gemini3_pro_model_card.pdf` | PDF | 9 | ~15 | multi-image | 849 KB |
| `epa_sample_letter.pdf` | PDF | 1 | 0 (scanned) | scanned | 1.93 MB |
| `medrxiv_llama4_benchmark.docx` | DOCX | n/a | 0 | text-only | 11 KB |
| `policy_gradient_rl_lecture.pptx` | PPTX | ~30 | ~25 | multi-image | 1.9 MB |
| `medrxiv_llm_imaging_eval.xlsx` | XLSX | n/a | 0 | tabular | 24 KB |

### OCR and Mixed-Content Set

| Filename | Format | Pages | Expected Images | Category | Size |
|----------|--------|------:|----------------:|----------|-----:|
| `xerox_mfp_scan_forestburg.pdf` | PDF | 5 | 0 (scanned) | scanned | 1.5 MB |
| `archive_newspaper_1948.pdf` | PDF | 6 | 0 (mixed OCR) | mixed-content | 23 MB |

These fixtures support Task 07.4 (OCR Strategy and Document Complexity
Validation). The Xerox scan is a pure image-only PDF from a multifunction
printer. The archive.org newspaper is a scanned 1948 newspaper with an
embedded OCR text layer (67K extractable characters, 85+ font references),
making it a mixed-content document where both text extraction and OCR
produce results.

**Gap:** An image-bearing DOCX with embedded figures is still needed to
test non-PDF image extraction on DOCX format. The current `medrxiv`
DOCX fixture is text-only (11 KB). Candidate sources: DOE OSTI technical
reports, KVision test document collection.

<br><br>

### Extended Set

| Filename | Format | Pages | Expected Images | Category | Size |
|----------|--------|------:|----------------:|----------|-----:|
| `gpt4_system_card.pdf` | PDF | 60 | ~10 | multi-image | 991 KB |
| `icml2019_importance_sampling.pdf` | PDF | 19 | ~8 | multi-image | 2.7 MB |
| `imf_economic_impacts_ai.pdf` | PDF | 69 | ~5 | multi-image | 1.3 MB |
| `anthropic_economic_index.pdf` | PDF | 47 | ~30 | multi-image | 13 MB |
| `gemini_multimodal_report.pdf` | PDF | 90 | ~40 | multi-image | 26 MB |
| `arxiv_2206_01062.pdf` | PDF | ~15 | ~5 | multi-image | ~1 MB |

Image counts are estimates based on document descriptions. Exact counts
will be determined during Task 05 (image capture) and recorded here.

<br><br>

## Fixture Details

### gemini3_pro_model_card.pdf

- **Source:** https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf
- **Format:** PDF, 9 pages
- **Category:** multi-image
- **SHA-256:** not available
- **Content:** Google DeepMind Gemini 3 Pro model card. Contains model
  architecture diagrams, benchmark result charts, and evaluation tables.
  Mix of structured text, tables, and embedded figures across all pages.
- **Why included:** Representative multi-image PDF with mixed content
  types (text, figures, tables). Good baseline for image anchor ordering.

### epa_sample_letter.pdf

- **Source:** https://19january2021snapshot.epa.gov/sites/static/files/2016-02/documents/epa_sample_letter_sent_to_commissioners_dated_february_29_2015.pdf
- **Format:** PDF, scanned image-only
- **Category:** scanned
- **SHA-256:** not available
- **Content:** Scanned EPA letter. Entire document is a raster image with
  no embedded text. OCR is required to extract any text content.
- **Why included:** Tests the scanned document path where Docling
  structure extraction finds no text layers and OCR produces all content.
  No figure elements expected (the whole page is one image).

### medrxiv_llama4_benchmark.docx

- **Source:** https://www.medrxiv.org/content/medrxiv/early/2025/10/07/2025.10.05.25337350/DC1/embed/media-1.docx?download=true
- **Format:** DOCX
- **Category:** text-only
- **SHA-256:** not available
- **Content:** Medical benchmark supplementary material. Text-heavy
  document with tables and structured data. No embedded figures.
- **Why included:** Tests DOCX format support and text-only output path.
  Validates that no spurious image anchors appear in text-only documents.

### policy_gradient_rl_lecture.pptx

- **Source:** https://www.cs.princeton.edu/courses/archive/spring17/cos598F/lectures/RL.pptx
- **Format:** PPTX
- **Category:** multi-image
- **SHA-256:** not available
- **Content:** Princeton university lecture slides on policy gradient
  reinforcement learning. Image-heavy presentation with mathematical
  equations, algorithm diagrams, and conceptual figures on most slides.
- **Why included:** Tests PPTX format support with high image density.
  Validates handling of slide-based documents where most "pages" contain
  at least one figure.

### medrxiv_llm_imaging_eval.xlsx

- **Source:** https://www.medrxiv.org/content/medrxiv/early/2025/10/29/2025.10.27.25338904/DC3/embed/media-3.xlsx?download=true
- **Format:** XLSX
- **Category:** tabular
- **SHA-256:** not available
- **Content:** Medical imaging evaluation data in tabular form. Multiple
  worksheets with numerical data, categories, and evaluation metrics.
- **Why included:** Tests XLSX format support. Validates that tabular
  documents produce structured text output with no image anchors.

### xerox_mfp_scan_forestburg.pdf

- **Source:** https://files.gabbart.com/1605/scanned_from_a_xerox_multifunction_printer.pdf
- **Format:** PDF, scanned image-only
- **Category:** scanned
- **SHA-256:** not available
- **Content:** Scanned document from a Xerox multifunction printer at
  Forestburg ISD. 5-page pure raster image with no embedded text layer
  (0 extractable characters via pdftotext). Used in KVision's OCR
  detection real-world validation test suite as a confirmed image-only
  PDF.
- **Why included:** Tests scanned document handling beyond the 3-page EPA
  letter. Validates OCR behavior on a different scanner source and
  confirms image-only detection heuristics. Critical for Task 07.4 OCR
  strategy testing.

### archive_newspaper_1948.pdf

- **Source:** https://archive.org/download/cupl_003575/cupl_003575_access.pdf
- **Format:** PDF, mixed-content (scanned with embedded OCR layer)
- **Category:** mixed-content
- **SHA-256:** not available
- **Content:** Scanned historical newspaper from September 1, 1948
  (Upland-Ontario, California -- archive.org CUPL 003575). 6-page
  broadsheet with both scanned page images and an embedded OCR text
  layer containing 138K extractable characters and 5,739 lines. The OCR
  layer was added by archive.org's digitization pipeline.
- **Why included:** Tests the mixed-content document scenario where both
  text extraction and OCR produce results. Validates pipeline behavior
  when a PDF has both a text layer and scanned content. Critical for
  Task 07.4 mixed-content document handling.

### gpt4_system_card.pdf

- **Source:** https://cdn.openai.com/papers/gpt-4-system-card.pdf
- **Format:** PDF, 60 pages
- **Category:** multi-image
- **SHA-256:** `ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004`
- **Content:** OpenAI GPT-4 system card. Long-form technical document with
  structured tables, bulleted lists, performance charts, and evaluation
  figures. Heavy on text with periodic figures.
- **Why included:** Tests handling of long documents with structured
  content. Good stress test for page boundary ordering rules.

### icml2019_importance_sampling.pdf

- **Source:** https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/ICML2019-Hanna.pdf
- **Format:** PDF, 19 pages
- **Category:** multi-image
- **SHA-256:** `8160f6e88d54944e9c99571ff6dc759744d33ba9d47178ff7979ac53f5c8b9a3`
- **Content:** Academic paper on importance sampling for reinforcement
  learning. Two-column layout with mathematical notation, algorithm
  pseudocode blocks, and result figures/plots.
- **Why included:** Tests academic paper layout with two-column format,
  inline math, and figure positioning typical of conference papers.

### imf_economic_impacts_ai.pdf

- **Source:** https://www.imf.org/-/media/Files/Publications/WP/2024/English/wpiea2024065-print-pdf.ashx
- **Format:** PDF, 69 pages
- **Category:** multi-image
- **SHA-256:** `324b4e2c519940ac69c25061597d6b3828b748570025cb966a3d39bd62350948`
- **Content:** IMF working paper on economic impacts of AI. Dense text
  with citations, footnotes, and occasional charts. Primarily a text
  document with sparse figures.
- **Why included:** Tests long, text-heavy documents where figures are
  sparse but must still appear at correct document positions.

### anthropic_economic_index.pdf

- **Source:** https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf
- **Format:** PDF, 47 pages
- **Category:** multi-image
- **SHA-256:** `42c34a517e9184ff06d5e3ab084e8a70c013c6fda60db4c97407bfbd582fde42`
- **Content:** Anthropic economic index report. Graphics-heavy document
  with full-page charts, data visualizations, and infographic-style
  layouts. Many pages dominated by visual content.
- **Why included:** Tests graphics-heavy documents where figures outnumber
  text paragraphs. Validates consecutive image anchor handling and
  high image density per page.

### gemini_multimodal_report.pdf

- **Source:** https://arxiv.org/pdf/2312.11805v5.pdf
- **Format:** PDF, 90 pages
- **Category:** multi-image
- **SHA-256:** `8ca95b27851b09c335fa2abe9b84cec5848195a5914eec7fb0b635ba2d8fe4fe`
- **Content:** Google Gemini multimodal capabilities report. Large
  technical document with benchmark tables, architecture diagrams,
  sample outputs, and evaluation figures throughout.
- **Why included:** Largest fixture by both page count and file size
  (26 MB). Stress tests the pipeline for memory usage, processing time,
  and image extraction at scale.

### arxiv_2206_01062.pdf

- **Source:** https://arxiv.org/pdf/2206.01062.pdf
- **Format:** PDF, ~15 pages
- **Category:** multi-image
- **SHA-256:** not available
- **Content:** arXiv research paper. Standard academic format with
  abstract, introduction, methods, results, and figures.
- **Why included:** Used in KVision load balancing tests. Provides a
  medium-size academic paper for performance benchmarking and
  regression testing.

<br><br>

## Image-Aware Categories

| Category | Description | Fixtures |
|----------|-------------|----------|
| text-only | No embedded figures; output contains only text | `medrxiv_llama4_benchmark.docx` |
| multi-image | Multiple figures across pages; tests anchor ordering | `gemini3_pro_model_card.pdf`, `policy_gradient_rl_lecture.pptx`, `gpt4_system_card.pdf`, `icml2019_importance_sampling.pdf`, `imf_economic_impacts_ai.pdf`, `anthropic_economic_index.pdf`, `gemini_multimodal_report.pdf`, `arxiv_2206_01062.pdf` |
| scanned | Image-only PDF with no text layer; requires OCR | `epa_sample_letter.pdf`, `xerox_mfp_scan_forestburg.pdf` |
| mixed-content | Scanned pages with embedded OCR text layer | `archive_newspaper_1948.pdf` |
| tabular | Spreadsheet data; no figures expected | `medrxiv_llm_imaging_eval.xlsx` |

<br><br>

## Expected Outcomes Summary

| Fixture | Text Output | Image Anchors | Notes |
|---------|-------------|---------------|-------|
| `gemini3_pro_model_card.pdf` | Structured text + tables | Yes, ~15 anchors | Mixed content with charts |
| `epa_sample_letter.pdf` | OCR-extracted text | No | Whole page is a scan |
| `medrxiv_llama4_benchmark.docx` | Clean text paragraphs | No | Text-only DOCX |
| `policy_gradient_rl_lecture.pptx` | Slide text content | Yes, ~25 anchors | High image density |
| `medrxiv_llm_imaging_eval.xlsx` | Tabular data as text | No | Spreadsheet format |
| `gpt4_system_card.pdf` | Long-form structured text | Yes, ~10 anchors | Tables and lists |
| `icml2019_importance_sampling.pdf` | Academic text + equations | Yes, ~8 anchors | Two-column layout |
| `imf_economic_impacts_ai.pdf` | Dense text + citations | Yes, ~5 anchors | Sparse figures |
| `anthropic_economic_index.pdf` | Minimal text between charts | Yes, ~30 anchors | Graphics-heavy |
| `gemini_multimodal_report.pdf` | Long technical text | Yes, ~40 anchors | Largest fixture |
| `arxiv_2206_01062.pdf` | Academic text | Yes, ~5 anchors | Medium academic paper |
| `xerox_mfp_scan_forestburg.pdf` | OCR-extracted text | No | Pure image-only scan |
| `archive_newspaper_1948.pdf` | OCR + text layer | No | Mixed scanned/OCR content |

Image anchor counts are estimates. Exact values depend on Docling's figure
detection and will be updated after Task 05 validates the image capture pipeline.

<br><br>

## Checksum Verification

Five extended-set PDFs have SHA-256 checksums verified during download.
The download script checks these automatically and re-downloads on mismatch.

| Fixture | SHA-256 |
|---------|---------|
| `gpt4_system_card.pdf` | `ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004` |
| `icml2019_importance_sampling.pdf` | `8160f6e88d54944e9c99571ff6dc759744d33ba9d47178ff7979ac53f5c8b9a3` |
| `imf_economic_impacts_ai.pdf` | `324b4e2c519940ac69c25061597d6b3828b748570025cb966a3d39bd62350948` |
| `anthropic_economic_index.pdf` | `42c34a517e9184ff06d5e3ab084e8a70c013c6fda60db4c97407bfbd582fde42` |
| `gemini_multimodal_report.pdf` | `8ca95b27851b09c335fa2abe9b84cec5848195a5914eec7fb0b635ba2d8fe4fe` |

Baseline set documents do not have published checksums. The download
script skips verification for these files.

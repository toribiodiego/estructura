# Evaluation

This evaluation framework produces an evidence-based architecture recommendation
for KVision's image-aware document transcription. The results determine which
pipeline approach (custom annotation vs Docling's native VLM integration) and
which vision model to deploy for upstream RAG ingestion on the production
cluster.

The framework covers two tracks that answer different questions:

- **Pipeline coverage** (document-level): Does the pipeline reliably extract
  and crop images across all formats KVision will encounter?
- **Annotation quality** (image-level): Do VLM-generated annotations recover
  enough visual information to be queryable in a text-only RAG system?

Methodology and reference material below cover both tracks, including
document-level extraction testing and image-level annotation quality assessment.

> **Quick links:** [Analysis Template](./analysis-template.md) |
> [Pass 2 Workflow](./pass2-workflow.md) |
> [Pipeline Test Set](./pipeline-test-set.md) |
> [Annotation Test Set](./annotation-test-set.md) |
> [Image Catalog](../image-catalog.md)

<br><br>

## Two-Pass Evaluation Approach

Annotation quality evaluation uses a two-pass methodology to produce calibrated,
reproducible scoring.

**Pass 1 -- Scoring calibration:** Run the rubric against real annotations from
a calibration subset of 8-10 images. Record where scoring is ambiguous, where
ground truth is missing, and where dimension-specific anchors are needed. Output
is a calibration log with priority list, rubric adjustment notes, and
identification of systematic biases.

**Pass 2 -- Ground truth recording:** For each eval subset image, fill in the
analysis template with detailed per-image ground truth: visual inventory,
verifiable facts, hallucination risks, detail inventory, domain context, search
keywords, and annotation quality anchors. This creates the reference material
that makes rubric scoring reproducible.

After both passes, the evaluation framework combines:
1. Annotation rubric (3 dimensions, scoring bands, hard rules)
2. Per-image ground truth (visual inventory, facts, risks)
3. Per-image scoring anchors (40/70/95 examples per dimension)
4. Calibration notes (biases, adjustments)

Target: two independent scorers using the same rubric + ground truth + anchors
agree within +/-10 points on >80% of images.

<br><br>

## How the Files Relate

```text
image-catalog.md              master inventory of all 289 taggable images
       |                      across 31 evaluation fixtures
       v
pipeline-test-set.md          document-level: 31 documents with extraction
       |                      difficulty, format coverage, run instructions
       v
annotation-test-set.md        image-level: 101-image eval subset with annotation
       |                      difficulty, content type matrices, scoring rubric
       v
image-analysis/               per-image ground truth organized by format,
  pdf-digital/                  filled during pass 2 using analysis-template.md
  docx/
  pptx/
  standalone/
  xlsx/
  html/
```

Each layer builds on the previous:
- The **image catalog** is the master reference for what images exist
- The **pipeline test set** tests whether the pipeline can find and crop images
- The **annotation test set** selects the 64-image subset and defines what
  annotation quality means
- The **image analysis files** record the detailed ground truth needed to score
  annotations against concrete per-image reference material

<br><br>

## Directory Contents

| File | Purpose |
|------|---------|
| `README.md` | This file: evaluation methodology overview |
| `analysis-template.md` | Strict template for per-image ground truth, with content-type-specific formats and rubric dimension mapping |
| `pass2-workflow.md` | Step-by-step workflow for pass 2: independent image extraction, verification, and ground truth recording |
| `pipeline-test-set.md` | Document-level test index: 31 documents with extraction difficulty, format coverage, and run instructions |
| `annotation-test-set.md` | Image-level test index: 101-image eval subset with annotation difficulty, content type and format matrices, scoring rubric summary |
| `annotation-rubric.md` | Annotation quality rubric: 3 dimensions (Correctness/Information Recovery/Retrieval Value), scoring anchors, hard rules, tolerance bands, scoring protocol |
| `image-analysis/` | Per-document ground truth files organized by format (6 subdirectories, 24 files) |

<br><br>

## Scoring Dimensions

Annotation quality is scored on three weighted dimensions designed for
text-only RAG evaluation. The full rubric with scoring anchors, hard rules,
per-content-type guidance, and scoring protocol is at
[`annotation-rubric.md`](./annotation-rubric.md).

| Dimension | Weight | What it measures |
|-----------|--------|------------------|
| Correctness | 40% | No hallucinations; stated facts verifiable from image; values within tolerance |
| Information Recovery | 35% | Queryable entities captured; key values extracted; relationships described |
| Retrieval Value | 25% | Natural language prose; domain vocabulary; self-contained for RAG |

<br><br>

## Image Analysis Files

The `image-analysis/` directory contains one file per document that has taggable
images (24 documents across 6 format subdirectories). Files are organized by
source format to support a format-first workflow where all documents of one
format are completed before moving to the next.

### `pdf-digital/` (7 documents, 153 images)

| File | Document | Images | Status |
|------|----------|--------|--------|
| `doc00-gemini3-model-card.md` | 00 -- Gemini 3 Pro model card | 1 | Filled |
| `doc01-gpt4-system-card.md` | 01 -- GPT-4 system card | 13 | Stub |
| `doc02-icml-importance-sampling.md` | 02 -- ICML importance sampling | 18 | Stub |
| `doc04-anthropic-econ-index.md` | 04 -- Anthropic economic index | 22 | Stub |
| `doc05-gemini-multimodal.md` | 05 -- Gemini multimodal report | 31 | Filled |
| `doc06-doclaynet.md` | 06 -- DocLayNet paper | 22 | Stub |
| `doc18-ibm-microservices.md` | 18 -- IBM microservices redbook | 46 | Stub |

### `docx/` (3 documents, 32 images)

| File | Document | Images | Status |
|------|----------|--------|--------|
| `doc16-cambridge-mitoball.md` | 16 -- Cambridge mitoball biology | 8 | Stub |
| `doc19-cris-screens.md` | 19 -- CRIS electronic screens | 10 | Stub |
| `doc25-va-tiu-manual.md` | 25 -- VA TIU clinical manual | 14 | Stub |

### `pptx/` (4 documents, 79 images)

| File | Document | Images | Status |
|------|----------|--------|--------|
| `doc11-policy-gradient-rl.md` | 11 -- Policy gradient RL lecture | 14 | Stub |
| `doc12-minnstate-budget.md` | 12 -- MinnState FY2025 budget | 1 | Stub |
| `doc26-concordia-digital-logic.md` | 26 -- Concordia digital logic | 22 | Stub |
| `doc27-era-annual-report.md` | 27 -- ERA annual report 2023 | 42 | Stub |

### `standalone/` (4 documents, 4 images)

| File | Document | Images | Status |
|------|----------|--------|--------|
| `doc13-artpro-table.md` | 13 -- ArtPro table (WebP) | 1 | Stub |
| `doc14-simple-table.md` | 14 -- Simple table (PNG) | 1 | Stub |
| `doc15-timetable.md` | 15 -- Timetable (JPG) | 1 | Stub |
| `doc29-nasa-helio-fleet.md` | 29 -- NASA heliophysics fleet (JPG) | 1 | Stub |

### `xlsx/` (3 documents, 38 images)

| File | Document | Images | Status |
|------|----------|--------|--------|
| `doc20-illinois-workforce.md` | 20 -- Illinois workforce dashboard | 5 | Stub |
| `doc21-praxie-portfolio.md` | 21 -- Praxie project portfolio | 4 | Stub |
| `doc28-eurostat-climate.md` | 28 -- Eurostat climate driving forces | 29 | Stub |

### `html/` (3 documents, 32 images)

| File | Document | Images | Status |
|------|----------|--------|--------|
| `doc22-nasa-global-warming.md` | 22 -- NASA global warming | 20 | Stub |
| `doc23-nvie-git-branching.md` | 23 -- nvie git branching model | 6 | Stub |
| `doc24-fowler-microservices.md` | 24 -- Fowler microservices | 6 | Stub |

### Totals

| Format | Documents | Images |
|--------|-----------|--------|
| PDF (digital) | 7 | 153 |
| DOCX | 3 | 32 |
| PPTX | 4 | 79 |
| Standalone | 4 | 4 |
| XLSX | 3 | 38 |
| HTML | 3 | 32 |
| **Total** | **24** | **338** |

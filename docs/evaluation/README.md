# Evaluation

Methodology and reference material for evaluating the image-aware document
transcription pipeline. Covers both document-level extraction testing and
image-level annotation quality assessment.

> **Quick links:** [Analysis Template](./analysis-template.md) |
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
1. Generic rubric (4 dimensions, scoring bands)
2. Per-image ground truth (visual inventory, facts, risks)
3. Per-image scoring anchors (40/70/95 examples per dimension)
4. Calibration notes (biases, adjustments)

Target: two independent scorers using the same rubric + ground truth + anchors
agree within +/-10 points on >80% of images.

<br><br>

## How the Files Relate

```text
image-catalog.md              master inventory of all 189 taggable images
       |                      across 20 evaluation fixtures
       v
pipeline-test-set.md          document-level: 20 documents with extraction
       |                      difficulty, format coverage, run instructions
       v
annotation-test-set.md        image-level: 64-image eval subset with annotation
       |                      difficulty, content type matrices, scoring rubric
       v
image-analysis/               per-image ground truth: one file per document,
                              filled during pass 2 using analysis-template.md
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
| `pipeline-test-set.md` | Document-level test index: 20 documents with extraction difficulty, format coverage, and run instructions |
| `annotation-test-set.md` | Image-level test index: 64-image eval subset with annotation difficulty, content type and format matrices, scoring rubric summary |
| `image-analysis/` | Per-document ground truth files (one per document with eval subset images) |

<br><br>

## Scoring Dimensions

Annotation quality is scored on four weighted dimensions. The full rubric with
scoring anchors and protocol is maintained in the evaluation work items.

| Dimension | Weight | What it measures |
|-----------|--------|------------------|
| Accuracy | 30% | Factual correctness, no hallucinations |
| Specificity | 25% | Concrete details vs generic descriptions |
| Completeness | 25% | Coverage of all significant visual elements |
| Usefulness | 20% | Searchability and understanding without seeing the image |

<br><br>

## Image Analysis Files

The `image-analysis/` directory contains one file per document that has images
in the 64-image evaluation subset. 14 documents qualify:

| File | Document | Eval images | Priority |
|------|----------|-------------|----------|
| `doc05.md` | 05 -- Gemini multimodal report | 14 | High (most images) |
| `doc04.md` | 04 -- Anthropic economic index | 9 | High |
| `doc01.md` | 01 -- GPT-4 system card | 6 | High |
| `doc02.md` | 02 -- ICML importance sampling | 6 | High |
| `doc11.md` | 11 -- Policy gradient RL lecture | 6 | High |
| `doc18.md` | 18 -- IBM microservices redbook | 6 | High |
| `doc06.md` | 06 -- DocLayNet paper | 4 | Medium |
| `doc16.md` | 16 -- Cambridge mitoball biology | 4 | Medium |
| `doc19.md` | 19 -- CRIS electronic screens | 4 | Medium |
| `doc00.md` | 00 -- Gemini 3 Pro model card | 1 | Low (single image) |
| `doc12.md` | 12 -- MinnState FY2025 budget | 1 | Low |
| `doc13.md` | 13 -- ArtPro table | 1 | Low |
| `doc14.md` | 14 -- Simple table | 1 | Low |
| `doc15.md` | 15 -- Timetable | 1 | Low |

Fill documents with the most eval subset images first to maximize coverage per
file. Single-image documents can be completed in a batch.

# Annotation Test Set

Image-level test index for annotation quality evaluation. Each row represents
one image from the 64-image evaluation subset selected in the
[Image Catalog](./image-catalog.md). Difficulty is classified by how
challenging it is for a vision model to **accurately and completely describe**
the image content -- independent of how hard the image is to extract from
its source document.

> **Related:** [Image Catalog](./image-catalog.md) (master reference) |
> [Pipeline Test Set](./pipeline-test-set.md) (document-level extraction
> testing)

<br><br>

## What Annotation Testing Measures

- **Accuracy** -- factual correctness, no hallucinations, no fabricated details
- **Specificity** -- concrete details (values, labels, trend directions) vs
  generic descriptions ("a chart about data")
- **Completeness** -- covers all significant visual elements, not just the
  main subject
- **Usefulness** -- searchability and document understanding without seeing the
  image; would this annotation surface in a relevant search?

<br><br>

## Annotation Difficulty Criteria

Annotation difficulty describes how hard it is for a vision model to produce
a high-quality description of an image. It is based on image content complexity,
not on the source document's extraction difficulty.

| Level | Criteria | Examples |
|-------|----------|---------|
| Easy | Single clear subject, obvious content, minimal interpretation needed | Simple bar chart with labeled axes, a photograph, a single equation |
| Medium | Multiple elements to identify and relate, moderate domain knowledge | Multi-series line chart, architecture diagram, algorithm pseudocode box |
| Hard | Dense information, requires understanding relationships or domain context | Multi-panel composite figure, dense scatter plot with annotations, infographic with data layers |

<br><br>

## Test Images

| ID | Source Doc | Source Format | Content Type | Difficulty | Description |
|----|-----------|---------------|-------------|------------|-------------|
| `doc00-R03` | 00 | PDF | table-image | Medium | Benchmark comparison table |
| `doc01-R01` | 01 | PDF | chart-complex | Medium | IF evaluation heatmap, 3x3 color grid |
| `doc01-V01` | 01 | PDF | infographic | Hard | 3-column harmful content comparison, 7 pairs |
| `doc01-V04` | 01 | PDF | infographic | Hard | Disinformation examples, 3-column layout |
| `doc01-V07` | 01 | PDF | infographic | Hard | Tool-augmented risky task, chain-of-thought |
| `doc01-V09` | 01 | PDF | chart-simple | Easy | Bar chart of incorrect behavior rate |
| `doc01-V12` | 01 | PDF | infographic | Hard | Jailbreaks for GPT-4-launch |
| `doc02-R01` | 02 | PDF | chart-complex | Medium | Gridworld MSE with 6 method lines |
| `doc02-R08` | 02 | PDF | chart-simple | Easy | Hopper MSE grouped bar chart |
| `doc02-R10` | 02 | PDF | chart-complex | Hard | 3-panel vertical training curves |
| `doc02-R11` | 02 | PDF | chart-simple | Easy | Policy and Reward line chart (386x252) |
| `doc02-R16` | 02 | PDF | chart-complex | Hard | 3-panel stacked chart (NLL, MSE, Value) |
| `doc02-V01` | 02 | PDF | diagram | Easy | SinglePath MDP state diagram |
| `doc04-V01` | 04 | PDF | chart-complex | Hard | 8-panel grid of line charts |
| `doc04-V03` | 04 | PDF | chart-simple | Easy | Top 20 countries horizontal bar chart |
| `doc04-V05` | 04 | PDF | chart-complex | Hard | World choropleth map by AI Usage Index |
| `doc04-V06` | 04 | PDF | chart-complex | Hard | Income vs AUI scatter plot, log scale |
| `doc04-V09` | 04 | PDF | chart-complex | Hard | 4-panel scatter plots by occupation |
| `doc04-V10` | 04 | PDF | infographic | Medium | Overrepresented request clusters, 4 panels |
| `doc04-V17` | 04 | PDF | chart-complex | Hard | 2-panel Lorenz curves + power-law |
| `doc04-V18` | 04 | PDF | chart-complex | Hard | 2-panel scatter, automation vs augmentation |
| `doc04-V22` | 04 | PDF | chart-complex | Hard | Partial regression scatter plot |
| `doc05-R02` | 05 | PDF | screenshot | Hard | Handwritten physics problem + model response |
| `doc05-R03` | 05 | PDF | diagram | Medium | Gemini architecture overview |
| `doc05-R04` | 05 | PDF | screenshot | Hard | Multimodal matplotlib code gen composite |
| `doc05-R06` | 05 | PDF | photo | Easy | Cooking omelet in pan |
| `doc05-R11` | 05 | PDF | photo | Easy | Persian shield plant |
| `doc05-R15` | 05 | PDF | photo | Medium | Handwritten shapes sequence puzzle |
| `doc05-R17` | 05 | PDF | photo | Medium | Moon photograph (puzzle input) |
| `doc05-R19` | 05 | PDF | photo | Easy | NYC street at night |
| `doc05-R20` | 05 | PDF | other | Medium | Internet meme (humor understanding) |
| `doc05-R21` | 05 | PDF | diagram | Medium | Chinese family tree diagram |
| `doc05-R23` | 05 | PDF | chart-complex | Hard | 4 matplotlib subplots (sin, 3D, contour) |
| `doc05-V03` | 05 | PDF | diagram | Hard | Post-training data flywheel flow diagram |
| `doc05-V04` | 05 | PDF | diagram | Medium | Gemini tool-use control loop |
| `doc05-V06` | 05 | PDF | infographic | Hard | Multimodal chart understanding + response |
| `doc06-R07` | 06 | PDF | screenshot | Medium | CCS annotation UI with bounding boxes |
| `doc06-R09` | 06 | PDF | screenshot | Medium | Figure 4 example (representative of 8) |
| `doc06-R17` | 06 | PDF | screenshot | Medium | Figure 6 example (representative of 6) |
| `doc06-V01` | 06 | PDF | chart-simple | Easy | Pie chart of DocLayNet distribution |
| `doc11-R01` | 11 | PPTX | screenshot | Medium | Tabular TD(0) pseudocode |
| `doc11-R04` | 11 | PPTX | screenshot | Hard | DQN loss function and gradient |
| `doc11-R05` | 11 | PPTX | screenshot | Hard | Deep Q-learning with Experience Replay |
| `doc11-R10` | 11 | PPTX | screenshot | Hard | A3C actor-critic pseudocode |
| `doc11-R11` | 11 | PPTX | equation | Easy | Softmax policy parameterization |
| `doc11-R13` | 11 | PPTX | equation | Medium | Actor-critic update with baseline |
| `doc12-R03` | 12 | PPTX | table-image | Medium | North Star Promise Program financial table |
| `doc13-R01` | 13 | WebP | table-image | Easy | Aircraft wing specification table |
| `doc14-R01` | 14 | PNG | table-image | Easy | Spreadsheet cell/format/formula table |
| `doc15-R01` | 15 | JPG | table-image | Medium | Color-coded course timetable |
| `doc16-R02` | 16 | DOCX | photo | Hard | 9-sub-panel composite: spermatogenesis + microscopy + charts |
| `doc16-R03` | 16 | DOCX | photo | Hard | 7-sub-panel composite: testis + EM + fluorescence |
| `doc16-R05` | 16 | DOCX | photo | Hard | Mitoball ultrastructure at multiple stages |
| `doc16-R08` | 16 | DOCX | photo | Hard | Cross-species comparison (8+ insect species) |
| `doc18-F1-3` | 18 | PDF | diagram | Medium | Microservices architecture |
| `doc18-F2-3` | 18 | PDF | diagram | Medium | Circuit breaker sequence diagram |
| `doc18-F5-2` | 18 | PDF | diagram | Hard | North Star Architecture (DevOps Services) |
| `doc18-F5-8` | 18 | PDF | diagram | Hard | Watson Developer Cloud platform (4-layer) |
| `doc18-F5-9` | 18 | PDF | diagram | Hard | IaaS++ architecture (multi-zone) |
| `doc18-F3-3` | 18 | PDF | infographic | Hard | IBM DevOps framework |
| `doc19-R01` | 19 | DOCX | chart-simple | Easy | Pie chart: equipment market share |
| `doc19-R06` | 19 | DOCX | chart-complex | Medium | Multi-line chart: power vs screen area (9 lines) |
| `doc19-R07` | 19 | DOCX | chart-complex | Hard | Multi-line chart: max power vs area (11 lines, annotated) |
| `doc19-R09` | 19 | DOCX | infographic | Easy | Energy rating label: Super Efficiency |

<br><br>

## By Content Type

| Content Type | Easy | Medium | Hard | Total |
|-------------|------|--------|------|-------|
| chart-simple | 6 | 0 | 0 | 6 |
| chart-complex | 0 | 3 | 11 | 14 |
| diagram | 1 | 5 | 4 | 10 |
| table-image | 2 | 3 | 0 | 5 |
| equation | 1 | 1 | 0 | 2 |
| infographic | 1 | 1 | 6 | 8 |
| photo | 3 | 2 | 4 | 9 |
| screenshot | 0 | 4 | 5 | 9 |
| other | 0 | 1 | 0 | 1 |
| **Total** | **14** | **20** | **30** | **64** |

<br><br>

## By Source Format

| Source Format | Easy | Medium | Hard | Total | % of subset |
|---------------|------|--------|------|-------|-------------|
| PDF | 9 | 15 | 22 | 46 | 72% |
| DOCX | 2 | 1 | 5 | 8 | 13% |
| PPTX | 1 | 3 | 3 | 7 | 11% |
| WebP | 1 | 0 | 0 | 1 | 2% |
| PNG | 1 | 0 | 0 | 1 | 2% |
| JPG | 0 | 1 | 0 | 1 | 2% |
| XLSX | 0 | 0 | 0 | 0 | 0% |
| **Total** | **14** | **20** | **30** | **64** | **100%** |

<br><br>

## By Difficulty

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 14 | 22% |
| Medium | 20 | 31% |
| Hard | 30 | 47% |
| **Total** | **64** | **100%** |

The subset intentionally over-represents hard images (47% vs 25% in the full
corpus) because these are the cases that differentiate model quality. Medium
and hard together comprise 78% of the subset.

<br><br>

## Coverage Gaps

| Area | Gap | Impact | Priority |
|------|-----|--------|----------|
| Equations | Only 2 images in subset (both from PPTX Doc 11) | Insufficient coverage of equation annotation quality | High |
| Table-image | 4 images; 3 are standalone, 1 from PPTX | No embedded table-images from PDF or DOCX in subset | Medium |
| XLSX source | 0 images | Annotation quality on spreadsheet-embedded charts untested | Medium |
| HTML source | 0 images | Annotation quality on web-captured images untested | Medium |
| Standalone hard | 0 hard images from standalone formats | All standalone images are easy; no challenging single-image annotation test | Low |
| Other content type | Only 1 image (`doc05-R20`, internet meme) | Minimal coverage of non-standard image types | Low |

<br><br>

## Scoring Rubric

Annotation quality is scored on four weighted dimensions. The full rubric with
scoring anchors and protocol is in the evaluation work items at
`tmp/task-17-eval/03-design-evaluation-rubric.md`.

| Dimension | Weight | What it measures |
|-----------|--------|------------------|
| Accuracy | 30% | Factual correctness, no hallucinations |
| Specificity | 25% | Concrete details vs generic descriptions |
| Completeness | 25% | Coverage of all significant visual elements |
| Usefulness | 20% | Searchability and understanding without seeing the image |

**Weighted score:**
`score = (accuracy * 0.30) + (specificity * 0.25) + (completeness * 0.25) + (usefulness * 0.20)`

# Annotation Test Set

Image-level test index for annotation quality evaluation. Each row represents
one image from the 102-image evaluation subset selected in the
[Image Catalog](../image-catalog.md). Difficulty is classified by how
challenging it is for a vision model to **accurately and completely describe**
the image content -- independent of how hard the image is to extract from
its source document.

> **Related:** [Image Catalog](../image-catalog.md) (master reference) |
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
| `doc20-C01` | 20 | XLSX | chart-complex | Medium | Grouped bar: Obligations, Accrual & Expense Breakdown (12 series) |
| `doc20-C03` | 20 | XLSX | chart-simple | Easy | Pie: Total WIOA Formula Grant Budget (5 segments) |
| `doc20-C04` | 20 | XLSX | chart-simple | Easy | Grouped bar: Direct Training (4 series) |
| `doc21-C01` | 21 | XLSX | chart-simple | Easy | Bar: Priority distribution (3 bars) |
| `doc21-C04` | 21 | XLSX | chart-simple | Easy | Bar: Budget vs Actual Expenditure (2 bars) |
| `doc22-R01` | 22 | HTML | chart-complex | Medium | GISS temperature anomaly: global surface temperature 1880-present |
| `doc22-R03` | 22 | HTML | chart-complex | Hard | EPICA 800,000-year temperature + CO2 reconstruction from ice cores |
| `doc22-R05` | 22 | HTML | chart-complex | Hard | Anthropogenic vs natural climate attribution comparison |
| `doc22-R09` | 22 | HTML | chart-simple | Easy | Ocean carbon cycle diagram |
| `doc22-R12` | 22 | HTML | photo | Easy | ISS022-E-6674: Earth from space |
| `doc22-R15` | 22 | HTML | photo | Medium | Solar corona comparison: solar maximum vs minimum (side-by-side) |
| `doc23-R01` | 23 | HTML | diagram | Medium | Complete git-flow branching model with merge topology |
| `doc23-R04` | 23 | HTML | diagram | Easy | Feature branch create-and-merge workflow |
| `doc23-R05` | 23 | HTML | diagram | Easy | Merge comparison: fast-forward vs no-ff commit graph |
| `doc24-R01` | 24 | HTML | diagram | Medium | Monolith vs microservices architecture comparison |
| `doc24-R02` | 24 | HTML | diagram | Medium | Conway's Law: org structure mapped to system architecture |
| `doc24-R06` | 24 | HTML | diagram | Medium | Micro-deployment: monolith vs microservices infrastructure |
| `doc25-R08` | 25 | DOCX | screenshot | Medium | UI panel: record display |
| `doc25-R02` | 25 | DOCX | screenshot | Medium | Application window: clinical record view |
| `doc25-R07` | 25 | DOCX | screenshot | Medium | UI panel: form layout |
| `doc25-R19` | 25 | DOCX | screenshot | Medium | Full form: clinical documentation |
| `doc26-R01` | 26 | PPTX | diagram | Medium | Full adder circuit schematic |
| `doc26-R08` | 26 | PPTX | other | Medium | IC pinout specification table |
| `doc26-R13` | 26 | PPTX | diagram | Medium | Sequential multiplier timing/waveform simulation |
| `doc27-R01` | 27 | PPTX | diagram | Medium | European rail map |
| `doc27-R03` | 27 | PPTX | chart-complex | Medium | Paired panel (left), medium format |
| `doc27-R09` | 27 | PPTX | chart-simple | Easy | Wide horizontal chart |
| `doc27-R38` | 27 | PPTX | chart-complex | Medium | Medium panel |
| `doc27-R41` | 27 | PPTX | infographic | Medium | Summary overview |
| `doc27-R42` | 27 | PPTX | infographic | Medium | Summary overview (wide) |
| `doc28-C01` | 28 | XLSX | chart-complex | Medium | Line: GHG emissions index 1990=100, 4 series |
| `doc28-C07` | 28 | XLSX | chart-complex | Medium | Pie-of-pie: GHG by source sector, EU 2020 |
| `doc28-C08` | 28 | XLSX | chart-complex | Hard | Combo (area+bar+line): GHG by sector, 4 series |
| `doc28-C11` | 28 | XLSX | chart-complex | Medium | Stacked area: Electricity/heat from renewables, 7 series |
| `doc28-C24` | 28 | XLSX | chart-complex | Hard | Combo (area+line): LULUCF GHG, 7 series |
| `doc28-C29` | 28 | XLSX | chart-simple | Easy | Pie: GHG by gas type in CO2-equivalents, EU |
| `doc29-R01` | 29 | JPG | diagram | Medium | NASA heliophysics fleet: all active missions |

<br><br>

## By Content Type

| Content Type | Easy | Medium | Hard | Total |
|-------------|------|--------|------|-------|
| chart-simple | 13 | 0 | 0 | 13 |
| chart-complex | 0 | 10 | 15 | 25 |
| diagram | 3 | 13 | 4 | 20 |
| table-image | 2 | 3 | 0 | 5 |
| equation | 1 | 1 | 0 | 2 |
| infographic | 1 | 3 | 6 | 10 |
| photo | 4 | 3 | 4 | 11 |
| screenshot | 0 | 8 | 5 | 13 |
| other | 0 | 2 | 0 | 2 |
| **Total** | **24** | **43** | **34** | **101** |

<br><br>

## By Source Format

| Source Format | Easy | Medium | Hard | Total | % of subset |
|---------------|------|--------|------|-------|-------------|
| PDF | 9 | 15 | 22 | 46 | 45% |
| PPTX | 2 | 11 | 3 | 16 | 16% |
| DOCX | 2 | 5 | 5 | 12 | 12% |
| HTML | 4 | 6 | 2 | 12 | 12% |
| XLSX | 5 | 4 | 2 | 11 | 11% |
| JPG | 0 | 2 | 0 | 2 | 2% |
| WebP | 1 | 0 | 0 | 1 | 1% |
| PNG | 1 | 0 | 0 | 1 | 1% |
| **Total** | **24** | **43** | **34** | **101** | **100%** |

<br><br>

## By Difficulty

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 24 | 24% |
| Medium | 43 | 43% |
| Hard | 34 | 33% |
| **Total** | **101** | **100%** |

The expanded subset shifts the difficulty balance toward medium images (43%)
compared to the original 64-image subset (31% medium). Hard images remain
well-represented at 34%. Medium and hard together comprise 76% of the subset,
ensuring the test set remains weighted toward the cases that differentiate
model quality.

<br><br>

## Coverage Gaps

| Area | Gap | Impact | Priority |
|------|-----|--------|----------|
| Equations | Only 2 images in subset (both from PPTX Doc 11) | Insufficient coverage of equation annotation quality | High |
| Table-image | 5 images; 3 are standalone, 1 from PPTX, 1 from PDF | No embedded table-images from DOCX in subset | Medium |
| Standalone hard | 0 hard images from standalone formats | All standalone images are easy or medium; no challenging single-image annotation test | Low |
| Other content type | 2 images (`doc05-R20` internet meme, `doc26-R08` IC pinout table) | Limited coverage of non-standard image types | Low |

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

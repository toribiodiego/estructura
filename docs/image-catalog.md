# Image Catalog

Master catalog of all images, figures, charts, and diagrams across the
evaluation fixture set. Includes difficulty ratings and evaluation subset
selection.

> **Related:** [Pipeline Test Set](./evaluation/pipeline-test-set.md)
> (document-level extraction testing) |
> [Annotation Test Set](./evaluation/annotation-test-set.md) (image-level
> annotation evaluation) |
> [Image Analysis](./evaluation/image-analysis/) (per-image ground truth)

**Documents cataloged:** 25
**Last updated:** 2026-02-28

<br><br>

## ID Format

Image IDs use the pattern `doc{NN}-{R|V|S}{seq}`:

| Prefix | Meaning |
|--------|---------|
| `R` | Raster (embedded bitmap image) |
| `V` | Vector (PATH/FORM/TEXT-drawn figure) |
| `S` | Scanned (full-page scan) |
| `C` | Chart object (XML-defined, rendered by application) |

Example: `doc05-R11` = Doc 05, raster image #11.

Doc 18 uses figure-based IDs (`doc18-F1-1`) matching the document's own
figure numbering.

<br><br>

## Content Types

| Type | Description |
|------|-------------|
| `chart-simple` | Bar, pie, single-line chart with clear labels |
| `chart-complex` | Multi-series, stacked, scatter with dense data |
| `diagram` | Architecture, flow, process, system diagrams |
| `table-image` | Screenshot or figure of a table (not extracted table) |
| `equation` | Mathematical notation rendered as image |
| `infographic` | Mixed visual with text, icons, data, layout |
| `photo` | Photograph or natural image |
| `screenshot` | UI screenshot, terminal output, code |
| `decorative` | Logo, icon, separator, decorative element |
| `other` | Anything that does not fit above |

<br><br>

## Difficulty Criteria

| Level | Criteria | Examples |
|-------|----------|---------|
| Easy | Single clear subject, obvious content, minimal interpretation needed | Simple bar chart with labeled axes, a photo, a single equation |
| Medium | Multiple elements to identify and relate, moderate domain knowledge | Multi-series line chart, architecture diagram, algorithm pseudocode box |
| Hard | Dense information, requires understanding relationships or domain context | Multi-panel composite figure, dense scatter plot with annotations, infographic with data layers |

<br><br>

## Doc 00 -- 00_gemini3_pro_model_card.pdf

PDF, 9 pages, text-heavy
Source: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc00-R01 | 1 | decorative | 837x13 | -- | Black horizontal bar | Yes: decorative line |
| doc00-R02 | 1 | decorative | 932x312 | -- | Google logo | Yes: decorative logo |
| doc00-R03 | 5 | table-image | 2048x1872 | Medium | Benchmark comparison table: Gemini 3 Pro vs 3 competitors across ~22 benchmarks, color-coded cells | -- |

**Taggable:** 1 (1 medium)

<br><br>

## Doc 01 -- 01_gpt4_system_card.pdf

PDF, 60 pages, vector-heavy
Source: https://cdn.openai.com/papers/gpt-4-system-card.pdf

### Raster

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc01-R01 | 58 | chart-complex | 1448x1317 | Medium | Figure 11: IF evaluation heatmap, 3x3 color-coded grid | -- |

### Vector

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc01-V01 | 8 | infographic | Hard | Figure 1: 3-column harmful content comparison, 7 prompt-response pairs | -- |
| doc01-V02 | 9 | infographic | Medium | Figure 2: Non-adversarial bias example, 3-column comparison | -- |
| doc01-V03 | 10 | infographic | Medium | Figure 3: Biased content examples, 3-column, 2 pairs | -- |
| doc01-V04 | 11 | infographic | Hard | Figure 4: Disinformation examples, 3-column, 3 pairs | -- |
| doc01-V05 | 13 | infographic | Medium | Dual-use substance prompt + response, 2-box layout | -- |
| doc01-V06 | 14 | infographic | Medium | Cybersecurity prompt + response, 2-box layout | -- |
| doc01-V07 | 17 | infographic | Hard | Figure 5: Tool-augmented risky task, chain-of-thought | -- |
| doc01-V08 | 23 | infographic | Hard | Figure 6: RBRM prompt example, styled text boxes | -- |
| doc01-V09 | 23 | chart-simple | Easy | Figure 7: Bar chart of incorrect behavior rate, 3 models | -- |
| doc01-V10 | 25 | chart-simple | Easy | Figure 8: TruthfulQA accuracy bar chart | -- |
| doc01-V11 | 27 | infographic | Medium | Figure 9: GPT-4 classification prompt, natural language rubric | -- |
| doc01-V12 | 28 | infographic | Hard | Figure 10: Jailbreaks for GPT-4-launch, 2 attack types | -- |

**Taggable:** 13 (2 easy, 5 medium, 6 hard)

<br><br>

## Doc 02 -- 02_icml2019_importance_sampling.pdf

PDF, 19 pages, multi-image
Source: https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/ICML2019-Hanna.pdf

### Raster

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc02-R01 | 6 | chart-complex | 1350x1200 | Medium | Figure 2a: Gridworld MSE vs trajectories, 6 method lines with confidence bands | -- |
| doc02-R02 | 6 | chart-complex | 1350x1200 | Medium | Figure 2b: Gridworld Alt | -- |
| doc02-R03 | 6 | chart-complex | 1350x1200 | Medium | Figure 2c: Gridworld On-Policy variant | -- |
| doc02-R04 | 6 | chart-complex | 1350x1200 | Medium | Figure 2d: Gridworld On-Policy Alt | -- |
| doc02-R05 | 6 | chart-complex | 1350x1200 | Medium | Figure 3: SinglePath MDP off-policy estimation | -- |
| doc02-R06 | 6 | chart-complex | 1350x1200 | Medium | Figure 4a: Linear dynamical system MSE | -- |
| doc02-R07 | 6 | chart-complex | 1350x1200 | Medium | Figure 4b: Linear dynamical system alt weights | -- |
| doc02-R08 | 7 | chart-simple | 1800x1600 | Easy | Figure 5a: Hopper MSE grouped bar chart | -- |
| doc02-R09 | 7 | chart-simple | 1800x1600 | Easy | Figure 5b: HalfCheetah MSE grouped bar chart | -- |
| doc02-R10 | 7 | chart-complex | 1350x1200 | Hard | Figure 6: 3-panel vertical chart (error, squared error, estimate) | -- |
| doc02-R11 | 16 | chart-simple | 386x252 | Easy | Figure 7a: Policy and Reward line chart | -- |
| doc02-R12 | 16 | chart-simple | 386x252 | Easy | Figure 7b: 10 Sample Approximation | -- |
| doc02-R13 | 16 | chart-simple | 386x252 | Easy | Figure 7c: 200 Sample Approximation | -- |
| doc02-R14 | 18 | chart-complex | 1350x1200 | Medium | Figure 9a: Gridworld Off-Policy EIS variant | -- |
| doc02-R15 | 18 | chart-complex | 1350x1200 | Medium | Figure 9b: Gridworld On-Policy EIS variant | -- |
| doc02-R16 | 19 | chart-complex | 1350x1200 | Hard | Figure 10: 3-panel stacked chart (NLL, MSE, Value) | -- |

### Vector

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc02-V01 | 5 | diagram | Easy | Figure 1: SinglePath MDP state diagram, s0-s4 with action arrows | -- |
| doc02-V02 | 16 | diagram | Easy | Figure 8: SinglePath MDP diagram (same as Figure 1) | -- |

**Taggable:** 18 (7 easy, 9 medium, 2 hard)

<br><br>

## Doc 03 -- 03_imf_economic_impacts_ai.pdf

PDF, 69 pages, text-heavy
Source: https://www.imf.org/-/media/Files/Publications/WP/2024/English/wpiea2024065-print-pdf.ashx

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc03-R01 | 1 | decorative | 1633x2113 | -- | Cover page background | Yes: decorative cover |
| doc03-R02 | 69 | decorative | 1633x2113 | -- | Back cover background | Yes: decorative cover |

**Taggable:** 0

<br><br>

## Doc 04 -- 04_anthropic_economic_index.pdf

PDF, 47 pages, vector-heavy
Source: https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf

### Raster

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc04-R01 | 17 | decorative | 20x397 | -- | Gradient color bar within scatter plot | Yes: decorative element |
| doc04-R02 | 27 | decorative | 11x248 | -- | Gradient color bar within scatter plot | Yes: decorative element |

### Vector

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc04-V01 | 8 | chart-complex | Hard | Figure 1.1: 8-panel grid of line charts, usage share trends | -- |
| doc04-V02 | 10 | chart-complex | Hard | Figure 1.2: 2-panel automation vs augmentation trends | -- |
| doc04-V03 | 13 | chart-simple | Easy | Figure 2.1: Top 20 countries horizontal bar chart | -- |
| doc04-V04 | 14 | chart-simple | Easy | Figure 2.2: Top 20 countries by AI Usage Index | -- |
| doc04-V05 | 15 | chart-complex | Hard | Figure 2.3: World choropleth map by AI Usage Index | -- |
| doc04-V06 | 17 | chart-complex | Hard | Figure 2.4: Income vs AUI scatter plot, log scale | -- |
| doc04-V07 | 19 | chart-simple | Easy | Figure 2.5: Top 30 US states horizontal bar chart | -- |
| doc04-V08 | 20 | chart-complex | Hard | Figure 2.6: US choropleth map by per-capita usage | -- |
| doc04-V09 | 22 | chart-complex | Hard | Figure 2.7: 4-panel scatter plots by occupation group | -- |
| doc04-V10 | 23 | infographic | Medium | Figure 2.8: Overrepresented clusters (US, Brazil, Vietnam, India) | -- |
| doc04-V11 | 25 | infographic | Medium | Figure 2.9: Overrepresented categories (CA, TX, FL, SC) | -- |
| doc04-V12 | 26 | infographic | Medium | Figure 2.10: DC highest Claude usage, 2-panel tasks/clusters | -- |
| doc04-V13 | 27 | chart-complex | Hard | Figure 2.11: Augmentation share vs AUI residuals scatter | -- |
| doc04-V14 | 32 | chart-simple | Easy | Figure 3.1: AI adoption rates line chart | -- |
| doc04-V15 | 33 | chart-simple | Medium | Figure 3.2: Horizontal stacked bar, taxonomy of usage | -- |
| doc04-V16 | 34 | chart-complex | Medium | Figure 3.3: Grouped horizontal bars, Claude.ai vs API | -- |
| doc04-V17 | 35 | chart-complex | Hard | Figure 3.4: 2-panel Lorenz curves + power-law rank chart | -- |
| doc04-V18 | 37 | chart-complex | Hard | Figure 3.5: 2-panel scatter, automation vs augmentation | -- |
| doc04-V19 | 39 | chart-simple | Easy | Figure 3.6: Average output token index bar chart | -- |
| doc04-V20 | 40 | chart-complex | Hard | Figure 3.7: Output vs input token scatter with regression | -- |
| doc04-V21 | 42 | chart-complex | Medium | Figure 3.8: API cost vs usage share scatter | -- |
| doc04-V22 | 43 | chart-complex | Hard | Figure 3.9: Partial regression scatter, cost vs usage | -- |

**Taggable:** 22 (5 easy, 6 medium, 11 hard)

<br><br>

## Doc 05 -- 05_gemini_multimodal_report.pdf

PDF, 90 pages, multi-image
Source: https://arxiv.org/pdf/2312.11805v5.pdf

### Raster

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc05-R01 | 1 | decorative | 3810x512 | -- | Thin decorative bar | Yes: decorative |
| doc05-R02 | 3 | screenshot | 4760x3421 | Hard | Figure 1: Handwritten physics problem with model verification | -- |
| doc05-R03 | 4 | diagram | 1383x617 | Medium | Figure 2: Gemini model family architecture, Transformer decoder | -- |
| doc05-R04 | 15 | screenshot | 4760x5014 | Hard | Figure 5: Multimodal matplotlib code gen composite | -- |
| doc05-R05 | 17 | decorative | 20x397 | -- | Thin gradient element | Yes: decorative |
| doc05-R06 | 19 | photo | 4080x3072 | Easy | Table 13 image 1: Cooking omelet in pan | -- |
| doc05-R07 | 19 | photo | 3069x3021 | Easy | Table 13 image 2: Omelet partially cooked | -- |
| doc05-R08 | 19 | photo | 4080x3072 | Easy | Table 13 image 3: Finished omelet on plate | -- |
| doc05-R09 | 21 | decorative | 560x560 | -- | Small icon within Figure 7 | Yes: decorative |
| doc05-R10 | 21 | decorative | -- | -- | Nested icon inside FORM | Yes: decorative |
| doc05-R11 | 78 | photo | 1170x1560 | Easy | Figure 11: Persian shield plant | -- |
| doc05-R12 | 79 | photo | 256x256 | Easy | Figure 12 image 1: Goldendoodle at beach | -- |
| doc05-R13 | 79 | photo | 256x256 | Easy | Figure 12 image 2: Goldendoodle in city | -- |
| doc05-R14 | 79 | photo | 256x256 | Easy | Figure 12 image 3: Goldendoodle portrait | -- |
| doc05-R15 | 80 | photo | 4080x3072 | Medium | Figure 13: Handwritten shapes sequence puzzle | -- |
| doc05-R16 | 81 | diagram | 539x158 | Easy | Figure 14: Parallelogram with dimensions | -- |
| doc05-R17 | 81 | photo | 514x510 | Medium | Figure 15 image 1: Moon photograph | -- |
| doc05-R18 | 81 | photo | 672x370 | Medium | Figure 15 image 2: Golf balls on lunar surface | -- |
| doc05-R19 | 82 | photo | 2072x1560 | Easy | Figure 16: NYC street at night | -- |
| doc05-R20 | 83 | other | 1521x2046 | Medium | Figure 17: Internet meme ("Game at 300 FPS / 75 Hz Monitor") | -- |
| doc05-R21 | 84 | diagram | 493x512 | Medium | Figure 18: Chinese family tree diagram | -- |
| doc05-R22 | 86 | screenshot | 512x271 | Medium | Figure 19: Rendered "Opossum Search" website | -- |
| doc05-R23 | 89 | chart-complex | 512x506 | Hard | Figure 22 image 1: 4 matplotlib subplots | -- |
| doc05-R24 | 89 | chart-simple | 512x327 | Easy | Figure 22 image 2: Rendered exponential curve | -- |
| doc05-R25 | 90 | photo | 480x270 | Easy | Figure 23 frame 1: Soccer penalty kick | -- |
| doc05-R26 | 90 | photo | 480x270 | Easy | Figure 23 frame 2: Soccer kick in progress | -- |
| doc05-R27 | 90 | photo | 480x270 | Easy | Figure 23 frame 3: Ball in flight | -- |
| doc05-R28 | 90 | photo | 480x270 | Easy | Figure 23 frame 4: Post-kick follow-through | -- |

### Vector

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc05-V01 | 9 | chart-simple | Easy | Figure 3: Grouped bar chart, language understanding | -- |
| doc05-V02 | 11 | chart-simple | Medium | Figure 4: Neg log likelihood vs token index | -- |
| doc05-V03 | 21 | diagram | Hard | Figure 7: Post-training data flywheel, SFT/RM/RL | -- |
| doc05-V04 | 23 | diagram | Medium | Figure 8: Gemini tool-use control loop | -- |
| doc05-V05 | 74 | chart-simple | Easy | Figure 9: CoT with uncertainty routing, GPT-4 vs Gemini | -- |
| doc05-V06 | 77 | infographic | Hard | Figure 10: Multimodal chart understanding + response | -- |
| doc05-V07 | 87 | other | Easy | Figure 20: Text-based calculus problem | -- |
| doc05-V08 | 88 | other | Medium | Figure 21: Multi-step math problem with table | -- |

**Taggable:** 31 (16 easy, 10 medium, 5 hard)

<br><br>

## Doc 06 -- 06_arxiv_2206_01062.pdf

PDF, 9 pages, multi-image
Source: https://arxiv.org/pdf/2206.01062.pdf

### Raster

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc06-R01 | 1 | screenshot | 271x459 | Medium | Figure 1 thumbnail 1: Document page with colored layout boxes | -- |
| doc06-R02 | 1 | decorative | 20x20 | -- | Small icon | Yes: too small |
| doc06-R03 | 1 | decorative | 20x20 | -- | Small icon | Yes: too small |
| doc06-R04 | 1 | screenshot | 140x189 | Medium | Figure 1 thumbnail 2: Annotated document page | -- |
| doc06-R05 | 1 | screenshot | 140x189 | Medium | Figure 1 thumbnail 3: Annotated document page | -- |
| doc06-R06 | 1 | screenshot | 170x166 | Medium | Figure 1 thumbnail 4: Annotated document page | -- |
| doc06-R07 | 4 | screenshot | 1120x1512 | Medium | Figure 3: CCS annotation UI with bounding boxes | -- |
| doc06-R08 | 4 | screenshot | 486x1528 | Medium | Annotated PDF pages column, layout categories | -- |
| doc06-R09 to R16 | 5 | screenshot | 1025x1025 | Medium | Figure 4: 8 document pages showing annotation alternatives | -- |
| doc06-D01 to D08 | 5 | decorative | 434x26 | -- | 8 thin separator bars | Yes: decorative |
| doc06-R17 to R22 | 9 | screenshot | 1025x1025 | Medium | Figure 6: 6 layout prediction examples | -- |

### Vector

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc06-V01 | 3 | chart-simple | Easy | Figure 2: Pie chart of DocLayNet page distribution | -- |
| doc06-V02 | 6 | chart-complex | Medium | Figure 5: mAP prediction performance, multi-series line | -- |

**Taggable:** 22 (2 easy, 20 medium) -- many near-identical document screenshots

<br><br>

## Doc 07 -- 07_epa_sample_letter.pdf

PDF, 3 pages, scanned
Source: https://19january2021snapshot.epa.gov/sites/static/files/2016-02/documents/epa_sample_letter_sent_to_commissioners_dated_february_29_2015.pdf

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc07-S01 | 1 | other | 1275x1650 | Easy | Full-page scan: EPA letterhead, typed text | Yes: OCR only |
| doc07-S02 | 2 | other | 1275x1650 | Easy | Full-page scan: letter continuation | Yes: OCR only |
| doc07-S03 | 3 | other | 1275x1650 | Easy | Full-page scan: closing and signature | Yes: OCR only |

**Taggable:** 0 (all skipped -- scanned text, no visual content)

<br><br>

## Doc 08 -- 08_xerox_mfp_scan_forestburg.pdf

PDF, 5 pages, scanned
Source: https://files.gabbart.com/1605/scanned_from_a_xerox_multifunction_printer.pdf

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc08-S01 | 1 | other | 2208x1728 | Medium | Full-page scan: employment form with fields, checkboxes, logo | Yes: OCR/form only |
| doc08-S02 | 2 | other | 2208x1728 | Medium | Full-page scan: employment history form with table structure | Yes: OCR/form only |
| doc08-S03 | 3 | other | 2208x1728 | Medium | Full-page scan: references and education tables | Yes: OCR/form only |
| doc08-S04 | 4 | other | 2208x1728 | Easy | Full-page scan: criminal history verification text | Yes: OCR only |
| doc08-S05 | 5 | other | 2208x1728 | Easy | Full-page scan: criminal history addendum | Yes: OCR only |

**Taggable:** 0 (all skipped -- scanned forms, no visual content)

<br><br>

## Doc 09 -- 09_archive_newspaper_1948.pdf

PDF, 6 pages, mixed-content
Source: https://archive.org/download/cupl_003575/cupl_003575_access.pdf

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc09-S01 | 1 | other | 5508x6845 | Hard | Front page: headlines, news photos, multi-column layout | Yes: no separate crops |
| doc09-S02 | 2 | other | 5484x6832 | Hard | Society/ads with Safeway ad illustrations | Yes: no separate crops |
| doc09-S03 | 3 | other | 5484x6832 | Hard | News page with portrait, service directory | Yes: no separate crops |
| doc09-S04 | 4 | other | 5485x6823 | Hard | Editorial/comics page with marching photo, comic strips, crossword | Yes: no separate crops |
| doc09-S05 | 5 | other | 5485x6823 | Hard | Sports/ads page with portrait, theater listings | Yes: no separate crops |
| doc09-S06 | 6 | other | 5484x6817 | Hard | Classified ads, dense multi-column | Yes: no separate crops |

**Taggable:** 0 (photos/illustrations within full-page scans, not individually extractable)

<br><br>

## Doc 10 -- 10_medrxiv_llama4_benchmark.docx

DOCX, text-only
Source: https://www.medrxiv.org/content/medrxiv/early/2025/10/07/2025.10.05.25337350/DC1/embed/media-1.docx?download=true

No images. 4 native text tables (specialty mapping, t-test results, prompting
effects, supplementary statistics).

**Taggable:** 0

<br><br>

## Doc 11 -- 11_policy_gradient_rl_lecture.pptx

PPTX, 80 slides, multi-image
Source: https://www.cs.princeton.edu/courses/archive/spring17/cos598F/lectures/RL.pptx

### Algorithm Pseudocode

| ID | Slide | Content Type | Size | Difficulty | Description | Skip? |
|----|-------|-------------|------|------------|-------------|-------|
| doc11-R01 | 36 | screenshot | 784x307 | Medium | Tabular TD(0) pseudocode: initialize V(s), episode loop | -- |
| doc11-R02 | 39 | screenshot | 744x301 | Medium | Sarsa on-policy TD control: Q(S,A) update | -- |
| doc11-R03 | 41 | screenshot | 767x277 | Medium | Q-learning off-policy TD: max_a Q(S',a) update | -- |
| doc11-R04 | 48 | screenshot | 699x356 | Hard | DQN loss function and gradient from Mnih et al. | -- |
| doc11-R05 | 49 | screenshot | 717x362 | Hard | Deep Q-learning with Experience Replay, full algorithm | -- |
| doc11-R06 | 60 | screenshot | 753x265 | Medium | REINFORCE Monte-Carlo policy gradient pseudocode | -- |
| doc11-R07 | 63 | screenshot | 753x477 | Medium | One-step Actor-Critic pseudocode | -- |
| doc11-R08 | 72 | screenshot | 470x441 | Hard | Asynchronous one-step Q-learning (A3C paper) | -- |
| doc11-R09 | 76 | screenshot | 797x578 | Hard | Asynchronous n-step Q-learning (A3C supplementary) | -- |
| doc11-R10 | 79 | screenshot | 803x482 | Hard | Asynchronous advantage actor-critic (A3C) | -- |

### Equations

| ID | Slide | Content Type | Size | Difficulty | Description | Skip? |
|----|-------|-------------|------|------------|-------------|-------|
| doc11-R11 | 55 | equation | 246x70 | Easy | Softmax policy parameterization pi(a|s,theta) | -- |
| doc11-R12 | 58 | equation | 336x72 | Easy | REINFORCE update rule theta_{t+1} | -- |
| doc11-R13 | 62 | equation | 567x131 | Medium | Actor-critic update with baseline, two-line | -- |
| doc11-R14 | 78 | equation | 941x78 | Medium | Generalized advantage estimate | -- |

### Decorative

| ID | Slides | Description | Skip? |
|----|--------|-------------|-------|
| doc11-D01 to D12 | 21-34 | 12 white/blank separator bars | Yes: blank images |

**Taggable:** 14 (2 easy, 7 medium, 5 hard)

<br><br>

## Doc 12 -- 12_minnstate_fy2025_budget.pptx

PPTX, 17 slides, multi-image
Source: https://www.minnstate.edu/system/finance/budget/docs/fy2025-operating-budget-second-reading-june-2024-final.pptx

| ID | Slide | Content Type | Difficulty | Description | Skip? |
|----|-------|-------------|------------|-------------|-------|
| doc12-R01 | -- | decorative | -- | Minnesota State logo (small header) | Yes: decorative logo |
| doc12-R02 | -- | decorative | -- | Minnesota State "M" banner (large) | Yes: decorative logo |
| doc12-R03 | -- | table-image | Medium | Table 9: North Star Promise Program Projected Awards, FY2025 | -- |
| doc12-R04 | -- | decorative | -- | Minnesota State full logo (large) | Yes: decorative logo |

**Taggable:** 1 (1 medium)

<br><br>

## Doc 13 -- 13_artpro_table.webp

WebP, 1 page, table-image
Source: https://standupsurfshop.com.au/wp-content/uploads/2023/09/ARTPRO-Table.webp

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc13-R01 | table-image | Easy | Aircraft wing specification table: 6 models, 7 numeric columns, alternating row shading | -- |

**Taggable:** 1 (1 easy)

<br><br>

## Doc 14 -- 14_simple_table.png

PNG, 1 page, table-image
Source: https://raw.githubusercontent.com/eihli/image-table-ocr/master/resources/test_data/simple.png

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc14-R01 | table-image | Easy | Simple 3-column table (Cell, Format, Formula), 5 rows, clean gridlines | -- |

**Taggable:** 1 (1 easy)

<br><br>

## Doc 15 -- 15_timetable.jpg

JPG, 1 page, table-image
Source: https://courses.washington.edu/fish340/Images/timetable.jpg

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc15-R01 | table-image | Medium | SWORD Deadlines: 9-week schedule, 4 assignment types, color-coded cells | -- |

**Taggable:** 1 (1 medium)

<br><br>

## Doc 16 -- 16_cambridge_mitoball_biology.docx

DOCX, 6.8 MB, multi-image
Source: https://www.repository.cam.ac.uk/bitstreams/a5e95699-d0d4-49e1-a471-e7dc381cdbac/download

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc16-R01 | decorative | -- | TIFF logo/icon (11 KB) | Yes: decorative branding |
| doc16-R02 | photo | Hard | Figure 1: 9-sub-panel composite (A-I) -- spermatogenesis diagram, fluorescence microscopy, EM series, bar charts, time-lapse | -- |
| doc16-R03 | photo | Hard | Figure 2: 7-sub-panel composite (A-G) -- testis cross-section, EM, fluorescence grid, PolG1 dual stain | -- |
| doc16-R04 | photo | Hard | Figure 3: Genetic knockdown panels -- control vs mfn RNAi vs Drp1 KD | -- |
| doc16-R05 | photo | Hard | Figure 4: Mitoball ultrastructure -- fluorescence and EM at multiple stages | -- |
| doc16-R06 | photo | Hard | Figure 5: Cross-species fluorescence comparison with scale bars | -- |
| doc16-R07 | photo | Hard | Figure S1: Supplementary control/experimental fluorescence panels | -- |
| doc16-R08 | photo | Hard | Figure S2: Extended cross-species panel -- 8+ insect species | -- |
| doc16-R09 | photo | Hard | Figure S3: Cytoskeletal markers, control vs hts mutant | -- |

**Taggable:** 8 (8 hard)

<br><br>

## Doc 17 -- 17_arxiv_fractional_brownian_sde.pdf

PDF, 24 pages, text-heavy (equation-dense)
Source: https://arxiv.org/pdf/2306.08324.pdf

No embedded raster images. All 63 equations are native LaTeX. Equation regions
must be identified and cropped from rendered pages by the pipeline.

**Taggable:** 0 (equations are native LaTeX, not raster)

Note: If the pipeline extracts equation crops from page renders, each would
be medium-to-hard difficulty. Estimated 15-20 distinct equation regions.

<br><br>

## Doc 18 -- 18_ibm_microservices_redbook.pdf

PDF, 170 pages, multi-image
Source: https://www.redbooks.ibm.com/redbooks/pdfs/sg248275.pdf

| Image ID | Content Type | Difficulty | Description | Skip? |
|----------|-------------|------------|-------------|-------|
| doc18-F1-1 | diagram | Easy | Sample microservices application | -- |
| doc18-F1-2 | diagram | Easy | Monolithic multi-tiered architecture | -- |
| doc18-F1-3 | diagram | Medium | Microservices architecture (languages + data stores) | -- |
| doc18-F2-1 | diagram | Easy | "Old" style service design | -- |
| doc18-F2-2 | diagram | Medium | Microservices redesign | -- |
| doc18-F2-3 | diagram | Medium | Circuit breaker sequence diagram | -- |
| doc18-F2-4 | diagram | Medium | Bulkhead pattern (thread pool isolation) | -- |
| doc18-F2-5 | diagram | Easy | RESTful API calls | -- |
| doc18-F2-6 | diagram | Medium | API Gateway fronting microservices | -- |
| doc18-F2-7 | infographic | Medium | Hills Playback timeline | -- |
| doc18-F2-8 | diagram | Medium | REST architecture with caches | -- |
| doc18-F2-9 | diagram | Easy | Messaging use cases | -- |
| doc18-F2-10 | diagram | Easy | Event notification (stock price) | -- |
| doc18-F3-1 | infographic | Medium | DevOps continuous delivery | -- |
| doc18-F3-2 | infographic | Easy | Challenges with traditional delivery | -- |
| doc18-F3-3 | infographic | Hard | IBM DevOps framework | -- |
| doc18-F3-4 | diagram | Medium | Decentralized data store | -- |
| doc18-F3-5 | diagram | Medium | Microservices transformation | -- |
| doc18-F4-1 | screenshot | Easy | Bluemix service categories | -- |
| doc18-F4-3 | diagram | Medium | Deployment models (local, dedicated, public) | -- |
| doc18-F4-5 | diagram | Medium | Cloud integration flow | -- |
| doc18-F4-8 | infographic | Medium | ALM of microservices in Bluemix | -- |
| doc18-F4-9 | screenshot | Easy | Create app from Bluemix catalog | -- |
| doc18-F4-10 | screenshot | Medium | Create microservice in dashboard | -- |
| doc18-F4-12 | diagram | Medium | Multi-region delivery pipeline | -- |
| doc18-F4-13 | screenshot | Easy | Scaling options in Bluemix console | -- |
| doc18-F4-14 | screenshot | Easy | Load balance on Bluemix | -- |
| doc18-F4-16 | diagram | Easy | Application communication in Bluemix | -- |
| doc18-F5-1 | screenshot | Easy | DevOps Services starting point | -- |
| doc18-F5-2 | diagram | Hard | North Star Architecture (DevOps Services) | -- |
| doc18-F5-3 | diagram | Hard | Bluemix console architecture (pre-microservice) | -- |
| doc18-F5-5 | screenshot | Medium | Bluemix landing page UI composition | -- |
| doc18-F5-6 | diagram | Hard | Bluemix console microservice transformation | -- |
| doc18-F5-8 | diagram | Hard | Watson Developer Cloud platform (4-layer) | -- |
| doc18-F5-9 | diagram | Hard | IaaS++ architecture (multi-zone) | -- |
| doc18-F5-10 | screenshot | Easy | Watson services in Bluemix | -- |
| doc18-F5-11 | diagram | Medium | Service register and discovery | -- |
| doc18-F5-12 | diagram | Medium | Watson service onboarding | -- |
| doc18-F6-1 | screenshot | Easy | CloudTrader user interface | -- |
| doc18-F6-2 | diagram | Medium | CloudTrader components overview | -- |
| doc18-F6-4 | diagram | Medium | CloudTrader with externalized Quote | -- |
| doc18-F6-5 | screenshot | Medium | Code editing in DevOps Services | -- |
| doc18-F7-1 | screenshot | Medium | Online Store sample | -- |
| doc18-F7-2 | screenshot | Medium | Monitoring: performance | -- |
| doc18-F7-3 | screenshot | Medium | Monitoring: availability | -- |
| doc18-F8-1 | diagram | Easy | Acme Air monolithic architecture | -- |
| doc18-F8-4 | screenshot | Easy | Acme Air web app in Bluemix | -- |
| doc18-F8-11 | screenshot | Easy | Acme Air home page | -- |
| doc18-F8-12 | diagram | Medium | Acme Air microservices architecture | -- |
| doc18-F8-16 | screenshot | Easy | Hystrix Dashboard home | -- |
| doc18-F8-17 | screenshot | Medium | Hystrix Dashboard (streams) | -- |
| doc18-F8-18 | screenshot | Medium | Bluemix dashboard: Acme Air components | -- |

**Taggable:** ~52 (18 easy, 22 medium, 6 hard; excludes some minor duplicate figures)

<br><br>

## Doc 19 -- 19_cris_electronic_screens_2023.docx

DOCX, 1.3 MB, multi-image
Source: https://www.energyrating.gov.au/sites/default/files/2023-06/Cost%20Recovery%20Impact%20Statement%20-%20Electronic%20Screens%20-%202023.docx

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc19-R01 | chart-simple | Easy | Pie chart: equipment market share (5 segments) | -- |
| doc19-R02 | photo | Medium | Airport departure hall with display screens | -- |
| doc19-R03 | photo | Easy | Changi Airport digital signage kiosk | -- |
| doc19-R04 | chart-simple | Easy | Stacked area chart: EU energy use 1990-2030 | -- |
| doc19-R05 | chart-complex | Medium | Scatter/strip chart: energy ratings data | -- |
| doc19-R06 | chart-complex | Medium | Multi-line chart: power vs screen area (9 lines) | -- |
| doc19-R07 | chart-complex | Hard | Multi-line chart: max power vs area (11 lines, annotated) | -- |
| doc19-R08 | chart-simple | Easy | Bar chart: star rating distribution (12 bars) | -- |
| doc19-R09 | infographic | Easy | Energy rating label: Super Efficiency (199 kWh) | -- |
| doc19-R10 | infographic | Easy | Energy rating label: Standard (485 kWh) | -- |
| -- | decorative | -- | 4 logos + 3 spacers + 1 divider | Yes: decorative/spacer |

**Taggable:** 10 (6 easy, 3 medium, 1 hard)

<br><br>

## Doc 20 -- 20_illinois_workforce_dashboard.xlsx

XLSX, 99 KB, multi-image
Source: https://www.illinoisworknet.com/WIOA/Resources/Documents/6.%20Dashboard%20for%20the%20Local%20Workforce%20Board%20-%20TEMPLATE.xlsx

Chart objects are XML-defined (not raster). 5 unique charts on Sheet 2,
duplicated on Sheet 3 (charts 6-10 mirror charts 1-5). Only unique charts
are cataloged.

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc20-C01 | chart-complex | Medium | Grouped bar: Obligations, Accrual & Expense Breakdown (12 series, 4 categories: Required/Adult/DW/Youth) | -- |
| doc20-C02 | chart-complex | Medium | Grouped bar: Obligations (5 series, 3 categories: Adult/DW/Youth) | -- |
| doc20-C03 | chart-simple | Easy | Pie: Total WIOA Formula Grant Budget (5 segments: Admin/Youth In School/Out of School/Adult/DW) | -- |
| doc20-C04 | chart-simple | Easy | Grouped bar: Direct Training (4 series, 3 categories: Adult/DW/Combined) | -- |
| doc20-C05 | chart-simple | Easy | Grouped bar: Youth Work Based Learning (4 series, 1 category) | -- |
| -- | -- | -- | Charts 6-10 duplicate charts 1-5 on Sheet 3 | Yes: duplicates |

**Taggable:** 5 (3 easy, 2 medium)

<br><br>

## Doc 21 -- 21_praxie_project_portfolio.xlsx

XLSX, 58 KB, multi-image
Source: https://praxie.com/wp-content/uploads/2021/08/Project-Portfolio-Management-Template.xlsx

4 single-series bar charts summarizing project portfolio metrics. 1 raster
logo (decorative).

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc21-C01 | chart-simple | Easy | Bar: Priority distribution (3 bars: Low/Medium/High) | -- |
| doc21-C02 | chart-simple | Easy | Bar: Status distribution (3 bars: Completed/In Progress/Not Started) | -- |
| doc21-C03 | chart-simple | Easy | Bar: Risk distribution (3 bars: Low/Medium/High Risk) | -- |
| doc21-C04 | chart-simple | Easy | Bar: Budget summary (2 bars: Budget vs Actual Expenditure) | -- |
| -- | decorative | -- | Praxie logo (8.5 KB JPEG) | Yes: decorative logo |

**Taggable:** 4 (4 easy)

<br><br>

## Doc 22 -- 22_nasa_global_warming.html

HTML, 351 KB, multi-image
Source: https://science.nasa.gov/earth/climate-change/global-warming/

20 content images inline within `<figure>` tags. ~35 navigation thumbnails
for unrelated articles in header/sidebar. All images are remote-hosted
(NASA CDN URLs, not embedded). No captions in `<figcaption>` elements.

### Charts

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc22-R01 | chart-complex | Medium | GISS temperature anomaly: global surface temperature 1880-present, baseline comparison | -- |
| doc22-R02 | chart-complex | Medium | Greenhouse gas concentrations 1750-2008: dual-axis CO2 + methane trends | -- |
| doc22-R03 | chart-complex | Hard | EPICA 800,000-year temperature + CO2 reconstruction from ice cores | -- |
| doc22-R04 | chart-complex | Medium | Proxy-based temperature reconstruction: 1000-year history, multiple proxy series | -- |
| doc22-R05 | chart-complex | Hard | Anthropogenic vs natural climate contribution: multi-factor attribution comparison | -- |
| doc22-R06 | chart-simple | Easy | ACRIM total solar irradiance: daily + monthly measurements since 1979 | -- |
| doc22-R07 | chart-complex | Medium | MSU troposphere/stratosphere temperature trends 1978-2010 | -- |
| doc22-R08 | chart-complex | Medium | IPCC future warming scenarios: multiple emission pathways | -- |
| doc22-R09 | chart-simple | Easy | Ocean carbon cycle diagram | -- |
| doc22-R10 | chart-complex | Medium | IPCC precipitation change projections: global map | -- |
| doc22-R11 | chart-simple | Easy | Sea level rise: multi-dataset composite trend | -- |

### Photos

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc22-R12 | photo | Easy | ISS022-E-6674: Earth from space, thin atmosphere layer visible | -- |
| doc22-R13 | photo | Easy | Glacial ice core cross-section | -- |
| doc22-R14 | photo | Medium | Climate monitoring equipment: ground station and satellite composite | -- |
| doc22-R15 | photo | Medium | Solar corona comparison: solar maximum vs minimum (side-by-side) | -- |
| doc22-R16 | photo | Easy | Athabasca Glacier retreat | -- |
| doc22-R17 | photo | Easy | ISS STS-131 Earth observation | -- |
| doc22-R18 | photo | Medium | GOES East hurricane satellite image | -- |
| doc22-R19 | photo | Easy | Lake Powell bathtub ring: drought impact | -- |
| doc22-R20 | photo | Easy | Massachusetts nor'easter 2007: coastal storm impact | -- |
| -- | decorative | -- | ~35 navigation thumbnails + 4 footer/sidebar images | Yes: navigation/branding |

**Taggable:** 20 (8 easy, 8 medium, 2 hard)

<br><br>

## Doc 23 -- 23_nvie_git_branching_model.html

HTML, 31 KB, multi-image
Source: https://nvie.com/posts/a-successful-git-branching-model/

6 git flow diagrams inline as `<img>` tags with relative paths. Clean
layout with minimal decorative content (1 author avatar, 1 PDF icon).

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc23-R01 | diagram | Medium | Complete git-flow branching model: feature, release, hotfix branches with merge topology | -- |
| doc23-R02 | diagram | Easy | Centralized/decentralized repository setup: origin + developer nodes | -- |
| doc23-R03 | diagram | Easy | Main branches: master and develop parallel tracks | -- |
| doc23-R04 | diagram | Easy | Feature branch create-and-merge workflow | -- |
| doc23-R05 | diagram | Easy | Merge comparison: fast-forward vs no-ff commit graph | -- |
| doc23-R06 | diagram | Easy | Hotfix branch: emergency release workflow | -- |
| -- | decorative | -- | Author avatar + PDF download icon | Yes: decorative |

**Taggable:** 6 (5 easy, 1 medium)

<br><br>

## Doc 24 -- 24_fowler_microservices.html

HTML, 84 KB, multi-image
Source: https://martinfowler.com/articles/microservices.html

6 architecture and organization diagrams. 8 decorative elements (site
logo, author photos, book cover, thumbnails, footer branding).

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc24-R01 | diagram | Medium | Monolith vs microservices: side-by-side architecture comparison | -- |
| doc24-R02 | diagram | Medium | Conway's Law: org structure mapped to system architecture | -- |
| doc24-R03 | diagram | Easy | Functional staff organization: cross-functional team boundaries | -- |
| doc24-R04 | diagram | Medium | Decentralized data management: per-service database pattern | -- |
| doc24-R05 | diagram | Easy | Basic deployment pipeline: build-test-deploy flow | -- |
| doc24-R06 | diagram | Medium | Micro-deployment: monolith vs microservices infrastructure comparison | -- |
| -- | decorative | -- | Site logo, 2 author photos, book cover, 2 thumbnails, footer logo | Yes: decorative/branding |

**Taggable:** 6 (2 easy, 4 medium)

<br><br>

## Corpus Summary

| Category | Docs | Content images | Decorative | Vector figures | Tables |
|----------|------|---------------|------------|----------------|--------|
| multi-image | 02, 05, 06, 11, 12, 16, 18, 19, 20, 21, 22, 23, 24 | 162 | 81 | 12 | 24 |
| vector-heavy | 01, 04 | 1 | 2 | 34 | 3 |
| text-heavy | 00, 03, 17 | 1 | 4 | 0 | 4 |
| scanned | 07, 08 | 8 | 0 | 0 | 0 |
| mixed-content | 09 | 6 | 0 | 0 | 0 |
| text-only | 10 | 0 | 0 | 0 | 4 |
| table-image | 13, 14, 15 | 3 | 0 | 0 | 0 |
| **Total** | **25** | **181** | **87** | **46** | **35** |

<br><br>

## Gap Tracker

| Gap | Status | Notes |
|-----|--------|-------|
| Table-as-image | Covered | 5 examples across 5 docs (00, 12-15) |
| Equations | Covered | 4 raster (Doc 11) + 63 native LaTeX (Doc 17) |
| Diagrams | Covered | 36 total; Doc 18 adds ~27 architecture diagrams |
| Photos (non-scanned) | Improved | Docs 05, 16, 19 span consumer, scientific, and environmental |
| DOCX with images | Covered | Docs 16, 19 provide scientific photos + charts |
| Chart-simple raster | Covered | Docs 02, 05 have raster charts |
| Algorithm pseudocode | Covered | Doc 11 has 10 algorithm screenshots |
| Scanned documents | Covered | Docs 07-09 cover letter, form, newspaper |
| XLSX with charts | Covered | Docs 20, 21 provide XML-defined chart objects (bar, pie) |
| HTML with images | Covered | Doc 22 provides 20 inline images (charts + photos) from NASA |
| Infographics | Open | 16 total concentrated in 3 docs; add slide decks or consulting reports |

<br><br>

## Distribution Summary

### By difficulty (taggable content images only)

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 79 | 33% |
| Medium | 100 | 42% |
| Hard | 49 | 21% |
| **Total** | **230** | **100%** |

### By content type (taggable only)

| Content Type | Easy | Medium | Hard | Total |
|-------------|------|--------|------|-------|
| chart-simple | 22 | 3 | 0 | 25 |
| chart-complex | 0 | 21 | 16 | 37 |
| diagram | 19 | 22 | 7 | 48 |
| table-image | 2 | 3 | 0 | 5 |
| equation | 2 | 2 | 0 | 4 |
| infographic | 3 | 7 | 6 | 16 |
| photo | 21 | 7 | 8 | 36 |
| screenshot | 11 | 28 | 2 | 41 |
| other | 0 | 5 | 2 | 7 |
| **Total** | **79** | **100** | **49** | **230** |

Note: Doc 06 contributes 20 medium-difficulty screenshots that are mostly
near-identical. For evaluation, only 2-3 representative examples are included.

Format-level coverage matrices and gap analysis are maintained in the
dedicated test set files:
- [Pipeline Test Set](./evaluation/pipeline-test-set.md) -- document-level
  format coverage matrix and extraction gaps
- [Annotation Test Set](./evaluation/annotation-test-set.md) -- image-level
  format coverage matrix and annotation gaps

### By document

| Doc | Easy | Medium | Hard | Total | Format |
|-----|------|--------|------|-------|--------|
| 00 | 0 | 1 | 0 | 1 | PDF |
| 01 | 2 | 5 | 6 | 13 | PDF |
| 02 | 7 | 9 | 2 | 18 | PDF |
| 03 | 0 | 0 | 0 | 0 | PDF |
| 04 | 5 | 6 | 11 | 22 | PDF |
| 05 | 16 | 10 | 5 | 31 | PDF |
| 06 | 2 | 20 | 0 | 22 | PDF |
| 07 | 0 | 0 | 0 | 0 | PDF (scanned) |
| 08 | 0 | 0 | 0 | 0 | PDF (scanned) |
| 09 | 0 | 0 | 0 | 0 | PDF (scanned) |
| 10 | 0 | 0 | 0 | 0 | DOCX |
| 11 | 2 | 7 | 5 | 14 | PPTX |
| 12 | 0 | 1 | 0 | 1 | PPTX |
| 13 | 1 | 0 | 0 | 1 | WebP |
| 14 | 1 | 0 | 0 | 1 | PNG |
| 15 | 0 | 1 | 0 | 1 | JPG |
| 16 | 0 | 0 | 8 | 8 | DOCX |
| 17 | 0 | 0 | 0 | 0 | PDF (equations) |
| 18 | 18 | 22 | 6 | 46 | PDF |
| 19 | 5 | 4 | 1 | 10 | DOCX |
| **Total** | **57** | **85** | **47** | **189** | |

<br><br>

## Evaluation Subset

### Selection criteria

- Target: 40-60 images
- Over-represent medium and hard (these differentiate models)
- At least 2 per content type
- At least 5 documents represented
- Exclude decorative, blank, and scanned-text-only images
- For Doc 06, include only 2-3 representative screenshots (not all 20)
- Prefer diverse content over repetitive examples from the same figure

### Selected subset (64 images)

| ID | Doc | Page | Content Type | Difficulty | Description |
|----|-----|------|-------------|------------|-------------|
| doc00-R03 | 00 | 5 | table-image | Medium | Benchmark comparison table |
| doc01-R01 | 01 | 58 | chart-complex | Medium | IF evaluation heatmap, 3x3 color grid |
| doc01-V01 | 01 | 8 | infographic | Hard | 3-column harmful content comparison, 7 pairs |
| doc01-V04 | 01 | 11 | infographic | Hard | Disinformation examples, 3-column layout |
| doc01-V07 | 01 | 17 | infographic | Hard | Tool-augmented risky task, chain-of-thought |
| doc01-V09 | 01 | 23 | chart-simple | Easy | Bar chart of incorrect behavior rate |
| doc01-V12 | 01 | 28 | infographic | Hard | Jailbreaks for GPT-4-launch |
| doc02-R01 | 02 | 6 | chart-complex | Medium | Gridworld MSE with 6 method lines |
| doc02-R08 | 02 | 7 | chart-simple | Easy | Hopper MSE grouped bar chart |
| doc02-R10 | 02 | 7 | chart-complex | Hard | 3-panel vertical training curves |
| doc02-R11 | 02 | 16 | chart-simple | Easy | Policy and Reward line chart (386x252) |
| doc02-R16 | 02 | 19 | chart-complex | Hard | 3-panel stacked chart (NLL, MSE, Value) |
| doc02-V01 | 02 | 5 | diagram | Easy | SinglePath MDP state diagram |
| doc04-V01 | 04 | 8 | chart-complex | Hard | 8-panel grid of line charts |
| doc04-V03 | 04 | 13 | chart-simple | Easy | Top 20 countries horizontal bar chart |
| doc04-V05 | 04 | 15 | chart-complex | Hard | World choropleth map by AI Usage Index |
| doc04-V06 | 04 | 17 | chart-complex | Hard | Income vs AUI scatter plot, log scale |
| doc04-V09 | 04 | 22 | chart-complex | Hard | 4-panel scatter plots by occupation |
| doc04-V10 | 04 | 23 | infographic | Medium | Overrepresented request clusters, 4 panels |
| doc04-V17 | 04 | 35 | chart-complex | Hard | 2-panel Lorenz curves + power-law |
| doc04-V18 | 04 | 37 | chart-complex | Hard | 2-panel scatter, automation vs augmentation |
| doc04-V22 | 04 | 43 | chart-complex | Hard | Partial regression scatter plot |
| doc05-R02 | 05 | 3 | screenshot | Hard | Handwritten physics problem + model response |
| doc05-R03 | 05 | 4 | diagram | Medium | Gemini architecture overview |
| doc05-R04 | 05 | 15 | screenshot | Hard | Multimodal matplotlib code gen composite |
| doc05-R06 | 05 | 19 | photo | Easy | Cooking omelet in pan |
| doc05-R11 | 05 | 78 | photo | Easy | Persian shield plant |
| doc05-R15 | 05 | 80 | photo | Medium | Handwritten shapes sequence puzzle |
| doc05-R17 | 05 | 81 | photo | Medium | Moon photograph (puzzle input) |
| doc05-R19 | 05 | 82 | photo | Easy | NYC street at night |
| doc05-R20 | 05 | 83 | other | Medium | Internet meme (humor understanding) |
| doc05-R21 | 05 | 84 | diagram | Medium | Chinese family tree diagram |
| doc05-R23 | 05 | 89 | chart-complex | Hard | 4 matplotlib subplots (sin, 3D surface, contour) |
| doc05-V03 | 05 | 21 | diagram | Hard | Post-training data flywheel flow diagram |
| doc05-V04 | 05 | 23 | diagram | Medium | Gemini tool-use control loop |
| doc05-V06 | 05 | 77 | infographic | Hard | Multimodal chart understanding + response |
| doc06-R07 | 06 | 4 | screenshot | Medium | CCS annotation UI with bounding boxes |
| doc06-R09 | 06 | 5 | screenshot | Medium | Figure 4 example (representative of 8) |
| doc06-R17 | 06 | 9 | screenshot | Medium | Figure 6 example (representative of 6) |
| doc06-V01 | 06 | 3 | chart-simple | Easy | Pie chart of DocLayNet distribution |
| doc11-R01 | 11 | 36 | screenshot | Medium | Tabular TD(0) pseudocode |
| doc11-R04 | 11 | 48 | screenshot | Hard | DQN loss function and gradient |
| doc11-R05 | 11 | 49 | screenshot | Hard | Deep Q-learning with Experience Replay |
| doc11-R10 | 11 | 79 | screenshot | Hard | A3C actor-critic pseudocode |
| doc11-R11 | 11 | 55 | equation | Easy | Softmax policy parameterization |
| doc11-R13 | 11 | 62 | equation | Medium | Actor-critic update with baseline |
| doc12-R03 | 12 | -- | table-image | Medium | North Star Promise Program financial table |
| doc13-R01 | 13 | 1 | table-image | Easy | Aircraft wing specification table |
| doc14-R01 | 14 | 1 | table-image | Easy | Spreadsheet cell/format/formula table |
| doc15-R01 | 15 | 1 | table-image | Medium | Color-coded course timetable |
| doc16-R02 | 16 | -- | photo | Hard | 9-sub-panel composite: spermatogenesis + microscopy + charts |
| doc16-R03 | 16 | -- | photo | Hard | 7-sub-panel composite: testis + EM + fluorescence |
| doc16-R05 | 16 | -- | photo | Hard | Mitoball ultrastructure at multiple stages |
| doc16-R08 | 16 | -- | photo | Hard | Cross-species comparison (8+ insect species) |
| doc18-F1-3 | 18 | 10 | diagram | Medium | Microservices architecture |
| doc18-F2-3 | 18 | -- | diagram | Medium | Circuit breaker sequence diagram |
| doc18-F5-2 | 18 | 94 | diagram | Hard | North Star Architecture (DevOps Services) |
| doc18-F5-8 | 18 | 104 | diagram | Hard | Watson Developer Cloud platform (4-layer) |
| doc18-F5-9 | 18 | 105 | diagram | Hard | IaaS++ architecture (multi-zone) |
| doc18-F3-3 | 18 | -- | infographic | Hard | IBM DevOps framework |
| doc19-R01 | 19 | -- | chart-simple | Easy | Pie chart: equipment market share |
| doc19-R06 | 19 | -- | chart-complex | Medium | Multi-line chart: power vs screen area (9 lines) |
| doc19-R07 | 19 | -- | chart-complex | Hard | Multi-line chart: max power vs area (11 lines, annotated) |
| doc19-R09 | 19 | -- | infographic | Easy | Energy rating label: Super Efficiency |

### Subset statistics

**Total:** 64 images from 14 of 20 documents

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 14 | 22% |
| Medium | 20 | 31% |
| Hard | 30 | 47% |

| Content Type | Count |
|-------------|-------|
| chart-simple | 6 |
| chart-complex | 14 |
| diagram | 10 |
| table-image | 5 |
| equation | 2 |
| infographic | 8 |
| photo | 9 |
| screenshot | 9 |
| other | 1 |

The subset over-represents hard images (47% vs 25% in corpus) as intended.
Medium and hard together comprise 78%. All content types have at least 1
example. Doc 17 equations are not in the subset (native LaTeX, not raster)
but test equation region detection during pipeline evaluation.

For detailed breakdowns by content type, source format, and coverage gaps,
see the [Annotation Test Set](./evaluation/annotation-test-set.md).

# Image Catalog

Master catalog of all images, figures, charts, and diagrams across the
evaluation fixture set. Includes difficulty ratings and evaluation subset
selection.

> **Related:** [Pipeline Test Set](./evaluation/pipeline-test-set.md)
> (document-level extraction testing) |
> [Annotation Test Set](./evaluation/annotation-test-set.md) (image-level
> annotation evaluation) |
> [Image Analysis](./evaluation/image-analysis/) (per-image ground truth)

**Documents cataloged:** 31
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

## Doc 25 -- 25_va_tiu_clinical_manual.docx

DOCX, 1.8 MB, multi-image
Source: https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiutm.docx

19 raster images from a VA clinical software manual (CPRS Text Integration
Utility). Mix of full-window screenshots, dialog boxes, toolbar captures,
and small icons. Images range from 2.8 KB icons to 270 KB full screenshots.

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc25-R01 | screenshot | Medium | Application window: main CPRS interface (500x500) | -- |
| doc25-R02 | screenshot | Medium | Application window: clinical record view (912x651) | -- |
| doc25-R05 | screenshot | Easy | Dialog or form view (710x501) | -- |
| doc25-R06 | screenshot | Medium | UI panel: clinical data entry (772x421) | -- |
| doc25-R07 | screenshot | Medium | UI panel: form layout (912x586) | -- |
| doc25-R08 | screenshot | Medium | UI panel: record display (1055x742) | -- |
| doc25-R09 | screenshot | Medium | UI panel: data view (986x724) | -- |
| doc25-R10 | screenshot | Medium | Wide panel: clinical workflow (1280x560) | -- |
| doc25-R11 | screenshot | Medium | Dialog: configuration or settings (880x594) | -- |
| doc25-R12 | screenshot | Medium | Dialog: data entry form (992x760) | -- |
| doc25-R13 | screenshot | Easy | Small dialog: option panel (752x383) | -- |
| doc25-R14 | screenshot | Easy | Small dialog: selection panel (800x408) | -- |
| doc25-R18 | screenshot | Easy | Toolbar or menu capture (529x166) | -- |
| doc25-R19 | screenshot | Medium | Full form: clinical documentation (686x851) | -- |
| -- | decorative | -- | 5 small icons/buttons (<10 KB each): image3, image4, image15, image16, image17 | Yes: UI icons |

**Taggable:** 14 (4 easy, 10 medium)

<br><br>

## Doc 26 -- 26_concordia_coen6501_digital_logic.pptx

PPTX, 62 slides, 1.5 MB, multi-image
Source: https://users.encs.concordia.ca/~asim/COEN_6501/Lecture_Notes/Lecture_1_Slides.pptx

Computer engineering lecture on digital logic design (Concordia University
COEN 6501). 23 media files (15 PNG/JPEG raster + 8 WMF vector metafiles),
22 image references across 15 of 62 slides. Slide 13 is dense (7 circuit
diagrams). Remaining content slides have full-slide-sized schematics and
logic diagrams. No decorative elements in slide masters.

| ID | Slide | Content Type | Size | Difficulty | Description | Skip? |
|----|-------|-------------|------|------------|-------------|-------|
| doc26-R01 | 13 | diagram | 2.2x1.1 in | Medium | Full adder circuit schematic | -- |
| doc26-R02 | 13 | diagram | 2.5x1.0 in | Medium | Ripple-carry adder layout | -- |
| doc26-R03 | 13 | diagram | 2.4x1.6 in | Medium | Half adder schematic | -- |
| doc26-R04 | 13 | diagram | 2.3x1.2 in | Medium | Circuit design scenario | -- |
| doc26-R05 | 13 | diagram | 1.3x2.0 in | Easy | Logic gate layout (scenario_2b) | -- |
| doc26-R06 | 13 | diagram | 1.9x1.7 in | Easy | Inverter circuit (inv1) | -- |
| doc26-R07 | 13 | diagram | 2.8x1.1 in | Easy | Inverter circuit (inv2) | -- |
| doc26-R08 | 19 | diagram | 8.5x6.2 in | Medium | Full-slide digital logic diagram | -- |
| doc26-R09 | 21 | diagram | 8.5x4.3 in | Medium | Full-slide circuit schematic | -- |
| doc26-R10 | 23 | diagram | 8.5x6.6 in | Medium | Full-slide digital design diagram | -- |
| doc26-R11 | 24 | diagram | 8.5x7.4 in | Medium | Full-slide logic diagram | -- |
| doc26-R12 | 27 | diagram | 7.8x7.1 in | Medium | Full-slide circuit diagram | -- |
| doc26-R13 | 30 | diagram | 10.0x4.6 in | Medium | Wide-format circuit schematic | -- |
| doc26-R14 | 33 | diagram | 8.2x6.1 in | Medium | Full-slide digital design | -- |
| doc26-R15 | 34 | diagram | 8.9x6.4 in | Medium | Full-slide circuit layout | -- |
| doc26-R16 | 35 | diagram | 9.8x6.3 in | Medium | Full-slide digital schematic | -- |
| doc26-R17 | 36 | diagram | 6.5x4.1 in | Medium | Circuit comparison (left panel) | -- |
| doc26-R18 | 36 | diagram | 6.5x4.2 in | Medium | Circuit comparison (right panel) | -- |
| doc26-R19 | 58 | diagram | 8.5x7.8 in | Medium | Full-slide logic design | -- |
| doc26-R20 | 59 | diagram | 8.5x9.0 in | Medium | Full-slide circuit schematic | -- |
| doc26-R21 | 60 | diagram | 8.5x4.5 in | Medium | Full-slide digital design | -- |
| doc26-R22 | 61 | diagram | 2.1x4.5 in | Easy | Narrow circuit detail | -- |

Note: Descriptions are based on structural metadata (`descr` attributes and
slide positions). Detailed content-type classification pending visual
inspection during pass 2. 8 WMF vector metafiles in ppt/media/ may contain
equations or small circuit symbols not captured by the slide-level scan.

**Taggable:** 22 (4 easy, 18 medium)

<br><br>

## Doc 27 -- 27_era_annual_report_2023.pptx

PPTX, 32 slides, 1.9 MB, multi-image
Source: https://www.era-online.org/wp-content/uploads/2026/01/Slides-summarizing-AR2023_website.pptx

European Union Agency for Railways (ERA) 2023 annual report summary.
42 media files (41 PNG + 1 JPEG), 42 content image references across 31 of
32 slides. 4 decorative branding images in slide layouts. Document appears
to present the same data in two halves (slides 2-13 and 14-28 mirror layout
patterns), suggesting bilingual or year-over-year structure. Content includes
European rail network maps, horizontal bar/timeline charts, and paired
comparison panels.

| ID | Slide | Content Type | Dimensions | Difficulty | Description | Skip? |
|----|-------|-------------|------------|------------|-------------|-------|
| doc27-R01 | 2 | diagram | 1010x824 | Medium | European rail map (descr: "kaart, atlas, tekst") | -- |
| doc27-R02 | 3 | diagram | 1105x902 | Medium | European rail map (variant) | -- |
| doc27-R03 | 4 | chart-complex | 879x697 | Medium | Paired panel (left), medium format | -- |
| doc27-R04 | 4 | chart-complex | 802x875 | Medium | Paired panel (right), tall format | -- |
| doc27-R05 | 5 | chart-complex | 791x881 | Medium | Paired panel (left), tall format | -- |
| doc27-R06 | 5 | chart-complex | 792x945 | Medium | Paired panel (right), tall format | -- |
| doc27-R07 | 6 | chart-complex | 848x876 | Medium | Paired panel (left), tall format | -- |
| doc27-R08 | 6 | chart-complex | 848x502 | Easy | Paired panel (right), short format | -- |
| doc27-R09 | 7 | chart-simple | 1576x611 | Easy | Wide horizontal chart | -- |
| doc27-R10 | 8 | chart-simple | 1576x611 | Easy | Wide horizontal chart | -- |
| doc27-R11 | 9 | chart-simple | 1778x619 | Easy | Wide horizontal chart | -- |
| doc27-R12 | 10 | chart-simple | 1913x619 | Easy | Wide horizontal chart | -- |
| doc27-R13 | 11 | chart-simple | 1916x522 | Easy | Wide horizontal chart | -- |
| doc27-R14 | 12 | chart-simple | 1546x656 | Easy | Wide horizontal chart | -- |
| doc27-R15 | 13 | chart-simple | 1795x520 | Easy | Wide horizontal chart | -- |
| doc27-R16 | 14 | diagram | 1106x902 | Medium | European rail map (second half variant) | -- |
| doc27-R17 | 15 | chart-complex | 874x836 | Medium | Paired panel (left) | -- |
| doc27-R18 | 15 | chart-complex | 881x859 | Medium | Paired panel (right) | -- |
| doc27-R19 | 16 | chart-complex | 772x1170 | Medium | Paired panel (left), portrait format | -- |
| doc27-R20 | 16 | chart-complex | 848x851 | Medium | Paired panel (right) | -- |
| doc27-R21 | 17 | chart-complex | 829x626 | Medium | Paired panel (left) | -- |
| doc27-R22 | 17 | chart-complex | 1010x824 | Medium | Paired panel (right) | -- |
| doc27-R23 | 18 | chart-simple | 1576x611 | Easy | Wide horizontal chart (mirrors slide 7) | -- |
| doc27-R24 | 19 | chart-simple | 1576x611 | Easy | Wide horizontal chart (mirrors slide 8) | -- |
| doc27-R25 | 20 | chart-simple | 1778x619 | Easy | Wide horizontal chart (mirrors slide 9) | -- |
| doc27-R26 | 21 | chart-simple | 1968x518 | Easy | Wide horizontal chart | -- |
| doc27-R27 | 22 | chart-simple | 1546x611 | Easy | Wide horizontal chart (mirrors slide 12) | -- |
| doc27-R28 | 23 | chart-simple | 1899x454 | Easy | Wide horizontal chart | -- |
| doc27-R29 | 24 | chart-complex | 926x865 | Medium | Paired panel (left) | -- |
| doc27-R30 | 24 | chart-complex | 868x762 | Medium | Paired panel (right) | -- |
| doc27-R31 | 25 | chart-complex | 910x863 | Medium | Paired panel (left) | -- |
| doc27-R32 | 25 | chart-complex | 867x827 | Medium | Paired panel (right) | -- |
| doc27-R33 | 26 | chart-complex | 1029x863 | Medium | Paired panel (left) | -- |
| doc27-R34 | 26 | chart-complex | 914x837 | Medium | Paired panel (right) | -- |
| doc27-R35 | 27 | chart-simple | 1546x613 | Easy | Wide horizontal chart | -- |
| doc27-R36 | 28 | chart-simple | 1867x496 | Easy | Wide horizontal chart | -- |
| doc27-R37 | 29 | other | 497x484 | Easy | Small element (JPEG, 2.3x2.2 in) | -- |
| doc27-R38 | 29 | chart-complex | 689x774 | Medium | Medium panel | -- |
| doc27-R39 | 30 | other | 497x484 | Easy | Small element (reused, 2.3x2.2 in) | -- |
| doc27-R40 | 30 | chart-complex | 709x773 | Medium | Medium panel | -- |
| doc27-R41 | 31 | infographic | 945x712 | Medium | Summary overview | -- |
| doc27-R42 | 32 | infographic | 1329x743 | Medium | Summary overview (wide) | -- |

Decorative (skip):

| ID | Location | Description | Skip? |
|----|----------|-------------|-------|
| doc27-D01 | slideLayout1 | ERA branding banner (4.9x2.3 in) | Yes: decorative |
| doc27-D02 | slideLayout2 | ERA logo (2.7x1.3 in) | Yes: decorative |
| doc27-D03 | slideLayout3 | ERA logo (2.7x1.3 in) | Yes: decorative |
| doc27-D04 | slideLayout4 | ERA logo (2.7x1.3 in) | Yes: decorative |

Note: Content types are preliminary, based on structural metadata (dimensions,
slide position, layout patterns). The document's two-half structure (slides
2-13 mirroring 14-28) suggests near-duplicate charts in different languages
or time periods. Visual inspection during pass 2 will refine classifications.

**Taggable:** 42 (18 easy, 24 medium)

<br><br>

## Doc 28 -- 28_eurostat_climate_driving_forces_2022.xlsx

XLSX, 765 KB, multi-image
Source: https://ec.europa.eu/eurostat/statistics-explained/images/1/18/Climate_change_driving_forces_2022_figures_and_tables.xlsx

29 XML-defined chart objects across 24 figure sheets (Fig1-Fig23 plus
"Fig19 old"). 20 data sheets provide the underlying data. 2 raster media
files (logos/banners). 6 chart types: line, bar, area, pie, scatter,
pie-of-pie, plus 3 combo charts (area+line, area+bar+line). Several figure
sheets contain 2-3 charts each (Fig1: 2, Fig2: 3, Fig16: 2, Fig17: 2).

| ID | Sheet | Content Type | Difficulty | Description | Skip? |
|----|-------|-------------|------------|-------------|-------|
| doc28-C01 | Fig1 | chart-complex | Medium | Line: GHG emissions index 1990=100, 4 series (1990-2020) | -- |
| doc28-C02 | Fig1 | chart-simple | Easy | Line: GHG tonnes per capita | -- |
| doc28-C03 | Fig2 | chart-complex | Medium | Bar: GHG emissions by country, absolute change 1990-2020, 1 series | -- |
| doc28-C04 | Fig2 | chart-simple | Easy | Bar: GHG emissions by country (supplementary view) | -- |
| doc28-C05 | Fig2 | chart-simple | Easy | Bar: GHG emissions by country (supplementary view) | -- |
| doc28-C06 | Fig3 | chart-complex | Medium | Line: GHG vs GDP decoupling, 4 series (1990-2020) | -- |
| doc28-C07 | Fig4 | chart-complex | Medium | Pie-of-pie: GHG by source sector, EU 2020 | -- |
| doc28-C08 | Fig5 | chart-complex | Hard | Combo (area+bar+line): GHG by sector, change from 1990, 4 series | -- |
| doc28-C09 | Fig6 | chart-complex | Medium | Line: GHG from fuel combustion excl. transport, 3 series | -- |
| doc28-C10 | Fig7 | chart-complex | Medium | Bar: Electricity/heat by fuel, 1990 vs 2020, 6 series | -- |
| doc28-C11 | Fig8 | chart-complex | Medium | Stacked area: Electricity/heat from renewables, 7 series | -- |
| doc28-C12 | Fig9 | chart-simple | Easy | Line: Manufacturing/construction volume index, 2 series | -- |
| doc28-C13 | Fig10 | chart-complex | Medium | Bar: Industry energy consumption by fuel, 1990 vs 2020, 7 series | -- |
| doc28-C14 | Fig11 | chart-complex | Medium | Bar: Household energy consumption by fuel, 1990 vs 2020, 6 series | -- |
| doc28-C15 | Fig12 | chart-complex | Medium | Stacked bar: Transport GHG emissions, 1990-2020, 7 series | -- |
| doc28-C16 | Fig13 | chart-simple | Easy | Line: Transport activity index 1995=100, 2 series | -- |
| doc28-C17 | Fig14 | chart-simple | Easy | Bar: Agriculture GHG, 1990 vs 2020, 2 series | -- |
| doc28-C18 | Fig15 | chart-simple | Easy | Line: Livestock, EU, 2001-2021, 2 series (million head) | -- |
| doc28-C19 | Fig16 | chart-simple | Easy | Line: Manure nitrogen production, EU-27, 2 series | -- |
| doc28-C20 | Fig16 | chart-simple | Easy | Line: Manure nitrogen production, EU, 2 series | -- |
| doc28-C21 | Fig17 | chart-complex | Medium | Bar: Waste management GHG, 1990-2020, 3 series | -- |
| doc28-C22 | Fig17 | chart-complex | Hard | Scatter: Waste-related metric (1 series) | -- |
| doc28-C23 | Fig18 | chart-complex | Medium | Line: Municipal waste treatment, EU, 1995-2020, 3 series | -- |
| doc28-C24 | Fig19 | chart-complex | Hard | Combo (area+line): LULUCF GHG, 7 series (6 area + 1 line) | -- |
| doc28-C25 | Fig19 old | chart-complex | Medium | Combo (area+line): LULUCF with/without, 2 series | -- |
| doc28-C26 | Fig20 | chart-simple | Easy | Bar: Forest area, EU, 1990-2020, 2 series (million hectares) | -- |
| doc28-C27 | Fig21 | chart-simple | Easy | Pie: GHG by economic activity, air emissions accounts, 1 series | -- |
| doc28-C28 | Fig22 | chart-complex | Medium | Bar: GHG production vs consumption perspective, 4 series | -- |
| doc28-C29 | Fig23 | chart-simple | Easy | Pie: GHG by gas type in CO2-equivalents, EU, 1 series | -- |

Decorative (skip):

| ID | Location | Description | Skip? |
|----|----------|-------------|-------|
| doc28-D01 | xl/media/image1.png | Banner/logo (825x121) | Yes: decorative |
| doc28-D02 | xl/media/image2.png | Banner/logo (404x116) | Yes: decorative |

Note: Chart classifications are based on XML chart type elements and series
counts. Charts with 1-2 series in simple types (line, bar, pie) are
chart-simple/Easy. Charts with 3+ series, combo types, stacked areas, or
scatter plots are chart-complex/Medium or Hard. The 3 combo charts (C08,
C24, C25) mix area+line or area+bar+line types. Visual inspection during
pass 2 will refine difficulty ratings.

**Taggable:** 29 (12 easy, 14 medium, 3 hard)

<br><br>

## Doc 29 -- 29_nasa_helio_fleet_dec2025.jpg

JPG, 14 MB, standalone image
Source: https://svs.gsfc.nasa.gov/vis/a010000/a014700/a014718/Helio_Fleet_All_Active_Missions_TEXTDEC25.jpg

High-resolution standalone image (10800x7186 px). NASA Heliophysics Fleet
diagram showing all active solar and space science missions as of December
2025. Labeled spacecraft icons positioned around the Sun and planets with
orbit paths, mission names, and agency logos. Tests pipeline handling of
large raster files (14 MB, 77 megapixels) requiring memory management and
potential downscaling.

| ID | Content Type | Size | Difficulty | Description | Skip? |
|----|-------------|------|------------|-------------|-------|
| doc29-R01 | diagram | 10800x7186 | Medium | NASA heliophysics fleet: all active missions with labeled spacecraft, orbits, and planetary positions | -- |

**Taggable:** 1 (1 medium)

<br><br>

## Doc 30 -- 30_nrc_correspondence_2024.pdf

PDF (scanned), 548 KB, scanned
Source: https://www.nrc.gov/docs/ML2425/ML24253A016.pdf

2-page scanned NRC (Nuclear Regulatory Commission) correspondence. Page 1
is a landscape color scan (1104x850, RGB, FlateDecode). Page 2 is a
portrait bitonal scan stored as JBIG2-compressed segments (1394x1198 main
region + 5 smaller text segments). No fonts, no OCR text layer, no
embedded photographs or illustrations. Clean modern scan of single-column
regulatory correspondence.

| ID | Page | Content Type | Size | Difficulty | Description | Skip? |
|----|------|-------------|------|------------|-------------|-------|
| doc30-S01 | 1 | decorative | 1104x850 | -- | Full-page color scan (landscape, cover/envelope) | Yes: scanned page |
| doc30-S02 | 2 | decorative | 1394x1198 | -- | Full-page bitonal scan (portrait, correspondence text) | Yes: scanned page |

**Taggable:** 0 (scanned text-only pages, no separable content images)

<br><br>

## Corpus Summary

| Category | Docs | Content images | Decorative | Vector figures | Tables |
|----------|------|---------------|------------|----------------|--------|
| multi-image | 02, 05, 06, 11, 12, 16, 18, 19, 20-28 | 269 | 92 | 12 | 24 |
| vector-heavy | 01, 04 | 1 | 2 | 34 | 3 |
| text-heavy | 00, 03, 17 | 1 | 4 | 0 | 4 |
| scanned | 07, 08, 30 | 8 | 0 | 0 | 0 |
| mixed-content | 09 | 6 | 0 | 0 | 0 |
| text-only | 10 | 0 | 0 | 0 | 4 |
| table-image | 13, 14, 15, 29 | 4 | 0 | 0 | 0 |
| **Total** | **31** | **289** | **98** | **46** | **35** |

<br><br>

## Gap Tracker

| Gap | Status | Notes |
|-----|--------|-------|
| Table-as-image | Covered | 5 examples across 5 docs (00, 12-15) |
| Equations | Covered | 4 raster (Doc 11) + 63 native LaTeX (Doc 17) |
| Diagrams | Covered | 36 total; Doc 18 adds ~27 architecture diagrams |
| Photos (non-scanned) | Improved | Docs 05, 16, 19 span consumer, scientific, and environmental |
| DOCX with images | Covered | Docs 16, 19 (medium), Doc 25 (hard) span scientific, regulatory, and clinical |
| Chart-simple raster | Covered | Docs 02, 05 have raster charts |
| Algorithm pseudocode | Covered | Doc 11 has 10 algorithm screenshots |
| Scanned documents | Covered | Docs 07-09 cover letter, form, newspaper |
| XLSX with charts | Covered | Docs 20 (5 charts, medium), 21 (4 charts, easy), 28 (29 charts, hard) span easy/medium/hard |
| HTML with images | Covered | Doc 22 provides 20 inline images (charts + photos) from NASA |
| Infographics | Open | 16 total concentrated in 3 docs; add slide decks or consulting reports |

<br><br>

## Distribution Summary

### By difficulty (taggable content images only)

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 117 | 35% |
| Medium | 165 | 49% |
| Hard | 52 | 15% |
| **Total** | **338** | **100%** |

### By content type (taggable only)

| Content Type | Easy | Medium | Hard | Total |
|-------------|------|--------|------|-------|
| chart-simple | 49 | 3 | 0 | 52 |
| chart-complex | 1 | 54 | 19 | 74 |
| diagram | 23 | 44 | 7 | 74 |
| table-image | 2 | 3 | 0 | 5 |
| equation | 2 | 2 | 0 | 4 |
| infographic | 3 | 9 | 6 | 18 |
| photo | 21 | 7 | 8 | 36 |
| screenshot | 15 | 38 | 2 | 55 |
| other | 2 | 5 | 2 | 9 |
| **Total** | **117** | **165** | **52** | **338** |

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
| 26 | 4 | 18 | 0 | 22 | PPTX |
| 27 | 18 | 24 | 0 | 42 | PPTX |
| 28 | 12 | 14 | 3 | 29 | XLSX |
| 29 | 0 | 1 | 0 | 1 | JPG |
| 30 | 0 | 0 | 0 | 0 | PDF (scanned) |
| **Total** | **91** | **142** | **50** | **283** | |

<br><br>

## Evaluation Subset

### Selection criteria

- Target: 80-120 images covering all content-bearing documents
- Over-represent medium and hard (these differentiate models)
- At least 2 per content type
- Every document with content images must have representation
- Exclude decorative, blank, and scanned-text-only images
- For large repetitive sets, pick 3-6 representative images spanning the
  difficulty range
- Prefer diverse content over repetitive examples from the same figure

### Selected subset (102 images)

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
| doc20-C01 | 20 | -- | chart-complex | Medium | Grouped bar: Obligations, Accrual & Expense Breakdown (12 series) |
| doc20-C03 | 20 | -- | chart-simple | Easy | Pie: Total WIOA Formula Grant Budget (5 segments) |
| doc20-C04 | 20 | -- | chart-simple | Easy | Grouped bar: Direct Training (4 series) |
| doc21-C01 | 21 | -- | chart-simple | Easy | Bar: Priority distribution (3 bars) |
| doc21-C04 | 21 | -- | chart-simple | Easy | Bar: Budget vs Actual Expenditure (2 bars) |
| doc22-R01 | 22 | -- | chart-complex | Medium | GISS temperature anomaly: global surface temperature 1880-present |
| doc22-R03 | 22 | -- | chart-complex | Hard | EPICA 800,000-year temperature + CO2 reconstruction from ice cores |
| doc22-R05 | 22 | -- | chart-complex | Hard | Anthropogenic vs natural climate attribution comparison |
| doc22-R09 | 22 | -- | chart-simple | Easy | Ocean carbon cycle diagram |
| doc22-R12 | 22 | -- | photo | Easy | ISS022-E-6674: Earth from space |
| doc22-R15 | 22 | -- | photo | Medium | Solar corona comparison: solar maximum vs minimum (side-by-side) |
| doc23-R01 | 23 | -- | diagram | Medium | Complete git-flow branching model with merge topology |
| doc23-R04 | 23 | -- | diagram | Easy | Feature branch create-and-merge workflow |
| doc23-R05 | 23 | -- | diagram | Easy | Merge comparison: fast-forward vs no-ff commit graph |
| doc24-R01 | 24 | -- | diagram | Medium | Monolith vs microservices architecture comparison |
| doc24-R02 | 24 | -- | diagram | Medium | Conway's Law: org structure mapped to system architecture |
| doc24-R06 | 24 | -- | diagram | Medium | Micro-deployment: monolith vs microservices infrastructure |
| doc25-R01 | 25 | -- | screenshot | Medium | Application window: main CPRS interface |
| doc25-R02 | 25 | -- | screenshot | Medium | Application window: clinical record view |
| doc25-R07 | 25 | -- | screenshot | Medium | UI panel: form layout |
| doc25-R19 | 25 | -- | screenshot | Medium | Full form: clinical documentation |
| doc26-R01 | 26 | 13 | diagram | Medium | Full adder circuit schematic |
| doc26-R08 | 26 | 19 | diagram | Medium | Full-slide digital logic diagram |
| doc26-R13 | 26 | 30 | diagram | Medium | Wide-format circuit schematic |
| doc26-R22 | 26 | 61 | diagram | Easy | Narrow circuit detail |
| doc27-R01 | 27 | 2 | diagram | Medium | European rail map |
| doc27-R03 | 27 | 4 | chart-complex | Medium | Paired panel (left), medium format |
| doc27-R09 | 27 | 7 | chart-simple | Easy | Wide horizontal chart |
| doc27-R38 | 27 | 29 | chart-complex | Medium | Medium panel |
| doc27-R41 | 27 | 31 | infographic | Medium | Summary overview |
| doc27-R42 | 27 | 32 | infographic | Medium | Summary overview (wide) |
| doc28-C01 | 28 | -- | chart-complex | Medium | Line: GHG emissions index 1990=100, 4 series |
| doc28-C07 | 28 | -- | chart-complex | Medium | Pie-of-pie: GHG by source sector, EU 2020 |
| doc28-C08 | 28 | -- | chart-complex | Hard | Combo (area+bar+line): GHG by sector, 4 series |
| doc28-C11 | 28 | -- | chart-complex | Medium | Stacked area: Electricity/heat from renewables, 7 series |
| doc28-C24 | 28 | -- | chart-complex | Hard | Combo (area+line): LULUCF GHG, 7 series |
| doc28-C29 | 28 | -- | chart-simple | Easy | Pie: GHG by gas type in CO2-equivalents, EU |
| doc29-R01 | 29 | 1 | diagram | Medium | NASA heliophysics fleet: all active missions |

### Subset statistics

**Total:** 102 images from 24 documents

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 25 | 25% |
| Medium | 43 | 42% |
| Hard | 34 | 33% |

| Content Type | Count |
|-------------|-------|
| chart-simple | 13 |
| chart-complex | 25 |
| diagram | 22 |
| screenshot | 13 |
| photo | 11 |
| infographic | 10 |
| table-image | 5 |
| equation | 2 |
| other | 1 |

| Source Format | Count |
|--------------|-------|
| PDF | 46 |
| PPTX | 17 |
| DOCX | 12 |
| HTML | 12 |
| XLSX | 11 |
| JPG | 2 |
| WebP | 1 |
| PNG | 1 |

The expanded subset covers all 8 source formats and all content types. Medium
and hard together comprise 75%. Doc 17 equations are not in the subset (native
LaTeX, not raster) but test equation region detection during pipeline
evaluation.

For detailed breakdowns by content type, source format, and coverage gaps,
see the [Annotation Test Set](./evaluation/annotation-test-set.md).

# Difficulty Tags and Evaluation Subset

Difficulty classification of all content images and vector figures across
the evaluation fixture set. Based on visual inspection during cataloging
(Work Item 01). Feeds into rubric design (Work Item 03) and pipeline
comparison (Work Item 07).

**Created:** 2026-02-27
**Source:** fixtures/image-catalog.md


## Difficulty Criteria

| Level | Criteria | Examples |
|-------|----------|---------|
| Easy | Single clear subject, obvious content, minimal interpretation needed | Simple bar chart with labeled axes, a photo, a single equation |
| Medium | Multiple elements to identify and relate, moderate domain knowledge | Multi-series line chart, architecture diagram, algorithm pseudocode box |
| Hard | Dense information, requires understanding relationships or domain context | Multi-panel composite figure, dense scatter plot with annotations, infographic with data layers, complex multi-column layout |


## Tagging Legend

- **ID format:** `doc{NN}-{R|V|S}{seq}` where R=raster, V=vector, S=scanned
- **Skip:** images excluded from evaluation (decorative, blank, too small)
- Content types and descriptions come from the image catalog


## Doc 00: gemini3_pro_model_card.pdf

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc00-R01 | 1 | decorative | -- | Black horizontal bar (837x13) | Yes: decorative line |
| doc00-R02 | 1 | decorative | -- | Google logo (932x312) | Yes: decorative logo |
| doc00-R03 | 5 | table-image | Medium | Benchmark comparison table: Gemini 3 Pro vs 3 competitors across ~22 benchmarks, color-coded cells | -- |

**Taggable images:** 1 (1 medium)


## Doc 01: gpt4_system_card.pdf

### Raster Images

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc01-R01 | 58 | chart-complex | Medium | Figure 11: Heatmap of IF evaluation results, 3x3 color-coded grid with win/lose rates | -- |

### Vector Figures

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc01-V01 | 8 | infographic | Hard | Figure 1: 3-column harmful content comparison (7 prompt-response pairs), color-coded boxes | -- |
| doc01-V02 | 9 | infographic | Medium | Figure 2: Non-adversarial bias example, 3-column prompt-response comparison | -- |
| doc01-V03 | 10 | infographic | Medium | Figure 3: Biased content examples, 3-column layout, 2 prompt-response pairs | -- |
| doc01-V04 | 11 | infographic | Hard | Figure 4: Disinformation examples, 3-column layout, 3 prompt-response pairs | -- |
| doc01-V05 | 13 | infographic | Medium | Unlabeled: Dual-use substance prompt + response, 2-box layout | -- |
| doc01-V06 | 14 | infographic | Medium | Unlabeled: Cybersecurity prompt + response, 2-box layout | -- |
| doc01-V07 | 17 | infographic | Hard | Figure 5: Tool-augmented risky task, chain-of-thought for chemical compound | -- |
| doc01-V08 | 23 | infographic | Hard | Figure 6: RBRM prompt example, styled text boxes with classification output | -- |
| doc01-V09 | 23 | chart-simple | Easy | Figure 7: Bar chart of incorrect behavior rate, 3 models compared | -- |
| doc01-V10 | 25 | chart-simple | Easy | Figure 8: Bar chart of TruthfulQA accuracy across prompting variants | -- |
| doc01-V11 | 27 | infographic | Medium | Figure 9: GPT-4 classification prompt example, natural language rubric | -- |
| doc01-V12 | 28 | infographic | Hard | Figure 10: Jailbreaks for GPT-4-launch, 2 attack types with 3-column layout | -- |

**Taggable images:** 13 (2 easy, 5 medium, 6 hard)


## Doc 02: icml2019_importance_sampling.pdf

### Raster Images

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc02-R01 | 6 | chart-complex | Medium | Figure 2a: Gridworld MSE vs trajectories, 6 method lines with confidence bands | -- |
| doc02-R02 | 6 | chart-complex | Medium | Figure 2b: Gridworld Alt, same structure as 2a | -- |
| doc02-R03 | 6 | chart-complex | Medium | Figure 2c: Gridworld On-Policy variant | -- |
| doc02-R04 | 6 | chart-complex | Medium | Figure 2d: Gridworld On-Policy Alt | -- |
| doc02-R05 | 6 | chart-complex | Medium | Figure 3: SinglePath MDP off-policy estimation, RIS vs EIS | -- |
| doc02-R06 | 6 | chart-complex | Medium | Figure 4a: Linear dynamical system MSE vs trajectories | -- |
| doc02-R07 | 6 | chart-complex | Medium | Figure 4b: Linear dynamical system alternative weights | -- |
| doc02-R08 | 7 | chart-simple | Easy | Figure 5a: Hopper MSE grouped bar chart, architecture comparison | -- |
| doc02-R09 | 7 | chart-simple | Easy | Figure 5b: HalfCheetah MSE grouped bar chart | -- |
| doc02-R10 | 7 | chart-complex | Hard | Figure 6: 3-panel vertical chart (error, squared error, estimate) during training | -- |
| doc02-R11 | 16 | chart-simple | Easy | Figure 7a: Policy and Reward line chart (small, 386x252) | -- |
| doc02-R12 | 16 | chart-simple | Easy | Figure 7b: 10 Sample Approximation line chart | -- |
| doc02-R13 | 16 | chart-simple | Easy | Figure 7c: 200 Sample Approximation line chart | -- |
| doc02-R14 | 18 | chart-complex | Medium | Figure 9a: Gridworld Off-Policy EIS variant comparison | -- |
| doc02-R15 | 18 | chart-complex | Medium | Figure 9b: Gridworld On-Policy EIS variant comparison | -- |
| doc02-R16 | 19 | chart-complex | Hard | Figure 10: 3-panel stacked chart (NLL, MSE, Value), RIS vs OIS vs True Value | -- |

### Vector Figures

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc02-V01 | 5 | diagram | Easy | Figure 1: SinglePath MDP state diagram, s0-s4 with action arrows | -- |
| doc02-V02 | 16 | diagram | Easy | Figure 8: SinglePath MDP diagram (same as Figure 1) | -- |

**Taggable images:** 18 (7 easy, 9 medium, 2 hard)


## Doc 03: imf_economic_impacts_ai.pdf

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc03-R01 | 1 | decorative | -- | Cover page background (1633x2113) | Yes: decorative cover |
| doc03-R02 | 69 | decorative | -- | Back cover background (1633x2113) | Yes: decorative cover |

**Taggable images:** 0


## Doc 04: anthropic_economic_index.pdf

### Raster Images

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc04-R01 | 17 | decorative | -- | Gradient color bar (20x397) within scatter plot | Yes: decorative element |
| doc04-R02 | 27 | decorative | -- | Gradient color bar (11x248) within scatter plot | Yes: decorative element |

### Vector Figures

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc04-V01 | 8 | chart-complex | Hard | Figure 1.1: 8-panel grid of line charts, usage share trends across occupation groups | -- |
| doc04-V02 | 10 | chart-complex | Hard | Figure 1.2: 2-panel automation vs augmentation trends + individual interaction types | -- |
| doc04-V03 | 13 | chart-simple | Easy | Figure 2.1: Top 20 countries horizontal bar chart | -- |
| doc04-V04 | 14 | chart-simple | Easy | Figure 2.2: Top 20 countries by AI Usage Index, horizontal bars | -- |
| doc04-V05 | 15 | chart-complex | Hard | Figure 2.3: World choropleth map color-coded by AI Usage Index tiers | -- |
| doc04-V06 | 17 | chart-complex | Hard | Figure 2.4: Income vs AUI scatter plot with regression, log scale | -- |
| doc04-V07 | 19 | chart-simple | Easy | Figure 2.5: Top 30 US states horizontal bar chart | -- |
| doc04-V08 | 20 | chart-complex | Hard | Figure 2.6: US choropleth map by per-capita usage tiers | -- |
| doc04-V09 | 22 | chart-complex | Hard | Figure 2.7: 4-panel scatter plots by occupation group | -- |
| doc04-V10 | 23 | infographic | Medium | Figure 2.8: 4-panel overrepresented request clusters (US, Brazil, Vietnam, India) | -- |
| doc04-V11 | 25 | infographic | Medium | Figure 2.9: 4-panel overrepresented categories (CA, TX, FL, SC) | -- |
| doc04-V12 | 26 | infographic | Medium | Figure 2.10: DC highest Claude usage, 2-panel top tasks and clusters | -- |
| doc04-V13 | 27 | chart-complex | Hard | Figure 2.11: Augmentation share vs AUI residuals scatter plot with regression | -- |
| doc04-V14 | 32 | chart-simple | Easy | Figure 3.1: AI adoption rates line chart | -- |
| doc04-V15 | 33 | chart-simple | Medium | Figure 3.2: Horizontal stacked bar chart, taxonomy of Claude usage | -- |
| doc04-V16 | 34 | chart-complex | Medium | Figure 3.3: Grouped horizontal bars, Claude.ai vs API by occupation | -- |
| doc04-V17 | 35 | chart-complex | Hard | Figure 3.4: 2-panel Lorenz curves + power-law task rank chart | -- |
| doc04-V18 | 37 | chart-complex | Hard | Figure 3.5: 2-panel scatter plots, automation vs augmentation across O*NET tasks | -- |
| doc04-V19 | 39 | chart-simple | Easy | Figure 3.6: Average output token index horizontal bar chart | -- |
| doc04-V20 | 40 | chart-complex | Hard | Figure 3.7: Output vs input token index scatter plot with regression | -- |
| doc04-V21 | 42 | chart-complex | Medium | Figure 3.8: API cost vs usage share scatter plot | -- |
| doc04-V22 | 43 | chart-complex | Hard | Figure 3.9: Partial regression scatter plot, cost vs usage controlling for characteristics | -- |

**Taggable images:** 22 (5 easy, 6 medium, 11 hard)


## Doc 05: gemini_multimodal_report.pdf

### Raster Images

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc05-R01 | 1 | decorative | -- | Thin decorative bar (3810x512) | Yes: decorative |
| doc05-R02 | 3 | screenshot | Hard | Figure 1: Handwritten physics problem with model verification, composite prompt+response | -- |
| doc05-R03 | 4 | diagram | Medium | Figure 2: Gemini model family architecture overview, Transformer decoder diagram | -- |
| doc05-R04 | 15 | screenshot | Hard | Figure 5: Multimodal reasoning for matplotlib code gen, composite of code + chart renders | -- |
| doc05-R05 | 17 | decorative | -- | Thin gradient element (20x397) within Figure 6 | Yes: decorative |
| doc05-R06 | 19 | photo | Easy | Table 13 image 1: Cooking omelet in pan (early stage) | -- |
| doc05-R07 | 19 | photo | Easy | Table 13 image 2: Omelet partially cooked | -- |
| doc05-R08 | 19 | photo | Easy | Table 13 image 3: Finished omelet on plate | -- |
| doc05-R09 | 21 | decorative | -- | Small icon (560x560) within Figure 7 | Yes: decorative |
| doc05-R10 | 21 | decorative | -- | Nested icon inside FORM in Figure 7 | Yes: decorative |
| doc05-R11 | 78 | photo | Easy | Figure 11: Persian shield plant, species identification example | -- |
| doc05-R12 | 79 | photo | Easy | Figure 12 image 1: Goldendoodle at beach | -- |
| doc05-R13 | 79 | photo | Easy | Figure 12 image 2: Goldendoodle in city | -- |
| doc05-R14 | 79 | photo | Easy | Figure 12 image 3: Goldendoodle portrait | -- |
| doc05-R15 | 80 | photo | Medium | Figure 13: Handwritten shapes sequence (triangle, square, pentagon, ?) | -- |
| doc05-R16 | 81 | diagram | Easy | Figure 14: Parallelogram with labeled dimensions (x, s, 15) | -- |
| doc05-R17 | 81 | photo | Medium | Figure 15 image 1: Moon photograph (puzzle input) | -- |
| doc05-R18 | 81 | photo | Medium | Figure 15 image 2: Golf balls on lunar surface (puzzle input) | -- |
| doc05-R19 | 82 | photo | Easy | Figure 16: NYC street at night with Empire State Building | -- |
| doc05-R20 | 83 | other | Medium | Figure 17: Internet meme ("Game at 300 FPS / 75 Hz Monitor") | -- |
| doc05-R21 | 84 | diagram | Medium | Figure 18: Chinese family tree diagram with character labels | -- |
| doc05-R22 | 86 | screenshot | Medium | Figure 19: Rendered "Opossum Search" website from code gen | -- |
| doc05-R23 | 89 | chart-complex | Hard | Figure 22 image 1: 4 matplotlib subplots (sin, multi-line, 3D surface, contour) | -- |
| doc05-R24 | 89 | chart-simple | Easy | Figure 22 image 2: Rendered exponential curve output | -- |
| doc05-R25 | 90 | photo | Easy | Figure 23 frame 1: Soccer penalty kick video frame | -- |
| doc05-R26 | 90 | photo | Easy | Figure 23 frame 2: Soccer kick in progress | -- |
| doc05-R27 | 90 | photo | Easy | Figure 23 frame 3: Ball in flight | -- |
| doc05-R28 | 90 | photo | Easy | Figure 23 frame 4: Post-kick follow-through | -- |

### Vector Figures

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc05-V01 | 9 | chart-simple | Easy | Figure 3: Grouped bar chart of language understanding performance | -- |
| doc05-V02 | 11 | chart-simple | Medium | Figure 4: Negative log likelihood vs token index line chart | -- |
| doc05-V03 | 21 | diagram | Hard | Figure 7: Post-training data flywheel, SFT/RM/RL fine-tuning flow | -- |
| doc05-V04 | 23 | diagram | Medium | Figure 8: Gemini tool-use control loop flowchart | -- |
| doc05-V05 | 74 | chart-simple | Easy | Figure 9: CoT with uncertainty routing grouped bars, GPT-4 vs Gemini | -- |
| doc05-V06 | 77 | infographic | Hard | Figure 10: Multimodal chart understanding, bar charts + model response table | -- |
| doc05-V07 | 87 | other | Easy | Figure 20: Text-based calculus problem with solution | -- |
| doc05-V08 | 88 | other | Medium | Figure 21: Multi-step math problem with rendered table response | -- |

**Taggable images:** 31 (16 easy, 10 medium, 5 hard)


## Doc 06: arxiv_2206_01062.pdf

### Raster Images

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc06-R01 | 1 | screenshot | Medium | Figure 1 thumbnail 1: Document page with colored layout bounding boxes | -- |
| doc06-R02 | 1 | decorative | -- | Small icon (20x20) | Yes: too small |
| doc06-R03 | 1 | decorative | -- | Small icon (20x20) | Yes: too small |
| doc06-R04 | 1 | screenshot | Medium | Figure 1 thumbnail 2: Annotated document page (140x189) | -- |
| doc06-R05 | 1 | screenshot | Medium | Figure 1 thumbnail 3: Annotated document page (140x189) | -- |
| doc06-R06 | 1 | screenshot | Medium | Figure 1 thumbnail 4: Annotated document page (170x166) | -- |
| doc06-R07 | 4 | screenshot | Medium | Figure 3: CCS annotation UI with bounding boxes and label palette (1120x1512) | -- |
| doc06-R08 | 4 | screenshot | Medium | Annotated PDF pages column showing layout categories (486x1528) | -- |
| doc06-R09 to R16 | 5 | screenshot | Medium | Figure 4: 8 document pages showing annotation alternatives (all 1025x1025) | -- |
| doc06-D01 to D08 | 5 | decorative | -- | 8 thin separator bars (434x26) | Yes: decorative |
| doc06-R17 to R22 | 9 | screenshot | Medium | Figure 6: 6 layout prediction examples (all 1025x1025) | -- |

### Vector Figures

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc06-V01 | 3 | chart-simple | Easy | Figure 2: Pie chart of DocLayNet page distribution by category | -- |
| doc06-V02 | 6 | chart-complex | Medium | Figure 5: mAP prediction performance across models, multi-series line chart | -- |

**Taggable images:** 22 content (2 easy, 20 medium) -- but many are near-identical document screenshots


## Doc 07: epa_sample_letter.pdf

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc07-S01 | 1 | other | Easy | Full-page scan: EPA letterhead, typed text | Yes: no annotation target (OCR only) |
| doc07-S02 | 2 | other | Easy | Full-page scan: continuation of letter | Yes: no annotation target |
| doc07-S03 | 3 | other | Easy | Full-page scan: closing and signature | Yes: no annotation target |

**Taggable images:** 0 (all skipped -- scanned text, no visual content to annotate)


## Doc 08: xerox_mfp_scan_forestburg.pdf

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc08-S01 | 1 | other | Medium | Full-page scan: Employment form with fields, checkboxes, logo | Yes: no annotation target (OCR/form) |
| doc08-S02 | 2 | other | Medium | Full-page scan: Employment history form with table structure | Yes: no annotation target |
| doc08-S03 | 3 | other | Medium | Full-page scan: References and education tables | Yes: no annotation target |
| doc08-S04 | 4 | other | Easy | Full-page scan: Criminal history verification text | Yes: no annotation target |
| doc08-S05 | 5 | other | Easy | Full-page scan: Criminal history addendum | Yes: no annotation target |

**Taggable images:** 0 (all skipped -- scanned forms, no visual content to annotate)


## Doc 09: archive_newspaper_1948.pdf

| ID | Page | Content Type | Difficulty | Description | Skip? |
|----|------|-------------|------------|-------------|-------|
| doc09-S01 | 1 | other | Hard | Full-page scan: Front page with headlines, news photos, multi-column layout | Yes: no separate crops (photos within scan) |
| doc09-S02 | 2 | other | Hard | Full-page scan: Society/ads with Safeway ad illustrations | Yes: no separate crops |
| doc09-S03 | 3 | other | Hard | Full-page scan: News page with portrait, service directory | Yes: no separate crops |
| doc09-S04 | 4 | other | Hard | Full-page scan: Editorial/comics page with marching photo, comic strips, crossword | Yes: no separate crops |
| doc09-S05 | 5 | other | Hard | Full-page scan: Sports/ads page with woman's portrait, theater listings | Yes: no separate crops |
| doc09-S06 | 6 | other | Hard | Full-page scan: Classified ads, dense multi-column | Yes: no separate crops |

**Taggable images:** 0 (all skipped -- photos/illustrations embedded within full-page scans, not individually extractable)


## Doc 10: medrxiv_llama4_benchmark.docx

No images in this document.

**Taggable images:** 0


## Doc 11: policy_gradient_rl_lecture.pptx

### Algorithm Pseudocode

| ID | Slide | Content Type | Difficulty | Description | Skip? |
|----|-------|-------------|------------|-------------|-------|
| doc11-R01 | 36 | screenshot | Medium | Tabular TD(0) pseudocode: initialize V(s), episode loop, TD update | -- |
| doc11-R02 | 39 | screenshot | Medium | Sarsa on-policy TD control: Q(S,A) update with epsilon-greedy | -- |
| doc11-R03 | 41 | screenshot | Medium | Q-learning off-policy TD: max_a Q(S',a) update | -- |
| doc11-R04 | 48 | screenshot | Hard | DQN loss function and gradient from Mnih et al. Nature paper | -- |
| doc11-R05 | 49 | screenshot | Hard | Deep Q-learning with Experience Replay, full algorithm | -- |
| doc11-R06 | 60 | screenshot | Medium | REINFORCE Monte-Carlo policy gradient pseudocode | -- |
| doc11-R07 | 63 | screenshot | Medium | One-step Actor-Critic (episodic) pseudocode | -- |
| doc11-R08 | 72 | screenshot | Hard | Asynchronous one-step Q-learning pseudocode (A3C paper) | -- |
| doc11-R09 | 76 | screenshot | Hard | Asynchronous n-step Q-learning pseudocode (A3C supplementary) | -- |
| doc11-R10 | 79 | screenshot | Hard | Asynchronous advantage actor-critic pseudocode (A3C) | -- |

### Equations

| ID | Slide | Content Type | Difficulty | Description | Skip? |
|----|-------|-------------|------------|-------------|-------|
| doc11-R11 | 55 | equation | Easy | Softmax policy parameterization pi(a|s,theta) | -- |
| doc11-R12 | 58 | equation | Easy | REINFORCE update rule theta_{t+1} | -- |
| doc11-R13 | 62 | equation | Medium | Actor-critic update with baseline, two-line equation | -- |
| doc11-R14 | 78 | equation | Medium | Generalized advantage estimate, sum with V terms | -- |

### Decorative

| ID | Slides | Content Type | Difficulty | Description | Skip? |
|----|--------|-------------|------------|-------------|-------|
| doc11-D01 to D12 | 21-34 | decorative | -- | 12 white/blank separator bars | Yes: blank images |

**Taggable images:** 14 (2 easy, 7 medium, 5 hard)


## Doc 12: minnstate_fy2025_budget.pptx

| ID | Slide | Content Type | Difficulty | Description | Skip? |
|----|-------|-------------|------------|-------------|-------|
| doc12-R01 | -- | decorative | -- | Minnesota State logo (small header) | Yes: decorative logo |
| doc12-R02 | -- | decorative | -- | Minnesota State "M" banner (large) | Yes: decorative logo |
| doc12-R03 | -- | table-image | Medium | Table 9: North Star Promise Program Projected Awards, FY2025. 4 institution rows with student count, average award, total awards ($23.2M total) | -- |
| doc12-R04 | -- | decorative | -- | Minnesota State full logo (large) | Yes: decorative logo |

**Taggable images:** 1 (1 medium)


## Doc 13: artpro_table.webp

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc13-R01 | table-image | Easy | Aircraft wing specification table: 6 wing models, 7 numeric columns (wingspan, chord, area, volume, aspect ratio), alternating row shading | -- |

**Taggable images:** 1 (1 easy)


## Doc 14: simple_table.png

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc14-R01 | table-image | Easy | Simple 3-column table (Cell, Format, Formula) with 5 rows, clean gridlines, spreadsheet formulas | -- |

**Taggable images:** 1 (1 easy)


## Doc 15: timetable.jpg

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc15-R01 | table-image | Medium | SWORD Deadlines: 9-week course schedule with 4 assignment types, color-coded cells showing staggered submission pattern | -- |

**Taggable images:** 1 (1 medium)


## Doc 16: cambridge_mitoball_biology.docx

| ID | Content Type | Difficulty | Description | Skip? |
|----|-------------|------------|-------------|-------|
| doc16-R01 | decorative | -- | TIFF logo/icon (11 KB) | Yes: decorative branding |
| doc16-R02 | photo | Hard | Figure 1: 9-sub-panel composite (A-I) -- spermatogenesis diagram, fluorescence microscopy, EM series, bar charts, time-lapse, multi-channel staining | -- |
| doc16-R03 | photo | Hard | Figure 2: 7-sub-panel composite (A-G) -- testis cross-section, electron micrographs, 3x4 fluorescence grid, PolG1 dual stain | -- |
| doc16-R04 | photo | Hard | Figure 3: Genetic knockdown panels -- control vs mfn RNAi vs Drp1 KD across multiple fluorescence channels | -- |
| doc16-R05 | photo | Hard | Figure 4: Mitoball ultrastructure -- fluorescence and EM at multiple developmental stages | -- |
| doc16-R06 | photo | Hard | Figure 5: Cross-species fluorescence comparison with annotations and scale bars | -- |
| doc16-R07 | photo | Hard | Figure S1: Supplementary control/experimental fluorescence panels | -- |
| doc16-R08 | photo | Hard | Figure S2: Extended cross-species panel -- 8+ insect species (Drosophila, mosquito, cricket, cockroach, locust) | -- |
| doc16-R09 | photo | Hard | Figure S3: Cytoskeletal markers (Phalloidin, Pav-GFP, ATP5A, alpha-spectrin) control vs hts mutant | -- |

**Taggable images:** 8 (8 hard)


## Doc 17: arxiv_fractional_brownian_sde.pdf

No embedded raster images. All 63 equations are native LaTeX. Equation
regions must be identified and cropped from rendered pages by the pipeline.

**Taggable images:** 0 (equations are native LaTeX, not raster)

Note: If the pipeline extracts equation crops from page renders, each would
be medium-to-hard difficulty depending on complexity. Estimated 15-20
distinct equation regions suitable for annotation (display equations,
multi-line derivations, theorem blocks).


## Doc 18: ibm_microservices_redbook.pdf

Architecture diagrams are the primary content. Difficulty depends on
component count, layering complexity, and label density.

**Taggable images:** ~52 (27 architecture diagrams + 5 process diagrams + 20 UI screenshots)

| Image ID | Description | Content Type | Difficulty |
|----------|-------------|-------------|------------|
| doc18-F1-1 | Sample microservices application | diagram | Easy |
| doc18-F1-2 | Monolithic multi-tiered architecture | diagram | Easy |
| doc18-F1-3 | Microservices architecture (languages + data stores) | diagram | Medium |
| doc18-F2-1 | "Old" style service design | diagram | Easy |
| doc18-F2-2 | Microservices redesign | diagram | Medium |
| doc18-F2-3 | Circuit breaker sequence diagram | diagram | Medium |
| doc18-F2-4 | Bulkhead pattern (thread pool isolation) | diagram | Medium |
| doc18-F2-5 | RESTful API calls | diagram | Easy |
| doc18-F2-6 | API Gateway fronting microservices | diagram | Medium |
| doc18-F2-8 | REST architecture with caches | diagram | Medium |
| doc18-F2-9 | Messaging use cases | diagram | Easy |
| doc18-F2-10 | Event notification (stock price) | diagram | Easy |
| doc18-F3-4 | Decentralized data store | diagram | Medium |
| doc18-F3-5 | Microservices transformation | diagram | Medium |
| doc18-F4-5 | Cloud integration flow | diagram | Medium |
| doc18-F5-2 | North Star Architecture (DevOps Services) | diagram | Hard |
| doc18-F5-3 | Bluemix console architecture (pre-microservice) | diagram | Hard |
| doc18-F5-6 | Bluemix console microservice transformation | diagram | Hard |
| doc18-F5-8 | Watson Developer Cloud platform (4-layer) | diagram | Hard |
| doc18-F5-9 | IaaS++ architecture (multi-zone) | diagram | Hard |
| doc18-F5-11 | Service register and discovery | diagram | Medium |
| doc18-F5-12 | Watson service onboarding | diagram | Medium |
| doc18-F6-2 | CloudTrader components overview | diagram | Medium |
| doc18-F6-4 | CloudTrader with externalized Quote | diagram | Medium |
| doc18-F8-1 | Acme Air monolithic architecture | diagram | Easy |
| doc18-F8-12 | Acme Air microservices architecture | diagram | Medium |
| doc18-F4-16 | Application communication in Bluemix | diagram | Easy |
| doc18-F2-7 | Hills Playback timeline | infographic | Medium |
| doc18-F3-1 | DevOps continuous delivery | infographic | Medium |
| doc18-F3-2 | Challenges with traditional delivery | infographic | Easy |
| doc18-F3-3 | IBM DevOps framework | infographic | Hard |
| doc18-F4-8 | ALM of microservices in Bluemix | infographic | Medium |
| doc18-F4-1 | Bluemix service categories | screenshot | Easy |
| doc18-F4-9 | Create app from Bluemix catalog | screenshot | Easy |
| doc18-F4-10 | Create microservice in dashboard | screenshot | Medium |
| doc18-F4-13 | Scaling options in Bluemix console | screenshot | Easy |
| doc18-F4-14 | Load balance on Bluemix | screenshot | Easy |
| doc18-F5-1 | DevOps Services starting point | screenshot | Easy |
| doc18-F5-5 | Bluemix landing page UI composition | screenshot | Medium |
| doc18-F5-10 | Watson services in Bluemix | screenshot | Easy |
| doc18-F6-1 | CloudTrader user interface | screenshot | Easy |
| doc18-F6-5 | Code editing in DevOps Services | screenshot | Medium |
| doc18-F7-1 | Online Store sample | screenshot | Medium |
| doc18-F7-2 | Monitoring: performance | screenshot | Medium |
| doc18-F7-3 | Monitoring: availability | screenshot | Medium |
| doc18-F8-4 | Acme Air web app in Bluemix | screenshot | Easy |
| doc18-F8-11 | Acme Air home page | screenshot | Easy |
| doc18-F8-16 | Hystrix Dashboard home | screenshot | Easy |
| doc18-F8-17 | Hystrix Dashboard (streams) | screenshot | Medium |
| doc18-F8-18 | Bluemix dashboard: Acme Air components | screenshot | Medium |
| doc18-F4-3 | Deployment models (local, dedicated, public) | diagram | Medium |
| doc18-F4-12 | Multi-region delivery pipeline | diagram | Medium |

Difficulty distribution for Doc 18:
- Easy: 18 (8 simple diagrams + 1 infographic + 9 screenshots)
- Medium: 22 (14 diagrams + 3 infographics + 5 screenshots + 2 screenshots)
- Hard: 6 (5 complex multi-layer architectures + 1 framework diagram)
- Total: ~46 (excluding some duplicate figure references and minor screenshots)


## Doc 19: cris_electronic_screens_2023.docx

Australian government energy efficiency report with mixed raster content.
First DOCX with charts (simple + complex) and first easy/medium DOCX images.

**Taggable images:** 10

| Image ID | Description | Content Type | Difficulty |
|----------|-------------|-------------|------------|
| doc19-R01 | Pie chart: equipment market share (5 segments) | chart-simple | Easy |
| doc19-R02 | Photo: airport departure hall with display screens | photo | Medium |
| doc19-R03 | Photo: Changi Airport digital signage kiosk | photo | Easy |
| doc19-R04 | Stacked area chart: EU energy use 1990-2030 | chart-simple | Easy |
| doc19-R05 | Scatter/strip chart: energy ratings data | chart-complex | Medium |
| doc19-R06 | Multi-line chart: power vs screen area (9 lines) | chart-complex | Medium |
| doc19-R07 | Multi-line chart: max power vs area (11 lines, annotated) | chart-complex | Hard |
| doc19-R08 | Bar chart: star rating distribution (12 bars) | chart-simple | Easy |
| doc19-R09 | Energy rating label: Super Efficiency (199 kWh) | infographic | Easy |
| doc19-R10 | Energy rating label: Standard (485 kWh) | infographic | Easy |


## Distribution Summary

### By difficulty (taggable content images only)

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 57 | 30% |
| Medium | 85 | 45% |
| Hard | 47 | 25% |
| **Total** | **189** | **100%** |

### By content type (taggable only)

| Content Type | Easy | Medium | Hard | Total |
|-------------|------|--------|------|-------|
| chart-simple | 12 | 3 | 0 | 15 |
| chart-complex | 0 | 14 | 14 | 28 |
| diagram | 12 | 17 | 7 | 36 |
| table-image | 2 | 3 | 0 | 5 |
| equation | 2 | 2 | 0 | 4 |
| infographic | 3 | 7 | 6 | 16 |
| photo | 15 | 4 | 8 | 27 |
| screenshot | 11 | 28 | 2 | 41 |
| other | 0 | 5 | 2 | 7 |
| chart-simple (vector) | -- | -- | -- | (incl above) |
| **Total** | **57** | **85** | **47** | **189** |

Note: Doc 06 contributes 20 medium-difficulty screenshots that are mostly
near-identical document page examples. For evaluation subset selection,
only 2-3 representative examples should be included.

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
| 17 | 0 | 0 | 0 | 0 | PDF (equations only) |
| 18 | 18 | 22 | 6 | 46 | PDF |
| 19 | 5 | 4 | 1 | 10 | DOCX |
| **Total** | **57** | **85** | **47** | **189** | |


## Gap Analysis

### Underrepresented content types

| Gap | Current count | Issue | Recommendation |
|-----|--------------|-------|----------------|
| table-image | 5 (doc00, 12-15) | Addressed: was 1, now 5 across 5 docs (government budget, aircraft specs, spreadsheet, course schedule) | Covered |
| equation | 4 raster (doc11) + 63 native LaTeX (doc17) | Doc 17 adds diverse LaTeX equations (display, inline, multi-line, theorem environments) | Covered |
| infographic | 9 (doc01: 8, doc04: 3, doc05: 1) | Concentrated in 2 documents; mostly vector-drawn | Add slide decks or consulting reports with raster infographics |
| diagram | 36 (docs 02, 05, 18) | Doc 18 adds ~27 architecture diagrams (component, sequence, deployment, topology) | Covered |
| photo | 25 (doc05: 17 consumer, doc16: 8 scientific microscopy) | Now spans 2 documents with distinct domains (consumer + scientific) | Improved |

### Underrepresented difficulty combinations

| Combination | Count | Issue |
|-------------|-------|-------|
| chart-simple + hard | 0 | No hard simple charts (expected -- simple charts are inherently easy/medium) |
| photo + hard | 8 | Addressed by Doc 16 (scientific microscopy composites) |
| diagram + hard | 2 | Only 2 hard diagrams (doc05-V03, doc05-V06) |
| table-image + hard | 0 | No complex table-as-image examples (but 5 easy/medium now available) |

### Format coverage

| Format | Documents | Taggable images | Issue |
|--------|-----------|----------------|-------|
| PDF (digital) | 00-06, 17, 18 | 153 | Well covered; Doc 18 adds architecture diagrams |
| PDF (scanned) | 07-09 | 0 | No annotation targets; only OCR testing |
| DOCX | 10, 16, 19 | 18 | Doc 16: scientific photos; Doc 19: charts + photos + infographics |
| PPTX | 11, 12 | 15 | Two documents; RL algorithms + government budget |
| Standalone images | 13-15 | 3 | WebP, PNG, JPG table-image fixtures |

### Recommended additional fixtures

To address the gaps above, the following fixture types should be sourced:

1. **Consulting/business slide deck (PPTX)** -- infographics, data
   visualizations, photos, mixed content types. Addresses: infographic
   gap, photo diversity, PPTX format coverage.

2. ~~**Government statistical report (PDF)**~~ -- Addressed by Docs 12-15
   (table-as-image now has 5 examples across 5 documents).

3. ~~**Academic paper with equations (PDF)**~~ -- Addressed by Doc 17
   (63 native LaTeX equations across 24 pages, diverse notation).

4. ~~**Technical documentation with diagrams (PDF or DOCX)**~~ -- Addressed
   by Doc 18 (IBM Redbook with ~27 architecture diagrams: component,
   sequence, deployment, topology).

5. ~~**Medical/scientific paper with photos (PDF)**~~ -- Addressed by Doc 16
   (Cambridge biology paper with fluorescence microscopy, electron
   micrographs, cross-species comparisons; 8 hard-difficulty composites).


## Evaluation Subset Selection

### Selection criteria

- Target: 40-60 images
- Over-represent medium and hard (these differentiate models)
- At least 2 per content type
- At least 5 documents represented
- Exclude decorative, blank, and scanned-text-only images
- For Doc 06, include only 2-3 representative screenshots (not all 20)
- Prefer diverse content over repetitive examples from the same figure

### Selected subset

| ID | Doc | Page | Content Type | Difficulty | Description |
|----|-----|------|-------------|------------|-------------|
| doc00-R03 | 00 | 5 | table-image | Medium | Benchmark comparison table (only table-as-image in corpus) |
| doc01-R01 | 01 | 58 | chart-complex | Medium | IF evaluation heatmap, 3x3 color grid |
| doc01-V01 | 01 | 8 | infographic | Hard | 3-column harmful content comparison, 7 pairs |
| doc01-V04 | 01 | 11 | infographic | Hard | Disinformation examples, 3-column layout |
| doc01-V07 | 01 | 17 | infographic | Hard | Tool-augmented risky task, chain-of-thought |
| doc01-V09 | 01 | 23 | chart-simple | Easy | Bar chart of incorrect behavior rate |
| doc01-V12 | 01 | 28 | infographic | Hard | Jailbreaks for GPT-4-launch |
| doc02-R01 | 02 | 6 | chart-complex | Medium | Gridworld MSE with 6 method lines and confidence bands |
| doc02-R08 | 02 | 7 | chart-simple | Easy | Hopper MSE grouped bar chart |
| doc02-R10 | 02 | 7 | chart-complex | Hard | 3-panel vertical training curves |
| doc02-R11 | 02 | 16 | chart-simple | Easy | Policy and Reward line chart (small, 386x252) |
| doc02-R16 | 02 | 19 | chart-complex | Hard | 3-panel stacked chart (NLL, MSE, Value) |
| doc02-V01 | 02 | 5 | diagram | Easy | SinglePath MDP state diagram |
| doc04-V01 | 04 | 8 | chart-complex | Hard | 8-panel grid of line charts, usage trends |
| doc04-V03 | 04 | 13 | chart-simple | Easy | Top 20 countries horizontal bar chart |
| doc04-V05 | 04 | 15 | chart-complex | Hard | World choropleth map by AI Usage Index |
| doc04-V06 | 04 | 17 | chart-complex | Hard | Income vs AUI scatter plot, log scale |
| doc04-V09 | 04 | 22 | chart-complex | Hard | 4-panel scatter plots by occupation |
| doc04-V10 | 04 | 23 | infographic | Medium | Overrepresented request clusters, 4 panels |
| doc04-V17 | 04 | 35 | chart-complex | Hard | 2-panel Lorenz curves + power-law |
| doc04-V18 | 04 | 37 | chart-complex | Hard | 2-panel scatter, automation vs augmentation |
| doc04-V22 | 04 | 43 | chart-complex | Hard | Partial regression scatter plot |
| doc05-R02 | 05 | 3 | screenshot | Hard | Handwritten physics problem + model response |
| doc05-R03 | 05 | 4 | diagram | Medium | Gemini architecture overview, Transformer decoder |
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
| doc06-R07 | 06 | 4 | screenshot | Medium | CCS annotation UI with bounding boxes (1120x1512) |
| doc06-R09 | 06 | 5 | screenshot | Medium | Figure 4 example: annotation alternative (representative of 8) |
| doc06-R17 | 06 | 9 | screenshot | Medium | Figure 6 example: layout prediction (representative of 6) |
| doc06-V01 | 06 | 3 | chart-simple | Easy | Pie chart of DocLayNet distribution |
| doc11-R01 | 11 | 36 | screenshot | Medium | Tabular TD(0) pseudocode |
| doc11-R04 | 11 | 48 | screenshot | Hard | DQN loss function and gradient |
| doc11-R05 | 11 | 49 | screenshot | Hard | Deep Q-learning with Experience Replay |
| doc11-R10 | 11 | 79 | screenshot | Hard | A3C actor-critic pseudocode |
| doc11-R11 | 11 | 55 | equation | Easy | Softmax policy parameterization |
| doc11-R13 | 11 | 62 | equation | Medium | Actor-critic update with baseline |
| doc12-R03 | 12 | -- | table-image | Medium | North Star Promise Program financial table |
| doc13-R01 | 13 | 1 | table-image | Easy | Aircraft wing specification table (6 models, 7 columns) |
| doc14-R01 | 14 | 1 | table-image | Easy | Spreadsheet cell/format/formula table |
| doc15-R01 | 15 | 1 | table-image | Medium | Color-coded course timetable (SWORD Deadlines) |
| doc16-R02 | 16 | -- | photo | Hard | 9-sub-panel composite: spermatogenesis diagram + microscopy + charts |
| doc16-R03 | 16 | -- | photo | Hard | 7-sub-panel composite: testis cross-section + EM + fluorescence grid |
| doc16-R05 | 16 | -- | photo | Hard | Mitoball ultrastructure at multiple developmental stages |
| doc16-R08 | 16 | -- | photo | Hard | Cross-species comparison panel (8+ insect species) |
| doc18-F1-3 | 18 | 10 | diagram | Medium | Microservices architecture (languages + data stores) |
| doc18-F2-3 | 18 | -- | diagram | Medium | Circuit breaker sequence diagram |
| doc18-F5-2 | 18 | 94 | diagram | Hard | North Star Architecture (DevOps Services) |
| doc18-F5-8 | 18 | 104 | diagram | Hard | Watson Developer Cloud platform (4-layer) |
| doc18-F5-9 | 18 | 105 | diagram | Hard | IaaS++ architecture (multi-zone) |
| doc18-F3-3 | 18 | -- | infographic | Hard | IBM DevOps framework |
| doc19-R01 | 19 | -- | chart-simple | Easy | Pie chart: equipment market share (5 segments) |
| doc19-R06 | 19 | -- | chart-complex | Medium | Multi-line chart: power vs screen area (9 lines) |
| doc19-R07 | 19 | -- | chart-complex | Hard | Multi-line chart: max power vs area (11 lines, annotated) |
| doc19-R09 | 19 | -- | infographic | Easy | Energy rating label: Super Efficiency |

### Subset statistics

**Total selected:** 64 images

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Easy | 14 | 22% |
| Medium | 21 | 33% |
| Hard | 29 | 45% |

| Content Type | Count |
|-------------|-------|
| chart-simple | 6 |
| chart-complex | 14 |
| diagram | 11 |
| table-image | 5 |
| equation | 2 |
| infographic | 7 |
| photo | 9 |
| screenshot | 8 |
| other | 2 |

| Document | Count |
|----------|-------|
| Doc 00 | 1 |
| Doc 01 | 5 |
| Doc 02 | 5 |
| Doc 04 | 8 |
| Doc 05 | 12 |
| Doc 06 | 4 |
| Doc 11 | 6 |
| Doc 12 | 1 |
| Doc 13 | 1 |
| Doc 14 | 1 |
| Doc 15 | 1 |
| Doc 16 | 4 |
| Doc 18 | 6 |
| Doc 19 | 4 |
| **Docs represented** | **14 of 20** |

The subset over-represents hard images (44% vs 30% in corpus) as intended.
Medium and hard together comprise 78% of the subset. All content types
are represented with at least 2 examples. Doc 16 adds hard scientific
microscopy composites, filling the photo+hard gap. Doc 17 equations are
not in the subset (native LaTeX, not raster) but will test equation region
detection during pipeline evaluation.

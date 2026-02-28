# Image Catalog

Master catalog of all images, figures, charts, and diagrams across the
evaluation fixture set. Produced by manual inspection of each document
followed by pipeline extraction comparison.

**Status:** In progress
**Last updated:** 2026-02-27


## Fixture Index

| ID | Filename | Format | Pages | Category | Cataloged? |
|----|----------|--------|-------|----------|------------|
| 00 | 00_gemini3_pro_model_card.pdf | PDF | 9 | text-heavy | Yes |
| 01 | 01_gpt4_system_card.pdf | PDF | 60 | vector-heavy | Yes |
| 02 | 02_icml2019_importance_sampling.pdf | PDF | 19 | multi-image | Yes |
| 03 | 03_imf_economic_impacts_ai.pdf | PDF | 69 | text-heavy | Yes |
| 04 | 04_anthropic_economic_index.pdf | PDF | 47 | vector-heavy | Yes |
| 05 | 05_gemini_multimodal_report.pdf | PDF | 90 | multi-image | Yes |
| 06 | 06_arxiv_2206_01062.pdf | PDF | ~15 | multi-image | No |
| 07 | 07_epa_sample_letter.pdf | PDF | 1 | scanned | No |
| 08 | 08_xerox_mfp_scan_forestburg.pdf | PDF | 5 | scanned | No |
| 09 | 09_archive_newspaper_1948.pdf | PDF | 6 | mixed-content | No |
| 10 | 10_medrxiv_llama4_benchmark.docx | DOCX | n/a | text-only | No |
| 11 | 11_policy_gradient_rl_lecture.pptx | PPTX | ~30 | multi-image | No |

**Other files** (moved to `fixtures/other/`, not part of evaluation):
- `medrxiv_llm_imaging_eval.xlsx` -- tabular data, no images


## Content Type Legend

| Type | Description |
|------|-------------|
| chart-simple | Bar, pie, single-line chart with clear labels |
| chart-complex | Multi-series, stacked, scatter with dense data |
| diagram | Architecture, flow, process, system diagrams |
| table-image | Screenshot or figure of a table (not extracted table) |
| equation | Mathematical notation rendered as image |
| infographic | Mixed visual with text, icons, data, layout |
| photo | Photograph or natural image |
| decorative | Logo, icon, separator, decorative element |
| screenshot | UI screenshot, terminal output, code |
| other | Anything that does not fit above |


## Gap Tracker

Content types or difficulty levels that need more representation. Updated
as documents are cataloged.

| Gap | Description | Status |
|-----|-------------|--------|
| TBD | Populated after cataloging | -- |


---


## Doc 00: gemini3_pro_model_card.pdf

**Format:** PDF, 9 pages
**Category:** text-heavy (recategorized from multi-image)
**Source:** Google DeepMind Gemini 3 Pro model card

### Embedded Images

Verified via pypdfium2 PDF object inspection (image object type = 3).

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | decorative | 837x13 | Black horizontal bar under header | Thin decorative line rendered as image |
| 2 | 1 | decorative | 932x312 | Google logo at top of title page | Small, top-left; colored Google wordmark |
| 3 | 5 | table-image | 2048x1872 | Benchmark comparison table -- Gemini 3 Pro vs Gemini 2.5 Pro, Claude Sonnet 4.5, GPT-5.1 across ~22 benchmarks | Large image spanning most of page; rendered as raster image, NOT a native text table |

**Total embedded images:** 3 (2 decorative, 1 table-image)
**Pages with image objects:** 1, 5
**Pages with no image objects:** 2-4, 6-9

### Tables (native text)

| # | Page | Rows | Cols | Description | Notes |
|---|------|------|------|-------------|-------|
| 1 | 7 | 5 | 3 | Safety evaluation results -- Gemini 3 Pro vs Gemini 2.5 Pro across Text Safety, Multilingual Safety, Image Safety, Tone, Unjustified-refusals | Color-coded percentages: green for improvements, red for regressions; native text table (no image objects on page) |
| 2 | 9 | 5 | 4 | Frontier Safety evaluation -- Domain (CBRN, Cybersecurity, Harmful Manipulation, ML R&D, Misalignment) with CCL levels and whether CCL was reached | Native text table (no image objects on page); all domains show "CCL not reached" |

**Total native tables:** 2

### Summary

Estimated count in fixtures/README.md was ~15 -- actual is 3 embedded
images (2 decorative + 1 table rendered as image). The benchmark table on
page 5 is an embedded raster image (2048x1872 px), while the tables on
pages 7 and 9 are native text tables. Verified by inspecting PDF page
objects with pypdfium2: pages 2-4 and 6-9 contain zero image objects.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 01: gpt4_system_card.pdf

**Format:** PDF, 60 pages
**Category:** vector-heavy
**Source:** OpenAI GPT-4 System Card

### Embedded Images

Verified via pypdfium2 PDF object inspection. Also recursed into Form
XObjects -- no nested images found on any page.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 58 | chart-complex | 1448x1317 | Figure 11: Heatmap -- "Results on IF evaluations across GPT3.5, GPT3.5-Turbo, GPT-4-launch" with 3x3 color-coded grid (Win rate vs Lose rate) | Only raster image in entire document; color-coded cells (purple, teal, green, yellow); percentage values 29.8%-70.2% |

**Total embedded images:** 1
**Pages with image objects:** 58
**Pages with no image objects:** 1-57, 59-60

### Vector Figures (PATH + TEXT + FORM, no raster image objects)

These are labeled figures in the document drawn entirely with vector paths,
text objects, and form XObjects. They are NOT embedded images. The pipeline
may or may not extract these as picture elements depending on how it
classifies vector content.

| # | Page | Content Type | Label | Description | Object Counts |
|---|------|-------------|-------|-------------|---------------|
| 1 | 8 | infographic | Figure 1 | Harmful content examples -- 3-column layout (Prompt / GPT-4-early / GPT-4-launch) with 7 prompt-response pairs, color-coded boxes | 1 FORM, 85 PATH, 99 TEXT |
| 2 | 9 | infographic | Figure 2 | Non-adversarial bias example about marriage -- 3-column prompt-response comparison | 1 FORM, 13 PATH, 72 TEXT |
| 3 | 10 | infographic | Figure 3 | Biased content examples -- 3-column layout, 2 prompt-response pairs | 1 FORM, 26 PATH, 93 TEXT |
| 4 | 11 | infographic | Figure 4 | Disinformation/influence operation examples -- 3-column layout, 3 prompt-response pairs | 1 FORM, 37 PATH, 82 TEXT |
| 5 | 13 | infographic | (unlabeled) | Dual-use substance prompt + GPT-4 (launch) response about anthrax toxin sequences -- 2-box layout with colored headers | 1 FORM, 10 PATH, 50 TEXT |
| 6 | 14 | infographic | (unlabeled) | Cybersecurity penetration testing prompt + GPT-4 (launch) vulnerability analysis -- 2-box layout with colored headers | 1 FORM, 9 PATH, 63 TEXT |
| 7 | 17 | infographic | Figure 5 | Tool-augmented risky task -- large prompt box + GPT-4-early chain-of-thought (chemical compound search) | 1 FORM, 9 PATH, 39 TEXT |
| 8 | 23 | infographic | Figure 6 | Example RBRM prompt -- styled text boxes with colored headers showing classification prompt and example output | 8 FORM, 38 PATH, 80 TEXT (shared page with Figure 7) |
| 9 | 23 | chart-simple | Figure 7 | Bar chart -- "Incorrect Behavior Rate on Disallowed and Sensitive Content" comparing 3 models | Vector-drawn chart; grouped bars with error bars (shared page with Figure 6) |
| 10 | 25 | chart-simple | Figure 8 | Bar chart -- "Accuracy on adversarial questions (TruthfulQA mc1)" across prompting variants | 17 FORM, 44 PATH, 46 TEXT; vector-drawn grouped bars |
| 11 | 27 | infographic | Figure 9 | Example prompt for GPT-4 classification in natural language -- content policy rubric and example classification | 1 FORM, 9 PATH, 40 TEXT |
| 12 | 28 | infographic | Figure 10 | "Jailbreaks" for GPT-4-launch -- 2 attack types with 3-column layout | 1 FORM, 25 PATH, 94 TEXT |

**Total vector figures:** 12 (8 infographic, 2 chart-simple drawn as vectors, 2 unlabeled)

### Tables (native text)

No native data tables found in this document. The appendices (pages 40-60)
contain bordered text boxes (RBRM prompts, prompt/response examples) that
use PATH objects for borders, but these are formatted text content, not
structured data tables.

### Summary

Estimated count in fixtures/README.md was ~10. The document contains 11
explicitly labeled figures (Figures 1-11) plus 2 unlabeled inline
prompt/response boxes (pages 13-14). However, only Figure 11 (the heatmap
on page 58) is an actual embedded raster image. All other figures (1-10
plus the unlabeled boxes) are drawn entirely with vector graphics (PATH,
TEXT, FORM objects). The bar charts on pages 23 and 25 are vector-drawn,
not raster images. This means the pipeline's image extraction depends
heavily on how Docling classifies vector content vs raster content.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 02: icml2019_importance_sampling.pdf

**Format:** PDF, 19 pages
**Category:** multi-image
**Source:** ICML 2019 -- "Importance Sampling Policy Evaluation with an Estimated Behavior Policy"

### Embedded Images

Verified via pypdfium2 PDF object inspection. No nested images found
inside Form XObjects on any page.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 6 | chart-complex | 1350x1200 | Figure 2a: Gridworld -- MSE vs number of trajectories for RIS, EIS, BIS, OIS, DR, WDR methods | Multi-series line chart with confidence bands |
| 2 | 6 | chart-complex | 1350x1200 | Figure 2b: Gridworld Alt. -- same metrics as 2a with alternative weighting | Multi-series line chart |
| 3 | 6 | chart-complex | 1350x1200 | Figure 2c: Gridworld On-Policy -- on-policy variant of Gridworld evaluation | Multi-series line chart |
| 4 | 6 | chart-complex | 1350x1200 | Figure 2d: Gridworld On-Policy Alt. -- alternative on-policy weighting | Multi-series line chart |
| 5 | 6 | chart-complex | 1350x1200 | Figure 3: Off-policy estimation in the SinglePath MDP -- RIS and EIS curves vs trajectories | Larger than Figure 2 subfigures (164x146 pts vs 112x100 pts on page) |
| 6 | 6 | chart-complex | 1350x1200 | Figure 4a: Linear dynamical system results -- MSE vs trajectories | Multi-series line chart |
| 7 | 6 | chart-complex | 1350x1200 | Figure 4b: Linear dynamical system alternative weights | Multi-series line chart |
| 8 | 7 | chart-simple | 1800x1600 | Figure 5a: Hopper -- MSE bar chart comparing neural network architectures (specified # layers x # units) | Grouped bar chart with error bars |
| 9 | 7 | chart-simple | 1800x1600 | Figure 5b: HalfCheetah -- same architecture comparison as 5a | Grouped bar chart with error bars |
| 10 | 7 | chart-complex | 1350x1200 | Figure 6: Mean squared error and estimate of importance sampling during training -- 3-panel vertical chart (error, squared error, estimate) | Multi-panel training curves; larger on page (199x177 pts) |
| 11 | 16 | chart-simple | 386x252 | Figure 7a: Policy and Reward -- continuous bandit evaluation | Line chart; notably smaller pixel size than other figures |
| 12 | 16 | chart-simple | 386x252 | Figure 7b: 10 Sample Approximation -- bandit policy approximation | Line chart; same small pixel size |
| 13 | 16 | chart-simple | 386x252 | Figure 7c: 200 Sample Approximation -- bandit policy with more samples | Line chart; same small pixel size |
| 14 | 18 | chart-complex | 1350x1200 | Figure 9a: Gridworld Off-Policy -- EIS variant comparison, MSE vs trajectories | Multi-series line chart |
| 15 | 18 | chart-complex | 1350x1200 | Figure 9b: Gridworld On-Policy -- EIS variant comparison | Multi-series line chart |
| 16 | 19 | chart-complex | 1350x1200 | Figure 10: MSE and estimate of importance sampling estimator during training of pi_D -- 3 stacked panels (Neg. Log Likelihood, MSE, Value) | RIS vs OIS vs True Value; largest on-page rendering (316x281 pts) |

**Total embedded images:** 16 (9 chart-complex, 7 chart-simple)
**Pages with image objects:** 6, 7, 16, 18, 19
**Pages with no image objects:** 1-5, 8-15, 17

### Vector Figures (PATH + TEXT + FORM, no raster image objects)

| # | Page | Content Type | Label | Description | Object Counts |
|---|------|-------------|-------|-------------|---------------|
| 1 | 5 | diagram | Figure 1 | SinglePath MDP state diagram -- states s0 through s4 with action transitions a0, a1; circles connected by arrows | 3 FORM, 18 PATH, 3 SHADING |
| 2 | 16 | diagram | Figure 8 | SinglePath MDP diagram (same as Figure 1) -- referenced in Section 4 of the main text | 3 FORM, 17 PATH, 3 SHADING (shared page with Figure 7 raster images) |

**Total vector figures:** 2 (both diagrams of the same MDP)

### Tables (native text)

| # | Page | Rows | Cols | Description | Notes |
|---|------|------|------|-------------|-------|
| 1 | 17 | 3 | 3 | Table 1: State and action dimensions for each OpenAI Robotseed environment -- Hopper (11 state, 3 action), HalfCheetah (17 state, 6 action) | Native text table (no image objects on page); 9 PATH objects for borders/formatting |

**Total native tables:** 1

### Summary

Estimated count in fixtures/README.md was ~8. Actual count is 16 embedded
raster images across 10 labeled figures (Figures 2-7, 9-10), plus 2 vector-
drawn diagrams (Figures 1 and 8, both showing the same SinglePath MDP), and
1 native text table (Table 1). All raster images are line charts or bar
charts from reinforcement learning experiments. Figure 7 subfigures are
notably lower resolution (386x252 px) compared to other figures (1350x1200
or 1800x1600 px). Pages 3, 12-14 have vector PATH objects for mathematical
equation formatting only (no visual figures).

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 03: imf_economic_impacts_ai.pdf

**Format:** PDF, 69 pages
**Category:** text-heavy
**Source:** IMF Working Paper WP/24/65 -- "The Economic Impacts and the Regulation of AI: A Review of the Academic Literature and Policy Actions"

### Embedded Images

Verified via pypdfium2 PDF object inspection. Also recursed into Form
XObjects -- no nested images found on any page.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | decorative | 1633x2113 | Cover page background -- gray gradient with IMF logo, title text, and "Working Paper" sidebar | Full-page raster image (612x792 pts = entire page); text and paths overlaid on top |
| 2 | 69 | decorative | 1633x2113 | Back cover -- solid blue background with IMF Publications logo and paper title | Full-page raster image (612x792 pts = entire page) |

**Total embedded images:** 2 (both decorative)
**Pages with image objects:** 1, 69
**Pages with no image objects:** 2-68

### Vector Figures

No vector figures found. Pages 2 (48 PATH), 37 (22 PATH), and 58 (52
PATH) have elevated PATH counts, but these are formatting rules, table
borders, and styled text elements -- not labeled figures.

**Total vector figures:** 0

### Tables (native text)

| # | Page | Rows | Cols | Description | Notes |
|---|------|------|------|-------------|-------|
| 1 | 37 | 4 | ~10 | Table 1: AI-Specific Regulations in selected AEs and China -- EU AI Act, US Executive Order, China Interim Measures compared across approach, coverage, and policy domains (innovation, privacy, copyright, military, ethics) | Color-coded cells with checkmarks; 22 PATH objects for borders/fills; 1 FORM object |
| 2 | 58 | 5 | 2 | Table 2: AI definition in regulation -- formal AI definitions from EU (AI Act 2021 proposal), US (Bill of Rights + Executive Order), China (Interim Measures Art. 2), UK (White Paper 3.2.1) | Appendix A.1; simple 2-column layout (Country, Definition) with long-form text in definition cells; 52 PATH objects for borders |

**Total native tables:** 2

### Summary

Estimated count in fixtures/README.md was ~5. Actual count is 2 embedded
raster images, both full-page decorative backgrounds (cover and back
cover). The document contains zero content images -- no charts, diagrams,
or figures of any kind. It is a 69-page academic literature review
consisting almost entirely of prose text with footnotes. The only
structured content is 2 native text tables in the body (page 37) and
appendix (page 58). Pages 3-68 (excluding 37 and 58) are pure text.
Category recategorized from "multi-image" to "text-heavy".

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 04: anthropic_economic_index.pdf

**Format:** PDF, 47 pages
**Category:** vector-heavy
**Source:** Anthropic -- "The Anthropic Economic Index report: Uneven geographic and enterprise AI adoption" (September 2025)

### Embedded Images

Verified via pypdfium2 PDF object inspection. Also recursed into Form
XObjects -- no nested images found on any page.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 17 | decorative | 20x397 | Gradient color bar element within Figure 2.4 scatter plot | Extremely thin raster element embedded in vector figure |
| 2 | 27 | decorative | 11x248 | Gradient color bar element within Figure 2.11 scatter plot | Extremely thin raster element embedded in vector figure |

**Total embedded images:** 2 (both decorative gradient elements within vector figures)
**Pages with image objects:** 17, 27
**Pages with no image objects:** 1-16, 18-26, 28-47

### Vector Figures (PATH + TEXT + FORM, no raster image objects)

All 22 figures in this document are drawn entirely with vector graphics.

| # | Page | Content Type | Label | Description | Object Counts |
|---|------|-------------|-------|-------------|---------------|
| 1 | 8 | chart-complex | Figure 1.1 | Claude.ai usage over time -- 8-panel grid of line charts showing usage share trends across major occupation groups (V1 to V3) | 9 FORM, 330 PATH |
| 2 | 10 | chart-complex | Figure 1.2 | Collaboration mode frequencies across Anthropic Economic Index Reports -- 2-panel: automation vs augmentation trends (left), individual interaction types (right) | 2 FORM, 127 PATH |
| 3 | 13 | chart-simple | Figure 2.1 | Top 20 countries by share of global Claude.ai usage share -- horizontal orange bar chart | 1 FORM, 142 PATH |
| 4 | 14 | chart-simple | Figure 2.2 | Top 20 countries by Anthropic AI Usage Index (per capita) -- horizontal orange bar chart; Israel leads | 1 FORM, 115 PATH |
| 5 | 15 | chart-complex | Figure 2.3 | Claude diffusion varies across continents -- world choropleth map color-coded by AI Usage Index tiers | 17 FORM, 8126 PATH |
| 6 | 17 | chart-complex | Figure 2.4 | Income and Anthropic AI Usage Index by country -- scatter plot with regression line, log scale GDP per working-age capita vs AUI | 117 FORM, 68 PATH (+1 IMAGE gradient bar) |
| 7 | 19 | chart-simple | Figure 2.5 | Top 30 US states by Anthropic AI Usage Index -- horizontal orange bar chart; DC leads | 1 FORM, 103 PATH |
| 8 | 20 | chart-complex | Figure 2.6 | Claude usage varies across US states -- US choropleth map color-coded by per-capita usage tiers | 14 FORM, 563 PATH |
| 9 | 22 | chart-complex | Figure 2.7 | Usage pattern shifts from lower to higher adoption countries -- 4-panel scatter plots by occupation group (Computer/Math, Education, Arts/Design, Office/Admin) | 331 FORM, 862 PATH |
| 10 | 23 | infographic | Figure 2.8 | Overrepresented request clusters for US, Brazil, Vietnam, India -- 4-panel styled data boxes with top request categories and percentages | 1 FORM, 11 PATH |
| 11 | 25 | infographic | Figure 2.9 | Overrepresented request categories for California, Texas, Florida, South Carolina -- 4-panel styled data boxes | 1 FORM, 11 PATH |
| 12 | 26 | infographic | Figure 2.10 | Washington DC highest Claude usage per capita -- 2-panel styled data boxes showing top O*NET tasks and request clusters | 1 FORM, 6 PATH |
| 13 | 27 | chart-complex | Figure 2.11 | Countries with higher AI Usage Index tend to use Claude more collaboratively -- scatter plot with regression, augmentation share vs AUI residuals | 113 FORM, 82 PATH (+1 IMAGE gradient bar) |
| 14 | 32 | chart-simple | Figure 3.1 | AI adoption rates among US firms (Census Business Trends & Outlook Survey) -- line chart with trend line | 2 FORM, 157 PATH |
| 15 | 33 | chart-simple | Figure 3.2 | Bottom-up taxonomy of Claude usage among sampled 1P API transcripts -- horizontal stacked bar chart by use case category | 16 FORM, 101 PATH |
| 16 | 34 | chart-complex | Figure 3.3 | Leading occupational categories by overall usage: Claude.ai vs 1P API -- grouped horizontal bar chart comparing two platforms | 2 FORM, 64 PATH |
| 17 | 35 | chart-complex | Figure 3.4 | Concentration of usage among tasks -- 2-panel: Lorenz curves (left) and power-law task rank vs usage share (right) | 289 FORM, 665 PATH |
| 18 | 37 | chart-complex | Figure 3.5 | Automation vs augmentation collaboration modes across O*NET tasks -- 2-panel scatter plots with labeled task clusters | 3558 FORM, 7194 PATH |
| 19 | 39 | chart-simple | Figure 3.6 | Average output token index across leading occupational categories -- horizontal orange bar chart | 7 FORM, 56 PATH |
| 20 | 40 | chart-complex | Figure 3.7 | Output token index vs input token index across O*NET tasks -- scatter plot with regression line | 2062 FORM, 4178 PATH |
| 21 | 42 | chart-complex | Figure 3.8 | API cost per task and usage share across occupational categories -- scatter plot with regression | 45 FORM, 57 PATH |
| 22 | 43 | chart-complex | Figure 3.9 | API cost per task vs usage share controlling for task characteristics -- partial regression scatter plot | 1334 FORM, 2723 PATH |

**Total vector figures:** 22 (6 chart-simple, 13 chart-complex, 3 infographic)

### Tables (native text)

| # | Page | Rows | Cols | Description | Notes |
|---|------|------|------|-------------|-------|
| 1 | 15 | 6 | 4 | Table 2.1: Anthropic Economic Index tiers with examples, number of countries, and AUI range -- Leading top 25%, Upper middle, Lower middle, Emerging bottom 25%, Minimal | Shares page with Figure 2.3 world map; color-coded tier rows |
| 2 | 20 | 6 | 4 | Table 2.2: Claude per capita usage tiers for US states -- similar tier structure as Table 2.1 applied to states | Shares page with Figure 2.6 US map |
| 3 | 38 | 3 | 3 | Table 3.1: Example O*NET tasks with shorter and longer output lengths with Claude summaries -- shows 90th and 10th percentile examples with Claude task descriptions | Styled comparison layout with colored category headers |

**Total native tables:** 3

### Summary

Estimated count in fixtures/README.md was ~30. The document contains 22
labeled figures (Figures 1.1-1.2, 2.1-2.11, 3.1-3.9) plus 3 native text
tables. However, ALL 22 figures are drawn entirely with vector graphics
(PATH + FORM objects) -- the only 2 raster IMAGE objects in the entire
47-page document are tiny gradient color bars (20x397 and 11x248 px)
embedded within scatter plot figures. Several figures have extremely high
vector complexity: Figure 3.5 (7194 PATH, 3558 FORM) and Figure 3.7
(4178 PATH, 2062 FORM) are scatter plots with hundreds of individually
drawn data points. The pipeline's ability to extract these figures depends
entirely on how it handles vector-drawn content. Category set to
"vector-heavy".

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 05: gemini_multimodal_report.pdf

**Format:** PDF, 90 pages
**Category:** multi-image
**Source:** Google DeepMind -- "Gemini: A Family of Highly Capable Multimodal Models"

### Embedded Images

Verified via pypdfium2 PDF object inspection. Recursed into Form XObjects
-- 1 nested image found on page 21.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | decorative | 3810x512 | Thin decorative bar across header | 90x12 pts on page |
| 2 | 3 | screenshot | 4760x3421 | Figure 1: Student's handwritten physics problem with model verification -- shows handwritten equations and Gemini response | Large composite prompt+response figure |
| 3 | 4 | diagram | 1383x617 | Figure 2: Overview of the Gemini 1.0 model family -- architecture diagram showing interleaved text/image/audio/video inputs with Transformer decoder | 424x189 pts |
| 4 | 15 | screenshot | 4760x5014 | Figure 5: Multimodal reasoning for matplotlib code generation -- prompt with subplot charts, rendered code, and rearranged output | Largest image in document; composite of code + chart renders |
| 5 | 17 | decorative | 20x397 | Thin gradient element within Figure 6 layout | Figure 6 content (AI-generated images) appears embedded in FORM objects beyond scan depth |
| 6 | 19 | photo | 4080x3072 | Table 13 image 1: Cooking omelet -- overhead photo of omelet in pan (early stage) | Within audio-visual qualitative example table; 99x75 pts on page |
| 7 | 19 | photo | 3069x3021 | Table 13 image 2: Cooking omelet -- omelet partially cooked | 99x98 pts |
| 8 | 19 | photo | 4080x3072 | Table 13 image 3: Cooking omelet -- finished omelet on plate | 99x75 pts |
| 9 | 21 | decorative | 560x560 | Small icon element within Figure 7 flowchart diagram | 30x30 pts; Figure 7 is primarily vector |
| 10 | 21 | decorative | (nested) | Additional icon nested inside FORM object in Figure 7 | Found via FORM recursion |
| 11 | 78 | photo | 1170x1560 | Figure 11: Persian shield plant -- multimodal question answering example, recognizes tropical plant species | 176x234 pts |
| 12 | 79 | photo | 256x256 | Figure 12 image 1: Goldendoodle dog at beach -- interleaved text and image generation | 132x132 pts |
| 13 | 79 | photo | 256x256 | Figure 12 image 2: Goldendoodle in city | 132x132 pts |
| 14 | 79 | photo | 256x256 | Figure 12 image 3: Goldendoodle portrait | 132x132 pts |
| 15 | 80 | photo | 4080x3072 | Figure 13: Handwritten shapes sequence (triangle, square, pentagon, ?) -- multimodal reasoning problem | 214x161 pts |
| 16 | 81 | diagram | 539x158 | Figure 14: Parallelogram with dimensions (x, s, 15) -- geometrical reasoning task | 257x75 pts |
| 17 | 81 | photo | 514x510 | Figure 15 image 1: Moon photograph -- puzzle input for finding connection between objects | 107x106 pts |
| 18 | 81 | photo | 672x370 | Figure 15 image 2: Golf balls on lunar surface -- second puzzle input | 193x106 pts |
| 19 | 82 | photo | 2072x1560 | Figure 16: NYC street at night with Empire State Building -- visual location identification | 257x194 pts |
| 20 | 83 | other | 1521x2046 | Figure 17: Internet meme ("Game at 300 FPS / 75 Hz Monitor") -- humor understanding example | 257x346 pts |
| 21 | 84 | diagram | 493x512 | Figure 18: Chinese family tree diagram with character labels -- commonsense reasoning in multilingual setting | 257x267 pts |
| 22 | 86 | screenshot | 512x271 | Figure 19: Rendered "Opossum Search" website -- code generation output rendered in browser | 351x186 pts; code on page 85 (vector) |
| 23 | 89 | chart-complex | 512x506 | Figure 22 image 1: 4 matplotlib subplots (sin, multi-line, 3D surface, contour) -- inverse graphics prompt | 220x217 pts |
| 24 | 89 | chart-simple | 512x327 | Figure 22 image 2: Rendered output plot (exponential curve) -- model's code output | 176x112 pts |
| 25 | 90 | photo | 480x270 | Figure 23 frame 1: Soccer penalty kick video -- player approaching ball | 176x99 pts |
| 26 | 90 | photo | 480x270 | Figure 23 frame 2: Soccer kick in progress | 176x99 pts |
| 27 | 90 | photo | 480x270 | Figure 23 frame 3: Ball in flight toward goal | 176x99 pts |
| 28 | 90 | photo | 480x270 | Figure 23 frame 4: Post-kick follow-through | 176x99 pts |

**Total embedded images:** 28 (11 photo, 4 screenshot/diagram, 2 chart, 4 decorative, 7 other content)
**Pages with image objects:** 1, 3, 4, 15, 17, 19, 21, 78-84, 86, 89-90

### Vector Figures (PATH + TEXT + FORM, no raster image objects)

| # | Page | Content Type | Label | Description | Object Counts |
|---|------|-------------|-------|-------------|---------------|
| 1 | 9 | chart-simple | Figure 3 | Language understanding and generation performance of Gemini model family -- grouped bar chart across capabilities | 1 FORM, 54 PATH |
| 2 | 11 | chart-simple | Figure 4 | Negative log likelihood as a function of token index across 32K context -- line chart | 1 FORM, 53 PATH |
| 3 | 21 | diagram | Figure 7 | Modeling overview -- post-training data flywheel with SFT, RM Training, RL fine-tuning stages | 7 FORM, 40 PATH (+2 small raster icons) |
| 4 | 23 | diagram | Figure 8 | Gemini tool-use control loop -- flowchart with Gemini Apps, API modes, Extensions | 1 FORM, 33 PATH |
| 5 | 74 | chart-simple | Figure 9 | Chain-of-Thought with uncertainty routing on MMLU -- grouped bar chart, GPT-4 vs Gemini Ultra | 1 FORM, 31 PATH |
| 6 | 77 | infographic | Figure 10 | Multimodal chart understanding problem -- prompt with horizontal bar charts about plastic waste by country + model response with markdown table | 17 FORM, 159 PATH |
| 7 | 87 | other | Figure 20 | Solving a calculus problem -- text-based math with model solution | 15 PATH |
| 8 | 88 | other | Figure 21 | Solving a multi-step math problem -- factory production with rendered table response | 37 PATH |

**Total vector figures:** 8 (3 chart-simple, 2 diagram, 1 infographic, 2 other)

Note: Figure 6 (page 17), Figure 10 (page 77), and Figures 20-21 (pages
87-88) contain visual content that appears to be encoded within deeply
nested FORM objects beyond the scan's 1-level recursion depth. The scan
reports only the top-level and first-nested objects.

### Tables (native text)

This document contains 18 numbered tables (Tables 1-18), most of which
are benchmark result tables. Only the most notable are listed here.

| # | Page | Rows | Cols | Description | Notes |
|---|------|------|------|-------------|-------|
| 1 | 4 | 4 | 2 | Table 1: Gemini model family overview -- Ultra, Pro, Nano with model descriptions | Shares page with Figure 2 (raster) |
| 2 | 8 | ~15 | 7 | Table 2: Gemini performance on text benchmarks vs GPT-4, PaLM 2-L, Claude 2, LLaMA-2 | Large benchmark comparison; 23 PATH for borders |
| 3 | 13 | ~12 | 7 | Table 7: Image understanding -- Gemini Ultra vs existing approaches on vision benchmarks | 17 PATH |
| 4 | 19 | 4 | 3 | Table 13: Audio-visual qualitative example -- omelet cooking with interleaved text, images, and audio | Contains 3 embedded raster photos |

**Total numbered tables:** 18 (Tables 1-18)
**Pages with tables:** 4, 8, 9, 10, 12, 13, 14, 16, 18, 19, 22, 23, 24, 25, 26

Additional unlabeled table-like structures: Model cards in Appendix
(pages 71-73) for Gemini Ultra, Pro, and Nano.

### Summary

Estimated count in fixtures/README.md was ~40. The document contains 23
labeled figures (Figures 1-23) and 18 labeled tables (Tables 1-18). Of the
23 figures, 15 contain raster image content (photos, screenshots, diagrams,
charts) totaling 28 IMAGE objects, while 8 are vector-drawn (charts,
diagrams, flowcharts). The document is unusual in that many figures in the
appendix (pages 77-90) showcase multimodal capabilities with embedded
photos, memes, video frames, and handwritten content -- making this a
diverse test case for image extraction. Table 13 uniquely combines a native
text table structure with embedded raster images. Some figures (notably
Figure 6 on page 17) appear to have image content encoded in deeply nested
FORM objects that the 1-level scan does not reach.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 06: arxiv_2206_01062.pdf

*Pending inspection*


---


## Doc 07: epa_sample_letter.pdf

*Pending inspection*


---


## Doc 08: xerox_mfp_scan_forestburg.pdf

*Pending inspection*


---


## Doc 09: archive_newspaper_1948.pdf

*Pending inspection*


---


## Doc 10: medrxiv_llama4_benchmark.docx

*Pending inspection*


---


## Doc 11: policy_gradient_rl_lecture.pptx

*Pending inspection*

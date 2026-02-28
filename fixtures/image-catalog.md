# Image Catalog

Master catalog of all images, figures, charts, and diagrams across the
evaluation fixture set. Produced by manual inspection of each document
followed by pipeline extraction comparison.

**Status:** Cataloging complete (all 18 fixtures inspected)
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
| 06 | 06_arxiv_2206_01062.pdf | PDF | 9 | multi-image | Yes |
| 07 | 07_epa_sample_letter.pdf | PDF | 3 | scanned | Yes |
| 08 | 08_xerox_mfp_scan_forestburg.pdf | PDF | 5 | scanned | Yes |
| 09 | 09_archive_newspaper_1948.pdf | PDF | 6 | mixed-content | Yes |
| 10 | 10_medrxiv_llama4_benchmark.docx | DOCX | n/a | text-only | Yes |
| 11 | 11_policy_gradient_rl_lecture.pptx | PPTX | 80 | multi-image | Yes |
| 12 | 12_minnstate_fy2025_budget.pptx | PPTX | 17 | multi-image | Yes |
| 13 | 13_artpro_table.webp | WebP | 1 | table-image | Yes |
| 14 | 14_simple_table.png | PNG | 1 | table-image | Yes |
| 15 | 15_timetable.jpg | JPG | 1 | table-image | Yes |
| 16 | 16_cambridge_mitoball_biology.docx | DOCX | n/a | multi-image | Yes |
| 17 | 17_arxiv_fractional_brownian_sde.pdf | PDF | 24 | text-heavy | Yes |
| 18 | 18_ibm_microservices_redbook.pdf | PDF | 170 | multi-image | Yes |
| 19 | 19_cris_electronic_screens_2023.docx | DOCX | n/a | multi-image | Yes |

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
| Infographics | Only Doc 01 (GPT-4) and Doc 04 (Anthropic) have infographic-style figures; limited variety | Open |
| Photos (non-scanned) | Doc 05 has consumer photos; Doc 16 adds scientific microscopy | Improved |
| Diagrams | Docs 02, 05 have structured diagrams; Doc 18 adds ~27 architecture diagrams (component, sequence, deployment, topology) | Covered |
| Equations as images | Doc 11 has 4 rendered equations; Doc 17 adds 63 native LaTeX equations across 24 pages | Covered |
| DOCX with images | Doc 16 adds 8 scientific figures in DOCX format | Covered |
| chart-simple raster | Docs 02 and 05 have raster charts; Docs 01 and 04 charts are all vector | Covered |
| Algorithm pseudocode | Doc 11 has 10 algorithm screenshots; single content type in entire PPTX | Covered |
| Scanned documents | Docs 07-09 cover letter, form, and newspaper; good variety | Covered |
| Table-as-image | Docs 12-15 add 4 table-image examples (was 1); now 5 total across 4 docs | Covered |

### Corpus Summary

| Category | Docs | Content images | Decorative | Vector figures | Tables |
|----------|------|---------------|------------|----------------|--------|
| multi-image | 02, 05, 06, 11, 12, 16, 18, 19 | 121 | 31 | 12 | 24 |
| vector-heavy | 01, 04 | 1 | 2 | 34 | 3 |
| text-heavy | 00, 03, 17 | 1 | 4 | 0 | 4 |
| scanned | 07, 08 | 8 | 0 | 0 | 0 |
| mixed-content | 09 | 6 | 0 | 0 | 0 |
| text-only | 10 | 0 | 0 | 0 | 4 |
| table-image | 13, 14, 15 | 3 | 0 | 0 | 0 |
| **Total** | **20** | **140** | **37** | **46** | **35** |


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

**Format:** PDF, 9 pages
**Category:** multi-image
**Source:** arXiv 2206.01062 -- "DocLayNet: A Large Human-Annotated Dataset for Document-Layout Analysis"

### Embedded Images

Verified via pypdfium2 PDF object inspection. All pages also checked for
nested images inside Form XObjects -- every IMAGE object has a nested
duplicate inside a FORM on the same page.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | screenshot | 271x459 | Figure 1 thumbnail 1: Example document page with colored bounding boxes showing layout categories (text, title, list, table, figure) | Small thumbnail on title page; 28x47 pts |
| 2 | 1 | decorative | 20x20 | Small icon element on title page | Tiny decorative square |
| 3 | 1 | screenshot | 20x20 | Small icon element on title page | Duplicate size of #2 |
| 4 | 1 | screenshot | 140x189 | Figure 1 thumbnail 2: Example annotated document page | Title page thumbnail; 30x40 pts |
| 5 | 1 | screenshot | 140x189 | Figure 1 thumbnail 3: Example annotated document page | Title page thumbnail; duplicate dimensions of #4 |
| 6 | 1 | screenshot | 170x166 | Figure 1 thumbnail 4: Example annotated document page with different layout | Title page thumbnail; 37x36 pts |
| 7 | 4 | screenshot | 1120x1512 | Figure 3: Annotation user interface -- screenshot of the CCS annotation tool showing PDF page with bounding boxes and label palette | Large screenshot; 623x841 pts (nearly full page) |
| 8 | 4 | screenshot | 486x1528 | Annotated PDF pages column -- series of annotated document examples showing different layout categories | 266x837 pts; appears alongside Table 1 |
| 9 | 5 | screenshot | 1025x1025 | Figure 4 example 1: Document page showing plausible annotation alternatives | Part of 2x4 grid of examples |
| 10 | 5 | screenshot | 1025x1025 | Figure 4 example 2: Document page with alternative annotations | 2x4 grid |
| 11 | 5 | screenshot | 1025x1025 | Figure 4 example 3: Document page with alternative annotations | 2x4 grid |
| 12 | 5 | screenshot | 1025x1025 | Figure 4 example 4: Document page with alternative annotations | 2x4 grid |
| 13 | 5 | screenshot | 1025x1025 | Figure 4 example 5: Document page with alternative annotations | 2x4 grid |
| 14 | 5 | screenshot | 1025x1025 | Figure 4 example 6: Document page with alternative annotations | 2x4 grid |
| 15 | 5 | screenshot | 1025x1025 | Figure 4 example 7: Document page with alternative annotations | 2x4 grid |
| 16 | 5 | screenshot | 1025x1025 | Figure 4 example 8: Document page with alternative annotations | 2x4 grid |
| 17 | 5 | decorative | 434x26 | Thin separator bar between Figure 4 rows | 8 identical bars interspersed with the 8 content images |
| 18-23 | 5 | decorative | 434x26 | Additional thin separator bars (x6) | Same as #17 |
| 24 | 5 | decorative | 434x26 | Final separator bar | Same as #17 |
| 25 | 9 | screenshot | 1025x1025 | Figure 6 example 1: Layout prediction on document page with colored bounding boxes | Part of 2x3 grid showing model predictions |
| 26 | 9 | screenshot | 1025x1025 | Figure 6 example 2: Layout prediction on document page | 2x3 grid |
| 27 | 9 | screenshot | 1025x1025 | Figure 6 example 3: Layout prediction on document page | 2x3 grid |
| 28 | 9 | screenshot | 1025x1025 | Figure 6 example 4: Layout prediction on document page | 2x3 grid |
| 29 | 9 | screenshot | 1025x1025 | Figure 6 example 5: Layout prediction on document page | 2x3 grid |
| 30 | 9 | screenshot | 1025x1025 | Figure 6 example 6: Layout prediction on document page | 2x3 grid |

**Total embedded images:** 30 (22 screenshot, 8 decorative)
**Pages with image objects:** 1, 4, 5, 9
**Pages with no image objects:** 2, 3, 6, 7, 8

Note: Each IMAGE object on every page also has an identical nested copy
inside a FORM XObject (6 nested on page 1, 2 nested on page 4, 16 nested
on page 5, 6 nested on page 9).

### Vector Figures (PATH + TEXT + FORM, no raster image objects)

| # | Page | Content Type | Label | Description | Object Counts |
|---|------|-------------|-------|-------------|---------------|
| 1 | 3 | chart-simple | Figure 2 | DocLayNet page distribution by document category -- pie chart showing Financial Reports, Manuals, Scientific Articles, Laws & Regulations, Patents, Government Tenders proportions | 1 FORM, 8 PATH |
| 2 | 6 | chart-complex | Figure 5 | Prediction performance (mAP) comparison across models and label sets -- line chart with multiple series | 19 FORM, 133 PATH |

**Total vector figures:** 2 (1 chart-simple, 1 chart-complex)

### Tables (native text)

| # | Page | Rows | Cols | Description | Notes |
|---|------|------|------|-------------|-------|
| 1 | 4 | ~12 | 6 | Table 1: DocLayNet dataset overview -- label frequencies per document category (Financial Reports, Manuals, etc.) with totals | Shares page with Figure 3 (raster); 82 PATH for borders |
| 2 | 6 | ~8 | 5 | Table 2: Prediction performance (mAP) across models -- Faster R-CNN, Mask R-CNN, YOLO v5 on different label sets | Shares page with Figure 5 (vector); 133 PATH includes both table borders and chart |
| 3 | 7 | ~8 | 5 | Table 3: Effect of pre-training data -- model performance with different pre-training datasets | 103 PATH for borders |
| 4 | 7 | ~6 | 5 | Table 4: Effect of image resolution -- model performance at different DPI settings | Shares page with Table 3 |
| 5 | 8 | ~8 | 6 | Table 5: Cross-dataset prediction performance -- models trained on DocLayNet vs PubLayNet vs DocBank evaluated across datasets | 68 PATH for borders |

**Total native tables:** 5

### Summary

Estimated count in fixtures/README.md was ~5. Actual count is 30 embedded
raster images across 6 labeled figures (Figures 1, 3, 4, 6) and decorative
elements, plus 2 vector-drawn figures (Figures 2 and 5) and 5 native text
tables (Tables 1-5). The document is image-heavy relative to its 9 pages:
Figure 4 alone contributes 16 IMAGE objects (8 content + 8 decorative
separator bars), and Figure 6 contributes 6. All content images are
screenshots of annotated document pages (1025x1025 px each) used to
illustrate layout analysis results. The thin separator bars (434x26 px)
on page 5 are decorative and should be filtered during extraction.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 07: epa_sample_letter.pdf

**Format:** PDF, 3 pages
**Category:** scanned
**Source:** US EPA Office of Ground Water and Drinking Water -- sample letter
to state drinking water administrators about Lead and Copper Rule compliance

### Embedded Images

Verified via pypdfium2 PDF object inspection. No Form XObjects found.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | other | 1275x1650 | Full-page scan: EPA letterhead with agency name, "SAMPLE LETTER" header, date, salutation, and body text about Safe Drinking Water Act compliance | Full page (612x792 pts); page also has 1 TEXT object |
| 2 | 2 | other | 1275x1650 | Full-page scan: continuation of letter body with numbered action items and bulleted policy goals | Full page (612x792 pts); no TEXT objects |
| 3 | 3 | other | 1275x1650 | Full-page scan: closing paragraph, signature block (Joel Beauvais, Deputy Assistant Administrator), "Enclosure" note | Full page (612x792 pts); no TEXT objects; mostly white space |

**Total embedded images:** 3 (all full-page scans)
**Pages with image objects:** 1, 2, 3
**Pages with no image objects:** (none)

### Vector Figures

No vector figures. No PATH, FORM, or SHADING objects on any page.

**Total vector figures:** 0

### Tables (native text)

No tables. The document is a plain typed letter with no tabular data.

**Total native tables:** 0

### Summary

Listed as 1 page in the fixture index -- actual page count is 3. This is a
classic scanned document: each page consists of a single full-page raster
image (1275x1650 px at ~150 DPI) with no native text, vector, or structured
content. Page 1 has one TEXT object (possibly from partial OCR) but pages 2-3
are pure image. The content is a government letter with no charts, figures,
or data tables -- only typed prose. Useful as a scanned-document test case
for OCR quality evaluation but provides no image annotation targets.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 08: xerox_mfp_scan_forestburg.pdf

**Format:** PDF, 5 pages
**Category:** scanned
**Source:** Forestburg ISD (Texas) -- scanned employment application package
from a Xerox multifunction printer

### Embedded Images

Verified via pypdfium2 PDF object inspection. No Form XObjects, no TEXT,
no PATH objects on any page -- pure image-only scans.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | other | 2208x1728 | Full-page scan: Personal information form -- Forestburg ISD letterhead with longhorn logo, fields for name, address, phone, employment eligibility | Landscape orientation (795x622 pts); form with blank fields and check boxes |
| 2 | 2 | other | 2208x1728 | Full-page scan: Employment history -- criminal history question, driver's license, 3 repeated employment blocks (company, address, supervisor, dates, reason for leaving) | Structured repeating form layout |
| 3 | 3 | other | 2208x1728 | Full-page scan: References and education -- 3-column references table, education table (school, course, years, degree), military service section | Contains table structures within the scan |
| 4 | 4 | other | 2208x1728 | Full-page scan: DPS Computerized Criminal History (CCH) Verification (Agent Copy) -- legal text about background check process, signature fields | Dense text with form fields at bottom |
| 5 | 5 | other | 2208x1728 | Full-page scan: Criminal History Record Information Addendum -- personal info fields (name, SSN, DOB, sex, ethnicity), signature/date line | Shorter form; mostly white space in lower half |

**Total embedded images:** 5 (all full-page scans)
**Pages with image objects:** 1, 2, 3, 4, 5
**Pages with no image objects:** (none)

### Vector Figures

No vector figures. Zero PATH, FORM, TEXT, or SHADING objects on any page.

**Total vector figures:** 0

### Tables (native text)

No native tables. All tabular structures (employment history blocks,
references table, education table) exist only within the scanned images
and are not extractable as structured data without OCR.

**Total native tables:** 0

### Summary

This is a 5-page scanned employment application from a Xerox MFP scanner.
Every page is a single full-page raster image (2208x1728 px, landscape
at ~200 DPI) with absolutely no native text or vector content. The scans
contain structured form layouts with labeled fields, check boxes, and
tabular sections (employment history, references, education) that exist
only as pixels. Useful as a scanned-form test case: tests OCR accuracy on
form field labels and whether the pipeline can recognize table-like
structures within scanned images. The Forestburg ISD longhorn logo on
page 1 is a small graphic element within the scan. No annotation targets
for image description -- the content is purely textual forms.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 09: archive_newspaper_1948.pdf

**Format:** PDF, 6 pages
**Category:** mixed-content
**Source:** Daily News-Herald, Upland-Ontario, California, Wednesday
September 1, 1948 (Internet Archive digitized newspaper)

### Embedded Images

Verified via pypdfium2 PDF object inspection. Each page has a single
high-resolution scanned image PLUS an OCR text overlay (600-1300 TEXT
objects per page). No Form XObjects or PATH objects.

| # | Page | Content Type | Pixel Size | Description | Notes |
|---|------|-------------|------------|-------------|-------|
| 1 | 1 | other | 5508x6845 | Full-page scan: Front page -- masthead "Daily News-Herald", headlines ("COAST SHIP TIEUP LOOMS", "China Bars Foreign Planes", "Espionage Rings"), 2 news photos (men at legal proceeding, group photo), multi-column news layout | 1322x1643 pts; ~300 DPI; OCR overlay: 819 TEXT objects |
| 2 | 2 | other | 5484x6832 | Full-page scan: Society/ads page -- "CLUBS..SOCIETY" section, large Safeway grocery ad with prices and illustrations, Weber's ad, marriage licenses column | 1316x1640 pts; ad illustrations embedded in scan |
| 3 | 3 | other | 5484x6832 | Full-page scan: News/services page -- "German Court Releases Nazi Minister Schacht", portrait photo, "Service Information" business directory, Van Heusen shirt ad with illustration | 1316x1640 pts; 936 TEXT objects |
| 4 | 4 | other | 5485x6823 | Full-page scan: Editorial/comics page -- editorials, Berlin march photo, crossword puzzle, 2 comic strips ("Betty and Bob", another strip), community service notice | 1316x1638 pts; 885 TEXT objects |
| 5 | 5 | other | 5485x6823 | Full-page scan: Sports/ads page -- "Rotarians 'Rush' Football Season", woman's portrait (phone numbers ad), theater listings (Granada, Park, California, Valley Drive-In), local business ads | 1316x1638 pts; 697 TEXT objects |
| 6 | 6 | other | 5484x6817 | Full-page scan: Classified ads page -- "CLASSIFIED" banner, dense multi-column listings (for sale, services, real estate, wanted), small ad illustrations | 1316x1636 pts; 1349 TEXT objects (highest) |

**Total embedded images:** 6 (all full-page scans with embedded photos/illustrations)
**Pages with image objects:** 1, 2, 3, 4, 5, 6
**Pages with no image objects:** (none)

### Visual content within scans

The following photos and illustrations exist within the full-page scan
images but are NOT separate image objects in the PDF structure:

- Page 1: 2 news photos (legal proceeding, group photo at event)
- Page 2: Safeway ad illustrations (grocery items), Weber's logo
- Page 3: Portrait photo (man in suit), Van Heusen shirt illustration
- Page 4: Berlin soldiers marching photo, 2 comic strips with panels
- Page 5: Woman's portrait (large, phone numbers ad), theater ad graphics
- Page 6: Small classified ad illustrations, decorative typography

These cannot be individually extracted without region detection within
the full-page scans.

### Vector Figures

No vector figures. Zero PATH or FORM objects on any page.

**Total vector figures:** 0

### Tables (native text)

No native tables. All tabular content (classified ad columns, sports
scores, grocery price lists) exists only within the scanned images.

**Total native tables:** 0

### Summary

This is a 6-page digitized 1948 newspaper at high resolution (~5500x6800
px per page, ~300 DPI). Each page consists of a single full-page raster
scan with an OCR text overlay (600-1349 TEXT objects per page). The
newspaper contains rich visual content -- news photos, advertisement
illustrations, comic strips, crossword puzzle, decorative typography --
but all of it exists within the full-page scan images as pixel data. There
are no separate embedded image objects for individual photos or ads.
Category set to "mixed-content" because the document combines scanned
images with OCR text, and the visual content within the scans includes
both text and photographs. Useful as a test case for: (1) OCR quality on
aged newspaper print, (2) multi-column layout detection, (3) whether the
pipeline can identify photo regions within full-page scans.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 10: medrxiv_llama4_benchmark.docx

**Format:** DOCX, ~216 paragraphs
**Category:** text-only
**Source:** medRxiv -- supplementary material for LLM medical benchmark
evaluation (specialty mapping, accuracy comparisons, prompting effects)

### Embedded Images

Inspected via DOCX ZIP archive. No media/ directory, no image files, no
drawing elements, no blip references in document.xml.

**Total embedded images:** 0

### Vector Figures

Not applicable (DOCX format). No drawing elements in document.xml.

**Total vector figures:** 0

### Tables

Inspected via document.xml table element parsing.

| # | Rows | Cols | Description | Notes |
|---|------|------|-------------|-------|
| 1 | 25 | 2 | Table 1A: Specialty mapping to Surgical and Non-surgical domains -- maps medical specialties (Rheumatology, Nephrology, etc.) to domain categories | Simple 2-column lookup table |
| 2 | 25 | 2 | Table 2: T-test p-values comparing MCQ accuracy between medical vs surgical specialties per model | Statistical results table |
| 3 | 40 | ~5 | Table 3: Effect of prompting for selected LLMs -- base, base + few-shot, instruct, instruct + few-shot accuracy per model (GPT-4o, Llama variants, etc.) | Largest table; multi-condition comparison |
| 4 | 4 | 5 | Supplementary table -- additional statistical data | Small summary table |

**Total tables:** 4

### Summary

This is a pure text/table supplementary materials document with zero
images of any kind. The DOCX ZIP archive contains only document.xml,
styles, fonts, and theme -- no media/ folder. The 4 tables contain
medical specialty mappings and LLM benchmark accuracy comparisons.
Category set to "text-only" as there are no annotation targets. Useful
only for testing table extraction quality on DOCX format.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


---


## Doc 11: policy_gradient_rl_lecture.pptx

**Format:** PPTX, 80 slides
**Category:** multi-image
**Source:** Reinforcement learning lecture slides covering TD learning,
Q-learning, SARSA, policy gradients, actor-critic, DQN, and A3C

### Embedded Images

Inspected via PPTX ZIP archive media/ directory. 26 PNG files found,
mapped to slides via relationship files.

**Algorithm pseudocode boxes (screenshots from textbooks/papers):**

| # | Slide | Content Type | Pixel Size | Description | Notes |
|---|-------|-------------|------------|-------------|-------|
| 1 | 36 | screenshot | 784x307 | Tabular TD(0) for estimating v_pi -- pseudocode with initialize V(s), episode loop, TD update rule | image11.png; Sutton & Barto style |
| 2 | 39 | screenshot | 744x301 | Sarsa: An on-policy TD control algorithm -- pseudocode with Q(S,A) update, epsilon-greedy action selection | image13.png |
| 3 | 41 | screenshot | 767x277 | Q-learning: An off-policy TD control algorithm -- pseudocode with max_a Q(S',a) update | image15.png |
| 4 | 48 | screenshot | 699x356 | DQN loss function and gradient from Mnih et al. -- mathematical text with equations (2) and (3) for Q-network training | image16.png; excerpt from Nature paper |
| 5 | 49 | screenshot | 717x362 | Algorithm 1: Deep Q-learning with Experience Replay -- full pseudocode with replay memory, minibatch sampling | image17.png; Mnih et al. |
| 6 | 60 | screenshot | 753x265 | REINFORCE: A Monte-Carlo Policy-Gradient Method (episodic) -- pseudocode with G_t return calculation and theta update | image20.png; Sutton & Barto |
| 7 | 63 | screenshot | 753x477 | One-step Actor-Critic (episodic) -- pseudocode with policy weights theta, value weights w, TD error delta | image22.png; Sutton & Barto |
| 8 | 72 | screenshot | 470x441 | Algorithm 1: Asynchronous one-step Q-learning -- pseudocode for actor-learner thread with target network updates | image23.png; Mnih et al. A3C paper |
| 9 | 76 | screenshot | 797x578 | Algorithm S2: Asynchronous n-step Q-learning -- pseudocode for actor-learner thread with n-step returns | image24.png; A3C supplementary |
| 10 | 79 | screenshot | 803x482 | Algorithm S3: Asynchronous advantage actor-critic -- pseudocode with policy gradient and value function updates | image26.png; A3C supplementary |

**Mathematical equations (rendered as images):**

| # | Slide | Content Type | Pixel Size | Description | Notes |
|---|-------|-------------|------------|-------------|-------|
| 11 | 55 | equation | 246x70 | Softmax policy parameterization: pi(a|s,theta) = exp(h(s,a,theta)) / sum_b exp(h(s,b,theta)) | image18.png |
| 12 | 58 | equation | 336x72 | REINFORCE update rule: theta_{t+1} = theta_t + alpha * gamma^t * G_t * grad log pi(A_t|S_t,theta) | image19.png |
| 13 | 62 | equation | 567x131 | Actor-critic update with baseline: theta_{t+1} = theta_t + alpha * (G^(1) - v_hat) * grad log pi / pi | image21.png; two-line equation |
| 14 | 78 | equation | 941x78 | Generalized advantage estimate: sum gamma^i r_{t+i} + gamma^k V(s_{t+k}) - V(s_t) | image25.png |

**Decorative elements (white/blank separator bars):**

| # | Slides | Content Type | Pixel Size | Description | Notes |
|---|--------|-------------|------------|-------------|-------|
| 15-26 | 21-34 | decorative | various (83-244 px height, 782-2369 px width) | White/blank horizontal bars used as slide separators or spacers | 12 images: image1-10, image12, image14; all appear blank white |

**Total embedded images:** 26 (10 algorithm pseudocode, 4 equations, 12 decorative)
**Slides with images:** 24 of 80 slides
**Slides without images:** 56 slides (text, bullet points, mathematical notation in native PPTX format)

### Vector Figures

Not applicable (PPTX format). No chart files in the archive.

**Total vector figures:** 0

### Tables

No tables found in the PPTX content.

**Total tables:** 0

### Summary

Estimated count in fixtures/README.md was ~25. Actual count is 26 media
files across 80 slides, but only 14 contain meaningful content (10
algorithm pseudocode boxes + 4 mathematical equations). The remaining 12
are blank white separator bars. All content images are screenshots from
RL textbooks (Sutton & Barto) and papers (Mnih et al. DQN, A3C) showing
algorithm pseudocode with mathematical notation. No charts, diagrams, or
photographs. The 56 slides without images contain native PPTX text with
bullet points, equations, and lecture content. This document tests: (1)
annotation of algorithm pseudocode images, (2) filtering of blank
decorative images, (3) PPTX format handling. Category confirmed as
"multi-image" due to 14 content images.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 12: minnstate_fy2025_budget.pptx

**Format:** PPTX, 17 slides
**Category:** multi-image
**Source:** Minnesota State FY2025 Operating Budget, Second Reading (June 2024).
Sourced from KVIS-173 test fixtures.

### Embedded Images

Inspected via PPTX ZIP archive media/ directory. 4 PNG files found.

| # | Content Type | Pixel Size | Description | Notes |
|---|-------------|------------|-------------|-------|
| 1 | decorative | ~300x100 | Minnesota State logo with text (small header) | image1.png |
| 2 | decorative | ~475x800 | Minnesota State "M" banner logo (large) | image2.png |
| 3 | table-image | ~1024x540 | Table 9: North Star Promise Program Projected Awards, FY2025. 4 institution rows (MN State Colleges, Universities, U of M, Tribal) with projected student count, average award, total awards | image3.png; financial data table rendered as image |
| 4 | decorative | ~1440x760 | Minnesota State full logo with text (large) | image4.png |

**Total embedded images:** 4 (1 table-image, 3 decorative logos)
**Slides with images:** ~4 of 17
**Slides without images:** ~13 slides (text, bullet points, budget line items)

### Summary

Government budget presentation with mostly text-based slides. The primary
evaluation target is Table 9 (North Star Promise Program), which is a
financial data table rendered as a raster image rather than native PPTX
table. This directly addresses the table-as-image gap. The 3 logo images
are decorative and should be skipped.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 13: artpro_table.webp

**Format:** WebP (standalone image)
**Category:** table-image
**Source:** Aircraft wing specification table from ArtPro product catalog.
Sourced from KVIS-174 test fixtures.

### Image Content

| # | Content Type | Description | Notes |
|---|-------------|-------------|-------|
| 1 | table-image | Aircraft wing specification table: 6 models (1401, 1201, 1121, 1051, 1001, 951) with 7 columns (wingspan, chord, mean average chord, actual area, projected area, volume, aspect ratio). Alternating row shading, bold header. Units in mm/in and cm2/in2. | Clean tabular layout with mixed metric/imperial units |

**Total images:** 1
**Annotation target:** Full image is the annotation target.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 14: simple_table.png

**Format:** PNG (standalone image)
**Category:** table-image
**Source:** Spreadsheet cell/format/formula reference table.
Sourced from KVIS-174 test fixtures (originally from image-table-ocr GitHub repo).

### Image Content

| # | Content Type | Description | Notes |
|---|-------------|-------------|-------|
| 1 | table-image | Simple 3-column table (Cell, Format, Formula) with 5 rows (B4-F4). Shows cell formats (Percentage, General, Accounting, Currency) and formulas (=PMT(B4/12,C4,D4), =E4*C4). White background with black gridlines. | Clean OCR-friendly table with formulas |

**Total images:** 1
**Annotation target:** Full image is the annotation target.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 15: timetable.jpg

**Format:** JPG (standalone image)
**Category:** table-image
**Source:** University of Washington SWORD Deadlines course timetable.
Sourced from KVIS-174 test fixtures.

### Image Content

| # | Content Type | Description | Notes |
|---|-------------|-------------|-------|
| 1 | table-image | Course assignment schedule: "SWORD Deadlines" header, 9 weeks (3-11), 4 assignment types (draft, review, feedback + final). Color-coded cells: pink (draft), blue (review), green (feedback), red (final). Staggered submission pattern across weeks. | Color-coded schedule requiring understanding of temporal relationships |

**Total images:** 1
**Annotation target:** Full image is the annotation target.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 16: cambridge_mitoball_biology.docx

**Format:** DOCX (6.8 MB)
**Category:** multi-image
**Source:** Cambridge University Repository -- Drosophila spermatogenesis
biology paper. Sourced from Cambridge institutional repository.

### Embedded Images

Inspected via DOCX ZIP archive media/ directory. 9 files found (8 JPEG,
1 TIFF).

| # | Content Type | File Size | Description | Notes |
|---|-------------|-----------|-------------|-------|
| 1 | decorative | 11 KB | TIFF logo/icon | image1.tiff; likely journal or institution branding |
| 2 | photo | 788 KB | Figure 1: Multi-panel composite (A-I). (A) Spermatogenesis diagram with cell stages, (B) fluorescence microscopy of testis cross-section (ATP5A, green/magenta), (C) mito-YFP close-up, (D) bar chart of mitoball diameter by stage, (E) 4-panel electron micrograph series, (F) mitochondrial velocity dot plot, (G) time-lapse series (6 frames, Dendra green/magenta), (H) dsDNA puncta bar chart with statistics, (I) 5-panel fluorescence (DAPI/YFP/EdU/Merge/Zoom) | Complex composite; 9 sub-panels mixing diagram, microscopy, charts, EM |
| 3 | photo | 960 KB | Figure 2: Multi-panel composite (A-G). (A) Full testis cross-section with zoom insets, (B) electron micrographs (Mitoball, Nebenkern), (C) fluorescence with dashed boundary, (D) mito-YFP close-up, (E) mtSSB-RFP/dsDNA 3-channel, (F) 3-row x 4-column fluorescence grid (Mitotic/Mitoball/Nebenkern x DAPI/YFP/EdU/Merge), (G) PolG1 dual stain | Complex composite; EM + fluorescence + multi-channel grids |
| 4 | photo | 744 KB | Figure 3: Multi-panel with genetic knockdowns. Fluorescence panels showing control vs mutant (mfn RNAi, Drp1 KD) across multiple staining channels | Genetic perturbation experiments |
| 5 | photo | 1.1 MB | Figure 4: Large multi-panel composite. Multiple fluorescence and EM panels showing mitoball ultrastructure at different developmental stages | Largest figure; detailed ultrastructure |
| 6 | photo | 666 KB | Figure 5: Cross-species fluorescence comparison panels with annotations, scale bars, and labeled species names | Multi-species comparative data |
| 7 | photo | 764 KB | Figure S1 (supplementary): Additional fluorescence panels with control/experimental comparisons | Supplementary data |
| 8 | photo | 1.0 MB | Figure S2: Extended cross-species comparison (A) 6 Drosophila species + 2 other insects, each with overview + zoom, (B) Drosophila bocqueti and Anopheles coluzzii, (C) Schistoserca gregaria and Teleogryllus/Blaberus | Large comparative panel across 8+ insect species |
| 9 | photo | 804 KB | Figure S3: Additional experimental panels (Phalloidin, Pav-GFP, ATP5A staining + alpha-spectrin control vs hts mutant comparison) | Cytoskeletal markers |

**Total embedded images:** 9 (1 decorative TIFF, 8 scientific composite figures)
**Content diversity:** fluorescence microscopy, electron micrographs, diagrams, bar charts with statistics, time-lapse series, cross-species comparisons
**Unique value:** First DOCX with content images; all figures are complex multi-panel composites requiring domain knowledge to annotate

### Summary

Cell biology paper on mitochondrial dynamics during insect spermatogenesis.
Each of the 8 scientific figures is a complex multi-panel composite containing
a mix of fluorescence microscopy (DAPI/YFP/RFP channels in blue/green/magenta),
electron micrographs (grayscale TEM), diagrams, bar charts with statistical
annotations, and time-lapse sequences. Figures span multiple insect species
(Drosophila, mosquito, cricket, cockroach, locust). This is the first DOCX
with meaningful image content and simultaneously addresses the photo variety
gap with domain-specific scientific imagery. All figures are hard difficulty
due to multi-panel structure, domain-specific labels, and the need to
understand biological context.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 17: arxiv_fractional_brownian_sde.pdf

**Format:** PDF, 24 pages (248 KB)
**Category:** text-heavy (equation-dense)
**Source:** arXiv 2306.08324 -- "Stochastic differential equations driven
by fractional Brownian motion" by Dordevic and Oksendal (2024).

### Embedded Images

No embedded raster images. All mathematical content is native LaTeX.

**Total embedded images:** 0

### Equation Content

All equations are LaTeX-rendered (native PDF text/vector, not raster images).
The pipeline must crop equation regions from rendered pages to produce
annotation targets.

| Category | Count | Examples |
|----------|-------|---------|
| Numbered display equations | 63 | (2.14), (2.15), (3.27), (4.1)-(4.3) |
| Theorem environments | 15 | Theorem 2.1 (Bochner-Minlos), Theorem 2.10, Theorem 4.1 |
| Lemma environments | 9 | Lemma 2.11, Lemma 3.4 |
| Definition environments | 6 | Definition 2.7 (fractional Brownian motion), Definition 2.9 (WIS integral) |
| Proof blocks | 7 | Multi-page proofs with QED squares |
| Corollary | 1 | |

**Symbol diversity:** Integrals (Lebesgue, Ito, WIS), expectations E[],
stochastic differentials (dX_t, dB^H), Schwartz space S(R), Wick products,
L^p norms, supremum bounds, Greek letters, summations, fractions, multi-line
aligned derivations (up to 6-line inequality chains).

### Summary

Pure mathematics paper on stochastic differential equations. Contains no
embedded images but is extremely equation-dense (63 numbered equations in
24 pages, ~2.6 per page). Equations are rendered natively in LaTeX, providing
a completely different annotation challenge from Doc 11's screenshot-based
equations. This tests whether the pipeline can: (1) identify equation regions
in born-digital PDFs, (2) annotate formal mathematical notation with correct
symbol identification, (3) handle multi-line aligned derivations and nested
expressions. The equation styles are diverse: display equations, inline math,
multi-line proofs, theorem/definition environments.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 18: ibm_microservices_redbook.pdf

**Format:** PDF, 170 pages (7.0 MB)
**Category:** multi-image
**Source:** IBM Redbooks -- "Microservices: From Theory to Practice" (SG24-8275-00, April 2016)

### Embedded Images

Total raster images: 206 across 72 pages (many are composited icon elements
within complex architecture diagrams). 91 named figures spanning architecture
diagrams, UI screenshots, process diagrams, and code listings.

#### Architecture and System Diagrams (~27 figures)

| Figure | Description | Content Type |
|--------|-------------|-------------|
| 1-1 | Sample application using microservices | diagram |
| 1-2 | Monolithic multi-tiered architecture | diagram |
| 1-3 | Microservices architecture with multiple languages and data stores | diagram |
| 2-1 | "Old" style of service design | diagram |
| 2-2 | Application redesigned with microservices approach | diagram |
| 2-3 | Circuit breaker sequence diagram | diagram |
| 2-4 | Bulkhead pattern: separate thread pools to isolate failure | diagram |
| 2-5 | RESTful API calls between client and services | diagram |
| 2-6 | Fronting microservices with an API Gateway | diagram |
| 2-8 | REST architecture with intermediary caches | diagram |
| 2-9 | Common use cases for messaging | diagram |
| 2-10 | Event notification for stock price | diagram |
| 3-4 | Decentralized data store for microservices | diagram |
| 3-5 | Microservices transformation | diagram |
| 4-5 | Cloud integration flow | diagram |
| 5-2 | North Star Architecture for DevOps Services | diagram |
| 5-3 | High-level Bluemix console architecture (pre-microservice) | diagram |
| 5-6 | Bluemix console microservice transformation end-goal | diagram |
| 5-8 | IBM Watson Developer Cloud platform architecture (multi-layer) | diagram |
| 5-9 | IBM IaaS++ architecture (multi-zone with availability regions) | diagram |
| 5-11 | Service register and discovery | diagram |
| 5-12 | Onboarding a Watson service to cloud environment | diagram |
| 6-2 | CloudTrader components overview | diagram |
| 6-4 | CloudTrader with externalized Quote microservice | diagram |
| 8-1 | Acme Air monolithic architecture | diagram |
| 8-12 | Acme Air microservices architecture | diagram |
| 4-16 | Communication between applications in Bluemix | diagram |

#### Process and Framework Diagrams (~8 figures)

| Figure | Description | Content Type |
|--------|-------------|-------------|
| 2-7 | Hills Playback timeline | infographic |
| 3-1 | DevOps approach: continuous delivery | infographic |
| 3-2 | Common challenges with traditional software delivery | infographic |
| 3-3 | IBM DevOps framework to continuous delivery | infographic |
| 4-2 | Applications on Bluemix (deployment flow) | diagram |
| 4-3 | Bluemix deployment models (local, dedicated, public) | diagram |
| 4-8 | Application lifecycle management of microservices | infographic |
| 4-12 | Multi-region DevOps delivery pipeline | diagram |

#### UI Screenshots (~20 figures)

Figures 4-1, 4-6, 4-7, 4-9, 4-10, 4-11, 4-13, 4-14, 4-15, 4-17,
5-1, 5-5, 5-10, 6-1, 6-5, 7-1, 7-2, 7-3, 8-2 through 8-11, 8-13
through 8-18.

Content: Bluemix dashboard views, service catalogs, deployment
consoles, monitoring dashboards, Hystrix dashboard, code editors.
All are raster screenshots of web UIs.

### Image Summary

| Content Type | Count | Notes |
|-------------|-------|-------|
| diagram | ~27 | Architecture, component, sequence, deployment, topology |
| infographic | ~5 | DevOps frameworks, timelines, process flows |
| screenshot | ~20 | Bluemix/Watson dashboard UIs, deployment consoles |
| decorative | 0 | No decorative images |
| Total content images | ~52 | Counted from 91 named figures minus inline text refs |

Annotation targets: Architecture diagrams (27) and process diagrams (5)
are the primary annotation targets. UI screenshots (20) are secondary.

### Summary

IBM Redbooks technical guide covering microservices architecture patterns,
DevOps practices, and IBM Bluemix deployment. The document's primary value
for our evaluation is its ~27 architecture diagrams spanning component
diagrams (microservices decomposition), sequence diagrams (circuit breaker),
deployment diagrams (Bluemix regions, scaling), topology diagrams (Watson
platform layers, IaaS zones), and pattern diagrams (API gateway, bulkhead,
messaging). Diagrams range from simple box-and-arrow (2-3 components) to
complex multi-layer architectures (Watson Developer Cloud with 4 layers and
12+ components; IaaS++ with availability zones, regions, and service mesh).
This directly addresses the "Diagrams" gap -- no complex architecture/UML
diagrams existed in the corpus before this fixture.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*


## Doc 19: cris_electronic_screens_2023.docx

**Format:** DOCX (1.3 MB)
**Category:** multi-image
**Source:** Australian Government Office of Impact Analysis -- CRIS Electronic
Screens 2023 (Equipment Energy Efficiency / E3 program)

### Embedded Images

Total media files: 18 (11 content images + 3 decorative + 3 spacers + 1 icon)

| Image | Description | Content Type | Difficulty |
|-------|-------------|-------------|------------|
| image1 | E3 program cover page with appliance icons | decorative | -- |
| image2 | Small icon/label (5K PNG) | decorative | -- |
| image3 | Spacer (134 bytes) | spacer | -- |
| image4 | Spacer (134 bytes) | spacer | -- |
| image5 | Pie chart: equipment type market share (5 segments with %) | chart-simple | Easy |
| image6 | Photo: airport departure hall with electronic display screens | photo | Medium |
| image7 | Photo: Changi Airport digital signage kiosk | photo | Easy |
| image8 | Stacked area chart: EU energy use on-mode 1990-2030 (3 series) | chart-simple | Easy |
| image9 | Scatter/strip chart: energy ratings data (small, dense) | chart-complex | Medium |
| image10 | Multi-line chart: on-mode power vs screen area, 9 regulatory lines | chart-complex | Medium |
| image11 | Multi-line chart: max ON-mode power vs screen area, 11 lines with annotations | chart-complex | Hard |
| image12 | Bar chart: star rating distribution histogram (12 bars) | chart-simple | Easy |
| image13 | Energy rating label: Super Efficiency (199 kWh) | infographic | Easy |
| image14 | Energy rating label: Standard (485 kWh) | infographic | Easy |
| image15 | Spacer (140 bytes) | spacer | -- |
| image16 | Spacer (141 bytes) | spacer | -- |
| image17 | Small divider (767 bytes) | decorative | -- |
| image18 | E3 back cover page (logo) | decorative | -- |

### Image Summary

| Content Type | Count | Notes |
|-------------|-------|-------|
| chart-simple | 3 | Pie, stacked area, bar histogram |
| chart-complex | 3 | Scatter/strip, 2 multi-line regulatory comparisons |
| photo | 2 | Airport electronic display scenes |
| infographic | 2 | Australian energy rating labels |
| decorative | 4 | Cover pages, icon, divider |
| spacer | 3 | Sub-200-byte transparent PNGs |
| Total content images | 10 | |

### Summary

Australian government regulatory impact assessment on electronic display
energy efficiency standards. This fixture is critical for filling the DOCX
format gap: it provides the first raster charts in DOCX format (3 simple +
3 complex), the first easy/medium-difficulty DOCX images (previously DOCX
had only 8 hard-difficulty photos from Doc 16), and expands DOCX content
type coverage from 1 type (photo) to 4 types (chart-simple, chart-complex,
photo, infographic). All charts are pasted as raster PNG/JPEG images rather
than EMF vector metafiles, making them proper extraction targets for the
pipeline.

### Pipeline Extraction

*Pending extraction*

### Coverage Comparison

*Pending comparison*

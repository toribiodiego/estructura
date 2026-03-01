# Image Analysis: Doc 02 -- 02_icml2019_importance_sampling.pdf

**Document:** `02_icml2019_importance_sampling.pdf`
**Format:** PDF
**Source:** https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/ICML2019-Hanna.pdf
**Category:** multi-image
**Images:** 18
**Document context:** ICML 2019 paper on importance sampling for off-policy
evaluation in reinforcement learning. Compares estimation methods (WIS, PDIS,
AM, DR, etc.) across gridworld, linear dynamical system, and MuJoCo domains.

<br><br>

## doc02-R01 -- Gridworld MSE with 6 method lines

**Figure reference:** Figure 2a, page 6
**Content type:** chart-complex
**Annotation difficulty:** Medium
**Dimensions:** 1350x1200 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** Log-log line chart with confidence bands
- **Axes:**
  - Y-axis: "Mean Squared Error" (log scale, range 10^-3 to 10^4)
  - X-axis: "Number of Trajectories" (log scale, range ~10^1 to ~10^4)
- **Legend (inside plot, top area, 3 rows x 2 columns):**
  - Row 1: RIS (thick blue solid line) | OIS (thin blue dashed line)
  - Row 2: RIS WIS (thick red dotted line) | OIS WIS (thin pink/red dotted
    line)
  - Row 3: RIS WDR (thick green dashed line) | OIS WDR (thin gray/green
    dashed line)
- **Lines (6 total, three color groups from top to bottom):**
  - Blue group (highest MSE): RIS and OIS -- start around 10^2 at ~10^1
    trajectories, decrease to roughly 10^0 at ~10^4
  - Red group (middle MSE): RIS WIS and OIS WIS -- start around 10^0 to
    10^1, decrease to roughly 10^-2
  - Green group (lowest MSE): RIS WDR and OIS WDR -- start around 10^-1,
    decrease to roughly 10^-2 to 10^-3
- **Confidence bands:** Translucent shaded regions around each line (same
  color as line)
- **Subplot label:** "(a) Gridworld" below the chart
- **Grid lines:** Light gray horizontal grid lines at each power-of-10 tick
- **Y-axis tick marks:** 10^-3, 10^-2, 10^-1, 10^0, 10^1, 10^2, 10^3, 10^4
- **X-axis tick marks:** 10^1, 10^2, 10^3

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 6 lines in the chart, one per method
- FACT: The y-axis label reads "Mean Squared Error"
- FACT: The x-axis label reads "Number of Trajectories"
- FACT: Both axes use logarithmic scale
- FACT: The legend lists 6 methods: RIS, OIS, RIS WIS, OIS WIS, RIS WDR,
  OIS WDR
- FACT: RIS is represented by a thick blue solid line
- FACT: OIS is represented by a thin blue dashed line
- FACT: RIS WIS is red and dotted; OIS WIS is pink/red and dotted
- FACT: RIS WDR is green and dashed; OIS WDR is a thin gray/green dashed
  line
- FACT: All 6 lines trend downward from left to right (MSE decreases with
  more trajectories)
- FACT: The blue lines (RIS/OIS) have the highest MSE across the full x-range
- FACT: The green lines (WDR variants) have the lowest MSE across the full
  x-range
- FACT: The red lines (WIS variants) fall between blue and green
- FACT: The subplot label reads "(a) Gridworld"
- FACT: All lines have translucent shaded confidence bands

### Hallucination Risks [-> Accuracy]

- RISK: A model might report precise MSE values at specific trajectory counts
  (e.g., "RIS has MSE of exactly 150 at 100 trajectories")
  REALITY: The log-scale axes and confidence bands make precise readings
  unreliable; only approximate orders of magnitude and relative positions are
  confidently readable
- RISK: A model might confuse the RIS/OIS pair with the WIS pair, since both
  blue and red lines have two variants with similar line styles
  REALITY: The color distinction (blue vs red vs green) is clear, but within
  each color pair the solid vs dashed distinction is subtle, especially where
  confidence bands overlap
- RISK: A model might claim the lines cross or reverse ordering
  REALITY: The blue > red > green ordering appears consistent across the full
  x-range; no clear crossover is visible
- RISK: A model might state the x-axis extends to 10^5 or beyond
  REALITY: The x-axis range appears to end at or just past 10^3, not reaching
  10^5
- RISK: A model might describe the OIS WDR legend entry as "OIS WDR" with
  confidence, but the rightmost letter may be truncated
  REALITY: The legend's last entry on the right column appears as "OIS WD"
  with possible "R" truncation at the plot border
- RISK: A model might describe these as separate experiments rather than one
  figure subplot
  REALITY: This is Figure 2a, one of four subplots in Figure 2

### Detail Inventory [-> Specificity]

- 6 lines in 3 color groups: blue (RIS/OIS), red (RIS WIS/OIS WIS), green
  (RIS WDR/OIS WDR)
- Line style encoding: thick lines for RIS variants, thin lines for OIS
  variants
- Line style encoding: solid for base IS, dotted for WIS, dashed for WDR
- Confidence bands: same color as line, translucent fill
- Y-axis spans 7 orders of magnitude (10^-3 to 10^4)
- X-axis spans roughly 2.5 orders of magnitude (~10^1 to ~10^4)
- All lines roughly linear on the log-log scale (power-law decay)
- The blue lines (basic IS) have wider confidence bands than green (WDR)
  lines
- Grid lines: light gray horizontal lines at each power-of-10 tick
- White background inside the plot area
- No annotations, callouts, or additional text beyond labels and legend

### Domain Context [-> Usefulness]

- **Figure caption context:** Figure 2a from an ICML 2019 paper on importance
  sampling for off-policy evaluation in reinforcement learning. The paper
  compares estimation methods for evaluating a policy using data collected by
  a different (behavior) policy.
- **Methods compared:**
  - RIS: Regular Importance Sampling
  - OIS: Ordinary Importance Sampling (per-step variant)
  - WIS: Weighted Importance Sampling (self-normalizing variant)
  - WDR: Weighted Doubly Robust (combining importance sampling with a
    model-based estimate)
- **What the chart shows:** Mean Squared Error of policy value estimates in a
  Gridworld domain as the number of trajectories (episodes) increases. Lower
  MSE = more accurate estimation.
- **Key finding visible in chart:** WDR methods (green) achieve dramatically
  lower MSE than basic IS methods (blue), spanning 2-3 orders of magnitude
  improvement. WIS (red) provides intermediate improvement.
- **Domain terminology:**
  - Off-policy evaluation: estimating the value of one policy using data from
    another
  - Trajectories: sequences of state-action-reward transitions in the MDP
  - MSE: Mean Squared Error, measuring estimation accuracy

### Search Keywords [-> Usefulness]

importance sampling, off-policy evaluation, reinforcement learning, MSE,
Mean Squared Error, gridworld, WIS, weighted importance sampling, WDR,
weighted doubly robust, RIS, OIS, trajectories, policy evaluation, ICML 2019,
confidence bands, log-log plot, estimation methods, Hanna

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A line chart showing method performance" (no axis labels, no method names, wrong MSE direction) | "Log-log plot of MSE vs trajectories for 6 importance sampling methods; WDR lowest, basic IS highest; all decrease with more data" (correct key facts) | All 6 method names correct (RIS, OIS, RIS WIS, OIS WIS, RIS WDR, OIS WDR); correct axis labels and scales; correct color-to-method mapping; correct ordering (blue > red > green); notes confidence bands |
| Specificity | "Lines going down with some shading" (no method names, no scale info) | "6 colored lines on log-log axes; blue lines highest (RIS/OIS), green lines lowest (WDR variants); x-axis is trajectories from ~10 to ~10,000" (some specifics) | Names all 6 methods with their line style (thick/thin, solid/dotted/dashed) and color; cites Y range (10^-3 to 10^4); identifies confidence band colors match line colors; notes grid lines at powers of 10 |
| Completeness | Mentions only "some lines on a chart"; misses legend, axis labels, or confidence bands | Covers 6 lines, both axis labels, log scale, confidence bands, and the (a) Gridworld label | All 6 legend entries with line styles, both axes with labels and tick ranges, confidence bands with transparency, grid lines, subplot label, relative ordering of all three method groups |
| Usefulness | "A graph from a paper" (no searchable terms, no domain context) | "Off-policy evaluation MSE comparison in gridworld; importance sampling variants compared; from ICML 2019 paper" (searchable, domain-appropriate) | Explains RIS/OIS/WIS/WDR method distinctions, notes the 2-3 order-of-magnitude improvement of WDR over basic IS, contextualizes as off-policy evaluation in RL, connects to the paper's broader comparison across domains |

<br><br>

## doc02-R08 -- Hopper MSE grouped bar chart

**Figure reference:** Figure 5a, page 7
**Content type:** chart-simple
**Annotation difficulty:** Easy
**Dimensions:** 1800x1600 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** Dual-axis grouped bar chart with error bars
- **Left y-axis:** "Mean Squared Error" (linear scale, range 0 to 700)
- **Right y-axis:** "Negative Log Likelihood" (linear scale, range 0.003 to
  0.013)
- **X-axis categories (5):** `0-0`, `1-64`, `2-64`, `3-64`, `OIS`
- **Subplot label:** "(a) Hopper" below the chart
- **Bar encoding (per the figure caption, not visible as a legend in the
  crop):**
  - Blue-toned bars = MSE values (read against left y-axis)
  - Red/pink-toned bars = Negative Log Likelihood (read against right y-axis)
  - The architecture with the lowest hold-out NLL is given the darkest pair
    of bars; other architectures appear in progressively lighter shades
- **Bars by category:**
  - `0-0`: Very light blue and very light pink bars, both capped at the top
    of the chart (~700 MSE / ~0.013 NLL), indicating off-scale values for the
    no-hidden-layer baseline
  - `1-64`: Medium-light blue bar (~340 MSE) and light pink bar
  - `2-64`: **Darkest blue bar** (~450 MSE) and **dark red cross-hatched bar**
    (~0.007 NLL) -- highlighted as the architecture with lowest hold-out NLL
  - `3-64`: Medium blue bar (~400 MSE) and light pink bar
  - `OIS`: Medium blue bar (~510 MSE) with light bar
- **Error bars:** Vertical lines with horizontal caps visible on several bars
  (most prominent on `2-64` and `OIS` categories)
- **Grid lines:** Light gray horizontal lines on left y-axis ticks (0, 100,
  200, 300, 400, 500, 600, 700)
- UNCERTAIN: Small text annotations may appear near the top of the `0-0`
  bars showing actual off-chart values, but these are not clearly readable at
  this crop resolution

### Verifiable Facts [-> Accuracy]

- FACT: The left y-axis label reads "Mean Squared Error"
- FACT: The right y-axis label reads "Negative Log Likelihood"
- FACT: There are exactly 5 x-axis categories: 0-0, 1-64, 2-64, 3-64, OIS
- FACT: The subplot label reads "(a) Hopper"
- FACT: The `0-0` bars extend to or beyond the top of the y-axis range (both
  MSE and NLL values are off-scale)
- FACT: The `2-64` category has the darkest bars, with the red bar displaying
  a diagonal cross-hatch pattern
- FACT: The `2-64` MSE bar (~450) is HIGHER than the `1-64` MSE bar (~340)
  and the `3-64` MSE bar (~400)
- FACT: The `OIS` MSE bar (~510) is higher than all neural network
  architecture bars except `0-0`
- FACT: Error bars (standard deviation/error indicators) are visible on
  multiple bars
- FACT: Left y-axis tick marks are at 0, 100, 200, 300, 400, 500, 600, 700
- FACT: Right y-axis tick marks range from 0.003 to 0.013
- FACT: No legend is visible within the chart crop -- bar encoding is defined
  in the figure caption below the subplots

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe the `2-64` architecture as having the lowest
  MSE because it is highlighted (darkest bars)
  REALITY: The `2-64` is highlighted because it has the lowest NLL (best
  model fit), not the lowest MSE. Its MSE (~450) is actually higher than
  `1-64` (~340) and `3-64` (~400). This counterintuitive result is the
  paper's key finding.
- RISK: A model might invent a legend that is not visible in the crop
  REALITY: The bar encoding is explained only in the figure caption text
  (below the subplots), not in a legend inside the chart
- RISK: A model might report precise NLL values for each bar, but the right
  y-axis scale (0.003-0.013) makes precise readings difficult
  REALITY: Only approximate NLL values can be read; exact values would
  require the underlying data
- RISK: A model might describe the `0-0` bars as having specific MSE/NLL
  values at exactly 700 / 0.013
  REALITY: The bars are clipped at the chart boundary -- actual values exceed
  the displayed range
- RISK: A model might interpret the architecture notation (e.g., "2-64") as
  something other than "#layers-#units"
  REALITY: The caption specifies the format as "#-layers-#-units"
- RISK: A model might describe the cross-hatched red bar at `2-64` as a
  different type of data rather than a visual highlight
  REALITY: The hatching distinguishes the lowest-NLL architecture

### Detail Inventory [-> Specificity]

- 5 architecture categories on x-axis: 0-0 (no hidden layers), 1-64 (1
  layer, 64 units), 2-64 (2 layers, 64 units), 3-64 (3 layers, 64 units),
  OIS (baseline estimator)
- Dual y-axis: MSE (0-700, left) and NLL (0.003-0.013, right)
- Bar color gradient: lighter shades for worse architectures, darkest for the
  best-NLL architecture (2-64)
- Cross-hatch pattern on the 2-64 NLL bar (dark red with diagonal lines)
- Error bars with horizontal caps on multiple bars
- 0-0 bars clipped at chart ceiling, suggesting values well above 700 MSE
- Gray horizontal grid lines at each 100-unit MSE increment
- White background inside the plot area
- No legend within the chart area

### Domain Context [-> Usefulness]

- **Figure caption context:** Figure 5a from the ICML 2019 paper. The chart
  compares different neural network architectures for regression-based
  importance sampling (RIS) in the MuJoCo Hopper domain.
- **Architecture notation:** `#layers-#units` specifies the number of hidden
  layers and hidden units per layer. `0-0` is a linear model (no hidden
  layers). `2-64` means 2 hidden layers with 64 units each.
- **OIS:** Ordinary Importance Sampling -- a non-parametric baseline that does
  not use a regression model, included for comparison.
- **Key finding visible in chart:** The architecture with the best model fit
  (lowest NLL, `2-64`) does NOT have the lowest MSE. The `1-64` architecture
  has lower MSE (~340) than `2-64` (~450) despite worse NLL. This suggests
  that the best-fitting model does not necessarily produce the best importance
  sampling estimates -- a central finding of the paper.
- **NLL (Negative Log Likelihood):** Measures how well the regression model
  fits held-out data. Lower NLL = better model fit.
- **MSE (Mean Squared Error):** Measures how close the policy value estimate
  is to the true value. Lower MSE = more accurate estimation.

### Search Keywords [-> Usefulness]

importance sampling, regression, MSE, Mean Squared Error, negative log
likelihood, NLL, neural network architecture, Hopper, MuJoCo, bar chart,
dual axis, OIS, RIS, model selection, hidden layers, policy evaluation,
off-policy, ICML 2019, architecture comparison

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A bar chart comparing methods" (no axis labels, no architecture notation, no dual-axis mention) | "Dual-axis bar chart of MSE and NLL for 5 neural network architectures in Hopper; 2-64 highlighted as lowest NLL; 0-0 exceeds chart range" (correct key facts) | Correct MSE ordering (0-0 > OIS > 2-64 > 3-64 > 1-64); notes 2-64 is lowest NLL but NOT lowest MSE; correct axis labels and ranges; identifies cross-hatch on 2-64 NLL bar; notes error bars |
| Specificity | "Bars of different heights and colors" (no categories, no values) | "5 categories (0-0, 1-64, 2-64, 3-64, OIS) with blue MSE bars and red NLL bars; approximate MSE values given for each" (structural detail) | Cites approximate MSE values per category (~340, ~450, ~400, ~510); identifies bar shading gradient; notes cross-hatch pattern; describes error bar style; specifies axis tick ranges |
| Completeness | Mentions bars and one axis; misses dual-axis encoding, architecture notation, or bar highlighting | Covers both axes, all 5 categories, bar color encoding, and the (a) Hopper label; may miss error bars or the 0-0 clipping | Both axes with labels and tick ranges, all 5 categories with bar heights, dual-axis encoding, cross-hatch on 2-64, error bars, grid lines, 0-0 clipping, bar shading gradient, subplot label |
| Usefulness | "A chart from a paper about neural networks" (not searchable) | "Architecture comparison for regression importance sampling in Hopper (MuJoCo); shows MSE and NLL for different layer/unit configurations" (domain-appropriate) | Explains the counterintuitive finding (best model fit != lowest MSE), contextualizes architecture notation, describes OIS as baseline, connects to the paper's argument about model selection in importance sampling |

<br><br>

## doc02-R10 -- 3-panel vertical training curves

**Figure reference:** Figure 6, page 7
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** 1350x1200 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** 3-panel vertically stacked line charts with shared x-axis
- **Shared x-axis:** "Training Step" (linear scale, range 0 to 7000, ticks at
  every 1000)
- **Shared vertical reference:** Black dashed vertical line at approximately
  step ~1500-2000, marking the minimum validation loss point; passes through
  all three panels

**Top panel -- Neg. Log Likelihood:**
- Y-axis: "Neg. Log Likelihood" (range 2.26 to 2.34)
- Legend (inside plot, top-right): "Validation" (black/gray dotted line) and
  "Train Loss" (red/pink dotted line)
- Validation line: starts ~2.34, drops sharply, reaches minimum ~2.27 around
  step ~1500, then rises slightly and levels off ~2.28
- Train Loss line: starts ~2.34, continuously decreases, reaches ~2.26 by
  step 7000 (drops below validation after the crossing point)
- Both lines have light shaded confidence bands (gray for validation, pink
  for train)
- Annotation: black arrow pointing to the validation minimum with text "Min
  validation loss"

**Middle panel -- MSE:**
- Y-axis: "MSE" (range 0 to 700)
- Legend (inside plot, bottom-right): "RIS" (blue solid line) and "OIS"
  (green dashed line)
- OIS: green horizontal dashed line at ~500 with wide green shaded confidence
  band; essentially constant across training steps
- RIS: blue solid line starting ~600-700, dropping sharply to minimum ~100-
  200 around step ~1000-1500, then gradually rising and stabilizing ~400-500
  by step 7000
- Blue confidence band around the RIS line
- The "Training Step" x-axis label appears between the middle and bottom
  panels

**Bottom panel -- Value:**
- Y-axis: "Value" (range 0 to 300)
- Legend (inside plot, bottom area): "RIS" (blue solid), "OIS" (green
  dashed), "True Value" (green solid)
- True Value: green solid horizontal line at ~130, with light green shaded
  band
- OIS: green dashed line tracking close to the True Value, approximately
  ~140-150
- RIS: blue solid line starting very high (~280), dropping sharply, crossing
  through ~150 around step ~1500, and stabilizing near ~130-140 close to the
  True Value
- Blue confidence band around the RIS line

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 3 vertically stacked panels sharing the x-axis
- FACT: The x-axis label reads "Training Step" with ticks at 0, 1000, 2000,
  3000, 4000, 5000, 6000, 7000
- FACT: A vertical black dashed line passes through all three panels at
  approximately step ~1500-2000
- FACT: The top panel's y-axis label reads "Neg. Log Likelihood"
- FACT: The top panel legend shows "Validation" (dotted) and "Train Loss"
  (red/pink)
- FACT: An annotation arrow labeled "Min validation loss" points to the
  validation curve minimum in the top panel
- FACT: The middle panel's y-axis label reads "MSE"
- FACT: The middle panel legend shows "RIS" (blue solid) and "OIS" (green
  dashed)
- FACT: The OIS line in the middle panel is approximately horizontal (constant
  across training steps)
- FACT: The RIS line in the middle panel has a clear U-shaped or valley
  pattern (drops then rises)
- FACT: The bottom panel's y-axis label reads "Value"
- FACT: The bottom panel legend shows "RIS", "OIS", and "True Value"
- FACT: The True Value line in the bottom panel is horizontal at approximately
  130
- FACT: The RIS value estimate starts far above the True Value and converges
  toward it during training

### Hallucination Risks [-> Accuracy]

- RISK: A model might report the exact training step of the minimum
  validation loss (e.g., "step 1742")
  REALITY: The vertical dashed line is at approximately step 1500-2000; the
  exact value is not labeled
- RISK: A model might claim the RIS MSE reaches zero or near zero at its
  minimum
  REALITY: The RIS MSE minimum appears to be around 100-200, not zero
- RISK: A model might confuse OIS and True Value lines in the bottom panel,
  as both are green
  REALITY: True Value is a solid green line; OIS is a dashed green line. They
  are at similar but not identical vertical positions
- RISK: A model might describe the RIS MSE as monotonically decreasing
  REALITY: The RIS MSE has a clear valley -- it decreases, hits a minimum
  near the vertical dashed line, then increases again as the model overfits
- RISK: A model might state the Train Loss and Validation lines never cross
  REALITY: The train loss drops below the validation loss after approximately
  step 2000-3000, as is typical during overfitting
- RISK: A model might describe the confidence bands as different data series
  REALITY: The shaded regions are confidence/uncertainty bands around their
  respective lines

### Detail Inventory [-> Specificity]

- 3 panels: Neg. Log Likelihood (top), MSE (middle), Value (bottom)
- Shared x-axis: Training Step, 0-7000, linear scale
- Vertical dashed line at ~1500-2000 (min validation loss) through all panels
- Top panel: 2 lines (Validation=black dotted, Train Loss=red dotted), range
  2.26-2.34, annotation arrow with "Min validation loss" text
- Middle panel: 2 lines (RIS=blue solid, OIS=green dashed), range 0-700;
  OIS constant ~500 with wide green confidence band; RIS U-shaped with
  minimum near the vertical dashed line
- Bottom panel: 3 lines (RIS=blue solid, OIS=green dashed, True Value=green
  solid), range 0-300; True Value constant ~130; RIS converges from ~280
  toward True Value
- All data lines have translucent shaded confidence bands
- Gray grid lines at y-axis tick positions in each panel
- White background in all panels

### Domain Context [-> Usefulness]

- **Figure caption:** "Figure 6: Mean squared error and estimate of the
  importance sampling estimator during training of pi_D." The figure shows
  how the IS estimate quality changes as the behavior policy model is trained.
- **What the chart demonstrates:** This is a training dynamics visualization
  from the Hopper domain. As the regression model (pi_D) trains:
  1. The model fit improves (NLL decreases) until overfitting begins
  2. The RIS MSE decreases as the model improves, reaching its best near the
     validation loss minimum
  3. The RIS value estimate converges toward the True Value
  4. After overfitting begins, RIS MSE increases again
- **Key insight:** The minimum validation loss (early stopping point) roughly
  corresponds to the best RIS estimate. This motivates using early stopping
  based on hold-out NLL to select when to stop training the behavior policy
  model.
- **OIS constancy:** OIS does not use the trained model, so its MSE and value
  estimates are constant across training steps. OIS serves as a fixed
  reference baseline.
- **Domain terminology:**
  - pi_D: the estimated behavior policy (a neural network being trained)
  - Training step: iteration of gradient descent on the behavior policy model
  - Validation/Train Loss: hold-out and training negative log likelihood

### Search Keywords [-> Usefulness]

training curves, MSE, negative log likelihood, validation loss, train loss,
overfitting, early stopping, importance sampling, RIS, OIS, True Value,
behavior policy, Hopper, MuJoCo, training dynamics, model selection,
policy evaluation, off-policy, ICML 2019, confidence bands

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Three line charts stacked vertically" (no panel identification, no line labels, misses the vertical reference line) | "3-panel training curves: NLL (top), MSE (middle), Value (bottom); vertical dashed line marks min validation loss; RIS MSE shows U-shaped pattern" (correct structure and key pattern) | All panel labels and line identities correct; notes RIS MSE valley, OIS constancy, True Value convergence; identifies validation/train loss crossing; correct y-axis ranges per panel |
| Specificity | "Lines going up and down in three charts" (no values, no line names) | "Top: NLL 2.26-2.34 with validation and train loss; Middle: MSE 0-700 with RIS dropping then rising; Bottom: Value 0-300 with True Value at ~130" (approximate values per panel) | Cites approximate values (RIS MSE minimum ~100-200, True Value ~130, validation min ~2.27); identifies line styles (solid vs dashed vs dotted) and colors per panel; notes confidence bands |
| Completeness | Mentions only one or two of the three panels; misses the vertical reference line or the annotation | Covers all 3 panels, the vertical dashed line, legends, and axis labels; may miss confidence bands or the annotation arrow | All 3 panels with y-axis ranges, all line identities with styles/colors, vertical dashed line, "Min validation loss" annotation, confidence bands, x-axis ticks, shared x-axis label |
| Usefulness | "Training graphs from a paper" (no domain context) | "Training dynamics of importance sampling estimator in Hopper; shows model overfitting degrades RIS quality; OIS is constant baseline" (captures main story) | Explains the early stopping motivation, the relationship between NLL minimum and MSE minimum, OIS constancy rationale, and connects to the paper's argument about model selection for importance sampling |

<br><br>

## doc02-R11 -- Policy and Reward line chart

**Figure reference:** Figure 7a, page 16
**Content type:** chart-simple
**Annotation difficulty:** Easy
**Dimensions:** 386x252 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** Line chart with 3 overlaid functions
- **Y-axis:** No label text; tick marks at 0.00, 0.25, 0.50, 0.75, 1.00,
  1.25, 1.50, 1.75, 2.00
- **X-axis:** No label text; tick marks at 0.0, 0.2, 0.4, 0.6, 0.8, 1.0
- **Subplot label:** "(a) Policy and Reward" below the chart
- **Legend (inside plot, top-right, 2 rows):**
  - Row 1: R-bar-star (green dashed line, displayed as R with overline and
    asterisk) | R (blue dotted line)
  - Row 2: pi (black dash-dot line, displayed as Greek letter)
- **Lines:**
  - **pi (black dash-dot):** A step function -- flat at 0.25 from x=0 to
    x=0.5, vertical jump at x=0.5, then flat at 0.75 from x=0.5 to x=1.0
  - **R-bar-star (green dashed):** Monotonically increasing curve from
    approximately (0, 0.00) to (1.0, ~1.02); slightly concave, consistently
    above the R line in the middle portion of the x-range
  - **R (blue dotted):** Monotonically increasing, approximately linear from
    (0, 0.00) to (1.0, ~1.00); close to a straight diagonal
- **Background:** White, with light gray grid lines at major tick positions
- **No confidence bands or shading** on any line

### Verifiable Facts [-> Accuracy]

- FACT: The subplot label reads "(a) Policy and Reward"
- FACT: There are exactly 3 lines in the chart
- FACT: The legend lists three entries: R-bar-star (green dashed), R (blue
  dotted), pi (black dash-dot)
- FACT: The pi line is a step function with exactly one jump at x=0.5
- FACT: The pi line is flat at 0.25 for x < 0.5
- FACT: The pi line is flat at 0.75 for x >= 0.5
- FACT: Both R-bar-star and R start near 0 at x=0 and end near 1.0 at x=1.0
- FACT: R-bar-star is above R in the middle region (approximately x=0.1 to
  x=0.8)
- FACT: Both R-bar-star and R are monotonically increasing
- FACT: The x-axis range is 0.0 to 1.0
- FACT: The y-axis range is 0.00 to 2.00
- FACT: No axis label text is present (only tick values)

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe the R line as perfectly linear (R = s)
  REALITY: The R line appears approximately linear but may have slight
  curvature; it is close to but not necessarily identical to the identity
  function
- RISK: A model might claim the y-axis goes to 1.0 instead of 2.0
  REALITY: The y-axis extends to 2.00, with tick marks up to 2.00, even
  though no data reaches above ~1.0
- RISK: A model might describe pi as a smooth sigmoid rather than a step
  function
  REALITY: Pi is a discrete step function with a sharp vertical jump at
  x=0.5, not a smooth transition
- RISK: A model might invent specific y-axis or x-axis labels (e.g., "state"
  or "probability")
  REALITY: No axis labels are visible in the chart; only tick values are
  shown
- RISK: A model might describe R-bar-star and R as identical or
  indistinguishable
  REALITY: They are visually distinct -- R-bar-star (green dashed) is
  consistently above R (blue dotted) in the middle region, though they
  converge near x=0 and x=1

### Detail Inventory [-> Specificity]

- 3 line styles: green dashed (R-bar-star), blue dotted (R), black dash-dot
  (pi)
- Pi step function: two levels (0.25 and 0.75), transition at x=0.5
- R-bar-star: slightly concave increasing curve, passes through approximately
  (0.2, ~0.25), (0.5, ~0.55), (0.8, ~0.85)
- R: approximately linear increasing, passes through approximately
  (0.2, ~0.15), (0.5, ~0.50), (0.8, ~0.75)
- Y-axis ticks at every 0.25 from 0.00 to 2.00
- X-axis ticks at every 0.2 from 0.0 to 1.0
- Legend uses mathematical notation: R with overline and asterisk, Greek pi
- Light gray grid lines at major tick positions
- Small image (386x252 pixels original)

### Domain Context [-> Usefulness]

- **Figure caption context:** Figure 7a from the paper's appendix section on
  policy evaluation in a continuous armed bandit task. The caption states:
  "Figure 7(a) shows a reward function, R, and the pdf of a policy, pi, with
  support on the range [0, 1]."
- **What the chart shows:**
  - R: the reward function mapping states to rewards (approximately linear,
    higher states yield higher rewards)
  - R-bar-star: a stretched version of R, adjusted according to the density
    of pi (the evaluation policy)
  - pi: the evaluation policy's probability density function, which assigns
    more probability mass to the upper half of the state space (0.75 vs 0.25)
- **Domain terminology:**
  - Continuous armed bandit: a simplified RL setting with continuous state
    space [0, 1]
  - PDF: probability density function of the policy
  - R-bar-star: the expected reward function stretched to account for
    non-uniform sampling under the policy
- **Why this image matters:** Visualizes the test problem used to demonstrate
  importance sampling behavior in a simple, interpretable domain before
  scaling to complex MuJoCo environments.

### Search Keywords [-> Usefulness]

policy, reward function, continuous armed bandit, step function, PDF,
probability density, importance sampling, R-bar-star, stretched reward,
state space, evaluation policy, ICML 2019, off-policy, SinglePath MDP

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A chart with some lines" (no function names, wrong line descriptions) | "Chart showing reward function R (increasing), stretched reward R-bar-star (increasing), and policy pi (step function at 0.25/0.75) over state space [0,1]" (correct key elements) | All three functions correctly identified with line styles; pi step values (0.25 and 0.75) and transition point (0.5) correct; R and R-bar-star endpoints correct (~0 to ~1); notes R-bar-star above R in the middle region |
| Specificity | "Lines on a graph from 0 to 1" (no function names, no values) | "Three lines: green dashed R-bar-star, blue dotted R, black dash-dot pi; pi jumps from 0.25 to 0.75 at x=0.5" (identifies lines and key value) | Names all line styles and colors; cites pi step values and transition point; notes approximate y-values at intermediate x-positions; identifies y-axis range extends to 2.0 despite data only reaching ~1.0 |
| Completeness | Mentions only one or two of the three lines; misses legend or axis ranges | Covers all 3 lines with colors and styles, x-axis range, y-axis range, and the subplot label | All 3 legend entries with mathematical notation, all line shapes and styles, both axis tick ranges, grid lines, subplot label, relationship between R-bar-star and R |
| Usefulness | "A math chart" (no domain context) | "Policy and reward functions for a continuous bandit test problem in an importance sampling paper" (domain-appropriate) | Explains the roles of R, R-bar-star, and pi in the IS evaluation context; notes the policy's non-uniform density and its relationship to the reward stretching; connects to the paper's test domain progression |

<br><br>

## doc02-R16 -- 3-panel stacked chart (NLL, MSE, Value)

**Figure reference:** Figure 10, page 19
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** 1350x1200 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** 3-panel vertically stacked line charts with shared x-axis
- **Shared x-axis:** "Training Step" (linear scale, range 0 to 1000, ticks at
  0, 200, 400, 600, 800, 1000)
- **Shared vertical reference:** Thick black dashed vertical line at
  approximately step ~200, passing through all three panels; marks the
  approximate point where overfitting begins (min validation loss)

**Top panel -- Neg. Log Likelihood:**
- Y-axis: "Neg. Log Likelihood" (range 5.80 to 6.20, ticks at every 0.05)
- Legend (inside plot, top-right): "Validation" (black/gray dotted) and
  "Train Loss" (red/pink dotted)
- Both lines start high (~6.20), drop steeply during early training
- Validation: reaches minimum ~5.88-5.90 around step ~200, then levels off
  at ~5.92 with a very slight rise
- Train Loss: decreases continuously, reaching ~5.82 by step 1000 (below
  validation line, indicating overfitting)
- Both lines have shaded confidence bands (gray for validation, pink for
  train)

**Middle panel -- MSE:**
- Y-axis: "MSE" (range 0 to 700, ticks at 0, 100, 200, 300, 400, 500, 600,
  700)
- Legend (inside plot, bottom-right): "RIS" (blue solid) and "OIS" (green
  dashed)
- OIS: green horizontal dashed line at ~600 with wide green shaded confidence
  band; constant across training steps
- RIS: blue solid line with dramatic V-shaped transient -- starts at ~700,
  drops sharply to a minimum near ~20-50 around step ~80-100, then rises
  steeply back to ~600 by step ~300, and stabilizes near the OIS level
- Blue confidence band around RIS line
- "Training Step" x-axis label between middle and bottom panels

**Bottom panel -- Value:**
- Y-axis: "Value" (range ~0 to 140, ticks at 20, 40, 60, 80, 100, 120, 140)
- Legend (inside plot, top area): "RIS" (blue solid), "OIS" (green dashed),
  "True Value" (green solid)
- True Value: green solid horizontal line at ~50
- OIS: green dashed line at ~25-30, well below the True Value, with green
  shaded confidence band
- RIS: blue solid line with dramatic spike up to ~140 at step ~50-80 (severe
  overestimation), then sharp drop, crossing through the True Value around
  step ~100, and settling at ~25-30 (underestimation, near OIS level)
- Blue confidence band around RIS line

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 3 vertically stacked panels sharing the x-axis
- FACT: The x-axis ticks are at 0, 200, 400, 600, 800, 1000
- FACT: A thick vertical black dashed line passes through all three panels at
  approximately step ~200
- FACT: The top panel y-axis label reads "Neg. Log Likelihood" with range
  5.80-6.20
- FACT: The top panel legend shows "Validation" and "Train Loss"
- FACT: The middle panel y-axis label reads "MSE" with range 0-700
- FACT: The middle panel legend shows "RIS" (blue solid) and "OIS" (green
  dashed)
- FACT: The OIS line in the middle panel is approximately horizontal at ~600
- FACT: The RIS MSE reaches a minimum far below the OIS level (~20-50 vs
  ~600) at approximately step ~80-100
- FACT: The bottom panel y-axis label reads "Value" with range ~0-140
- FACT: The True Value line is horizontal at approximately 50
- FACT: The OIS value estimate (~25-30) is substantially below the True Value
  (~50)
- FACT: The RIS line in the bottom panel spikes to ~140 before dropping below
  the True Value
- FACT: Shaded regions represent 95% confidence intervals (per the caption)
- FACT: Results are averaged over 200 trials (per the caption)

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe the RIS MSE as monotonically decreasing (as in
  a simpler training curve)
  REALITY: The RIS MSE has a dramatic V-shape -- it drops to near zero at
  step ~80-100, then rises sharply back to ~600. This is NOT a simple
  convergence.
- RISK: A model might assume both OIS and RIS converge to the True Value
  REALITY: Both OIS (~25-30) and RIS (after transient, ~25-30) stabilize well
  BELOW the True Value (~50); both underestimate by approximately 40-50%
- RISK: A model might report the exact step of the MSE minimum
  REALITY: The minimum is approximately at step 80-100 but is not labeled
  precisely
- RISK: A model might confuse the vertical dashed line (~step 200) with the
  MSE minimum (~step 80-100); the caption notes these are close but distinct
  REALITY: The MSE minimum is "slightly before" the overfitting onset (the
  vertical line)
- RISK: A model might describe the RIS spike in the Value panel as noise
  REALITY: The spike is a systematic overestimation pattern: at step ~50-80,
  RIS overestimates the policy value by ~3x (140 vs 50)
- RISK: A model might claim OIS equals the True Value
  REALITY: OIS is visibly below the True Value by a substantial margin
  (~25-30 vs ~50)

### Detail Inventory [-> Specificity]

- 3 panels: Neg. Log Likelihood (top), MSE (middle), Value (bottom)
- Shared x-axis: Training Step, 0-1000
- Vertical dashed line at ~step 200 (overfitting onset)
- Top panel: NLL range 5.80-6.20; validation minimum ~5.88-5.90; train loss
  reaches ~5.82 by step 1000; confidence bands on both lines
- Middle panel: MSE range 0-700; OIS constant at ~600 with green band; RIS
  V-shaped with minimum ~20-50 at step ~80-100 then rises to ~600
- Bottom panel: Value range 0-140; True Value at ~50; OIS at ~25-30; RIS
  spikes to ~140 then settles to ~25-30
- Blue confidence bands on RIS lines in both middle and bottom panels
- Green confidence bands on OIS lines
- "Training Step" label between middle and bottom panels
- Gray grid lines in each panel

### Domain Context [-> Usefulness]

- **Figure caption:** "Figure 10: Mean squared error and estimate of the
  importance sampling estimator during training of pi_D." This is the
  continuous armed bandit domain from the paper's appendix.
- **Key finding visible:** Unlike the Hopper domain (Figure 6/R10), this
  domain shows that:
  1. The RIS MSE has a dramatic V-shaped transient, reaching near zero before
     rising to the OIS baseline level
  2. The RIS value estimate transitions from severe overestimation (~140, 3x
     the True Value) to underestimation (~25-30, about half the True Value)
  3. Both OIS and RIS converge to similar values (~25-30) that substantially
     underestimate the True Value (~50)
- **The transition point:** The caption notes that the MSE minimum corresponds
  to where RIS transitions from overestimation to underestimation. This is
  the optimal early stopping point.
- **95% confidence intervals:** Shaded bands represent 95% CI over 200 trials.
- **Domain terminology:**
  - pi_D: the estimated behavior policy being trained
  - Gradient ascent steps: the training iterations for the policy model
  - Continuous armed bandit: a simplified RL domain with continuous actions

### Search Keywords [-> Usefulness]

training curves, MSE, negative log likelihood, importance sampling, RIS,
OIS, True Value, overestimation, underestimation, continuous armed bandit,
early stopping, policy evaluation, off-policy, behavior policy, overfitting,
confidence interval, ICML 2019, value estimate

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Three training charts showing loss and error" (no panel specifics, misses the dramatic RIS transient) | "3-panel chart: NLL top, MSE middle, Value bottom; RIS MSE drops then rises; RIS value overshoots then underestimates True Value; OIS is constant baseline" (captures key dynamics) | Notes RIS MSE minimum at ~20-50 (step ~80-100) vs OIS at ~600; RIS value spike to ~140 crossing True Value at ~50 then settling to ~25-30; both OIS and RIS underestimate; 95% CI over 200 trials; MSE minimum slightly before overfitting onset |
| Specificity | "Line charts with blue and green lines" (no values, no panel labels) | "NLL range 5.80-6.20, MSE range 0-700, Value range 0-140; True Value at ~50; vertical dashed line at step ~200" (approximate values per panel) | Cites specific values: NLL minimum ~5.88, RIS MSE minimum ~20-50 at step ~80-100, True Value ~50, OIS ~25-30, RIS spike ~140; notes vertical line at ~200 is distinct from MSE minimum at ~80-100 |
| Completeness | Mentions one or two panels; misses the dramatic RIS transient or the True Value discrepancy | Covers all 3 panels, both estimators, the vertical dashed line, and the overestimation-to-underestimation transition | All 3 panels with y-ranges, all line identities and styles, vertical dashed line, RIS transient spike and V-shape, True Value vs OIS discrepancy, confidence bands, x-axis range, figure caption details |
| Usefulness | "Training plots from a paper" (no domain context) | "IS estimator training dynamics in a continuous bandit domain; shows dramatic overestimation-to-underestimation transition; early stopping matters" | Explains the overestimation/underestimation transition, compares behavior to Hopper domain (Figure 6), notes both estimators underestimate True Value, connects to the paper's argument about early stopping for IS |

<br><br>

## doc02-V01 -- SinglePath MDP state diagram

**Figure reference:** Figure 1, page 5
**Content type:** diagram
**Annotation difficulty:** Easy
**Dimensions:** vector

### Visual Inventory

Single-panel state transition diagram rendered as vector art. A horizontal
chain of circle nodes represents states s_0, s_1, ..., s_5. Three states are
drawn explicitly (s_0, s_1, s_5) with an ellipsis ("...") between s_1 and s_5
indicating omitted intermediate states (s_2, s_3, s_4). Above the chain,
curved arrows labeled a_0 connect consecutive states in the forward direction
(s_0 to s_1, s_1 to next, preceding state to s_5). Below each state, curved
arrows labeled a_1 loop back to the same state (self-loops). All elements are
black line art on a white background. The caption is partially visible at the
bottom of the crop.

### Verifiable Facts

- 3 state nodes drawn explicitly: s_0, s_1, s_5 (circles with subscript labels)
- Ellipsis "..." between s_1 and s_5 indicates 3 omitted states (s_2, s_3, s_4)
- Total states: 5 (s_0 through s_4) plus terminal s_5 (caption confirms
  "5 states")
- 2 actions: a_0 and a_1 (caption confirms "2 actions")
- L = 5 (episode length, from caption)
- a_0 arrows: curved arcs above the chain, pointing rightward between
  consecutive states
- a_1 arrows: curved arcs below each state node, forming self-loops
- Agent begins in state 0 (from caption)
- Both actions can either advance (state n to n+1) or stay (remain in state n)
- Caption states: "Not shown: If the agent takes action a_1 it remains in its
  current state with probability 0.5"
- This implies a_0 has a different (lower) probability of staying; exact value
  not stated in the visible caption
- Figure number: "Figure 1" (from caption)
- Paper title fragment visible at top of crop: "Importance Sampling Policy
  Evaluatio[n]"

### Hallucination Risks

- **Transition probabilities:** The diagram shows only topology (arrows), not
  probabilities. The caption reveals a_1 stay probability = 0.5 but does NOT
  state a_0's probabilities in the visible portion. An annotator might invent
  specific probability values for a_0.
- **Reward structure:** No rewards are shown or labeled in the diagram. An
  annotator might fabricate reward values or assign rewards to specific
  transitions.
- **Terminal state behavior:** Whether s_5 is absorbing or has outgoing
  transitions is not shown. The a_0 arrow at s_5 curves above the node but
  the destination is ambiguous -- it may be a self-loop at the terminal state.
- **Direction semantics:** The a_1 arrows visually suggest self-loops, but the
  caption says both actions can advance OR stay. An annotator might claim a_1
  always stays (the visual suggests this) when in reality a_1 stays with only
  p=0.5.
- **Number of states:** An annotator might count 6 states (s_0 through s_5)
  when the caption says "5 states" -- clarification needed from the paper
  whether s_5 is the 5th or 6th state (likely 6 states with indices 0-5 but
  the caption says "5 states, 2 actions, and L=5").

### Detail Inventory

- **State nodes:** 3 explicitly drawn circles (s_0, s_1, s_5), subscript
  notation uses italic s with subscript digit
- **Omitted states:** Horizontal ellipsis "..." centered between s_1 and s_5
- **a_0 arrows:** 3 visible curved arcs above the chain; each has an arrowhead
  pointing right; labeled "a_0" in italic with subscript 0
- **a_1 arrows:** 3 visible curved arcs below each drawn state; each loops
  back to the same node; labeled "a_1" in italic with subscript 1
- **Layout:** Left-to-right linear chain, evenly spaced
- **Typography:** Math italic for state and action labels; subscripts in
  regular weight
- **Border:** Thin horizontal rule at the very top of the crop (paper column
  separator), not part of the figure
- **Caption text:** Partially visible at bottom, begins "Figure 1: The
  SinglePath MDP..."

### Domain Context

- The SinglePath MDP is a toy evaluation domain used in off-policy evaluation
  (OPE) research to study importance sampling estimators
- "L = 5" is the episode horizon (maximum number of steps)
- The simplicity of the domain (linear chain, 2 actions, known dynamics) makes
  it possible to compute ground-truth policy values analytically
- This environment is one of several benchmarks in the paper; others include
  Gridworld, Hopper, and continuous bandit domains
- The stochastic transitions (both actions can advance or stay) create variance
  in importance sampling weights, which is the central challenge the paper
  addresses

### Search Keywords

state transition diagram, MDP, Markov decision process, SinglePath,
importance sampling, off-policy evaluation, state nodes, self-loop,
linear chain, episode horizon, stochastic transitions, reinforcement learning,
toy domain, ICML 2019

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A diagram showing circles connected by arrows" (no state labels, no action labels) | "State transition diagram with states s_0 through s_5 connected by action a_0 (forward) and a_1 (self-loop); 5 states, 2 actions" (captures structure) | Notes 3 explicit states with ellipsis for omitted ones; a_0 forward arcs above, a_1 self-loops below; caption reveals a_1 stay probability = 0.5; L = 5 horizon; agent starts in s_0 |
| Specificity | "Circles and arrows" (no labels read) | "States labeled s_0, s_1, ..., s_5; actions labeled a_0 and a_1; linear left-to-right layout" (reads all labels) | All label typography (italic, subscripts), arrow curvature direction (a_0 above, a_1 below), ellipsis notation for omitted states, partial caption content including the "Not shown" probability detail |
| Completeness | Mentions circles but misses action labels or self-loops | Covers states, actions, forward transitions, and self-loops; notes the linear chain structure | All visual elements (nodes, arrows, ellipsis, caption fragment, paper title bleed, top rule), both arrow types with positions, caption "Not shown" detail about a_1 probability |
| Usefulness | "A graph from a paper" (no domain context) | "MDP state transition diagram for a toy reinforcement learning domain with 5 states and 2 actions; used for off-policy evaluation experiments" | Explains role as a toy OPE benchmark, connects to importance sampling variance challenge, notes the linear chain makes analytical computation possible, identifies as Figure 1 from ICML 2019 paper on IS policy evaluation |

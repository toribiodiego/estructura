# Image Analysis: Doc 04 -- 04_anthropic_economic_index.pdf

**Document:** `04_anthropic_economic_index.pdf`
**Format:** PDF
**Source:** https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf
**Category:** vector-heavy
**Images:** 22
**Document context:** Anthropic Economic Index report analyzing global AI usage
patterns, geographic distribution, occupation-level adoption, and economic
implications based on Claude usage data.

<br><br>

## doc04-V01 -- 8-panel grid of line charts

**Figure reference:** Figure 1.1, page 8
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector


### Visual Inventory [-> Completeness]

- **Layout:** 4x2 grid of 8 individual area charts sharing the same visual
  design
- **Overall title:** "Usage share trends across economic index reports (V1 to
  V3)"
- **Chart style:** Orange line with light tan area fill beneath; 3 annotated
  data points per panel with percentage labels
- **Shared x-axis:** Jan 2025, Mar 2025, Aug 2025
- **Shared y-axis label:** "Percentage" (scales differ per panel)
- **Figure caption (partial):** "Figure 1.1: Claude.ai usage over time Each
  panel shows the share of sampled conversations on Claude.ai associated with
  tasks from each SOC major group..."

**Panel data (top row, left to right):**

| Panel | Title | Jan 2025 | Mar 2025 | Aug 2025 | Y-axis max | Trend |
|-------|-------|----------|----------|----------|------------|-------|
| 1 | Computer and Mathematical | 37.2% | 39.6% | 36.9% | 40 | Rises then falls |
| 2 | Arts, Design, Entertainment, Sports, and Media | 10.2% | 9.4% | 8.5% | 14 | Steady decline |
| 3 | Educational Instruction and Library | 9.3% | 11.0% | 12.7% | 14 | Steady rise |
| 4 | Office and Administrative Support | 7.8% | 7.0% | 8.4% | 8 | Dips then rises |

**Panel data (bottom row, left to right):**

| Panel | Title | Jan 2025 | Mar 2025 | Aug 2025 | Y-axis max | Trend |
|-------|-------|----------|----------|----------|------------|-------|
| 5 | Life, Physical, and Social Science | 6.3% | 6.8% | 7.4% | 8 | Steady rise |
| 6 | Business and Financial Operations | 5.9% | 4.4% | 3.1% | 6 | Steep decline |
| 7 | Architecture and Engineering | 4.7% | 3.8% | 2.5% | 5 | Steep decline |
| 8 | Management | 4.5% | 3.1% | 2.7% | 5 | Steep decline |


### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 8 panels arranged in a 4x2 grid
- FACT: The overall title reads "Usage share trends across economic index
  reports (V1 to V3)"
- FACT: Computer and Mathematical is the largest category at all 3 time
  points (37.2%, 39.6%, 36.9%)
- FACT: Educational Instruction and Library shows the largest increase (9.3%
  to 12.7%, +3.4 percentage points)
- FACT: Business and Financial Operations shows a steep decline (5.9% to
  3.1%, -2.8 percentage points)
- FACT: Architecture and Engineering shows the steepest proportional decline
  (4.7% to 2.5%, nearly halved)
- FACT: Management is the smallest category by Aug 2025 at 2.7%
- FACT: All panels share the same x-axis time points: Jan 2025, Mar 2025,
  Aug 2025
- FACT: Y-axis scales vary across panels (top-left goes to 40, others to
  14, 8, 6, or 5)
- FACT: Office and Administrative Support is the only category with a
  non-monotonic trend (7.8% -> 7.0% -> 8.4%)
- FACT: Each data point has an explicit percentage label annotation
- FACT: The y-axis label on every panel reads "Percentage"


### Hallucination Risks [-> Accuracy]

- RISK: Stating the panels represent different models or products
  REALITY: All panels show SOC (Standard Occupational Classification) major
  groups for Claude.ai usage
- RISK: Claiming there are more or fewer than 8 panels
  REALITY: Exactly 8 panels in a 4x2 grid
- RISK: Confusing the y-axis scale across panels (e.g., saying Management
  at 2.7% is on the same scale as Computer and Mathematical at 36.9%)
  REALITY: Each panel has its own y-axis scale
- RISK: Reporting wrong percentage values or swapping values between panels
  REALITY: All 24 values are explicitly labeled on the chart
- RISK: Claiming "all categories decline" or "all categories rise"
  REALITY: Mixed trends -- 3 rise (Educational, Life/Physical/Social,
  Office/Admin after dip), 4 decline (Arts, Business, Architecture,
  Management), 1 roughly flat (Computer/Math)
- RISK: Inventing a legend or color coding for different data series
  REALITY: Each panel has a single orange line with tan area fill; there is
  no legend and no multi-series comparison within panels


### Detail Inventory [-> Specificity]

- All 8 panel titles (SOC major group names)
- All 24 data point values (3 per panel)
- The overall figure title text
- The x-axis time points (Jan 2025, Mar 2025, Aug 2025)
- The y-axis label ("Percentage") and that scales differ
- The chart style (area chart with orange line and tan fill)
- The trend direction for each panel
- The figure caption reference to "sampled conversations on Claude.ai" and
  "SOC major group"
- That Computer and Mathematical dominates (>35%) while the bottom 4
  categories are all under 8%
- The V1/V2/V3 reference in the title (corresponding to the 3 time points)


### Domain Context [-> Usefulness]

This figure is from the Anthropic Economic Index, an analysis of how
Claude.ai usage maps to Standard Occupational Classification (SOC) major
groups. The 8 panels show the top 8 occupation categories by usage share.
"V1 to V3" in the title refers to three successive versions of the economic
index report (corresponding to data from Jan, Mar, and Aug 2025).

The key finding visible in this figure is that Computer and Mathematical
occupations dominate Claude.ai usage (>35% share) but the composition is
shifting: Educational usage is growing rapidly while Business/Financial,
Architecture/Engineering, and Management are declining.


### Search Keywords [-> Usefulness]

Claude.ai usage, occupation categories, SOC major groups, usage share
trends, economic index, Anthropic, Computer and Mathematical, Educational
Instruction, area chart, line chart, grid chart, AI adoption by occupation,
workforce AI usage, V1 V2 V3 reports


### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|----------------|-----------------|---------------------|
| Accuracy | "8 line charts showing AI model performance" (wrong subject -- these are occupation usage shares, not model performance) | "8-panel chart showing Claude.ai usage by occupation category with trends from Jan to Aug 2025" (correct subject, no value errors) | Correctly identifies all 8 categories, trend directions, and notes varying y-axis scales |
| Specificity | "Grid of line charts with percentages" (no categories named, no values cited) | "Computer and Mathematical is the largest at ~37%, Educational Instruction is growing" (some values and trends) | Names all 8 categories with all 24 percentage values and describes each trend direction |
| Completeness | Mentions only 1-2 panels, ignores the grid structure | Covers most panels and the overall title, mentions the SOC context | Covers all 8 panels, the title, caption context, time range, y-axis variation, and chart style |
| Usefulness | "Charts about percentages" (no searchable context) | "Claude.ai occupation usage trends from Anthropic Economic Index" (searchable) | Links to SOC classification, identifies V1/V2/V3 report versions, notes the dominance of Computer/Math and growth of Educational categories |

<br><br>

## doc04-V03 -- Top 30 countries vertical bar chart

**Figure reference:** Figure 2.1, page 13
**Content type:** chart-simple
**Annotation difficulty:** Easy
**Dimensions:** vector

Note: Catalog says "Top 20 countries horizontal bar chart" but the actual
figure shows 30 countries as a vertical bar chart. Corrected here.


### Visual Inventory [-> Completeness]

- **Chart type:** Vertical bar chart with 30 bars in descending order
- **Title:** "Top 30 countries by share of global Claude usage"
- **Y-axis label:** "Share of global usage (%)", scale 0 to ~22
- **X-axis:** 30 country names, rotated at an angle
- **Bar style:** Orange gradient -- darker orange for higher-value bars,
  progressively lighter/tan for lower values
- **Data labels:** Each bar has a percentage label above it
- **Figure caption:** "Figure 2.1: Leading countries in terms of global
  Claude.ai usage share The data includes Claude.ai Free and Pro
  conversations."

**All 30 bars (left to right):**

| Rank | Country | Share |
|------|---------|-------|
| 1 | United States | 21.6% |
| 2 | India | 7.2% |
| 3 | Brazil | 3.7% |
| 4 | Japan | 3.7% |
| 5 | Korea | 3.7% |
| 6 | United Kingdom | 3.2% |
| 7 | Germany | 2.6% |
| 8 | France | 2.2% |
| 9 | Canada | 2.1% |
| 10 | Australia | 1.9% |
| 11 | Indonesia | 1.9% |
| 12 | Italy | 1.5% |
| 13 | Thailand | 1.3% |
| 14 | Israel | 1.1% |
| 15 | Vietnam | 1.1% |
| 16 | Spain | 1.1% |
| 17 | Turkey | 1.1% |
| 18 | Poland | 1.0% |
| 19 | Taiwan | 1.0% |
| 20 | Pakistan | 1.0% |
| 21 | Mexico | 1.0% |
| 22 | Philippines | 0.9% |
| 23 | Colombia | 0.8% |
| 24 | Netherlands | 0.8% |
| 25 | Nigeria | 0.7% |
| 26 | Argentina | 0.6% |
| 27 | Ukraine | 0.6% |
| 28 | Egypt | 0.6% |
| 29 | Singapore | 0.6% |
| 30 | South Africa | 0.5% |


### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 30 bars (not 20 as the catalog states)
- FACT: This is a vertical bar chart, not horizontal
- FACT: The United States has the highest share at 21.6%
- FACT: India is second at 7.2% -- a ~3x gap from the US
- FACT: Brazil, Japan, and Korea are tied at 3.7% each
- FACT: The United Kingdom is 6th at 3.2%
- FACT: The bottom 5 countries (Argentina through South Africa) range from
  0.5% to 0.6%
- FACT: All 30 bars have explicit percentage labels
- FACT: The caption specifies "Claude.ai Free and Pro conversations"
- FACT: The y-axis label reads "Share of global usage (%)"
- FACT: The bars use a gradient coloring (darker orange to lighter tan)
- FACT: Israel, Vietnam, Spain, and Turkey are all tied at 1.1%
- FACT: Poland, Taiwan, Pakistan, and Mexico are all tied at 1.0%


### Hallucination Risks [-> Accuracy]

- RISK: Calling this a "horizontal bar chart" (as the catalog does)
  REALITY: It is a vertical bar chart with country names on the x-axis
- RISK: Saying there are 20 countries (as the catalog says)
  REALITY: There are 30 countries
- RISK: Misidentifying truncated country names (e.g., "Kingdom" could be
  confused with other kingdoms)
  REALITY: The rotated labels are partially cropped; "Kingdom" is United
  Kingdom based on position and the 3.2% value matching the body text
- RISK: Claiming China appears in the chart
  REALITY: China is not among the 30 countries shown
- RISK: Inventing specific values for bars that are hard to distinguish
  visually (e.g., the four 1.0% bars)
  REALITY: All values are explicitly labeled, no estimation needed
- RISK: Saying the data represents "all Anthropic products" or "API usage"
  REALITY: Caption specifies Claude.ai Free and Pro conversations only


### Detail Inventory [-> Specificity]

- All 30 country names in rank order
- All 30 percentage values
- The large gap between US (21.6%) and India (7.2%)
- The three-way tie at 3.7% (Brazil, Japan, Korea)
- The four-way ties at 1.1% and 1.0%
- The gradient bar coloring scheme
- The y-axis label and scale
- The figure caption text including "Free and Pro conversations"
- The chart title specifying "Top 30" and "global Claude usage"
- The long-tail distribution shape (steep drop after US, then gradual
  decline)


### Domain Context [-> Usefulness]

This figure appears in Chapter 2 ("Claude diffusion across the globe") of
the Anthropic Economic Index. The surrounding text notes that "the United
States accounts for the highest share (21.6%), with the next highest usage
countries showing significantly lower shares (India at 7.2%, Brazil at
3.7%)" and that "this concentration is affected by the population size of
each country -- larger countries may have larger usage shares purely because
of their population size." The per-capita analysis appears in the next
figure (Figure 2.2).


### Search Keywords [-> Usefulness]

Claude usage by country, global Claude adoption, geographic distribution,
Anthropic Economic Index, United States India Brazil, top 30 countries,
usage share, bar chart, Claude.ai Free and Pro, international AI adoption,
country-level AI usage


### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|----------------|-----------------|---------------------|
| Accuracy | "Bar chart of AI usage by country" (vague, no values) | "Vertical bar chart of top 30 countries by Claude usage share; US leads at 21.6%, India second at 7.2%" (correct key facts) | All 30 countries and values correct, notes gradient coloring, identifies caption scope (Free and Pro) |
| Specificity | "Bar chart showing countries" (no counts, no values) | "30 countries shown, US dominates at 21.6%, long-tail distribution" (key pattern identified) | Lists all 30 countries with values, notes ties (Brazil/Japan/Korea at 3.7%), identifies the 3x gap between #1 and #2 |
| Completeness | Mentions US bar only, misses the other 29 | Covers top 5-10 countries, mentions the gradient and y-axis | All 30 countries, chart title, caption, y-axis, gradient, distribution shape |
| Usefulness | "Chart about countries" (not searchable) | "Claude.ai global usage distribution from Anthropic Economic Index" (searchable) | Links to Chapter 2 geographic analysis, notes Free/Pro scope, identifies the population-size caveat from surrounding text |

<br><br>

## doc04-V05 -- World choropleth map by AI Usage Index

**Figure reference:** Figure 2.3, page 15
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector


### Visual Inventory [-> Completeness]

- **Chart type:** World choropleth map with countries colored by tier
- **Title:** "Anthropic AI Usage Index tiers by country"
- **Legend title:** "Anthropic AI Usage Index tier"
- **Legend tiers (7 categories, top to bottom):**
  1. Leading (top 25%) -- dark orange
  2. Upper middle (50-75%) -- medium orange
  3. Lower middle (25-50%) -- light orange/peach
  4. Emerging (bottom 25%) -- very light tan
  5. Minimal -- light gray
  6. Claude not available -- medium gray
  7. No data -- lightest gray
- **Legend position:** Bottom-left corner, overlapping South America
- **Map projection:** Standard world map (likely Mercator or equirectangular),
  showing all continents with country borders
- **Figure caption:** "Figure 2.3: Claude diffusion varies across countries,
  with countries in North America, Europe and Oceania leading in Claude
  adoption per working-age capita The different tiers reflect a country's
  position within the global distribution of the Anthropic AI Usage Index
  as defined in this chapter.5,6"

**Observable country colorings by region:**

- **North America:** US and Canada both dark orange (Leading)
- **Europe:** Western Europe largely dark or medium orange (UK, France,
  Germany, Scandinavia appear Leading or Upper middle); Eastern Europe
  mixed lighter tones
- **South America:** Brazil appears medium orange; other countries range
  from light orange to tan
- **Asia:** Japan and South Korea dark orange (Leading); India medium
  orange; China appears gray (Claude not available); Southeast Asia mixed
  (lighter tones); Middle East mixed
- **Africa:** Mostly light gray to tan (Minimal/Emerging), some countries
  medium
- **Oceania:** Australia dark orange (Leading); New Zealand dark orange

**Prominent gray (Claude not available) regions:** China is the most
visually prominent gray country. Several other countries also appear gray,
indicating Claude is not available there.


### Verifiable Facts [-> Accuracy]

- FACT: The legend has exactly 7 categories: Leading, Upper middle, Lower
  middle, Emerging, Minimal, Claude not available, No data
- FACT: The tier definitions use percentile quartiles (top 25%, 50-75%,
  25-50%, bottom 25%) plus Minimal and not-available
- FACT: The title reads "Anthropic AI Usage Index tiers by country"
- FACT: The caption references "per working-age capita" adoption
- FACT: The US and Canada are both in the darkest (Leading) tier
- FACT: Australia is in the Leading tier
- FACT: China appears gray (Claude not available)
- FACT: The caption references chapter footnotes 5 and 6
- FACT: The legend is positioned in the bottom-left corner of the map
- FACT: Africa is predominantly in lighter tiers (Emerging/Minimal)
- FACT: The caption bold text reads "Claude diffusion varies across
  countries, with countries in North America, Europe and Oceania leading"


### Hallucination Risks [-> Accuracy]

- RISK: Assigning specific AUI numeric values to countries from the map
  REALITY: The map shows tier categories only, not numeric values; AUI
  ranges appear in Table 2.1 which is a separate element below the map
- RISK: Listing exact countries in each tier based on color interpretation
  REALITY: Small countries are hard to distinguish on a choropleth; only
  large, clearly colored countries can be confidently identified
- RISK: Claiming Russia or China are in a specific usage tier
  REALITY: China appears gray (not available); Russia's color is ambiguous
  at this resolution
- RISK: Stating the number of countries in each tier
  REALITY: Country counts come from Table 2.1 (not part of this figure),
  not from visually counting on the map
- RISK: Confusing "Minimal" (light gray, has population data but no usage)
  with "No data" (lightest gray)
  REALITY: These are distinct legend categories; both appear as gray tones
  that are hard to distinguish on small countries
- RISK: Describing this as showing "total usage" or "number of users"
  REALITY: Caption specifies "per working-age capita" -- this is a
  normalized index, not raw usage volume


### Detail Inventory [-> Specificity]

- All 7 legend categories with their color descriptions
- The percentile-based tier definitions (top 25%, 50-75%, etc.)
- The chart title and legend title text
- The full caption text including "per working-age capita" qualifier
- Regional patterns: North America/Europe/Oceania leading, Africa mostly
  Emerging/Minimal, China not available
- Specific identifiable countries by tier (US, Canada, Australia, Japan,
  South Korea in Leading; India, Brazil in middle tiers; China gray)
- The legend's bottom-left positioning
- The map projection style showing all continents
- The footnote references (5, 6) in the caption
- The color gradient scheme from dark orange through tan to gray


### Domain Context [-> Usefulness]

This figure appears in Chapter 2 of the Anthropic Economic Index, in the
section on geographic distribution of Claude usage. The preceding text
explains that the AI Usage Index (AUI) normalizes raw usage by
working-age population to account for country size differences. Countries
are assigned to quartile-based tiers. The surrounding text notes that
"countries in North America, Europe and Oceania" lead in per-capita
adoption.

Table 2.1 (separate from this figure, below it on the same page) provides
the tier definitions with AUI ranges and country counts: Leading (37
countries, AUI 1.84-7.00), Upper middle (35, 0.89-1.71), Lower middle
(39, 0.37-0.85), Emerging (53, 0.01-0.36), Minimal (25, 0.00).


### Search Keywords [-> Usefulness]

choropleth map, world map, AI Usage Index, Anthropic Economic Index,
Claude adoption by country, geographic distribution, per capita AI usage,
Leading tier, Emerging tier, global AI adoption, country-level comparison,
working-age capita, AUI tiers


### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|----------------|-----------------|---------------------|
| Accuracy | "World map showing AI usage" (misses the tier system and per-capita normalization) | "Choropleth map of Anthropic AI Usage Index tiers; US, Canada, Australia in Leading tier; China not available" (correct key facts) | Correctly identifies all 7 legend categories, notes per-capita normalization, identifies regional patterns without overclaiming specific small-country tiers |
| Specificity | "Map with colors showing countries" (no tiers named, no regions identified) | "7-tier color scheme from Leading (dark orange) to No data (gray); North America and Europe mostly Leading/Upper middle" (tier structure described) | Names all 7 tiers with percentile definitions, identifies specific countries per tier, describes the color gradient, notes China gray |
| Completeness | Mentions only the map, ignores legend and caption | Covers map, legend categories, and a few identifiable countries | All 7 legend tiers, regional patterns for all continents, caption text including per-capita qualifier, footnote references, legend positioning |
| Usefulness | "A colorful world map" (not searchable) | "Anthropic AI Usage Index choropleth showing global Claude adoption tiers" (searchable) | Links to AUI methodology, explains per-capita normalization, identifies which regions lead and which lag, notes China unavailability |

<br><br>

## doc04-V06 -- Income vs AUI scatter plot, log scale

**Figure reference:** Figure 2.4, page 17
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector


### Visual Inventory [-> Completeness]

- **Chart type:** Scatter plot with regression line and color-coded points
- **Title:** "Income and Anthropic AI Usage Index by country"
- **X-axis:** "ln(GDP per working-age capita in USD)", range approximately
  7 to 12+
- **Y-axis:** "ln(Anthropic AI Usage Index)", range approximately -3 to 2+
- **Both axes on log scale** (natural logarithm)
- **Regression line:** Dashed gray diagonal from lower-left to upper-right
- **Legend (top-right):** "Power law: AUI ~ GDP^0.69"
- **Statistics box (top-left):** beta = 0.690 (p < 0.001), R-squared = 0.709
- **Color bar (right side):** Vertical gradient from dark orange (high AUI,
  ~2) to light tan (low AUI, ~-3), labeled "ln(Anthropic AI Usage Index)"
- **Data points:** Country dots labeled with 3-letter ISO codes, colored by
  their AUI value matching the color bar gradient
- **Figure caption:** "Figure 2.4: Claude usage per capita is positively
  correlated with income per capita across countries We only include
  countries with at least 200 observations in our sample for this figure
  because of the uncertainty of the measure for low-usage countries in our
  random sample. Axes are on a log scale, highlighting a power law
  distribution. Each country is represented by its 3-letter ISO code."

**Notable country positions:**

- **Above regression line (higher AUI than income predicts):** ISR (Israel,
  highest AUI overall), GEO (Georgia, well above line for its income),
  KOR, SGP
- **On/near regression line:** USA, AUS, NZL, GBR, CAN, FRA, DEU, JPN,
  BRA, IND
- **Below regression line (lower AUI than income predicts):** QAT, SAU,
  KWT, OMN (oil-rich Gulf states -- high income but low AUI)
- **Lowest (bottom-left):** MDG, MOZ, TZA, UGA, BFA (low-income African
  countries)
- **Highest income (rightmost):** LUX, CHE, NOR, IRL, SGP


### Verifiable Facts [-> Accuracy]

- FACT: The title reads "Income and Anthropic AI Usage Index by country"
- FACT: beta = 0.690 with p < 0.001
- FACT: R-squared = 0.709
- FACT: The legend states "Power law: AUI ~ GDP^0.69"
- FACT: Both axes use natural logarithm (ln) scale
- FACT: X-axis label is "ln(GDP per working-age capita in USD)"
- FACT: Y-axis label is "ln(Anthropic AI Usage Index)"
- FACT: ISR (Israel) appears as the highest point on the y-axis (~2+)
- FACT: Countries are labeled with 3-letter ISO codes
- FACT: The caption states a minimum of 200 observations threshold
- FACT: The color bar on the right maps point color to ln(AUI) values
- FACT: Gulf states (QAT, SAU, KWT, OMN) cluster below the regression
  line at relatively high income levels
- FACT: The positive slope indicates higher income correlates with higher
  Claude usage per capita


### Hallucination Risks [-> Accuracy]

- RISK: Reporting precise x,y coordinate values for specific countries
  REALITY: The log-scale axes and dense point clustering make precise
  coordinate reading unreliable; only relative positions and clear
  outliers can be confidently identified
- RISK: Claiming the R-squared is 0.71 or rounding differently
  REALITY: The statistics box explicitly shows R-squared = 0.709
- RISK: Calling this a "linear regression" without qualification
  REALITY: This is a power-law fit (AUI ~ GDP^0.69) shown on log-log
  axes, which appears linear on the log scale
- RISK: Listing country names instead of ISO codes
  REALITY: The chart uses 3-letter ISO codes only; a model might
  misidentify codes (e.g., confusing GEO=Georgia with the US state)
- RISK: Claiming China or Russia appear on the chart
  REALITY: CHN does not appear (Claude not available); RUS may or may
  not be visible in the dense middle region -- unclear at this resolution
- RISK: Stating the number of countries shown
  REALITY: The exact count is not labeled; caption says "countries with
  at least 200 observations" without stating how many qualified
- RISK: Interpreting the color gradient as representing a different variable
  REALITY: The color bar maps to ln(AUI), the same as the y-axis -- it
  provides redundant visual encoding, not a third variable


### Detail Inventory [-> Specificity]

- Chart title and both axis labels with units
- The power-law equation in the legend (AUI ~ GDP^0.69)
- The beta coefficient (0.690) and R-squared (0.709) with p-value
- The color bar and its range
- The dashed gray regression line style
- ISO code labels on all visible points
- Israel as the highest-AUI outlier
- Gulf states cluster below the line (high income, low AUI)
- African countries in the lower-left corner
- Wealthy European/Oceania countries in the upper-right
- Georgia (GEO) as a positive outlier (above line at low income)
- The caption's 200-observation minimum threshold
- The log-log axis interpretation (power-law relationship)
- The caption's note that "Axes are on a log scale, highlighting a
  power law distribution"


### Domain Context [-> Usefulness]

This figure appears in Chapter 2 of the Anthropic Economic Index,
demonstrating that national income is the strongest predictor of per-capita
Claude usage. The power-law relationship (AUI ~ GDP^0.69) with R-squared
of 0.709 means income explains about 71% of the cross-country variation
in Claude adoption. The exponent 0.69 < 1 implies that AUI grows
sublinearly with income: doubling GDP per capita increases AUI by about
61% (2^0.69), not 100%.

The Gulf states below the regression line suggest that high income alone
is insufficient -- factors like digital infrastructure, workforce
composition, and language/cultural factors also matter. Israel's position
as the highest-AUI country (above even the US) despite lower income
suggests strong tech-sector and knowledge-worker concentration.


### Search Keywords [-> Usefulness]

scatter plot, income vs AI usage, GDP per capita, Anthropic AI Usage
Index, power law, log scale, country-level comparison, R-squared, Israel
outlier, Gulf states, Claude adoption, economic development, cross-country
regression, AUI, ISO country codes


### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|----------------|-----------------|---------------------|
| Accuracy | "Scatter plot of countries showing AI usage" (wrong axis labels, no statistics) | "Log-log scatter of GDP vs AUI per capita with power-law fit; R-squared = 0.709; Israel highest AUI" (correct key facts) | All statistics correct (beta=0.690, R-sq=0.709, p<0.001), identifies power-law equation, notes Gulf states below line, correctly describes log-scale axes |
| Specificity | "Scatter plot with dots and a line" (no axis labels, no countries identified) | "Countries labeled by ISO code; US, Israel, Singapore among highest; African countries lowest; regression line slopes upward" (some specifics) | Names axis labels with units, cites exact statistics, identifies outlier clusters (Israel above, Gulf below), describes color bar encoding |
| Completeness | Mentions scatter plot and regression line only | Covers axes, regression line, statistics box, and several country positions | Statistics box, legend equation, both axis labels, color bar, caption text including 200-observation threshold, regression line style, outlier clusters |
| Usefulness | "Chart about countries and money" (not searchable) | "Income-AUI scatter showing positive correlation across countries from Anthropic Economic Index" (searchable) | Explains power-law interpretation (sublinear growth), contextualizes Gulf state and Israel outliers, links to digital infrastructure and workforce factors |

<br><br>

## doc04-V09 -- 4-panel scatter plots by occupation

**Figure reference:** Figure 2.7, page 22
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector

### 1. Visual Inventory

- 2x2 grid of scatter plots sharing common visual design
- Main title: "Occupation group shares vs Anthropic AI Usage Index"
- Each panel titled with a SOC (Standard Occupation Classification) group name
  in orange/brown text
- X-axis (shared label on bottom panels): "Anthropic AI Usage Index
  (usage % / working-age population %)" ranging 0 to 7
- Y-axis per panel: "Occupation group share (%)" with panel-specific ranges
- Bubble scatter points in each panel: size encodes usage count, color encodes
  AUI tier (5-level categorical: Minimal, Emerging/bottom 25%, Lower middle/
  25-50%, Upper middle/50-75%, Leading/top 25%)
- Dashed regression line in each panel
- Statistics box (top-right of each panel): beta coefficient, p-value,
  R-squared
- Bottom-left panel: color/tier legend ("Anthropic AI Usage Index tier")
- Bottom-right panel: size legend ("Claude usage count" with 100, 1,000,
  10,000 reference circles)
- Caption below: Figure 2.7 description text

### 2. Verifiable Facts

**Top-left panel: Computer and Mathematical**
- Y-axis range: approximately 5% to 55%
- Beta = -0.700, p = 0.385, R-squared = 0.007
- Negative slope (downward dashed line)
- Largest bubble near top-left (~0.5 on x-axis, ~53% on y-axis)
- Most data points clustered in x = 0 to 2 range

**Top-right panel: Educational Instruction and Library**
- Y-axis range: approximately 0% to 25%
- Beta = 0.082, p = 0.858, R-squared = 0.000
- Nearly flat regression line (essentially horizontal around 8%)
- One outlier bubble near top-left (~0.3 on x-axis, ~25% on y-axis)
- Large cluster between x = 0 and 2, y = 2% to 17%

**Bottom-left panel: Arts, Design, Entertainment, Sports, and Media**
- Y-axis range: approximately 2% to 11%
- Beta = 0.357, p = 0.146, R-squared = 0.037
- Slight positive slope
- One large bubble cluster at approximately x = 3, y = 9%
- Tighter spread than other panels (most points between 2% and 10%)

**Bottom-right panel: Office and Administrative Support**
- Y-axis range: approximately 1% to 12%
- Beta = 0.448, p = 0.009, R-squared = 0.091
- Positive slope -- the only statistically significant panel (p < 0.05)
- One outlier at approximately x = 0.8, y = 11.5%
- Rightmost point at approximately x = 7, y = 6%

**Caption text (Figure 2.7):** "As we move from lower to higher adoption
countries, Claude usage appears to shift away from programming-dominant
tasks to a more diverse mix of tasks, though the overall pattern is noisy."
Methodology: SOC share based on O*NET tasks per geography. Only countries
with 200+ observations included. Regression weights every country equally.

### 3. Hallucination Risks

- Individual country ISO codes are NOT labeled on these scatter plots (unlike
  V06). A model may invent country identifications from bubble positions.
- Exact data point coordinates are approximate -- bubbles overlap extensively
  in the x = 0 to 2 cluster region. A model should not claim precise values
  for individual countries.
- The statistical significance distinction (only bottom-right panel has
  p < 0.05) is critical and easy to miss. A model might describe "trends"
  in all panels without noting that three of four are not significant.
- The title says "Anthropic AI Usage Index" but a model may shorten this to
  "AI usage" and lose the specific Anthropic/Claude context.
- The regression lines are dashed (not solid), indicating fitted trends not
  raw data. A model should not describe them as data series.

### 4. Detail Inventory

- 5 AUI tier categories with distinct colors (light beige to dark
  salmon/brown): Minimal, Emerging (bottom 25%), Lower middle (25-50%),
  Upper middle (50-75%), Leading (top 25%)
- 3 bubble size references: 100, 1,000, 10,000 (Claude usage count)
- 4 separate regression statistics boxes, each with beta, p-value, R-squared
- Panel title font: bold orange/brown colored text
- X-axis tick marks at 0, 1, 2, 3, 4, 5, 6, 7
- Y-axis tick marks vary per panel to fit data range
- Light gray grid lines in background of each panel
- Dashed line style for all four regression lines
- Bubble opacity/transparency allows overlapping points to be partially visible
- Caption is bold for the interpretive summary, normal weight for methodology

### 5. Domain Context

This figure explores whether AI usage patterns diversify as adoption
increases. The key finding is that Computer and Mathematical occupation share
(dominated by programming) actually decreases with higher AUI (beta = -0.700)
while Office and Administrative Support increases significantly
(beta = 0.448, p = 0.009). This supports the report's thesis that higher-
adoption countries use AI for a broader range of tasks beyond coding.

SOC groups are U.S. Bureau of Labor Statistics Standard Occupation
Classification categories. O*NET is the Occupational Information Network
that maps tasks to occupations. The AUI (Anthropic AI Usage Index) normalizes
Claude usage by working-age population to compare across countries of
different sizes.

The "noisy" caveat in the caption is important: three of four panels show
non-significant relationships. Only Office and Administrative Support clears
the p < 0.05 threshold.

### 6. Search Keywords

scatter plot, occupation group share, SOC, Standard Occupation Classification,
Anthropic AI Usage Index, AUI, Computer and Mathematical, Educational
Instruction and Library, Arts Design Entertainment Sports Media, Office and
Administrative Support, regression, beta coefficient, R-squared, p-value,
bubble chart, country comparison, AI adoption, task diversification, O*NET,
working-age population, Claude usage count, AUI tier, Figure 2.7

### 7. Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Four scatter plots about different jobs and AI" (no statistics, wrong axis descriptions) | "4-panel scatter of occupation group share vs Anthropic AI Usage Index; identifies that Computer & Mathematical trends negative while Office & Administrative trends positive" (captures main pattern) | All four beta values, p-values, and R-squared values correct; notes only Office & Administrative is statistically significant (p=0.009); correctly describes AUI as usage %/working-age population %; captures caption's "noisy" caveat |
| Specificity | "Scatter plots with dots of different sizes and colors" (no panel names, no numbers) | "Panel titles named correctly; bubble size = usage count; color = AUI tier; regression lines shown with statistics" (structural details present) | Names all 4 SOC groups verbatim; cites exact statistics per panel; describes 5-tier color encoding with category names; identifies 3 size reference values (100, 1K, 10K); notes dashed line style |
| Completeness | Mentions it is a multi-panel scatter plot with regression lines | Covers all 4 panel titles, regression statistics, bubble encoding (size and color), and axis labels | All 4 panels with statistics, both legends (tier + size), axis labels with units, caption text including methodology (200-observation threshold, equal-weight regression), grid lines, title |
| Usefulness | "Chart about jobs and AI usage" (not searchable) | "Cross-country scatter showing occupation diversification with AI adoption; Computer/Math share drops, Office/Admin share rises" (captures key insight) | Explains the diversification thesis (programming-dominant to broader usage), contextualizes SOC/O*NET framework, notes the significant vs non-significant distinction as the key analytical takeaway, connects to report's broader argument about AI usage patterns |

<br><br>

## doc04-V10 -- Overrepresented request clusters

**Figure reference:** Figure 2.8, page 23
**Content type:** infographic
**Annotation difficulty:** Medium
**Dimensions:** vector

### 1. Visual Inventory

- Title: "Top overrepresented requests for the United States, Brazil,
  Vietnam and India"
- 2x2 grid of country panels, each a light pink/beige card with rounded
  corners
- Each panel has a dark brown/salmon banner at top with country name in
  bold white text
- Each panel lists 5 request categories (left-aligned text) with
  overrepresentation multipliers (right-aligned, red/brown text, format
  "N.NNx")
- Rows have subtle alternating background shading
- Figure caption below (Figure 2.8)
- Preceding paragraph text visible above the figure title (body text
  discussing country specialization patterns)

### 2. Verifiable Facts

**United States (top-left panel, 5 rows):**
- Row 1: "Provide comprehensive cooking, nutrition, and meal planning
  assistance" -- 1.43x
- Row 2: "Help with job applications, resumes, and career documents" --
  1.41x
- Row 3: "Provide personal relationship advice and life guidance
  support" -- 1.34x
- Row 4: "Provide comprehensive travel planning and booking assistance"
  -- 1.30x
- Row 5: "Provide comprehensive medical and healthcare guidance across
  multiple specialties" -- 1.29x

**Brazil (top-right panel, 5 rows):**
- Row 1: "Provide translation services and comprehensive language
  learning assistance across multiple languages" -- 6.4x
- Row 2: "Provide comprehensive legal assistance and document drafting
  across multiple practice areas" -- 5.0x
- Row 3: "Help create and optimize comprehensive digital marketing
  content and strategies" -- 1.15x
- Row 4: "Edit and improve existing written content and documents" --
  1.07x
- Row 5: "Assist with game development programming and general gaming
  support" -- 1.01x

**Vietnam (bottom-left panel, 5 rows):**
- Row 1: "Help with cross-platform mobile app development, debugging,
  and feature implementation" -- 1.85x
- Row 2: "Debug and fix web application errors and technical issues" --
  1.73x
- Row 3: "Fix and improve web and mobile application UI layouts,
  styling, and components" -- 1.70x
- Row 4: "Create comprehensive K-12 educational materials and teaching
  resources" -- 1.59x
- Row 5: "Provide comprehensive multi-technology programming development
  assistance and technical guidance" -- 1.48x

**India (bottom-right panel, 5 rows):**
- Row 1: "Fix and improve web and mobile application UI layouts,
  styling, and components" -- 2.4x
- Row 2: "Debug and fix web application errors and technical issues" --
  2.1x
- Row 3: "Help develop, debug, and modify web applications and frontend
  components" -- 2.1x
- Row 4: "Help with cross-platform mobile app development, debugging,
  and feature implementation" -- 2.1x
- Row 5: "Help build complete web applications and websites from
  scratch" -- 2.1x

**Structural facts:**
- Each panel shows exactly 5 request clusters
- All 20 entries are unique text descriptions with multiplier values
- US multipliers range 1.29x-1.43x (narrow, low range)
- Brazil multipliers range 1.01x-6.4x (widest range, most extreme
  outliers)
- Vietnam multipliers range 1.48x-1.85x (moderate range)
- India multipliers range 2.1x-2.4x (tight cluster, all 2x+)

### 3. Hallucination Risks

- A model may truncate or paraphrase the long request descriptions. The
  exact wording matters because these are cluster labels, not summaries.
  For example, "Help with job applications" is not the same as the full
  "Help with job applications, resumes, and career documents."
- The multiplier values have varying decimal precision (6.4x, 5.0x,
  1.43x, 2.1x). A model may normalize these to consistent precision or
  round incorrectly.
- A model may conflate Vietnam's and India's lists since they share
  several overlapping software development categories. Three categories
  appear in both panels with different multipliers. The model must keep
  country attributions correct.
- A model may invent a 6th row or additional detail for panels where the
  rows look similar.
- The preceding body text (visible above the figure title in the crop)
  discusses Brazil as "an early adopter of AI in the judicial system"
  and India having "a large information technology sector." A model
  should not attribute these contextual observations to the figure
  content itself.
- The multiplier "1.01x" for Brazil's 5th row (game development) is
  barely above 1.0x. A model might omit it or misread it as 1.1x.

### 4. Detail Inventory

- Country banner design: dark salmon/brown background with white bold
  text, slightly rounded corners
- Card background: light pink/cream (#FDF0ED or similar warm tone)
- Multiplier text color: red/brown (#C0392B or similar)
- Row dividers: subtle horizontal lines separating entries
- Request description text: dark gray/black, left-aligned, wrapping to
  2-3 lines for longer descriptions
- Panel layout: top-left US, top-right Brazil, bottom-left Vietnam,
  bottom-right India
- Title text: bold, sans-serif, centered above the panels
- White space between panels creates visual separation
- No icons, charts, or visual decorations within panels -- text-only
  layout
- The 5-row structure is consistent across all 4 panels

### 5. Domain Context

This figure illustrates geographic specialization in AI usage patterns.
The overrepresentation metric compares a country's share of a request
type against the global average. A value of 6.4x means Brazil's share
of translation requests is 6.4 times higher than the global share.

The figure uses "middle-level granularity" request clusters (not the
most specific task descriptions, not the broadest categories). This
level was chosen to balance interpretability with specificity.

Key narrative from the surrounding text: US usage is diversified across
non-technical domains (cooking, career, relationships, travel,
healthcare). Brazil has extreme specialization in translation (6.4x) and
legal (5.0x), reflecting its judicial system's early AI adoption.
Vietnam and India are both software development-heavy, but India's
concentrations are stronger (all 5 entries are 2.1x+). Vietnam uniquely
includes K-12 education materials (1.59x).

The 1% frequency threshold means these are common request types, not
niche use cases. The "middle level of granularity" means the clusters
are more aggregated than individual tasks but less aggregated than
top-level categories.

Caption: "Figure 2.8: Overrepresented request clusters for the United
States, Brazil, Vietnam and India. A request is overrepresented in a
country when the share of conversations containing that request is
higher for that country than globally. For this figure, we focus on
request clusters at the middle level of granularity, i.e. more
aggregated than the lowest level request clusters, but less aggregated
than the highest level request clusters. Only includes requests with at
least 1% frequency globally and for that country."

### 6. Search Keywords

overrepresented requests, request clusters, country comparison, United
States, Brazil, Vietnam, India, AI usage patterns, geographic
specialization, translation services, legal assistance, cooking
nutrition, job applications, software development, mobile app
development, web development, debugging, K-12 education, digital
marketing, Anthropic Economic Index, Claude usage, overrepresentation
multiplier, Figure 2.8

### 7. Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Four panels showing different countries and what they use AI for" (no specific categories, no multipliers) | "US panel lists cooking (1.43x), job help (1.41x), relationships (1.34x); Brazil has translation (6.4x) and legal (5.0x); Vietnam and India focus on software development" (captures main patterns and some values) | All 20 row descriptions verbatim with correct multipliers for all 4 panels; notes Brazil's extreme outliers (6.4x, 5.0x) vs US's narrow range (1.29x-1.43x); correctly identifies overlapping categories between Vietnam and India |
| Specificity | "Lists of AI tasks for four countries with numbers" (no descriptions, no multiplier values) | "Names all 4 countries; gives 2-3 request descriptions per panel with multipliers; notes that US is non-technical while India is software-focused" (partial enumeration) | All 20 request descriptions quoted exactly; all 20 multiplier values correct to stated precision; notes varying decimal formats (6.4x vs 1.43x); describes card design (salmon banner, pink background, alternating rows) |
| Completeness | Mentions 4 country panels with some request types | Covers all 4 panels with partial row content, title text, and general layout | All 20 rows with exact text and multipliers, title, caption text including methodology (middle granularity, 1% threshold), panel layout order, visual design elements (banner colors, card styling, text alignment) |
| Usefulness | "Chart comparing AI use in different countries" (not searchable) | "Infographic showing US AI usage favors non-technical tasks (cooking, jobs, healthcare) while Vietnam and India favor software development, with Brazil specializing in translation and legal" (captures key insight) | Explains overrepresentation metric (country share vs global share), notes the contrast between US diversified non-technical usage and South/Southeast Asian software development concentration, contextualizes Brazil's extreme translation/legal values with early judicial AI adoption, connects to geographic specialization thesis |

<br><br>

## doc04-V17 -- 2-panel Lorenz curves + power-law

**Figure reference:** Figure 3.4, page 35
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector

### 1. Visual Inventory

- Main title: "Lorenz curves and power law analysis across tasks: 1P API
  vs Claude.ai" (orange/brown text)
- 2-panel horizontal layout, left and right
- Left panel subtitle: "Lorenz curves" (orange/brown text)
- Right panel subtitle: "Task rank versus usage share" (orange/brown text)

**Left panel (Lorenz curves):**
- X-axis: "Cumulative percentage of tasks" (0 to 100, ticks at 0, 20,
  40, 60, 80, 100)
- Y-axis: "Cumulative percentage of usage" (0 to 100, ticks at 0, 20,
  40, 60, 80, 100)
- Three lines in legend:
  - Gray solid line: "1P API (Gini = 0.842)"
  - Red/orange solid line: "Claude.ai (Gini = 0.822)"
  - Gray dashed line: "Perfect Equality" (45-degree diagonal)
- Annotation box (upper-left area): "The bottom 80% of tasks account
  for: 1P API: 10.5% of usage; Claude.ai: 12.7% of usage"
- Two highlighted data points on the curves at the 80% task mark:
  - Red/orange dot with label "12.7% of usage" (Claude.ai)
  - Gray dot with label "10.5% of usage" (1P API)
- Both Lorenz curves are highly convex, hugging the bottom-right

**Right panel (log-log scatter / power law):**
- X-axis: "ln(Share of usage)" (approximately -2 to 2)
- Y-axis: "ln(Rank by usage)" (approximately 0 to 5)
- Three elements in legend:
  - Gray circles: "1P API: y = -1.11x + 2.51"
  - Red/orange circles: "Claude.ai: y = -1.13x + 2.53"
  - Black dashed line: "Zipf's Law: y = -1.00x + 2.52"
- Data points form a roughly linear descending pattern from upper-left
  (high rank, low usage share) to lower-right (low rank, high usage)
- Scatter increases at the extremes (bottom-right: a few high-usage
  outlier tasks deviate from the linear trend)
- Light gray grid lines in background

### 2. Verifiable Facts

**Left panel:**
- 1P API Gini coefficient = 0.842
- Claude.ai Gini coefficient = 0.822
- Bottom 80% of tasks account for 10.5% of usage (1P API)
- Bottom 80% of tasks account for 12.7% of usage (Claude.ai)
- The Claude.ai curve (red/orange) is slightly closer to the equality
  line than the 1P API curve (gray), consistent with lower Gini
- Both curves start at origin (0,0) and end at (100,100)
- The Perfect Equality line is a 45-degree diagonal from (0,0) to
  (100,100)

**Right panel:**
- 1P API regression: y = -1.11x + 2.51
- Claude.ai regression: y = -1.13x + 2.53
- Zipf's Law reference: y = -1.00x + 2.52
- Both regression slopes are steeper than Zipf's Law (-1.11 and -1.13
  vs -1.00), indicating slightly more concentration than pure Zipf
- The intercepts are nearly identical (2.51, 2.53, 2.52)
- 1P API points (gray) and Claude.ai points (red/orange) are
  interleaved along the trend line, not separated

### 3. Hallucination Risks

- The Gini coefficients (0.842 and 0.822) are close. A model might
  reverse which platform has the higher Gini or describe the difference
  as large when it is only 0.020.
- The annotation box values (10.5% and 12.7%) must be attributed to the
  correct platform. 1P API = 10.5%, Claude.ai = 12.7%. A model may swap
  these.
- The regression equations in the right panel have similar coefficients.
  A model may confuse which slope belongs to which platform (-1.11 is
  1P API, -1.13 is Claude.ai).
- A model may claim individual task names are visible in the scatter
  plot. No task labels appear on either panel.
- The right panel axes are logarithmic (ln-transformed). A model might
  describe them as raw values rather than natural log.
- A model may describe the Lorenz curves as "nearly overlapping" when
  there is visible separation, particularly in the 40-80% range on the
  x-axis where the Claude.ai curve is measurably above the 1P API
  curve.
- The "Perfect Equality" line in the legend might be described as a
  "regression line" or "fit line" by a model. It is a theoretical
  reference line, not fitted.

### 4. Detail Inventory

- Line colors: gray for 1P API, red/orange for Claude.ai, gray dashed
  for Perfect Equality, black dashed for Zipf's Law
- Left panel legend position: below the annotation box, left side
- Right panel legend position: upper-right area, boxed
- Annotation box has a thin black border with white background
- Highlighted points at the 80% mark use filled circles matching line
  colors, with text labels ("12.7% of usage", "10.5% of usage") in
  matching colors
- Right panel data points: semi-transparent circles allowing overlap
  visibility
- Right panel: most points cluster tightly along the linear trend in the
  upper-left to center region; scatter increases at the lower-right
  (highest-usage tasks deviate from the power law)
- Grid lines: light gray, both horizontal and vertical
- Panel titles in orange/brown text, matching the report's heading style

### 5. Domain Context

This figure demonstrates that Claude usage follows a power-law
distribution across O*NET task categories. A small number of tasks
(primarily software development) account for a disproportionate share of
total usage.

The Lorenz curve (left) is a standard inequality visualization: the
further a curve bows from the 45-degree equality line, the more
concentrated the distribution. Gini coefficients (0 = perfect equality,
1 = perfect inequality) of 0.842 (1P API) and 0.822 (Claude.ai)
indicate extreme concentration for both platforms, comparable to wealth
inequality levels in the most unequal economies. The bottom 80% of tasks
account for only 10-13% of usage.

The power-law/Zipf analysis (right) plots the same data in log-log
space. A perfect Zipf's Law distribution (exponent = -1) would appear
as a straight line with slope -1. Both platforms' slopes (-1.11, -1.13)
are slightly steeper than Zipf, meaning usage is even more concentrated
than Zipf predicts. The near-identical intercepts (~2.52) and slopes
suggest both platforms serve very similar task distributions.

Caption: "Figure 3.4: Visualizing concentration of usage among a small
number of tasks: Claude.ai versus 1P API. The left panel of this chart
calculates Lorenz curves across O*NET tasks for both our Claude.ai and
1P API samples. The highlighted points on the curves indicate how much
overall usage the bottom 80% of tasks account for. The right panel plots
task rank against task usage share for tasks representing at least 0.1%
of overall usage in our samples. Zipf's law, in which the coefficient
of the best-fit-line is equal to -1, occurs with some regularity in
various economic settings."

### 6. Search Keywords

Lorenz curve, Gini coefficient, power law, Zipf's law, task
concentration, usage distribution, 1P API, Claude.ai, O*NET tasks,
cumulative percentage, log-log plot, regression, inequality, task rank,
usage share, bottom 80 percent, software development concentration,
Anthropic Economic Index, Figure 3.4

### 7. Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Two charts comparing Claude and API usage" (no Gini values, no regression equations, wrong chart type description) | "Left panel shows Lorenz curves with Gini coefficients (0.842 for 1P API, 0.822 for Claude.ai); right panel is a log-log scatter plot showing power-law behavior" (correct structure and some statistics) | All 4 statistics correct (Gini 0.842/0.822, bottom-80% 10.5%/12.7%); all 3 regression equations correct with slopes and intercepts; notes slopes are steeper than Zipf's -1.00; correctly attributes each value to the right platform |
| Specificity | "Charts with curves and dots comparing two things" (no axis labels, no values, no line descriptions) | "Lorenz panel has gray (1P API) and red (Claude.ai) curves with a diagonal equality line; scatter panel has gray and red data points with regression lines" (structural elements identified) | Names exact Gini values per platform; quotes annotation box text verbatim; gives all 3 regression equations with coefficients; describes highlighted points at 80% mark with labeled values; notes dashed vs solid line styles; identifies ln-scale axes |
| Completeness | Mentions two panels with curves | Covers both panels with axis labels, legend entries, and key statistics | Both panel subtitles, both axis labels with units, all legend entries (6 total across both panels), annotation box, highlighted data points with labels, regression equations, Zipf reference line, grid lines, caption methodology (0.1% threshold, O*NET tasks) |
| Usefulness | "Charts about how people use AI" (not searchable) | "Lorenz curves and power-law analysis showing Claude usage is extremely concentrated among a few tasks (Gini ~0.83)" (captures key insight) | Explains Gini interpretation (extreme inequality comparable to most unequal economies), contextualizes bottom-80%/10-13% finding (vast majority of tasks see minimal usage), interprets slopes steeper than Zipf as super-Zipfian concentration, notes the two platforms have nearly identical distributions despite different user bases |

<br><br>

## doc04-V18 -- 2-panel scatter, automation vs augmentation

**Figure reference:** Figure 3.5, page 37
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector

### 1. Visual Inventory

- Main title: "Automation and augmentation dominance across tasks:
  Claude.ai vs. 1P API" (orange/brown text)
- 2-panel horizontal layout, left and right
- Left panel subtitle: "1P API" (orange/brown text)
- Right panel subtitle: "Claude.ai" (orange/brown text)
- Both panels share identical axis structure:
  - X-axis: "Automation Share (%)" (0 to 100, ticks at 0, 20, 40, 60,
    80, 100)
  - Y-axis: "Augmentation Score (%)" (0 to 100, ticks at 0, 20, 40, 60,
    80, 100)
- Gray dashed 45-degree diagonal line in each panel (where automation
  share = augmentation score)
- Bubble scatter points with two colors:
  - Purple: automation dominant tasks
  - Blue: augmentation dominant tasks
- Bubble size varies (encodes usage volume)
- Each panel has a legend box with percentage breakdown

### 2. Verifiable Facts

**Left panel (1P API):**
- Legend: "Automation dominant (97.9% of Tasks)" (purple),
  "Augmentation dominant (2.1% of Tasks)" (blue)
- Vast majority of points are purple (automation dominant)
- Only a small handful of blue (augmentation dominant) points, scattered
  in the upper-left region (high augmentation, low automation)
- Dense strip of points along y=0 line from approximately x=40% to
  x=100% (tasks with near-zero augmentation score)
- Triangular spread of points: bounded by the x-axis at bottom, the
  diagonal in the upper-right, and tapering off at left
- Largest bubbles cluster in the x=60-100%, y=0-10% region
- Maximum augmentation score approximately 65%
- A few blue outlier points near x=10-30%, y=50-65%

**Right panel (Claude.ai):**
- Legend: "Automation dominant (47.0% of Tasks)" (purple),
  "Augmentation dominant (53.0% of Tasks)" (blue)
- Near-even split between purple and blue points
- Much denser scatter than 1P API -- many more data points visible
- Points fill a broader triangular region, with many above the diagonal
  (augmentation dominant, blue)
- Dense cluster in the center region (approximately x=30-70%,
  y=30-70%)
- Points along y=0 axis extend from approximately x=20% to x=100%
  but are sparser than in 1P API
- Maximum augmentation score approximately 90%+
- Blue points dominate the upper-left quadrant; purple points dominate
  the lower-right
- Several large purple bubbles in the lower-right corner (high
  automation, low augmentation)

**Cross-panel comparison:**
- 1P API: 97.9% automation dominant, only 2.1% augmentation dominant
- Claude.ai: 47.0% automation dominant, 53.0% augmentation dominant
- The shift is dramatic: API usage is nearly all automation; Claude.ai
  is roughly split between automation and augmentation

### 3. Hallucination Risks

- A model may confuse which panel is which. Left = 1P API, right =
  Claude.ai. Getting this backward would invert the entire finding.
- The percentages (97.9%/2.1% vs 47.0%/53.0%) are the most important
  numbers. A model may approximate these (e.g., "about 98%" or "roughly
  half") rather than citing the exact values.
- The 45-degree diagonal is a reference line, not a regression fit. A
  model may describe it as a fitted line or trend line.
- The y-axis label says "Augmentation Score (%)" not "Augmentation
  Share (%)". The x-axis says "Automation Share (%)". A model may
  homogenize these to both be "Share" or both be "Score."
- A model may claim to identify specific task names from point
  positions. No task labels appear on either panel.
- The bubble sizes encode usage volume but no size legend is provided
  in the figure. A model should not claim specific size-to-value
  mappings.
- The caption mentions privacy-preserving zeros: some 0% values are
  real zeros, others are suppressed for privacy. A model may not
  distinguish these, but should note the caveat exists.
- A model may describe the 1P API panel as having "no" augmentation
  dominant tasks when it has 2.1% (a small but nonzero amount with
  visible blue points).

### 4. Detail Inventory

- Point colors: purple/violet for automation dominant, blue/teal for
  augmentation dominant
- Bubble sizes vary within each panel (no explicit size legend)
- The 1P API panel is visually sparse compared to Claude.ai (fewer
  visible data points, or points overlapping heavily at y=0)
- The Claude.ai panel has a much denser scatter with more visual
  variety in the spatial distribution
- Gray dashed diagonal line style consistent across both panels
- Grid lines: light gray, horizontal and vertical
- Panel subtitles centered above each chart, orange/brown text
- The strip of points at y=0 in both panels represents tasks where
  no augmentation usage was observed (or was privacy-suppressed)
- Points along x=0 would represent tasks with no automation usage,
  visible mainly in Claude.ai panel (left edge, blue points at high
  augmentation scores)

### 5. Domain Context

This figure visualizes the fundamental difference between how Claude is
used via its web interface (Claude.ai) versus its API (1P API).
"Automation" means the AI completes a task with minimal human input
(e.g., generating code from a spec). "Augmentation" means the AI
assists a human who remains actively involved (e.g., brainstorming,
editing, iterating).

The finding is striking: API usage is 97.9% automation dominant --
developers build automated pipelines that feed tasks to the API with
minimal human-in-the-loop interaction. Claude.ai usage is roughly split
(47%/53%), reflecting the conversational, iterative nature of chat-based
interaction where humans actively collaborate with the model.

This distinction matters for economic analysis: automation tends to
substitute for human labor (potentially displacing tasks), while
augmentation complements human labor (potentially enhancing
productivity). The different modalities (API vs chat) thus have
different economic implications even when using the same underlying
model.

The privacy-preserving zeros in the caption mean some data points at 0%
are real (the task genuinely has no usage in that mode) while others are
suppressed. This is relevant for interpreting the dense strip at y=0 in
the 1P API panel.

Caption: "Figure 3.5: Automation versus augmentation collaboration modes
across O*NET tasks: Claude.ai versus 1P API. This figure reports the
share of Claude.ai conversations and 1P API transcripts that exhibit
automation or augmentation patterns of usage for each O*NET task.
Automation and augmentation modes are defined in Chapter 1. When for
privacy-preserving reasons we do not observe usage shares for a
particular collaboration mode we give that category a value of 0% in
this figure. Automation dominance is defined as a task having a greater
observed share of automation usage. Likewise for augmentation
dominance."

### 6. Search Keywords

automation, augmentation, collaboration modes, 1P API, Claude.ai,
O*NET tasks, automation dominant, augmentation dominant, scatter plot,
bubble chart, automation share, augmentation score, human-AI
collaboration, task substitution, task complementarity, API vs chat,
economic impact, labor displacement, productivity enhancement, Anthropic
Economic Index, Figure 3.5, privacy-preserving

### 7. Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Two scatter plots comparing automation and augmentation for AI" (no percentages, no platform labels) | "Left panel (1P API) shows 97.9% automation dominant; right panel (Claude.ai) shows 47% automation / 53% augmentation dominant; both plot automation share vs augmentation score with a diagonal reference" (key finding captured) | Exact percentages (97.9%/2.1% for 1P API, 47.0%/53.0% for Claude.ai); correctly identifies which panel is which platform; notes the diagonal is a reference line not a fit; correctly distinguishes axis labels ("Automation Share" vs "Augmentation Score"); mentions privacy-preserving zero caveat from caption |
| Specificity | "Purple and blue dots on two charts" (no axis labels, no percentages, no platform distinction) | "1P API nearly all purple (automation), Claude.ai mixed purple and blue; x-axis is automation share 0-100%, y-axis is augmentation score 0-100%; diagonal line separates dominant regions" (structural details present) | Cites exact legend percentages for both panels; describes spatial distribution differences (1P API dense strip at y=0, Claude.ai broad triangular fill); notes bubble size variation without legend; identifies blue outlier positions in 1P API panel (~10-30% x, 50-65% y); describes the asymmetric axis labels |
| Completeness | Mentions two scatter panels with different colors | Covers both panels with legends, axis labels, diagonal line, and the key percentage contrast | Both panel titles, both axis labels with exact text, both legends with exact percentages, diagonal reference line, bubble size variation, spatial distribution description for both panels, caption text including privacy-preserving methodology, grid lines |
| Usefulness | "Chart about AI automation" (not searchable) | "Scatter comparison showing API usage is almost entirely automation (97.9%) while Claude.ai chat splits evenly between automation and augmentation modes" (captures the core finding) | Explains automation/augmentation distinction (substitution vs complementarity), contextualizes the API-vs-chat modality difference, notes economic implications (automation displaces tasks, augmentation enhances productivity), connects to O*NET task classification framework, explains privacy-preserving zero caveat |

<br><br>

## doc04-V22 -- Partial regression scatter plot

**Figure reference:** Figure 3.9, page 43
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector

### 1. Visual Inventory

- Title (two lines, orange/brown text):
  - "Task usage share vs API Cost Index"
  - "(partial regression after controlling for task characteristics)"
- Single scatter plot (not multi-panel)
- X-axis: "Residual ln(API Cost Index)" (ticks at -3, -2, -1, 0, 1, 2)
- Y-axis: "Residual ln(Usage share (%))" (ticks at -3, -2, -1, 0, 1, 2,
  3, 4)
- All data points are uniform salmon/orange circles (no color encoding,
  no size variation)
- Black dashed regression line sloping downward from upper-left to
  lower-right
- Legend box (upper-right): "Partial relationship (R-squared = 0.025)"
  with dashed line icon
- Light gray grid lines in background
- Caption below (Figure 3.9)

### 2. Verifiable Facts

- R-squared = 0.025 (shown in legend)
- Estimated elasticity = -0.29 (stated in caption: "each 1% increase in
  the API cost index for a given task is associated with a 0.29%
  decrease in prevalence")
- X-axis range: approximately -3 to 2
- Y-axis range: approximately -3 to 4+
- Regression line slopes downward (negative relationship)
- The regression line crosses y=0 at approximately x=0 (the residuals
  are centered)
- At x=-3, the regression line is at approximately y=1
- At x=2, the regression line is at approximately y=-1
- Dense cluster of points in the region x=-1 to 1, y=-2 to 2
- Sparse outlier points in upper-left quadrant (y=3 to 4, x=-1 to 0)
  representing tasks with much higher usage than cost would predict
- Sparse outlier points at the bottom (y=-3 to -2) representing tasks
  with much lower usage than predicted
- Both axes use residual (partialled-out) values, not raw values
- The regression controls for: occupational category fixed effects,
  collaboration mode share, and privacy-censoring indicators

### 3. Hallucination Risks

- R-squared = 0.025 is extremely low. A model may describe this as a
  "strong" or "clear" relationship when the scatter shows almost no
  linear pattern visually. The vast majority of variance is unexplained.
- A model may misread the R-squared value (0.025 is easy to confuse
  with 0.25, which would imply a much stronger relationship).
- The axes show RESIDUAL values (partialled-out), not raw values. A
  model may describe them as "API cost" and "usage share" without the
  "residual" qualifier, which changes the interpretation entirely.
- A model may claim to identify specific task names from point positions.
  No task labels appear on the chart.
- The elasticity of -0.29 is from the caption, not labeled on the chart
  itself. A model may attempt to estimate the slope from the visual and
  get a different value.
- A model may confuse the natural log scale with a linear scale. The
  x-axis is ln(API Cost Index), so a move from 0 to 1 represents an
  e-fold (~2.7x) increase in cost, not a unit increase.
- The dashed line is a partial regression fit, not a simple OLS line.
  A model may describe it generically as "regression line" without
  noting the partial/controlled nature.

### 4. Detail Inventory

- Point color: uniform salmon/orange (no categorical or continuous
  color encoding -- all tasks shown equally)
- Point size: appears uniform (no size encoding)
- Regression line style: black dashed
- Legend box: thin border, white background, upper-right corner
- The scatter forms a roughly elliptical cloud with no obvious linear
  pattern to the naked eye -- consistent with R-squared = 0.025
- A few extreme outlier points at y=4+ (upper-left) are well above the
  main cloud
- Points at y=-3 (bottom) are sparse and isolated
- The densest region of the scatter is centered around (0, 0) extending
  to (1, 0), consistent with the residual regression centering
- Grid line spacing: 1 unit on both axes
- Title uses two lines with the parenthetical on the second line

### 5. Domain Context

This figure tests whether API cost affects task adoption. The "API Cost
Index" measures the average API cost for transcripts associated with
each O*NET task, normalized by the overall average. Higher cost index
means the task uses more expensive API calls (longer prompts/responses,
more complex reasoning).

The partial regression removes confounding factors (occupational
category, collaboration mode) so the scatter shows only the
cost-prevalence relationship. The result is weak: R-squared = 0.025
means cost explains only 2.5% of the variance in task prevalence. The
elasticity of -0.29 is statistically meaningful but economically modest
-- a task that costs 10% more is only about 3% less prevalent.

The report's interpretation (from the preceding body text) is that
"other factors, beyond the cost of using Claude for particular tasks,
appear to matter more for patterns of use." Cost is a real but minor
factor compared to task characteristics, occupational patterns, and
capability match.

Caption: "Figure 3.9: Scatter plot of API cost per task and usage share
controlling for task characteristics. For each O*NET task matched to 1P
API traffic we calculate an API cost index: Dividing the average API
cost across transcripts associated with that task by the average
(unweighted) value across all tasks in our sample. We then restrict the
sample to tasks appearing in both our 1P API and Claude.ai samples.
This partial scatter plot controls for the following task-level
characteristics: fixed effects for occupational category, collaboration
mode share from Claude.ai, and indicators for whether a given
collaboration mode was censored for privacy-preserving reasons in the
Claude.ai sample. The estimated elasticity of -0.29 implies that each
1% increase in the API cost index for a given task is associated with a
0.29% decrease in prevalence in our sample, after controlling for task
characteristics."

### 6. Search Keywords

partial regression, scatter plot, API cost index, usage share, task
prevalence, elasticity, R-squared, residual, O*NET tasks, cost
sensitivity, price elasticity, occupational category, collaboration
mode, privacy-preserving, task characteristics, controlled regression,
Anthropic Economic Index, Figure 3.9, natural log, API pricing

### 7. Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Scatter plot of cost vs usage with a downward trend line" (no R-squared, no elasticity, wrong axis descriptions) | "Partial regression scatter of residual API cost index vs residual usage share; R-squared = 0.025; negative slope showing higher cost tasks are less prevalent" (captures key statistics and direction) | R-squared = 0.025 correct; elasticity = -0.29 from caption; correctly identifies both axes as RESIDUAL ln-transformed values; notes the regression controls for occupational category, collaboration mode, and privacy censoring; describes the relationship as weak (2.5% variance explained) |
| Specificity | "Dots with a line on a chart about cost" (no axis labels, no statistics) | "X-axis is residual ln(API Cost Index) from -3 to 2; y-axis is residual ln(usage share) from -3 to 4; dashed regression line; R-squared shown in legend" (axis details present) | Names both axis labels verbatim with ranges; cites R-squared = 0.025; describes the dense cluster center and outlier positions; notes uniform salmon point color with no encoding; identifies the 2-line title format; notes legend position and dashed line icon |
| Completeness | Mentions a scatter plot with a regression line | Covers both axis labels, R-squared, regression line, point distribution shape, and title | Title (both lines), both axis labels with tick ranges, legend with R-squared, regression line style (dashed black), point appearance (uniform salmon, no size/color encoding), scatter shape description (elliptical cloud centered at origin), outlier positions, grid lines, full caption including methodology (cost index calculation, control variables, elasticity interpretation) |
| Usefulness | "Chart about API costs and usage" (not searchable) | "Partial regression showing weak negative relationship (R-sq=0.025) between API cost and task prevalence after controlling for task characteristics" (captures the finding) | Explains that cost explains only 2.5% of usage variance (economically modest effect); contextualizes the -0.29 elasticity (10% cost increase = ~3% prevalence decrease); notes the report's conclusion that other factors matter more than cost; explains the partial regression methodology (removing occupational and collaboration mode confounds); distinguishes residual from raw values |

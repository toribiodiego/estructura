# Image Analysis: Doc 27 -- 27_era_annual_report_2023.pptx

**Document:** `27_era_annual_report_2023.pptx`
**Format:** PPTX
**Source:** https://www.era-online.org/wp-content/uploads/2026/01/Slides-summarizing-AR2023_website.pptx
**Category:** multi-image
**Images:** 42
**Document context:** European Renal Association (ERA) 2023 Registry Annual
Report summary with 42 content images (maps, charts, paired comparisons)
across 31 of 32 slides. Covers kidney replacement therapy (KRT) incidence,
prevalence, transplantation, and survival statistics across European
countries. Near-duplicate halves suggest stratified breakdowns (unadjusted
vs. age-adjusted, by sex, by disease). 4 decorative branding images in
slide layouts. NOTE: Catalog originally misidentified ERA as "European
Union Agency for Railways" -- it is actually the European Renal Association.

**Eval subset:** 6 of 42 content images

<br><br>

## doc27-R01 -- Choropleth map of European countries (two-color)

**Slide:** 2
**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory

Choropleth map of Europe and surrounding regions. Countries are filled
in three states: red, orange, or white (unfilled). Sea areas are light
blue. Country borders drawn with thin black lines. No legend, title,
or text labels appear in the extracted crop.

### Verifiable Facts

- Map extent: Iceland (upper left) to Turkey (lower right), with
  North Africa and Middle East partially visible at edges
- Three fill states: red, orange, white
- Red countries include (approximate): United Kingdom, Ireland, France,
  Spain, Netherlands, Belgium, Luxembourg, Norway, Sweden, Denmark,
  Czech Republic, Austria, Switzerland, Greece, Bulgaria, Romania,
  Croatia, North Macedonia, Serbia
- Orange countries include (approximate): Iceland, Finland, Estonia,
  Latvia, Lithuania, Poland, Hungary, Slovakia, Turkey, portions of the
  Iberian peninsula (Portugal appears orange-red border)
- White/unfilled: Germany, Italy (appears partially white/orange),
  Russia, Belarus, non-European countries
- No legend is visible in the crop -- the color key must be on the
  slide outside this image region
- No text labels on any country

### Hallucination Risks

- **Country identification**: Borders are not labeled; small countries
  (Balkans, Baltics) could be misidentified or color-assigned wrongly
- **Color ambiguity**: Some countries appear borderline red/orange;
  without the legend the meaning of each color is unknown from the crop
  alone
- **Italy**: Parts appear white and parts orange, making classification
  uncertain
- **Portugal vs Spain**: The red-orange boundary on the Iberian
  peninsula is hard to distinguish cleanly
- **Topic inference**: An annotator might guess what the map represents
  (registry type, data coverage) from document context rather than
  from the image itself

### Detail Inventory

- Country count colored red: approximately 18-20
- Country count colored orange: approximately 10-12
- Germany is distinctly white/unfilled, standing out in central Europe
- Sea fill is a uniform light blue (#D6E8F7 approximate)
- No gridlines, scale bar, or compass rose
- Map projection appears to be a standard European projection centered
  roughly on central Europe

### Domain Context

This map is from the European Renal Association (ERA) 2023 Registry
Annual Report. Slide 2 is titled "National and regional renal registries
that contributed." The two colors (red, orange) likely represent
different categories of registry contribution (e.g., providing
individual vs. aggregated data, or complete vs. partial coverage). The
absence of a legend in the crop means an annotator must describe the
visual pattern without asserting the thematic meaning.

### Search Keywords

choropleth, Europe, map, countries, red, orange, ERA, renal registry,
kidney replacement therapy, KRT, EU member states, thematic map

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Describes this as a "European rail network map" or fabricates a meaning for the color coding (e.g. "red = non-compliant"). There are no rail lines, labels, or legend in the image. Inventing text labels or a legend not present triggers the hallucination cap. Misassigning a country's color (e.g. calling Germany red when it is white) is a factual error. | Correctly identifies as a choropleth map with red, orange, and white countries. Major country-color assignments accurate (UK red, Finland orange, Germany white). May mis-assign one or two smaller countries. No fabricated legend or labels. | All visible country-color assignments accurate: red (UK, France, Spain, Norway, Sweden, Denmark, Netherlands, Belgium, Austria, Czech Republic, Greece, Romania, Bosnia, Montenegro, etc.), orange (Iceland, Ireland, Finland, Poland, Latvia, Lithuania, Ukraine, Hungary, Turkey, etc.), white (Germany, Italy core, Russia, and others). Notes absence of legend, title, and text labels in the crop. |
| Information Recovery | Identifies a map but recovers fewer than half the queryable entities (country-color assignments, color scheme description, geographic extent). A search for "choropleth" or "Finland orange" would fail. | Color scheme (red/orange/white) described. Several major countries identified by color. Geographic extent noted (Iceland to Turkey). A search for "red countries Europe map" would match. Missing specific assignments for smaller or ambiguous countries. | All discernible country-color assignments recovered. Three-color scheme documented (red, orange, white/unfilled). Geographic scope (Iceland to Turkey, including North Africa coastline). Absence of legend and labels explicitly noted. A search for "Norway red" or "Turkey orange" or "Germany white unfilled" returns a match. |
| Retrieval Value | Fabricates domain context ("railway compliance levels") making the annotation actively misleading. Not self-contained due to false framing. | Self-contained: "Choropleth map of Europe with countries colored red, orange, or white. No legend or labels visible." Acknowledges the missing legend without fabricating meaning. | Self-contained annotation identifying this as a choropleth from the ERA-EDTA Registry Annual Report, likely showing contributing national/regional renal registries. Notes that the legend is absent from the crop so color categories cannot be definitively interpreted, but the two-color coding (red vs orange) likely distinguishes registry contribution levels. Findable by "European choropleth renal registry" or "ERA country map." |

<br><br>

## doc27-R03 -- Unadjusted KRT incidence by country (aggregated data)

**Slide:** 4
**Content type:** chart-complex
**Annotation difficulty:** Medium

### Visual Inventory

Horizontal bar chart with dark gold/bronze bars. Title "Unadjusted
incidence" in bold, subtitle "renal registries providing aggregated
data" in italics. X-axis labeled "Incidence (per million population)"
ranging from 0 to 350 with gridlines at 50-unit intervals. Y-axis
lists 18 countries plus an "All countries" summary bar separated by a
gap at the bottom. Each bar has its numeric value displayed to the
right of the bar end.

### Verifiable Facts

- Title: "Unadjusted incidence"
- Subtitle: "renal registries providing aggregated data"
- X-axis label: "Incidence (per million population)"
- X-axis range: 0 to 350, gridlines at 0, 50, 100, 150, 200, 250, 300, 350
- Number of country bars: 18 (plus 1 "All countries" summary)
- Countries and values (top to bottom): Finland 83, Belarus** 105,
  Latvia 107, Lithuania 129, Kosovo** 133, Hungary 138, Albania 144,
  Croatia*** 148, Poland*** 150, Spain 152, Turkiye 160, Czech Republic
  161, Italy (10 of 20 regions) 170, Slovakia*** 178, Israel 188,
  North Macedonia 232, Portugal 237, Cyprus 269
- All countries: 155
- Bars sorted ascending by value (lowest at top)
- Asterisk annotations: Belarus (**), Kosovo (**), Croatia (***),
  Poland (***), Slovakia (***)
- Italy shown with qualifier "(10 of 20 regions)"
- Spelled "Turkiye" (modern official name, no diacritical marks)

### Hallucination Risks

- **Asterisk meanings**: The ** and *** annotations have no visible
  legend in the crop; an annotator might invent explanations
- **KRT not stated**: The abbreviation KRT (kidney replacement therapy)
  does not appear in this crop; the term comes from the slide title
  context, not the image
- **Country ordering**: An annotator might describe the sort order
  incorrectly (it is ascending, lowest at top)
- **Bar color**: The gold/bronze color could be described variously
  (dark yellow, ochre, tan, gold)

### Detail Inventory

- Bar color: dark gold/bronze (approximately #B8960C)
- All 18 country values are individually labeled with integers
- The "All countries" bar is visually separated from the country bars
  by a small gap
- Font: sans-serif, black text for labels and values
- Title is larger and bold; subtitle is smaller and italic
- No border or frame around the chart area
- Grid lines are thin gray, vertical only

### Domain Context

This is part of the ERA (European Renal Association) 2023 Registry
Annual Report. Slide 4 covers "Incident patients accepted for KRT in
2023, at day 1." This panel shows unadjusted incidence rates from
registries that report aggregated (not individual-level) data. The
right panel on the same slide (R04) likely shows the corresponding
chart for registries providing individual-level data.

### Search Keywords

bar chart, horizontal, incidence, renal, kidney replacement therapy,
KRT, per million population, European countries, unadjusted, ERA
registry, aggregated data

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Misidentifies the domain (e.g. "railway incident rates") or misreads labeled values (e.g. "Finland 93" for 83, or "Cyprus 296" for 269). Fabricating country names not in the chart triggers the hallucination cap. Swapping the sort order (claiming Cyprus is lowest) is a structural misread. | Chart type, title, and axis label correct. Country-value pairs accurate for major entries (Finland 83, Cyprus 269, All countries 155). May misread one or two mid-range values. Asterisk annotations acknowledged. | All 18 country-value pairs exact (Finland 83 through Cyprus 269), plus All countries 155. Asterisk annotations correctly placed (Belarus**, Kosovo**, Croatia***, Poland***, Slovakia***). Italy qualified as "10 of 20 regions." Ascending sort order noted. Tolerance: zero -- all values are explicitly labeled on bars. |
| Information Recovery | Identifies a bar chart but recovers fewer than half of the 19 country-value pairs. A search for "Albania 144" or "Kosovo 133" would fail. Missing title and axis label. | All 18 country names and most values recovered. Title and axis label present. Asterisk annotations noted but unexplained. A search for "Finland 83" or "Cyprus 269" matches. Some mid-range values may be missing or rounded. | All 19 bars (18 countries + All countries) with exact labeled values. Full title ("Unadjusted incidence") and subtitle ("renal registries providing aggregated data"). Axis label ("Incidence (per million population)"). Asterisk counts per country. Italy regional qualifier. A search for any country-value pair returns a match. Parity met. |
| Retrieval Value | Lists numbers without chart structure or medical context. Depends on surrounding slides to be meaningful. Not self-contained. | Self-contained: "Horizontal bar chart of unadjusted KRT incidence per million population for 18 European countries plus aggregate." Readable standalone. Missing domain context about what KRT incidence measures or why values vary. | Self-contained annotation identifying this as unadjusted kidney replacement therapy incidence from the ERA-EDTA Registry Annual Report. Notes the 3x range (Finland 83 to Cyprus 269 pmp) and that asterisks indicate data caveats. Findable by "KRT incidence per million Europe" or "Cyprus renal incidence 269" or "Finland kidney replacement 83." |

<br><br>

## doc27-R09 -- KRT incidence by age category (dual chart)

**Slide:** 7
**Content type:** chart-complex
**Annotation difficulty:** Medium

### Visual Inventory

Wide image containing two side-by-side charts. Left: horizontal bar
chart showing KRT incidence rates by 5 age bands. Right: 100% stacked
bar chart showing the same age distribution as percentages across three
registry data types. Both charts share the title "Incidence by age
category" but have different subtitles. Color-coded by age band with
consistent palette across both charts.

### Verifiable Facts

**Left chart:**
- Title: "Incidence by age category"
- Subtitle: "for all registries" (italics)
- Chart type: horizontal bar chart
- X-axis label: "Incidence (per million age-related population)"
- X-axis range: 0 to 600, gridlines at 100-unit intervals
- 5 age bands with values (top to bottom):
  - 75+: 533.4 (gray-green bar)
  - 65-74: 422.6 (olive green bar)
  - 45-64: 163.9 (dark gray/charcoal bar)
  - 20-44: 46.5 (steel blue bar)
  - 0-19: 8.0 (light yellow bar)

**Right chart:**
- Title: "Incidence by age category"
- Subtitle: "by type of data provided by registry" (italics)
- Chart type: 100% stacked bar chart (vertical)
- Y-axis: 0% to 100%, gridlines at 10% intervals
- 3 columns: "All countries", "Individual data", "Aggregated data"
- Legend (right side, top to bottom): 75+, 65-74, 45-64, 20-44, 0-19
- Values within segments (bottom to top):
  - All countries: 1, 11, 30, 29, 29
  - Individual data: 1, 10, 30, 28, 31
  - Aggregated data: 1, 11, 30, 30, 29

**Color palette (consistent across both charts):**
- 0-19: light yellow/cream
- 20-44: steel blue
- 45-64: dark charcoal
- 65-74: olive green
- 75+: gray-green/sage

### Hallucination Risks

- **Single vs. dual chart**: An annotator might describe only one of
  the two charts and miss the other
- **Percentage values**: The stacked bar segment labels are small
  integers (percentages) that could be misread
- **Color assignment**: The colors are muted and could be described
  differently (e.g., "dark green" vs. "olive", "teal" vs. "steel blue")
- **Complexity underestimate**: Catalog rated this as "chart-simple" /
  "Easy" but it contains two distinct chart types with substantial data

### Detail Inventory

- Left chart bar values are labeled with one decimal place
- Right chart segment values are labeled as integers (percentages
  that sum to 100 for each column)
- The 0-19 age band has "1" in all three right-chart columns (barely
  visible at the bottom of each stack)
- Fonts: sans-serif throughout; titles bold, subtitles italic
- No border or frame around either chart
- The two charts are separated by whitespace, not a divider

### Domain Context

This is from the ERA (European Renal Association) 2023 Registry Annual
Report, slide 7: "Incident patients accepted for KRT in 2023, at day
1." The left chart shows that KRT incidence rises sharply with age,
peaking at 533.4 per million for ages 75+. The right chart shows that
the age distribution is nearly identical regardless of whether
registries provide individual or aggregated data. The 65-74 and 75+
age groups together account for roughly 58-60% of all incident KRT
patients.

### Search Keywords

bar chart, stacked bar, age category, incidence, renal, kidney
replacement therapy, KRT, per million, age distribution, 75+, 65-74,
ERA registry, age-related population

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Misidentifies the domain (e.g. "railway incidents by age group") or misreads labeled values (e.g. "533" for 533.4 or "423" for 422.6). Only describing one chart while two are present is a structural omission. Fabricating age bands not shown (e.g. "85+") triggers the hallucination cap. Swapping the right panel's percentage values between columns is a precision error. | Both charts identified. Left panel values correct for all 5 age bands (8.0, 46.5, 163.9, 422.6, 533.4). Right panel structure correct (3 stacked columns). May approximate some percentage labels. No fabricated content. | Left panel: all 5 values exact to one decimal (0-19: 8.0, 20-44: 46.5, 45-64: 163.9, 65-74: 422.6, 75+: 533.4 pmp). Right panel: all 15 percentage labels exact (All countries 1/11/30/29/29, Individual data 1/10/30/28/31, Aggregated data 1/11/30/30/29, bottom to top). Tolerance: zero for bar-labeled values; ~1% for stacked percentages that are harder to read. |
| Information Recovery | Describes "a bar chart about age groups" but recovers fewer than half the queryable entities (5 age-value pairs, 15 percentage labels, 2 chart titles, axis labels, legend). A search for "533.4" or "age 45-64 163.9" would fail. | Left panel: all 5 age-value pairs recovered. Right panel: 3-column structure and age distribution noted. Titles and subtitles present. A search for "75+ 533.4" or "incidence by age category" matches. Some percentage labels in right panel missing. | All queryable entities recovered: 5 age-value pairs (left), 15 percentage labels across 3 columns (right), both titles with subtitles, axis label ("Incidence per million age-related population"), x-axis range (0-600), legend (5 age categories with colors). A search for any labeled value from either panel returns a match. Parity met. |
| Retrieval Value | Lists some numbers without identifying the dual-chart structure or medical context. Depends on slide context. Not self-contained. | Self-contained: "Dual chart showing KRT incidence by age category: absolute rates (left) and percentage distribution by registry type (right)." Readable standalone. Missing interpretation of the age gradient or clinical significance. | Self-contained annotation explaining KRT incidence rising from 8.0 pmp (0-19) to 533.4 pmp (75+), a 67-fold gradient. Notes the near-identical age distributions across registry types (individual vs aggregated), with 65-74 and 75+ together comprising ~58% of incident patients. Findable by "KRT incidence age category 533" or "renal registry age distribution." |

<br><br>

## doc27-R38 -- Dialysis patient survival curve (unadjusted, from day 91)

**Slide:** 29
**Content type:** chart-complex
**Annotation difficulty:** Medium

### Visual Inventory

Line chart (survival curve) with two descending lines from ~100% to
~40-48% over 5 years. Light blue line for haemodialysis, red/coral
line for peritoneal dialysis. Title in two bold lines plus an italic
subtitle. Legend embedded in the lower-left area of the plot. Clean
white background with gray gridlines.

### Verifiable Facts

- Title (line 1): "Patient survival"
- Title (line 2): "Incident dialysis patients"
- Subtitle: "From day 91, unadjusted" (italics)
- Y-axis label: "Survival probability (%)"
- Y-axis range: 0 to 100, gridlines at 10% intervals
- X-axis label: "Years"
- X-axis range: 0 to 5, gridlines at 1-year intervals
- Two lines:
  - Haemodialysis (light blue): starts ~99-100% at year 0, ends
    ~47-48% at year 5
  - Peritoneal dialysis (red/coral): starts ~99-100% at year 0, ends
    ~41-42% at year 5
- Both curves are nearly overlapping from year 0 to approximately
  year 2, then gradually diverge
- Peritoneal dialysis has consistently lower survival after ~year 2
- At year 3, both lines are near 58-60%
- Legend shows colored squares with labels "Haemodialysis" and
  "Peritoneal dialysis"
- Spelling: "Haemodialysis" (British/European spelling with ae)

### Hallucination Risks

- **Exact endpoint values**: The curves end at approximately 47-48%
  (haemodialysis) and 41-42% (peritoneal dialysis) but exact values
  are not labeled; an annotator might read them too precisely
- **Curve shape**: The curves appear roughly linear but are actually
  slightly concave; an annotator might describe them as "exponential
  decay" which would be inaccurate
- **Statistical significance**: An annotator might claim the difference
  between modalities is statistically significant; no confidence
  intervals or p-values are shown
- **Kaplan-Meier vs. other**: The curves resemble Kaplan-Meier but
  appear smooth (no step function), suggesting they may be modeled
  or smoothed survival curves

### Detail Inventory

- Line thickness: both lines are of similar moderate thickness
- The haemodialysis line color is a pale/steel blue
- The peritoneal dialysis line color is a muted red/coral/salmon
- At year 1: both lines near ~80%
- At year 2: both lines near ~68-70%
- At year 4: haemodialysis ~49-50%, peritoneal dialysis ~46-47%
- No data markers (dots) on the lines
- No confidence interval bands shown
- Grid lines are thin gray, both horizontal and vertical

### Domain Context

This is from the ERA 2023 Registry Annual Report, slide 29: "Patient
survival by modality." The chart compares 5-year unadjusted survival
for incident dialysis patients starting from day 91 (the standard
landmark used to allow for initial modality stabilization). Both
modalities show roughly 50% 5-year survival, with haemodialysis having
a slight advantage of approximately 5-7 percentage points by year 5.
This unadjusted comparison does not account for age, comorbidity, or
other confounders that differ between modality populations.

### Search Keywords

survival curve, dialysis, haemodialysis, peritoneal dialysis, patient
survival, Kaplan-Meier, 5-year survival, incident patients, day 91,
unadjusted, ERA registry, kidney replacement therapy

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Claims "significantly better outcomes for haemodialysis" when no statistical test is shown, or describes step-function Kaplan-Meier when the curves are smooth. Fabricating confidence intervals not present triggers the hallucination cap. Misreading the year-5 values (e.g. "peritoneal 51%" when it is ~41%) is a precision error. Swapping which modality has higher survival reverses the clinical finding. | Two smooth survival curves correctly identified. Modalities named (haemodialysis, peritoneal dialysis). Year-5 endpoints approximately correct (~47% vs ~41%). Notes curves are unadjusted and start from day 91. | Curves correctly characterized as smooth (not step-function), starting ~100% at day 91. Year-by-year readings: year 1 ~80% both, year 2 ~68-70%, year 3 ~58-60%, year 5 haemodialysis ~47% peritoneal ~41%. Notes ~6pp divergence emerging after year 2. No fabricated confidence intervals or statistical claims. Tolerance: ~2-3% for axis-read values (no labeled data points on curves). |
| Information Recovery | Identifies a line chart but recovers fewer than half the queryable entities (title, subtitle, 2 modality names, axis labels, year-by-year readings, line colors, absence of CI). A search for "haemodialysis" or "peritoneal dialysis" would fail. | Both modality names recovered with year-5 survival approximations. Title and subtitle present. Axis labels noted. A search for "haemodialysis survival 5 years" matches. Missing intermediate year readings and curve convergence/divergence description. | All queryable entities recovered: full title ("Patient survival / Incident dialysis patients"), subtitle ("From day 91, unadjusted"), both axis labels, both modality names with colors, year-by-year approximate readings at each gridline, legend description, absence of confidence bands. A search for "peritoneal dialysis 41% 5 years" or "day 91 unadjusted survival" returns a match. |
| Retrieval Value | Describes "two declining lines" without medical context. Not self-contained as a clinical reference. | Self-contained: "5-year unadjusted survival for incident dialysis patients from day 91 comparing haemodialysis and peritoneal dialysis." Readable standalone. Missing context about why the comparison is unadjusted or the day-91 landmark. | Self-contained annotation explaining this as unadjusted 5-year survival from day 91 (excluding early mortality) for incident dialysis patients. Notes the ~6pp haemodialysis advantage at year 5 but cautions that this is unadjusted for age or comorbidity. British spelling "haemodialysis" preserved. Findable by "dialysis survival unadjusted day 91" or "haemodialysis vs peritoneal 5-year survival." |

<br><br>

## doc27-R41 -- Expected remaining lifetime by age (general vs. KRT)

**Slide:** 31
**Content type:** chart-complex
**Annotation difficulty:** Medium

### Visual Inventory

Grouped horizontal bar chart with three bars per age band: black
(general population), olive/tan (transplant), and steel blue (dialysis).
14 age bands from 20-24 to 85-89. Title spans two lines at the top.
X-axis shows expected remaining years of life (0-70). Legend in the
right-center area of the chart.

### Verifiable Facts

- Title: "Expected remaining years of life of the general population
  and of prevalent dialysis and kidney transplant patients"
- Y-axis label: "Age (years)"
- Y-axis categories (bottom to top): 20-24, 25-29, 30-34, 35-39,
  40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-84,
  85-89
- X-axis label: "Expected remaining years of life"
- X-axis range: 0 to 70, gridlines at 10-year intervals
- Three series per age band:
  - General population (black bars) -- always longest
  - Transplant (olive/tan bars) -- intermediate
  - Dialysis (steel blue bars) -- always shortest
- Legend: "General population" (black square), "Transplant" (olive
  square), "Dialysis" (blue square)
- Approximate values at age 20-24:
  - General population: ~62 years
  - Transplant: ~40 years
  - Dialysis: ~25 years
- Approximate values at age 85-89:
  - General population: ~4 years
  - Transplant: ~2 years
  - Dialysis: ~2 years
- 14 age bands x 3 bars = 42 total bars
- All bars decrease from bottom to top (younger ages have more
  remaining years)

### Hallucination Risks

- **Exact values**: No numeric labels on bars; values must be
  estimated from the x-axis gridlines
- **Color names**: The transplant bar color could be described as
  olive, tan, khaki, or gold -- multiple reasonable descriptions
- **Dialysis vs. transplant gap**: At older ages the transplant and
  dialysis bars are very close; an annotator might overstate or
  understate the difference
- **Missing age bands**: An annotator might miss that 14 bands are
  shown (not all decades from 0) and the range starts at 20-24

### Detail Inventory

- Bar grouping: for each age band, bars are stacked vertically in
  order: black (top), olive (middle), blue (bottom)
- At younger ages (20-24), the general population bar extends to
  approximately 62, creating a dramatic visual gap with dialysis (~25)
- The gap narrows progressively with age
- At 70-74: general ~13, transplant ~9, dialysis ~6 (approximate)
- At 80-84: general ~7, transplant ~3, dialysis ~3 (approximate)
- Grid lines are thin gray, vertical only
- No bar value labels displayed
- White background, no border

### Domain Context

This is from the ERA 2023 Registry Annual Report, slide 31: "Expected
remaining lifetime." The chart illustrates the life-years lost due to
kidney failure. A 20-24 year old on dialysis can expect ~25 more years
of life versus ~62 for the general population -- a gap of ~37 years.
Kidney transplant substantially narrows this gap (to ~22 years lost)
but does not eliminate it. The comparison uses prevalent (not incident)
patients, meaning it reflects the current population on treatment
rather than newly starting patients.

### Search Keywords

grouped bar chart, expected remaining lifetime, life expectancy, age,
general population, transplant, dialysis, kidney replacement therapy,
prevalent patients, ERA registry, years of life lost

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Misidentifies chart type (e.g. "infographic" or "stacked bar" when it is a grouped bar chart). Claiming "dialysis patients live about half as long" is wrong -- the ratio varies by age and the chart shows remaining years, not total lifespan. Fabricating bar value labels not present triggers the hallucination cap. Swapping the series order (claiming dialysis bars are longest) reverses the clinical finding. | Chart type correct (grouped horizontal bar). Three series correctly identified (General population, Transplant, Dialysis). Ordering always general > transplant > dialysis. Key readings approximately right (20-24: general ~62, dialysis ~25). No fabricated data labels. | Series ordering and approximate readings at multiple age bands correct: 20-24 (~62/~40/~25), 70-74 (~13/~9/~6), 85-89 (converging near 2-4 years). Notes the progressive narrowing of the gap with age. Correctly identifies no numeric labels on bars. Tolerance: ~2-3 years for axis-read values (no labeled data points). |
| Information Recovery | Describes "a bar chart about life expectancy" but recovers fewer than half the queryable entities (14 age bands, 3 series with approximate values at each band, title, axis labels, legend, bar colors). A search for "transplant remaining years" or "age 20-24" would fail. | Three series names and several age-band readings recovered. Title and axis labels present. Legend described. A search for "general population transplant dialysis life expectancy" matches. Missing readings for many of the 14 age bands and the convergence pattern at older ages. | Approximate readings at multiple representative age bands documented (youngest, middle, oldest). All 14 age band labels listed (20-24 through 85-89). Full title, both axis labels, legend with 3 series and colors (black, olive, blue). Bar ordering within each band described. A search for "expected remaining years dialysis age 45-49" returns a match via the documented pattern. |
| Retrieval Value | Lists some bar lengths without identifying the medical comparison or the three patient groups. Depends on slide context. Not self-contained. | Self-contained: "Grouped bar chart comparing expected remaining years of life for general population, transplant, and dialysis patients across 14 age bands." Readable standalone. Missing clinical interpretation. | Self-contained annotation explaining this as ERA-EDTA Registry data on life-years lost to kidney disease. Notes that at age 20-24, dialysis patients lose ~37 years vs general population while transplant narrows the loss to ~22 years. Documents the progressive convergence at older ages. Uses prevalent (not incident) patients. Findable by "expected remaining lifetime dialysis transplant" or "years of life lost kidney replacement therapy." |

<br><br>

## doc27-R42 -- Expected remaining lifetime by age and sex (general vs. KRT)

**Slide:** 32
**Content type:** chart-complex
**Annotation difficulty:** Medium

### Visual Inventory

Wide image containing two side-by-side grouped horizontal bar charts,
"Males" (left) and "Females" (right). Each panel has the same structure
as R41: three bars per age band (general population, transplant,
dialysis) across 14 age bands. Shared title above both panels, shared
legend between panels on the right. Same color palette as R41.

### Verifiable Facts

- Title: "Expected remaining years of life of the general population
  and of prevalent dialysis and kidney transplant patients"
- Two panels with bold subtitles: "Males" (left), "Females" (right)
- Y-axis: "Age (years)" -- labeled on left panel only
- Y-axis categories (both panels, bottom to top): 20-24, 25-29, 30-34,
  35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79,
  80-84, 85-89
- X-axis (both panels): "Expected remaining years of life", range 0-70
- Three series (same as R41):
  - General population (black)
  - Transplant (olive/tan)
  - Dialysis (steel blue)
- Legend shared between panels, right-center area
- Males panel approximate values at age 20-24:
  - General population: ~58 years
  - Transplant: ~38 years
  - Dialysis: ~20-21 years
- Females panel approximate values at age 20-24:
  - General population: ~64 years
  - Transplant: ~42 years
  - Dialysis: ~27 years
- Females have longer bars than males at every age for all three groups
- 14 age bands x 3 bars x 2 panels = 84 total bars

### Hallucination Risks

- **Exact values**: No numeric labels on bars; all values estimated
  from gridlines
- **Male vs. female differences**: The visual gap between sexes is
  modest and easy to overstate; an annotator might claim "substantially
  longer" when the difference is 4-6 years for general population
- **Panel confusion**: An annotator might swap male and female panels
  or describe the wrong panel's data
- **Relationship to R41**: This is the sex-stratified version of R41;
  an annotator might fail to note the connection or might conflate
  the two images

### Detail Inventory

- Bar grouping order (top to bottom within each age band): black,
  olive, blue -- same as R41
- At age 85-89: all bars are very short (2-5 years), difficult to
  distinguish individual groups
- The right panel (Females) has slightly longer general population bars
  than the left panel (Males) at all ages, consistent with known female
  longevity advantage
- At age 70-74 Males: general ~12, transplant ~8, dialysis ~5
- At age 70-74 Females: general ~15, transplant ~10, dialysis ~7
- Grid lines are thin gray, vertical only, in both panels
- No border separating the two panels -- just whitespace
- Y-axis title "Age (years)" appears only on the left panel

### Domain Context

This is from the ERA 2023 Registry Annual Report, slide 32: "Expected
remaining lifetime." This sex-stratified version of R41 shows that
females have a longevity advantage in all three groups (general
population, transplant, dialysis) at every age band. The life-years
lost due to kidney failure (gap between general population and dialysis)
is similar for both sexes in absolute terms but represents a larger
proportional reduction for males. Transplant narrows the gap for both
sexes.

### Search Keywords

grouped bar chart, expected remaining lifetime, life expectancy, males,
females, sex-stratified, general population, transplant, dialysis,
kidney replacement therapy, age, ERA registry, prevalent patients

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Misidentifies chart type (e.g. "infographic") or claims "males and females have the same life expectancy on dialysis" (females are consistently higher across all ages and groups). Fabricating bar value labels not present triggers the hallucination cap. Confusing the two panels (swapping male/female) reverses the sex comparison. | Dual-panel structure correctly identified (Males left, Females right). Three series named and ordered correctly. Key readings approximately right (20-24: male general ~58 vs female general ~64). Females consistently longer bars noted. | Approximate readings at representative age bands correct for both panels: Males 20-24 (~58/~38/~20-21), Females 20-24 (~64/~42/~27); at 70-74 Males (~12/~8/~5), Females (~15/~10/~7); at 85-89 all converge to 2-5 years. 84 total bars (14 x 3 x 2). No fabricated labels. Tolerance: ~2-3 years for axis-read values. |
| Information Recovery | Describes "bar charts about males and females" but recovers fewer than half the queryable entities (2 panels x 14 age bands x 3 series = 84 bars, plus title, axis labels, legend, panel headers). A search for "male dialysis 20-24" or "female transplant 45-49" would fail. | Both panels described with representative readings. Three series and 14 age bands listed. Title, axis labels, and shared legend noted. A search for "males females remaining years general population transplant dialysis" matches. Most mid-range age-band readings missing. | Representative readings documented at young, middle, and old ages for both panels. All structural elements recovered: shared title, panel headers ("Males"/"Females"), both axis labels, legend position and colors, 14 age bands, bar ordering within each band. Sex difference in general population (~6 years at age 20-24) quantified. A search for "female dialysis expected remaining years" returns a match. |
| Retrieval Value | Lists some bar lengths without identifying the dual-panel structure, sex stratification, or medical comparison. Not self-contained. | Self-contained: "Side-by-side grouped bar charts comparing expected remaining years of life for males and females across 14 age bands for general population, transplant, and dialysis patients." Readable standalone. Missing clinical interpretation. | Self-contained annotation explaining this as the sex-stratified version of the ERA-EDTA remaining lifetime comparison. Notes that females have ~6-year longevity advantage in the general population but life-years lost to kidney failure are similar in absolute terms for both sexes (~37 years at age 20-24). Transplant narrows the gap for both sexes. Findable by "sex-stratified remaining lifetime dialysis transplant" or "male female kidney replacement life expectancy." |

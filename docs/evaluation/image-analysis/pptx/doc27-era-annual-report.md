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
| Accuracy | "Map of European rail network" (wrong domain; no rail lines shown) | "Map of Europe with colored countries" (correct but vague on color scheme) | "Choropleth map with countries in red, orange, or white. No legend visible in the crop." |
| Specificity | "Map with some countries highlighted" | "About 20 countries are colored red and 10 orange, with Germany unfilled" | "Red countries include UK, France, Spain, Norway, Sweden, Greece, Romania; orange includes Finland, Poland, Turkey, Iceland. Germany is distinctly white." |
| Completeness | "A map of Europe" (misses color scheme, country counts, and absence of legend) | "Choropleth map with red and orange countries; no legend or labels" (covers main features) | "Choropleth of Europe with ~20 red, ~10 orange, remaining white countries. No legend, title, or text labels. Sea areas light blue, thin black borders. Map extends from Iceland to Turkey." |
| Usefulness | "Map showing EU railway safety compliance levels with red meaning non-compliant" (fabricates meaning from wrong domain) | "Thematic map of European countries colored by some category, likely related to the document's topic" | "Choropleth from ERA 2023 Registry Annual Report slide 2 ('National and regional renal registries that contributed'). Colors likely represent registry contribution categories but legend is not in the crop." |

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
| Accuracy | "Chart showing railway incident rates across Europe" (wrong domain entirely) | "Horizontal bar chart of incidence per million for European countries" (correct type and metric) | "Horizontal bar chart titled 'Unadjusted incidence' showing renal incidence per million population for 18 countries. Finland lowest at 83, Cyprus highest at 269, All countries 155." |
| Specificity | "Bar chart with some countries" (no counts, no values) | "18 countries ranging from 83 to 269, with an All countries bar at 155" (key range and count) | "Values top to bottom: Finland 83, Belarus** 105, Latvia 107, Lithuania 129, Kosovo** 133, Hungary 138, Albania 144, Croatia*** 148, Poland*** 150, Spain 152, Turkiye 160, Czech Republic 161, Italy (10 of 20 regions) 170, Slovakia*** 178, Israel 188, North Macedonia 232, Portugal 237, Cyprus 269. Asterisks have no visible legend." |
| Completeness | "Bar chart of kidney disease rates" (misses title, subtitle, axis labels, country count, sort order) | "Horizontal bar chart titled 'Unadjusted incidence' with subtitle about aggregated data. 18 countries plus All countries. Sorted ascending." (covers structure) | "Title 'Unadjusted incidence', subtitle 'renal registries providing aggregated data' in italics. X-axis 'Incidence (per million population)' 0-350. 18 country bars sorted ascending plus separated All countries bar. Asterisk annotations on 5 countries. Italy qualified as '10 of 20 regions'." |
| Usefulness | "A bar chart from some report" (no domain context, not searchable) | "Renal incidence chart from ERA 2023 report showing aggregated registry data" (domain identified) | "Unadjusted KRT incidence from aggregated renal registries, ERA 2023. Slide 4 left panel. Cyprus highest (269 pmp), Finland lowest (83 pmp). Companion right panel (R04) shows individual-data registries." |

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
| Accuracy | "Chart showing incidence of railway incidents by age group" (wrong domain) | "Dual chart of disease incidence by age, with bars and stacked percentages" (correct structure) | "Left: horizontal bar chart of incidence per million age-related population. 75+ at 533.4, 65-74 at 422.6, 45-64 at 163.9, 20-44 at 46.5, 0-19 at 8.0. Right: 100% stacked bar showing near-identical age distributions across three registry types." |
| Specificity | "Bar chart of age groups" (no values, no chart count) | "Two charts: bar chart with 5 age bands ranging from 8.0 to 533.4, and stacked bar with 3 columns" (key counts and range) | "Left chart x-axis 0-600, values labeled to one decimal. Right chart: All countries 1/11/30/29/29, Individual data 1/10/30/28/31, Aggregated data 1/11/30/30/29 (bottom to top). Legend: 75+, 65-74, 45-64, 20-44, 0-19." |
| Completeness | "A bar chart about age" (misses second chart, titles, subtitles, all values) | "Two charts both titled 'Incidence by age category' with different subtitles. Five age bands, three registry types. Color-coded consistently." (covers both charts) | "Left: 'Incidence by age category / for all registries', 5 bars with values and colors. Right: 'Incidence by age category / by type of data provided by registry', 3 stacked columns with percentage labels, legend listing all 5 age categories. Consistent color palette across both." |
| Usefulness | "Some medical charts" (no searchable terms, no domain context) | "Renal incidence by age from ERA 2023 report, showing sharp increase in older age groups" (domain identified) | "KRT incidence by age from ERA 2023, slide 7. Incidence rises from 8.0 pmp (ages 0-19) to 533.4 pmp (75+). Age distribution nearly identical for individual-data and aggregated-data registries, with 65-74 and 75+ together comprising ~58% of incident patients." |

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
| Accuracy | "Kaplan-Meier plot showing significantly better outcomes for haemodialysis" (no statistical test shown; curves are smooth not stepped; overstates difference) | "Survival curve comparing two dialysis types over 5 years, both declining from 100% to roughly 40-48%" (correct structure and range) | "Smooth survival curves for haemodialysis (~47% at year 5) and peritoneal dialysis (~41% at year 5). Curves nearly overlap until year 2, then diverge by ~6 percentage points. No confidence intervals or step-function shape." |
| Specificity | "Chart of two declining lines" (no axis labels, no values, no modality names) | "Haemodialysis and peritoneal dialysis survival from day 91, unadjusted. Y-axis 0-100%, x-axis 0-5 years." (axes and modalities identified) | "Haemodialysis (light blue) and peritoneal dialysis (red/coral). At year 1 both ~80%, year 2 both ~68-70%, year 3 both ~58-60%. By year 5: haemodialysis ~47%, peritoneal ~41%. Title: 'Patient survival / Incident dialysis patients', subtitle: 'From day 91, unadjusted'." |
| Completeness | "A line chart about dialysis" (misses title, subtitle, axis labels, legend, values, line colors) | "Two survival curves with legend showing Haemodialysis and Peritoneal dialysis. Title and subtitle present. Gridlines at 10% and 1-year intervals." (covers major elements) | "Title in two lines plus italic subtitle. Y-axis 'Survival probability (%)' 0-100 at 10% gridlines. X-axis 'Years' 0-5 at 1-year gridlines. Two smooth lines with embedded legend (colored squares). No data markers, no confidence bands. British spelling 'Haemodialysis'." |
| Usefulness | "Some medical chart with lines going down" (no searchable terms) | "Dialysis patient survival comparison from ERA 2023 Registry report, unadjusted from day 91" (domain and landmark identified) | "5-year unadjusted survival for incident dialysis patients from day 91, ERA 2023. Haemodialysis has ~6pp advantage at year 5. Comparison does not adjust for age or comorbidity. Slide 29: 'Patient survival by modality'." |

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
| Accuracy | "Infographic summarizing key statistics" (wrong chart type; this is a grouped bar chart) | "Bar chart comparing life expectancy for general population, transplant, and dialysis patients across age groups" (correct type and groups) | "Grouped horizontal bar chart with 14 age bands (20-24 to 85-89) and 3 series. General population always longest, transplant intermediate, dialysis shortest. At 20-24: general ~62, transplant ~40, dialysis ~25. No numeric labels on bars." |
| Specificity | "Chart showing dialysis patients live about half as long" (wrong ratio; varies by age) | "Three groups compared across 14 age bands from 20-24 to 85-89. At age 20-24 the gap between general population and dialysis is about 37 years." (key data point) | "At 20-24: general ~62, transplant ~40, dialysis ~25. At 70-74: general ~13, transplant ~9, dialysis ~6. At 85-89: all three groups converge near 2-4 years. Gap narrows progressively with age. 42 total bars (14 bands x 3 series)." |
| Completeness | "A bar chart about life expectancy" (misses title, axis labels, group names, age range, bar count) | "Grouped bar chart titled 'Expected remaining years of life...' with Y-axis 'Age (years)' and X-axis 0-70. Three series in legend: General population, Transplant, Dialysis." (covers structure) | "Full title across two lines. Y-axis 'Age (years)' with 14 bands 20-24 to 85-89. X-axis 'Expected remaining years of life' 0-70 with 10-year gridlines. Legend with three colored squares. Within each band: black (top), olive (middle), blue (bottom). No bar value labels, vertical gridlines only." |
| Usefulness | "Some medical bar chart" (no searchable terms, no domain) | "Expected remaining lifetime comparison from ERA 2023 report for general population vs. kidney patients" (domain identified) | "ERA 2023 Registry, slide 31. Prevalent dialysis and transplant patients vs. general population. At age 20-24, dialysis loses ~37 years vs. general population; transplant narrows loss to ~22 years. Uses prevalent (not incident) patients. Complements sex-stratified version on slide 32 (R42)." |

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
| Accuracy | "Infographic of life expectancy statistics" (wrong chart type; this is a grouped bar chart, not an infographic) | "Side-by-side bar charts comparing life expectancy for males and females across age groups and patient types" (correct structure) | "Two grouped horizontal bar charts: Males (left) and Females (right), each with 14 age bands and 3 series. At 20-24: male general ~58, transplant ~38, dialysis ~20-21; female general ~64, transplant ~42, dialysis ~27. No numeric labels on bars." |
| Specificity | "Chart showing males and females have the same life expectancy on dialysis" (wrong; females consistently higher) | "Females have longer bars than males in all three groups at every age. At 20-24, male general ~58 vs. female ~64." (key comparison) | "Males 20-24: general ~58, transplant ~38, dialysis ~20-21. Females 20-24: general ~64, transplant ~42, dialysis ~27. At 70-74 Males: ~12/~8/~5; Females: ~15/~10/~7. At 85-89 all bars converge to 2-5 years. 84 total bars (14 x 3 x 2)." |
| Completeness | "Bar charts about life expectancy by sex" (misses title, axis labels, age range, group names, panel structure) | "Two panels 'Males' and 'Females', same title as R41. Three series with shared legend. Y-axis 'Age (years)' on left panel only. X-axis 0-70 on both." (covers structure) | "Full title spanning both panels. Left panel 'Males', right panel 'Females'. Y-axis 'Age (years)' labeled only on left, 14 bands 20-24 to 85-89 on both. X-axis 'Expected remaining years of life' 0-70 on both. Legend between panels: General population (black), Transplant (olive), Dialysis (blue). No bar labels, vertical gridlines only, no panel border." |
| Usefulness | "Some medical charts about men and women" (no domain, no searchable terms) | "Sex-stratified remaining lifetime from ERA 2023 report for general population vs. kidney patients" (domain identified) | "ERA 2023 Registry, slide 32. Sex-stratified version of R41. Females have ~6-year longevity advantage in general population. Life-years lost to kidney failure similar in absolute terms for both sexes (~37 years at age 20-24). Transplant narrows the gap for both sexes." |

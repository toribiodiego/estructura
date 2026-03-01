# Image Analysis: Doc 28 -- 28_eurostat_climate_driving_forces_2022.xlsx

**Document:** `28_eurostat_climate_driving_forces_2022.xlsx`
**Format:** XLSX
**Source:** https://ec.europa.eu/eurostat/statistics-explained/images/1/18/Climate_change_driving_forces_2022_figures_and_tables.xlsx
**Category:** multi-image
**Images:** 29
**Document context:** Eurostat climate change driving forces statistical
workbook with 29 XML-defined charts across 24 figure sheets. 6 chart types
(line, bar, area, pie, scatter, combo) covering greenhouse gas emissions,
energy consumption, transport, agriculture, and waste indicators for EU
member states.

**Eval subset:** 6 of 29 content charts

<br><br>

## doc28-C01 -- Line: GHG emissions index 1990=100, 4 series

**Sheet:** Fig1
**Content type:** chart-complex
**Annotation difficulty:** Medium

**Note:** The right portion of the chart (~2015-2020) is truncated by the page
boundary in the LibreOffice PDF export. The two target series ("Target for
2020" and "Target for 2030 (net)") are likely rendered as short segments or
markers in the truncated region. Legend text for the first two series is also
truncated. European comma decimal notation is used throughout (e.g., ",100"
means 100).

### Visual Inventory [-> Information Recovery]

- **Chart type:** Line chart with 4 data series
- **Title:** "Greenhouse gas emissions, EU, 1990-2020 (index 1990 = 100)"
  (bold, black, two lines centered)
- **Subtitle (above title):** "enhouse gas emissions, EU, 1990-2020"
  (truncated at left -- this is a sheet header or navigation label, gray
  italic text)
- **Y-axis (vertical, left):** Scale from ",10" to ",100" in ",10" increments
  (European notation: these represent index values 10 to 100)
- **X-axis (horizontal, bottom):** Year labels from 1990 to ~2014 visible
  (rotated ~45 degrees), additional years truncated at right page edge
- **Gridlines:** Gray horizontal gridlines at each ",10" increment
- **Legend (below chart, 4 entries):**
  1. Cyan/light blue line -- "Total (excluding LULUCF and memo items,
     including internati..." (truncated)
  2. Pink/magenta line -- "Net GHG emissions (including LULUCF, excluding
     memo item..." (truncated)
  3. Dark blue line with diamond markers -- "Target for 2020"
  4. Dark pink/magenta line with diamond markers -- "Target for 2030 (net)"
- **Line data (visible portion, approximate index values):**
  - Both "Total" (cyan) and "Net GHG" (pink) lines start at ~100 in 1990
  - Lines track very close together throughout, with the Net GHG line
    generally slightly below the Total line
  - General downward trend from ~100 (1990) to ~75-80 (by ~2014)
  - Notable dip around 2009 (to ~83-85) followed by slight recovery
  - The two lines begin diverging more visibly after ~2005
- **Target lines:** Not clearly visible in the crop -- likely appear as short
  horizontal segments or markers in the truncated right portion (2020, 2030)
- **Source line:** "Source: EEA, republished by Eurostat (online data code:
  env_air_gge)" visible below the legend
- **Chart border:** Thin line enclosing the plot area
- **Background:** White

### Verifiable Facts [-> Correctness]

- FACT: The chart title reads "Greenhouse gas emissions, EU, 1990-2020
  (index 1990 = 100)"
- FACT: There are 4 legend entries
- FACT: The y-axis ranges from ",10" to ",100" in ",10" increments using
  European comma decimal notation
- FACT: Year labels on the x-axis are rotated approximately 45 degrees
- FACT: The x-axis begins at 1990 and extends rightward; years up to
  approximately 2014 are visible before the chart is truncated
- FACT: Both main data lines (Total and Net GHG) begin at approximately the
  ",100" gridline in 1990
- FACT: The Total line is cyan/light blue and the Net GHG line is
  pink/magenta
- FACT: The two main lines track very close together, with the Net GHG
  (pink) line generally slightly below the Total (cyan) line
- FACT: There is a visible dip in both lines around 2009
- FACT: The general trend is downward from left to right
- FACT: The "Target for 2020" legend shows a dark blue line with diamond
  markers
- FACT: The "Target for 2030 (net)" legend shows a dark pink line with
  diamond markers
- FACT: The source is attributed to "EEA, republished by Eurostat"

### Hallucination Risks [-> Correctness]

- RISK: Reporting specific index values for the target lines (e.g., "Target
  for 2020 = 80")
  REALITY: The target lines are not visible in the crop due to right-side
  truncation; any specific values would be fabricated from domain knowledge
  rather than read from the chart
- RISK: Stating the chart shows data through 2020 (as the title suggests)
  REALITY: Only data through approximately 2014 is visible in this render;
  the right portion is truncated at the page boundary
- RISK: Reading exact index values for specific years (e.g., "2009 value is
  83.5")
  REALITY: The y-axis gridlines are at ",10" intervals (10-unit steps) and
  the lines are thin; exact values between gridlines are approximate
- RISK: Confusing the two main data lines where they overlap closely
  (especially 1990-2005)
  REALITY: The cyan and pink lines are nearly indistinguishable in the
  1990-2000 region where they overlap; color differences become visible only
  when they diverge slightly after ~2005
- RISK: Interpreting European comma notation (",100") as thousands separators
  REALITY: The commas are decimal separators in European notation; ",100"
  means the integer 100, not "one hundred thousand"
- RISK: Describing the target lines as continuous series from 1990 to 2020
  REALITY: Target lines are likely single points or short segments positioned
  at their respective target years

### Detail Inventory [-> Information Recovery]

- Full chart title text (two lines): "Greenhouse gas emissions, EU, 1990-2020"
  and "(index 1990 = 100)"
- Truncated gray subtitle above: "enhouse gas emissions, EU, 1990-2020"
- Y-axis labels in European comma notation: ,10, ,20, ,30, ,40, ,50, ,60,
  ,70, ,80, ,90, ,100
- X-axis year labels rotated ~45 degrees: 1990, 1991, 1992, ... through ~2014
  visible
- Cyan line: Total GHG excluding LULUCF
- Pink/magenta line: Net GHG including LULUCF
- Dark blue with diamond: Target for 2020
- Dark pink with diamond: Target for 2030 (net)
- Both main lines start at ~,100 (index base year)
- Dip around 2009 (global financial crisis effect)
- Gradual divergence of Total vs Net lines after ~2005
- Source attribution to EEA/Eurostat with data code env_air_gge
- Gray horizontal gridlines at each 10-unit interval
- White chart background
- Right-side truncation at page boundary (~2015-2020 region missing)

### Domain Context [-> Retrieval Value]

This chart is Figure 1 from the Eurostat "Climate change - driving forces
2022" statistical workbook. It tracks EU greenhouse gas (GHG) emissions as an
index relative to 1990 levels (1990 = 100), comparing total emissions
(excluding land use change) against net emissions (including land use, land-use
change and forestry -- LULUCF).

The two target lines represent EU policy commitments: the 2020 target (20%
reduction below 1990 levels, i.e., index value of 80) and the 2030 net target
(55% reduction, i.e., index value of 45 under the European Green Deal/Fit for
55 package).

LULUCF (Land Use, Land-Use Change and Forestry) refers to the carbon
sequestration and emission effects of forests, cropland, and land management.
Including LULUCF typically lowers the net emissions figure because forests
absorb CO2. The visible dip around 2009 corresponds to the global financial
crisis reducing industrial output.

### Search Keywords [-> Retrieval Value]

greenhouse gas emissions, GHG, EU, index 1990=100, LULUCF, climate change,
Eurostat, EEA, line chart, emissions target, 2020 target, 2030 target,
European Green Deal, net emissions, driving forces, env_air_gge

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A line chart showing EU greenhouse gas emissions going down over time" -- no index values, no series names, no date range. Or: fabricates target line values (e.g., "Target for 2020 = 80") when these lines are not visible in the truncated crop. Or: states chart shows data through 2020 when only 1990-~2014 is visible. Any fabricated data point triggers the hallucination cap. | Title correct, 4 legend entries identified with correct colors and marker styles. Cyan/pink lines declining from ~100 to ~75-80 noted with appropriate hedging. 2009 dip identified. Right-side truncation acknowledged. May confuse European comma notation or miss that target lines are not visible in the crop. | All verifiable facts exact: title text (2 lines), y-axis ,10-,100 in ,10 steps (European comma notation), x-axis 1990-~2014 rotated 45 degrees. Cyan Total and pink Net GHG both start ~100, decline to ~75-80, track closely until ~2005 then diverge. 2009 dip noted. Target lines in legend only (dark blue/dark pink with diamond markers) -- correctly states they are not visible in the truncated right portion. No fabricated index values. |
| Information Recovery | Identifies as a line chart with declining emissions. No series names, no axis format, no legend details. A search for "LULUCF" or "Target for 2030" would not match. The European comma notation and 4-series structure are invisible to the system. | All 4 legend entries named with colors. Trend description present. Y-axis range and European notation documented. Right-side truncation noted. "EU GHG index 1990" would match. May miss the gray truncated subtitle, the closely-tracking behavior pre-2005, or the source data code. | Complete recovery: title text (2 lines), gray subtitle (truncated), 4 legend entries with line styles/colors/marker types, y-axis European comma notation ,10-,100, x-axis 1990-~2014 rotated, both main lines' trend behavior (close tracking, post-2005 divergence, 2009 dip), target lines in legend but not visible, source/data code env_air_gge, chart border, right-side truncation documented. Any chart element visible in the image is findable -- parity principle met. |
| Retrieval Value | "A Eurostat climate chart" -- no domain vocabulary, not self-contained. Would not surface for "GHG emissions index" or "LULUCF carbon accounting." Cannot understand what the index baseline means or why two measurement scopes exist. | "EU GHG emissions indexed to 1990=100 from Eurostat climate driving forces 2022. Total and Net lines decline. Reduction targets for 2020 and 2030." Contains searchable terms but doesn't explain LULUCF distinction or target values. Partially self-contained. | Natural prose identifying Fig1 from Eurostat climate change driving forces 2022. Explains two measurement scopes: Total (excl. LULUCF) and Net (incl. LULUCF). EU policy targets contextualized: 2020 (-20%, index 80) and 2030 net (-55%, index 45 under Fit for 55). 2009 dip linked to financial crisis. LULUCF explained (Land Use, Land-Use Change and Forestry). Domain vocabulary embedded. Self-contained. Findable by "EU GHG emissions trend" or "climate target index." |

<br><br>

## doc28-C07 -- Pie-of-pie: GHG by source sector, EU 2020

**Sheet:** Fig4
**Content type:** chart-complex
**Annotation difficulty:** Medium

**Note:** Several labels are truncated at the page boundary: "Manufacturing..."
(percentage cut off), "Households, commerce,... 15.4..." (last digit cut),
"Industrial processes and p..." (full text: "product use"), "Fuels - fugiti..."
(full text: "fugitive emissions", percentage shows only "1..."). The full
sector names are confirmed from the data table on the same rendered page.

### Visual Inventory [-> Information Recovery]

- **Chart type:** Pie-of-pie chart (main pie with a secondary "drill-down" pie
  connected by lines)
- **Title:** "...ssions by source sector, EU, 2020" (truncated at left; full
  title: "Greenhouse gas emissions by source sector, EU, 2020")
- **Main pie (right, larger) -- 9 sectors with percentage labels:**
  1. Energy industries -- 23.3% -- light cyan
  2. Manufacturing industries and construction -- percentage truncated at page
     edge -- magenta/pink
  3. Households, commerce, institutions, and others -- 15.4...% (last digit
     cut) -- dark blue
  4. Transport (including international aviation) -- 23.2% -- red
  5. Industrial processes and product use -- 9.4% -- olive/yellow-green
  6. Fuels - fugitive emissions -- 1...% (digit cut) -- blue (small slice)
  7. Agriculture -- percentage obscured by secondary pie overlap -- dark
     teal/green
  8. Waste management -- 3.3% -- pink/light purple (small slice)
  9. Indirect CO2 and other -- 0.0% -- very thin slice
- **Secondary pie (left, smaller) -- Fuel combustion subtotal:**
  - Label: "Fuel combustion" with "74.0%" centered inside
  - Color: dark teal, matching the "combustion" portion of the energy sectors
  - Connected to the main pie by two thin lines forming a wedge shape
  - This pie appears to aggregate the fuel combustion component across
    multiple source sectors
- **Connecting lines:** Two thin diagonal lines connect the secondary pie to
  a wedge region of the main pie
- **Source line:** "...ostat (online data code: env_air_gge)" (truncated at
  left)
- **Background:** White
- **No legend** -- all labels are directly on or adjacent to slices

### Verifiable Facts [-> Correctness]

- FACT: The chart is a pie-of-pie (two connected pie charts)
- FACT: The main pie has 9 labeled sectors
- FACT: Energy industries = 23.3%
- FACT: Transport (including international aviation) = 23.2%
- FACT: Households, commerce,... = 15.4...% (truncated)
- FACT: Industrial processes and p... = 9.4%
- FACT: Waste management = 3.3%
- FACT: Indirect CO2 and other = 0.0%
- FACT: The secondary pie is labeled "Fuel combustion 74.0%"
- FACT: Energy industries and Transport are the two largest sectors (both
  ~23%)
- FACT: Two thin lines connect the secondary pie to the main pie
- FACT: Labels are placed directly on/adjacent to slices (no separate legend)
- FACT: The data code is env_air_gge

### Hallucination Risks [-> Correctness]

- RISK: Fabricating the truncated percentage for "Manufacturing industries
  and construction"
  REALITY: The percentage label is cut off at the right page edge; it cannot
  be read from this crop alone
- RISK: Stating Agriculture percentage (e.g., "Agriculture 10.8%")
  REALITY: The Agriculture label is partially obscured by the secondary pie
  overlap; the percentage is not clearly readable in the crop
- RISK: Stating the "Fuels - fugitive emissions" percentage as a specific
  value (e.g., "1.5%")
  REALITY: Only "1..." is visible; the remaining digits are truncated
- RISK: Describing the secondary pie as showing a breakdown of fuel
  combustion by sub-sector
  REALITY: The secondary pie appears to show fuel combustion as a single
  aggregate (74.0%) without visible sub-sector breakdown within it
- RISK: Claiming all 9 sector percentages sum to exactly 100%
  REALITY: Several percentages are truncated, making verification impossible
  from the crop alone
- RISK: Misidentifying which sectors are "fuel combustion" vs non-combustion
  REALITY: The connecting lines between pies are small and the wedge they
  delimit is not precisely clear

### Detail Inventory [-> Information Recovery]

- Title text (truncated): "...ssions by source sector, EU, 2020"
- 9 sector names with their full text from data table: Energy industries,
  Manufacturing industries and construction, Households/commerce/
  institutions/others, Transport (incl. international aviation), Industrial
  processes and product use, Fuels - fugitive emissions, Agriculture, Waste
  management, Indirect CO2 and other
- Readable percentages: 23.3%, 23.2%, 15.4...%, 9.4%, 3.3%, 0.0%
- Truncated percentages: Manufacturing (not visible), Fuels (1...%),
  Agriculture (obscured)
- Secondary pie: "Fuel combustion 74.0%" in dark teal
- Color scheme: light cyan (energy), magenta/pink (manufacturing), dark blue
  (households), red (transport), olive/yellow-green (industrial processes),
  blue (fuels fugitive), dark teal (agriculture), pink/purple (waste),
  thin slice (indirect CO2)
- Two connecting lines from secondary to main pie
- Source: Eurostat, data code env_air_gge
- No separate legend -- direct labeling only
- Page boundary truncation affects right-side labels

### Domain Context [-> Retrieval Value]

This is Figure 4 from Eurostat's "Climate change - driving forces 2022"
workbook. It shows the breakdown of EU greenhouse gas emissions by IPCC source
categories for the year 2020.

The pie-of-pie format highlights that fuel combustion (74.0%) is the dominant
source of GHG emissions, cutting across multiple sectors (energy industries,
manufacturing, households, transport). The remaining 26% comes from
non-combustion sources: industrial processes (chemical reactions, cement
production), fugitive emissions (leaks from fuel extraction/distribution),
agriculture (livestock, fertilizers), waste management (landfills), and
indirect CO2.

Transport and energy industries are nearly equal as the top two sectors (~23%
each), together accounting for almost half of EU emissions. IPCC = the
Intergovernmental Panel on Climate Change source categorization framework.

### Search Keywords [-> Retrieval Value]

greenhouse gas emissions, GHG by source sector, EU 2020, pie-of-pie chart,
fuel combustion, energy industries, transport, manufacturing, agriculture,
waste management, IPCC source categories, Eurostat, env_air_gge, climate
change driving forces

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A pie chart showing EU emissions by sector with Energy and Transport as the largest" -- misses pie-of-pie structure, no specific values, no truncation note. Or: fabricates the truncated Manufacturing percentage or states Agriculture percentage (obscured by secondary pie overlap). Any invented percentage for a truncated/obscured label triggers the hallucination cap. | Pie-of-pie structure identified. Readable percentages correct: Energy 23.3%, Transport 23.2%, Industrial processes 9.4%, Waste 3.3%, Indirect CO2 0.0%. Secondary pie 74.0% correct. Notes that Manufacturing and Fuels percentages are truncated. May miss that Agriculture is obscured by secondary pie overlap. | All readable percentages exact: Energy industries 23.3%, Transport (incl. aviation) 23.2%, Households/commerce 15.4...% (last digit cut), Industrial processes 9.4%, Waste management 3.3%, Indirect CO2 0.0%. Three unreadable values correctly flagged: Manufacturing (truncated at page edge), Fuels fugitive (only "1..." visible), Agriculture (obscured by secondary pie). Secondary pie "Fuel combustion 74.0%" exact. No fabricated percentages for truncated labels. |
| Information Recovery | Identifies as a pie chart with emission sectors. Names 2-3 sectors. No pie-of-pie structure, no specific percentages, no truncation documentation. A search for "Fuel combustion 74%" or "Industrial processes 9.4%" would not match. Most of the 9 sectors invisible to the system. | Most sectors named with readable percentages. Pie-of-pie structure captured. Truncated labels documented. "GHG by source sector" would match. May miss the specific truncation details (which digit is cut, which label is obscured vs truncated) or the direct-labeling format (no legend). | Complete recovery: all 9 sector names, 6 readable percentages exact, 3 truncated/obscured values documented with what IS visible ("1..." for Fuels, "15.4..." for Households). Secondary pie with label text and 74.0% value. Two connecting lines. Direct callout labeling (no legend). Source data code. Title truncation noted. Any sector visible in the chart is findable -- parity principle met. |
| Retrieval Value | "An EU emissions breakdown chart from Eurostat" -- no domain vocabulary, not self-contained. Would not surface for "IPCC source categories" or "fuel combustion share." Cannot understand why the pie-of-pie structure matters analytically. | "EU 2020 GHG by source sector from Eurostat. Energy and Transport each ~23%. Fuel combustion 74%." Contains searchable terms but doesn't explain the fuel combustion cross-cutting significance or IPCC categorization. Partially self-contained. | Natural prose identifying Fig4 from Eurostat climate change driving forces 2022. Explains IPCC source categorization: fuel combustion (74%) cuts across multiple sectors (energy, manufacturing, households, transport). Transport and energy industries near-equal at ~23% each (nearly half of total). Non-combustion sources contextualized (industrial processes, fugitive emissions, agriculture, waste). Domain vocabulary embedded (IPCC, fuel combustion, fugitive emissions). Self-contained. Findable by "GHG by source sector" or "fuel combustion share EU." |

<br><br>

## doc28-C08 -- Combo bar+marker: GHG change by source sector 1990-2020

**Sheet:** Fig5
**Content type:** chart-complex
**Annotation difficulty:** Hard

**Note:** The catalog describes this as "Combo (area+bar+line)" but the rendered
crop shows vertical bars plus diamond markers -- no continuous line or area fill
is visible. The x-axis labels render as generic numbers "1, 2, 3, 4" instead of
sector names (a LibreOffice chart rendering limitation). The right portion of the
chart is truncated by the page boundary: the title's closing parenthesis is cut
off, the legend text is truncated, no secondary y-axis for % change is visible,
and additional bars for sectors 5-8 may extend beyond the page. The data table on
the adjacent rendered page confirms the sector mapping: 1 = Energy industries,
2 = Manufacturing industries and construction, 3 = Households/commerce/
institutions/others, 4 = Transport (including international aviation).

### Visual Inventory [-> Information Recovery]

- **Chart type:** Combo chart with vertical bars and diamond markers (2 visual
  encodings: bars for absolute change, markers likely for % change)
- **Title (3 lines, centered, bold):**
  1. "Greenhouse gas emissions by source sector, EU"
  2. "change from 1990 to 2020"
  3. "(million tonnes of CO2 equivalent and % change" -- closing parenthesis
     truncated at right page edge
- **Sheet navigation label (above title):** "Greenhouse gas emissions by source
  sector, EU, change from 1990 to 2020" (small text, yellow highlight arrow
  icon at left)
- **Y-axis (vertical, left):** Scale from -700 to 100 in 100-unit increments
  (labels: 100, 0, -100, -200, -300, -400, -500, -600, -700)
- **X-axis (horizontal, bottom):** Labels "1", "2", "3", "4" (rotated ~45
  degrees). These are generic numeric placeholders -- sector names did not render
  in the LibreOffice PDF export
- **Gridlines:** Gray horizontal gridlines at each 100-unit increment
- **Bars (teal/cyan, 4 visible):**
  - Bar 1: extends from 0 downward to approximately -620 to -640 (longest bar,
    past the -600 gridline)
  - Bar 2: extends from 0 downward to approximately -310 to -330 (between -300
    and -400 gridlines, closer to -300)
  - Bar 3: extends from 0 downward to approximately -100 to -120 (near the -100
    gridline)
  - Bar 4: extends from 0 UPWARD to approximately +50 to +60 (the only positive
    bar, between 0 and 100 gridlines)
- **Diamond markers (light blue/pale cyan, 4 visible):** One small diamond
  marker appears near each bar. Positioned at vertical coordinates that do NOT
  correspond to the left y-axis scale in a meaningful way -- these are likely
  plotted against a secondary (right) y-axis for % change that is not visible
  due to right-side truncation:
  - Marker 1: near bar 1, at approximately y = -540 (left-axis reading)
  - Marker 2: near bar 2, at approximately y = -530 (left-axis reading)
  - Marker 3: near bar 3, at approximately y = -380 to -400 (left-axis reading)
  - Marker 4: near bar 4, at approximately y = -20 to -40 (left-axis reading)
- **Right edge:** Additional chart content appears truncated at the page
  boundary. A thin teal vertical element is partially visible at the far right
  edge, suggesting additional bars (sectors 5-8) may have been cut off
- **Legend (below chart, partially truncated):** Shows teal square icon followed
  by "absolute change in million ton..." (text truncated at right edge). A
  second legend entry for the diamond markers is not visible (likely also
  truncated)
- **Note (below legend):** "Note: fuel combustion as a source of GHG emissions
  is indicated by the grey ba..." (truncated; full text: "grey background
  shading")
- **Source line:** "Source: EEA, republished by Eurostat (online data code:
  env_air_gge)"
- **Grey background shading:** The note references grey background shading to
  indicate fuel combustion sectors, but this shading is not clearly discernible
  in the rendered crop
- **Secondary y-axis (right):** Not visible -- truncated at the right page edge.
  Based on the title mentioning "% change", this axis likely shows percentage
  change values
- **Background:** White
- **Chart border:** Thin line enclosing the plot area

### Verifiable Facts [-> Correctness]

- FACT: The chart title includes "Greenhouse gas emissions by source sector, EU
  change from 1990 to 2020 (million tonnes of CO2 equivalent and % change"
  (closing parenthesis truncated)
- FACT: There are exactly 4 visible bars in the chart
- FACT: There are exactly 4 visible diamond markers
- FACT: The x-axis labels read "1", "2", "3", "4" (not sector names)
- FACT: The y-axis ranges from -700 to 100 in 100-unit increments
- FACT: Bar 1 is the longest, extending past the -600 gridline (negative)
- FACT: Bar 4 is the only bar extending above zero (positive)
- FACT: Bars 1, 2, and 3 all extend downward (negative values)
- FACT: Bar 1 is significantly longer than Bar 2, which is significantly longer
  than Bar 3
- FACT: All 4 bars are the same teal/cyan color
- FACT: The legend text reads "absolute change in million ton..." (truncated)
- FACT: The note references "grey background shading" for fuel combustion
- FACT: The source is "EEA, republished by Eurostat (online data code:
  env_air_gge)"
- FACT: No secondary y-axis is visible on the right side of the chart

### Hallucination Risks [-> Correctness]

- RISK: Stating specific sector names for bars 1-4 (e.g., "Energy industries",
  "Manufacturing")
  REALITY: The x-axis shows only "1, 2, 3, 4". The sector names are confirmed
  by the data table on an adjacent page, but they are NOT readable in the chart
  crop itself
- RISK: Reading diamond marker values from the left y-axis (e.g., "marker 1 is
  at -540 million tonnes")
  REALITY: The diamond markers are likely plotted on a secondary y-axis (for %
  change) that is not visible due to truncation. Reading their pixel position
  against the left axis produces meaningless values
- RISK: Stating specific % change values for any sector
  REALITY: No secondary y-axis is visible, so % change values cannot be read
  from this crop
- RISK: Describing this as an "area+bar+line" chart (matching the catalog)
  REALITY: No area fill or continuous line connecting markers is visible in the
  rendered crop. The visible encodings are bars + unconnected diamond markers
- RISK: Stating the chart shows all 8 IPCC source sectors
  REALITY: Only 4 bars are visible. Additional bars for sectors 5-8 may be
  truncated at the right page boundary, or the chart may show only a subset
- RISK: Fabricating exact bar values (e.g., "Energy industries reduced by
  exactly 627 Mt")
  REALITY: No data labels are present. Y-axis gridlines are at 100-unit
  intervals, allowing only coarse estimation (~50 Mt precision)
- RISK: Describing grey background shading behind fuel combustion bars
  REALITY: The note mentions this shading, but it is not clearly discernible
  in the rendered crop
- RISK: Stating the chart has 4 data series because the catalog says "4 series"
  REALITY: What is visible is 2 visual encodings (bars and markers) across 4
  categories. The "4 series" label in the catalog may refer to categories, not
  data series

### Detail Inventory [-> Information Recovery]

- Title text across 3 lines (third line truncated at closing parenthesis)
- Sheet navigation label with yellow arrow icon
- Y-axis labels: 100, 0, -100, -200, -300, -400, -500, -600, -700
- X-axis labels: 1, 2, 3, 4 (rotated ~45 degrees, generic numbers)
- 4 teal/cyan bars: approximate heights -620, -320, -120, +50
- 4 light blue/pale diamond markers at distinct vertical positions
- Bar 1 longest (past -600 gridline), Bar 4 only positive
- Gray horizontal gridlines at each 100-unit step
- Legend with teal square: "absolute change in million ton..." (truncated)
- No visible second legend entry for diamond markers
- Note about fuel combustion grey background shading (truncated)
- Source: EEA/Eurostat, data code env_air_gge
- Right-side page boundary truncation affecting: title, legend, note, possible
  additional bars, secondary y-axis
- White chart background
- Thin chart border enclosing plot area
- No data labels on bars or markers
- No visible area fill or line connecting diamond markers

### Domain Context [-> Retrieval Value]

This chart is Figure 5 from Eurostat's "Climate change - driving forces 2022"
workbook. It shows the absolute change in greenhouse gas emissions by IPCC source
sector between 1990 and 2020 (in million tonnes of CO2 equivalent), with diamond
markers indicating percentage change.

The data table on the adjacent page confirms the sector mapping:
- Bar 1 (Energy industries): largest absolute reduction, reflecting the EU's
  shift toward renewable electricity generation
- Bar 2 (Manufacturing industries and construction): significant reduction from
  industrial efficiency improvements and structural economic changes
- Bar 3 (Households, commerce, institutions): smaller reduction from building
  energy efficiency improvements
- Bar 4 (Transport including international aviation): the only sector showing an
  INCREASE in emissions from 1990 to 2020, consistent with well-known growth in
  road transport and aviation

The chart's dual encoding (absolute + percentage change) is important because
sectors with large absolute reductions may have different percentage reductions
depending on their 1990 baseline. The secondary axis (not visible in this crop)
would show this percentage perspective.

The note about "grey background shading for fuel combustion" refers to the
distinction between combustion-related emissions (burning fossil fuels) and
process emissions (e.g., cement production, agricultural methane) -- a key
analytical distinction in climate policy.

### Search Keywords [-> Retrieval Value]

greenhouse gas emissions, GHG by source sector, EU, change 1990-2020, absolute
change, percentage change, million tonnes CO2 equivalent, energy industries,
manufacturing, transport emissions increase, combo chart, bar chart with markers,
Eurostat, EEA, env_air_gge, climate change driving forces, IPCC source
categories, fuel combustion

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A bar chart showing emissions reductions by sector with Energy having the largest reduction" -- fabricates sector names from domain knowledge when x-axis only shows "1,2,3,4." Naming sectors visible only in a separate data table triggers the hallucination cap. Or: reads diamond marker positions against the left y-axis as absolute values when they are likely mapped to an invisible secondary % axis. | Combo bar+marker structure identified. 4 bars with correct direction (3 negative, 1 positive). Approximate bar heights reasonable (~-620, ~-320, ~-120, ~+50). X-axis labels correctly described as "1,2,3,4" (not sector names). Diamond markers noted. Right-side truncation acknowledged. May conflate marker values with left-axis readings. | All verifiable facts exact: 3-line title (third truncated at closing parenthesis), y-axis -700 to 100 in 100-unit steps, x-axis "1,2,3,4" rotated ~45 degrees (sector names did not render). 4 teal bars with approximate heights hedged to gridline precision (~50 Mt). 4 pale diamond markers noted with caveat that their positions likely map to invisible secondary % axis. Legend truncated. Note about grey fuel combustion shading. No fabricated sector names or exact bar values. |
| Information Recovery | Identifies as a bar chart with 4 bars. No dual encoding (bars + markers), no axis ranges, no truncation details. A search for "combo bar marker chart" or "secondary axis truncated" would not match. The dual encoding and rendering limitations are invisible to the system. | Both visual encodings documented (bars for absolute, markers for % change). Bar heights approximated. X-axis generic labels noted. Y-axis range documented. Truncation described (legend, title, possible additional bars). "GHG change by sector" would match. May miss the fuel combustion shading note or the secondary axis inference. | Complete recovery: 3-line title text (third truncated), sheet navigation label, 4 bars with approximate heights, 4 diamond markers with positions and secondary-axis caveat, x-axis generic "1-4" (sector names failed to render), y-axis -700 to 100 with gridlines, truncated legend text, note about grey shading (truncated), source/data code env_air_gge, right-side truncation documented (title, legend, possible bars 5-8, secondary axis). Any chart element visible in the crop is findable -- parity principle met. |
| Retrieval Value | "An emissions chart from Eurostat" -- no domain vocabulary, not self-contained. Would not surface for "sector emissions change" or "transport emissions increase." Cannot understand the dual encoding or why the rendering failed. | "Absolute GHG change by sector 1990-2020 from Eurostat. Largest reduction in sector 1 (~-620 Mt). Sector 4 is the only increase (~+50 Mt)." Contains searchable terms but can't explain which sectors these are or why the dual encoding matters. Partially self-contained. | Natural prose identifying Fig5 from Eurostat climate change driving forces 2022. Explains dual encoding: bars for absolute change (Mt CO2eq), markers for percentage change (secondary axis truncated). Data table confirms sector mapping: Energy industries (~-620 Mt, largest reduction), Manufacturing (~-320 Mt), Households (~-120 Mt), Transport (~+50 Mt, only sector with increased emissions). Transport growth contextualized as a key EU climate policy challenge. Domain vocabulary embedded (IPCC source sectors, CO2 equivalent, fuel combustion). Self-contained. |

<br><br>

## doc28-C11 -- Stacked area: Electricity/heat from renewables, 7 series

**Sheet:** Fig8
**Content type:** chart-complex
**Annotation difficulty:** Medium

**Note:** The right portion of the chart is truncated by the page boundary,
cutting off the title text, final ~15 years of data (approximately 2006-2020),
and additional legend entries beyond the 4 visible. The catalog states 7 series
but only 4 legend entries are readable (Hydro, Wind, Solar photovoltaic, Primary
solid biofuels). Approximately 5-6 distinct color layers are visible in the
stacked area, suggesting additional series exist but their legend labels are
truncated. The data table on the same page confirms series including Wind and
Solar photovoltaic at 0 in 1990, growing in later years. The note below the
chart identifies the "Other" category as: geothermal, solar thermal, tide, wave,
ocean, liquid biofuels and ambient air.

### Visual Inventory [-> Information Recovery]

- **Chart type:** Stacked area chart with multiple colored area layers
- **Title (3 lines, centered, bold, truncated at right):**
  1. "Gross electricity and heat production from renewa..." (truncated; full:
     "renewables and biofuels, EU, 1990-")
  2. "2020"
  3. "(million tonnes of oil equiv..." (truncated; full: "oil equivalent)")
- **Sheet navigation label (above title):** "Gross electricity and heat
  production from renewables and biofuels, EU, 1990-2020" (small text, yellow
  highlight arrow icon)
- **Y-axis (vertical, left):** Scale from approximately -10 to 110, with labels
  at 10, 30, 50, 70, 90, 110 (20-unit increments). A "- 10" label appears at
  the very bottom near the x-axis origin
- **X-axis (horizontal, bottom):** Year labels from 1990 to approximately 2005
  visible (rotated ~45 degrees). Visible years: 1990, 1991, 1992, 1993, 1994,
  1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 200... (truncated
  at right page edge)
- **Gridlines:** Gray horizontal gridlines at each 20-unit increment
- **Stacked area layers (bottom to top, based on visible colors):**
  1. **Cyan/teal (dominant base layer)** -- Hydro. Fills from ~0 to ~20-25
     throughout. Relatively flat with year-to-year fluctuation (hydro depends on
     rainfall). Slight upward trend but relatively stable compared to other
     sources
  2. **Olive/yellow-green (thin layer above cyan)** -- likely an unlabeled
     series from the truncated legend. Very thin in early years, slightly growing
  3. **Red/crimson (visible layer)** -- Primary solid biofuels. Thin consistent
     band, slightly growing over time
  4. **Magenta/pink (growing layer)** -- Wind. Negligible in 1990-1995, begins
     growing visibly from ~2000 onward, becoming a significant layer by ~2004-2005
  5. **Dark blue/navy (late-appearing layer)** -- Solar photovoltaic. Barely
     visible until ~2003-2005, appearing as a thin band at the top-right
  6. **Yellow/gold (very thin top layer)** -- possibly another unlabeled series
     (Biogas or Other). Thin sliver at the very top of the stack
- **Total stack height:** approximately 28-30 in 1990, growing to approximately
  45-50 by ~2005 (the latest visible year)
- **Legend (below chart, 4 entries visible, remainder truncated):**
  1. Cyan square -- "Hydro"
  2. Magenta/pink square -- "Wind"
  3. Dark blue square -- "Solar photovoltaic"
  4. Red/crimson square -- "Primary solid biof..." (truncated; full: "Primary
     solid biofuels")
  - Additional legend entries for remaining series are truncated at right page
    edge
- **Note (below legend, truncated):** "Note: Other consists of geothermal, solar
  thermal, tide, wave, ocean, liquid biof..." (truncated; full: "liquid biofuels
  and ambient air")
- **Source line:** "Source: Eurostat (online data code: nrg_bal_c)"
- **Background:** White
- **Chart border:** Thin line enclosing the plot area

### Verifiable Facts [-> Correctness]

- FACT: The chart is a stacked area chart with multiple colored layers
- FACT: The title begins "Gross electricity and heat production from renewa..."
  (truncated at right)
- FACT: The subtitle reads "2020" and the third line reads "(million tonnes of
  oil equiv..." (truncated)
- FACT: The y-axis shows labels at 10, 30, 50, 70, 90, 110
- FACT: The x-axis shows year labels from 1990 through approximately 2005
  (rotated ~45 degrees)
- FACT: The cyan/teal (Hydro) layer is the dominant base, filling most of the
  area height
- FACT: The total stack height in 1990 is approximately 28-30 units
- FACT: The total stack height grows to approximately 45-50 by the latest
  visible year (~2005)
- FACT: Wind (magenta/pink) is negligible in the early 1990s but visibly growing
  from ~2000 onward
- FACT: Solar photovoltaic (dark blue) is barely visible, appearing only in the
  last few visible years
- FACT: 4 legend entries are visible: Hydro, Wind, Solar photovoltaic, Primary
  solid biofuels
- FACT: The note mentions "Other" as consisting of geothermal, solar thermal,
  tide, wave, ocean, liquid biofuels
- FACT: The source is Eurostat with data code nrg_bal_c
- FACT: The right portion of the chart (~2006-2020) is truncated by the page
  boundary

### Hallucination Risks [-> Correctness]

- RISK: Stating the chart covers data through 2020 (as the title suggests)
  REALITY: Only data through approximately 2005 is visible. The final 15 years
  are truncated at the page boundary, which is significant because the fastest
  growth in wind and solar occurred after 2005
- RISK: Reporting specific values for individual series in specific years (e.g.,
  "Hydro was 26 Mtoe in 1990")
  REALITY: No data labels are present. Y-axis gridlines are at 20-unit intervals,
  allowing only coarse estimation. The data table on the same page confirms exact
  values but the chart itself only allows visual approximation
- RISK: Naming all 7 series confidently
  REALITY: Only 4 series are labeled in the visible legend. The additional 2-3
  thin layers visible in the chart cannot be definitively identified without the
  truncated legend entries
- RISK: Describing the dramatic growth of wind and solar power
  REALITY: In the visible portion (1990-2005), wind is just beginning to grow and
  solar is barely visible. The dramatic growth occurred after 2005, in the
  truncated region. Describing a "solar revolution" based on this crop would be
  fabricating trends from domain knowledge, not from the chart
- RISK: Confusing the stacking order of the thin middle layers
  REALITY: Between the large Hydro base and the visible Wind/Solar layers, there
  are thin layers of olive/yellow-green, red, and possibly other colors. These
  are difficult to distinguish at this resolution
- RISK: Describing the Hydro layer as "constant" or "declining"
  REALITY: The Hydro layer fluctuates year-to-year (hydropower depends on
  precipitation) but has a slight overall upward trend. It appears relatively
  flat compared to the growing renewable sources, but is not constant

### Detail Inventory [-> Information Recovery]

- Title text across 3 lines (all partially truncated at right edge)
- Sheet navigation label with yellow arrow: full title visible
- Y-axis labels: 110, 90, 70, 50, 30, 10 (plus "- 10" near x-axis)
- Y-axis gridlines at 20-unit intervals
- X-axis years: 1990-~2005 rotated ~45 degrees
- 5-6 distinct color layers visible in stacked area
- Identified layers: cyan (Hydro), magenta/pink (Wind), dark blue (Solar PV),
  red/crimson (Primary solid biofuels)
- Unidentified layers: olive/yellow-green (thin), yellow/gold (thin at top)
- Hydro: ~20-25 Mtoe, base layer, slight year-to-year fluctuation
- Wind: negligible pre-2000, growing to visible band by ~2004-2005
- Solar PV: barely visible, thin sliver at far right only
- Primary solid biofuels: thin consistent red band, slight growth
- Total stack: ~28-30 (1990) to ~45-50 (~2005)
- 4 legend entries visible (7 expected per catalog)
- Note about "Other" category composition (truncated)
- Source: Eurostat, data code nrg_bal_c
- Right-side page boundary truncation: ~15 years of data cut off
- White background, thin chart border

### Domain Context [-> Retrieval Value]

This chart is Figure 8 from Eurostat's "Climate change - driving forces 2022"
workbook. It shows gross electricity and heat production from renewable and
biofuel sources in the EU from 1990 to 2020, measured in million tonnes of oil
equivalent (Mtoe).

The stacked area format reveals how the EU's renewable energy mix has evolved.
Hydropower has been the dominant renewable source since the 1990s, providing a
relatively stable base of ~20-25 Mtoe. Wind energy began growing significantly
from around 2000, while solar photovoltaic became notable only in the later
years (mostly after 2005, in the truncated portion of this chart).

"Primary solid biofuels" refers to wood, wood waste, and other solid biomass
burned directly for electricity or heat generation. "Other" encompasses
geothermal, solar thermal (concentrated solar power), tidal, wave, ocean energy,
liquid biofuels (e.g., biodiesel used in CHP plants), and ambient heat (heat
pumps).

The data code nrg_bal_c refers to Eurostat's energy balance statistics. The unit
"million tonnes of oil equivalent" is the standard EU energy accounting unit
(1 Mtoe = 41.868 PJ).

The truncation is particularly impactful for this chart because the most dramatic
changes in the EU renewable energy mix occurred after 2005 (the latest visible
year), with wind and solar capacity expanding enormously under the EU Renewable
Energy Directive.

### Search Keywords [-> Retrieval Value]

electricity heat production, renewables, biofuels, EU 1990-2020, stacked area
chart, hydropower, wind energy, solar photovoltaic, primary solid biofuels,
million tonnes oil equivalent, Mtoe, Eurostat, nrg_bal_c, climate change driving
forces, renewable energy mix, energy transition

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A stacked area chart showing renewable energy growth in the EU with solar and wind growing dramatically" -- fabricates dramatic growth from domain knowledge. In the visible 1990-~2005 range, wind is just beginning to grow and solar is barely a sliver. Describing a "solar revolution" based on this crop triggers the hallucination cap. Or: names all 7 series when only 4 legend entries are visible. | Stacked area structure identified. Hydro as dominant base (~20-25 Mtoe) correct. Wind growing from ~2000 onward. 4 visible legend entries named correctly. Right-side truncation acknowledged (~2006-2020 missing). Total stack height approximated. May over-describe thin unidentified layers or miss the year-to-year hydro fluctuation. | All verifiable facts exact: 3-line title (all truncated at right), y-axis 10-110 in 20-unit steps, x-axis 1990-~2005 rotated. Hydro (cyan) base ~20-25 with year-to-year fluctuation. Wind (magenta) negligible pre-2000, growing by ~2005. Solar PV (dark blue) barely visible at far right. Primary solid biofuels (red) thin consistent band. 1-2 additional thin unidentified layers noted without fabricating names. 4 of 7 legend entries visible -- correctly states remainder truncated. No fabricated growth trends for the missing 2006-2020 period. |
| Information Recovery | Identifies as a stacked area chart with some renewable sources. Names 1-2 layers. No axis ranges, no layer proportions, no truncation documentation. A search for "Hydro base layer" or "nrg_bal_c" would not match. The 5-6 layer structure and legend truncation are invisible to the system. | 4 labeled layers named (Hydro, Wind, Solar PV, biofuels) with approximate proportions. Stack height growth documented. Y-axis range and truncation noted. "Renewable energy stacked area" would match. May miss the unidentified thin layers, the "Other" category note, or the sheet navigation label. | Complete recovery: title text (3 truncated lines), sheet navigation label with full title, y-axis labels and gridlines, x-axis 1990-~2005, all 5-6 visible layers described (4 identified, 1-2 unidentified), layer heights and growth trends, total stack height over time, 4 of 7 legend entries, note about "Other" composition (truncated), source/data code nrg_bal_c, right-side truncation documented (~15 years missing). Any visible chart element is findable -- parity principle met. |
| Retrieval Value | "A renewable energy chart from Eurostat" -- no domain vocabulary, not self-contained. Would not surface for "hydropower dominance" or "EU renewable energy mix evolution." Cannot understand why the truncation matters analytically. | "EU renewable electricity/heat 1990-~2005 from Eurostat. Hydro dominates. Wind beginning to grow." Contains searchable terms but doesn't explain the analytical significance of the truncation or the energy unit (Mtoe). Partially self-contained. | Natural prose identifying Fig8 from Eurostat climate change driving forces 2022. Explains EU renewable energy mix evolution: hydropower stable ~20-25 Mtoe base, wind emerging from ~2000, solar PV barely visible by 2005. Truncation at ~2005 is analytically significant: post-2005 EU Renewable Energy Directive drove massive wind/solar growth not visible in this crop. "Other" category contextualized (geothermal, solar thermal, tidal, wave, ocean, liquid biofuels, ambient air). Unit explained (Mtoe). Domain vocabulary embedded. Self-contained. Findable by "EU renewable energy mix" or "hydropower stacked area." |

<br><br>

## doc28-C24 -- Combo (area+line): LULUCF GHG, 7 series

**Sheet:** Fig19
**Content type:** chart-complex
**Annotation difficulty:** Hard

### Visual Inventory [-> Information Recovery]

- **Chart type:** Stacked area chart with 6 area series and 1 overlaid line
  (combo area+line)
- **Title:** "Greenhouse gas emissions from LULUCF (Land use, land use
  c..." (truncated at right page edge; full title from data table below:
  "Greenhouse gas emissions from LULUCF, EU, 1990-2020")
- **Subtitle:** "(million tonnes of CO2 equivale..." (truncated; full:
  "million tonnes of CO2 equivalent")
- **Y-axis (vertical, left):** Labeled from -500 to 100 in increments of 100
  (tick marks at 100, 0, -100, -200, -300, -400, -500)
- **X-axis (horizontal, bottom):** Years from 1990 to 2007 visible, labels at
  45-degree angle. The chart should extend to 2020 per the data table title
  but the right portion is truncated by the page boundary
- **Gridlines:** Light gray horizontal gridlines at each 100-unit increment
  (7 gridlines)
- **Area series (bottom to top in the stack):**
  - Forest land (teal/cyan): Dominant area, filling most of the negative
    region. Extends from approximately -250 (bottom boundary, 1990) to about
    +10/+20 (top boundary). The band narrows from 1990 to the mid-1990s, then
    remains relatively stable around -280 to +15. This is the net carbon sink
  - Cropland (dark navy/royal blue): Thin positive band sitting on top of
    Forest land, extending above the 0 line to approximately +20 to +40.
    Relatively stable over time
  - Grassland (red/salmon): Extremely thin band, barely visible as a
    distinct area. Appears as a red line running at approximately -250 to -350
    through the chart. May be the lower boundary of the stacked area or a
    separate overlaid line
  - Wetlands (light blue/cyan): Barely visible thin band if present as a
    distinct area; not distinguishable from Forest land at this scale
  - Settlements: Not visible as a distinct area in the crop (legend entry
    truncated to "S...")
  - Other land: Not visible as a distinct area (legend entry fully truncated)
- **Overlaid line:** A red/scarlet line is visible running through the chart at
  approximately -230 (1990) to -350 (2006-2007), with fluctuations. This
  appears to represent either the Grassland area boundary or the net LULUCF
  total line. The line dips notably around 2000-2001 (reaching approximately
  -360) and again around 2006 (reaching approximately -380)
- **Legend:** Single row below the chart. 5 of 7 entries visible (left to
  right): Forest land (teal square), Cropland (dark blue square), Grassland
  (red/salmon square), Wetlands (light blue square), "S..." (truncated,
  likely Settlements with pink/magenta square). Two rightmost entries are
  cut off by the page boundary (likely Other land and LULUCF total line)
- **Data labels:** None
- **Source note:** "Source: EEA, republished by Eurostat (online data code:
  env_air_gge)" appears twice (once in italics as chart footer, once as
  hyperlinked text below)
- **Chart border:** Thin gray line on left and top edges of plot area
- **Background:** White
- **Data table:** Begins at the bottom of the crop, showing
  "Greenhouse gas emissions from LULUCF, EU, 1990-2020 (million tonnes of
  CO2 equivalent)" with row headers: "Land use, land use change, and
  forestry (LULUCF)" and "Forest land" visible before the crop ends

### Verifiable Facts [-> Correctness]

- FACT: The chart is a stacked area chart with at least one overlaid line
- FACT: The title begins "Greenhouse gas emissions from LULUCF (Land use,
  land use c..." and is truncated at the right edge
- FACT: The y-axis ranges from -500 to 100 in increments of 100
- FACT: The x-axis shows years from 1990 to 2007, with labels at 45-degree
  angle
- FACT: The x-axis is truncated at the right page boundary (data table
  confirms range should extend to 2020)
- FACT: Forest land (teal/cyan) is the dominant area series, occupying most
  of the chart's negative region
- FACT: Cropland (dark navy blue) is a thin positive band extending above
  the 0 line
- FACT: A red line is visible running through the chart at approximately
  -230 to -380 over the visible time range
- FACT: The legend shows 5 entries with colored squares; at least 2 more
  entries are truncated at the right edge
- FACT: The legend identifies: Forest land, Cropland, Grassland, Wetlands,
  and a fifth entry beginning with "S" (truncated)
- FACT: No data labels appear on the chart
- FACT: The source is "EEA, republished by Eurostat (online data code:
  env_air_gge)"
- FACT: The overall chart value is in negative territory (net carbon sink)
  throughout the visible period
- FACT: The Cropland band is the only series with values above 0 (net source)

### Hallucination Risks [-> Correctness]

- RISK: Stating the x-axis extends to 2020
  REALITY: Only 1990-2007 are visible in the crop; the right portion
  (2008-2020) is truncated by the LibreOffice page boundary
- RISK: Identifying all 7 series by name and describing their individual
  trends
  REALITY: Only Forest land and Cropland are clearly distinguishable as
  area bands. Grassland, Wetlands, Settlements, and Other land are either
  too thin to distinguish or fully truncated from the legend
- RISK: Stating the red line is the "LULUCF total" or "net emissions" line
  REALITY: The red line's identity is ambiguous from the chart alone. The
  legend shows Grassland with a red/salmon square, so this could be the
  Grassland area boundary. Without the truncated legend entries visible,
  the line identity cannot be confirmed from the crop alone
- RISK: Reading exact values for any series in any year
  REALITY: No data labels are present. All values are visual estimates from
  gridline positions. The thin area series are nearly indistinguishable
- RISK: Describing the full title text
  REALITY: The title is truncated. Only "Greenhouse gas emissions from
  LULUCF (Land use, land use c..." is visible. The full title can be
  inferred from the data table but is not visible in the chart title itself
- RISK: Describing series that are not visible (e.g., "Other land shows...")
  REALITY: Several series are too thin or their colors too similar to
  distinguish. Only Forest land (teal) and Cropland (dark blue) are clearly
  separable areas

### Detail Inventory [-> Information Recovery]

- Title text: "Greenhouse gas emissions from LULUCF (Land use, land use
  c..." (truncated, black, bold, sans-serif)
- Subtitle text: "(million tonnes of CO2 equivale..." (truncated)
- Y-axis labels: 100, 0, -100, -200, -300, -400, -500 (black text, no
  unit prefix)
- X-axis labels: 1990 through 2007 visible, rotated 45 degrees, black text
- 7 horizontal gray gridlines at each 100-unit increment
- Forest land area color: teal/cyan (#66CDAA approximate)
- Cropland area color: dark navy/royal blue (#003366 approximate)
- Grassland legend square: red/salmon (#FF6347 approximate)
- Wetlands legend square: light blue/cyan (#87CEEB approximate)
- Fifth legend entry ("S..."): appears to have a pink/magenta square
- Red line: runs from approximately (-230, 1990) to (-300, 2007), dipping
  to -360 around 2000-2001 and -380 around 2006
- Forest land top boundary: approximately +10 to +20 (stable, just above 0)
- Cropland top boundary: approximately +20 to +40 (thin band above Forest
  land)
- Source note appears twice: once in italics (chart element) and once with
  hyperlinked "env_air_gge"
- Data table header visible at bottom: "Greenhouse gas emissions from
  LULUCF, EU, 1990-2020 (million tonnes of CO2 equivalent)"
- Chart border: thin gray lines on left and top edges
- White background
- Right-side truncation: ~40% of time series missing (2008-2020), plus 2+
  legend entries and full title/subtitle text

### Domain Context [-> Retrieval Value]

This chart appears on the Fig19 sheet of the Eurostat "Climate change --
driving forces" statistical annex. It shows greenhouse gas emissions and
removals from LULUCF (Land Use, Land-Use Change and Forestry) for the EU
from 1990 to 2020.

LULUCF is the land sector of national GHG inventories, covering how land
management affects atmospheric carbon. The six subcategories are: Forest
land (typically the largest net carbon sink in the EU, absorbing CO2 through
tree growth), Cropland, Grassland, Wetlands, Settlements, and Other land.
Some categories are net sinks (negative values, removing CO2) while others
are net sources (positive values, releasing CO2).

In the crop, Forest land dominates as a massive negative area (carbon sink
of roughly 250-300 Mt CO2eq per year), while Cropland is the only visible
net source (small positive band above 0). The other categories are too thin
to distinguish visually.

The data table on the following pages (visible in the crop footer) confirms
the subcategory breakdown with detailed row items including drainage/
rewetting, unconverted land, and land conversion subcategories for each
main LULUCF type.

The significant right-side truncation (2008-2020 missing) is particularly
impactful because the EU's LULUCF sink has been declining in recent years
due to aging forests, increased harvesting, and natural disturbances -- a
trend that would be visible in the missing portion.

### Search Keywords [-> Retrieval Value]

LULUCF, land use land use change forestry, greenhouse gas emissions,
carbon sink, forest land, cropland, stacked area chart, EU emissions,
1990-2020, EEA, Eurostat, env_air_gge, CO2 equivalent, climate driving
forces, carbon removals, net sink

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A chart showing LULUCF emissions with several colored areas" -- no axis values, no series identification, no truncation note. Or: identifies all 7 series by name and describes individual trends when only Forest land and Cropland are clearly distinguishable as area bands. Or: states the red line is "LULUCF total" when its identity is ambiguous (legend shows Grassland with red square). Fabricating identities for indistinguishable thin layers triggers the hallucination cap. | Stacked area + line combo identified. Forest land (teal) as dominant sink correct. Cropland (dark blue) as only positive band correct. Y-axis -500 to 100 in 100-unit steps. X-axis 1990-2007 visible. Red line noted with approximate range. Right-side truncation acknowledged (2008-2020 missing). May misidentify the red line or over-describe thin indistinguishable layers. | All verifiable facts exact: title and subtitle (both truncated at right), y-axis -500 to 100 in 100-unit steps, x-axis 1990-2007 at 45 degrees. Forest land (teal) fills ~-280 to +15, Cropland (dark blue) thin band ~+20-40 (only net source). Red line fluctuates -230 to -380 with dips at 2000-01 and 2006 -- identity noted as ambiguous (Grassland boundary or total line). 5 of 7 legend entries visible. Remaining thin layers correctly described as indistinguishable at this scale. No fabricated series identities or values. |
| Information Recovery | Identifies as an area chart with forest data. No axis ranges, no series beyond Forest land, no line description, no truncation details. A search for "LULUCF carbon sink" or "Cropland net source" would not match. The combo chart structure and 40% temporal truncation are invisible to the system. | Forest land and Cropland identified with approximate values. Red line documented. Y-axis range and x-axis range present. Legend partial visibility noted. "LULUCF stacked area" would match. May miss the data table at bottom, the source appearing twice, or the ambiguity of the red line identity. | Complete recovery: title text (truncated), subtitle (truncated), y-axis -500 to 100 with gridlines, x-axis 1990-2007 (2008-2020 truncated), Forest land area boundaries, Cropland band, red line with fluctuation points, 5 of 7 legend entries (Forest land, Cropland, Grassland, Wetlands, "S..."), 2 truncated entries, source note appearing twice (italic + hyperlinked), data table visible at bottom of crop, chart border, right-side truncation documented (~40% of time series missing). Any chart element visible in the crop is findable -- parity principle met. |
| Retrieval Value | "An environmental chart" -- no domain vocabulary, not self-contained. Would not surface for "LULUCF carbon sink" or "forest land emissions." Cannot understand what LULUCF is or why negative values represent carbon absorption. | "LULUCF emissions chart from Eurostat showing EU forest land as major carbon sink, 1990-2007 visible." Contains searchable terms but doesn't explain the LULUCF framework or why the truncation matters analytically. Partially self-contained. | Natural prose identifying Fig19 from Eurostat climate change driving forces annex. Explains LULUCF (Land Use, Land-Use Change and Forestry) GHG balance: Forest land as ~250-300 Mt CO2eq annual sink (negative values = carbon absorption), Cropland as only net source. Right truncation (2008-2020) analytically significant: hides recent EU sink decline from aging forests and increased harvesting. Data table below confirms 6 subcategories with land conversion breakdowns. Domain vocabulary embedded (LULUCF, carbon sink, net source, CO2 equivalent). Self-contained. Findable by "LULUCF forest sink" or "EU land use emissions." |

<br><br>

## doc28-C29 -- Pie: GHG by gas type in CO2-equivalents, EU

**Sheet:** Fig23
**Content type:** chart-simple
**Annotation difficulty:** Easy

### Visual Inventory [-> Information Recovery]

- **Chart type:** Pie chart with 4 slices and direct labels (no legend)
- **Title:** "Greenhouse gas emissions by gas type in CO..." (truncated at
  right page edge; from sheet tab: "Greenhouse gas emissions by gas type in
  CO2-equivalents, EU, 2020") -- wraps to two lines, bold, black, sans-serif
- **Sheet navigation label:** Yellow tab at top-left reads
  "<= Greenhouse gas emissions by gas type in CO2-equivalents, EU, 2020"
- **Slices (clockwise from 12 o'clock position):**
  1. Fluorinated gases (F gases) -- 2 %: very small slice at approximately
     1 o'clock, pink/light magenta color
  2. Carbon dioxide (CO2): dominant slice, approximately 80% of the pie,
     teal/dark cyan color. Label reads "Carbon" and is truncated at the right
     page edge (no percentage visible in the crop)
  3. Methane (CH4) -- 10 %: medium-small slice at approximately 8-10
     o'clock, magenta/dark pink color
  4. Nitrous oxide (N2O) -- 6 %: small slice at approximately 11 o'clock,
     light cyan/mint color
- **Label format:** Each slice has a callout label outside the pie with the
  gas name, chemical formula in parentheses, and percentage on a second line,
  except CO2 whose full label is truncated
- **Source note:** "Source: EEA, republished by Eurostat (online data code:
  env_air_gge)" in italics below the chart
- **Background:** White
- **No legend, no border around the pie, no 3D effects**

### Verifiable Facts [-> Correctness]

- FACT: The chart is a 2D pie chart with exactly 4 slices
- FACT: The title begins "Greenhouse gas emissions by gas type in CO..."
  and is truncated at the right edge
- FACT: The sheet navigation tab shows the full title:
  "Greenhouse gas emissions by gas type in CO2-equivalents, EU, 2020"
- FACT: The largest slice (CO2) is teal/dark cyan and occupies approximately
  80% of the pie
- FACT: The CO2 slice label reads only "Carbon" -- the rest is truncated at
  the right page boundary
- FACT: Methane (CH4) is labeled "10 %" and shown in magenta/dark pink
- FACT: Nitrous oxide (N2O) is labeled "6 %" and shown in light cyan/mint
- FACT: Fluorinated gases (F gases) is labeled "2 %" and shown in pink/light
  magenta
- FACT: The three labeled percentages (10% + 6% + 2% = 18%) imply the CO2
  slice is approximately 82% (or 80% with rounding)
- FACT: No legend is present -- labels are direct callouts from each slice
- FACT: The source is "EEA, republished by Eurostat (online data code:
  env_air_gge)"

### Hallucination Risks [-> Correctness]

- RISK: Stating the CO2 percentage as "80%" from the chart
  REALITY: The CO2 slice label is truncated and its percentage is not visible
  in the crop. The 80% can be inferred from the other slices (100% - 18% =
  82%) or from the data table on the same page, but it is not directly
  readable from the pie chart's labels
- RISK: Reading the CO2 label as "Carbon dioxide (CO2) 80 %"
  REALITY: Only "Carbon" is visible; the rest is cut off at the right edge
- RISK: Describing this as a chart with a legend
  REALITY: Labels are direct callouts from slices, not a separate legend
- RISK: Noting discrepancy with data table values (CH4: 10% vs 11%, F
  gases: 2% vs 3%)
  REALITY: The pie chart labels (10%, 6%, 2%) differ slightly from the data
  table's 2020 column (11%, 6%, 3%). This is likely a rounding difference
  in how the chart and table were generated. Both are present on the same
  page. Describing only what the pie chart shows is correct.
- RISK: Describing the Nitrous oxide slice as "dark blue" or similar
  REALITY: The N2O slice is a lighter shade of cyan/mint, distinct from the
  darker teal of the CO2 slice

### Detail Inventory [-> Information Recovery]

- Chart title: "Greenhouse gas emissions by gas type in CO..." (truncated,
  bold, black, centered, wraps to 2 lines)
- Sheet tab: yellow rounded rectangle, "<=" arrow prefix, full title text
  in small font
- CO2 slice: teal/dark cyan (#009688 approximate), ~80% of pie, label
  reads "Carbon" (truncated)
- CH4 slice: magenta/dark pink (#CC3366 approximate), labeled "Methane
  (CH4)" on line 1, "10 %" on line 2
- N2O slice: light cyan/mint (#B2DFDB approximate), labeled "Nitrous oxide
  (N2O)" on line 1, "6 %" on line 2
- F gases slice: pink/light magenta (#E8A0BF approximate), labeled
  "Fluorinated gases (F gases)" on line 1, "2 %" on line 2
- Label text: black, sans-serif, positioned as callouts outside the pie
  perimeter
- Pie orientation: CO2 slice spans roughly from 3 o'clock to 11 o'clock
  (most of the circle)
- Source note: italic text, "Source:" prefix, mentions "online data code:
  env_air_gge"
- White background, no gridlines, no axis, no border
- Right-side truncation: CO2 label and title text cut off

### Domain Context [-> Retrieval Value]

This chart appears on the Fig23 sheet of the Eurostat "Climate change --
driving forces" statistical annex. It shows the breakdown of EU greenhouse
gas emissions by gas type in CO2-equivalents for 2020.

The four greenhouse gas categories in the UNFCCC reporting framework are:
- Carbon dioxide (CO2): dominant GHG, primarily from fossil fuel combustion
  and industrial processes
- Methane (CH4): from agriculture (livestock, rice), waste management, and
  energy production
- Nitrous oxide (N2O): from agriculture (fertilizers), industrial processes,
  and combustion
- Fluorinated gases (F gases): synthetic gases from refrigeration, air
  conditioning, electronics manufacturing

CO2 dominance at ~80% is consistent with EU emissions profiles. The data
table on the same page shows that the composition has been remarkably stable
between 1990 and 2020 (CO2: 80% both years; CH4 decreased from 12% to 11%;
N2O from 7% to 6%; F gases increased from 1% to 3%).

The note in the data table states: "Including international aviation and
indirect CO2, excluding LULUCF and memo items."

### Search Keywords [-> Retrieval Value]

greenhouse gas emissions, gas type, CO2 equivalents, pie chart, carbon
dioxide, methane, nitrous oxide, fluorinated gases, F gases, EU emissions,
2020, EEA, Eurostat, env_air_gge, UNFCCC, GHG composition, climate
driving forces

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A pie chart showing different greenhouse gases" -- no percentages, no gas names, no year. Or: reads the CO2 label as "Carbon dioxide (CO2) 80%" when only "Carbon" is visible (rest truncated at right edge). Stating the CO2 percentage as a chart-labeled value when it is only inferable from the other three (100% - 18% = 82%) triggers the hallucination cap. | 4 slices identified with correct gas names and readable percentages: CH4 10%, N2O 6%, F gases 2%. CO2 correctly noted as ~80% (inferred, label truncated). Title truncation acknowledged. Direct callout labeling format correct. May miss the sheet navigation tab or the 2-line label format. | All verifiable facts exact: 4 slices with correct names, formulas, and percentages (CH4 10%, N2O 6%, F gases 2%). CO2 percentage correctly stated as inferred (~82% from arithmetic, ~80% visual estimate) -- not read from a label. CO2 label truncated to "Carbon" at right edge. Title truncated. Sheet tab provides full title. Direct 2-line callout labels (name+formula, then percentage). No legend. No fabricated CO2 percentage as "labeled." |
| Information Recovery | Identifies as a pie chart with CO2 as largest gas. No specific percentages, no chemical formulas, no label format details. A search for "CH4 10%" or "F gases 2%" would not match. Three of four gas types invisible to the system. | All 4 gases named with percentages. CO2 dominance noted. Title text and source present. "GHG by gas type" would match. May miss the 2-line label format, the sheet navigation tab, or the CO2 label truncation detail. | Complete recovery: all 4 slices with gas names, chemical formulas (CH4, N2O), percentages, and colors. CO2 label truncation documented ("Carbon" visible only). Title text (truncated) and sheet tab (full title). 2-line callout label format. Source/data code env_air_gge. White background, 2D, no legend/border. Right-side truncation affects CO2 label and title. Any gas visible in the chart is findable -- parity principle met. |
| Retrieval Value | "A greenhouse gas chart" -- no domain vocabulary, not self-contained. Would not surface for "GHG composition by gas" or "CO2 dominance EU." Cannot understand what CO2-equivalents means or why F gases are separately tracked. | "EU GHG composition 2020: CO2 ~80%, CH4 10%, N2O 6%, F gases 2%. Data from EEA/Eurostat." Contains searchable terms but doesn't explain the UNFCCC gas categories or emission sources. Partially self-contained. | Natural prose identifying Fig23 from Eurostat climate change driving forces annex. EU GHG by gas type in CO2-equivalents, 2020. CO2 ~80% (fossil fuel combustion, industrial processes), CH4 10% (agriculture, waste), N2O 6% (fertilizers, industrial), F gases 2% (refrigeration, electronics manufacturing). Composition stable since 1990. Excludes LULUCF. UNFCCC reporting framework contextualized. Domain vocabulary embedded. Self-contained. Findable by "GHG composition by gas type" or "EU greenhouse gas breakdown." |

# Image Analysis: Doc 22 -- 22_nasa_global_warming.html

**Document:** `22_nasa_global_warming.html`
**Format:** HTML
**Source:** https://science.nasa.gov/earth/climate-change/global-warming/
**Category:** multi-image
**Images:** 20
**Document context:** NASA Earth Science climate change article covering
global warming evidence, causes, effects, and scientific consensus. 20
content images including temperature anomaly charts, greenhouse gas trend
graphs, ice core reconstructions, satellite imagery, and climate
photography.

**Eval subset:** 6 of 20 content images

<br><br>

## doc22-R01 -- GISS temperature anomaly

**Content type:** chart-complex
**Annotation difficulty:** Medium

### Visual Inventory

Line chart titled "Global Mean Surface Temperature" showing temperature anomaly
trends from 1880 to approximately 2005. Two data series plotted: a thin light
red line (annual mean) and a thick dark red line (5-year running mean). A legend
in the upper-left area lists both series plus an uncertainty indicator. Several
I-shaped vertical error bars (uncertainty markers) appear at irregular intervals
along the time series. The y-axis shows "Temperature Anomaly (C)" ranging from
-0.4 to 0.6 with horizontal gridlines at 0.2 increments. The x-axis shows
"Year" with tick marks at 1880, 1900, 1920, 1940, 1960, 1980, and 2000. White
background with light gray gridlines.

### Verifiable Facts

- Title: "Global Mean Surface Temperature"
- Y-axis label: "Temperature Anomaly (C)" (degree symbol present)
- Y-axis range: -0.4 to 0.6, gridlines at each 0.2 increment
- X-axis label: "Year"
- X-axis range: 1880 to approximately 2005, tick marks at every 20 years
- Legend entries: "annual mean" (thin light red line), "5-year running mean"
  (thick dark red line), "uncertainty" (I-shaped error bar symbol)
- Lowest values: approximately -0.4 around 1905-1910
- Highest value: approximately 0.6 at the right end (circa 2005)
- The 5-year running mean crosses 0.0 upward around 1935-1940, dips back near 0
  around 1950-1960, then remains above 0 permanently after approximately 1975
- A mid-century dip occurs between roughly 1940 and 1965 where the running mean
  briefly returns toward 0 after an initial rise
- Steep upward trend from approximately 1975 to 2005
- Approximately 6 vertical uncertainty (error) bars visible at irregular
  intervals (roughly at 1890, 1900, 1940, 1950, 1960, 2000)
- Error bars are I-shaped: vertical line with small horizontal caps at top and
  bottom
- Annual mean line shows high inter-year variability (jagged peaks and valleys)
  while the running mean is smoother

### Hallucination Risks

- **Exact temperature values:** The y-axis gridlines are at 0.2 intervals, so
  reading values to 0.01 precision would be fabrication. Values between
  gridlines (e.g., "0.15" or "0.35") are approximate visual estimates, not
  labeled data points.
- **End year:** The x-axis extends to roughly 2005 but the exact final year is
  ambiguous -- an annotator might claim "2010" or "present" without justification
  from the crop.
- **Baseline period:** The baseline (1951-1980) is mentioned in the HTML caption
  but is NOT visible anywhere in the chart image itself. An annotator might state
  the baseline as if it were labeled in the chart.
- **Number of uncertainty bars:** The exact count depends on whether closely
  spaced bars near 2000 are one or two. An annotator might state a precise count
  that differs slightly.
- **Color description:** The two lines are both red-family colors (light vs dark
  red). An annotator might describe them as "orange and red" or "pink and red"
  -- the distinction is subtle.
- **Gridline interpretation:** Minor gridlines between the 0.2 labeled gridlines
  are not clearly present. An annotator might invent minor gridlines at 0.1
  intervals.

### Detail Inventory

- **Line rendering:** Annual mean is thin (~1px weight), light red/salmon color;
  5-year running mean is thick (~3px weight), darker red/crimson color
- **Legend placement:** Upper-left corner, inside the plot area, with a subtle
  background; three rows: "annual mean" with thin line swatch, "5-year running
  mean" with thick line swatch, "uncertainty" with I-bar symbol
- **Error bar style:** Thin black I-bars (vertical line with horizontal serif
  caps); placed at approximately 1885-1890, 1900, 1940, 1950, 1960, and 2000
- **Gridlines:** Light gray horizontal lines at -0.4, -0.2, 0, 0.2, 0.4, 0.6;
  no vertical gridlines
- **Axis tick marks:** Small outward-facing ticks on both axes
- **Notable data patterns:**
  - Early cool period (1880-1910): anomalies mostly between -0.2 and -0.4
  - First warming (1910-1940): rise from about -0.3 to about 0.1
  - Mid-century plateau/dip (1940-1975): fluctuation near 0
  - Rapid warming (1975-2005): steep rise from about 0.0 to about 0.6
- **Font:** Sans-serif for all text (title, axis labels, legend, tick labels)
- **Background:** Pure white, no border around the plot area

### Domain Context

- Source: NASA Goddard Institute for Space Studies (GISS) Surface Temperature
  Analysis dataset
- The chart appears in NASA's "What is Global Warming?" article section, after
  defining global warming as "the unusually rapid increase in Earth's average
  surface temperature over the past century"
- HTML caption: "Despite ups and downs from year to year, global average surface
  temperature is rising. By the beginning of the 21st century, Earth's
  temperature was roughly 0.5 degrees Celsius above the long-term (1951-1980)
  average."
- Credit: "NASA figure adapted from Goddard Institute for Space Studies Surface
  Temperature Analysis"
- Temperature anomaly is relative to the 1951-1980 baseline average (stated in
  caption, not in chart)
- GISS is one of the primary global temperature datasets alongside HadCRUT
  (UK Met Office) and NOAA GlobalTemp

### Search Keywords

GISS, global mean surface temperature, temperature anomaly, global warming,
NASA, Goddard Institute for Space Studies, annual mean, 5-year running mean,
1880-2005, climate change, surface temperature trend, uncertainty bars,
baseline 1951-1980

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A line chart showing temperature over time" (no axis values or series names) | "Global Mean Surface Temperature chart with annual mean and 5-year running mean from 1880 to about 2005; anomaly ranges from -0.4 to 0.6 C" (key facts correct) | All axis labels and ranges exact, both series named with visual descriptions (thin light red vs thick dark red), uncertainty bars noted with approximate positions, mid-century dip and post-1975 acceleration described, end value approximately 0.6 |
| Specificity | "Red line going up" (minimal detail) | "Two red lines: thin jagged annual data and thicker smooth running mean; temperature rises steeply after 1975 to about 0.5 C" (reads key features) | Thin vs thick line weights, light red vs dark red colors, I-shaped error bars at ~6 positions, gridline spacing at 0.2 intervals, 20-year x-axis tick spacing, early cool period 1880-1910, warming 1910-1940, mid-century plateau, rapid rise 1975-2005, legend placement in upper-left |
| Completeness | Mentions the upward trend but omits axes, legend, error bars | Both data series described, axis labels and ranges stated, legend noted, upward trend after 1975 highlighted | Title, both axis labels with units and ranges, legend with all 3 entries, error bar count and style, gridline pattern, data pattern in 4 phases (early cool, first warming, plateau, rapid rise), font style, white background, no vertical gridlines |
| Usefulness | "A temperature chart from NASA" (no context) | "GISS surface temperature anomaly showing global warming trend; temperature roughly 0.5 C above 1951-1980 baseline by 2005" | Identifies GISS dataset source, explains anomaly baseline (1951-1980), connects to NASA Earth Observatory global warming article, notes the chart illustrates the "unusually rapid" warming described in the text, mentions GISS as one of the primary global temperature datasets |

<br><br>

## doc22-R03 -- EPICA 800,000-year temperature reconstruction

**Content type:** chart-complex
**Annotation difficulty:** Hard

### Visual Inventory

Line chart showing temperature anomaly over the past 800,000 years based on
EPICA ice core data. A single dark olive/yellow-green line traces the
temperature record with lighter olive/gray scatter points behind it
representing the raw or higher-resolution data. The y-axis shows "Temperature
Anomaly (C)" ranging from approximately -8 to +4. The x-axis shows "Year"
ranging from -800,000 to 0. The chart displays a pronounced sawtooth pattern:
gradual cooling into ice ages (deep troughs reaching -8 to -9) followed by
rapid warming into interglacial periods (sharp peaks reaching +2 to +4). White
background with no gridlines. No legend present.

### Verifiable Facts

- Y-axis label: "Temperature Anomaly (C)" (degree symbol present)
- Y-axis range: approximately -8 to +4 (labeled tick marks at -8, -4, 0, 4)
- X-axis label: "Year"
- X-axis range: -800,000 to 0 (labeled tick marks at -800,000, -600,000,
  -400,000, -200,000, 0)
- Single data series: dark olive/yellow-green line with lighter scatter points
  behind it
- No explicit legend
- Approximately 8 major glacial-interglacial cycles visible over the 800,000-
  year span
- Ice age troughs (deepest cold periods) reach approximately -8 to -9 C anomaly
- Interglacial peaks reach approximately +2 to +4 C anomaly
- The most recent interglacial peak (near year 0) reaches approximately +2 to
  +3 C
- The highest peak appears around -400,000 years, reaching approximately +4 C
- The sawtooth pattern shows gradual cooling descents (taking tens of thousands
  of years) followed by rapid warming ascents (taking roughly 5,000-10,000
  years)
- The data begins at approximately -800,000 years with a cold period (anomaly
  around -6 to -7)
- The line at the right end (year 0) terminates at a warm interglacial value

### Hallucination Risks

- **CO2 data:** The catalog description mentions "temperature + CO2
  reconstruction" but the crop shows ONLY temperature anomaly on the y-axis.
  There is no second axis, no CO2 data series, and no CO2 labels anywhere in
  the chart image. An annotator might describe CO2 data that is not present,
  influenced by the caption or general knowledge about EPICA data.
- **Exact cycle count:** Counting the glacial-interglacial cycles is ambiguous
  because some cycles have multiple sub-peaks. An annotator might state a
  precise count (e.g., "exactly 8 cycles") when the visual evidence supports
  different counts depending on counting criteria.
- **Peak temperature values:** The y-axis gridlines are spaced 4 degrees apart
  (-8, -4, 0, 4). Reading specific peak heights to 0.1-degree precision would
  be fabrication. Most peaks and troughs fall between labeled gridlines.
- **Temporal precision:** The x-axis covers 800,000 years with labels every
  200,000 years. Placing specific events to within 1,000-year precision is not
  supported by the chart resolution.
- **Data series interpretation:** The lighter scatter behind the main line could
  be interpreted as "raw data" or "uncertainty bounds." The chart does not label
  which it is. An annotator might assert one interpretation as fact.
- **Present-day reference:** The rightmost data point (year 0) represents
  pre-industrial or ice-core-record end, NOT present-day temperature. An
  annotator might conflate this with current warming.

### Detail Inventory

- **Line rendering:** Solid dark olive/yellow-green line (~2px weight) tracing
  the main time series
- **Background data:** Lighter olive-gray scatter points or translucent data
  markers visible behind the main line throughout the full time span, giving
  a sense of data density and variability
- **Axis styling:** Sans-serif font for all labels and tick values; outward-
  facing tick marks; no gridlines (neither horizontal nor vertical)
- **Background:** White/very light gray
- **Y-axis tick marks:** Labeled at -8, -4, 0, 4 (4-degree increments)
- **X-axis tick marks:** Labeled at -800,000, -600,000, -400,000, -200,000, 0
  (200,000-year increments) using comma-separated number format
- **Sawtooth pattern details (left to right):**
  - ~-800,000 to -720,000: cold period then rise to first interglacial peak
  - ~-720,000 to -620,000: cycle through trough and peak
  - ~-620,000 to -530,000: deep cold trough (~-8) then peak
  - ~-530,000 to -420,000: cold trough then tallest peak (reaching ~+4)
  - ~-420,000 to -330,000: gradual descent then rise
  - ~-330,000 to -240,000: moderate peak then descent
  - ~-240,000 to -130,000: cold trough then sharp rise to high peak (~+3)
  - ~-130,000 to 0: descent into last ice age (~-8 at ~-20,000) then rapid rise
    to present interglacial (~+2)
- **Comma formatting:** Negative year values use comma separators (e.g.,
  "-800,000")
- **No title:** Unlike R01, this chart has no title text above the plot area

### Domain Context

- Source: EPICA (European Project for Ice Cores in Antarctica) Dome C ice core
- Data from Jouzel et al., 2007 (as credited in the HTML caption)
- HTML caption: "Glacial ice and air bubbles trapped in it (top) preserve an
  800,000-year record of temperature & carbon dioxide. Earth has cycled between
  ice ages (low points, large negative anomalies) and warm interglacials
  (peaks)."
- Credit: "Photograph courtesy National Snow & Ice Data Center. NASA graph by
  Robert Simmon, based on data from Jouzel et al., 2007."
- The "(top)" reference in the caption refers to a separate photo of an ice core
  section that appears immediately above this chart on the NASA page
- This chart appears in the "How is Today's Warming Different from the Past?"
  section of the NASA global warming article
- The accompanying text notes: "As the Earth moved out of ice ages over the past
  million years, the global temperature rose a total of 4 to 7 degrees Celsius
  over about 5,000 years"
- Temperature anomaly baseline is not stated in the chart; EPICA data typically
  uses a pre-industrial or long-term average baseline
- The ~100,000-year periodicity of the glacial cycles is driven by Milankovitch
  orbital cycles (obliquity, eccentricity, precession)

### Search Keywords

EPICA, ice core, 800000-year, temperature anomaly, paleoclimate,
glacial-interglacial cycles, ice ages, interglacial, sawtooth pattern,
Dome C, Antarctica, Jouzel, Milankovitch cycles, NASA, Robert Simmon,
climate history, proxy record

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A chart showing temperature changes over a long time" (no axis values, no time scale) | "800,000-year temperature anomaly chart from -8 to +4 C showing glacial-interglacial cycles; data is olive-colored line on white background" (key ranges correct) | Correct axis ranges and labels, notes approximately 8 major cycles, identifies the tallest peak around -400,000 years at ~+4 C, describes sawtooth asymmetry (gradual cooling, rapid warming), correctly states no CO2 data in the chart image despite the caption's mention, notes scatter data behind the main line |
| Specificity | "Squiggly green line going up and down" (minimal) | "Olive/green line oscillating between ice age troughs near -8 C and interglacial peaks near +2-4 C; x-axis from -800,000 to 0 with 200,000-year tick spacing" (reads axes) | Dark olive vs lighter scatter point distinction, tick mark values (-8, -4, 0, 4 on y-axis; -800,000 through 0 on x-axis), comma-separated number format, no gridlines, no title, sans-serif font, approximate peak/trough positions for each cycle, highest peak identification at ~-400,000 |
| Completeness | Mentions oscillating temperature but omits axis labels, time range, or anomaly values | Both axes labeled with ranges, data series described, cyclic pattern noted, approximate number of cycles stated | All axis labels with units and tick values, data series rendering (line + scatter), all major cycle peaks and troughs roughly positioned, sawtooth asymmetry, no legend noted, no title noted, no gridlines noted, background scatter/uncertainty data noted, comma formatting in axis labels |
| Usefulness | "An old climate chart" (no source context) | "EPICA ice core temperature record showing Earth's glacial-interglacial cycles over 800,000 years; from NASA's global warming article" | Identifies EPICA Dome C source and Jouzel et al. 2007 data, explains context in NASA article's "How is Today's Warming Different?" section, connects to Milankovitch orbital cycles, notes that rate of modern warming (~0.7 C per century) far exceeds ice-age recovery rates (~1 C per 1,000 years), clarifies that CO2 data is absent from the chart despite the catalog suggesting otherwise |

<br><br>

## doc22-R05 -- Anthropogenic vs natural climate attribution

**Content type:** chart-complex
**Annotation difficulty:** Hard

### Visual Inventory

Four vertically stacked sub-plots sharing a common x-axis (approximately 1890
to 2005), each showing the estimated temperature change contribution from a
different climate forcing factor. The top three panels use olive/dark
yellow-green lines and identical y-axis ranges (-0.2 to 0.2 C). The bottom
panel uses a red line and an expanded y-axis range (-0.2 to 0.6 C). All four
panels have "Temperature Change (C)" as their y-axis label. Each panel has a
bold title above it identifying the forcing factor. A thin black horizontal
reference line at 0 is present in each panel.

- **Panel 1 (top) -- "El Nino/Southern Oscillation":** High-frequency
  oscillating olive line varying rapidly between roughly -0.2 and +0.2 C.
  No discernible long-term trend; variability is approximately symmetric
  around zero.
- **Panel 2 -- "Total Solar Irradiance":** Olive line with much smaller
  amplitude than Panel 1. Oscillations stay very close to zero, roughly
  between -0.05 and +0.05 C. Small cyclical variations visible (likely
  ~11-year solar cycle) but negligible magnitude compared to other factors.
- **Panel 3 -- "Volcanic Aerosols":** Olive line mostly at zero with sharp
  negative spikes (cooling events). Several distinct downward excursions
  visible. The deepest spike reaches approximately -0.2 to -0.3 C around
  1991-1992. Other notable spikes appear around 1902, 1963, and 1982.
  Between eruptions the line returns to approximately zero.
- **Panel 4 (bottom) -- "Human-caused Forcings" with subtitle "(greenhouse
  gases, albedo, aerosols)":** Red line (distinctly different color from the
  other three panels). Stays near -0.1 to -0.2 C from 1890 to approximately
  1960, then rises steeply from about 0 in 1970 to approximately 0.6 C by
  2005. The y-axis extends higher (to 0.6) to accommodate this larger signal.

### Verifiable Facts

- 4 sub-plots stacked vertically, sharing x-axis range (~1890 to ~2005)
- X-axis tick marks at 1900, 1920, 1940, 1960, 1980, 2000 (20-year intervals)
- X-axis label not explicitly visible but implied by year tick labels
- All four panels have "Temperature Change (C)" as y-axis label (degree symbol)
- Top 3 panels: y-axis range -0.2 to 0.2 with tick marks at -0.2, 0, 0.2
- Bottom panel: y-axis range -0.2 to 0.6 with tick marks at -0.2, 0, 0.2,
  0.4, 0.6
- Panel titles (top to bottom): "El Nino/Southern Oscillation", "Total Solar
  Irradiance", "Volcanic Aerosols", "Human-caused Forcings"
- Bottom panel subtitle in regular weight: "(greenhouse gases, albedo, aerosols)"
- Top 3 panels use olive/dark yellow-green line color
- Bottom panel uses red line color
- Each panel has a horizontal zero-reference line
- The human-caused forcing signal (~0.6 C by 2005) is approximately 3x larger
  than the maximum amplitude of any individual natural forcing factor (~0.2 C)
- The volcanic aerosols panel shows the deepest spike around 1991 (consistent
  with Mount Pinatubo eruption)

### Hallucination Risks

- **Attributing specific eruptions:** The volcanic spikes are visible but not
  labeled with eruption names. An annotator might name specific volcanoes
  (Santa Maria 1902, Agung 1963, El Chichon 1982, Pinatubo 1991) based on
  general knowledge, but these labels are not in the image.
- **Solar cycle period:** The TSI oscillations suggest an ~11-year cycle but
  the chart resolution makes precise period measurement impossible. An
  annotator might state "11-year solar cycle clearly visible" when the
  oscillations are barely distinguishable from noise.
- **Exact human forcing onset:** The transition from flat to rising in the
  bottom panel is gradual. An annotator might state a precise onset year
  (e.g., "1960" or "1970") when the actual transition is spread over decades.
- **ENSO event identification:** The ENSO panel shows spikes but they are not
  labeled. An annotator might identify specific El Nino years (1997-98, 1982-83)
  from peak positions, but these are inferences, not labeled data.
- **Combined/total temperature curve:** The chart shows individual forcings
  separately but does not show their sum. An annotator might describe a combined
  effect or total that is not visually present.
- **Panel y-axis difference:** The bottom panel's different y-axis range (up to
  0.6 vs 0.2) is a critical detail. An annotator who misses this might
  incorrectly compare magnitudes across panels at face value (e.g., claiming
  the ENSO signal is "similar in size" to the human forcing signal because the
  lines appear similar height on screen).

### Detail Inventory

- **Panel layout:** Vertically stacked with small vertical gaps between panels;
  each panel shares the same x-axis timeline but has independent y-axis scaling
- **Line styles:**
  - Panels 1-3: olive/dark yellow-green, approximately 1-2px weight, solid
  - Panel 4: red/crimson, approximately 1-2px weight, solid
- **Panel titles:** Bold sans-serif text, positioned above each sub-plot;
  bottom panel has bold "Human-caused Forcings" followed by regular-weight
  "(greenhouse gases, albedo, aerosols)"
- **Zero line:** Thin black horizontal line at y=0 in each panel
- **No legend in any panel** -- each panel shows a single data series
- **No gridlines** beyond the zero reference line
- **Background:** White
- **ENSO panel detail:** Roughly 5-6 oscillations per decade, with largest
  positive spikes reaching ~0.15-0.2 and negative excursions to ~-0.15-0.2
- **TSI panel detail:** Very low amplitude oscillations barely distinguishable
  from the zero line; slight positive peaks at approximately 11-year intervals
- **Volcanic panel detail:** Distinct negative spikes at approximately 1902
  (moderate), 1963 (moderate-deep), 1982 (deep), and 1991 (deepest at ~-0.25);
  between events the line hovers at 0 or very slightly below
- **Human forcing panel detail:** Approximately flat or slightly negative from
  1890 to ~1940; gradual rise from ~1940 to ~1970; steep acceleration from
  ~1970 to 2005 reaching ~0.6; the curve is smooth (no high-frequency
  variability like the ENSO panel)

### Domain Context

- HTML caption: "Although Earth's temperature fluctuates naturally, human
  influence on climate has eclipsed the magnitude of natural temperature changes
  over the past 120 years. Natural influences on temperature -- El Nino, solar
  variability, and volcanic aerosols -- have varied approximately plus and minus
  0.2 C (0.4 F), (averaging to about zero), while human influences have
  contributed roughly 0.8 C (1 F) of warming since 1889."
- Credit: "Graphs adapted from Lean et al., 2008"
- This chart appears in the "Is Current Warming Natural?" section of the NASA
  global warming article
- The chart is a key piece of the attribution argument: natural forcings
  oscillate around zero with no long-term trend, while human forcings show a
  clear upward trend, demonstrating that observed warming cannot be explained
  by natural factors alone
- Lean et al. (2008) is a widely cited climate attribution study that
  decomposes observed temperature change into natural and anthropogenic
  components
- The different y-axis scale for the bottom panel visually emphasizes that
  human forcing is much larger in magnitude than any individual natural factor

### Search Keywords

climate attribution, anthropogenic forcing, natural forcing, El Nino, ENSO,
total solar irradiance, volcanic aerosols, greenhouse gases, human-caused
warming, temperature change, Lean et al., NASA, multi-panel comparison,
climate factors, radiative forcing, Pinatubo, solar cycle

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Four charts showing different climate factors" (no values, no color distinction) | "4-panel chart: ENSO, solar, volcanic (olive lines, +/-0.2 C range), and human forcings (red line, rising to ~0.6 C); all from ~1890 to ~2005" (panel names and key distinction correct) | All 4 panel titles exact (including "Human-caused Forcings (greenhouse gases, albedo, aerosols)"), correct y-axis ranges for top 3 vs bottom panel, volcanic spike timing (~1902, ~1963, ~1982, ~1991), human forcing flat-then-rising shape, color distinction (olive vs red) noted with visual significance |
| Specificity | "Lines going up and down in four boxes" (generic) | "ENSO has rapid oscillations, solar is near-zero, volcanic has downward spikes, human forcing rises steeply after 1970; deepest volcanic spike around 1991" (main patterns identified) | Line color and weight per panel, y-axis tick values (-0.2/0/0.2 vs -0.2/0/0.2/0.4/0.6), zero reference lines, approximate volcanic spike positions and depths, human forcing curve shape (flat to ~1940, gradual to ~1970, steep to 2005), ENSO oscillation frequency (~5-6 per decade), TSI amplitude barely distinguishable from zero |
| Completeness | Describes 2 of 4 panels, misses the y-axis range difference | All 4 panels described with titles, key patterns, and the critical y-axis range difference between top 3 and bottom panel | All 4 panel titles with subtitle text, both y-axis ranges, x-axis range and tick spacing, zero reference lines, line colors per panel, no legend/no gridlines noted, all major volcanic spike positions, ENSO symmetry around zero, TSI negligible amplitude, human forcing curve inflection points, white background |
| Usefulness | "Climate charts from NASA" (no attribution context) | "Shows natural climate factors (ENSO, solar, volcanic) are small and oscillate around zero, while human forcing has risen to 0.6 C -- demonstrates humans are the dominant cause" | Identifies as Lean et al. 2008 attribution analysis, explains the chart's role in the "Is Current Warming Natural?" section, notes that different y-axis scales visually emphasize the magnitude difference, connects volcanic spikes to known eruptions (though unlabeled), explains why this decomposition is central to the attribution argument |

<br><br>

## doc22-R09 -- Anthropogenic CO2 in ocean water (global map)

**Content type:** chart-simple
**Annotation difficulty:** Easy

### Visual Inventory

Global map in an elliptical (Mollweide-like) projection showing the total
amount of anthropogenic CO2 dissolved in ocean water from surface to sea floor.
Continents are rendered in gray. Ocean areas are colored on a gradient from dark
navy blue (low CO2) through medium blue, teal/cyan, to yellow/cream (high CO2).
A horizontal color bar at the bottom center reads "Anthropogenic CO2 (mol/m2)"
with tick marks at 0, 50, and 100. White background around the map edges.

### Verifiable Facts

- Map projection: elliptical (Mollweide or similar equal-area)
- Color bar label: "Anthropogenic CO2 (mol/m2)" with superscript 2
- Color bar range: 0 to 100, with labeled tick marks at 0, 50, and 100
- Color gradient: dark navy blue (0) through medium blue, teal/cyan, to
  yellow/cream (100)
- Continents: solid gray, no country borders
- Highest CO2 concentrations (yellow/cream): North Atlantic Ocean, particularly
  between North America and Europe/Greenland
- Moderate-high concentrations (teal/cyan): Southern Ocean around Antarctica,
  parts of the North Pacific
- Low concentrations (dark blue): tropical Pacific, Indian Ocean, equatorial
  Atlantic
- The North Atlantic shows the most intense yellow region, centered roughly
  between 30-60N latitude
- A secondary moderate-concentration region appears in the Southern Ocean
  (roughly 40-60S latitude)
- The central tropical Pacific is among the darkest (lowest CO2) areas
- Continents visible include: North America, South America, Africa, Europe,
  Asia, Australia, Antarctica (partial, at bottom edge)
- No latitude/longitude grid lines or labels
- No title text above the map (title information is in the color bar only)

### Hallucination Risks

- **"Ocean carbon cycle":** The catalog describes this as a "carbon cycle
  diagram" but it is a concentration map, not a process/cycle diagram. An
  annotator influenced by the catalog might describe carbon flux arrows,
  uptake/release processes, or cycle components that are not present.
- **Specific concentration values:** The color bar allows rough estimation but
  not precise readings. An annotator might state exact mol/m2 values for
  specific ocean regions when only approximate color matching is possible.
- **Geographic labels:** No countries, oceans, or geographic features are
  labeled. An annotator must identify regions by continental outlines, which
  could lead to errors (e.g., confusing the Bay of Bengal with the Arabian Sea).
- **Temporal coverage:** The map represents a cumulative total (not a single
  year), but this is not stated in the image. An annotator might attribute it
  to a specific year or time period.
- **Depth integration:** The caption says "surface to sea floor" but this is
  not in the image. An annotator might describe it as surface-only or a
  specific depth layer.

### Detail Inventory

- **Color gradient specifics:**
  - 0 mol/m2: very dark navy/near-black blue
  - ~25 mol/m2: medium dark blue
  - ~50 mol/m2: medium blue transitioning to teal
  - ~75 mol/m2: teal/cyan/light green
  - ~100 mol/m2: yellow/cream
- **Geographic CO2 distribution:**
  - North Atlantic (yellow/cream): highest concentration area, spanning roughly
    from the US East Coast to Western Europe, extending into the Labrador Sea
    and Norwegian Sea
  - Southern Ocean (teal/cyan band): moderate concentration ring around
    Antarctica at roughly 40-60S
  - North Pacific (moderate blue-teal): intermediate values, higher in
    subpolar regions
  - Tropical oceans (dark blue): uniformly low across equatorial Pacific,
    Indian Ocean, and equatorial Atlantic
  - Arctic Ocean: appears as light teal/cyan where visible north of Eurasia
- **Continent rendering:** Uniform medium gray, smooth coastlines, no internal
  features (rivers, borders, topography)
- **Map border:** Elliptical edge with white exterior
- **Color bar:** Horizontal bar below the map, approximately 1/3 the map width,
  centered; gradient fills the bar from left (dark blue) to right (yellow);
  tick labels "0", "50", "100" below the bar

### Domain Context

- HTML caption: "About half the carbon dioxide emitted into the air from
  burning fossil fuels dissolves in the ocean. This map shows the total amount
  of human-made carbon dioxide in ocean water from the surface to the sea floor.
  Blue areas have low amounts, while yellow regions are rich in anthropogenic
  carbon dioxide. High amounts occur where currents carry the carbon-dioxide-
  rich surface water into the ocean depths."
- Credit: "Map adapted from Sabine et al., 2004"
- This map appears in the "How Will Global Warming Change Earth?" section of the
  NASA global warming article, in the context of discussing ocean impacts
- Sabine et al. (2004) published in Science is a landmark study estimating
  cumulative anthropogenic CO2 uptake by the global ocean
- The high concentrations in the North Atlantic correspond to deep water
  formation regions where surface water (enriched in atmospheric CO2) sinks to
  depth, carrying anthropogenic carbon with it
- The Southern Ocean band reflects the Antarctic Circumpolar Current and
  deep water formation around Antarctica
- The unit mol/m2 represents a column-integrated (depth-integrated) quantity --
  total moles of anthropogenic CO2 per square meter of ocean surface, summed
  through the entire water column

### Search Keywords

anthropogenic CO2, ocean carbon, global map, Sabine et al., dissolved carbon
dioxide, ocean uptake, North Atlantic, Southern Ocean, deep water formation,
mol per square meter, column-integrated, fossil fuel, ocean acidification,
NASA, climate change

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A blue and yellow map of the ocean" (no variable identified) | "Global map of anthropogenic CO2 in oceans, 0-100 mol/m2; North Atlantic has highest values (yellow), tropical Pacific is lowest (dark blue)" (key variable and patterns correct) | Correct variable name and units from color bar, identifies North Atlantic and Southern Ocean as high-uptake regions, notes tropical oceans as low, gray continents with no borders, elliptical projection, no grid lines, color gradient description matches actual rendering |
| Specificity | "Colorful ocean map" (no data read) | "Color bar: Anthropogenic CO2 (mol/m2) from 0 to 100; yellow in North Atlantic (~30-60N), dark blue in tropical Pacific; gray continents" (reads color bar and main patterns) | Color gradient at ~25 intervals (navy, medium blue, teal, cyan, yellow), specific geographic regions for each concentration level, tick marks at 0/50/100, Mollweide-like projection, color bar position and size relative to map, no title above map |
| Completeness | Mentions the map exists but omits the variable, color bar, or geographic patterns | Color bar with label and range, major high/low concentration regions, continent rendering described | Color bar label with units and superscript, tick values, full color gradient description, all major ocean basins characterized (North Atlantic, Southern Ocean, North Pacific, tropical, Arctic), continent rendering (gray, no borders), projection type, no grid lines, map border style, white background |
| Usefulness | "A NASA ocean map" (no scientific context) | "Shows where human-emitted CO2 accumulates in the ocean; highest in North Atlantic where currents carry surface CO2 to depth" | Identifies Sabine et al. 2004 source, explains deep water formation driving North Atlantic maximum, connects to ocean's role as carbon sink (~50% of emissions), notes column-integrated units, places in context of NASA article's discussion of ocean climate impacts |

<br><br>

## doc22-R12 -- ISS022-E-6674: Earth from space

**Content type:** photo
**Annotation difficulty:** Easy

### Visual Inventory

Wide-format panoramic photograph of Earth taken from the International Space
Station. The image shows Earth's surface dominated by ocean (deep blue) with
scattered white cloud formations of varying sizes. Sun glint (bright white
specular reflection) illuminates the ocean surface in the left-center portion
of the frame. The Earth's curvature is visible along the top edge, with a thin
bright blue atmospheric limb band transitioning to the blackness of space
above. The overall composition is approximately 3:1 aspect ratio (very wide
relative to height).

### Verifiable Facts

- Photograph taken from orbit (ISS vantage point based on the designation
  ISS022-E-6674)
- Earth's limb (curved horizon) visible along the upper edge of the frame
- Thin blue atmospheric band visible between Earth's surface and black space
- Sun glint reflection visible on the ocean surface in the left-center area
- Ocean covers the majority of the visible surface (estimated 80%+ of frame)
- Multiple cloud formations visible: scattered cumulus clusters, some larger
  cloud systems
- No clearly identifiable landmasses in this crop (mostly open ocean)
- Black space visible above the atmospheric limb in the upper portion
- The atmospheric layer appears as a very thin bright blue-white gradient band
- Image is photographic (not rendered/CGI) with natural lighting and exposure

### Hallucination Risks

- **Geographic identification:** The crop shows mostly open ocean with no
  obvious continental outlines. An annotator might attempt to identify the
  specific ocean basin or nearby landmasses, but there is insufficient
  geographic context in the image to confirm any location.
- **Cloud type classification:** An annotator might provide specific
  meteorological classifications (cumulonimbus, cirrus, etc.) when the
  resolution and viewing angle make precise identification uncertain.
- **ISS expedition details:** The "ISS022" designation identifies Expedition 22,
  but mission dates and crew details are not visible in the image. An annotator
  might add these from external knowledge.
- **Atmosphere thickness:** The atmospheric band is visible but its exact
  apparent thickness relative to Earth's radius is hard to quantify. An
  annotator might state specific measurements.

### Detail Inventory

- **Sun glint:** Bright white specular reflection covering a broad area in the
  left-center, creating a bright patch on the ocean surface where sunlight
  reflects directly toward the camera
- **Ocean color:** Deep blue in areas away from sun glint; appears almost black
  in the right portion where viewing angle is steeper
- **Cloud patterns:** Mix of isolated cumulus clusters and larger organized
  systems; some clouds cast visible shadows on the ocean surface; clouds appear
  bright white against the blue ocean
- **Atmospheric limb:** Thin gradient band from bright white/blue at the surface
  transition to deep blue to black space; the band is remarkably thin compared
  to Earth's radius, emphasizing the atmosphere's thinness
- **Earth curvature:** Gentle arc along the top edge showing the planet's
  spherical shape
- **Lighting:** Sun positioned to the left of frame based on glint location;
  natural orbital photography lighting conditions
- **Image quality:** Sharp, well-exposed NASA astronaut photograph
- **Aspect ratio:** Approximately 3:1 (panoramic/banner format)

### Domain Context

- HTML caption: "NASA astronaut photograph ISS022-E-6674."
- ISS022 indicates Expedition 22 (November 2009 to March 2010)
- This image serves as the header/banner image for the NASA global warming
  article, appearing at the very top before any text content
- The thin atmospheric limb visible in the photo is thematically relevant to
  the article's topic: it visually demonstrates how thin and fragile Earth's
  atmosphere is -- the same atmosphere that greenhouse gases are altering
- The designation format "ISS022-E-6674" follows NASA's standard: ISS +
  expedition number, E for electronic (digital) camera, frame number
- The photo is linked to NASA's Earth observation photo database at
  earth.jsc.nasa.gov

### Search Keywords

ISS, International Space Station, Earth from space, astronaut photograph,
orbital photography, atmospheric limb, thin atmosphere, sun glint, ocean,
clouds, Earth curvature, Expedition 22, NASA, climate change, global warming,
blue marble

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A photo of Earth" (correct but minimal) | "Panoramic ISS photo showing Earth's curved horizon with thin blue atmosphere band, ocean surface with sun glint, and scattered clouds over open ocean" (main elements correct) | All elements accurately described: sun glint location (left-center), atmospheric limb gradient (white-blue-black), ocean dominance (~80%+), cloud patterns with shadows, curvature along top edge, panoramic 3:1 aspect ratio, black space above limb |
| Specificity | "Blue planet photo" (generic) | "Wide-format image from ISS showing bright sun reflection on ocean, thin blue atmospheric band at horizon, scattered white clouds" (key visual features noted) | Sun glint position and extent, atmospheric limb color gradient (bright white to blue to black), ocean color variation (deep blue vs near-black at steep angles), cloud shadow details, approximate aspect ratio, photographic quality characteristics |
| Completeness | Mentions Earth and space but misses atmosphere, clouds, or sun glint | Sun glint, atmospheric limb, clouds, ocean, curvature, and black space all described | Sun glint with position, atmospheric limb with color gradient, cloud patterns with shadows, ocean color variation, Earth curvature, black space, aspect ratio, photographic (not CGI) nature, no visible landmasses noted |
| Usefulness | "A space photo on a climate website" (no thematic connection) | "ISS Expedition 22 astronaut photograph used as banner image for NASA's global warming article; thin atmosphere visible" | Identifies ISS022-E-6674 designation and Expedition 22 timeframe, explains thematic relevance (thin atmosphere fragility), notes placement as article header/banner, connects the visible atmospheric thinness to the global warming context, references NASA Earth observation database link |

<br><br>

## doc22-R15 -- Solar corona comparison: maximum vs minimum

**Content type:** photo
**Annotation difficulty:** Medium

### Visual Inventory

Side-by-side comparison of two extreme ultraviolet (EUV) images of the Sun,
showing the solar corona during solar maximum (left) and solar minimum (right).
Both images are false-color in shades of orange/red against a black space
background. Each Sun disk fills most of its respective panel. Text labels at
the bottom of each panel identify the images:
- Left: **"Solar Maximum"** (bold) **(February 22, 2002)** (regular weight)
- Right: **"Solar Minimum"** (bold) **(May 10, 2008)** (regular weight)

The two panels are separated by a thin black vertical gap.

### Verifiable Facts

- Two side-by-side Sun images in false-color orange/red EUV
- Left panel label: "Solar Maximum (February 22, 2002)" -- "Solar Maximum" in
  bold, date in regular weight
- Right panel label: "Solar Minimum (May 10, 2008)" -- "Solar Minimum" in bold,
  date in regular weight
- Left image (solar maximum) shows:
  - Brighter overall appearance with more contrast and variation
  - Several bright white/yellow active regions (hotspots) visible on the disk,
    concentrated in the central and lower-left area
  - Visible coronal loops and arcs extending from active regions
  - More texture and structure across the disk surface
  - A prominent bright active region near the center-left of the disk
- Right image (solar minimum) shows:
  - More uniform, dimmer, and evenly textured disk
  - No prominent bright active regions
  - A small prominence or coronal loop visible extending above the upper-right
    limb of the disk
  - Generally smoother, more homogeneous appearance
  - Slightly smaller apparent coronal extent
- Both images: black background representing space, full disk visible with no
  portion cut off
- Label text is white, positioned at the bottom-left of each panel

### Hallucination Risks

- **Sunspot identification:** The images are EUV (not visible light), so dark
  sunspots are not visible. An annotator might describe sunspots based on
  general knowledge of solar maximum, but this wavelength shows coronal
  emission (bright active regions) not photospheric sunspots.
- **Exact active region counts:** The number of distinct bright regions in the
  left image depends on resolution and how overlapping regions are counted. An
  annotator might state a precise count (e.g., "7 active regions") when the
  boundaries between regions are ambiguous.
- **Solar cycle number:** The 2002/2008 dates correspond to Solar Cycle 23
  (maximum ~2000-2002, minimum ~2008-2009), but this is not labeled in the
  image. An annotator might add cycle numbers from external knowledge.
- **Wavelength identification:** The orange/red false color is characteristic of
  EUV imaging (likely 304 angstrom from the EIT instrument), but the specific
  wavelength is not labeled. An annotator might state a precise wavelength
  without visual evidence.
- **Corona visibility:** The caption refers to "the transparent halo known as
  the solar corona" but the corona as a distinct halo is subtle in these EUV
  images. An annotator might describe a prominent corona halo that is not
  clearly visible in the crop.

### Detail Inventory

- **Left image (solar maximum):**
  - Bright white/yellow active regions: at least 3-4 distinct bright clusters
    visible on the disk
  - Prominent bright patch near center-left, spanning roughly 10-15% of the
    disk diameter
  - Additional bright regions in the lower-left quadrant
  - Coronal loops visible as arc-shaped structures extending from active regions
  - Overall disk shows mottled texture with alternating brighter and dimmer
    patches
  - Limb (edge) of the disk appears bright with some extension beyond the
    surface
- **Right image (solar minimum):**
  - Disk appears uniformly orange with granular texture
  - No prominent bright active regions on the disk face
  - One small prominence visible extending above the upper-right limb (a small
    loop or jet of material above the solar surface)
  - Limb appears cleaner/sharper with less coronal extension
  - Overall appearance is calmer, more uniform
- **False color:** Orange-red palette typical of EUV solar imaging; brighter
  features appear white/yellow, dimmer features appear dark orange/red
- **Background:** Pure black (space) in both panels
- **Text rendering:** White sans-serif font; bold for "Solar Maximum" / "Solar
  Minimum"; regular weight for the parenthetical dates
- **Panel layout:** Approximately equal-sized panels side by side with thin
  (~5-10px) black gap between them
- **Image quality:** Moderate resolution; individual features on the disk are
  visible but not extremely sharp

### Domain Context

- HTML caption: "The transparent halo known as the solar corona changes between
  solar maximum (left) and solar minimum (right)"
- Credit: "NASA Extreme Ultraviolet Telescope images from the SOHO Data Archive"
- The images are from the EIT (Extreme ultraviolet Imaging Telescope) instrument
  on the SOHO (Solar and Heliospheric Observatory) spacecraft
- This comparison appears in the "Is Current Warming Natural?" section, in the
  context of discussing whether solar variability can explain observed warming
- The article argues that while solar activity varies on an ~11-year cycle, the
  total solar irradiance change between maximum and minimum is only about 0.1%
  -- too small to explain observed warming of 0.6+ C
- Solar Cycle 23: maximum around 2000-2002, minimum in 2008-2009
- The visual difference between the two images illustrates that the Sun does
  change, but the accompanying charts (ACRIM TSI data) show the energy
  variation is very small

### Search Keywords

solar maximum, solar minimum, solar corona, SOHO, EIT, extreme ultraviolet,
Sun, solar cycle, active regions, coronal loops, solar variability, 2002, 2008,
NASA, false color, solar activity, climate forcing, total solar irradiance

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Two orange pictures of the Sun" (no dates, no max/min distinction) | "Side-by-side EUV images: Solar Maximum (Feb 22, 2002) on left with bright active regions, Solar Minimum (May 10, 2008) on right with uniform appearance" (dates and key difference correct) | Both labels quoted exactly with bold/regular styling, active regions described with approximate positions on the left disk, prominence on upper-right limb of right image noted, false-color orange/red palette identified, black backgrounds, EUV imaging noted |
| Specificity | "The Sun looks different in these two photos" (vague) | "Left image is brighter with several white/yellow hotspots; right image is more uniform orange; both against black background; dates labeled at bottom" (main visual differences noted) | Active region positions (center-left concentration), prominence location (upper-right limb), disk texture differences (mottled vs uniform), coronal loop structures in maximum image, limb brightness differences, text styling (bold labels, regular dates), panel gap width, false-color characteristics (brighter = white/yellow, dimmer = dark orange) |
| Completeness | Mentions two Sun images but omits dates, labels, or activity differences | Both labels with dates, active region vs quiet sun distinction, false color noted, black backgrounds described | Both labels with exact dates and text styling, active region description with positions and approximate count, prominence in minimum image, coronal loops, limb characteristics, false-color palette, text placement (bottom-left), panel layout (side-by-side with gap), disk texture in both images, no sunspots visible (EUV not visible light) |
| Usefulness | "Photos of the Sun from NASA" (no scientific context) | "Comparison showing how the Sun's corona changes during the 11-year solar cycle; from SOHO/EIT instrument; used in NASA article about whether solar changes cause global warming" | Identifies SOHO EIT instrument and data archive, places in Solar Cycle 23 context, connects to the article's argument that solar variability is too small to explain observed warming (~0.1% TSI variation), notes the visual drama of the comparison versus the small actual energy difference |

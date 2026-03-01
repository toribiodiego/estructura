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
| Correctness | "A line chart showing temperature over time" -- no axis values, no series names, no title. Or: fabricates specific annual values (e.g., "1998 was 0.63 C") when no data labels exist -- all values are approximate axis readings with ~0.05 C tolerance. Describing the trend as "linear increase" mischaracterizes the 4-phase pattern (cool, first warming, plateau, rapid rise). Inventing a third data series or additional legend entries triggers the hallucination cap. | Title "Global Mean Surface Temperature" correct, both series named (annual mean, 5-year running mean), y-axis range -0.4 to 0.6 C, x-axis 1880-~2005. Post-1975 steep rise noted, end value ~0.6 C. Uncertainty bars present. May miss the mid-century dip detail or the 0.2-increment gridline spacing. | All axis labels and ranges exact: "Temperature Anomaly (C)" -0.4 to 0.6 in 0.2 increments, "Year" 1880-~2005 in 20-year ticks. Legend entries: annual mean (thin light red), 5-year running mean (thick dark red), uncertainty (I-shaped bars). 4-phase pattern described: cool period ~1880-1910, first warming ~1910-1940, mid-century dip ~1940-1965, rapid rise ~1975-2005. End value ~0.6. All values hedged as axis readings. No fabricated data points. |
| Information Recovery | Identifies as a temperature chart with a rising line. A search for "5-year running mean" or "Temperature Anomaly" or "1880" would not match. The two series, uncertainty bars, and 4-phase temporal structure are invisible. | Both series named with colors, axis labels and ranges present, legend entries listed, post-1975 acceleration highlighted. "Global mean surface temperature anomaly" would match. May miss the I-shaped error bar style, the exact number of uncertainty markers, the 0.2-increment gridline spacing, or the 20-year tick marks. | Complete recovery: title text, both axis labels with units and full ranges, legend with all 3 entries and visual descriptions (line weights, colors), I-shaped uncertainty bars at ~6 positions, gridline pattern (horizontal at 0.2, no vertical gridlines), data trend in 4 phases with approximate transition years, white background. Any data feature visible in the chart is findable -- parity principle met. |
| Retrieval Value | "A temperature chart from NASA" -- no dataset name, not self-contained. Would not surface for "GISS temperature anomaly" or "global warming trend chart" or "1951-1980 baseline." | "GISS surface temperature anomaly chart showing global warming from 1880 to 2005; ~0.6 C above baseline by end." Searchable but doesn't explain anomaly baseline (1951-1980) or the significance of the 4-phase pattern. | Natural prose identifying this as the GISS (Goddard Institute for Space Studies) global mean surface temperature anomaly chart from NASA's climate change article. Explains anomaly baseline (1951-1980 average), 4-phase warming pattern, and the post-1975 acceleration to ~0.6 C. Notes GISS as one of the primary global temperature datasets alongside HadCRUT and NOAA MLOST. Domain vocabulary embedded (GISS, temperature anomaly, running mean, global warming, baseline period). Self-contained. Findable by "GISS temperature anomaly chart" or "global mean surface temperature trend." |

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
| Correctness | "A chart showing temperature changes over a long time" -- no axis values, no time scale, no anomaly range. Or: claims the chart shows CO2 data (it does not -- the caption mentions CO2 but the chart image only shows temperature). Fabricating specific temperature values for individual peaks (e.g., "the interglacial at -125,000 years was exactly +3.2 C") when no data labels exist is a precision error -- all readings are approximate axis alignments with ~0.5 C tolerance at this scale. Describing the pattern as "random fluctuation" mischaracterizes the cyclic glacial-interglacial structure. | 800,000-year temperature anomaly chart identified with correct axis ranges (-8 to +4 C, -800,000 to 0 years). Cyclic glacial-interglacial pattern noted, ~8 major cycles. Olive/green data line described. CO2 data correctly absent from the image. May miss the scatter data behind the main line or the sawtooth asymmetry. | Axis labels exact: "Temperature Anomaly (C)" with ticks at -8, -4, 0, 4; "Year" from -800,000 to 0 in 200,000-year increments with comma formatting. ~8 glacial-interglacial cycles with sawtooth asymmetry (gradual cooling, rapid warming). Tallest peak ~+4 C around -400,000 years. Deepest troughs near -8 C. Dark olive line with lighter scatter/uncertainty data behind it. No title, no legend, no gridlines. CO2 data absent despite catalog description. All values hedged as axis readings. |
| Information Recovery | Identifies as a climate chart with oscillating data. A search for "EPICA" or "glacial-interglacial" or "-800,000" would not match. The time scale, anomaly range, cyclic structure, and data rendering details are invisible. | Both axes labeled with ranges, ~8 cycles noted, olive line and scatter data described, sawtooth pattern mentioned. "800,000-year temperature anomaly" would match. May miss the comma formatting in axis labels, the absence of title/legend/gridlines, or the tallest peak identification at ~-400,000 years. | Complete recovery: both axis labels with units, tick mark values, and formatting. Data rendering described (dark olive line + lighter scatter). All ~8 major cycle peaks and troughs approximately positioned. Sawtooth asymmetry documented (gradual cooling, rapid warming). Tallest peak and deepest troughs identified. Absence of title, legend, and gridlines noted. Background scatter/uncertainty data noted. Any cycle feature visible in the chart is findable -- parity principle met. |
| Retrieval Value | "An old climate chart" -- no source, not self-contained. Would not surface for "EPICA ice core reconstruction" or "glacial-interglacial temperature cycles" or "Milankovitch cycles." | "EPICA ice core temperature record showing glacial-interglacial cycles over 800,000 years; from NASA's global warming article." Searchable but doesn't explain the significance of the cyclicity or the comparison to modern warming rates. | Natural prose identifying this as the EPICA Dome C 800,000-year temperature reconstruction (Jouzel et al. 2007). Explains glacial-interglacial cycles driven by Milankovitch orbital forcing. Notes that modern warming rate (~0.7 C/century) far exceeds ice-age recovery rates (~1 C/millennium). Context: NASA article section on "How is Today's Warming Different?" CO2 data absent from this chart despite catalog mention. Domain vocabulary embedded (EPICA, Dome C, glacial-interglacial, Milankovitch, temperature anomaly, ice core). Self-contained. Findable by "EPICA 800K year temperature" or "glacial cycle ice core reconstruction." |

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
| Correctness | "Four charts showing different climate factors" -- no panel titles, no axis values, no color distinction, no scale difference. Or: describes all 4 panels as having the same y-axis range (the top 3 span -0.2 to +0.2 C, while the bottom panel spans -0.2 to +0.6 C -- this scale difference is the chart's core analytical point). Fabricating specific ENSO peak values or volcanic spike depths beyond approximate axis readings triggers the hallucination cap. Labeling volcanic spikes with eruption names (e.g., "Pinatubo") is domain knowledge fabrication -- no eruption labels appear in the image. | 4-panel chart identified: ENSO, Total Solar Irradiance, Volcanic Aerosols (olive lines), Human-caused Forcings (red line). Top 3 panels oscillate near zero within +/-0.2 C; bottom panel rises to ~0.6 C. Time range ~1890-2005 correct. Color distinction (olive vs red) noted. May miss the subtitle text on the bottom panel or the exact volcanic spike timing. | All 4 panel titles exact: "El Nino/Southern Oscillation", "Total Solar Irradiance", "Volcanic Aerosols", "Human-caused Forcings (greenhouse gases, albedo, aerosols)." Y-axis ranges correct: top 3 at -0.2 to +0.2, bottom at -0.2 to +0.6. X-axis ~1890-2005 in 20-year ticks. Volcanic spike timing approximate (~1902, ~1963, ~1982, ~1991). Human forcing flat to ~1940, gradual rise to ~1970, steep rise to ~0.6 by 2005. Zero reference lines in all panels. Olive vs red color distinction. No fabricated eruption labels or exact peak values. |
| Information Recovery | Identifies as multiple climate charts. A search for "El Nino/Southern Oscillation" or "Volcanic Aerosols" or "Human-caused Forcings" would not match. The 4-panel structure, the y-axis scale difference, and the olive/red color coding are invisible. | All 4 panel titles recovered, y-axis ranges for both scales documented, main patterns per panel described (ENSO oscillation, TSI near-zero, volcanic spikes, human forcing rise). "Climate attribution multi-panel chart" would match. May miss ENSO oscillation frequency, TSI amplitude details, individual volcanic spike positions, or the human forcing curve inflection points. | Complete recovery: all 4 panel titles with subtitle text, both y-axis ranges (0.2 vs 0.6 top), x-axis range and tick spacing, zero reference lines in all panels, line colors per panel (3 olive + 1 red), volcanic spike positions (~4 major spikes), ENSO high-frequency oscillation, TSI barely distinguishable from zero, human forcing curve shape with inflection points. No legend, no gridlines noted. Any panel feature visible in the chart is findable -- parity principle met. |
| Retrieval Value | "Climate charts from NASA" -- no attribution context, not self-contained. Would not surface for "climate attribution analysis" or "natural vs human forcing comparison" or "ENSO volcanic solar decomposition." | "Shows natural factors (ENSO, solar, volcanic) oscillate around zero while human forcing rises to 0.6 C -- demonstrates humans are the dominant warming cause." Searchable but doesn't explain the visual design (different y-axis scales) or the analytical significance. | Natural prose identifying this as a climate forcing attribution analysis (Lean et al. 2008 style) from NASA's global warming article. Explains the chart's core argument: natural forcings (ENSO, solar, volcanic) are small and oscillate around zero, while human-caused forcings have risen 3x beyond the natural range. Notes the deliberate y-axis scale difference that visually emphasizes this magnitude gap. Volcanic spikes correspond to known eruptions (unlabeled). Context: "Is Current Warming Natural?" section. Domain vocabulary embedded (ENSO, solar irradiance, volcanic aerosols, climate attribution, forcing). Self-contained. Findable by "climate forcing attribution" or "natural vs human warming factors." |

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
| Correctness | "A blue and yellow map of the ocean" -- no variable name, no units, no concentration range. Or: describes the yellow region as showing "high ocean temperature" or "pollution" rather than anthropogenic CO2 concentration. Fabricating specific mol/m2 values for individual ocean regions beyond the color bar range (0-100) triggers the hallucination cap -- individual pixel values are approximate color-bar readings. Calling the projection "Mercator" when it is elliptical (Mollweide-like) is a misidentification. | Global map of anthropogenic CO2 in oceans identified, 0-100 mol/m2 color bar correct. North Atlantic highest (yellow/cyan), tropical Pacific lowest (dark blue). Gray continents, elliptical projection. May miss the Southern Ocean as a secondary high-uptake region or the tick mark positions (0/50/100). | Color bar label exact: "Anthropogenic CO2 (mol/m2)" with superscript 2, range 0-100, ticks at 0/50/100. North Atlantic and Southern Ocean high-uptake (yellow/cyan), tropical oceans low (dark blue/navy). Gray continents with no borders. Elliptical (Mollweide-like) projection. No grid lines, no title above map. Color gradient described accurately (navy through medium blue, teal, cyan, yellow). No fabricated specific regional values beyond color bar approximation. |
| Information Recovery | Identifies as an ocean map with colors. A search for "Anthropogenic CO2" or "mol/m2" or "North Atlantic carbon uptake" would not match. The variable name, color bar, and geographic distribution pattern are invisible. | Color bar label and range recovered, major high/low regions identified (North Atlantic, tropical Pacific), gray continents noted, elliptical projection described. "Anthropogenic CO2 ocean map" would match. May miss the full color gradient description, the superscript in units, or the characterization of all major ocean basins. | Complete recovery: color bar label with units (including superscript), tick values, full color gradient (navy to yellow with ~5 color steps), geographic characterization of all major ocean basins (North Atlantic, Southern Ocean, North Pacific, tropical Pacific, tropical Indian, Arctic). Continent rendering (gray, no borders), projection type, absence of grid lines and title. Any ocean region or color bar feature visible in the map is findable -- parity principle met. |
| Retrieval Value | "A NASA ocean map" -- no scientific context, not self-contained. Would not surface for "anthropogenic CO2 ocean uptake" or "carbon sink distribution" or "deep water formation." | "Shows where human-emitted CO2 accumulates in the ocean; highest in North Atlantic, 0-100 mol/m2." Searchable but doesn't explain why the North Atlantic has the highest concentration or the oceanographic context. | Natural prose identifying this as a global ocean anthropogenic CO2 column inventory map (Sabine et al. 2004). Explains North Atlantic maximum driven by deep water formation (thermohaline circulation carrying surface CO2 to depth). Ocean as major carbon sink (~50% of anthropogenic emissions). Column-integrated units (mol/m2 = total CO2 per unit ocean surface area). Context: NASA article's discussion of ocean carbon cycle and climate impacts. Domain vocabulary embedded (anthropogenic CO2, carbon sink, deep water formation, column inventory). Self-contained. Findable by "ocean anthropogenic CO2 map" or "North Atlantic carbon uptake distribution." |

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
| Correctness | "A photo of Earth" -- correct but no visual elements described. Or: claims to identify a specific continent or landmass (no landmasses are visible -- only ocean, clouds, and atmosphere). Describing this as a "satellite image" rather than an astronaut photograph is an imprecise characterization. Fabricating geographic coordinates or a specific ocean region without visible reference points triggers the hallucination cap. | Panoramic ISS photo showing Earth's curved horizon, thin blue atmospheric band, ocean surface with sun glint (left-center), and scattered clouds. No landmasses visible. Black space above the limb. Panoramic aspect ratio noted. May miss the atmospheric limb color gradient detail or cloud shadow patterns on the ocean surface. | All visual elements accurate: sun glint position (left-center, bright white), atmospheric limb gradient (white to blue to black), ocean surface dominant (~80%+, deep blue varying with viewing angle), scattered white clouds with visible shadows on ocean, Earth curvature along top edge, black space above limb, panoramic ~3:1 aspect ratio. Correctly notes no visible landmasses. Photographic (not CGI) quality. No fabricated geographic identifications. |
| Information Recovery | Identifies as a photo of Earth from space. A search for "atmospheric limb" or "sun glint" or "ISS panoramic" would not match. The specific visual elements (glint position, limb gradient, cloud patterns, aspect ratio) are invisible. | Sun glint, atmospheric band, clouds, ocean, curvature, and black space all described. "Earth from space panoramic ocean" would match. May miss the atmospheric limb color gradient stages, the ocean color variation with viewing angle, or the cloud shadow details. | Complete recovery: sun glint with position and brightness, atmospheric limb with full color gradient (white-blue-black), cloud patterns with ocean-surface shadows, ocean color variation (deep blue to near-black at steep angles), Earth curvature, black space, panoramic aspect ratio, photographic quality. Absence of landmasses explicitly noted. Any visual feature in the photograph is findable -- parity principle met. |
| Retrieval Value | "A space photo on a climate website" -- no thematic connection, not self-contained. Would not surface for "ISS Earth photograph" or "atmospheric thinness" or "climate change header image." | "ISS astronaut photo used as banner for NASA's global warming article; thin atmosphere visible." Searchable but doesn't explain the thematic significance of the atmospheric thinness in a climate context. | Natural prose identifying this as ISS Expedition 22 photograph ISS022-E-6674 used as the NASA global warming article banner. Explains thematic relevance: the visibly thin atmospheric band dramatizes the fragility of the atmosphere that climate change is altering. Panoramic format emphasizes the horizon-spanning scale. Context: article header image framing the climate change discussion. Domain vocabulary embedded (ISS, atmospheric limb, sun glint, Earth observation). Self-contained. Findable by "ISS Earth atmosphere photograph" or "NASA global warming article banner image." |

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
| Correctness | "Two orange pictures of the Sun" -- no dates, no max/min distinction, no activity differences described. Or: swaps the dates (assigning Feb 2002 to the right/minimum image). Describing the bright regions as "sunspots" is incorrect -- these are EUV active regions, not visible-light sunspots. Fabricating specific temperatures or wavelength values not shown in the image triggers the hallucination cap. Calling these "photographs" without noting the false-color EUV imaging is imprecise. | Side-by-side EUV images correctly identified: Solar Maximum (Feb 22, 2002) left with bright active regions, Solar Minimum (May 10, 2008) right with uniform appearance. False-color orange/red palette noted. Black backgrounds. Dates and labels correct. May miss the prominence on the minimum image's limb or the text styling differences. | Both labels quoted exactly: "Solar Maximum (February 22, 2002)" and "Solar Minimum (May 10, 2008)" with bold/regular text styling. Active regions in maximum image with approximate disk positions (center-left concentration). Prominence on upper-right limb of minimum image noted. False-color orange/red EUV palette identified. Disk texture difference (mottled vs uniform). Black backgrounds. No fabricated wavelength or temperature values. |
| Information Recovery | Identifies as two Sun images. A search for "Solar Maximum" or "February 22, 2002" or "EUV corona" would not match. The date labels, max/min distinction, and activity comparison are invisible. | Both labels with dates recovered, active region vs quiet sun distinction described, false-color noted, side-by-side layout documented. "Solar maximum minimum comparison" would match. May miss active region positions on the disk, the prominence in the minimum image, coronal loop structures, or the text styling details. | Complete recovery: both labels with exact dates and text styling (bold labels, regular dates), active region description with disk positions, prominence location (upper-right limb of minimum image), coronal loop structures in maximum, limb brightness differences, false-color characteristics (brighter = white/yellow, dimmer = dark orange), panel layout (side-by-side with gap), text placement (bottom-left of each panel). Any visual feature in either panel is findable -- parity principle met. |
| Retrieval Value | "Photos of the Sun from NASA" -- no scientific context, not self-contained. Would not surface for "solar cycle comparison" or "SOHO EIT corona" or "solar variability and climate." | "Solar cycle comparison showing maximum (2002) vs minimum (2008) from SOHO EIT; used in NASA's global warming article about whether solar changes cause warming." Searchable but doesn't explain the scientific argument. | Natural prose identifying this as a SOHO EIT (Extreme Ultraviolet Imaging Telescope) comparison of Solar Cycle 23 maximum and minimum. Explains that the dramatic visual difference (active regions, coronal loops) corresponds to only ~0.1% change in total solar irradiance (TSI). Context: NASA article argument that solar variability is far too small to explain observed warming. The visual drama vs actual energy difference is the key pedagogical point. Domain vocabulary embedded (solar cycle, EUV, active regions, corona, TSI, SOHO). Self-contained. Findable by "solar maximum minimum EUV comparison" or "SOHO solar cycle climate argument." |

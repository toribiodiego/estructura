# Image Analysis: Doc 21 -- 21_praxie_project_portfolio.xlsx

**Document:** `21_praxie_project_portfolio.xlsx`
**Format:** XLSX
**Source:** https://praxie.com/wp-content/uploads/2021/08/Project-Portfolio-Management-Template.xlsx
**Category:** multi-image
**Images:** 4
**Document context:** Praxie project portfolio management template with 4
single-series bar charts summarizing project priority distribution, status,
risk levels, and budget vs actual expenditure.

**Eval subset:** 2 of 4 content images

<br><br>

## doc21-C01 -- Horizontal bar: Priority distribution

**Content type:** chart-simple
**Annotation difficulty:** Easy

**Note:** Catalog describes "3 bars: Low/Medium/High" but the rendered chart
has 4 bars including a "Total Result" summary bar. The catalog undercounted.

### Visual Inventory [-> Information Recovery]

- **Chart type:** Horizontal bar chart with 4 categories and a single data
  series
- **Title:** None visible (a blue decorative band appears above the chart but
  contains no readable text)
- **X-axis (horizontal, bottom):** Numeric scale from 0 to 1 with tick marks
  at 0, 0.5, and 1
- **Y-axis (vertical, left) categories (top to bottom):** Total Result, HIGH,
  MEDIUM, LOW
- **Category labels:** Gray text, all caps except "Total Result" which uses
  title case across two lines
- **Gridlines:** Three light gray vertical gridlines at 0, 0.5, and 1
- **Bars:** All bars are a muted sage/olive green color with slight saturation
  variation:
  - Total Result: extends slightly past the 1.0 gridline (~1.05), deepest
    green
  - HIGH: extends to approximately 1.0, medium green
  - MEDIUM: extends to approximately 1.0, medium green
  - LOW: shorter bar, extends to approximately 0.8, lightest/most washed-out
    green
- **Legend:** None
- **Data labels:** None on bars
- **Chart border:** Thin gray line enclosing the plot area on left and top
- **Background:** White
- **Decorative element:** Blue rectangular band (~50px tall) above the chart
  area, no text visible

### Verifiable Facts [-> Correctness]

- FACT: The chart is a horizontal bar chart (bars extend right from the
  y-axis)
- FACT: There are exactly 4 bars with categories: Total Result, HIGH, MEDIUM,
  LOW
- FACT: The x-axis has exactly 3 labeled tick marks: 0, 0.5, and 1
- FACT: No chart title text is visible
- FACT: No legend is present
- FACT: No data labels appear on or adjacent to the bars
- FACT: The "Total Result" bar is the longest, extending past the 1.0
  gridline
- FACT: The "LOW" bar is visibly shorter than the other three
- FACT: The HIGH and MEDIUM bars appear approximately equal in length, both
  reaching approximately the 1.0 gridline
- FACT: All bars use a green/olive color palette with the LOW bar being
  noticeably lighter/more washed out
- FACT: Category labels are gray text in all caps (LOW, MEDIUM, HIGH) except
  "Total Result" which wraps to two lines

### Hallucination Risks [-> Correctness]

- RISK: Stating there are 3 bars (as the catalog says)
  REALITY: There are 4 bars; the catalog omits the "Total Result" bar
- RISK: Calling this a vertical bar chart
  REALITY: This is a horizontal bar chart -- bars extend rightward from
  category labels on the left
- RISK: Fabricating specific numeric values for bar lengths (e.g., "HIGH = 1",
  "LOW = 0.8")
  REALITY: No data labels are present; bar lengths can only be estimated
  visually from gridline positions. Exact values are not readable.
- RISK: Inventing a chart title (e.g., "Priority Distribution" or "Project
  Priority")
  REALITY: No title text is visible in the crop; the blue band above the
  chart contains no readable text
- RISK: Describing bars as different colors to indicate different data series
  REALITY: All bars are the same color family (sage/olive green); the
  saturation variation does not indicate separate series, it likely reflects
  the charting library's gradient or the LOW category having a different value
  range
- RISK: Adding a legend description
  REALITY: No legend is present in the chart

### Detail Inventory [-> Information Recovery]

- Horizontal bar orientation (not vertical)
- 4 category labels with exact text and casing: "Total Result" (two lines),
  "HIGH", "MEDIUM", "LOW"
- X-axis scale: 0, 0.5, 1
- 3 vertical gridlines corresponding to x-axis tick marks
- Bar color: muted sage/olive green (#9CB973 approximate)
- LOW bar lighter saturation than other three bars
- Total Result bar extends ~5% past the 1.0 gridline
- HIGH and MEDIUM bars terminate near the 1.0 gridline
- LOW bar terminates between 0.5 and 1.0, closer to 1.0 (~0.8)
- Blue decorative band above chart (~50px tall, cornflower blue, #6495ED
  approximate)
- Thin gray border on left and top edges of plot area
- White chart background
- No data labels, no legend, no title text, no annotations

### Domain Context [-> Retrieval Value]

This chart appears in the Praxie Project Portfolio Management (PPM) template,
a spreadsheet tool for tracking multiple projects across dimensions like
priority, status, risk, and budget. The chart summarizes how many projects fall
into each priority level (LOW, MEDIUM, HIGH) with a Total Result aggregation.

The x-axis scale (0 to 1) and the fact that all bars hover near 1.0 suggest
this is a template with placeholder data (likely 1 project per priority
level). In real use, the bars would reflect actual project counts from a
portfolio data table.

Project Portfolio Management is a business practice for centrally managing a
collection of projects to achieve strategic objectives, optimize resource
allocation, and balance risk.

### Search Keywords [-> Retrieval Value]

project portfolio management, PPM, priority distribution, horizontal bar
chart, project priority, Low Medium High, Praxie template, portfolio
dashboard, project tracking, resource allocation

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A bar chart showing project priorities" -- misses Total Result bar, does not specify horizontal orientation, no values. Or: describes bars as reaching specific values not readable from the image (no data labels exist, so bar heights are approximate axis readings with ~10% tolerance). Inventing data labels triggers the hallucination cap. | Horizontal bar chart with 4 categories (Total Result, HIGH, MEDIUM, LOW). X-axis 0-to-1 scale correct. Notes Total Result extends past 1.0, HIGH and MEDIUM near 1.0, LOW shorter (~0.8). Minor imprecision on approximate bar lengths acceptable (axis readings). | All 4 categories named in correct order. X-axis scale 0/0.5/1.0 correct. Bar lengths described with appropriate hedging (approximate readings, no data labels). Notes absence of title, legend, and data labels. No fabricated values. |
| Information Recovery | Identifies as a bar chart with priority levels. Names 2-3 categories. A search for "Total Result priority" or "LOW bar length" would not match. The horizontal orientation and 0-1 scale are missing. | All 4 categories named, horizontal orientation specified, 0-1 scale documented. Approximate bar lengths described. "HIGH priority bar" would match. May miss the blue decorative band or the Total Result wrapping to two lines. | All 4 categories with approximate bar lengths recovered. Chart structure fully documented (horizontal, 0-1 scale, no title/legend/data labels). Blue decorative band and absence of metadata noted. Any category visible in the chart is findable -- parity principle met. |
| Retrieval Value | "A chart from a spreadsheet" -- no domain vocabulary, not self-contained. Would not surface for "project priority distribution" or "portfolio management." | "Priority distribution chart from a project portfolio management template" -- searchable terms. Partially self-contained but doesn't explain the 0-1 scale or template context. | Natural prose identifying this as a Praxie PPM template priority distribution chart. Notes placeholder data (all near 1.0) indicating template state. Domain vocabulary embedded (PPM, priority distribution, portfolio dashboard). Self-contained. Findable by "project priority chart" or "portfolio management dashboard." |

<br><br>

## doc21-C04 -- Vertical bar: Budget vs Actual Expenditure

**Content type:** chart-simple
**Annotation difficulty:** Easy

**Note:** The second bar ("Sum of Actual Expenditure") and its x-axis label are
truncated at the right edge of the rendered page. This is a PDF export
rendering limitation -- the chart extends beyond the page boundary in the
LibreOffice conversion. The data table on the following sheet confirms the
values: Sum of Budget = $600.00, Sum of Actual Expenditure = $500.00.

### Visual Inventory [-> Information Recovery]

- **Chart type:** Vertical bar chart with 2 categories and a single data series
- **Title:** "BUDGET" (centered, black text, all caps)
- **Y-axis (vertical, left):** Dollar amounts from $440.00 to $620.00 in
  $20.00 increments
- **X-axis (horizontal, bottom) category labels:**
  1. "Sum of Budget" -- fully visible
  2. "Sum of Actu..." -- truncated at page edge (full label: "Sum of Actual
     Expenditure")
- **Gridlines:** Gray horizontal gridlines at each $20.00 increment (10
  gridlines from $440.00 to $620.00)
- **Bars:**
  - Sum of Budget: peach/salmon colored bar, top edge aligns with the $600.00
    gridline
  - Sum of Actual Expenditure: lighter peach/salmon bar, top edge aligns
    between $480.00 and $500.00 gridlines (approximately $500.00), partially
    cut off on right side
- **Legend:** None
- **Data labels:** None on bars
- **Chart border:** Thin gray line on left and top edges of plot area
- **Background:** White
- **Y-axis origin:** $440.00 (NOT zero -- this is a truncated axis)
- **Rendering artifact:** The right ~15% of the chart is clipped by the page
  boundary, cutting through the second bar and its label

### Verifiable Facts [-> Correctness]

- FACT: The chart title reads "BUDGET" in all caps
- FACT: There are exactly 2 bars
- FACT: The first bar is labeled "Sum of Budget"
- FACT: The second bar label is truncated to "Sum of Actu..." in the crop
- FACT: The y-axis ranges from $440.00 to $620.00 in $20.00 increments
- FACT: The y-axis does NOT start at zero -- it starts at $440.00
- FACT: The first bar (Sum of Budget) reaches the $600.00 gridline
- FACT: The second bar (Sum of Actual Expenditure) reaches approximately the
  $500.00 gridline
- FACT: The first bar is taller than the second bar
- FACT: Both bars are peach/salmon colored; the Budget bar is more saturated
  than the Actual Expenditure bar
- FACT: No data labels appear on or adjacent to the bars
- FACT: No legend is present
- FACT: The second bar is partially clipped at the right edge of the rendered
  page

### Hallucination Risks [-> Correctness]

- RISK: Stating the y-axis starts at zero
  REALITY: The y-axis starts at $440.00, making the visual height difference
  between bars appear much larger than the actual proportional difference
  ($600 vs $500 is a 20% gap, but visually the Budget bar appears ~3x taller
  than the Actual bar due to the truncated axis)
- RISK: Reading the second bar label as "Sum of Actual" or inventing the full
  label text from context
  REALITY: The label is visibly truncated to "Sum of Actu..." in the crop;
  the full text is only confirmable from the data table on a separate page
- RISK: Fabricating exact dollar values for bar heights (e.g., "$600.00" and
  "$500.00")
  REALITY: While the bars align closely with gridlines, no data labels are
  present. The $600.00 value is visually precise (top of bar matches
  gridline); the $500.00 value is approximate (top of bar is near but the bar
  is partially clipped)
- RISK: Describing this as a "grouped bar chart" or "comparison chart" with
  two series
  REALITY: This appears to be a simple bar chart with 2 categories, not a
  grouped chart with multiple series per category
- RISK: Missing the truncated y-axis and describing the bars as proportionally
  different (e.g., "Budget is much larger than Actual")
  REALITY: The truncated axis exaggerates the visual difference; $600 vs $500
  is only a 17% difference

### Detail Inventory [-> Information Recovery]

- Chart title text: "BUDGET" (all caps, centered, black, sans-serif font)
- Y-axis labels: $440.00, $460.00, $480.00, $500.00, $520.00, $540.00,
  $560.00, $580.00, $600.00, $620.00 (all with dollar sign and two decimal
  places)
- X-axis labels: "Sum of Budget" (full), "Sum of Actu..." (truncated)
- 10 horizontal gray gridlines at each $20.00 increment
- Bar 1 color: medium peach/salmon (#F4B183 approximate)
- Bar 2 color: light peach/salmon (#F8D7BE approximate, noticeably lighter)
- Bar 1 height: top edge precisely at $600.00 gridline
- Bar 2 height: top edge at approximately $500.00 (between $480.00 and
  $500.00 gridlines, closer to $500.00)
- Y-axis starts at $440.00 (truncated, not zero-based)
- Thin gray border on left and top of plot area
- White chart background
- Right-side clipping: second bar and label cut off by page boundary
- Chart appears within a gray-bordered cell/frame on the spreadsheet page

### Domain Context [-> Retrieval Value]

This chart appears on the Budget sheet of the Praxie Project Portfolio
Management template. It compares total budgeted amounts against actual
expenditure across all projects in the portfolio. The accompanying data table
(visible on the next rendered page) confirms: Sum of Budget = $600.00, Sum of
Actual Expenditure = $500.00.

The template uses placeholder data ($200, $100, $300 budget entries for three
sample projects), so the totals ($600 budget, $500 actual) are illustrative.
In real use, these values would reflect actual project financial data.

The truncated y-axis (starting at $440 instead of $0) is a common spreadsheet
charting default that visually exaggerates differences between values -- a
known data visualization concern that document processing systems should
ideally flag.

### Search Keywords [-> Retrieval Value]

budget vs actual expenditure, project portfolio, PPM, vertical bar chart,
budget comparison, Praxie template, sum of budget, actual spending, financial
dashboard, truncated axis, project tracking

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A bar chart showing budget data with two bars" -- no title, no axis range, no mention of truncated y-axis. Or: states y-axis starts at zero (it starts at $440), fabricates exact dollar values as "data labels" (none exist), or calls the second bar label "Sum of Actual Expenditure" without noting visible truncation to "Sum of Actu..." Any fabricated data label triggers the hallucination cap. | Title "BUDGET" correct, 2 bars identified with correct labels (noting truncation of second). Y-axis range $440-$620 correct with truncated origin noted. Bar heights described with appropriate hedging (~$600, ~$500). May miss $20 increment detail or the saturation difference between bars. | All verifiable facts exact: title "BUDGET" (all caps), "Sum of Budget" bar at $600.00 gridline, "Sum of Actual" bar at ~$500.00 (hedged -- no data labels). Y-axis $440.00-$620.00 in $20 increments, truncated axis (not zero-based). Second bar and label clipped at right page edge. No data labels, no legend. Bar height values derived from gridline alignment, not fabricated labels. |
| Information Recovery | Identifies as a bar chart with two bars. No title text, no axis range, no colors, no clipping artifact. A search for "truncated axis" or "Sum of Budget" would not match. The truncated y-axis -- the most important analytical detail -- is invisible to the system. | Title "BUDGET" recovered, both bar labels present (with truncation noted), y-axis $440-$620 range documented, peach/salmon colors described, truncated axis flagged. "Budget vs actual bar chart" would match. May miss gridline count, dollar format (.00), or the rendering clipping artifact. | Complete recovery: title text, both x-axis labels (full and truncated forms), y-axis scale with all 10 tick values in $20 increments, bar heights relative to gridlines, color descriptions with saturation difference, truncated origin at $440, clipping artifact on right edge, absence of data labels/legend, chart border details. Any chart element visible in the image is findable -- parity principle met. |
| Retrieval Value | "A financial chart" -- no domain vocabulary, not self-contained. Would not surface for "budget vs actual expenditure" or "project portfolio financial tracking." Cannot understand what the chart compares or why the truncated axis matters. | "Budget comparison chart from a project portfolio template showing ~$600 budgeted vs ~$500 actual." Contains searchable terms but doesn't explain truncated axis concern or template placeholder context. Partially self-contained. | Natural prose identifying this as a Praxie PPM template budget comparison. Notes truncated y-axis ($440 origin) exaggerates the visual difference between $600 and $500 (17% gap appears much larger). Template placeholder context explained (3 sample projects). Rendering clipping identified as XLSX-to-PDF conversion artifact. Domain vocabulary embedded (budget vs actual expenditure, portfolio management). Self-contained. Findable by "budget comparison chart" or "portfolio financial tracking." |

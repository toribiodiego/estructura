# Image Analysis: Doc 20 -- 20_illinois_workforce_dashboard.xlsx

**Document:** `20_illinois_workforce_dashboard.xlsx`
**Format:** XLSX
**Source:** https://www.illinoisworknet.com/WIOA/Resources/Documents/6.%20Dashboard%20for%20the%20Local%20Workforce%20Board%20-%20TEMPLATE.xlsx
**Category:** multi-image
**Images:** 5
**Document context:** Illinois WorkNet WIOA formula grant dashboard template
with 5 XML-defined chart objects (grouped bar and pie charts) tracking
workforce program obligations, expenses, and training metrics.

**Eval subset:** 3 of 5 content images

<br><br>

## doc20-C01 -- Stacked bar: Obligations, Accrual & Expense Breakdown

**Content type:** chart-complex
**Annotation difficulty:** Medium

**Note:** Catalog describes this as "Grouped bar" with "12 series" but the
rendered chart is a stacked bar chart with 4 legend entries and 4 x-axis
categories. The "12 series" likely refers to XML chart series definitions in
the XLSX, not visually distinct data series.

### Visual Inventory [-> Information Recovery]

- **Chart type:** Stacked bar chart with 4 categories and 4 data series
- **Title:** "Obligations, Accrual & Expense Breakdown"
- **Y-axis:** 0% to 90% in 10% increments with gray dashed horizontal
  gridlines
- **X-axis categories (left to right):** Required, Adult, Dislocated Worker,
  Youth
- **Legend (right side, 4 entries top to bottom):**
  1. Obligations & Expense Required % -- dark navy square
  2. Obligations Actual % -- medium blue square
  3. Accruals Actual % -- yellow/gold square
  4. Expense Actual % -- green/olive square
- **Chart border:** Thin black line enclosing the plot area
- **Background:** White

**Bar data by category:**

| Category | Expense Actual % (green, bottom) | Accruals Actual % (yellow, middle) | Obligations Actual % (blue, top) | Obligations & Expense Required % (navy) | Approx. total height |
|----------|-----|--------|------|------|------|
| Required | -- | -- | -- | 80% | 80% |
| Adult | 22% | 1% | 20% | -- | ~43% |
| Dislocated Worker | 22% | 9% | 16% | -- | ~47% |
| Youth | 12% | 9% | 21% | -- | ~42% |

- **Required** has only one segment: a single dark navy bar labeled "80%"
- **Adult, Dislocated Worker, Youth** each have 3 stacked segments (green
  bottom, yellow middle, blue top) with percentage labels on each segment
- All percentage labels are placed inside or adjacent to their segment

### Verifiable Facts [-> Correctness]

- FACT: The chart title reads "Obligations, Accrual & Expense Breakdown"
- FACT: There are exactly 4 x-axis categories: Required, Adult, Dislocated
  Worker, Youth
- FACT: The legend contains exactly 4 entries
- FACT: The Required category has a single dark navy bar at 80%
- FACT: Adult segments are 22% (green), 1% (yellow), 20% (blue)
- FACT: Dislocated Worker segments are 22% (green), 9% (yellow), 16% (blue)
- FACT: Youth segments are 12% (green/bottom), 9% (yellow), 21% (blue)
- FACT: The y-axis ranges from 0% to 90% in 10% increments
- FACT: Gray dashed horizontal gridlines appear at each 10% mark
- FACT: The Required bar is the tallest at 80%
- FACT: Dislocated Worker has the tallest stacked bar among the 3 program
  categories (~47%)
- FACT: Adult and Dislocated Worker share the same Expense Actual % value
  (22%)

### Hallucination Risks [-> Correctness]

- RISK: Calling this a "grouped bar chart" (as the catalog does)
  REALITY: This is a stacked bar chart -- segments are stacked vertically
  within each category, not arranged side by side
- RISK: Claiming 12 data series are visible (as the catalog states)
  REALITY: Only 4 legend entries are visible; the "12 series" likely refers
  to internal XLSX XML definitions
- RISK: Confusing the Obligations Actual % (blue) with Obligations & Expense
  Required % (dark navy) -- both are blue-family colors
  REALITY: Dark navy appears only in the Required category; medium blue
  appears in the 3 program categories
- RISK: Stating that the Required category has stacked segments like the
  others
  REALITY: Required has only one segment (dark navy at 80%)
- RISK: Misreading the Youth bottom segment color as blue instead of green
  REALITY: The bottom segment in all 3 program categories represents Expense
  Actual % (green), though the Youth segment appears slightly different in
  shade due to its smaller size
- RISK: Inventing values for segments that are not labeled (e.g., claiming
  Required has an Obligations Actual % segment)
  REALITY: Only labeled segments are visible; Required shows only 80% navy

### Detail Inventory [-> Information Recovery]

- Chart title text: "Obligations, Accrual & Expense Breakdown"
- All 4 legend entries with exact text and color descriptions
- All 10 labeled data values (1 for Required + 3 each for Adult, DW, Youth)
- Y-axis gridlines at every 10% interval from 0% to 90%
- X-axis category labels including "Dislocated Worker" wrapping to two lines
- Stacking order: green (bottom), yellow (middle), blue (top)
- The single-segment pattern for Required vs three-segment pattern for others
- Chart border style (thin black line)
- White background
- The approximate total heights of each stacked bar

### Domain Context [-> Retrieval Value]

This chart appears on the dashboard sheet of an Illinois WorkNet WIOA
(Workforce Innovation and Opportunity Act) formula grant budget template. It
shows how actual obligations, accruals, and expenses compare to required
percentages across four funding categories: a combined Required threshold
(80%), and three program streams (Adult, Dislocated Worker, Youth).

The 80% Required bar represents the minimum obligation threshold that local
workforce boards must meet by June 30 to avoid losing grant funds. The three
program category bars break down actual financial activity into obligations
(committed funds), accruals (incurred costs), and expenses (paid costs).

WIOA is the primary federal workforce development law in the United States,
funding job training, education, and employment services through state and
local boards.

### Search Keywords [-> Retrieval Value]

WIOA, Workforce Innovation and Opportunity Act, Illinois WorkNet, obligations,
accruals, expenses, formula grant, budget dashboard, stacked bar chart, Adult
program, Dislocated Worker, Youth program, required percentage, workforce
board, financial breakdown

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "Bar chart showing budget percentages" -- no category names, no values cited. Or: misidentifies chart type as grouped rather than stacked, invents a segment value not shown, or swaps stacking order. All 10 percentage labels are printed text requiring exact match; fabricating a value triggers the hallucination cap. | Correctly identifies stacked bar chart with 4 categories, names Required at 80%, and reports most segment values accurately. May get one secondary value wrong or confuse which series is yellow vs green. | All 10 labeled values exact (Required 80%; Adult 22%/1%/20%; DW 22%/9%/16%; Youth 12%/9%/21%). Stacking order correct (green bottom, yellow middle, blue top). Required single-segment pattern distinguished from 3-segment others. All 4 legend entries named correctly. No fabricated values. |
| Information Recovery | Identifies as a bar chart with percentages. Names 1-2 categories, 2-3 values. A search for "Dislocated Worker obligations" or "Youth expense percentage" would not match. Most of the 10 data values invisible to the system. | All 4 categories named, all 4 legend entries identified, most of the 10 values extracted. Stacking pattern described. "Adult 22% expense" would match. May miss the single-segment Required vs 3-segment pattern. | All 10 percentage values recovered across all 4 categories. Legend entries with color assignments documented. Stacking order and segment pattern captured. Any value visible in the chart is findable -- parity principle met. |
| Retrieval Value | "A financial chart" -- no domain vocabulary, not self-contained. Would not surface for "WIOA obligations" or "workforce board budget." | "WIOA formula grant obligations and expenses breakdown from Illinois workforce dashboard" -- contains key domain terms. Partially self-contained but doesn't explain what the 80% threshold means. | Natural prose explaining WIOA obligation/accrual/expense breakdown for Adult, Dislocated Worker, and Youth program streams. Notes the 80% required threshold. Domain vocabulary embedded (WIOA, formula grant, obligations, accruals, expenses). Self-contained. Findable by "WIOA budget breakdown" or "workforce board expenditure." |

<br><br>

## doc20-C03 -- Pie: Total WIOA Formula Grant Budget

**Content type:** chart-simple
**Annotation difficulty:** Easy

### Visual Inventory [-> Information Recovery]

- **Chart type:** Pie chart with 5 segments
- **Title (two lines):** "Total WIOA Formula Grant Budget" / "(Amounts in
  Thousands)"
- **Chart border:** Thin black line enclosing the chart area
- **Background:** White
- **Segments (clockwise from ~12 o'clock):**
  1. **Admin** -- gray, labeled "Admin 12%" inside the segment
  2. **Youth In School** -- small orange/tan slice, labeled "Youth In School
     5%" with a leader line extending to the right outside the pie (slice is
     slightly exploded/pulled out)
  3. **Youth Out of School** -- large orange segment, labeled "Youth Out of
     School 31%" inside the segment
  4. **Adult** -- yellow/gold, labeled "Adult 23%" inside the segment
  5. **Dislocated Worker** -- blue, labeled "Dislocated Worker 30%" inside
     the segment
- **Label style:** Each segment has its category name and percentage either
  inside the slice or (for the smallest segment) pulled out with a leader
  line
- **No separate legend** -- labels are placed directly on or adjacent to each
  segment

**Adjacent context (outside chart border):** A summary table to the right of
the chart on the dashboard shows dollar amounts: Admin $900, Youth In School
$375, Youth Out of School $2,370, Adult $1,740, Dislocated Worker $2,335,
Total $7,720. This table is NOT part of the chart object itself.

### Verifiable Facts [-> Correctness]

- FACT: The chart title reads "Total WIOA Formula Grant Budget (Amounts in
  Thousands)"
- FACT: There are exactly 5 pie segments
- FACT: Admin = 12% (gray)
- FACT: Youth In School = 5% (orange/tan, smallest segment, with leader line)
- FACT: Youth Out of School = 31% (orange, largest segment)
- FACT: Adult = 23% (yellow/gold)
- FACT: Dislocated Worker = 30% (blue)
- FACT: The percentages sum to 101% (rounding artifact: 12+5+31+23+30=101)
- FACT: Youth Out of School (31%) is the largest segment
- FACT: Youth In School (5%) is the smallest segment
- FACT: Dislocated Worker (30%) and Youth Out of School (31%) are nearly
  equal, together comprising 61% of the budget
- FACT: There is no separate legend box; labels are on/near each segment

### Hallucination Risks [-> Correctness]

- RISK: Claiming the percentages sum to exactly 100%
  REALITY: They sum to 101% due to rounding (each individual percentage is
  rounded to the nearest integer)
- RISK: Confusing "Youth In School" and "Youth Out of School" segments or
  swapping their values
  REALITY: Youth Out of School (31%, orange, large) is the biggest segment;
  Youth In School (5%, small, with leader line) is the smallest
- RISK: Reporting dollar amounts from the adjacent summary table as if they
  are part of the chart
  REALITY: The chart shows only percentages; the dollar table is a separate
  spreadsheet element
- RISK: Stating that "Amounts in Thousands" means the percentages are in
  thousands
  REALITY: The subtitle refers to the dollar amounts in the adjacent table;
  the pie segments show percentages
- RISK: Describing additional segments not present (e.g., "Other" or
  "Overhead")
  REALITY: Exactly 5 segments are shown

### Detail Inventory [-> Information Recovery]

- Full two-line title text
- All 5 segment names and percentages
- Color of each segment (gray, orange/tan, orange, yellow/gold, blue)
- The Youth In School segment is slightly exploded with a leader line
- All other labels are positioned inside their segments
- The 101% rounding sum
- No legend box present
- Thin black chart border
- White background
- Clockwise ordering from Admin at ~12 o'clock

### Domain Context [-> Retrieval Value]

This pie chart shows the budget allocation for a WIOA (Workforce Innovation
and Opportunity Act) formula grant administered by the Illinois Workforce
Board. The five segments represent the major funding streams: administrative
overhead (Admin, 12%), two youth programs (In School 5%, Out of School 31%),
Adult services (23%), and Dislocated Worker services (30%).

The adjacent summary table (not part of the chart) shows the total grant
budget is $7,720 thousand ($7.72 million). The "Amounts in Thousands"
subtitle refers to these dollar values. Youth Out of School ($2,370K) and
Dislocated Worker ($2,335K) together receive over 60% of the funding.

The dashboard is a template for local workforce boards to report to the state
on their WIOA formula grant spending. Data is reported as of 3/31/2021 for
a 2-year grant period from 7/1/2020 to 6/30/2022.

### Search Keywords [-> Retrieval Value]

WIOA, Workforce Innovation and Opportunity Act, formula grant, budget
allocation, pie chart, Illinois WorkNet, Admin, Youth In School, Youth Out
of School, Adult, Dislocated Worker, workforce board, budget dashboard,
grant budget breakdown

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "Pie chart of a budget with 5 colored slices" -- no segment names or values. Or: confuses "Youth In School" with "Youth Out of School" (common error), or states percentages sum to 100% when they actually sum to 101% due to rounding. All labels are printed text; fabricating a segment name or value triggers the hallucination cap. | All 5 segments named with correct values (31%, 30%, 23%, 12%, 5%). May confuse which Youth segment is which or miss the rounding artifact. | All 5 segments exact: Youth Out of School 31%, Dislocated Worker 30%, Adult 23%, Admin 12%, Youth In School 5%. Notes 101% rounding sum. Full title with subtitle "(Amounts in Thousands)." Correctly distinguishes chart from adjacent table text. No fabricated segments. |
| Information Recovery | Identifies as a pie chart with a few segments. Names 2-3 segments. A search for "Admin 12%" or "Youth Out of School allocation" would not match. | All 5 segments named with values. Title captured. Largest/smallest segments identified. "Dislocated Worker 30%" would match. May miss the subtitle or the rounding observation. | All 5 segments with names, values, and colors recovered. Full title including subtitle. Leader line on smallest segment noted. Segment ordering documented. Any budget allocation visible in the chart is findable -- parity principle met. |
| Retrieval Value | "Budget pie chart" -- not self-contained. Would not surface for "WIOA formula grant" or "workforce funding streams." | "WIOA formula grant budget breakdown from Illinois workforce dashboard" -- searchable domain terms. Partially self-contained but doesn't explain the 5 funding streams. | Natural prose explaining the 5 WIOA funding streams (Adult, Dislocated Worker, Youth In/Out of School, Admin) and their budget shares. Domain vocabulary embedded (WIOA, formula grant, workforce board). Self-contained. Findable by "WIOA budget allocation" or "workforce grant breakdown." |

<br><br>

## doc20-C04 -- Grouped bar: Direct Training

**Content type:** chart-simple
**Annotation difficulty:** Easy

### Visual Inventory [-> Information Recovery]

- **Chart type:** Grouped bar chart with 3 categories and 4 data series
- **Title:** "DIRECT TRAINING" (all caps, bold, centered at top)
- **Y-axis:** 20% to 65% in 5% increments with gray dashed horizontal
  gridlines; axis does NOT start at 0%
- **X-axis categories (left to right):**
  1. Adult
  2. Dislocated Worker
  3. Adult and Dislocated Worker Combined (wraps to two lines)
- **Legend (below chart, 4 entries, each with colored rectangle + text):**
  1. Required Percentage -- dark navy (with yellow/gold horizontal stripe
     in the swatch)
  2. Adult Actual Direct Training Percentage -- yellow/gold (with light
     blue horizontal stripe in the swatch)
  3. Dislocated Worker Actual Direct Training Percentage -- light blue
     (with yellow/gold horizontal stripe in the swatch)
  4. Combined Adult & Dislocated Worker -- dark green/olive (with yellow/gold
     horizontal stripe in the swatch)
- **Chart border:** Thin black line enclosing the plot area
- **Background:** White

**Bar data:**

| Category | Required % (navy) | Actual % (color) | Actual series |
|----------|-----------|---------|---------------|
| Adult | 50% | 61.0% (yellow/gold) | Adult Actual Direct Training |
| Dislocated Worker | 50% | 60.8% (light blue) | DW Actual Direct Training |
| Combined | 50% | 60.9% (dark green) | Combined Adult & DW |

- Each category has exactly 2 side-by-side bars: Required (navy, left) and
  one category-specific actual bar (right)
- All data labels appear above their respective bars
- All three Required bars are identical at 50%

### Verifiable Facts [-> Correctness]

- FACT: The chart title reads "DIRECT TRAINING" in all caps
- FACT: There are exactly 3 x-axis categories
- FACT: All 3 Required Percentage bars are at exactly 50%
- FACT: Adult Actual Direct Training is 61.0% (yellow/gold bar)
- FACT: Dislocated Worker Actual Direct Training is 60.8% (light blue bar)
- FACT: Combined Adult & Dislocated Worker is 60.9% (dark green bar)
- FACT: The y-axis starts at 20%, not 0%
- FACT: The y-axis goes up to 65% in 5% increments
- FACT: Each category has exactly 2 bars side by side
- FACT: All 3 actual percentages exceed the 50% required threshold
- FACT: The legend contains exactly 4 entries
- FACT: The actual percentages are very close together (61.0%, 60.8%, 60.9%)

### Hallucination Risks [-> Correctness]

- RISK: Claiming the y-axis starts at 0%
  REALITY: The y-axis starts at 20%, exaggerating the visual difference
  between the Required (50%) and Actual (~61%) bars
- RISK: Stating there are 4 bars per category (one per legend entry)
  REALITY: Only 2 bars appear per category -- the Required bar plus the
  one applicable actual bar. Each actual series applies to only one category
- RISK: Reading the actual values as whole numbers (61%, 61%, 61%) instead
  of the precise labeled values (61.0%, 60.8%, 60.9%)
  REALITY: All three actual bars have one-decimal-place labels
- RISK: Describing this as a stacked bar chart
  REALITY: The bars are side by side (grouped), not stacked
- RISK: Claiming the Combined value is the average or sum of Adult and DW
  REALITY: Combined (60.9%) is between Adult (61.0%) and DW (60.8%), which
  is consistent with a weighted average, but the chart does not state this

### Detail Inventory [-> Information Recovery]

- Chart title text and style (all caps, bold)
- All 3 category labels including the two-line wrap on the third
- All 6 bar values (3 at 50%, plus 61.0%, 60.8%, 60.9%)
- 4 legend entries with full text names
- Color assignments: navy (Required), yellow/gold (Adult), light blue (DW),
  dark green (Combined)
- Y-axis range (20%-65%) and gridlines at 5% intervals
- The truncated y-axis not starting at 0%
- Data labels positioned above each bar
- The legend swatch pattern (each has a striped appearance with mixed colors)
- Chart border style
- 2 bars per category layout

### Domain Context [-> Retrieval Value]

This chart appears in the Direct Training section of the Illinois WorkNet
WIOA dashboard. WIOA requires that by June 30, at least 50% of the combined
Adult and Dislocated Worker actual expenditures from prior year grant funds
and current year grant funds be spent on Direct Training.

The 50% Required bars represent this regulatory threshold. All three actual
percentages (61.0% Adult, 60.8% DW, 60.9% Combined) exceed the 50%
requirement, indicating the local workforce board is meeting the direct
training expenditure mandate.

Direct Training refers to training services provided directly to participants,
as opposed to supportive services, administrative costs, or case management.

### Search Keywords [-> Retrieval Value]

WIOA, direct training, workforce board, required percentage, Adult program,
Dislocated Worker, combined expenditure, grouped bar chart, training
expenditure, Illinois WorkNet, 50 percent requirement, actual vs required,
formula grant compliance

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "Bar chart showing training data around 50-60%" -- no specific values, no category names. Or: misreads 60.8% as 60.0%, confuses grouped with stacked layout, or fails to note the y-axis starts at 20% (not 0%), which exaggerates visual differences. Labeled values (50%, 61.0%, 60.8%, 60.9%) require exact match; fabricating a value triggers the hallucination cap. | Correctly identifies grouped bar chart, names all 3 categories, reports Required at 50% and approximate actual values. Notes the comparison structure (required vs actual). May miss the truncated y-axis or one decimal place. | All 6 values exact: Adult 50%/61.0%, DW 50%/60.8%, Combined 50%/60.9%. Notes y-axis starts at 20% (truncated). Grouped (not stacked) layout correctly identified. All 4 legend entries named. No fabricated values. |
| Information Recovery | Identifies as a bar chart about training percentages. Names 1-2 categories. A search for "Dislocated Worker direct training" or "61.0% actual" would not match. | All 3 categories named, both bars per category described (required vs actual). Legend entries identified. "Adult 61.0% direct training" would match. May miss the truncated axis or one of the decimal-precise values. | All 6 values recovered with decimal precision. 3-category grouped structure documented. All 4 legend entries with full names. Required-vs-actual comparison pattern captured. Truncated y-axis noted. Any value visible in the chart is findable -- parity principle met. |
| Retrieval Value | "A training chart" -- no domain vocabulary, not self-contained. Would not surface for "WIOA direct training" or "workforce expenditure compliance." | "WIOA direct training expenditure compliance chart showing actual vs required percentages" -- searchable domain terms. Partially self-contained. | Natural prose explaining the WIOA 50% direct training requirement and that all categories exceed it. Domain vocabulary embedded (WIOA, direct training, required percentage, compliance). Self-contained. Findable by "WIOA direct training compliance" or "workforce board training expenditure." |

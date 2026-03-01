# Image Analysis: Doc 12 -- 12_minnstate_fy2025_budget.pptx

**Document:** `12_minnstate_fy2025_budget.pptx`
**Format:** PPTX
**Source:** https://www.minnstate.edu/system/finance/budget/docs/fy2025-operating-budget-second-reading-june-2024-final.pptx
**Category:** multi-image
**Images:** 1
**Document context:** Minnesota State FY2025 operating budget presentation
covering revenue allocation, tuition projections, North Star Promise Program
financial awards, and system-wide budget priorities.

<br><br>

## doc12-R03 -- North Star Promise Program financial table

**Figure reference:** Table 9
**Content type:** table-image
**Annotation difficulty:** Medium
**Dimensions:** (embedded PPTX image)

### Visual Inventory [-> Information Recovery]

- **Image type:** Financial data table rendered as an embedded image in PPTX
- **Title:** "Table 9: North Star Promise Program Projected Awards, Fiscal
  Year 2025" (bold, black text, centered above the table)
- **Table structure:** 4 columns, 1 header row, 5 data rows (4 institutions
  + 1 total row)
- **Column headers (dark navy/teal background, white bold text):**
  1. System
  2. Projected Student Count
  3. Projected Average Award
  4. Projected Total Awards
- **Data rows (alternating white and light gray backgrounds):**
  1. Minnesota State Colleges | 3,800 | $1,260 | $4,779,000
  2. Minnesota State Universities | 2,900 | $2,120 | $6,149,500
  3. University of Minnesota | 4,400 | $2,790 | $12,273,900
  4. Tribal Institutions | 10 | $1,660 | $16,600
  5. Total | 11,000 | $2,110 | $23,218,800
- **Text alignment:** Institution names left-aligned; numeric columns
  right-aligned
- **Number formatting:** Student counts use comma separators (3,800).
  Dollar amounts use $ prefix with comma separators ($1,260; $4,779,000)
- **Row separators:** Thin light gray horizontal lines between rows
- **Table border:** Thin outer border
- **Background:** White with alternating light gray row shading
- **Dimensions:** Approximately 1009x451 pixels

### Verifiable Facts [-> Correctness]

- FACT: The table title reads "Table 9: North Star Promise Program Projected
  Awards, Fiscal Year 2025"
- FACT: There are exactly 4 columns and 6 rows (1 header + 5 data)
- FACT: The 4 institution categories are: Minnesota State Colleges,
  Minnesota State Universities, University of Minnesota, Tribal Institutions
- FACT: The Total row shows: 11,000 students, $2,110 average award,
  $23,218,800 total awards
- FACT: University of Minnesota has the highest projected student count
  (4,400) and highest total awards ($12,273,900)
- FACT: Tribal Institutions has the lowest count (10) and lowest total
  ($16,600)
- FACT: The header row has a dark navy/teal background with white text
- FACT: All dollar amounts use the $ prefix
- FACT: The average award column ranges from $1,260 to $2,790
- FACT: 3,800 + 2,900 + 4,400 + 10 = 11,110, not 11,000 -- the Total row
  value (11,000) appears to be a rounded figure

### Hallucination Risks [-> Correctness]

- RISK: Assuming the student counts sum exactly to the Total
  REALITY: 3,800 + 2,900 + 4,400 + 10 = 11,110, but the Total row shows
  11,000. This 110-student discrepancy suggests the Total is independently
  rounded or projected, not a simple sum of the rows above
- RISK: Calculating Average Award as Total Awards / Student Count for each
  row
  REALITY: The values are close but not exact matches due to rounding:
  $4,779,000 / 3,800 = $1,257.63 (shown as $1,260). The table uses rounded
  projections, not precise calculations
- RISK: Describing the header background as "blue" or "black"
  REALITY: The header background appears to be a dark navy/teal color,
  consistent with Minnesota State branding
- RISK: Missing the Total row and describing only 4 data rows
  REALITY: There are 5 data rows: 4 institutions + 1 Total summary row

### Detail Inventory [-> Information Recovery]

- Title: bold black text, centered, serif or sans-serif font
- Header background: dark navy/teal (#003B5C approximate, Minnesota State
  brand color)
- Header text: white, bold, multi-line (column headers wrap to 2-3 lines)
- Data text: black, regular weight
- System column: left-aligned, centered vertically
- Numeric columns: right-aligned
- Alternating row shading: white and light gray (#F5F5F5 approximate)
- Thin gray row separators
- Dollar formatting: $X,XXX or $XX,XXX,XXX with commas
- Student counts: X,XXX with commas
- Image dimensions: 1009x451 pixels
- Clean, professional formatting consistent with government/education
  budget presentations

### Domain Context [-> Retrieval Value]

The North Star Promise Program is Minnesota's tuition-free college program
for eligible students from families with adjusted gross income at or below
$80,000. Enacted in 2023, it provides "last-dollar" scholarships covering
remaining tuition and fees after other financial aid.

This table from the FY2025 operating budget presentation shows projected
financial awards across four Minnesota higher education systems:
- Minnesota State system (colleges + universities): 6,700 students,
  ~$10.9M
- University of Minnesota: largest single system (4,400 students, $12.3M)
- Tribal Institutions: smallest allocation (10 students, $16,600)

The total projection of $23.2M across 11,000 students with an average
award of $2,110 reflects the "last-dollar" nature -- students who already
receive significant federal/state aid get smaller North Star awards to
fill the remaining gap.

The varying average awards ($1,260 for State Colleges vs. $2,790 for
U of M) reflect the higher tuition at university-level institutions.

### Search Keywords [-> Retrieval Value]

North Star Promise, Minnesota State, tuition-free college, FY2025 budget,
projected awards, financial aid, student count, average award, University
of Minnesota, Tribal Institutions, operating budget, higher education
funding

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | Misquotes dollar values (e.g. "$4,799,000" for $4,779,000) or invents a fifth institution row not in the table. Misreading any labeled cell value is a precision error; fabricating an institution name (e.g. "Minnesota Technical Colleges") triggers the hallucination cap. The row-sum discrepancy (3,800+2,900+4,400+10 = 11,110 vs stated 11,000) is a genuine table feature -- calling it an "error" is itself an error. | All 20 cell values correct, title accurate. May round $4,779,000 to "$4.8M" or $12,273,900 to "$12.3M" without noting the exact figures. Student count totals not cross-checked. | Every cell value exact as labeled (3,800 / $1,260 / $4,779,000 through Total 11,000 / $2,110 / $23,218,800). Notes the arithmetic discrepancy in student counts (11,110 vs 11,000) as a table feature, not an error. Tolerance: zero for labeled text values -- all numbers are explicitly printed. |
| Information Recovery | Identifies the table topic but recovers fewer than half of the 20 data cells. A search for "Tribal Institutions" or "$12,273,900" would fail. Missing column headers or institution names makes the data unqueryable. | All 4 institution names and totals row recovered. Most dollar values present but some cells omitted (e.g. Projected Average Award column skipped). A search for any institution name would match, but specific per-institution values may be missing. | All 20 cell values recovered across 4 columns and 5 rows. Full title including "Table 9" and "Fiscal Year 2025." Every institution-column intersection is queryable: a search for "$6,149,500" or "Tribal Institutions 10 students" returns a match. Parity met -- the annotation is as queryable as the original table. |
| Retrieval Value | Raw data dump listing numbers without table structure or program context. Depends on knowing this comes from a Minnesota budget presentation. Not self-contained as a standalone reference. | Self-contained summary: "North Star Promise Program FY2025 projected awards across 4 institution types, totaling $23.2M for 11,000 students." Structured as a readable table. Missing context about what North Star Promise is or why average awards vary by institution. | Self-contained, structured annotation with full table reproduction. Embeds domain context: North Star Promise as a tuition-free college program, last-dollar aid model explaining why higher-tuition institutions show higher average awards ($2,790 U of M vs $1,260 State Colleges). Findable by queries like "Minnesota tuition-free program budget" or "North Star Promise FY2025 projections." |

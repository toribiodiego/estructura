# Image Analysis: Doc 14 -- 14_simple_table.png

**Document:** `14_simple_table.png`
**Format:** PNG
**Source:** https://raw.githubusercontent.com/eihli/image-table-ocr/master/resources/test_data/simple.png
**Category:** table-image
**Images:** 1
**Document context:** Standalone image of a simple spreadsheet table used as a
test fixture for table OCR systems. Contains cell references, format
descriptions, and formulas.

<br><br>

## doc14-R01 -- Spreadsheet cell/format/formula table

**Figure reference:** (standalone image)
**Content type:** table-image
**Annotation difficulty:** Easy
**Dimensions:** (full image)

### Visual Inventory [-> Information Recovery]

- **Image type:** Spreadsheet reference table describing cell formats and
  formulas
- **Table structure:** 3 columns, 1 header row, 5 data rows
- **Column headers (bold black text, light gray background):**
  1. Cell
  2. Format
  3. Formula
- **Data rows:**
  1. B4 | Percentage | None
  2. C4 | General | None
  3. D4 | Accounting | None
  4. E4 | Currency | =PMT(B4/12,C4,D4)
  5. F4 | Currency | =E4*C4
- **Styling:**
  - Header row: light gray background (#E8E8E8 approximate), bold text
  - Data rows: white background, regular weight black text
  - Black border lines separating all cells (1px solid)
  - Left-aligned text in all columns
  - Sans-serif font (appears to be Arial or similar)
- **Background:** White with a subtle light gray margin at top
- **No title, legend, or additional annotations**

### Verifiable Facts [-> Correctness]

- FACT: The table has exactly 3 columns: Cell, Format, Formula
- FACT: There are exactly 5 data rows (B4 through F4)
- FACT: Cell references are B4, C4, D4, E4, F4 (all in row 4, columns B-F)
- FACT: Format types used: Percentage, General, Accounting, Currency (Currency
  appears twice)
- FACT: Three cells have "None" as their formula (B4, C4, D4)
- FACT: E4 contains formula =PMT(B4/12,C4,D4)
- FACT: F4 contains formula =E4*C4
- FACT: The PMT function takes 3 arguments: B4/12, C4, and D4
- FACT: All cell references are in column 4 (row 4 of a spreadsheet)

### Hallucination Risks [-> Correctness]

- RISK: Assuming this table shows actual cell values or computed results
  REALITY: The table only shows cell references, their format types, and
  formulas. No numerical values or results are displayed.
- RISK: Interpreting the PMT formula arguments incorrectly
  REALITY: =PMT(B4/12,C4,D4) is the exact formula shown. B4/12 divides cell
  B4 by 12 (monthly rate from annual), C4 is the second argument (number of
  periods), D4 is the third (present value/loan amount).
- RISK: Describing additional rows or columns not visible
  REALITY: Only 5 rows and 3 columns are shown. The spreadsheet may have more
  content but only this portion is captured.
- RISK: Calling this a "financial report" or "loan calculator output"
  REALITY: This is a metadata reference table (cell/format/formula), not a
  spreadsheet showing computed values. It is used as a test fixture for table
  OCR systems.

### Detail Inventory [-> Information Recovery]

- Table dimensions: 3 columns x 6 rows (including header)
- Header: bold text, light gray background
- Data cells: regular weight, white background
- Border: black solid lines (1px) on all cell edges
- Font: sans-serif (Arial or similar), black text
- Cell column: short values (2 chars each: B4-F4)
- Format column: single words (Percentage, General, Accounting, Currency)
- Formula column: "None" or spreadsheet formulas with = prefix
- Overall: clean, simple layout with no color coding or merged cells
- Small image, high contrast, easy to read

### Domain Context [-> Retrieval Value]

This is a test fixture image from the `image-table-ocr` GitHub project
(eihli/image-table-ocr), used to test optical character recognition of
tabular data in images. The table documents a spreadsheet layout for a
loan payment calculation:

- **B4** (Percentage): Annual interest rate
- **C4** (General): Number of payment periods
- **D4** (Accounting): Loan principal/present value
- **E4** (Currency): Monthly payment via PMT function
  - PMT(rate, nper, pv) computes a fixed periodic payment for a loan
  - B4/12 converts annual rate to monthly rate
- **F4** (Currency): Total cost = monthly payment * number of periods

The PMT function is a standard Excel/spreadsheet financial function. This
table describes the structure of a simple loan amortization worksheet.

### Search Keywords [-> Retrieval Value]

spreadsheet, table, cell reference, format, formula, PMT function, loan
payment, percentage, currency, accounting, Excel, OCR test fixture,
table-image, simple table

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A table with cells and formulas" (no specific values or structure) | "3-column table (Cell/Format/Formula) with 5 rows. Cells B4-F4 with formats (Percentage, General, Accounting, Currency) and formulas (None, =PMT(B4/12,C4,D4), =E4*C4)." | "3x6 table (header + 5 rows): B4 Percentage None, C4 General None, D4 Accounting None, E4 Currency =PMT(B4/12,C4,D4), F4 Currency =E4*C4. PMT takes 3 args: monthly rate (B4/12), periods (C4), principal (D4). Currency format used twice. No computed values shown -- this is a metadata reference table." |
| Specificity | "Black text in a bordered table" | "Bold header row on gray background. Sans-serif font, black borders, white data cells. Left-aligned text." | "Light gray header (#E8E8E8), 1px solid black borders, sans-serif font (Arial-like), bold headers, regular data weight. Left-aligned all columns. White data backgrounds. No color coding, no merged cells. Clean high-contrast rendering." |
| Completeness | "A spreadsheet table" (misses column names, cell values, formulas) | "3 columns, 5 data rows, all cell refs (B4-F4), all formats, all formulas listed. Header styling noted." | "All 3 column headers, all 5 data rows with exact values. Header styling (gray, bold). Data styling (white, regular). Border style. Font type. No title. Light gray top margin. OCR test fixture context. Image is standalone PNG from GitHub." |
| Usefulness | "A simple table image" | "Spreadsheet cell metadata table for a loan calculation. PMT function computes monthly payment. Used as OCR test fixture from image-table-ocr project." | "OCR test fixture from eihli/image-table-ocr. Documents a loan amortization worksheet: B4=annual rate, C4=periods, D4=principal, E4=PMT(monthly rate, periods, principal), F4=total cost (payment*periods). PMT is standard Excel financial function. Table shows metadata (format+formula) not computed values." |

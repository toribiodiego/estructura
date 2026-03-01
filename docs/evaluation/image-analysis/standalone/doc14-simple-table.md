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
| Correctness | "A table with cells and formulas" -- no column names, no cell references, no formula text. Or: misreads the PMT formula (e.g., =PMT(B4,C4,D4) instead of =PMT(B4/12,C4,D4), missing the /12 divisor). All values are labeled text requiring exact match; any fabricated cell reference or formula triggers the hallucination cap. | Correctly names all 3 columns, all 5 cell references (B4-F4), all format types, and both formulas. Minor error like misidentifying the number of "None" entries (says 2 instead of 3). | All values exact: B4 Percentage None, C4 General None, D4 Accounting None, E4 Currency =PMT(B4/12,C4,D4), F4 Currency =E4*C4. Notes Currency appears twice. Notes this shows metadata (format+formula), not computed values. No fabricated content. |
| Information Recovery | Identifies image as a table with formulas. No cell references, no format types, no formula text extracted. A search for "PMT function" or "B4 Percentage" would not match. | All 5 cell references named, all format types listed, both formulas quoted. Column structure documented. A search for "PMT(B4/12,C4,D4)" would match. May miss that the table is metadata vs computed values. | Complete recovery of all 15 cell values (5 rows x 3 columns). Table structure documented (3 columns, header + 5 rows). PMT arguments identified (monthly rate, periods, principal). Metadata-vs-computed distinction noted. Any cell value visible in the image is findable in the annotation. |
| Retrieval Value | "A simple table image" -- no domain vocabulary, not self-contained. Would not surface for queries about loan calculations, PMT function, or spreadsheet formulas. | Identifies this as a spreadsheet cell metadata table for a loan calculation. PMT function mentioned. Partially self-contained but doesn't explain what the cells represent. | Natural prose explaining this is an OCR test fixture documenting a loan amortization worksheet: B4=annual rate, C4=periods, D4=principal, E4=monthly payment via PMT, F4=total cost. Domain vocabulary embedded (PMT, loan amortization, cell reference). Fully self-contained. Findable by "spreadsheet PMT formula" or "loan payment calculation". |

# Image Analysis: Doc 06 -- 06_arxiv_2206_01062.pdf

**Document:** `06_arxiv_2206_01062.pdf`
**Format:** PDF
**Source:** https://arxiv.org/pdf/2206.01062.pdf
**Category:** multi-image
**Images:** 22
**Document context:** DocLayNet paper introducing a large-scale document layout
analysis dataset with 80K+ annotated pages across 6 document categories.
Covers annotation methodology, dataset statistics, and layout prediction
benchmarks.

<br><br>

## doc06-R07 -- CCS annotation UI with bounding boxes

**Figure reference:** Figure 3, page 4
**Content type:** screenshot
**Annotation difficulty:** Medium
**Dimensions:** 1120x1512 pixels

### Visual Inventory

Screenshot of the Corpus Conversion Service (CCS) annotation user interface.
The left side shows a document page rendered with semi-transparent colored
bounding boxes overlaid on text and figure regions. Each bounding box has small
"X" close buttons at its corners. The right side shows a "Clusters" label
palette listing 13 annotation categories, each with a colored indicator dot and
a rounded-rectangle button. The bottom of the interface has action buttons
(Skip, Filter, Submit) on the left and a "Report problem" button on the right.
Caption below the screenshot reads: "Figure 3: Corpus Conversion Service
annotation user interface."

### Verifiable Facts

- **Label palette (right panel):** 13 categories listed under "Clusters" heading:
  1. Text (yellow dot)
  2. Picture (pale yellow/cream dot)
  3. Formula (dark blue/navy dot)
  4. Code (pink/magenta dot)
  5. Complex-form (light cyan dot)
  6. Section-header (red dot)
  7. Page-footer (teal dot)
  8. Page-header (green dot)
  9. Footnote (dark green dot)
  10. Table (salmon/coral dot)
  11. Caption (gold/dark yellow dot)
  12. List-item (blue dot)
  13. Title (red dot)
- **Bounding boxes on the document page (top to bottom):**
  - Multiple blue/hatched boxes at top: text regions with horizontal blue
    striping pattern
  - Yellow/hatched box: a region in the middle area (likely text or formula)
  - Pink/red hatched boxes: regions below center (likely section headers or
    highlighted text areas)
  - Purple/dashed boxes: two figure regions at lower portion containing a bar
    chart and a pie chart
  - Thin blue box at bottom: a narrow region (possibly caption or list-item)
- **Action buttons at bottom:** "Skip" (blue), "Filter" (blue), "Submit" (blue)
  on the left; "Report problem" (outlined) on the right
- Each bounding box has corner/edge "X" dismiss controls
- The document content behind the overlays includes text paragraphs, a bar
  chart, and a pie chart
- Caption: "Figure 3: Corpus Conversion Service annotation user interface. The
  PDF page is shown in the background, with overlaid text-cells (in darker
  shades). The annotation boxes can be drawn by dragging a rectangle over each
  segment with the respective label from the palette on the right."

### Hallucination Risks

- **Exact label-to-box mapping:** The colored overlays on the document page do
  not have explicit labels. An annotator might incorrectly assign specific
  category names to specific bounding boxes based on color matching, but the
  overlay colors (with cross-hatch patterns) do not precisely match the small
  palette dots.
- **Document content behind overlays:** The underlying page content is partially
  obscured by the colored overlays. An annotator might describe content that is
  not actually visible or readable through the overlay.
- **Number of bounding boxes:** The exact count of distinct bounding boxes is
  difficult to determine because some boxes overlap or are nested. An annotator
  might miscount.
- **UI element text:** Some UI elements may be too small to read definitively in
  the screenshot. An annotator might guess at button labels or menu items.

### Detail Inventory

- **Interface layout:** Two-panel design -- document viewer (left, ~70% width)
  and label palette (right, ~30% width)
- **Document viewer:** White background with the PDF page centered; bounding
  boxes rendered as semi-transparent colored rectangles with cross-hatch or
  stripe fill patterns
- **Bounding box styles:** Each box has a distinct color fill with a pattern
  overlay (horizontal stripes or cross-hatch); small square "X" buttons at
  corners for deletion
- **Palette design:** Vertical list of rounded-rectangle buttons, each
  containing a small colored square indicator and category name text; heading
  "Clusters" at top
- **Bottom toolbar:** Three blue buttons (Skip, Filter, Submit) aligned left;
  one outlined button (Report problem) aligned right
- **Visible document content:** The underlying page appears to be a research
  paper page with text paragraphs, a simple bar chart (4-5 bars in pink/red),
  and a multi-colored pie chart

### Domain Context

- CCS (Corpus Conversion Service) is IBM's internal annotation platform used
  to create the DocLayNet dataset
- The 13 label categories shown in the palette are the DocLayNet annotation
  classes (reduced from an initial set during the label selection phase)
- The annotation workflow involves human annotators drawing bounding boxes
  around document layout elements and assigning category labels
- This screenshot demonstrates the annotation methodology described in
  Section 4 of the paper ("Annotation Campaign")
- The document being annotated appears to contain both text and figure
  elements, illustrating the variety of layout structures annotators encounter

### Search Keywords

annotation interface, CCS, Corpus Conversion Service, bounding boxes,
document layout, annotation tool, label palette, DocLayNet, document
segmentation, layout categories, Text, Picture, Table, Section-header,
annotation campaign, IBM Research, KDD 2022

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A screenshot of a software interface with colored boxes" (no tool or label identification) | "CCS annotation interface showing a document page with colored bounding boxes and a 13-category label palette on the right; categories include Text, Picture, Formula, Table, etc." (identifies tool and labels) | All 13 palette categories listed with their color indicators, bounding box overlay styles described (cross-hatch, colors), action buttons identified (Skip, Filter, Submit, Report problem), corner X controls noted |
| Specificity | "Colored rectangles on a document" (no categories named) | "13 annotation categories in the Clusters palette; document shows multiple overlapping colored rectangles with different fill patterns; bar chart and pie chart visible under overlays" | All 13 category names with color indicators, overlay pattern descriptions (striped, cross-hatched), button labels and positions, two-panel layout with width ratio, visible document content (bar chart ~4-5 bars, pie chart) |
| Completeness | Mentions boxes and palette but misses buttons or overlay patterns | Covers palette categories, bounding boxes, action buttons, and caption text | All palette entries with colors, all visible bounding box regions with approximate colors and patterns, all UI controls, caption verbatim, document content behind overlays, corner dismiss controls |
| Usefulness | "A screenshot from a paper" (no context) | "DocLayNet annotation interface showing how human annotators label document layout elements using 13 categories; part of IBM's document AI research" | Connects to CCS platform, explains annotation workflow (draw box then assign label), notes 13 classes are the DocLayNet taxonomy, identifies as Figure 3 from Section 4 of KDD 2022 paper |

<br><br>

## doc06-R09 -- Figure 4 example (representative)

**Figure reference:** Figure 4, page 5
**Content type:** screenshot
**Annotation difficulty:** Medium
**Dimensions:** 1025x1025 pixels

### Visual Inventory

Composite figure showing 4 labeled cases (A through D), each displaying a
pair of side-by-side document page screenshots with different annotation
bounding box overlays on the same underlying page. A vertical dashed line
separates the left and right alternatives in each pair. Each case is labeled
with a circled letter (A, B, C, D) and a hex hash string identifies the
specific page. The figure demonstrates plausible annotation inconsistencies.
Caption reads: "Figure 4: Examples of plausible annotation alternatives for
the same page. Criteria in our annotation guideline can resolve cases A to C,
while the case D remains ambiguous."

### Verifiable Facts

- 4 cases labeled A, B, C, D (circled black letters on left margin)
- Each case shows two annotation alternatives side by side for one document page
- A vertical dashed black line separates each left/right pair
- Each pair is identified by a hex hash string between the case panels
- **Case A:** A corporate/financial report page with text paragraphs and a small
  bar chart ("Sales per employees (in thousand)"). Both alternatives show
  yellow-highlighted text regions and small chart areas, but bounding box
  grouping differs (how text blocks are segmented)
- **Case B:** An English grammar reference page showing verb conjugation tables
  (infinitive, past tense, past participle). Left alternative highlights the
  table rows in pink/magenta; right alternative highlights them in yellow. The
  table includes verbs: to be, to break, to build, to do, to drink, to drive,
  to fall, to feel, to fling
- **Case C:** A knitting/crochet instruction page with a red header bar
  ("ADDING ANOTHER YARN IN THE MIDDLE OF A ROW") and photographs of hands
  working with yarn. Both alternatives show the same content but differ in
  how the photo regions are bounded (single large box vs. separate boxes)
- **Case D:** Labeled "Borderline case: Two guideline-compliant alternatives".
  Shows a page with a bar chart titled "Global Fisheries Production: Share of
  Capture and Aquaculture". Left alternative has the chart title as a separate
  text annotation above the chart box; right alternative groups the title
  inside the chart's bounding box (blue outline around title + chart together)
- Caption: "Figure 4: Examples of plausible annotation alternatives for the
  same page. Criteria in our annotation guideline can resolve cases A to C,
  while the case D remains ambiguous."

### Hallucination Risks

- **Annotation box colors:** The small screenshots make it hard to precisely
  match bounding box colors to specific DocLayNet categories. An annotator
  might guess that yellow = Text or pink = Table based on the Figure 3 palette,
  but the color rendering at this scale is unreliable.
- **Document text content:** The text within each small screenshot is partially
  readable but extremely small. An annotator might misread specific words or
  numbers from the underlying documents.
- **Exact annotation differences:** The difference between left and right
  alternatives in each case is subtle. An annotator might misdescribe the
  specific bounding box differences (e.g., claiming boxes differ in category
  labels when they actually differ in spatial grouping).
- **Case label explanations:** The figure does not explain what makes each case
  resolvable or ambiguous -- that context comes from the paper text. An
  annotator might invent explanations for why A-C are resolvable.

### Detail Inventory

- **Layout:** 4 rows (cases A-D), each containing a left-right pair separated
  by a vertical dashed line; the full figure spans the right column of the
  two-column paper layout
- **Case labels:** Black circled letters (A, B, C, D) positioned on the left
  margin of each case
- **Hash identifiers:** Hex strings (e.g., "1ef23f5e6d7f10d393f9947e8208285d...")
  between case pairs, identifying the specific DocLayNet page
- **Case A documents:** Corporate report with employee statistics, small grouped
  bar chart in the upper-right area of the page
- **Case B documents:** Grammar reference with a 3-column table (infinitive /
  past tense / past participle); pink vs. yellow highlighting difference
- **Case C documents:** Craft instructions with a red banner header and two
  photographs of yarn/knitting work
- **Case D documents:** Fisheries statistics with a grouped bar chart showing
  yellow/gold bars; "Borderline case" label in text above the pair
- **Screenshot quality:** Small embedded screenshots; text is legible at close
  inspection but fine details (font sizes, exact colors) are compressed

### Domain Context

- This figure illustrates the annotation consistency challenge central to
  the DocLayNet paper's methodology section
- Cases A-C demonstrate annotation ambiguities that the DocLayNet annotation
  guideline resolves with explicit rules (e.g., how to handle list items,
  tables, grouped sub-figures)
- Case D shows a genuinely ambiguous situation where two different annotation
  strategies are both valid under the guidelines
- The hex hashes identify specific pages in the DocLayNet corpus, enabling
  reproducibility
- This figure motivates why a detailed annotation guideline was necessary --
  without one, inter-annotator agreement would be low

### Search Keywords

annotation alternatives, annotation consistency, bounding boxes, annotation
ambiguity, DocLayNet, guideline-compliant, borderline case, document layout,
inter-annotator agreement, annotation guideline, layout segmentation,
side-by-side comparison, KDD 2022

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Multiple small screenshots of documents" (no case structure identified) | "4 labeled cases (A-D) each showing two annotation alternatives for the same page; cases A-C are resolvable, case D is ambiguous" (captures structure and purpose) | All 4 cases with document content described (corporate report, grammar table, knitting instructions, fisheries chart), specific annotation differences noted per case, "Borderline case" label on D, hex hashes noted |
| Specificity | "Documents with colored highlights" (no case details) | "Case A: financial report with bar chart; Case B: verb conjugation table with pink vs yellow highlights; Case C: craft instructions with photos; Case D: fisheries bar chart with title grouping difference" | Specific verbs in Case B table, chart title in Case D ("Global Fisheries Production"), red header text in Case C, annotation grouping differences described per case, dashed separator line, circled case labels |
| Completeness | Mentions some screenshots but misses the case structure or caption | All 4 cases described, caption quoted, side-by-side structure noted | All 4 cases with content and annotation differences, hex hashes, circled labels, dashed separators, "Borderline case" label, caption verbatim, connection to annotation guideline |
| Usefulness | "Figure from a paper showing documents" (no context) | "Demonstrates annotation ambiguity in DocLayNet; shows how same page can be annotated differently; guideline resolves A-C but D is genuinely ambiguous" | Connects to annotation consistency challenge, explains why detailed guidelines are needed, notes inter-annotator agreement implications, identifies as Figure 4 from DocLayNet's methodology section |

<br><br>

## doc06-R17 -- 6-panel layout prediction examples

**Figure reference:** Figure 6, page 9
**Content type:** screenshot
**Annotation difficulty:** Medium
**Dimensions:** 1025x1025 pixels

### Visual Inventory

Composite figure arranged as a 2x3 grid (panels A-F), each showing a different
document page with colored semi-transparent bounding boxes overlaid to indicate
predicted layout regions. The 6 panels represent different document categories
from the DocLayNet test set. Each panel has a circled letter label (A-F) in the
top-left corner and a hexadecimal document hash string along the left or bottom
edge. A page header above the figure reads "DocLayNet: A Large Human-Annotated
Dataset for Document-Layout Analysis" on the left and "KDD '22, August 14-18,
2022, Washington, DC, USA" on the right.

- **Panel A (top-left):** Corporate brochure page with teal/blue gradient
  background. Multiple green (Text) bounding boxes, yellow (Section-header)
  boxes, and a small data table with numerical values at top-right. An aerial
  photograph of a building/resort complex appears at the bottom.
- **Panel B (top-center):** Technical product manual page on white background,
  titled "OPERATION (cont.)" in a red Section-header box. Contains a labeled
  microscope illustration ("MODEL AY11236") with blue Text boxes, a red
  Section-header "MICROSCOPE USAGE", and another red Section-header
  "CONSTRUCTION". The microscope diagram has a Picture bounding box.
- **Panel C (top-right):** Academic/scientific paper page with dense mathematical
  content. Yellow bounding boxes on equations and formulas, blue/purple boxes on
  text paragraphs. Contains summation notation, subscripts, and multi-line
  derivations.
- **Panel D (bottom-left):** Corporate document page with dark red/maroon
  background, titled "SETTING THE FUTURE IN MOTION" in large gold text. Contains
  yellow Text boxes over body paragraphs, photos of buildings/infrastructure
  scenes in the left column, and orange/red decorative elements.
- **Panel E (bottom-center):** Aviation operations manual page on pink background.
  Contains green Section-header boxes ("Circling Minima", "Airport Sketch"),
  yellow Table boxes around tabular data, and a runway approach diagram/sketch
  at the bottom-right. Multiple form-like fields with pink and yellow background
  sections.
- **Panel F (bottom-right):** Chinese patent document. Red official header banner
  with a circular seal/emblem. Blue Text boxes on Chinese character paragraphs,
  yellow boxes on specific fields. Classification number "[51] Int. Cl. G06F
  1/00 (2006.01)" visible. Contains a mix of Chinese and English text with
  structured patent metadata fields.

### Verifiable Facts

- 6 panels arranged in a 2x3 grid, labeled A through F with circled letters
- Panel labels positioned: A top-left, B top-center, C top-right, D bottom-left,
  E bottom-center, F bottom-right
- Page header: "DocLayNet: A Large Human-Annotated Dataset for Document-Layout
  Analysis" (left) and "KDD '22, August 14-18, 2022, Washington, DC, USA" (right)
- Caption text: "Figure 6: Example layout predictions on selected pages from the
  DocLayNet test-set. (A, D) exhibit favourable results on coloured backgrounds.
  (B, C) show accurate list-item and paragraph differentiation despite
  densely-spaced lines. (E) demonstrates good table and figure distinction. (F)
  shows predictions on a Chinese patent with multiple overlaps, label confusion
  and missing boxes."
- Bounding box color scheme consistent across panels: blue/purple for Text,
  red for Section-header, yellow for Caption/Table, green for other categories
- Each panel has a hexadecimal hash string along one edge (document identifiers)
- Panel B contains the text "MODEL AY11236" and section headers "MICROSCOPE
  USAGE" and "CONSTRUCTION"
- Panel D title reads "SETTING THE FUTURE IN MOTION"
- Panel E contains section headers "Circling Minima" and "Airport Sketch"
- Panel F contains "[51] Int. Cl. G06F 1/00 (2006.01)"
- Panel A has a teal/blue gradient background with an aerial photograph
- Panel D has a dark red/maroon background
- Panel E has a pink background
- Bounding boxes use semi-transparent colored fills (not just outlines)

### Hallucination Risks

- **Bounding box color-to-label mapping:** The figure does not include an explicit
  color legend. An annotator might assign incorrect category names to box colors
  by guessing from the R07 palette or from the paper text rather than from
  visible evidence in this crop. The color-to-category mapping must be inferred
  from context (e.g., red boxes consistently appear on headings), which is
  inherently uncertain.
- **Panel content identification:** At the crop resolution, fine text within
  panels is partially legible. An annotator might fabricate specific text content
  (paragraph text, table cell values) that appears plausible but is not actually
  readable in the crop.
- **Document category assignment:** The caption mentions "coloured backgrounds"
  for A and D, but does not explicitly name the document categories (Financial,
  Tender, Manual, etc.). An annotator might assign categories based on
  appearance (e.g., Panel A looks like a Tender, Panel F is a Patent) but these
  are inferences, not labeled facts in the crop.
- **Bounding box completeness in Panel F:** The caption explicitly states Panel F
  has "multiple overlaps, label confusion and missing boxes." An annotator might
  not notice these prediction failures or might describe Panel F's predictions
  as equally successful as the other panels.
- **Hash strings:** The hex document IDs along panel edges are partially readable.
  An annotator might attempt to transcribe them but get characters wrong due to
  small font size and compression artifacts.

### Detail Inventory

- **Panel A:** Teal-to-blue diagonal gradient background; green Text boxes over
  body paragraphs; yellow boxes on section titles; small numerical table at
  top-right with rows/columns of data; aerial/satellite photograph of a
  building complex at bottom; hex hash along left edge
- **Panel B:** White background; "OPERATION (cont.)" red header; microscope line
  drawing labeled "MODEL AY11236" with callout labels pointing to components;
  "MICROSCOPE USAGE" red section header with blue text boxes below;
  "CONSTRUCTION" red section header; two small logo images at bottom
  (appears to be "BARSKA" brand logos)
- **Panel C:** White/cream background; dense mathematical content with equations
  spanning multiple lines; yellow bounding boxes on equation blocks; blue/purple
  boxes on text paragraphs; formulas include summation symbols, subscripts,
  fractions, and Greek letters
- **Panel D:** Dark red/maroon textured background; "SETTING THE FUTURE IN
  MOTION" in large gold serif text; large decorative "W" drop cap; photos of
  architecture/buildings in left column; body text in yellow Text boxes; overall
  magazine/brochure visual style
- **Panel E:** Pink tinted background; structured form layout with ruled sections;
  "Circling Minima" and "Airport Sketch" as green section headers; tabular data
  in yellow Table boxes; runway approach diagram/chart at bottom-right showing
  runway orientation and approach paths; text about airport elevation, taxiways,
  and approach bearings
- **Panel F:** Chinese patent format; red banner with circular official seal;
  "Int. Cl. G06F 1/00 (2006.01)" classification; structured patent metadata
  fields with Chinese labels; multiple blue Text boxes with visible overlaps;
  yellow highlight boxes on certain fields; mix of Chinese characters and
  alphanumeric codes
- **Bounding box rendering:** Semi-transparent colored fills rather than outlines
  only; boxes overlap in Panel F (the failure case)
- **Panel letter labels:** White or light-colored circled letters positioned at
  top-left of each panel

### Domain Context

- Figure 6 from the DocLayNet paper (KDD 2022) demonstrating the quality of
  layout prediction on the test set across diverse document types
- The 6 panels were selected to showcase different challenges: colored
  backgrounds (A, D), dense text with list-item/paragraph differentiation
  (B, C), table/figure distinction (E), and a failure case with overlaps and
  label confusion (F)
- DocLayNet defines 11 layout categories (Text, Title, Section-header, Caption,
  Table, List-item, Formula, Picture, Page-header, Page-footer, Footnote) --
  the bounding box colors in this figure correspond to predicted categories
- The document types likely represent: Tender (A), Manual (B), Scientific paper
  (C), Financial/annual report (D), Government/regulatory (E), Patent (F) --
  matching DocLayNet's 6 document categories
- Panel F is explicitly called out as a failure case, making this figure
  important for understanding model limitations alongside successes
- The hex strings along panel edges are likely internal document identifiers
  from the DocLayNet dataset

### Search Keywords

layout prediction, bounding boxes, DocLayNet, document layout analysis,
test-set examples, annotation categories, colored backgrounds, Chinese patent,
microscope manual, airport sketch, mathematical equations, KDD 2022,
semi-transparent overlays, prediction failures, label confusion, document
categories

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Six panels showing documents with colored boxes" (no panel-specific content) | "2x3 grid of annotated document pages labeled A-F; Panel B shows a microscope manual, Panel F is a Chinese patent with overlapping boxes" (key panels identified correctly) | All 6 panels described with correct content: A=teal corporate brochure with aerial photo, B=microscope manual with OPERATION header, C=math-heavy paper, D=red background SETTING THE FUTURE IN MOTION, E=pink aviation manual with Airport Sketch, F=Chinese patent with G06F classification; notes Panel F as the explicit failure case per caption |
| Specificity | "Colored rectangles on documents" (generic) | "Semi-transparent bounding boxes in blue, red, yellow, and green indicating different layout categories; Panel B has MODEL AY11236 label" (reads some details) | Specific text from each panel (MODEL AY11236, MICROSCOPE USAGE, CONSTRUCTION, SETTING THE FUTURE IN MOTION, Circling Minima, Airport Sketch, G06F 1/00), bounding box color patterns per panel, background colors (teal gradient, white, white, maroon, pink, white), hex hash strings noted, BARSKA logos in Panel B |
| Completeness | Mentions it is a multi-panel figure but describes only 2-3 panels | All 6 panels described with primary content; caption quoted; notes header text | All 6 panels with content, background color, bounding box colors, and layout structure; caption verbatim with per-panel commentary; page header text; hex document IDs; panel letter label styling; bounding box rendering style (semi-transparent fills); explicit identification of Panel F failure modes (overlaps, label confusion, missing boxes) |
| Usefulness | "Figure from a paper about documents" (no context) | "Figure 6 from DocLayNet showing layout prediction quality across different document types from the test set" | Connects to DocLayNet's 6 document categories, explains the deliberate selection of success cases (A-E) and failure case (F), identifies specific challenges each panel demonstrates (colored backgrounds, dense text, table/figure distinction), notes relevance for understanding model limitations in document layout analysis |

<br><br>

## doc06-V01 -- Pie chart of DocLayNet distribution

**Figure reference:** Figure 2, page 3
**Content type:** chart-simple
**Annotation difficulty:** Easy
**Dimensions:** vector

### Visual Inventory

Single pie chart showing the distribution of DocLayNet pages across 6 document
categories. Each slice is colored distinctly and labeled with the category name
(outside the slice) and percentage value (inside or near the slice). The
largest slice (Financial, 32%) dominates the upper-left quadrant. Caption reads
"Figure 2: Distribution of DocLayNet pages across document categories." Paper
title fragment visible at top of crop.

### Verifiable Facts

- 6 slices, each labeled with category name and percentage:
  - Financial: 32% (green, largest slice, upper-left)
  - Manuals: 21% (tan/brown, right side)
  - Scientific: 17% (peach/salmon, upper-right)
  - Laws: 16% (lavender/purple, bottom-center)
  - Patents: 8% (light blue, right)
  - Tenders: 6% (pink/coral, left, smallest slice)
- Percentages sum to 100% (32 + 21 + 17 + 16 + 8 + 6 = 100)
- Caption: "Figure 2: Distribution of DocLayNet pages across document
  categories."
- Paper title fragment at top: "DocLayNet: A Large Human-Annotated Dataset
  for Document-Lay[out Analysis]"
- No legend -- labels are placed directly adjacent to each slice
- No 3D effect -- flat 2D pie chart

### Hallucination Risks

- **Exact page counts:** The chart shows only percentages, not absolute page
  counts. An annotator might infer counts from the paper's stated 80K+ pages
  (e.g., "32% of 80K = 25,600 Financial pages") but these are calculations,
  not visible data.
- **Color name precision:** The slice colors are pastel/muted tones. An
  annotator might use different color names (e.g., "olive" vs "tan" for
  Manuals, "salmon" vs "peach" for Scientific). The exact color names are
  subjective.
- **Category ordering:** The slices appear in clockwise order starting from
  roughly 12 o'clock, but the exact starting angle is ambiguous. An annotator
  might impose a different reading order.
- **Exploded slice:** The Financial slice appears very slightly separated
  (exploded) from the pie. This is subtle and an annotator might not mention
  it or might overstate the separation.

### Detail Inventory

- **Slice colors (clockwise from top-left):**
  - Financial: medium green (pastel)
  - Scientific: peach/salmon (pastel)
  - Patents: light blue (pastel)
  - Manuals: tan/khaki (pastel)
  - Laws: lavender/light purple (pastel)
  - Tenders: pink/coral (pastel)
- **Label placement:** Category names outside the pie boundary, percentage
  values inside or at the edge of each slice
- **Font:** Sans-serif, black text for all labels and percentages
- **Percentage format:** Integer values followed by "%" sign (no decimals)
- **Chart background:** White, no gridlines or axes
- **Caption:** Bold "Figure 2:" followed by regular weight description text,
  positioned below the pie

### Domain Context

- DocLayNet is a document layout analysis dataset published by IBM Research
- The 6 categories represent different document types commonly processed in
  enterprise settings
- Financial documents (annual reports, SEC filings) dominate at 32%, reflecting
  the dataset's enterprise focus
- The distribution is intentionally imbalanced to reflect real-world document
  processing workloads
- This figure appears in the dataset description section, establishing the
  corpus composition before discussing annotation methodology and benchmarks

### Search Keywords

pie chart, distribution, DocLayNet, document categories, Financial, Manuals,
Scientific, Laws, Patents, Tenders, dataset composition, document layout
analysis, percentage, corpus statistics, KDD 2022

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A pie chart showing different categories" (no names or values) | "Pie chart of 6 document categories: Financial 32%, Manuals 21%, Scientific 17%, Laws 16%, Patents 8%, Tenders 6%" (all labels and values correct) | All 6 categories with exact percentages, notes they sum to 100%, identifies Financial as dominant, describes pastel color scheme, mentions the slight explosion of the Financial slice |
| Specificity | "A colorful pie chart" (no data read) | "6 slices with percentage labels; Financial is largest at 32%; smallest is Tenders at 6%" (reads key values) | All 6 category-percentage pairs, clockwise ordering, color assignments per slice, label placement (names outside, percentages inside), font style, caption text verbatim |
| Completeness | Mentions pie chart but misses half the categories | All 6 categories and percentages; notes caption and figure number | All slices with colors and percentages, label placement, caption verbatim, paper title bleed at top, flat 2D style, no legend needed, percentage sum verification |
| Usefulness | "A chart from a paper" (no domain context) | "Pie chart showing DocLayNet dataset distribution across 6 document types; Financial documents dominate at 32%" | Explains DocLayNet as IBM's document layout analysis dataset, notes enterprise focus reflected in Financial dominance, connects to the paper's dataset description section, identifies as Figure 2 from KDD 2022 paper |

# PDF Image Inspection Guide

How to identify all embedded images, vector figures, and native tables in
PDF fixtures. Uses pypdfium2 for structural analysis and visual page
rendering for confirmation.


## Why This Matters

Visually rendering a PDF page cannot reliably distinguish between:
- A table rendered as an embedded raster image (pipeline extracts as picture)
- A native text table with styling (pipeline extracts as structured table)
- A chart drawn with vector paths (may or may not be extracted as picture)
- A chart embedded as a raster image (definitely extracted as picture)

The only reliable method is combining structural PDF inspection with
visual verification.


## Two-Layer Verification Workflow

Every document must go through both layers before its catalog entry is
finalized. Neither layer alone is sufficient.

**Layer 1: pypdfium2 structural scan**

Run the scan script to get a definitive list of every embedded image
object per page, with pixel dimensions. This also checks inside Form
XObjects for nested images. The scan produces three outputs:
- Embedded raster images (IMAGE objects, type 3) with pixel sizes
- Pages with significant vector content (PATH + FORM counts) that may
  contain vector-drawn figures
- Pages with only TEXT objects (pure text, no visual elements)

**Layer 1.5: Text search for Figure and Table labels**

After the structural scan, search the PDF text for all "Figure" and
"Table" caption labels. This cross-references the structural scan and
catches content that might otherwise be missed:

```bash
docker compose exec dev python3 -c "
import pypdfium2 as pdfium

pdf = pdfium.PdfDocument('fixtures/downloaded/<filename>.pdf')

for i in range(len(pdf)):
    page = pdf[i]
    text = page.get_textpage().get_text_range()
    lines = text.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('Figure ') or stripped.startswith('Table '):
            label = stripped[:100]
            print(f'Page {i+1}: {label}')
    page.close()

pdf.close()
"
```

Compare the labels found against the structural scan:
- A Figure label on a page WITH IMAGE objects: the figure is raster
- A Figure label on a page with PATH/FORM but no IMAGE: the figure is
  vector-drawn
- A Figure label on a "text only" page: the figure may be on an adjacent
  page, or it is a text-only reference to a figure elsewhere
- A Table label on a page with no IMAGE objects: native text table
- A Table label on a page WITH IMAGE objects: the table may contain
  embedded images (e.g., Doc 05 Table 13 has cooking photos within a
  table structure)

This step also catches figures that span multiple pages or have captions
on a different page than their visual content.

**Layer 2: Visual page rendering**

After the structural scan and text search, render pages to visually
confirm findings:
- For pages WITH image objects: confirm what each image depicts (chart,
  photo, logo, table-as-image, decorative element)
- For pages with high PATH/FORM counts: check if these are labeled
  figures, vector-drawn charts, or just styled text formatting
- For pages with only TEXT objects: check for native data tables that
  should be cataloged separately
- Note any labeled figure captions (e.g., "Figure 3:") and whether the
  figure is raster or vector

**Why all three layers are needed:**
- Layer 1 without Layer 2: You know images exist but not what they are.
  A 2048x1872 image could be a chart, a photo, or a scanned page.
- Layer 2 without Layer 1: You see what looks like a chart but cannot
  tell if it is a raster image or vector drawing. You see what looks like
  a table but cannot tell if it is an embedded image or native text.
  This caused incorrect catalog entries in early attempts.


## Catalog Structure Per Document

Each document gets three sections based on the two-layer verification:

**Embedded Images** -- raster IMAGE objects confirmed by pypdfium2, with
pixel size and content type confirmed by visual rendering.

**Vector Figures** -- labeled figures drawn with PATH/TEXT/FORM objects
(no raster image). Record object counts per page. The pipeline may or
may not extract these depending on how it classifies vector content.

**Tables (native text)** -- data tables with rows and columns rendered as
native text, confirmed by zero IMAGE objects on the page. Record row
count, column count, and description.


## Scan Script: Full Document Analysis

This single script runs the complete Layer 1 analysis. It checks for
images at the top level AND recursively inside Form XObjects. Replace
`<filename>` with the actual PDF filename.

```bash
docker compose exec dev python3 -c "
import pypdfium2 as pdfium
import pypdfium2.raw as raw

TYPE_NAMES = {1: 'TEXT', 2: 'PATH', 3: 'IMAGE', 4: 'SHADING', 5: 'FORM'}

pdf = pdfium.PdfDocument('fixtures/downloaded/<filename>.pdf')
print(f'Document: <filename>.pdf')
print(f'Pages: {len(pdf)}')
print()

for i in range(len(pdf)):
    page = pdf[i]

    # Count top-level objects by type
    counts = {}
    top_images = []
    for obj in page.get_objects():
        name = TYPE_NAMES.get(obj.type, f'UNK({obj.type})')
        counts[name] = counts.get(name, 0) + 1
        if obj.type == raw.FPDF_PAGEOBJ_IMAGE:
            px = obj.get_px_size()
            bounds = obj.get_bounds()
            w = bounds[2] - bounds[0]
            h = bounds[3] - bounds[1]
            top_images.append((px[0], px[1], w, h))

    # Check for images nested inside Form XObjects
    nested_images = 0
    for obj in page.get_objects():
        if obj.type == raw.FPDF_PAGEOBJ_FORM:
            child_count = raw.FPDFFormObj_CountObjects(obj.raw)
            for j in range(child_count):
                child = raw.FPDFFormObj_GetObject(obj.raw, j)
                if raw.FPDFPageObj_GetType(child) == raw.FPDF_PAGEOBJ_IMAGE:
                    nested_images += 1

    # Report
    has_content = top_images or nested_images or counts.get('PATH', 0) > 5 or counts.get('FORM', 0) > 1
    if has_content:
        summary = ', '.join(f'{v} {k}' for k, v in sorted(counts.items()))
        print(f'Page {i+1}: {summary}')
        for idx, (pw, ph, ptw, pth) in enumerate(top_images):
            print(f'  -> IMAGE #{idx+1}: {pw}x{ph} px, {ptw:.0f}x{pth:.0f} pts')
        if nested_images:
            print(f'  -> {nested_images} image(s) nested inside FORM objects')
    else:
        print(f'Page {i+1}: text only')

    page.close()

pdf.close()
"
```


## Reading the Output

The script reports every page, categorized as either "text only" or with
a breakdown of object types.

Example output:

```
Document: 00_gemini3_pro_model_card.pdf
Pages: 9

Page 1: 2 IMAGE, 3 PATH, 15 TEXT
  -> IMAGE #1: 837x13 px, 628x15 pts
  -> IMAGE #2: 932x312 px, 77x26 pts
Page 2: text only
Page 3: text only
Page 4: text only
Page 5: 1 IMAGE, 12 TEXT
  -> IMAGE #1: 2048x1872 px, 456x416 pts
Page 6: text only
Page 7: 22 PATH, 18 TEXT
Page 8: text only
Page 9: 16 PATH, 24 TEXT
```

**How to interpret:**
- `IMAGE` entries with `->` details: Confirmed raster images. Render the
  page to identify what they depict.
- High `PATH` + `TEXT` counts without `IMAGE`: Likely vector-drawn figures
  or styled table borders. Render to confirm.
- `FORM` entries: Grouped vector content. The script already checks inside
  these for nested images.
- `text only`: No visual elements. Render to check for native data tables
  (which use TEXT objects for cell contents and may have minimal PATH
  objects for borders).

**Pixel size patterns:**
- Very thin (e.g., 837x13 px): Decorative lines or separators
- Small (< 200x200 px): Logos, icons, small graphics
- Medium (200-1000 px): Inline figures, small charts
- Large (> 1000 px): Full charts, table-as-image, photos, scanned pages


## Object Type Reference

| Constant | Value | What it means |
|----------|-------|---------------|
| `FPDF_PAGEOBJ_TEXT` | 1 | Native text (selectable, searchable) |
| `FPDF_PAGEOBJ_PATH` | 2 | Vector lines, shapes, borders, fills |
| `FPDF_PAGEOBJ_IMAGE` | 3 | Embedded raster image (PNG/JPEG/etc) |
| `FPDF_PAGEOBJ_SHADING` | 4 | Gradient fills |
| `FPDF_PAGEOBJ_FORM` | 5 | Grouped content (may contain any of the above) |

Only type 3 (IMAGE) represents actual embedded raster images. Types 1+2
together create vector-drawn figures and native tables. Type 5 groups
content that may include nested images (the script checks for this).


## Patterns Observed Across Documents

Patterns discovered during cataloging that help interpret scan results.

**Decorative cover images:** IMF and similar institutional PDFs often embed
full-page raster images (e.g., 1633x2113 px at 612x792 pts) as cover and
back cover backgrounds. These span the entire page and have TEXT/PATH
objects overlaid on top. Identify by: full-page point size matching the
PDF page dimensions (typically 612x792 pts for US Letter).

**Tiny gradient bars in scatter plots:** Some PDF generators embed thin
raster images as color gradient legends within vector-drawn scatter plots.
Examples: 20x397 px and 11x248 px in Doc 04. These are decorative
elements, not content images. Identify by: one dimension under 30 px with
the other dimension much larger.

**Vector-heavy documents:** Some documents (e.g., Doc 01 GPT-4 System Card,
Doc 04 Anthropic Economic Index) draw ALL figures entirely with vector
graphics. These can have extremely high object counts (Doc 04 Figure 3.5:
7194 PATH + 3558 FORM for a scatter plot with hundreds of data points).
The scan will show zero or near-zero IMAGE objects despite the document
being full of charts. The Layer 1.5 text search for figure labels is
essential for these documents.

**Tables with embedded images:** Some tables contain raster images within
their cell structure (e.g., Doc 05 Table 13 has cooking photos in an
audio-visual example table). These pages will show both TABLE-like text
structure and IMAGE objects. The table should be cataloged noting the
embedded images.

**Figures spanning multiple pages:** Figure captions sometimes appear on a
different page than the figure content. The Layer 1.5 text search catches
the caption page, while the structural scan catches the content page.
Cross-reference both to correctly attribute figures.

**Multi-figure pages:** Academic papers often pack multiple subfigures onto
a single page (e.g., Doc 02 page 6 has 7 IMAGE objects across Figures
2, 3, and 4). The text search helps map IMAGE objects to their figure
labels.


## Limitations

- Form XObject recursion is one level deep. Deeply nested forms (forms
  inside forms) would require additional recursion levels. This was
  observed in Doc 05 (Gemini report) where Figure 6 on page 17 had
  visual image content (AI-generated avocados, bunnies) that appeared in
  the rendered page but was not detected by the scan. The page showed
  117 FORM objects but only 1 tiny IMAGE (20x397 px decorative element).
  The actual image content was likely nested 2+ levels deep inside FORM
  objects. When a page has many FORM objects but the visual render shows
  image content not accounted for by the scan, note this as a deep
  nesting case in the catalog.
- DOCX and PPTX files use different formats (ZIP archives with media/
  folders). This guide applies to PDF only. For DOCX/PPTX, extract the
  ZIP and inspect the media/ directory for embedded images.
- Scanned PDFs typically have one large IMAGE object per page (the entire
  scan) with no native TEXT objects. The scan script will detect these.
- Some PDF generators encode vector charts as a single Form XObject
  containing many PATH and TEXT children. The script reports FORM counts
  but does not distinguish "chart-like forms" from "decorative forms".
- The text search for Figure/Table labels only catches captions that
  start a line with "Figure " or "Table ". Inline references (e.g.,
  "see Figure 3") are not captured. Some documents use non-standard
  labeling (e.g., "Fig. 1" or unlabeled figures) which require visual
  verification to detect.

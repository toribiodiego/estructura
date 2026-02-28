# Office Document Inspection Guide

How to identify all embedded images, charts, and visual content in DOCX, PPTX,
and XLSX fixtures. These formats are ZIP archives with known internal structures
that can be inspected programmatically before visual verification.

For PDF inspection, see [PDF Image Inspection Guide](./pdf-image-inspection.md).


## Why This Matters

Office documents store visual content in multiple ways:
- **Raster images** in `media/` directories (PNG, JPEG, TIFF, EMF, WMF)
- **Chart objects** as XML definitions that only become visible when rendered
- **SmartArt and diagrams** as XML that requires rendering
- **Embedded OLE objects** (e.g., Excel charts inside Word documents)

A file listing alone cannot distinguish between a decorative logo and a data
chart. Structural scanning identifies what exists; visual verification confirms
what it depicts.


## Two-Layer Verification Workflow

Same philosophy as the PDF guide: structural scan first, targeted visual
rendering second. Neither layer alone is sufficient.

**Layer 1: ZIP structure scan**

All Office Open XML formats (`.docx`, `.pptx`, `.xlsx`) are ZIP archives.
Unzip and inspect the internal directories to get a definitive inventory of
embedded content.

**Layer 2: Visual rendering**

Render the document to images (via LibreOffice headless or by reading
extracted media files directly) to confirm what each element depicts and
classify it for the catalog.


## Internal Structure Reference

### DOCX (`word/`)

```text
word/
  media/                  embedded raster images (image1.png, image2.jpeg, ...)
  charts/                 embedded chart XML (chart1.xml, ...)
  document.xml            main document body
  _rels/document.xml.rels relationship mappings (which images go where)
```

### PPTX (`ppt/`)

```text
ppt/
  media/                  embedded raster images
  charts/                 embedded chart XML
  slides/                 one XML file per slide
  _rels/                  relationship mappings
```

### XLSX (`xl/`)

```text
xl/
  media/                  embedded raster images (rare -- logos, photos)
  charts/                 chart object XML (chart1.xml, chart2.xml, ...)
  drawings/               drawing containers that position charts on sheets
  worksheets/             one XML file per sheet
  _rels/                  relationship mappings
```


## Scan Script: Full Document Analysis

This script inspects any DOCX, PPTX, or XLSX file and reports all embedded
content. Replace `<path>` with the fixture path.

```bash
docker compose exec dev python3 -c "
import zipfile, os, sys, xml.etree.ElementTree as ET

path = '<path>'
z = zipfile.ZipFile(path)
files = z.namelist()
ext = os.path.splitext(path)[1].lower()

print(f'Document: {os.path.basename(path)}')
print(f'Format: {ext}')
print()

# --- Raster images ---
if ext == '.docx':
    media_prefix = 'word/media/'
elif ext == '.pptx':
    media_prefix = 'ppt/media/'
elif ext == '.xlsx':
    media_prefix = 'xl/media/'
else:
    media_prefix = ''

images = sorted([f for f in files if f.startswith(media_prefix)])
print(f'Raster images: {len(images)}')
for img in images:
    info = z.getinfo(img)
    size_kb = info.file_size / 1024
    print(f'  {os.path.basename(img):30s} {size_kb:>8.1f} KB')
print()

# --- Charts ---
if ext == '.docx':
    chart_prefix = 'word/charts/'
elif ext == '.pptx':
    chart_prefix = 'ppt/charts/'
elif ext == '.xlsx':
    chart_prefix = 'xl/charts/'
else:
    chart_prefix = ''

chart_xmls = sorted([f for f in files if f.startswith(chart_prefix) and f.endswith('.xml') and not f.endswith(('style.xml', 'colors.xml'))])
# Filter to actual chart definitions (not style/colors files)
chart_xmls = [f for f in chart_xmls if '/chart' in f and 'style' not in f and 'colors' not in f and '_rels' not in f]

print(f'Chart objects: {len(chart_xmls)}')
for cf in chart_xmls:
    try:
        tree = ET.parse(z.open(cf))
        root = tree.getroot()
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}

        # Find chart type elements
        chart_types = []
        for elem in root.iter():
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag in ('barChart', 'bar3DChart', 'lineChart', 'line3DChart',
                       'pieChart', 'pie3DChart', 'doughnutChart',
                       'scatterChart', 'areaChart', 'area3DChart',
                       'radarChart', 'bubbleChart', 'stockChart',
                       'ofPieChart', 'surfaceChart', 'surface3DChart'):
                chart_types.append(tag)

        # Find title
        title = '(no title)'
        for t_elem in root.iter():
            tag = t_elem.tag.split('}')[-1] if '}' in t_elem.tag else t_elem.tag
            if tag == 'title':
                texts = [e.text for e in t_elem.iter() if e.text and e.text.strip()]
                if texts:
                    title = ' '.join(texts).strip()[:80]
                break

        types_str = ', '.join(chart_types) if chart_types else 'unknown'
        print(f'  {os.path.basename(cf):30s} type={types_str}  title={title}')
    except Exception as e:
        print(f'  {os.path.basename(cf):30s} (parse error: {e})')
print()

# --- Sheets/slides/pages ---
if ext == '.xlsx':
    sheets = sorted([f for f in files if f.startswith('xl/worksheets/sheet')])
    print(f'Worksheets: {len(sheets)}')
    for s in sheets:
        print(f'  {os.path.basename(s)}')
elif ext == '.pptx':
    slides = sorted([f for f in files if f.startswith('ppt/slides/slide') and f.endswith('.xml')])
    print(f'Slides: {len(slides)}')
elif ext == '.docx':
    print('Document body: word/document.xml')
print()

# --- Drawings (chart containers) ---
if ext == '.xlsx':
    drawings = [f for f in files if f.startswith('xl/drawings/drawing') and f.endswith('.xml')]
    print(f'Drawing containers: {len(drawings)}')
    for d in sorted(drawings):
        print(f'  {d}')

z.close()
"
```


## Reading the Output

Example output for an XLSX dashboard:

```text
Document: workforce-dashboard.xlsx
Format: .xlsx

Raster images: 0

Chart objects: 10
  chart1.xml                     type=barChart  title=Enrollment by Program
  chart2.xml                     type=pieChart  title=Funding Sources
  chart3.xml                     type=lineChart  title=Quarterly Trends
  ...

Worksheets: 3
  sheet1.xml
  sheet2.xml
  sheet3.xml

Drawing containers: 2
  xl/drawings/drawing1.xml
  xl/drawings/drawing2.xml
```

**How to interpret:**
- **Raster images** with large file sizes (>50 KB): likely content images (photos,
  screenshots). Small sizes (<10 KB): likely logos or icons.
- **Chart objects** with recognized types: Excel-generated charts that need rendering
  to see. The XML gives chart type, title, and data range but not the visual output.
- **Drawing containers**: indicate which sheets have charts positioned on them.
  Drawing count roughly corresponds to sheets-with-charts count.
- **EMF/WMF files** in media/: Windows metafiles, often vector diagrams or charts
  pasted from other applications. These need rendering to inspect.


## Image Size Patterns

| Size | Likely content |
|------|---------------|
| < 5 KB | Icons, bullets, small logos |
| 5-50 KB | Logos, small diagrams, thumbnails |
| 50-500 KB | Charts pasted as images, screenshots, small photos |
| 500 KB - 5 MB | High-resolution photos, complex diagrams, full-page images |
| > 5 MB | Multi-panel composites, TIFF images (common in scientific DOCX) |


## Visual Verification Methods

After the structural scan, use one of these methods to see what each element
looks like. Choose based on what you need:

### Method 1: Read extracted media directly

For raster images in `media/` directories, extract and read them:

```bash
# Extract all media files
docker compose exec dev python3 -c "
import zipfile, os
z = zipfile.ZipFile('<path>')
media = [f for f in z.namelist() if '/media/' in f]
os.makedirs('/tmp/inspect-media', exist_ok=True)
for m in media:
    data = z.read(m)
    out_path = f'/tmp/inspect-media/{os.path.basename(m)}'
    with open(out_path, 'wb') as f:
        f.write(data)
    print(f'Extracted: {out_path} ({len(data)} bytes)')
z.close()
"
```

Then read the extracted images. This works for PNG, JPEG, and most raster
formats. Does NOT work for EMF/WMF (vector) or chart objects (XML).

### Method 2: Render to PDF via LibreOffice

Converts the entire document to PDF, then use pypdfium2 to render specific
pages. This renders charts, SmartArt, and all visual elements.

```bash
# Convert to PDF
docker compose exec dev libreoffice --headless --convert-to pdf \
    --outdir /tmp/inspect '<path>'

# Then render specific pages using the PDF inspection workflow
docker compose exec dev python3 -c "
import pypdfium2 as pdfium
from PIL import Image

pdf = pdfium.PdfDocument('/tmp/inspect/<filename>.pdf')
print(f'Pages: {len(pdf)}')

# Render specific pages (adjust page numbers based on scan results)
for page_num in [1, 2, 3]:  # change as needed
    page = pdf[page_num - 1]
    bitmap = page.render(scale=2)
    img = bitmap.to_pil()
    out = f'/tmp/inspect/page-{page_num:03d}.png'
    img.save(out)
    print(f'Rendered: {out} ({img.size[0]}x{img.size[1]})')
    page.close()

pdf.close()
"
```

### Method 3: Run the pipeline

Run `run_docling.py` with `--image-capture` and inspect the output crops.
This tests what the pipeline actually extracts, which may differ from what
the document contains (the pipeline may miss some content or include
decorative elements).

```bash
docker compose exec dev python3 \
    src/estructura-java/src/main/resources/scripts/run_docling.py \
    '<path>' out/detect-<name> --image-capture --progress
```

Then read the crop files in `out/detect-<name>/images/crops/`.


## Format-Specific Notes

### DOCX

- Images are in `word/media/` with sequential naming (`image1.png`, etc.)
- The naming order does NOT correspond to document order. Use
  `word/_rels/document.xml.rels` to map image files to their positions.
- Scientific papers often use TIFF images (large, high-resolution). These
  may need conversion to PNG for viewing.
- Embedded Excel charts appear as `word/charts/chart1.xml` with a
  corresponding `word/embeddings/` OLE object.

### PPTX

- Images are in `ppt/media/` with sequential naming
- Each slide is a separate XML file in `ppt/slides/`
- The slide-to-image mapping is in `ppt/slides/_rels/slideN.xml.rels`
- Algorithm pseudocode screenshots (as in Doc 11) appear as raster images
- Equations may be raster images or OMML (Office Math Markup Language)

### XLSX

- Raster images are rare in XLSX files (usually logos or pasted screenshots)
- Most visual content is **chart objects** in `xl/charts/`
- Charts are XML definitions -- they specify data ranges, chart type, colors,
  and formatting but are NOT raster images
- Charts must be **rendered** to be visually inspected (Method 2 or 3)
- The chart XML provides: chart type, title, axis labels, data series count,
  and data ranges -- enough for a first-pass catalog entry
- Drawing containers in `xl/drawings/` position charts on specific sheets

### EMF/WMF files

- Windows Enhanced/Windows Metafile format -- vector graphics
- Common in DOCX/PPTX when content is pasted from other Office apps
- Cannot be read directly as images -- need rendering via LibreOffice
- Often contain charts, diagrams, or formatted text blocks


## Catalog Structure Per Document

Same structure as the PDF guide, adapted for Office formats:

**Raster images** -- files in `media/` directories, with file size and content
type confirmed by visual inspection.

**Chart objects** -- XML-defined charts in `charts/` directories. Record chart
type, title, data series count, and visual complexity after rendering.

**Embedded diagrams** -- SmartArt, EMF/WMF files, or other vector content.
Record after rendering via LibreOffice.

**Native tables** -- tables defined in document/slide XML (not images). Record
row count, column count, and description. These are extracted as structured
data by Docling, not as images.

# Image Analysis: Doc 13 -- 13_artpro_table.webp

**Document:** `13_artpro_table.webp`
**Format:** WebP
**Source:** https://standupsurfshop.com.au/wp-content/uploads/2023/09/ARTPRO-Table.webp
**Category:** table-image
**Images:** 1
**Document context:** Standalone product specification table for ArtPro SUP foil
wing models listing dimensions, area, volume, and aspect ratio across 6 models.
Source is an Australian standup paddleboard/surf foil shop (standupsurfshop.com.au).

<br><br>

## doc13-R01 -- SUP foil wing specification table

**Figure reference:** (standalone image)
**Content type:** table-image
**Annotation difficulty:** Easy
**Dimensions:** 1024x179 pixels (WebP)

### Visual Inventory [-> Information Recovery]

- **Image type:** Product specification data table
- **Title:** None (no visible title; product context implied by model names)
- **Table structure:** 7 columns, 1 header row, 6 data rows
- **Column headers (gray text, no background):**
  1. (unlabeled model number column)
  2. wingspan
  3. chord
  4. mean average chord
  5. actual area
  6. projected area
  7. volume
  8. aspect ratio
- **Note:** The model number column is visually distinct (dark gray background,
  bold white text) but has no header label. Counting it, the table has 8
  columns total; 7 have headers.
- **Data rows:**
  1. **1401** (bold white on dark gray) | 1401mm (55.1in) | 170mm (6.69in) |
     115.7mm | 1647cm2 (255.3in2) | 1611cm2 (249.7in2) | 1764cm3 (107in3) |
     12.17
  2. **1201** | 1201mm (47.2in) | 135mm (5.31in) | 107.7mm |
     1318cm2 (204.3in2) | 1291cm2 (200.1in2) | 1247cm3 (76.1in3) | 11.14
  3. **1121** | 1121mm (44.1in) | 120mm (4.72in) | 95mm |
     1088cm2 (168.6in2) | 1065cm2 (165in2) | 920cm3 (56.1in3) | 11.78
  4. **1051** | 1051mm (41.3in) | 110mm (4.33in) | 87.1mm |
     932cm2 (144.5in2) | 915cm2 (142in2) | 688cm3 (41.9in3) | 12.05
  5. **1001** | 1001mm (39.4in) | 105mm (4.13in) | 82.9mm |
     845cm2 (131in2) | 829cm2 (128.5in2) | 594cm3 (36.2in3) | 12.06
  6. **951** | 951mm (37.4in) | 100mm (3.94in) | 79.1mm |
     768cm2 (119in2) | 753cm2 (116.7in2) | 517cm3 (31.5in3) | 12.01
- **Row styling:** First row (1401) has bold text throughout; remaining rows
  use regular weight. All model number cells have dark gray backgrounds with
  bold white text. Data cells alternate between white and very light gray
  backgrounds.
- **Text formatting:** Metric values primary, imperial in parentheses. Units
  use superscript notation (cm2, cm3, in2, in3). Header text is gray,
  lowercase, multi-line for "mean average chord", "actual area", "projected
  area", "aspect ratio".
- **Alignment:** Model numbers centered; dimension columns center-aligned;
  aspect ratio right-aligned
- **Background:** White overall, clean minimalist design

### Verifiable Facts [-> Correctness]

- FACT: There are exactly 6 models: 1401, 1201, 1121, 1051, 1001, 951
- FACT: Model names correspond to wingspan in mm (1401 has 1401mm wingspan,
  etc.)
- FACT: The 1401 is the largest model: 1401mm wingspan, 1647cm2 actual area,
  1764cm3 volume, 12.17 aspect ratio
- FACT: The 951 is the smallest model: 951mm wingspan, 768cm2 actual area,
  517cm3 volume, 12.01 aspect ratio
- FACT: All wingspan values include both metric (mm) and imperial (in)
  conversions
- FACT: All area values include both metric (cm2) and imperial (in2)
  conversions
- FACT: All volume values include both metric (cm3) and imperial (in3)
  conversions
- FACT: Mean average chord values are metric only (no imperial conversion)
- FACT: Aspect ratio values range from 11.14 (model 1201) to 12.17
  (model 1401)
- FACT: Aspect ratio does NOT monotonically increase or decrease with size --
  the 1201 has the lowest (11.14) while the 1401 has the highest (12.17)
- FACT: The first row (1401) is visually emphasized with bold text throughout
- FACT: Projected area is consistently slightly less than actual area for
  every model

### Hallucination Risks [-> Correctness]

- RISK: Calling these "aircraft wings"
  REALITY: The source URL (standupsurfshop.com.au) identifies these as SUP
  (Stand Up Paddleboard) foil wings. The terminology (wingspan, chord, aspect
  ratio) is shared with aviation but the product is a hydrofoil wing.
- RISK: Assuming model numbers represent anything other than wingspan
  REALITY: Each model number matches its wingspan in mm exactly (1401 = 1401mm,
  1201 = 1201mm, etc.)
- RISK: Assuming aspect ratio increases linearly with wingspan
  REALITY: The relationship is non-linear. Model 1201 has the lowest aspect
  ratio (11.14) despite being the second-largest wing.
- RISK: Confusing "actual area" with "projected area"
  REALITY: Both are listed as separate columns. Actual area is consistently
  larger than projected area (by ~2-3%). Projected area is the planform
  projection.
- RISK: Reading superscript digits as regular digits (e.g., "cm2" as "cm 2")
  REALITY: The 2 and 3 in cm2, cm3, in2, in3 are superscript notation for
  squared and cubed units.

### Detail Inventory [-> Information Recovery]

- Model number cells: dark charcoal/gray background (#4A4A4A approximate),
  bold white text, large font
- Header text: medium gray (#999999 approximate), lowercase, smaller font,
  some headers wrap to 2-3 lines ("mean average chord", "actual area",
  "projected area", "aspect ratio")
- Data text: dark gray/black, regular weight (except row 1 which is bold)
- Alternating row backgrounds: white and very light gray (#F5F5F5 approximate)
- No visible grid lines or borders between cells
- No table title or brand name visible in the image
- Minimalist, modern design aesthetic
- Image dimensions: approximately 1024x179 pixels
- WebP format, clean rendering, no compression artifacts visible
- Units consistently formatted: Xmm (X.XXin), Xcm2 (Xin2), Xcm3 (Xin3)
- Decimal precision: wingspan imperial to 1 decimal, chord imperial to 2
  decimals, mean average chord to 1 decimal, areas to 1 decimal, volume to
  1 decimal, aspect ratio to 2 decimals

### Domain Context [-> Retrieval Value]

ArtPro is a brand of hydrofoil wings used in SUP (Stand Up Paddleboard)
foiling and wing foiling. The table lists technical specifications for 6 wing
sizes in the ArtPro range:

- **Wingspan** (also called span): tip-to-tip measurement of the wing
- **Chord**: width of the wing from leading edge to trailing edge at the
  widest point
- **Mean average chord**: average chord length across the full span
- **Actual area**: true surface area of the wing including curvature
- **Projected area**: planform area as seen from directly above (always
  slightly less than actual area due to wing curvature/anhedral)
- **Volume**: internal volume of the wing (relevant for buoyancy and
  structural stiffness)
- **Aspect ratio**: wingspan2 / projected area; higher values indicate a
  longer, narrower wing (more efficient glide, less drag, but less
  maneuverable)

The model numbers (1401, 1201, etc.) directly correspond to wingspan in mm.
Larger wings provide more lift and stability at lower speeds; smaller wings
are more maneuverable and suited to higher wind/speed conditions.

### Search Keywords [-> Retrieval Value]

ArtPro, foil wing, SUP foil, hydrofoil, wing specifications, wingspan, chord,
aspect ratio, projected area, actual area, volume, standup paddleboard, wing
foiling, product table, specification table

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A table with wing measurements" -- no model names, no values, no units. Or: states incorrect values (e.g., says 1401 has 12.05 AR when it reads 12.17). Since all values are labeled text, exact match is expected; any fabricated number triggers the hallucination cap. | Names all 6 models, identifies all 7 column headers correctly, reports flagship 1401 values accurately. Minor imprecision on secondary model values (e.g., rounds 107.7mm to 108mm for the 1201's mean average chord). | All 6 model names exact. All column headers exact. All reported values match the table precisely (labeled text = exact match required). Correctly notes metric+imperial dual units, metric-only mean average chord. No fabricated values. Notes non-monotonic aspect ratio (1201 lowest at 11.14). |
| Information Recovery | Identifies image as a data table, names 1-2 models and 1-2 columns. No specific values extracted. A search for "1201 aspect ratio" would not match. Most of the table's 48 data values are invisible to the system. | All 6 models named, all 7 column headers identified, flagship 1401 row values extracted, dual unit system noted. Some secondary model values missing. "ArtPro 1401 wingspan" would match but "ArtPro 951 volume" might not. | Near-complete value recovery: all 6 models with key measurements across all columns. 8-column structure documented (unlabeled model + 7 named). Both metric and imperial values captured. Any value visible in the table is findable in the annotation -- parity principle met. |
| Retrieval Value | "A product table" -- no domain vocabulary, not self-contained. A user searching "hydrofoil wing specifications" or "ArtPro foil" would not find this. Depends on surrounding page context to be meaningful. | "ArtPro foil wing specs: 6 sizes from 951mm to 1401mm wingspan. Key measurements for comparing wing performance." Contains product name and basic domain terms. Partially self-contained. | Natural prose identifying these as ArtPro SUP/wing foil hydrofoil wings. Domain vocabulary embedded (wingspan, chord, aspect ratio, projected vs actual area). Notes model number = wingspan in mm and non-monotonic AR relationship. Self-contained without the source webpage. Findable by "hydrofoil wing comparison", "ArtPro specifications", or "foil wing aspect ratio". |

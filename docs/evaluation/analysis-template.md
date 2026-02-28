# Image Analysis Template

Instructions for recording per-image ground truth during the second evaluation
pass. Each section maps to a rubric scoring dimension so that annotation quality
can be assessed against concrete, image-specific reference material rather than
generic descriptions.

> **Related:** [Evaluation README](./README.md) |
> [Annotation Test Set](./annotation-test-set.md) |
> [Image Catalog](../image-catalog.md)

<br><br>

## Document Header

Include once per file. Establishes the document context that applies to all
images analyzed within it.

```text
# Image Analysis: Doc NN -- filename

**Document:** [filename]
**Format:** [PDF / DOCX / PPTX / WebP / PNG / JPG]
**Source:** [URL]
**Category:** [multi-image / vector-heavy / text-heavy / scanned / table-image / etc.]
**Eval subset images:** [count]
**Document context:** [1-2 sentences: what this document is about, what domain]
```

<br><br>

## Per-Image Sections

Repeat for each eval subset image from this document. Every section targets a
specific rubric dimension. Fill in every section -- leave none blank.

<br><br>

### Image Header

Identifies the image and classifies it for scoring.

```text
## doc{NN}-{ID} -- [short description from catalog]

**Figure reference:** [e.g., "Figure 1.1, page 8" or "Slide 36"]
**Content type:** [chart-simple / chart-complex / diagram / table-image /
                    equation / infographic / photo / screenshot / other]
**Annotation difficulty:** [Easy / Medium / Hard]
**Dimensions:** [WxH pixels for raster, or "vector" for vector figures]
```

<br><br>

### Visual Inventory [-> Completeness]

Enumerate every significant visual element in the image. Use the
content-type-specific format that matches this image's content type. If the
image spans multiple types (e.g., an infographic containing charts), use all
applicable formats.

This section feeds the **Completeness** dimension (25%): scoring checks whether
the annotation mentioned these elements.

#### Charts (`chart-simple`, `chart-complex`)

- **Chart type:** bar / line / scatter / pie / heatmap / area / histogram / etc.
- **Axes:**
  - X-axis label and units
  - Y-axis label and units
  - Scale type (linear / log) and range
- **Data series:** list each series with identifying color, pattern, or label
- **Specific values:** numbers readable from the chart (axis ticks, data
  labels, annotations)
- **Trend directions:** for each series (rising, falling, flat, non-monotonic)
- **Legend:** content and position
- **Annotations:** callouts, reference lines, error bars, confidence bands
- **Panels:** if multi-panel, list each panel with its own inventory

#### Diagrams

- **Components/nodes:** each labeled box, shape, or entity
- **Connections:** arrows, lines, or edges with labels and direction
- **Hierarchy or flow direction:** top-to-bottom, left-to-right, cyclic, etc.
- **Layers or groupings:** visual clusters, swim lanes, containment
- **Annotations or callouts:** text labels not part of nodes/edges
- **Style elements that carry meaning:** color coding, line styles (dashed,
  solid), shape types (rectangle vs diamond)

#### Photos

- **Primary subject:** what the photo shows
- **Setting/environment:** indoor/outdoor, context clues
- **Notable objects or details:** secondary elements visible in the frame
- **Scale indicators:** if any (rulers, known objects for size reference)
- **Text visible in the photo:** signs, labels, captions
- **Composition:** panels, sequence, collage (if multi-panel photo composite)

#### Tables (`table-image`)

- **Column headers:** exact text of each header
- **Row labels:** exact text of row identifiers
- **Dimensions:** row count x column count
- **Key values:** corners, totals, notable cells, min/max entries
- **Formatting that carries meaning:** color coding, bold, shading, borders

#### Screenshots

- **Application/UI identified:** what software or interface is shown
- **Text content:** readable text in the screenshot
- **UI elements and their state:** buttons, menus, selections, highlights
- **What action or state is being shown:** the purpose of the screenshot
- **Code content:** if showing code, the language and key constructs visible

#### Equations

- **Variables and their meanings:** each symbol defined
- **Mathematical operations:** operators, functions, subscripts, superscripts
- **What the equation represents:** in plain language
- **Relationship to surrounding context:** what this equation is used for
- **Notation conventions:** if non-standard notation is used

#### Infographics

- **Sections/panels identified:** layout structure
- **Data points with values:** specific numbers shown
- **Visual hierarchy:** primary, secondary, and supporting elements
- **Text blocks and their content:** headings, body text, callouts
- **Embedded charts or diagrams:** inventory using the applicable format above
- **Color coding or visual encoding:** what colors/icons mean

#### Other / Mixed

Use whichever sections above apply. Describe the content type and list all
significant elements using the most relevant format.

<br><br>

### Verifiable Facts [-> Accuracy]

Bullet list of specific claims that can be verified against the image. Each fact
is something an annotation might state correctly or incorrectly. This section
feeds the **Accuracy** dimension (30%).

Format each entry as:

```text
- FACT: [statement that is true based on the image]
```

**What makes a good verifiable fact:**
- Specific and falsifiable (not "the chart shows data" but "the x-axis label
  reads 'Trajectories (thousands)'")
- Directly observable in the image (not inferred from document context)
- Covers different aspects: labels, values, counts, relationships, positions

**Examples:**

```text
- FACT: The x-axis label reads "Trajectories (thousands)"
- FACT: The bar for GPT-4 is taller than the bar for GPT-3.5
- FACT: There are exactly 6 data series in the legend
- FACT: The trend line slopes upward from 2020 to 2024
- FACT: The top-left panel shows "Gridworld Off-Policy"
```

<br><br>

### Hallucination Risks [-> Accuracy]

List plausible-sounding claims a model might fabricate for this image. This
section also feeds the **Accuracy** dimension (30%) by identifying what to watch
for during scoring.

Format each entry as:

```text
- RISK: [what a model might say]
  REALITY: [what is actually true]
```

**Common fabrication patterns by content type:**

- **Charts:** inventing specific values not readable from the image, wrong trend
  direction, wrong number of data series, fabricated axis labels
- **Diagrams:** adding components not in the diagram, wrong connection
  direction, fabricated labels, inventing layers
- **Photos:** misidentifying species/objects, fabricating text not visible,
  wrong spatial relationships, wrong count of items
- **Tables:** wrong values, wrong row/column counts, fabricated headers,
  inventing data not in the table
- **Screenshots:** wrong UI element identification, fabricated text content,
  wrong application name
- **Equations:** wrong variable names, wrong operations, wrong meaning,
  inventing terms not present
- **Infographics:** wrong data values, fabricated section labels, wrong
  visual hierarchy

**Examples:**

```text
- RISK: "The chart shows GPT-4 achieving 95% accuracy"
  REALITY: No specific percentage is readable from the bar height
- RISK: "The diagram includes a Redis cache component"
  REALITY: No caching layer is shown in this diagram
```

<br><br>

### Detail Inventory [-> Specificity]

List all concrete, specific details visible in the image that a high-quality
annotation would reference. This section feeds the **Specificity** dimension
(25%).

These are the details that separate a specific annotation ("6 data series with
confidence bands across 1000 trajectories") from a generic one ("a line chart
about data"). Include:

- Exact text of all labels, titles, and captions
- Specific numeric values visible in the image
- Color descriptions tied to meaning ("blue line = Method A")
- Spatial relationships between elements
- Count of elements (panels, bars, nodes, rows)
- Any detail that, if omitted, would make the annotation less informative

<br><br>

### Domain Context [-> Usefulness]

Background knowledge needed to interpret this image. This section feeds the
**Usefulness** dimension (20%).

- **Domain:** what field or topic this image belongs to
- **Surrounding document context:** what the document text says about this
  figure (figure caption, preceding paragraph)
- **Technical terminology:** terms a reader would need to understand
- **Why this image matters:** what point it makes in the document's argument

<br><br>

### Search Keywords [-> Usefulness]

Terms that should surface this image in a document search system. This section
also feeds the **Usefulness** dimension (20%).

Include:
- **Domain terms:** e.g., "reinforcement learning", "off-policy evaluation"
- **Specific entities:** e.g., "GPT-4", "Gemini", "Bluemix"
- **Visual content type terms:** e.g., "heatmap", "scatter plot", "flowchart"
- **Topic-level terms:** e.g., "benchmark comparison", "architecture overview"

<br><br>

### Annotation Quality Anchors

Concrete examples of what scores 40, 70, and 95 on each dimension for THIS
specific image. This makes the rubric calibration image-specific rather than
relying on generic scoring band descriptions.

```text
| Dimension     | Score 40 (poor)   | Score 70 (good)   | Score 95 (excellent) |
|---------------|-------------------|-------------------|----------------------|
| Accuracy      | [example]         | [example]         | [example]            |
| Specificity   | [example]         | [example]         | [example]            |
| Completeness  | [example]         | [example]         | [example]            |
| Usefulness    | [example]         | [example]         | [example]            |
```

Fill in each cell with a concrete description of what an annotation at that
score level would look like for this particular image. For example:

- **Accuracy 40:** "States the chart shows 5 data series when there are
  actually 6; misidentifies the y-axis as 'accuracy' when it reads 'MSE'"
- **Accuracy 95:** "All stated values, labels, and relationships match the
  image exactly; no fabricated details"

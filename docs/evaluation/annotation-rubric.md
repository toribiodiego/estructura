# Annotation Quality Rubric

Scoring guide for evaluating VLM-generated image annotations against
per-image ground truth. This rubric measures annotation quality in the
context of a text-only RAG pipeline: annotations must recover visual
information so it becomes queryable and answerable.

> **Related:** [Analysis Template](./analysis-template.md) |
> [Annotation Test Set](./annotation-test-set.md) |
> [Image Catalog](../image-catalog.md) |
> [Annotation Role in RAG](../../notes/annotation-role-in-rag.md)

<br><br>

## Scope

**What this rubric evaluates:** The quality of a VLM-generated annotation
for a single image, scored against image-specific ground truth recorded in
the analysis files (`docs/evaluation/image-analysis/`).

**What this rubric does NOT evaluate:**
- Pipeline image capture (whether the image was extracted at all)
- Image crop quality (whether the crop is complete and well-framed)
- Processing speed or resource usage
- Prompt engineering or context-level choices

Pipeline capture quality is evaluated separately. See
[Annotation Role in RAG](../../notes/annotation-role-in-rag.md) for the
distinction between pipeline evaluation and annotation evaluation.

<br><br>

## Core Principle: Information Recovery

Annotation is not captioning. Its purpose is to **recover visual-only
information so it can participate in text-based retrieval and answer
generation.** A chart's data values, a diagram's topology, a table's cell
contents -- these exist nowhere in the document's text layer. Without
annotation, they are invisible to the RAG system.

This means the rubric evaluates annotations against a functional standard:
**does this annotation make the image's unique information as queryable as
the document's text-sourced information?** This is the parity principle.

<br><br>

## Dimensions and Weights

| Dimension | Weight | Core question |
|-----------|--------|---------------|
| Correctness | 40% | Is everything the annotation states actually true? |
| Information Recovery | 35% | Does the annotation capture the image's queryable information? |
| Retrieval Value | 25% | Will this annotation work in the RAG pipeline? |

**Weighted score:**
`score = (correctness * 0.40) + (information_recovery * 0.35) + (retrieval_value * 0.25)`

### Why 40 / 35 / 25

**Correctness (40%)** gets the highest weight because hallucination is the
worst failure mode in RAG. A wrong answer creates confident misinformation.
The error asymmetry is sharp: hallucination >> imprecision >> omission. An
annotation that says nothing is better than one that invents values.

**Information Recovery (35%)** is the core function of annotation. Did the
VLM extract the information the image uniquely contributes? This is where
the parity principle is enforced. Without recovery, the annotation exists
but adds no knowledge to the system.

**Retrieval Value (25%)** catches the gap between correct-and-complete
annotations that still fail in practice. An annotation could extract all
the right data but format it as a raw value dump that embeds poorly, or
lack domain vocabulary that users would query for, or depend on surrounding
text to make sense.

<br><br>

## Scoring Anchors

Each dimension is scored on a 0-100 scale. Scoring anchors describe what
an annotation looks like at each level.

### Dimension 1: Correctness (40%)

Every factual claim in the annotation is checked against the image. No
tolerance for fabrication; graded tolerance for imprecision (see
[Value Tolerance Bands](#value-tolerance-bands)).

| Score | Level | Description |
|-------|-------|-------------|
| 0-20 | Critical failure | Major hallucinations: invents data series, components, or values not in the image. Misidentifies the fundamental subject (calls a pie chart a bar chart, describes a circuit diagram as a flowchart). The annotation describes something materially different from the image. |
| 21-40 | Significant errors | Core subject correctly identified but contains hallucinated specifics. States a wrong trend direction ("declining" when the chart shows growth). Invents labels or entities not present. Gets the count of elements wrong (says 5 series when there are 9). Multiple factual errors that change interpretation. |
| 41-60 | Moderate errors | Broadly correct identification and description. Contains specific factual errors: misreads values beyond tolerance bands, confuses series names, attributes a label to the wrong element, gets a secondary detail wrong. No invented entities, but existing ones are described inaccurately. |
| 61-80 | Minor errors | All major claims are correct and verifiable. Minor inaccuracies at or near tolerance bounds (reads "approximately 280W" when the actual value is 275W). Slight imprecision in spatial descriptions. No errors that would change a user's understanding of the image. |
| 81-100 | Accurate | All stated facts verifiable from the image. Values within tolerance bands. No hallucinations of any kind. Appropriate hedging for approximate readings ("approximately", "roughly"). Precise where precision is possible (labels, names, counts). |

#### Hard Rules for Correctness

**Hallucination cap:** Any hallucinated entity -- inventing a data series
that does not exist, fabricating a component not in the diagram, stating a
value that cannot be read from the image -- caps the Correctness score at
40, regardless of how much else is correct. Hallucination is not a minor
error.

**Subject misidentification cap:** Fundamentally misidentifying the image
content (wrong chart type, wrong image subject) caps Correctness at 20.

**Imprecision is not hallucination:** Reading a chart value as "approximately
280W" when the actual value is 275W (~2% error) is imprecision within
tolerance for chart data. This does not trigger the hallucination cap.
Reading it as "375W" or "180W" is beyond tolerance and indicates either a
hallucination or a gross misread -- scored accordingly.

**Count errors:** Getting the count of data series, table rows, diagram
components, or other enumerable elements wrong by more than one is a
significant error (score <=40 range). Off-by-one errors where elements are
ambiguous (e.g., a faint gridline that could be mistaken for a data series)
are moderate errors (41-60 range).

<br><br>

### Dimension 2: Information Recovery (35%)

Measures whether the annotation extracts the queryable information the image
uniquely contributes. Scored against the per-image queryable entities list
(derived from the Visual Inventory and Detail Inventory sections of the
ground truth).

| Score | Level | Description |
|-------|-------|-------------|
| 0-20 | Near-zero recovery | Identifies only the image type ("a chart", "a table", "a diagram"). No entities named, no values extracted, no relationships described. A search query about any specific image content would not match. |
| 21-40 | Minimal recovery | Identifies the topic or subject area. Names 1-2 entities but misses most. Extracts at most one value. Missing all secondary elements. The annotation answers "what kind of image is this?" but nothing more specific. |
| 41-60 | Partial recovery | Main subject described with some detail. 30-50% of queryable entities captured. Some key values present but significant gaps. Missing important secondary elements (annotations, secondary series, structural details). Enough to answer broad queries but not specific ones. |
| 61-80 | Substantial recovery | Most queryable entities captured (60-80%). Key values and relationships described. Main patterns, trends, or structure identified. Minor gaps in secondary details (a few series unnamed, some cell values missing). Enough for most queries, but detailed questions may go unanswered. |
| 81-100 | Comprehensive recovery | All or nearly all queryable entities present (>80%). Key values extracted with appropriate precision. Relationships and patterns fully described. Self-contained: a chunk containing only this annotation could answer specific queries about the image content without requiring surrounding text. Parity principle met. |

#### What Counts as a Queryable Entity

A queryable entity is any element in the image that a user could reasonably
formulate a query about. The complete per-content-type definitions are in
[Queryable Entities by Content Type](#queryable-entities-by-content-type).

The scoring check: for each queryable entity in the ground truth, is it
recoverable from the annotation? "Recoverable" means either explicitly named
or clearly implied (e.g., "all 9 regulatory standards" implies all 9 are
present even if they are not individually listed -- but individually listing
them scores higher).

#### Recovery Expectations by Category

Not all images carry the same amount of unique information. The annotation
depth should match the image's information contribution category:

| Category | Expected recovery level for 81-100 |
|----------|------------------------------------|
| A (image IS the data): charts, tables, equations | Near-complete extraction of queryable entities and key values |
| B (structure/relationships): diagrams, workflows | All components named, connections described, flow direction captured |
| C (evidence/detail): microscopy, screenshots | Key visual details described, states and content identified |
| D (illustration): photos described by text | Primary subject identified, notable details the text omits mentioned |

A Category D image (illustrative photo) with a 60-word annotation that
correctly identifies the subject and notes a few details the text does not
mention may score 80-90 on Information Recovery. A Category A image (data
chart) with a 60-word annotation that names only half the series and no
values may score 40-50 despite being well-written.

<br><br>

### Dimension 3: Retrieval Value (25%)

Measures whether the annotation will actually work in the knoso RAG pipeline:
findable by relevant queries, self-contained without surrounding text, and
structured for good embedding quality.

| Score | Level | Description |
|-------|-------|-------------|
| 0-20 | No retrieval value | Would not surface in any relevant search. Missing domain vocabulary entirely. Fragmentary, incomprehensible, or so generic it matches everything and nothing ("an image with some content"). |
| 21-40 | Minimal retrieval value | Vague topic signal ("a chart about environmental data") but no useful keywords for specific queries. Not self-contained -- requires surrounding text to make sense. Poorly structured or disjointed. |
| 41-60 | Moderate retrieval value | Contains some domain vocabulary ("GHG emissions", "power consumption"). Topic-level searches would match. Partially self-contained but missing context that would make specific queries answerable. May be a raw data list rather than natural prose. |
| 61-80 | Good retrieval value | Natural language prose with embedded data values. Domain vocabulary present and appropriate. Self-contained for most queries -- a user could understand what the image shows from the annotation alone. Would surface in both broad and some specific searches. |
| 81-100 | Excellent retrieval value | Well-structured natural language prose. Rich domain vocabulary matching how users in this field would query. Fully self-contained -- an LLM could generate a useful, accurate answer from this annotation alone without needing surrounding text or the original image. Would surface in both broad topic queries and precise value-specific queries. |

#### Natural Language Over Data Dumps

Embedding models (ada-002, text-embedding-3-small, etc.) are trained on
natural language prose. An annotation written as flowing narrative with
embedded data embeds better than a raw data list.

**Good:** "The chart compares 9 electronic display power standards against
screen area. AU/NZ MEPS 2013 is the most permissive at approximately 275W
for 10,000 cm2 screens, while EU Grade C is the most stringent at
approximately 50W."

**Poor:** "AU/NZ-MEPS 2013: 275W. AU/NZ 4 star 2013: 140W. EU 2021 UHD:
95W. EU 2021 HD: 90W. EU 2023 HD: 85W. EU Grade F: 90W. Grade E: 75W.
Grade D: 55W. Grade C: 50W."

Both contain the same data. The first embeds into a semantic space where
"power standards comparison" queries match well. The second has all the
numbers but may embed poorly because it lacks natural language structure.

An annotation that is factually complete but formatted as a raw list scores
lower on Retrieval Value (typically 40-60) than one written as prose with
the same data embedded (70-90).

#### Self-Containment

Chunk boundaries in knoso are unpredictable. An annotation that depends on
surrounding paragraphs to be understood ("As shown in the figure above..."
or "This continues the trend from Figure 2...") fails the self-containment
test. The annotation should make sense when read in isolation.

Self-containment is a necessary condition for scores above 60.

<br><br>

## Value Tolerance Bands

VLMs read approximate values from visual elements. The rubric defines
acceptable tolerance by content type to distinguish imprecision (acceptable)
from error (penalized) from hallucination (capped).

| Content type | Tolerance | Imprecision example | Error example |
|-------------|-----------|---------------------|---------------|
| Charts (axis readings) | ~5-10% of actual value | "approximately 280W" for 275W actual | "350W" for 275W actual |
| Charts (labeled values) | Exact match | (labels should be read precisely) | "37.5%" for labeled "37.2%" |
| Tables-as-images | Exact match | (text is precise and readable) | "1301mm" for "1201mm" |
| Equations | Exact match | (mathematical content must be precise) | Wrong exponent or operator |
| Diagrams (text labels) | Exact match | (node names and labels are text) | "MongoDB" for "MariaDB" |
| Diagrams (spatial) | Approximate | "to the left of" for "above and left of" | Reversing flow direction |
| Photos | N/A (qualitative) | "reddish-brown" for "rust-colored" | "blue car" for a red car |
| Infographics | Exact for text, ~5% for visual quantities | Slight misread of a chart within the infographic | Wrong text label |

**Labeled vs unlabeled values:** When a chart has explicit data labels
(e.g., "37.2%" annotated on a data point), the tolerance is exact match --
the VLM should read the label text. When values must be estimated from axis
position (e.g., reading a bar height against a y-axis), the ~5-10% tolerance
applies.

<br><br>

## Queryable Entities by Content Type

These lists define what Information Recovery evaluates for each content type.
They correspond to the Visual Inventory and Detail Inventory sections of
the per-image ground truth.

### Charts (simple and complex)

- Chart title (if present)
- All series or category names
- Axis labels and units
- Key values: maxima, minima, notable data points, labeled values
- Trend direction and notable patterns (crossovers, inflections, plateaus)
- Annotations or callouts within the chart
- Legend content (series identification)
- For multi-panel charts: all panel subjects and their individual content

**Example -- doc04-V01 (8-panel chart):** 8 panel titles (SOC group names),
24 labeled percentage values, 8 trend descriptions, overall title, time
range (Jan-Aug 2025), varying y-axis scales. Full recovery requires
naming all 8 groups and their values.

### Diagrams

- All labeled nodes or components
- Key relationships and connections (what connects to what)
- Direction of flow (if applicable)
- Grouping, layering, or containment
- Title and labels
- Meaningful style elements (dashed vs solid lines if they signify different
  relationship types)

**Example -- doc05-V03 (data flywheel diagram):** All stage names, the
cyclical flow direction, input/output at each stage, any labeled arrows.

### Tables-as-images

- Column and row headers
- All cell values (per the parity principle -- every cell is a potential
  query target)
- Table title (if present)
- Units and formatting context
- Any footnotes or annotations

**Example -- doc13-R01 (foil wing table):** 6 model numbers, 7 column
headers, 42 cell values (6 models x 7 measurements). Complete recovery
means every cell value is retrievable from the annotation.

### Equations and pseudocode

- The complete mathematical expression or algorithm steps
- Variable names and their roles (what each symbol represents)
- Surrounding labels or equation/algorithm identifiers
- Key operations and their meaning

**Example -- doc11-R01 (TD(0) pseudocode):** Algorithm title, input
specification, initialization, both loop structures, the TD update rule
`V(S) <- V(S) + alpha[R + gamma V(S') - V(S)]`, state transition, and
termination condition.

### Photos

- Primary subject identification
- Notable details not described in surrounding text
- Setting and context visible in the image
- Any text visible within the photo
- For composite photos: all panels and their content

**Example -- doc05-R06 (cooking photo):** Subject (omelet cooking in pan),
visible details (egg in pan, spatula, kitchen setting). Category D -- light
annotation sufficient.

### Screenshots

- Application or interface identified
- Key UI elements and their states
- Data or text visible on screen
- Workflow context (what action or state is being shown)

**Example -- doc25-R08 (VA medical system):** Application name, visible
patient data fields, menu/navigation state, form content.

### Infographics

- All text content (headings, labels, values, descriptions)
- Visual structure (hierarchy, grouping, flow)
- Key data points and their relationships
- Source attributions (if visible)
- Any embedded charts or diagrams (apply the relevant type's entities)

**Example -- doc01-V01 (harmful content comparison):** All column headers,
all row entries (7 pairs), category labels, any severity indicators.

<br><br>

## Hard Rules

These override the standard scoring bands. Apply before computing the
weighted score.

| Rule | Trigger | Effect |
|------|---------|--------|
| Hallucination cap | Annotation invents an entity, value, or relationship not in the image | Correctness capped at 40 |
| Subject misidentification cap | Annotation fundamentally misidentifies the image (wrong chart type, wrong subject) | Correctness capped at 20 |
| Self-containment floor | Annotation requires surrounding text to be understood | Retrieval Value capped at 60 |
| Empty annotation | Annotation is blank, minimal ("an image"), or a refusal | All dimensions score 0-10 |

**Hallucination vs omission:** Omitting a data series is an Information
Recovery penalty. Inventing a data series triggers the hallucination cap on
Correctness. The distinction matters because their damage profiles differ:
omission means a query goes unanswered; hallucination means a query gets
a confidently wrong answer.

<br><br>

## Scoring Protocol

For each image in the evaluation subset:

### Step 1: Preparation

1. Open the source crop image (PNG/JPG/WebP)
2. Open the corresponding ground truth file
   (`docs/evaluation/image-analysis/{format}/doc{NN}-{name}.md`)
3. Open the annotation to be scored

### Step 2: Score Correctness (40%)

Score this dimension FIRST, before reading the other dimensions' ground
truth sections. This prevents anchoring from the completeness checklist.

1. Read the annotation end to end
2. For each factual claim, check against the image:
   - Is this entity actually in the image?
   - Is this value readable from the image? Within tolerance?
   - Is this relationship (trend, comparison, connection) correct?
3. Cross-reference against the Verifiable Facts and Hallucination Risks
   sections of the ground truth
4. Apply hard rules (hallucination cap, subject misidentification cap)
5. Assign score (0-100)
6. Write 1-2 sentence justification citing specific correct or incorrect
   claims

### Step 3: Score Information Recovery (35%)

1. Review the Visual Inventory and Detail Inventory sections of the
   ground truth
2. Build the queryable entities list for this image
3. Check each entity against the annotation:
   - Present and accurately described? (full credit)
   - Present but vague or imprecise? (partial credit)
   - Absent? (no credit)
4. Consider the image's information contribution category (A/B/C/D) when
   setting expectations
5. Assign score (0-100)
6. Write 1-2 sentence justification noting what was captured and what
   was missed. Optionally note the fraction of queryable entities found.

### Step 4: Score Retrieval Value (25%)

1. Read the annotation as if you are the RAG system -- would this text
   surface in a relevant search?
2. Check for:
   - Natural language prose (vs raw data dump)
   - Domain vocabulary (from the Domain Context and Search Keywords
     sections of the ground truth)
   - Self-containment (would this make sense without surrounding text?)
3. Assign score (0-100)
4. Write 1-2 sentence justification

### Step 5: Compute Weighted Score

```text
weighted = (correctness * 0.40) + (information_recovery * 0.35) + (retrieval_value * 0.25)
```

### Step 6: Record Additional Metrics

See [Additional Metrics](#additional-metrics) below.

<br><br>

## Pairwise Comparison Protocol

When comparing two annotation sources (e.g., Docling native vs custom
pipeline, or model A vs model B):

1. Score annotation A for all three dimensions using the protocol above
2. Score annotation B for all three dimensions **independently** -- do NOT
   look at annotation A's scores before completing annotation B's scores
3. Only after both are scored independently, compare:
   - Weighted score difference
   - Per-dimension score differences
   - Which images show the largest gaps
4. Document which annotation source performed better on each dimension

**Why independent scoring:** Anchoring bias causes the second annotation
to be scored relative to the first rather than against the absolute rubric.
Independent scoring prevents this.

<br><br>

## Calibration Process

Before running the full evaluation, calibrate the rubric on a small sample
to ensure consistent scoring.

### Step 1: Select calibration images

Pick 8-10 images that span:
- At least 3 content types (chart, diagram, table, photo, etc.)
- All 3 difficulty levels (Easy, Medium, Hard)
- At least 2 information contribution categories (A, B, C, or D)
- At least 2 source formats (PDF, DOCX, PPTX, etc.)

### Step 2: Initial scoring

Score the calibration images using the rubric. Record scores and
justifications.

### Step 3: Human review

The human reviewer examines each score and justification:
- Does the score match the scoring anchor description?
- Is the justification specific and evidence-based?
- Are hard rules applied correctly?
- Are tolerance bands applied consistently?

### Step 4: Identify disagreements

For each score where human and scorer disagree by more than 10 points:
- Document the disagreement
- Identify whether the rubric language is ambiguous
- Adjust rubric criteria or scoring anchors to resolve the ambiguity

### Step 5: Second round

Score a fresh batch of 5 images using the adjusted rubric. If agreement
is within +/-10 on >80% of dimension scores, calibration is complete.

### Step 6: Document calibration

Record in the calibration log:
- Which images were used
- Scores before and after adjustment
- What rubric changes were made and why
- Any systematic biases discovered (e.g., "tendency to over-score
  Information Recovery on charts because labeled values feel complete even
  when trend descriptions are missing")

**Calibration is complete when:** Human spot-checks show consistent agreement
with scorer's outputs, and the scorer can explain their scores using rubric
language.

<br><br>

## Additional Metrics

Recorded alongside rubric scores but not part of the weighted score. These
provide diagnostic information for pipeline optimization.

| Metric | Type | How measured |
|--------|------|-------------|
| Annotation length | Integer (words) | Word count of the annotation text |
| Hallucination flag | Boolean | Does the annotation state anything contradicted by the image? |
| Hallucination detail | Text (optional) | What was hallucinated, if flagged |
| Language quality | Pass / fail | Grammatically correct, well-formed English |
| Format compliance | Pass / fail | Matches the output contract format |
| Information category | A / B / C / D | The image's information contribution category |
| Entity recovery fraction | Ratio (optional) | Queryable entities found / total queryable entities |

<br><br>

## Scoring Data Schema

JSON schema for collecting scoring data consistently across all images and
annotation sources.

```json
{
  "image_id": "doc04-V01",
  "content_type": "chart-complex",
  "difficulty": "Hard",
  "information_category": "A",
  "annotation_source": "gemini-2.0-flash",
  "annotation_text": "...",
  "scores": {
    "correctness": {
      "score": 75,
      "justification": "All 8 categories correctly identified. Trend directions correct for 7 of 8 panels. States Computer/Math at 37.2% (correct). Misreads Management as 3.1% for Aug 2025 (actual: 2.7%) -- beyond tolerance for a labeled value.",
      "hallucination_flag": false,
      "hallucination_detail": null,
      "hard_rule_applied": null
    },
    "information_recovery": {
      "score": 65,
      "justification": "Names all 8 SOC groups. Provides values for 5 of 8 panels. Misses Architecture/Engineering, Life/Physical/Social, and Office/Admin values. Describes 6 of 8 trend directions. Missing y-axis scale variation note.",
      "queryable_entities_found": 28,
      "queryable_entities_total": 42
    },
    "retrieval_value": {
      "score": 80,
      "justification": "Natural prose with embedded data. 'SOC major groups', 'Claude.ai usage', 'Economic Index' all present as domain terms. Self-contained. Would surface for queries about AI occupation usage trends."
    }
  },
  "weighted_score": 72.75,
  "additional_metrics": {
    "annotation_length_words": 156,
    "language_quality": "pass",
    "format_compliance": "pass"
  },
  "metadata": {
    "context_level": "minimal",
    "model": "gemini-2.0-flash",
    "prompt_version": "v1",
    "scored_by": "claude-evaluator",
    "scored_at": "2026-03-01"
  }
}
```

<br><br>

## Concrete Scoring Examples

These examples illustrate how the rubric applies to real images from the
evaluation subset. Each shows what different score levels look like for
a specific image.

### Example 1: doc19-R06 (Category A -- chart, Medium difficulty)

**Image:** 9-line chart comparing electronic display power consumption
standards against screen area. 9 named regulatory standard lines with
distinct colors and styles.

**Ground truth queryable entities:** 9 series names, axis labels (power W,
screen area cm2), axis ranges (0-300W, 0-10000cm2), key values (AU/NZ MEPS
~275W, Grade C ~50W), approximate linearity of all lines, convergence at
small screen areas.

**Annotation A (Correctness: 85, Recovery: 75, Retrieval: 80):**
"Multi-line chart comparing 9 electronic display power consumption standards
against screen area (0 to 10,000 cm2). AU/NZ MEPS 2013 is the most
permissive, reaching approximately 275W for the largest screens. AU/NZ 4
star 2013 is roughly half at around 140W. EU standards cluster lower: EU
MEPS 2021 and 2023 variants around 85-95W, EU energy label grades F through
C ranging from about 90W down to 50W. All lines are roughly linear and
converge near 10-25W at small screen areas."

- Correctness 85: All values within tolerance, no hallucinations, 9 series
  correctly counted, key relationships correct.
- Recovery 75: Names the aggregate groups but does not individually list
  all 9 series (EU standards summarized as clusters). Key values and
  patterns present but some granularity lost.
- Retrieval 80: Natural prose, domain terms present ("MEPS", "energy label
  grades", "power consumption"), self-contained.
- Weighted: 80.25

**Annotation B (Correctness: 30, Recovery: 45, Retrieval: 50):**
"Line chart showing 7 different energy efficiency standards for displays.
The chart shows power consumption on the y-axis and screen size on the
x-axis. Australian standards allow higher power consumption (up to 350W)
while European standards are more restrictive. The EU Grade A standard is
the most restrictive at about 30W."

- Correctness 30: Says 7 lines (actual: 9) -- hallucination cap applies,
  but this is a count error not an invented entity. More critically: 350W
  (actual ~275W, 27% error -- beyond tolerance), and "EU Grade A" does not
  exist in this chart (hallucinated entity -- cap at 40, but other errors
  push below 40).
- Recovery 45: Gets the overall concept (standards comparison, AU vs EU)
  but misses 2 series entirely, provides no individual series names, and
  the values given are wrong.
- Retrieval 50: Has some domain vocabulary ("energy efficiency", "standards")
  but the self-containment is undermined by inaccurate content. Would
  surface for broad queries but mislead on specifics.
- Weighted: 39.75

### Example 2: doc13-R01 (Category A -- table, Easy difficulty)

**Image:** Product specification table for 6 SUP foil wing models with 7
measurement columns (wingspan, chord, mean average chord, actual area,
projected area, volume, aspect ratio).

**Ground truth queryable entities:** 6 model numbers, 7 column headers,
42 cell values, dual metric/imperial units, no title.

**Annotation A (Correctness: 95, Recovery: 90, Retrieval: 85):**
"Specification table for 6 ArtPro SUP foil wing models (1401, 1201, 1121,
1051, 1001, 951). Columns: wingspan, chord, mean average chord, actual
area, projected area, volume, and aspect ratio. The largest model (1401) has
1401mm wingspan, 1647cm2 actual area, and 12.17 aspect ratio. The smallest
(951) has 951mm wingspan, 768cm2 actual area, and 12.01 aspect ratio.
All dimensions given in metric with imperial equivalents in parentheses.
Aspect ratios range from 11.14 (model 1201) to 12.17 (model 1401)."

- Correctness 95: All stated values exact matches. No hallucinations.
  Model names, column headers, and cited values all verifiable.
- Recovery 90: All 6 models named, all 7 columns listed, key values for
  extremes provided, unit format described. Does not reproduce all 42
  cell values, but the extremes and ranges are sufficient for most queries.
- Retrieval 85: Natural prose, product/domain terms present, self-contained,
  searchable by model number, measurement type, or product category.
- Weighted: 90.25

### Example 3: doc11-R01 (Category A -- pseudocode, Medium difficulty)

**Image:** Tabular TD(0) algorithm pseudocode from Sutton and Barto.

**Ground truth queryable entities:** Algorithm title, input specification,
initialization, loop structure (nested), TD update rule, state transition,
termination condition, all variable names.

**Annotation at score ~70 across dimensions:**
"Pseudocode for the Tabular TD(0) algorithm for estimating the state value
function. The algorithm iterates through episodes, taking actions according
to policy pi and updating state values using the temporal difference
update rule V(S) = V(S) + alpha * (R + gamma * V(S') - V(S)). It continues
until a terminal state is reached."

- Correctness ~75: The TD update uses `<-` (assignment) not `=`, and the
  brackets are rendered as parentheses with `*` instead of juxtaposition.
  Functionally equivalent but not exact. No hallucinations.
- Recovery ~70: Title, loop structure (mentioned but not detailed),
  TD update rule (present but slightly reformatted), termination condition
  all present. Missing: initialization step, input specification, the
  `S <- S'` state transition, the nested loop structure.
- Retrieval ~65: Natural prose, "TD(0)", "state value function",
  "temporal difference" are good domain terms. But the reformatted equation
  may not match queries looking for the exact notation.
- Weighted: ~70.5

<br><br>

## Mapping Ground Truth Sections to Rubric Dimensions

The per-image ground truth recorded in the analysis files
(`docs/evaluation/image-analysis/`) has 7 sections. They map to the 3
rubric dimensions as follows:

| Ground truth section | Primary dimension | How it informs scoring |
|---------------------|-------------------|----------------------|
| Visual Inventory | Information Recovery | Defines the queryable entities checklist |
| Verifiable Facts | Correctness | Provides specific claims to verify |
| Hallucination Risks | Correctness | Identifies likely fabrication patterns |
| Detail Inventory | Information Recovery | Lists concrete details to check for |
| Domain Context | Retrieval Value | Provides the domain vocabulary baseline |
| Search Keywords | Retrieval Value | Terms the annotation should contain |
| Quality Anchors | All dimensions | Image-specific scoring examples |

**Note:** The analysis template's Quality Anchors section currently
references the old 4-dimension rubric (Accuracy, Specificity, Completeness,
Usefulness). When updating ground truth files to align with this rubric,
the anchors should be rewritten for the 3 dimensions (Correctness,
Information Recovery, Retrieval Value). Existing ground truth content
remains valid -- the sections still contain the right information, only the
anchor examples need updating.

<br><br>

## Annotation Length Guidelines

These are guidelines for evaluating whether an annotation's length is
appropriate for its content type, not scoring criteria. An annotation
that is too short for its content type likely has Information Recovery
gaps. An annotation that is too long may be padding with visual styling
details that add no retrieval value.

| Information category | Target length | Rationale |
|---------------------|--------------|-----------|
| A (image IS the data) | 100-200 words | Must extract queryable entities and key values in natural prose |
| B (structure/relationships) | 75-150 words | Must capture topology and relationships |
| C (evidence/detail) | 50-100 words | Must describe visual specifics the text omits |
| D (illustration) | 30-50 words | Retrieval signal, not information recovery |

These ranges assume the annotation is written as natural language prose.
A raw data dump would need fewer words for the same coverage but would
score lower on Retrieval Value.

<br><br>

## Versioning

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-01 | Initial rubric: 3 dimensions (Correctness 40%, Information Recovery 35%, Retrieval Value 25%). Replaces the draft 4-dimension rubric from `tmp/task-17-eval/03-design-evaluation-rubric.md`. |

# Image Analysis: Doc 05 -- 05_gemini_multimodal_report.pdf

**Document:** `05_gemini_multimodal_report.pdf`
**Format:** PDF
**Source:** https://arxiv.org/pdf/2312.11805v5.pdf
**Category:** multi-image
**Images:** 31
**Document context:** Google Gemini technical report covering multimodal
capabilities across text, image, audio, and video. Includes benchmark
comparisons, architecture details, post-training methodology, and capability
demonstrations.

<br><br>

## doc05-R02 -- Handwritten physics problem + model response

**Figure reference:** Figure 1, page 3
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 4760x3421 pixels

**Note:** Unlike the Group A photos, this crop contains the full two-panel
Prompt/Response layout as part of the extracted image. The text described
below IS visible in the crop.

### Visual Inventory [-> Completeness]

- **Layout:** Two-panel side-by-side layout with "Prompt" header (left,
  white background) and "Response" header (right, light blue background);
  a small pen/pencil icon appears at the top left of the Prompt panel
- **Prompt panel (left) -- typed text at top:**
  - Opening line: "Here's a solution to a Physics problem by a student."
  - Problem number "23." with text: "A skier slides down the frictionless
    slope as shown. What is the skier's speed at the bottom?"
- **Prompt panel -- diagram:**
  - Simple line drawing of a slope: a horizontal line at bottom labeled
    "Finish" at right end, a diagonal line rising to the left labeled with
    height "H=40 m" (vertical) and length "L=80 m" (along slope), "Start"
    labeled at top of slope
  - A small red curved arrow/line near the top of the slope indicating the
    skier's starting path
- **Prompt panel -- handwritten student solution:**
  - "The conservation of energy means that the energy of the skier is same
    at the beginning and at the end"
  - "Start: E = mgL"
  - "End: E = 1/2 mv^2"
  - "=> mgL = 1/2 mv^2"
  - "=> v = sqrt(2gL) = sqrt(2 x 9.81 x 80) = 39.6 m.s^-1"
  - (Note: the student uses L=80 where H=40 should be used)
- **Prompt panel -- typed instruction text at bottom:**
  - "Try to reason about the question step by step."
  - "Did the student get the correct answer? If the solution is wrong,
    please explain what is wrong and solve the problem."
  - "Make sure to use LaTeX for math and round off the final answer to two
    decimal places."
- **Response panel (right) -- model's correction:**
  - Opening: "The student did not get the correct answer. The student made
    a mistake in the calculation of the potential energy at the start of
    the slope."
  - Identifies error: "The student used the length of the slope, L, instead
    of the height, H, in the calculation of the potential energy."
  - Step-by-step corrected solution with LaTeX-rendered equations:
    mgh = 1/2 mv^2, then gh = 1/2 v^2, then v = sqrt(2gh)
  - Final computation: v = sqrt(2 x 9.81 x 40) = 28.01 m/s
  - Concluding line: "Therefore, the skier's speed at the bottom of the
    slope is 28.01 m/s."
- **What action or state is being shown:** Gemini identifying and correcting
  a student's physics mistake (using slope length L instead of height H for
  potential energy)

### Verifiable Facts [-> Accuracy]

- FACT: The problem states the slope is frictionless
- FACT: The height H is labeled as 40 m in the diagram
- FACT: The slope length L is labeled as 80 m in the diagram
- FACT: The student's solution uses L=80 in the energy equation (E = mgL)
  instead of H=40
- FACT: The student arrives at v = 39.6 m.s^-1 (using SI notation, not m/s)
- FACT: The student uses g = 9.81 in the calculation
- FACT: The model's corrected answer is v = 28.01 m/s
- FACT: The model identifies the error as using slope length L instead of
  height H for potential energy
- FACT: The correct equation shown is v = sqrt(2gh)
- FACT: The prompt instructs to use LaTeX for math and round to two decimal
  places
- FACT: The layout has "Prompt" on the left (white) and "Response" on the
  right (light blue)
- FACT: Problem number is 23
- FACT: The opening line reads "Here's a solution to a Physics problem by
  a student."
- FACT: A small pen/pencil icon appears at the top left of the Prompt panel

### Hallucination Risks [-> Accuracy]

- RISK: A model might state the student used H instead of L
  REALITY: The student's error was using L (slope length, 80m) instead of H (height, 40m)
- RISK: A model might report the correct answer as 28.0 m/s or 28 m/s
  REALITY: The model response states 28.01 m/s (rounded to two decimal places)
- RISK: A model might claim the problem involves friction
  REALITY: The problem explicitly states the slope is frictionless
- RISK: A model might state the student used the wrong value of g
  REALITY: The student used g = 9.81 correctly; the error was using L instead of H
- RISK: A model might fabricate additional elements in the diagram (e.g., a
  skier figure, angle measurement)
  REALITY: The diagram shows Start, Finish, H=40 m, L=80 m, and a small red
  curve; no skier figure or angle value is drawn
- RISK: A model might state the student's units as "m/s" instead of "m.s^-1"
  REALITY: The handwritten answer uses SI notation "m.s^-1" (with superscript)
- RISK: A model might claim the response panel has a white background
  REALITY: The Response panel has a light blue background; the Prompt panel
  is white

### Detail Inventory [-> Specificity]

- Two-panel layout: "Prompt" (white, left) and "Response" (light blue, right)
- Pen/pencil icon at top left of Prompt panel
- Opening text: "Here's a solution to a Physics problem by a student."
- Physics problem number 23 about a skier on a frictionless slope
- Slope diagram with labeled parameters: H=40 m (height), L=80 m (slope
  length), Start at top, Finish at bottom, red curve near start
- Student's handwritten work: conservation of energy approach
- Student's specific error: using mgL instead of mgh for potential energy
- Student's incorrect answer: 39.6 m.s^-1 (using L=80)
- Model's correct answer: 28.01 m/s (using H=40)
- Model walks through correction step by step with LaTeX-rendered equations
- Prompt requests: LaTeX formatting, two-decimal-place rounding, step-by-step
  reasoning, identify and explain the error

### Domain Context [-> Usefulness]

- **Domain:** Physics education, conservation of energy, kinematics
- **Surrounding document context:** Figure 1 in the Gemini technical report,
  used as the opening demonstration of Gemini's multimodal reasoning capability.
  Shows the model can interpret handwritten work, identify mathematical errors,
  and provide corrections.
- **Technical terminology:**
  - Conservation of energy: principle that total energy remains constant
    (potential energy converts to kinetic energy for a frictionless slope)
  - Potential energy: mgh (mass x gravity x height), not mgl (mass x gravity
    x slope length)
  - Kinetic energy: 1/2 mv^2
- **Why this image matters:** It is the first figure in the paper, chosen to
  immediately demonstrate Gemini's ability to combine vision (reading a diagram
  and handwriting), mathematical reasoning (identifying the error), and
  instruction following (LaTeX, rounding).

### Search Keywords [-> Usefulness]

- Gemini, multimodal reasoning, physics problem
- conservation of energy, frictionless slope, skier
- handwritten solution, student error correction
- potential energy, kinetic energy, kinematics
- prompt response layout, error identification
- LaTeX math, step-by-step reasoning

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | States the student used the correct formula or reports the wrong answer value; confuses H and L roles | Correctly identifies the L-vs-H error and both answers (39.6 and 28.01); may misstate one parameter value | All values (H=40m, L=80m, g=9.81, 39.6 m/s, 28.01 m/s) match the image; correctly identifies which variable the student used and which is correct |
| Specificity | "A physics problem with a model response" -- no values, no formula, no error description | Names the conservation of energy approach, states the student got 39.6 m/s and the correct answer is 28.01 m/s, mentions slope vs height | Cites all labeled values, reproduces key equations (E=mgL vs E=mgH), mentions the two-decimal-place and LaTeX instructions, identifies problem number 23 |
| Completeness | Mentions only the prompt or only the response; omits the diagram or the handwritten work | Covers both panels, the diagram parameters, the student error, and the corrected solution; may omit the instruction text or specific equation steps | Accounts for both panels, the diagram with all labels, the handwritten solution steps, the specific error, the corrected solution, and the instruction text about LaTeX and rounding |
| Usefulness | "An image showing a math problem" -- not searchable, no domain context | Mentions Gemini, physics error correction, conservation of energy; enough context to find this image when searching for multimodal math reasoning | Includes the problem setup, the specific error type (slope length vs height), both numeric answers, and the educational/evaluation context within the Gemini technical report |

<br><br>

## doc05-R03 -- Gemini architecture overview

**Figure reference:** Figure 2, page 4
**Content type:** diagram
**Annotation difficulty:** Medium
**Dimensions:** 1383x617 pixels

### Visual Inventory [-> Completeness]

- **Components/nodes:**
  - "Input Sequence" label in the top-left corner
  - Input modality icons (left side, 4 stacked vertically, each in a
    color-coded square border):
    1. Text: blue "Aa" in blue-bordered square
    2. Audio: red vertical waveform bars in red-bordered square
    3. Image: green mountain/landscape icon in green-bordered square
    4. Video: yellow/orange play-button icon in yellow/orange-bordered square
  - Interleaved token sequence: rounded capsule/pill shape containing 6
    colored rectangles (blue, blue, red, yellow/orange, green, yellow/orange)
  - Central processing block: large blue rounded rectangle with white
    "Transformer" text
  - Output decoders (right side, 2 branches):
    - "Image Decoder" box with arrow to output icon (green mountain symbol
      with small sparkle/star decoration)
    - "Text Decoder" box with arrow to output icon (blue "Aa" with small
      sparkle/star decoration)
- **Connections:**
  - All 4 input icons connect via black lines into the token capsule
  - Token capsule feeds into the Transformer block via arrow
  - Transformer output splits into two branches (Image Decoder, Text Decoder)
  - Each decoder has an arrow to its respective output icon
- **Hierarchy or flow direction:** Left-to-right: inputs -> tokenization ->
  Transformer -> decoders -> outputs
- **Style elements that carry meaning:**
  - Each input icon border color matches its modality (blue=text, red=audio,
    green=image, yellow/orange=video)
  - Colored token segments represent interleaved multimodal tokenization
  - Output icons have sparkle decorations suggesting generated/enhanced content
  - Blue fill on Transformer block emphasizes it as the core component
  - White background throughout

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 4 input modality types (top to bottom): text,
  audio, image, video
- FACT: The central processing block is labeled "Transformer" in white text
  on a blue background
- FACT: There are exactly 2 output decoders: Image Decoder and Text Decoder
- FACT: The input tokens are in a rounded capsule/pill shape containing 6
  colored rectangle segments
- FACT: The token color sequence is: blue, blue, red, yellow/orange, green,
  yellow/orange
- FACT: The text icon is blue "Aa" in a blue-bordered square
- FACT: The audio icon is red waveform bars in a red-bordered square
- FACT: The image icon is a green mountain in a green-bordered square
- FACT: The video icon is a yellow/orange play button in a yellow/orange-
  bordered square
- FACT: Both output icons have small sparkle/star decorations
- FACT: The flow direction is left to right
- FACT: The label "Input Sequence" appears in the top-left corner

### Hallucination Risks [-> Accuracy]

- RISK: A model might claim there is an "Audio Decoder" output
  REALITY: Only two decoders are shown: Image Decoder and Text Decoder
- RISK: A model might state there are separate Transformer blocks for each modality
  REALITY: There is a single unified Transformer block processing all modalities
- RISK: A model might describe specific layer counts or attention head details
  REALITY: The diagram shows no internal architecture details of the Transformer
- RISK: A model might claim the diagram shows training vs inference paths
  REALITY: The diagram shows a single forward path with no training-specific annotations
- RISK: A model might state there is a "Video Decoder" output
  REALITY: Only Image Decoder and Text Decoder are shown on the output side

### Detail Inventory [-> Specificity]

- 4 input modalities with color-coded bordered icons (blue=text, red=audio,
  green=image, yellow/orange=video)
- "Input Sequence" label in the top-left corner
- Rounded capsule with 6 colored token segments (blue, blue, red,
  yellow/orange, green, yellow/orange)
- Single large blue Transformer block at center with white text
- Two output branches: Image Decoder (green mountain + sparkle icon) and
  Text Decoder (blue "Aa" + sparkle icon)
- Black connecting lines with arrows showing data flow
- Clean left-to-right flow with no feedback loops or skip connections
- Minimalist design with no internal architecture details
- White background throughout

### Domain Context [-> Usefulness]

- **Domain:** Deep learning architecture, multimodal language models
- **Surrounding document context:** Figure 2 in the Gemini technical report,
  appearing early in the paper to establish the high-level architecture. It
  shows that Gemini is a unified multimodal model that accepts multiple input
  types and can produce both text and image outputs through a single
  Transformer.
- **Technical terminology:**
  - Transformer: the core neural network architecture
  - Multimodal: processing multiple data types (text, audio, video, image)
  - Tokenization: converting raw inputs into discrete tokens for the model
  - Decoder: output module that converts model representations into a
    specific modality
- **Why this image matters:** Establishes the fundamental design principle of
  Gemini -- a single Transformer handling all modalities natively, rather than
  separate specialist models stitched together.

### Search Keywords [-> Usefulness]

- Gemini, architecture, Transformer, multimodal
- text audio video image, input modalities
- Image Decoder, Text Decoder, output
- model architecture, unified model
- tokenization, multimodal tokens

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies the number of input modalities or invents outputs not shown (e.g., "Audio Decoder") | Correctly identifies all 4 inputs, the Transformer, and both decoders; may fabricate minor details like internal layer counts | All components, labels, and connections match exactly; no fabricated architectural details |
| Specificity | "A diagram of a neural network" with no specific labels or modality names | Names the 4 input types, the Transformer block, and both decoders; mentions the left-to-right flow | Describes the colored token row, the specific icon types (Aa, waveform, film strip, mountain), both decoder labels, and the unified single-Transformer design |
| Completeness | Mentions only the Transformer or only the inputs; omits the output decoders or the token row | Covers inputs, Transformer, and outputs; may omit the colored token sequence or the specific icon descriptions | Accounts for all 4 input icons, the colored token row, the Transformer block, both output decoders with their icons, and the overall flow direction |
| Usefulness | "A model architecture diagram" -- no model name, no modality details | Mentions Gemini, multimodal inputs, unified Transformer; enough context to understand the basic design | Explains the significance of a single Transformer for all modalities, names all input/output types, and relates the diagram to the paper's argument about native multimodal processing |

<br><br>

## doc05-R04 -- Multimodal matplotlib code gen composite

**Figure reference:** Figure 5, page 15
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 4760x5014 pixels

**Note:** Like R02, this crop contains the full Prompt/Response panels and a
rendered output section. All text and plots described below are visible in
the extracted crop.

### Visual Inventory [-> Completeness]

- **Layout:** Three sections stacked vertically:
  1. Top: side-by-side Prompt (white, left) and Response (light blue, right)
     panels, each with header text
  2. Bottom: "Rendered code" section (white background, smaller) showing
     output of the generated code
- **Prompt panel (top left):**
  - Pen/pencil icon at top left
  - Instruction text describing the rearrangement task: put the 3D
    paraboloid top-left, tangent function bottom-right; for the remaining
    two, one stays in place and the other fills the last spot; describe
    each subplot, explain rearrangement, then write the full code
  - 2x2 grid of matplotlib subplots (original arrangement):
    - Top-left: sine wave (blue line, oscillating curve)
    - Top-right: tangent function (blue line with vertical asymptotes)
    - Bottom-left: exponential curve (blue line, rising curve)
    - Bottom-right: 3D surface/paraboloid (colorful surface with viridis
      colormap, rendered with wireframe visible)
- **Response panel (top right):**
  - Lists current subplot arrangement (4 bullets)
  - Lists new subplot arrangement (4 bullets):
    - Top left: The 3D paraboloid
    - Top right: The sine wave
    - Bottom left: The exponential function
    - Bottom right: The tangent function
  - Python code with syntax highlighting (colored text): imports (numpy,
    matplotlib.pyplot, mpl_toolkits.mplot3d), figure creation, 4 subplot
    blocks with comments in red/pink, data generation, plotting calls,
    plt.show()
- **Rendered code section (bottom):**
  - Monitor/screen icon at top left
  - "Rendered code" header text
  - 2x2 grid showing the rearranged subplots matching the Response's
    described new arrangement
- **What action or state is being shown:** Gemini interpreting visual
  mathematical plots, understanding the rearrangement instruction, and
  generating working matplotlib Python code that produces the correct output

### Verifiable Facts [-> Accuracy]

- FACT: The prompt contains a 2x2 grid of 4 matplotlib subplots
- FACT: The four plot types are: sine wave, tangent function, exponential
  curve, and 3D surface/paraboloid
- FACT: Original arrangement: sine (top-left), tangent (top-right),
  exponential (bottom-left), 3D paraboloid (bottom-right)
- FACT: The instruction asks to rearrange subplots so the 3D paraboloid
  moves to top-left and tangent to bottom-right
- FACT: New arrangement per Response: 3D paraboloid (top-left), sine wave
  (top-right), exponential (bottom-left), tangent (bottom-right)
- FACT: The response panel contains Python code with syntax highlighting
  (colored text, red/pink comments)
- FACT: The code imports numpy, matplotlib.pyplot, and mpl_toolkits.mplot3d
- FACT: A "Rendered code" section appears below the Prompt/Response panels
- FACT: The rendered output is also a 2x2 grid matching the new arrangement
- FACT: Both grids contain the same 4 plot types
- FACT: The 3D surface uses a viridis-like colormap (green-yellow-blue)

### Hallucination Risks [-> Accuracy]

- RISK: A model might state specific axis ranges or tick values for the subplot plots that are not clearly readable at the image resolution
  REALITY: The subplots are relatively small within the composite and exact axis values may not be fully legible
- RISK: A model might claim the code uses a specific library version or import style not visible
  REALITY: Only the visible code content should be described
- RISK: A model might confuse which plot is in which position in the original vs rearranged grid
  REALITY: The original has sine (top-left), tangent (top-right), exponential (bottom-left), 3D surface (bottom-right)
- RISK: A model might state the rendered output uses different colors or styles than shown
  REALITY: The rendered output replicates the same plot styles from the prompt
- RISK: A model might claim there are 5 or 6 subplots
  REALITY: Both the input and output grids contain exactly 4 subplots in a 2x2 arrangement

### Detail Inventory [-> Specificity]

- Composite image with 3 distinct sections: Prompt panel, Response panel,
  Rendered code output
- Prompt shows 4 subplots: sine wave (top-left), tangent (top-right),
  exponential (bottom-left), 3D paraboloid (bottom-right)
- Instruction text specifies the desired rearrangement of all 4 subplots
- Response contains Python matplotlib code with the rearrangement logic
- Rendered output shows the rearranged 2x2 grid matching the instructions
- The task demonstrates visual comprehension of mathematical plots, not just
  text-based code generation
- The composite layout is vertically tall (4760x5014 pixels), spanning
  prompt/response and rendered output

### Domain Context [-> Usefulness]

- **Domain:** Code generation, data visualization, mathematical plotting
- **Surrounding document context:** Figure 5 in the Gemini report,
  demonstrating multimodal code generation. The model must visually interpret
  plots (not just read code), understand the rearrangement instruction, and
  generate correct matplotlib code.
- **Technical terminology:**
  - matplotlib: Python plotting library
  - subplot: individual plot within a multi-panel figure
  - 3D surface plot / paraboloid: three-dimensional mathematical surface
  - Rendering: executing the generated code to produce visual output
- **Why this image matters:** Demonstrates that Gemini can interpret visual
  content (plots), reason about spatial layout (subplot positions), and
  generate executable code -- combining vision, spatial reasoning, and code
  generation in a single task.

### Search Keywords [-> Usefulness]

- Gemini, code generation, matplotlib, Python
- subplot rearrangement, sine wave, tangent, exponential, 3D surface
- multimodal code generation, visual reasoning
- plot interpretation, data visualization
- paraboloid, rendered code output

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies the plot types or confuses original and rearranged positions; states wrong number of subplots | Correctly identifies all 4 plot types and the rearrangement task; may get one position wrong in the original or output grid | All 4 plot types correctly identified, positions in both original and rearranged grids are accurate, notes the Python/matplotlib code generation |
| Specificity | "Some matplotlib plots and code" with no plot types or positions named | Names the 4 plot types, mentions the rearrangement task, notes the rendered output section | Identifies each plot type and its position in both grids, describes the 3-section composite layout, and notes the visual-to-code reasoning task |
| Completeness | Describes only the plots or only the code; omits the rendered output section | Covers the prompt plots, the rearrangement instruction, and the response code; may omit the rendered output or exact position details | Accounts for all 3 sections (prompt with plots, response with code, rendered output), all 4 plot types, their positions in both grids, and the instruction text |
| Usefulness | "A code generation example" -- no plot types, no task description | Mentions multimodal code generation with matplotlib, subplot rearrangement; searchable for "Gemini code generation" | Explains the specific multimodal challenge (interpreting visual plots to generate code), names all plot types, and connects to the paper's argument about combined vision and code capabilities |

<br><br>

## doc05-R06 -- Omelet ingredients on counter

**Figure reference:** Table 13 image 1, page 19
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 4080x3072 pixels

**Note:** The image catalog describes this as "Cooking omelet in pan" but the
extracted crop shows ingredient preparation on a countertop. No pan is visible.
This is the first of three photos (R06, R07, R08) used in Table 13's multi-turn
cooking conversation demonstration.

### Visual Inventory [-> Completeness]

- **Primary subject:** Overhead view of omelet ingredients laid out on a white
  countertop before cooking
- **Eggs:** 2 brown eggs sitting on top of a clear plastic egg carton; the
  carton is mostly empty (several vacant wells visible)
- **Vegetables:** Stainless steel colander with handle, containing broccoli
  florets (at least 2 pieces), red/orange pepper pieces, a small whole
  yellow/orange bell pepper, and green vegetable pieces
- **Background packaging:** Egg carton packaging visible at top-left with a
  nutrition facts panel (Total Fat, Saturated Fat, Cholesterol, Sodium, Total
  Carbohydrate, Protein) and a blue label area reading "OMEGA 3"
- **Brand text:** "HEALTHY HENS, HEALTHY EGGS, HEALTHY PLANET" and "SWELL
  FAMILY FARMS" printed on the egg packaging
- **Other objects:** Edge of a wooden cutting board in the bottom-right corner
  with partial embossed text
- **Setting:** White countertop surface, overhead camera angle, natural or
  ambient lighting
- **No cooking equipment visible** -- no pan, no stove, no heat source

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 2 brown eggs visible
- FACT: The eggs sit on a clear plastic egg carton that is mostly empty
- FACT: A stainless steel colander with a handle holds the vegetables
- FACT: Broccoli florets are visible in the colander
- FACT: At least one small yellow/orange bell pepper is in the colander
- FACT: Red or orange pepper pieces are visible alongside the broccoli
- FACT: The egg packaging displays "OMEGA 3" prominently
- FACT: Text on the packaging reads "HEALTHY HENS, HEALTHY EGGS, HEALTHY
  PLANET"
- FACT: The brand name "SWELL FAMILY FARMS" appears on the packaging
- FACT: A nutrition facts panel is partially visible on the packaging
- FACT: A wooden cutting board edge is visible in the bottom-right corner
- FACT: The countertop surface is white
- FACT: No pan, stove, or cooking equipment is visible in the image

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as "cooking in a pan" based on the
  catalog description or surrounding table context
  REALITY: No pan or stove is visible; this shows ingredient preparation only
- RISK: A model might claim there are 3 eggs (a common default for omelets)
  REALITY: Exactly 2 eggs are visible on the carton
- RISK: A model might identify vegetables not present (e.g., onions, mushrooms,
  tomatoes)
  REALITY: Visible vegetables are broccoli, bell peppers (yellow/orange and
  red/orange pieces); no onions, mushrooms, or tomatoes
- RISK: A model might describe the colander as a "bowl" or "pan"
  REALITY: It is a stainless steel colander with visible drainage holes and a
  handle
- RISK: A model might describe this as a complete Table 13 with multiple rows
  of conversation
  REALITY: This crop is a single photo extracted from the table; the table
  structure and text are not part of this image

### Detail Inventory [-> Specificity]

- Egg count: exactly 2 brown eggs
- Egg carton: clear plastic, mostly empty, multiple vacant wells
- Colander: stainless steel with perforated holes, single handle visible
- Vegetables identifiable: broccoli (green florets), bell pepper (small whole
  yellow/orange), pepper pieces (red/orange)
- Packaging: blue-labeled egg carton with "OMEGA 3" branding, nutrition facts
  panel with standard nutrient rows, farm name "SWELL FAMILY FARMS"
- Tagline: "HEALTHY HENS, HEALTHY EGGS, HEALTHY PLANET"
- Cutting board: wooden, bottom-right corner, partial embossed text
- Camera angle: overhead / bird's-eye view
- Lighting: even, natural or ambient, no harsh shadows

### Domain Context [-> Usefulness]

- **Domain:** Food photography, cooking demonstration, multimodal AI evaluation
- **Surrounding document context:** This photo is the first of three images
  embedded in Table 13 of the Gemini technical report. Table 13 demonstrates
  multi-turn multimodal dialogue where the model receives images and
  transcribed audio across conversation turns about cooking a veggie omelet.
  This image accompanies the first turn where the user asks "What's the first
  step to make a veggie omelet with these ingredients?"
- **Technical terminology:**
  - Table 13: a demonstration table in the Gemini report showing interleaved
    image + audio inputs with model text responses
  - Multi-turn multimodal: conversation spanning multiple exchanges with
    different input types (image, audio, text)
- **Why this image matters:** It is the input photo for the first turn of a
  multi-turn cooking conversation, showing the model what ingredients are
  available. The model must identify the ingredients from this image to provide
  relevant cooking instructions.

### Search Keywords [-> Usefulness]

- Gemini, multimodal conversation, Table 13
- cooking ingredients, omelet preparation, food photography
- eggs, broccoli, bell pepper, colander, countertop
- SWELL FAMILY FARMS, OMEGA 3, egg packaging
- ingredient identification, visual understanding
- overhead photo, kitchen preparation

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Describes this as "cooking in a pan" or describes the full Table 13 conversation instead of this single photo; wrong egg count | Correctly identifies eggs and vegetables on a countertop; identifies the colander; may misidentify a vegetable or miss the packaging text | All items correctly identified (2 brown eggs, colander with broccoli and peppers, egg packaging with OMEGA 3 and SWELL FAMILY FARMS); correctly notes no pan is visible |
| Specificity | "A photo of food ingredients" with no detail about what ingredients or how they are arranged | Names the egg count, identifies 2-3 vegetable types, mentions the colander and countertop | Names all visible items (2 brown eggs on clear plastic carton, stainless steel colander with broccoli and peppers, SWELL FAMILY FARMS OMEGA 3 packaging, wooden cutting board edge), describes the overhead angle |
| Completeness | Mentions only eggs or only vegetables; misses the packaging, the cutting board, or the countertop | Covers eggs, vegetables, colander, and countertop; may miss the packaging brand/text or the cutting board corner | Accounts for eggs (count + color + carton), all vegetable types, colander (material + holes + handle), packaging (brand + OMEGA 3 + nutrition panel + tagline), cutting board, countertop, camera angle |
| Usefulness | "A food photo" -- not searchable for any specific ingredient, brand, or context | Mentions eggs, vegetables, omelet ingredients, and that it's from the Gemini report; searchable for "omelet ingredients" | Includes all ingredient names, the SWELL FAMILY FARMS brand, OMEGA 3 label, Gemini Table 13 context, and enough detail that the image content is fully understood without viewing it |

<br><br>

## doc05-R07 -- Vegetable omelet cooking in pan

**Figure reference:** Table 13 image 2, page 19
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 3069x3021 pixels

### Visual Inventory [-> Completeness]

- **Primary subject:** A vegetable omelet in the early-to-mid cooking stage,
  viewed from slightly above at roughly 45 degrees
- **Pan:** Dark gray or black non-stick frying pan, roughly 10-12 inches in
  diameter, occupying most of the frame; the pan edge is visible all around
  with a slight gap at the top where the handle extends out of frame
- **Egg mixture:** Yellow beaten egg mixture covering the pan bottom, still
  visibly liquid in places (especially the center and edges), not yet fully
  set; the surface is uneven with some areas more opaque (partially cooked)
  and others glossy (still liquid)
- **Vegetables mixed into the egg:**
  - Broccoli florets: 4-5 small green florets scattered across the pan,
    clearly identifiable by their tree-like shape
  - Bell pepper pieces: diced chunks of orange, yellow, and red bell pepper,
    roughly 1-2 cm pieces, distributed throughout
  - Dark leafy greens: torn or chopped pieces of dark green/purple leaves
    (likely kale or mixed greens) scattered on top and partially submerged
    in the egg; some leaves show purple-red stems
- **Stovetop:** Visible around the pan edges -- dark metal gas burner grate
  with cast iron supports; a small silver/chrome knob or burner cap is
  partially visible at the lower left
- **Background:** Dark/black stovetop surface visible in corners around the
  pan; no other objects or context visible
- **Lighting:** Overhead or slightly angled kitchen lighting, creating a mild
  sheen on the liquid egg surface and slight shadow on the far side of the pan
- **No text visible in the image**

### Verifiable Facts [-> Accuracy]

- FACT: The pan is a dark non-stick frying pan on a gas stovetop
- FACT: The egg mixture is partially liquid and not fully set
- FACT: At least 3 types of vegetables are visible: broccoli, bell peppers,
  and dark leafy greens
- FACT: Bell pepper pieces include orange, yellow, and red colors
- FACT: The broccoli florets are green and small (bite-sized)
- FACT: Dark leafy greens have purple-red stems visible on some pieces
- FACT: The pan is viewed from a roughly 45-degree overhead angle
- FACT: Gas burner grate is partially visible around the pan edges
- FACT: No utensils, hands, or text are visible in the frame
- FACT: The egg mixture is yellow (standard beaten egg color)

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as a "finished omelet" or "fully cooked"
  REALITY: The egg is still partially liquid and clearly not done cooking
- RISK: A model might identify specific herbs like "basil" or "spinach"
  REALITY: The dark leafy greens are not clearly identifiable as a specific
  variety; they could be kale, mixed greens, or another leafy green
- RISK: A model might claim onions or mushrooms are visible
  REALITY: Only broccoli, bell peppers, and dark leafy greens are clearly
  identifiable
- RISK: A model might describe this as a "frittata" or "scrambled eggs"
  REALITY: The flat shape in a pan is consistent with an omelet; the
  vegetables are distributed across the surface rather than scrambled in
- RISK: A model might state the exact pan size (e.g., "12-inch pan")
  REALITY: The pan size cannot be precisely determined from the photo
- RISK: A model might claim cheese is visible
  REALITY: No cheese is visible; the yellow color is from the egg mixture

### Detail Inventory [-> Specificity]

- Pan material and color: dark gray/black non-stick
- Pan shape: round, roughly 10-12 inches, with handle extending out of frame
- Egg state: partially liquid, yellow, uneven cooking (some areas more opaque)
- Broccoli: 4-5 small green florets
- Bell peppers: diced, orange/yellow/red, roughly 1-2 cm pieces
- Leafy greens: dark green/purple torn pieces, some with purple-red stems
- Stovetop type: gas (cast iron grate visible)
- Camera angle: approximately 45 degrees above
- Lighting: overhead kitchen light, mild sheen on liquid egg
- No text, no utensils, no human hands visible

### Domain Context [-> Usefulness]

- **Domain:** Food photography, cooking process documentation
- **Surrounding document context:** This image appears in Table 13 of the
  Gemini 1.0 technical report (arxiv 2312.11805v5), page 19. Table 13
  demonstrates Gemini's interleaved image-text understanding capabilities.
  The table shows a multi-turn conversation where a user uploads three
  sequential cooking photos and the model identifies the dish, provides a
  recipe, and customizes it. This is the second of three photos (R06 shows
  ingredients, R07 shows cooking in progress, R08 shows the result).
- **Technical terminology:**
  - Interleaved image-text: input format where images and text alternate
    within a conversation, testing the model's ability to reason across
    multiple images in context
  - Multi-turn: conversation with multiple exchanges between user and model
- **Why this image matters:** It is part of a three-image sequence
  demonstrating multi-image reasoning. The cooking progression (ingredients
  -> cooking -> result) tests whether the model can track state changes
  across sequential images.

### Search Keywords [-> Usefulness]

- omelet, vegetable omelet, cooking, frying pan, stovetop
- broccoli, bell pepper, leafy greens, kale, eggs
- food photography, cooking process, recipe
- Gemini, Table 13, interleaved image-text, multi-image reasoning
- non-stick pan, gas stovetop, partially cooked
- multi-turn conversation, sequential images

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Describes this as a "finished omelet on a plate" or claims cheese or meat is visible; wrong cooking state | Correctly identifies partially cooked vegetable omelet in a pan; names most vegetable types; may add one ingredient not visible (e.g., onions) | All items correct: partially liquid egg, broccoli florets, multi-color bell peppers, dark leafy greens with purple stems; correctly notes no cheese, no utensils, gas stovetop |
| Specificity | "A pan of food cooking on a stove" with no ingredient detail | Names 2-3 vegetable types, mentions the egg is not fully cooked, identifies the pan as non-stick | Names all 3 vegetable types with colors (orange/yellow/red peppers, green broccoli, dark purple-green leafy greens), describes egg state (partially liquid, yellow), pan details (dark non-stick, gas burner grate visible) |
| Completeness | Mentions the omelet but omits the stovetop context, specific vegetables, or cooking state | Covers the pan, egg mixture, 2-3 vegetable types, and that it's on a stovetop; may miss the leafy green stems or the camera angle | Accounts for all vegetables (broccoli, peppers, greens), egg state, pan details, stovetop type (gas with grate), camera angle, lighting, and absence of text/utensils |
| Usefulness | "A cooking photo" -- not searchable for any specific food or context | Mentions vegetable omelet, pan, cooking, and that it's from the Gemini report; searchable for "omelet cooking" | Includes all ingredient names, cooking stage (partially cooked), Gemini Table 13 context as part of 3-image sequence, enough detail to understand progression from ingredients to cooking to result |

<br><br>

## doc05-R08 -- Finished vegetable omelet in pan

**Figure reference:** Table 13 image 3, page 19
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 4080x3072 pixels

**Note:** The image catalog describes this as "Finished omelet on plate" but
the actual crop shows the omelet still in the pan on the stovetop. No plate
is visible.

### Visual Inventory [-> Completeness]

- **Primary subject:** A fully cooked vegetable omelet in a dark non-stick
  frying pan, viewed from above at roughly 45 degrees
- **Pan:** Same dark gray/black non-stick pan as R07, roughly 10-12 inches;
  the handle extends toward the lower left and is partially visible (dark
  handle with a metal or riveted attachment point); the pan interior shows
  some browning residue around the edges
- **Omelet:** Fully set egg with browned top surface; the omelet fills most
  of the pan but is slightly irregular in shape (not a perfect circle);
  visible browning on portions of the surface (caramelized egg); some areas
  are golden-brown while others are lighter yellow where the egg is cooked
  but not browned
- **Vegetables visible in/on the omelet:**
  - Red bell pepper pieces: small diced pieces visible at several points on
    the surface
  - Orange/yellow bell pepper pieces: visible near the center and scattered
    across the surface
  - Dark leafy greens: pieces of dark green leaves visible throughout,
    some partially wilted/cooked into the egg, some on top
  - Broccoli: less prominently visible than in R07 but small green pieces
    can be seen embedded in the cooked egg
- **Omelet edges:** Slightly overcooked/browned and crispy at the edges;
  some small fragments of cooked egg have separated from the main body
  near the pan rim
- **Stovetop:** Same gas stovetop as R07 -- dark metal burner grate visible
  around the pan; the stainless steel/white stovetop surface is visible in
  the background, particularly at top left and bottom
- **Pan handle area:** A small rectangular marking or logo is faintly
  visible on the handle or near the handle attachment
- **No text visible in the image**
- **No utensils, hands, or plates visible**

### Verifiable Facts [-> Accuracy]

- FACT: The omelet is in a dark non-stick frying pan, not on a plate
- FACT: The egg is fully cooked and set (no visible liquid egg)
- FACT: The omelet surface has browned/caramelized areas
- FACT: At least 3 types of vegetables are visible: bell peppers (red and
  orange/yellow), dark leafy greens, and broccoli
- FACT: The pan is on a gas stovetop (burner grate visible)
- FACT: The omelet edges are browned and slightly crispy with small fragments
- FACT: The same pan from R07 is used (same size, color, handle style)
- FACT: The camera angle is roughly 45 degrees from above
- FACT: No plate, utensils, or hands are visible
- FACT: The pan handle extends toward the lower left of the frame

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as "on a plate" matching the catalog
  description
  REALITY: The omelet is clearly in the same frying pan, on the stovetop;
  no plate is visible anywhere in the frame
- RISK: A model might claim cheese is melted on top
  REALITY: The yellow/golden color is from the cooked egg; no cheese is
  visible
- RISK: A model might describe this as "perfectly round" or "neatly folded"
  REALITY: The omelet is irregular in shape with ragged browned edges
- RISK: A model might claim garnish or herbs are sprinkled on top
  REALITY: The visible green fragments are the same leafy greens mixed into
  the egg from R07, not a garnish added after cooking
- RISK: A model might describe the egg as "fluffy" or "light"
  REALITY: The egg appears relatively flat and firm, with browned areas
  suggesting it was cooked at medium-to-high heat

### Detail Inventory [-> Specificity]

- Pan: dark gray/black non-stick, ~10-12 inches, handle toward lower left
- Pan condition: browning residue at edges from cooking
- Omelet shape: irregular, not perfectly circular, fills most of pan
- Egg state: fully set, golden-yellow base with browned/caramelized patches
- Egg texture: flat and firm, not fluffy
- Edge condition: overcooked, crispy, small fragments separating near rim
- Red bell pepper: small diced pieces visible at surface
- Orange/yellow bell pepper: visible near center
- Dark leafy greens: throughout, some wilted into egg, some on surface
- Broccoli: small pieces embedded in cooked egg
- Stovetop: gas, dark metal grate, stainless steel/white surface visible
- Handle: partially visible, has a small marking/logo near attachment
- Camera angle: ~45 degrees above
- No text, utensils, hands, plates, or garnish

### Domain Context [-> Usefulness]

- **Domain:** Food photography, cooking process documentation
- **Surrounding document context:** This image appears in Table 13 of the
  Gemini 1.0 technical report (arxiv 2312.11805v5), page 19. Table 13
  demonstrates interleaved image-text understanding in a multi-turn
  conversation. This is the third and final photo in the cooking sequence:
  R06 shows ingredients on a counter, R07 shows the omelet partially
  cooked, R08 shows the finished result. In the conversation, the user
  presents these images and asks Gemini to identify the dish and provide a
  recipe.
- **Technical terminology:**
  - Interleaved image-text: input format mixing images and text in a single
    conversation, testing multi-image reasoning
  - Multi-turn: multiple exchanges between user and model
- **Why this image matters:** It completes the three-image cooking
  progression. The model must recognize that this is the same dish from R07
  in a later state (cooked vs. cooking), demonstrating temporal/state
  reasoning across sequential images.

### Search Keywords [-> Usefulness]

- omelet, vegetable omelet, finished, cooked, frying pan
- broccoli, bell pepper, leafy greens, eggs, browned
- food photography, cooking result, recipe
- Gemini, Table 13, interleaved image-text, multi-image reasoning
- non-stick pan, gas stovetop, fully cooked
- multi-turn conversation, sequential images, cooking progression

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | States "omelet on a plate" or claims it's still cooking (liquid egg visible); identifies wrong ingredients | Correctly identifies finished omelet in a pan on stovetop; names most vegetable types; may claim cheese is visible | All items correct: fully set egg with browned surface, no plate, identifies all vegetable types, notes irregular shape and crispy edges, correct stovetop type |
| Specificity | "A cooked omelet" with no detail about appearance, vegetables, or setting | Names 2-3 vegetable types, describes egg as cooked/browned, mentions the non-stick pan | Describes egg state (fully set, browned/caramelized patches, flat/firm), all vegetable types with colors, edge condition (crispy, fragments), pan details (non-stick, handle direction), stovetop type |
| Completeness | Mentions only the omelet; misses the pan, stovetop, edge condition, or specific vegetables | Covers omelet, pan, stovetop, and 2-3 vegetable types; may miss edge browning, pan handle, or residue at rim | Accounts for omelet (shape, color, texture), all vegetables, edge condition, pan details (handle, residue), stovetop type, camera angle, and what is absent (no plate, no utensils) |
| Usefulness | "A food photo" -- not searchable or contextually useful | Mentions finished vegetable omelet in a pan, connects to the Gemini report; searchable for "cooked omelet" | Includes all ingredient names, cooking state (fully done, browned), notes this is the third of three sequential images (R06 ingredients, R07 cooking, R08 finished), Gemini Table 13 context |

<br><br>

## doc05-R11 -- Persian shield plant

**Figure reference:** Figure 11, page 78
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 1170x1560 pixels

**Note:** The agent-written ground truth described the entire Figure 11 region
(photo + prompt text + model response) rather than the extracted raster crop.
Rewritten based on verified crop, which contains only the photograph.

### Visual Inventory [-> Completeness]

- **Primary subject:** A Persian shield plant (*Strobilanthes dyerianus*)
  occupying the center and lower two-thirds of the frame, displaying its
  characteristic iridescent purple leaves
- **Persian shield leaves:** 15-20 large lance-shaped (lanceolate) leaves
  radiating from central stems; each leaf shows a vivid iridescent
  purple/magenta surface with darker green-to-purple veins running parallel
  from midrib to leaf edge; leaves are 10-15 cm long and 3-5 cm wide
  (estimated); the iridescence gives a metallic shimmer that varies from
  pink to purple depending on angle; leaf undersides (visible on a few
  curling leaves) appear more muted green-purple
- **Stems:** Dark reddish-purple stems visible where leaves part, consistent
  with *Strobilanthes dyerianus*
- **Surrounding plants (background and edges):**
  - Upper left: pale pink/white flowers on a small shrub (possibly
    hydrangea or begonia), with small rounded green leaves
  - Lower left: bright red/magenta flowers (possibly impatiens), 2-3
    blooms visible
  - Lower left corner: a plant with dark green leaves edged in
    lighter cream/silver stripes (possibly a *Tradescantia* or similar
    variegated foliage plant)
  - Upper right: large solid green leaves (possibly a hosta or similar
    broad-leaved plant), partially out of frame
  - Lower right corner: small speckled/spotted leaves (possibly a polka
    dot plant, *Hypoestes phyllostachya*)
  - General: dense green foliage fills all edges and gaps between plants
- **Setting:** Outdoor garden bed or border planting; plants are densely
  packed in a mixed ornamental arrangement; no soil is directly visible
  due to foliage density
- **Lighting:** Natural daylight, slightly overcast or diffused; no harsh
  shadows; the iridescent leaves catch the light producing the
  characteristic shimmer
- **Camera angle:** Slightly above, looking down at approximately 30-40
  degrees
- **No text, labels, signs, or human-made objects visible in the photo**

### Verifiable Facts [-> Accuracy]

- FACT: The central plant has iridescent purple/magenta lance-shaped leaves
  with darker parallel veins
- FACT: The leaf color shows metallic iridescence (pink-to-purple shimmer)
- FACT: The plant stems are dark reddish-purple
- FACT: At least 15 leaves are visible on the main plant
- FACT: Bright red/magenta flowers (2-3 blooms) are visible at lower left
- FACT: Pale pink/white flowers are visible at upper left
- FACT: A variegated plant with cream/silver-striped dark leaves is visible
  at lower left corner
- FACT: Large solid green leaves are visible at upper right
- FACT: Small speckled/spotted leaves are visible at lower right corner
- FACT: No text, labels, or human-made objects appear in the photo
- FACT: The photo is taken outdoors in natural daylight
- FACT: No soil is visible due to dense planting

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe the purple leaves as flowers
  REALITY: The purple/magenta features are leaves, not flowers; the Persian
  shield's leaves are its ornamental feature
- RISK: A model might misidentify the plant as coleus, wandering Jew
  (*Tradescantia*), or another purple-leaved species
  REALITY: The iridescent metallic sheen and parallel vein pattern are
  distinctive to *Strobilanthes dyerianus*; coleus has different leaf shapes
  and vein patterns
- RISK: A model might describe text from the prompt/response panels that
  surround this image on the PDF page
  REALITY: The extracted crop contains only the photograph; no text is
  visible
- RISK: A model might claim the photo shows a single plant in a pot
  REALITY: The plant is in a garden bed surrounded by multiple other species
- RISK: A model might state exact leaf dimensions
  REALITY: No scale reference is visible; leaf sizes can only be estimated
- RISK: A model might identify all surrounding plants with certainty
  REALITY: The surrounding plants are partially obscured and at the frame
  edges; identifications are approximate (the red flowers could be
  impatiens or begonias; the variegated plant could be several species)

### Detail Inventory [-> Specificity]

- Central plant: Persian shield (*Strobilanthes dyerianus*), 15-20 leaves
- Leaf characteristics: lance-shaped, iridescent purple/magenta, metallic
  shimmer, darker parallel veins from midrib to edge
- Stem color: dark reddish-purple
- Surrounding plants: at least 5 distinct species visible at frame edges
- Red/magenta flowers at lower left: 2-3 blooms (possibly impatiens)
- Pink/white flowers at upper left: small shrub with rounded green leaves
- Variegated foliage at lower left corner: dark leaves with cream/silver
  stripes
- Large green leaves at upper right: broad, solid green (partially out of
  frame)
- Speckled leaves at lower right corner: small, spotted pattern
- Setting: dense outdoor garden bed, no soil visible
- Lighting: natural daylight, diffused, no harsh shadows
- Camera angle: ~30-40 degrees above
- No text, labels, or human-made objects visible

### Domain Context [-> Usefulness]

- **Domain:** Botany, horticulture, plant identification
- **Surrounding document context:** This photo appears in Figure 11 of the
  Gemini 1.0 technical report (arxiv 2312.11805v5), page 78. Figure 11
  demonstrates Gemini's visual plant identification capability. On the PDF
  page, the photo is embedded in a prompt box with the question "Do you know
  what it this plant? How do I best take care of it?" (note typo: "it this"
  instead of "is this"), followed by a model response identifying the plant
  as Persian shield and providing care instructions. However, none of this
  text appears in the extracted crop -- only the photograph.
- **Technical terminology:**
  - *Strobilanthes dyerianus*: scientific name for Persian shield, a tropical
    perennial native to Myanmar (Burma)
  - Iridescent: displaying shifting rainbow-like colors depending on viewing
    angle, caused by structural coloration in the leaf cells
  - Lanceolate: lance-shaped, narrow and tapered at both ends
- **Why this image matters:** Tests whether an annotation model can identify
  a specific ornamental plant species from a photograph showing it among
  other garden plants, and can describe the distinctive visual features
  (iridescent leaves) that distinguish it.

### Search Keywords [-> Usefulness]

- Persian shield, Strobilanthes dyerianus, purple leaves, iridescent
- garden plant, ornamental, tropical plant, foliage
- plant identification, horticulture, garden bed
- iridescent leaves, metallic shimmer, lance-shaped
- Gemini, Figure 11, visual identification, multimodal
- impatiens, variegated foliage, mixed planting

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies the plant (calls it coleus or describes leaves as flowers); describes prompt/response text not visible in the crop | Correctly identifies iridescent purple-leaved plant in a garden; may not provide the species name; correctly notes no text in image | Identifies as Persian shield (*Strobilanthes dyerianus*), correctly describes iridescent purple leaves with parallel veins, notes surrounding plants without over-identifying them, no text fabrication |
| Specificity | "A photo of a purple plant in a garden" with no species or detail | Describes purple/pink iridescent leaves, mentions the lance shape, notes surrounding flowers and green plants | Names the species (common + scientific), describes leaf iridescence and vein pattern, counts approximate leaf number, identifies 3+ surrounding plant types by appearance, notes stem color |
| Completeness | Mentions only the purple plant; omits surrounding plants, garden setting, or camera angle | Covers the central plant, 2-3 surrounding plant types, and the garden setting; may miss the variegated plant or spotted leaves at corners | Accounts for the central plant (leaves, stems, count), all visible surrounding species (5 types), garden setting, lighting, camera angle, and absence of text/labels |
| Usefulness | "A plant photo" -- not searchable for species or garden context | Mentions purple plant, garden, possibly Persian shield; searchable for "purple garden plant" | Includes species names (common + scientific), leaf characteristics (iridescent, lanceolate), garden context, and enough visual detail to distinguish this from other purple-leaved species |

<br><br>

## doc05-R12 -- Goldendoodle on city street with taxi

**Figure reference:** Figure 12 image 1, page 79
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 256x256 pixels

**Note:** The image catalog describes this as "Goldendoodle at beach" but the
actual crop shows the dog on a city street with a yellow taxi behind it. No
beach is visible.

### Visual Inventory [-> Completeness]

- **Primary subject:** A Goldendoodle (or similar doodle-breed dog) sitting
  on a wet city street, facing the camera with mouth open (panting,
  tongue out)
- **Dog details:** Golden/tan curly-to-wavy fur, medium-to-large size,
  wearing a dark collar (possibly red/maroon); fur is slightly damp or
  ruffled; the dog's expression appears happy/relaxed
- **Background:** Urban city street; a yellow taxi cab is visible in the
  mid-ground slightly to the right; tall buildings line both sides of the
  street creating an urban canyon effect; the street surface appears wet
  (reflective)
- **Lighting:** Overcast or diffused light; the overall color palette is
  cool/blue-toned with the warm golden dog and yellow taxi as contrasts
- **Depth of field:** Shallow -- the dog is in sharp focus while the
  background (taxi, buildings) is noticeably blurred (bokeh effect)
- **Camera angle:** Approximately eye level with the dog (low angle)
- **Image quality:** 256x256 is a small thumbnail; some fine details are
  lost to compression/resolution
- **No text visible in the image**

### Verifiable Facts [-> Accuracy]

- FACT: The dog has golden/tan curly-to-wavy fur consistent with a
  Goldendoodle
- FACT: The dog is wearing a dark collar
- FACT: A yellow taxi is visible in the background
- FACT: The setting is an urban street with tall buildings
- FACT: The street surface appears wet/reflective
- FACT: The dog is facing the camera with mouth open
- FACT: The background is blurred (shallow depth of field)
- FACT: The image is 256x256 pixels (small thumbnail)
- FACT: No beach, sand, or water is visible

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as "at a beach" matching the catalog
  REALITY: The setting is clearly a city street with a taxi and buildings;
  no beach elements are visible
- RISK: A model might identify the specific breed with certainty
  REALITY: "Goldendoodle" is likely but the small image size makes definitive
  breed identification uncertain; it could be a Labradoodle or similar
- RISK: A model might read text on the taxi or buildings
  REALITY: At 256x256 with background blur, no text is legible
- RISK: A model might identify the specific city
  REALITY: The yellow taxi suggests New York City but this cannot be
  confirmed from the image alone

### Detail Inventory [-> Specificity]

- Dog: golden/tan, curly-wavy fur, dark collar, mouth open, panting
- Setting: wet city street, urban canyon with tall buildings
- Background: yellow taxi, blurred buildings
- Lighting: cool/blue overcast tones, warm dog and taxi contrast
- Depth of field: shallow, dog sharp, background blurred
- Camera angle: low, approximately dog eye level
- Image size: 256x256 thumbnail
- No text visible

### Domain Context [-> Usefulness]

- **Domain:** Pet photography, dog breed identification
- **Surrounding document context:** This is the first of three Goldendoodle
  photos in Figure 12 of the Gemini 1.0 technical report (arxiv
  2312.11805v5), page 79. Figure 12 demonstrates multi-image entity
  recognition -- the model is asked to identify the breed across three
  photos showing the same type of dog in different settings (city street,
  autumn park, waterfront). R12 shows the city setting, R13 shows an
  autumn park, R14 shows a waterfront with skyline.
- **Technical terminology:**
  - Multi-image reasoning: the model must recognize the same breed across
    different photos with varying backgrounds
  - Goldendoodle: Golden Retriever / Poodle crossbreed
- **Why this image matters:** Part of a three-image set testing whether the
  model can identify the same dog breed across varied contexts. The urban
  setting tests recognition against a complex, distracting background.

### Search Keywords [-> Usefulness]

- Goldendoodle, dog, pet, curly fur, golden
- city street, yellow taxi, urban, wet street
- breed identification, multi-image, entity recognition
- Gemini, Figure 12, multimodal, dog breed
- shallow depth of field, bokeh, pet photography

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Calls it "a dog at a beach" or identifies the wrong breed entirely; claims legible text | Correctly identifies a curly-haired dog on a city street with a taxi; may state "Goldendoodle" without hedging certainty | Identifies as likely Goldendoodle, notes the city street setting, yellow taxi, wet surface, dark collar, and correctly notes no beach elements; hedges breed certainty due to small image |
| Specificity | "A photo of a dog" with no setting or breed detail | Describes golden curly fur, mentions the city street and taxi, notes the blurred background | Describes fur texture (curly-to-wavy), collar color, street condition (wet/reflective), lighting tone (cool/blue), shallow depth of field, camera angle (low/eye-level) |
| Completeness | Mentions the dog but omits the setting entirely | Covers dog appearance, city street, taxi, and background blur; may miss the wet street or collar | Accounts for dog (fur, collar, expression), setting (wet street, taxi, buildings), photographic qualities (depth of field, lighting, angle), and image limitations (256x256 thumbnail) |
| Usefulness | "A dog photo" -- not searchable | Mentions Goldendoodle, city, taxi; searchable for "dog city street" | Includes breed, setting details, Gemini Figure 12 context as part of 3-image breed identification set, photographic characteristics |

<br><br>

## doc05-R13 -- Goldendoodle in autumn park

**Figure reference:** Figure 12 image 2, page 79
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 256x256 pixels

**Note:** The image catalog describes this as "Goldendoodle in city" but the
actual crop shows the dog sitting on a path in an autumn park with fallen
leaves and trees, not in a city setting.

### Visual Inventory [-> Completeness]

- **Primary subject:** A Goldendoodle (or similar doodle-breed dog) sitting
  on a paved path, facing the camera; the dog appears smaller/younger than
  in R12, with a rounder face and shorter fur
- **Dog details:** Golden/tan curly fur, compact posture (sitting upright),
  dark eyes and nose visible; no collar clearly visible at this resolution
- **Background:** An autumn park scene; trees with yellow/golden fall foliage
  line both sides of a paved walkway; fallen leaves cover parts of the
  ground; a few people are visible as small blurred figures in the far
  distance walking along the path
- **Ground:** Gray paved path (cobblestone or similar) with scattered fallen
  leaves
- **Lighting:** Soft autumn light; warm golden tones throughout from the
  foliage; slightly hazy/atmospheric
- **Depth of field:** Moderate -- dog is sharp, background is somewhat
  blurred but trees and path remain recognizable
- **Camera angle:** Low, approximately eye level with the sitting dog
- **Color palette:** Warm golds and oranges dominate (fall foliage matches
  the dog's fur color)
- **Image quality:** 256x256 thumbnail; some fine detail lost
- **No text visible in the image**

### Verifiable Facts [-> Accuracy]

- FACT: The dog has golden/tan curly fur
- FACT: The dog is sitting on a paved path
- FACT: Trees with yellow/gold autumn foliage are visible on both sides
- FACT: Fallen leaves are on the ground
- FACT: Small blurred figures (people) are visible in the far background
- FACT: The overall color palette is warm golden tones
- FACT: The setting is a park with a walkway, not a city street
- FACT: The image is 256x256 pixels

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as "in city" matching the catalog
  REALITY: The setting is an autumn park with trees and a walking path;
  no buildings, streets, or vehicles are visible
- RISK: A model might claim the dog is the same individual as in R12
  REALITY: The dogs may be different individuals of the same breed; this
  cannot be confirmed from the photos
- RISK: A model might identify specific tree species
  REALITY: At 256x256 with background blur, tree species cannot be
  determined
- RISK: A model might describe a leash or collar
  REALITY: No collar or leash is clearly visible at this resolution

### Detail Inventory [-> Specificity]

- Dog: golden/tan curly fur, sitting upright, compact posture
- Setting: autumn park, paved walkway, fall foliage
- Trees: yellow/gold leaves, lining both sides of path
- Ground: gray paved path with scattered fallen leaves
- People: small blurred figures in far distance
- Lighting: soft autumn light, warm golden tones
- Depth of field: moderate, dog sharp, background somewhat blurred
- Camera angle: low, dog eye level
- Color harmony: dog fur matches fall foliage color
- Image size: 256x256 thumbnail

### Domain Context [-> Usefulness]

- **Domain:** Pet photography, dog breed identification
- **Surrounding document context:** Second of three Goldendoodle photos in
  Figure 12, page 79 of the Gemini 1.0 technical report. The three photos
  show the same breed in different settings to test multi-image entity
  recognition. R12 = city street, R13 = autumn park, R14 = waterfront.
- **Why this image matters:** The autumn park setting with matching warm
  tones tests whether the model can distinguish the dog from the similarly
  colored background and still identify the breed.

### Search Keywords [-> Usefulness]

- Goldendoodle, dog, pet, curly fur, golden
- autumn, fall, park, fallen leaves, golden foliage
- breed identification, multi-image, entity recognition
- Gemini, Figure 12, multimodal
- walkway, paved path, pet photography

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Calls it "a dog in a city" or misidentifies the season; wrong breed | Correctly identifies a curly-haired dog in an autumn park with fall foliage | Identifies as likely Goldendoodle in an autumn park, notes fallen leaves, paved path, distant people, warm golden tones, and correctly distinguishes from city setting |
| Specificity | "A photo of a dog outside" | Describes golden fur, autumn trees, fall leaves, path | Describes fur texture, sitting posture, paved path type, foliage colors, distant figures, color harmony between dog and foliage, camera angle |
| Completeness | Mentions dog only; misses the park setting | Covers dog, park, autumn foliage, path; may miss the distant people or leaf-covered ground | Accounts for dog (fur, posture), setting (park, path, trees, leaves), background elements (distant people), photographic qualities (lighting, depth of field, angle), and image limitations |
| Usefulness | "A dog photo" | Mentions Goldendoodle, autumn park; searchable for "dog autumn park" | Includes breed, season, setting details, Gemini Figure 12 context as multi-image set, color harmony observation |

<br><br>

## doc05-R14 -- Goldendoodle at waterfront with skyline

**Figure reference:** Figure 12 image 3, page 79
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 256x256 pixels

**Note:** The image catalog describes this as "Goldendoodle portrait" but the
actual crop shows the dog from behind, sitting at a waterfront facing a city
skyline. It is not a portrait in the conventional sense.

### Visual Inventory [-> Completeness]

- **Primary subject:** A Goldendoodle (or similar doodle-breed dog) sitting
  on a concrete ledge or wall, viewed FROM BEHIND; the dog faces away from
  the camera, looking toward a city skyline across water
- **Dog details:** Golden/tan curly-to-wavy fur, seen from behind; the head
  is slightly turned showing a partial profile; fur appears thick and
  slightly windblown
- **Background:** A city skyline across a body of water; the most prominent
  building appears to be One World Trade Center (tall, tapered spire) in
  lower Manhattan, with several other skyscrapers; the skyline is in sharp
  enough focus to identify building shapes despite the small image size
- **Water:** A body of water (likely the Hudson River or East River)
  separates the foreground ledge from the skyline
- **Foreground:** Light gray concrete ledge or waterfront railing where the
  dog sits
- **Sky:** Clear blue sky with no visible clouds
- **Lighting:** Bright daylight, warm tones on the dog's fur, cooler tones
  on the distant skyline
- **Camera angle:** Behind and slightly above the dog
- **Image quality:** 256x256 thumbnail; skyline buildings are small but
  identifiable by silhouette
- **No text visible in the image**

### Verifiable Facts [-> Accuracy]

- FACT: The dog is viewed from behind, facing away from the camera
- FACT: The dog sits on a light gray concrete surface
- FACT: A city skyline is visible across water
- FACT: A tall building with a tapered spire (consistent with One World
  Trade Center) is the most prominent structure
- FACT: The sky is clear blue
- FACT: The dog has golden/tan curly fur
- FACT: Water separates the foreground from the skyline
- FACT: The image is 256x256 pixels

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as a "portrait" matching the catalog
  REALITY: The dog is viewed from behind; this is not a portrait
- RISK: A model might definitively identify the skyline as Manhattan
  REALITY: The tall spired building is consistent with One World Trade
  Center but at 256x256, this is not certain
- RISK: A model might describe the dog's facial expression
  REALITY: The dog faces away; only a slight partial profile is visible
- RISK: A model might call the location "a beach"
  REALITY: The dog sits on a concrete ledge at a waterfront, not a beach

### Detail Inventory [-> Specificity]

- Dog: golden/tan curly fur, seen from behind, sitting on concrete ledge
- Dog posture: upright, head slightly turned, looking toward skyline
- Skyline: city buildings across water, tallest has tapered spire
- Water: body of water between foreground and skyline
- Foreground: light gray concrete surface
- Sky: clear blue, no clouds
- Lighting: bright daylight, warm on dog, cooler on skyline
- Camera angle: behind and slightly above
- Image size: 256x256 thumbnail

### Domain Context [-> Usefulness]

- **Domain:** Pet photography, scenic/landscape photography
- **Surrounding document context:** Third and final Goldendoodle photo in
  Figure 12, page 79 of the Gemini 1.0 technical report. Completes the
  three-image set (city street, autumn park, waterfront) for multi-image
  breed identification. The dog faces away in this image, adding difficulty
  to the identification task since breed features (face shape, eye color)
  are less visible.
- **Why this image matters:** The rear-view angle makes breed identification
  harder, testing whether the model can use fur texture and body shape
  alone. Also tests scene understanding (waterfront, skyline, water).

### Search Keywords [-> Usefulness]

- Goldendoodle, dog, pet, curly fur, golden
- waterfront, skyline, city, One World Trade Center, Manhattan
- breed identification, multi-image, entity recognition
- Gemini, Figure 12, multimodal
- rear view, back turned, scenic, water

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Calls it a "portrait" or describes the dog's facial expression; claims it's at a beach | Correctly notes the dog is viewed from behind facing a skyline across water; identifies curly fur | All items correct: rear view, concrete ledge, city skyline with tall spired building, water separation, clear sky; hedges on specific city identification |
| Specificity | "A photo of a dog looking at a city" | Describes golden fur, waterfront setting, skyline with buildings | Describes fur seen from behind, concrete surface, tapered spire building, water body, sky condition, lighting contrast (warm dog vs cool skyline), camera angle |
| Completeness | Mentions dog and skyline but misses the water, concrete surface, or viewing angle | Covers dog (from behind), skyline, water, and concrete surface; may miss the sky or lighting | Accounts for dog (fur, posture, viewing angle), setting (concrete, water, skyline, sky), photographic qualities (lighting, camera angle), and image limitations (256x256) |
| Usefulness | "A dog photo" | Mentions Goldendoodle, waterfront, skyline; searchable for "dog waterfront" | Includes breed, waterfront setting, possible Manhattan skyline, Gemini Figure 12 context as multi-image set, rear-view difficulty factor |

<br><br>

## doc05-R15 -- Handwritten shapes sequence puzzle

**Figure reference:** Figure 13, page 80
**Content type:** photo
**Annotation difficulty:** Medium
**Dimensions:** 4080x3072 pixels

**Note:** Agent-written ground truth referenced prompt text and model response
from the PDF page. Revised to describe only the extracted crop (the
photograph of shapes on paper).

### Visual Inventory [-> Completeness]

- **Primary subject:** Three hand-drawn geometric shapes and a question mark,
  arranged in a horizontal row from left to right on a sheet of paper
- **Shapes (left to right):**
  1. **Triangle** (3 sides): small, roughly equilateral, drawn with slightly
     uneven hand-drawn lines; positioned at the left of the row
  2. **Square** (4 sides): slightly larger than the triangle, drawn with
     thicker/bolder strokes; lines are roughly straight but clearly
     hand-drawn (not ruler-assisted)
  3. **Pentagon** (5 sides): roughly the same size as the square, regular
     pentagon shape with 5 approximately equal sides; drawn with bold
     black lines similar to the square
  4. **Question mark** (?): drawn in the same black ink as the shapes,
     roughly the same height as the shapes; serves as the puzzle prompt
     (what comes next?)
- **Paper/surface:** Light beige or off-white paper; slight texture visible;
  the paper fills the entire frame with no edges visible; a very subtle
  shadow or gradient appears at the top edge of the image (possibly from
  the photography lighting)
- **Ink:** All shapes are drawn in black ink with a marker or thick pen;
  the stroke width is consistent across all shapes (approximately 2-3mm)
- **Spacing:** The four elements are roughly evenly spaced across the
  center of the frame, positioned slightly below the vertical midpoint
- **Camera angle:** Directly overhead (top-down) or very close to it
- **No other text, numbers, labels, or objects visible in the image**

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 3 drawn geometric shapes plus a question mark
- FACT: The first shape is a triangle (3 sides)
- FACT: The second shape is a square (4 sides)
- FACT: The third shape is a pentagon (5 sides)
- FACT: The fourth position shows a question mark (?)
- FACT: All shapes and the question mark are drawn in black ink
- FACT: The shapes are on a light beige/off-white paper surface
- FACT: The shapes are hand-drawn (slightly imperfect lines, not
  ruler-straight)
- FACT: The shapes are arranged left to right in a horizontal row
- FACT: The shapes increase in number of sides: 3, 4, 5
- FACT: No other text, numbers, or objects are visible

### Hallucination Risks [-> Accuracy]

- RISK: A model might state there are 4 shapes (counting the question mark
  as a geometric shape)
  REALITY: There are 3 geometric shapes plus a question mark placeholder
- RISK: A model might describe the shapes as printed or computer-generated
  REALITY: The shapes are clearly hand-drawn with slightly uneven lines
- RISK: A model might misidentify the third shape as a hexagon
  REALITY: The third shape has 5 sides (pentagon); counting the sides in
  the image confirms this
- RISK: A model might claim additional shapes, text, or objects are visible
  REALITY: Only the 3 shapes and question mark are drawn; the rest is
  blank paper
- RISK: A model might describe prompt or response text from the PDF page
  REALITY: The extracted crop contains only the photograph; no
  surrounding text is visible
- RISK: A model might state the shapes are drawn with a pencil
  REALITY: The strokes are bold and dark, consistent with a marker or
  thick pen, not a pencil

### Detail Inventory [-> Specificity]

- Three geometric shapes in a sequence: triangle (3 sides), square (4
  sides), pentagon (5 sides)
- Question mark in the fourth position
- All drawn in black ink with marker/thick pen (bold strokes, ~2-3mm width)
- Paper: light beige/off-white, slight texture, fills entire frame
- Hand-drawn quality: slightly uneven lines, not ruler-straight
- Shapes are roughly similar in size (the triangle is slightly smaller)
- Horizontal row arrangement, evenly spaced
- Positioned slightly below vertical center of frame
- Subtle shadow/gradient at top edge from lighting
- Camera angle: top-down or near-top-down
- Pattern: side count increases by 1 (3, 4, 5, ?)
- No other text, numbers, labels, or objects

### Domain Context [-> Usefulness]

- **Domain:** Visual pattern recognition, geometric reasoning, IQ-test-style
  sequence puzzles
- **Surrounding document context:** This photo appears in Figure 13 of the
  Gemini 1.0 technical report (arxiv 2312.11805v5), page 80. On the PDF
  page, the photo is embedded in a prompt asking "Look at this sequence of
  three shapes. What shape should come as the fourth shape?" The model
  responds identifying a hexagon (6 sides) because the side count increases
  by one (3, 4, 5, 6). However, the extracted crop contains only the
  photograph itself.
- **Technical terminology:**
  - Polygon: closed shape with straight sides
  - Pentagon: 5-sided polygon
  - Hexagon: 6-sided polygon (the expected answer)
  - Sequence pattern: a rule governing the progression of elements
- **Why this image matters:** Tests the model's ability to interpret
  hand-drawn (imperfect) geometric shapes, count their sides correctly,
  identify the increasing pattern, and reason about what comes next. The
  hand-drawn quality adds difficulty compared to clean computer-generated
  shapes.

### Search Keywords [-> Usefulness]

- Gemini, shape sequence, pattern recognition
- triangle, square, pentagon, hexagon
- geometric reasoning, visual puzzle, sequence prediction
- handwritten shapes, hand-drawn, black ink
- side count pattern, polygon sequence
- IQ test, spatial reasoning, Figure 13

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies a shape (e.g., calls the pentagon a hexagon); states wrong side counts; describes text not in the crop | Correctly identifies all 3 shapes and the question mark; gets the side counts right (3, 4, 5); notes hand-drawn quality | All shapes correctly identified with side counts, question mark noted as placeholder not shape, correctly describes ink type and paper surface, no fabricated text |
| Specificity | "Shapes drawn on paper" with no shape names or side counts | Names triangle, square, pentagon; mentions increasing side count; describes black ink on paper | Lists each shape with side count, describes drawing quality (hand-drawn, thick pen/marker strokes, slightly uneven), paper color/texture, spacing and arrangement, camera angle |
| Completeness | Mentions only the shapes; omits the question mark, paper surface, or drawing medium | Covers 3 shapes, question mark, hand-drawn quality, and paper; may miss the relative sizing, spacing, or camera angle | Accounts for all shapes with side counts, question mark, ink type, paper surface, shape sizes, spacing, camera angle, and what is absent (no other text or objects) |
| Usefulness | "A picture of shapes" -- not searchable for pattern type or context | Mentions shape sequence puzzle, polygon names, increasing sides; searchable for "shape pattern" | Includes all polygon names, side count pattern (3, 4, 5), hand-drawn quality, Gemini Figure 13 context, and enough detail to understand the visual puzzle without seeing the image |

<br><br>

## doc05-R16 -- Parallelogram with dimensions

**Figure reference:** Figure 14, page 81
**Content type:** diagram
**Annotation difficulty:** Easy
**Dimensions:** 539x158 pixels

### Visual Inventory [-> Completeness]

- **Shape:** A parallelogram slanting upward to the right, with the bottom-
  left vertex as the leftmost point and the top-right vertex as the
  rightmost
- **Fill:** Light purple/lilac
- **Outline:** Dark purple/plum, relatively thick
- **Dimension labels (2 total):**
  - "x" (italic) -- labels the height, positioned to the left of the
    vertical height line inside the parallelogram
  - "x + 15" (italic) -- labels the top edge of the parallelogram,
    positioned above/along that edge
- **Height indicator:** A vertical line segment drawn inside the
  parallelogram on the left side, from the top-left slanted edge straight
  down to the bottom edge
- **Right-angle marker:** A small red/pink square at the base of the height
  line where it meets the bottom edge, confirming the height is
  perpendicular to the base
- **No other elements:** No formula, no additional measurements, no grid,
  no figure caption in the crop, no background elements

### Verifiable Facts [-> Accuracy]

- FACT: The shape is a parallelogram (two pairs of parallel sides)
- FACT: The height is labeled "x" (italic)
- FACT: The top edge is labeled "x + 15" (italic)
- FACT: There is a right-angle marker (small square) at the base of the
  height line
- FACT: The right-angle marker is red/pink colored
- FACT: The parallelogram fill is light purple/lilac
- FACT: The outline is dark purple/plum
- FACT: The height line is vertical, inside the parallelogram on the left
  side
- FACT: Only two dimension labels appear -- no other measurements are shown
- FACT: The parallelogram slants upward to the right
- FACT: No formula or equation appears in the image

### Hallucination Risks [-> Accuracy]

- RISK: "The base is labeled x + 15" -- REALITY: The TOP edge is labeled
  x + 15, not the base/bottom edge
- RISK: "The side length is x" -- REALITY: x labels the HEIGHT (the
  perpendicular distance between parallel edges), not a slanted side
  length. The right-angle marker confirms this.
- RISK: "The area formula is shown as x(x + 15)" -- REALITY: No formula
  appears in the image; only the two labeled dimensions
- RISK: "All four sides are labeled" -- REALITY: Only the height (x) and
  top edge (x + 15) are labeled
- RISK: Inventing a specific numerical value for x -- REALITY: x is a
  variable, not a specific number
- RISK: "The bottom edge is labeled" -- REALITY: The bottom edge has no
  label (though it would equal x + 15 since opposite sides of a
  parallelogram are equal)

### Detail Inventory [-> Specificity]

- Parallelogram shape with upward-right slant
- Light purple/lilac fill, dark purple/plum outline
- Height label "x" in italic, left of the vertical height line
- Top edge label "x + 15" in italic, along the top edge
- Vertical height line segment inside the parallelogram on the left
- Red/pink right-angle square marker at base of height line
- No other text, labels, measurements, or annotations
- Clean geometric drawing style (not hand-drawn, digitally rendered)
- White background, no grid or axis

### Domain Context [-> Usefulness]

This is a geometry problem figure from the Gemini technical report (Figure
14, page 81). It presents a parallelogram with algebraic dimension labels,
testing the model's ability to reason about geometric properties. The likely
question asks for the area: base times height = (x + 15) times x = x^2 + 15x.
The image specifically tests whether the model can distinguish height from
side length -- the right-angle marker is the visual cue that x is the
perpendicular height, not a slanted side.

### Search Keywords [-> Usefulness]

- parallelogram, geometry, area, dimensions
- algebraic expression, x + 15, variable, height
- right angle, perpendicular, base times height
- math problem, visual reasoning, Gemini Figure 14
- geometric shape, purple parallelogram

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Calls it a rectangle or rhombus; says x labels a side length; claims base is labeled x + 15 | Correctly identifies parallelogram; gives both labels "x" and "x + 15"; notes the right-angle marker | All labels placed correctly (height vs. top edge), right-angle marker noted at base of height line, fill/outline colors accurate, no fabricated measurements |
| Specificity | "A shape with labels" or "a purple quadrilateral" | Names "parallelogram," gives both labels, mentions purple color | Specifies light purple fill with dark purple outline, height line position (left interior), right-angle marker color (red/pink), label positions and italic style, slant direction |
| Completeness | Mentions only the shape or only one label; omits the right-angle marker | Covers shape, both labels, and right-angle marker; may miss color details or height line position | Accounts for shape with slant direction, both labels with positions, height line, right-angle marker with color, fill and outline colors, and absence of other measurements |
| Usefulness | "A purple shape" -- no geometric context | Mentions parallelogram with dimensions, math problem context; searchable for "parallelogram area" | Includes both algebraic labels, identifies this as a geometry/area problem, explains significance of right-angle marker for height vs. side distinction, connects to Gemini Figure 14 visual math reasoning |

<br><br>

## doc05-R17 -- Moon photograph

**Figure reference:** Figure 15 image 1, page 81
**Content type:** photo
**Annotation difficulty:** Medium
**Dimensions:** 514x510 pixels

**Note:** Agent-written ground truth described both R17 (moon) and R18 (golf
ball) as a single composite entry, plus prompt/response text. Rewritten to
describe only the extracted R17 crop (the moon photograph). This is also
another instance of the agent treating a multi-image figure as one unit (see
DF-01).

### Visual Inventory [-> Completeness]

- **Primary subject:** A near-full-disc photograph of the Moon against a
  black background
- **Moon disc:** The Moon fills most of the frame, slightly off-center to
  the right; it appears nearly full (gibbous to full phase), with the
  terminator (day/night boundary) not visible, suggesting full or very
  near-full illumination
- **Surface features visible:**
  - Multiple dark regions (maria/seas): a large dark area in the upper
    left quadrant (likely Mare Imbrium or Oceanus Procellarum), dark
    patches in the center-left (possibly Mare Serenitatis, Mare
    Tranquillitatis), and a prominent dark region at the lower center
  - Numerous impact craters of varying sizes: the most prominent is a
    bright-rayed crater in the lower portion (consistent with Tycho,
    identifiable by its prominent ray system extending across the surface)
  - Bright highlands (terrae): lighter regions especially prominent in
    the southern hemisphere
  - Ray systems: bright streaks radiating from several craters, most
    visible from the prominent southern crater
- **Background:** Solid black (space), surrounding the Moon disc on all
  sides
- **Lighting:** The Moon is brightly illuminated from approximately the
  right side; surface relief is visible through shadows in craters
- **Image quality:** 514x510 pixels -- moderate resolution; major features
  (maria, large craters, ray systems) are identifiable but fine detail is
  limited
- **No text, labels, or annotations visible**

### Verifiable Facts [-> Accuracy]

- FACT: The image shows the Moon as a near-full disc
- FACT: The background is solid black (space)
- FACT: Dark regions (maria) are visible, primarily in the upper-left and
  center
- FACT: A bright-rayed crater is prominent in the lower/southern portion
  of the disc
- FACT: Bright ray systems radiate from at least one crater
- FACT: The image is 514x510 pixels
- FACT: No text, labels, or annotations appear in the image
- FACT: The Moon fills most of the frame

### Hallucination Risks [-> Accuracy]

- RISK: A model might name specific craters or maria with certainty
  REALITY: At 514x510, features are suggestive but not definitively
  identifiable; Tycho is likely (bright rays in south) but other crater
  names are less certain
- RISK: A model might describe this as a "full Moon" definitively
  REALITY: It appears near-full but the exact phase cannot be determined
  with certainty
- RISK: A model might describe the companion golf ball image (R18) as part
  of this crop
  REALITY: The extracted crop contains only the Moon photograph
- RISK: A model might describe prompt/response text about Apollo 14
  REALITY: No text appears in this crop; the Apollo 14 connection is from
  the page context, not the image
- RISK: A model might claim this is a telescope image or specify the
  telescope/camera used
  REALITY: The equipment cannot be determined from the image

### Detail Inventory [-> Specificity]

- Moon phase: near-full, brightly illuminated
- Disc position: fills most of frame, slightly off-center to right
- Dark regions (maria): upper left and center-left quadrants
- Bright-rayed crater: prominent in southern portion (consistent with Tycho)
- Ray systems: bright streaks radiating from the prominent southern crater
- Highlands: bright regions in southern hemisphere
- Background: solid black (space)
- Surface relief: visible through crater shadows
- Image dimensions: 514x510 pixels
- No text, labels, or annotations

### Domain Context [-> Usefulness]

- **Domain:** Astronomy, space photography
- **Surrounding document context:** This is the first of two images in
  Figure 15 of the Gemini 1.0 technical report (arxiv 2312.11805v5), page
  81. On the PDF page, this Moon photo appears alongside a golf ball photo
  (R18) in a prompt that asks "Find a connection between these. Hint: think
  about historical events." The model connects them via the Apollo 14
  mission (1971) when astronaut Alan Shepard hit golf balls on the lunar
  surface. However, the extracted crop contains only this Moon photograph.
- **Technical terminology:**
  - Maria (singular: mare): dark, flat regions on the Moon's surface formed
    by ancient volcanic eruptions
  - Terrae (highlands): bright, cratered regions
  - Ray system: bright streaks of ejected material radiating from impact
    craters
  - Tycho: prominent young crater in the lunar southern hemisphere,
    identifiable by its extensive ray system
- **Why this image matters:** Part of a two-image visual puzzle testing
  the model's ability to identify the Moon, recognize a golf ball (R18),
  and connect them through historical knowledge (Apollo 14 lunar golf).

### Search Keywords [-> Usefulness]

- Moon, lunar surface, full Moon, craters, maria
- Tycho, ray system, impact crater, highlands
- space photography, astronomy
- Gemini, Figure 15, visual puzzle, image connection
- Apollo 14, lunar golf (page context)

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies the subject (calls it a planet or satellite); describes text or the companion golf ball image not in this crop | Correctly identifies the Moon, notes craters and dark regions; may over-identify specific features at this resolution | Identifies as near-full Moon, correctly describes maria, bright-rayed crater, ray systems, and black background; hedges appropriately on specific feature names given resolution |
| Specificity | "A photo of the Moon" with no surface detail | Describes dark and light regions, mentions craters, notes the black background | Describes maria locations (upper left, center), bright-rayed crater position (southern), ray system details, highlands distribution, illumination direction, and image resolution limitations |
| Completeness | Mentions the Moon but omits surface features or background | Covers the Moon disc, major maria, craters, and black background; may miss ray systems or illumination direction | Accounts for Moon disc (position, phase), maria (location), craters (including bright-rayed southern crater), ray systems, highlands, background, illumination, resolution, and absence of text |
| Usefulness | "A space photo" -- not searchable | Mentions Moon, craters, lunar surface; searchable for "Moon photograph" | Includes Moon, specific feature types (maria, Tycho-like crater, ray systems), Gemini Figure 15 context as part of visual puzzle, and enough detail to distinguish from other Moon photographs |

<br><br>

## doc05-R18 -- Hand holding golf ball indoors

**Figure reference:** Figure 15 image 2, page 81
**Content type:** photo
**Annotation difficulty:** Medium
**Dimensions:** 672x370 pixels

**Note:** The image catalog describes this as "Golf balls on lunar surface"
but the actual crop shows a hand holding a single golf ball in an indoor
setting. No lunar surface is visible. The "lunar" connection is from the
page context (Apollo 14 puzzle), not from the image content.

### Visual Inventory [-> Completeness]

- **Primary subject:** A human hand holding a single white golf ball between
  thumb and fingers, held up toward the ceiling
- **Golf ball:** White, standard size, dimpled surface visible; held between
  the thumb (below) and index/middle fingers (above); some faint markings
  or text may be on the ball but are not clearly legible at this resolution
- **Hand:** Light-skinned hand, viewed from below/behind; the fingers curve
  around the ball; the wrist and part of the forearm are visible
- **Background/setting:** Indoor space -- the photo is taken looking upward
  toward the ceiling:
  - Ceiling: industrial or commercial ceiling with a grid/mesh pattern
    (possibly perforated metal panels or open-grid ceiling tiles)
  - Lighting: multiple linear strip lights (LED or fluorescent) are
    visible through the ceiling grid, running in parallel
  - The ceiling and lighting create a geometric pattern above
- **Camera angle:** Low angle, looking upward; the hand and golf ball are
  between the camera and the ceiling
- **Color palette:** Muted indoor tones; the white golf ball is the
  brightest element; warm skin tone on the hand; gray/silver ceiling
- **Image quality:** 672x370 pixels -- moderate resolution; the golf ball
  dimples are visible but fine text on the ball is not legible
- **No clearly legible text in the image** (faint markings on the golf ball
  are too small to read)

### Verifiable Facts [-> Accuracy]

- FACT: A single golf ball is held in one hand
- FACT: The golf ball is white with visible dimpled surface
- FACT: The setting is indoors (ceiling with grid pattern and strip lights)
- FACT: The photo is taken from below, looking upward
- FACT: A grid/mesh ceiling pattern is visible above
- FACT: Linear strip lights run in parallel across the ceiling
- FACT: The image shows ONE golf ball, not multiple
- FACT: No lunar surface, outdoor scenery, or space-related elements are
  visible
- FACT: The image is 672x370 pixels

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe "golf balls on lunar surface" matching the
  catalog description
  REALITY: The setting is clearly indoors; one golf ball is held in a hand;
  no lunar surface is visible
- RISK: A model might state there are multiple golf balls
  REALITY: Only one golf ball is visible
- RISK: A model might read a specific brand name on the golf ball
  REALITY: Faint markings may be present but are not legible at 672x370
- RISK: A model might describe this as an outdoor setting
  REALITY: The grid ceiling and strip lighting are clearly indoor elements
- RISK: A model might describe the Apollo 14 connection as if visible in
  the image
  REALITY: The Apollo 14 connection is from the page-level prompt context,
  not from anything visible in the crop

### Detail Inventory [-> Specificity]

- Golf ball: white, single, standard size, dimpled surface, faint markings
- Hand: light-skinned, thumb and fingers gripping ball, forearm visible
- Setting: indoor, industrial/commercial ceiling
- Ceiling: grid/mesh pattern, possibly perforated metal panels
- Lighting: multiple parallel linear strip lights (LED or fluorescent)
- Camera angle: low, looking upward through hand toward ceiling
- Color: muted indoor tones, white ball is brightest element
- Image dimensions: 672x370 pixels
- No legible text

### Domain Context [-> Usefulness]

- **Domain:** Sports equipment, indoor photography
- **Surrounding document context:** This is the second of two images in
  Figure 15 of the Gemini 1.0 technical report (arxiv 2312.11805v5), page
  81. It appears alongside a Moon photograph (R17) in a visual puzzle. The
  prompt asks "Find a connection between these" with a hint about
  historical events. The model connects the Moon and golf ball through the
  Apollo 14 mission (1971), when astronaut Alan Shepard hit golf balls on
  the lunar surface. The connection is a knowledge-retrieval task, not
  something visible in either image.
- **Technical terminology:**
  - Apollo 14: third crewed Moon landing (1971); Alan Shepard famously
    hit two golf balls on the lunar surface
- **Why this image matters:** The golf ball is visually simple, but its
  meaning in context requires connecting it to the Moon image and recalling
  a specific historical event. Tests whether an annotation model describes
  what's actually in the crop (hand, golf ball, indoor setting) vs. what
  the page context says it means (lunar golf).

### Search Keywords [-> Usefulness]

- golf ball, hand, indoor, ceiling
- dimpled surface, white ball, strip lighting
- Gemini, Figure 15, visual puzzle, image connection
- Apollo 14, lunar golf (page context connection)
- sports equipment, grid ceiling, industrial interior

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Describes "golf balls on the Moon" or claims outdoor setting; wrong object count | Correctly identifies a hand holding a golf ball indoors; notes the ceiling and lighting | All items correct: single golf ball, held in hand, indoor setting with grid ceiling and strip lights, low angle looking up; does not fabricate lunar surface or outdoor setting |
| Specificity | "A golf ball" with no setting or perspective detail | Describes white dimpled golf ball, hand holding it, indoor ceiling visible | Describes dimple texture, hand position (thumb/fingers), ceiling type (grid/mesh), light type (linear strips), camera angle (low, looking up), color palette |
| Completeness | Mentions golf ball only; omits hand, setting, or camera angle | Covers golf ball, hand, indoor setting, and ceiling; may miss the strip lights or camera angle | Accounts for golf ball (color, texture, markings), hand (skin, grip), ceiling (grid pattern, material), lighting (strip lights, parallel), camera angle, and absence of outdoor/lunar elements |
| Usefulness | "A ball" -- not searchable | Mentions golf ball, hand, indoor; searchable for "golf ball photo" | Includes golf ball details, indoor setting description, Gemini Figure 15 context as part of Moon-golf visual puzzle, and clearly distinguishes the actual image content from the page-context meaning |

<br><br>

## doc05-R19 -- NYC street at night

**Figure reference:** Figure 16, page 82
**Content type:** photo
**Annotation difficulty:** Easy
**Dimensions:** 2072x1560 pixels

**Note:** Agent-written ground truth referenced prompt text and model response
(geolocation to 8th Avenue and West 34th Street). Revised to describe only
the extracted crop.

### Visual Inventory [-> Completeness]

- **Primary subject:** Nighttime photograph of a New York City street
  looking north/northeast, with the Empire State Building prominently
  visible in the center background
- **Empire State Building:** The building's illuminated tower and spire are
  clearly visible against the dark sky, lit in warm gold/yellow; it is the
  tallest and most prominent structure in the frame, positioned in the
  center of the composition
- **Street/road:**
  - A wide multi-lane avenue stretching into the distance toward the
    Empire State Building
  - A white-striped pedestrian crosswalk occupies the lower foreground
  - The road surface is dark asphalt, slightly reflective from moisture
    or artificial light
- **Vehicles:**
  - A large black SUV (appears to be a Chevrolet Suburban or similar)
    in the left foreground, driving through/across the crosswalk
  - Additional vehicle headlights visible further down the avenue
- **Pedestrians:** At least 5-6 people visible:
  - A person standing at the right edge of the crosswalk
  - Several pedestrians on the sidewalk at center-right
  - People near the construction area on the right
- **Traffic infrastructure:**
  - A red traffic light is visible at the left side (signal facing the
    camera direction)
  - Multiple street lights with bright white/yellow glow creating lens
    flare/starburst effects
  - A green street sign is visible near the center of the frame (text
    difficult to read at this resolution but appears to indicate an
    avenue name)
- **Construction area:** Orange/red construction barriers with reflective
  stripes are visible on the right side of the street; the barriers
  partially block the sidewalk
- **Bicycle:** A bicycle is visible parked or standing near center-right
  of the frame
- **Buildings:** Tall buildings line both sides of the street creating an
  urban canyon; many have lit windows; some buildings on the right show
  colored lighting (purple/blue accent lights)
- **Sky:** Dark/black nighttime sky; no stars visible (light pollution)
- **Lighting:** Mixed artificial lighting -- warm gold from the Empire
  State Building, white/yellow from street lights (with starburst
  effects), warm interior light from building windows, neon/accent
  lighting from some buildings
- **Text potentially visible:** A green street sign and possibly blue
  avenue signs are present but text is difficult to confirm at this
  resolution; some illuminated signs on buildings at right appear to have
  text but are not clearly legible

### Verifiable Facts [-> Accuracy]

- FACT: The Empire State Building is visible in the center background,
  illuminated in warm gold/yellow
- FACT: The scene is at nighttime with artificial lighting only
- FACT: A white-striped crosswalk is in the foreground
- FACT: A large black SUV is in the left foreground
- FACT: A red traffic light is visible at the left
- FACT: Orange/red construction barriers with reflective stripes are on the
  right side
- FACT: At least 5-6 pedestrians are visible in the scene
- FACT: A bicycle is visible near center-right
- FACT: Street lights produce visible starburst/lens flare effects
- FACT: Buildings on both sides have lit windows
- FACT: Some buildings on the right have colored accent lighting
  (purple/blue)
- FACT: A green street sign is present near center (text not clearly
  legible)
- FACT: The photo is taken from street level, looking along the avenue

### Hallucination Risks [-> Accuracy]

- RISK: A model might read specific street names from signs not legible at
  this resolution
  REALITY: A green street sign is visible but its text is not clearly
  readable in the crop; the identification as 8th Avenue comes from the
  page-level model response, not from reading signs in the image
- RISK: A model might identify specific store names or businesses
  REALITY: Some illuminated signs are visible on buildings at right but
  text is not clearly legible
- RISK: A model might misidentify the Empire State Building (e.g., calling
  it the Chrysler Building or One World Trade Center)
  REALITY: The distinctive Art Deco spire and tower shape are consistent
  with the Empire State Building
- RISK: A model might claim a specific commemorative lighting color for the
  Empire State Building
  REALITY: The illumination appears gold/yellow but whether this is a
  specific commemorative scheme cannot be determined
- RISK: A model might state the exact time of night
  REALITY: No clock, timestamp, or time indicator is visible
- RISK: A model might describe the SUV as a specific make/model with
  certainty
  REALITY: It appears to be a large black SUV but the exact make/model is
  not definitively identifiable

### Detail Inventory [-> Specificity]

- Empire State Building: center background, illuminated gold/yellow, tower
  and spire clearly visible
- Street: wide multi-lane avenue, looking north/northeast
- Crosswalk: white stripes, foreground
- Black SUV: large, left foreground, driving across crosswalk
- Red traffic light: left side
- Street lights: bright, white/yellow, creating starburst effects
- Green street sign: center, text not clearly legible
- Construction barriers: orange/red, reflective stripes, right side
- Bicycle: near center-right
- Pedestrians: 5-6 visible across the scene
- Buildings: both sides, lit windows, urban canyon effect
- Accent lighting: purple/blue on some right-side buildings
- Road surface: dark asphalt, slightly reflective
- Sky: dark/black, no stars (light pollution)
- Camera position: street level, eye height

### Domain Context [-> Usefulness]

- **Domain:** Urban photography, geolocation, landmark recognition
- **Surrounding document context:** This photo appears in Figure 16 of the
  Gemini 1.0 technical report (arxiv 2312.11805v5), page 82. On the PDF
  page, the photo is embedded in a prompt asking "Do you know the precise
  location where this image was taken?" The model responds identifying
  NYC, specifically 8th Avenue and West 34th Street, using the Empire State
  Building as the key landmark. The extracted crop contains only the
  photograph.
- **Technical terminology:**
  - Geolocation: determining the geographic location from an image
  - Empire State Building: iconic Art Deco skyscraper completed in 1931,
    located at 350 Fifth Avenue in Midtown Manhattan; visible from many
    surrounding streets and avenues
- **Why this image matters:** Tests precise geolocation from visual cues.
  The Empire State Building is an obvious NYC identifier, but pinpointing
  the specific avenue and cross-street requires more detailed spatial
  reasoning about viewing angle, nearby buildings, and street layout.

### Search Keywords [-> Usefulness]

- Empire State Building, New York City, NYC, Manhattan
- nighttime photography, urban scene, street at night
- crosswalk, traffic light, construction barriers
- geolocation, landmark recognition, street identification
- Gemini, Figure 16, visual location, multimodal
- 8th Avenue, West 34th Street (page context)

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies the building (Chrysler, One WTC) or the city; fabricates legible sign text | Correctly identifies Empire State Building and NYC; describes nighttime setting; may claim to read street signs not legible in the crop | All items correct: Empire State Building with gold illumination, nighttime, crosswalk, black SUV, red traffic light, construction barriers; hedges appropriately on sign text legibility |
| Specificity | "A city at night" with no landmark or location detail | Names Empire State Building, identifies NYC, describes nighttime street-level perspective, mentions a few elements (cars, lights) | Describes ESB illumination color (gold/yellow), black SUV in foreground, red traffic light, starburst street lights, construction barriers with reflective stripes, bicycle, 5-6 pedestrians, purple/blue accent lighting on buildings |
| Completeness | Mentions only the Empire State Building; omits street-level elements | Covers ESB, nighttime setting, crosswalk, vehicles, and pedestrians; may miss construction barriers, bicycle, or accent lighting | Accounts for ESB (position, illumination), street (crosswalk, surface), vehicles (SUV, distant cars), traffic infrastructure (red light, street lights, signs), pedestrians, construction area, bicycle, building lighting, sky, and camera position |
| Usefulness | "A photo of a building at night" -- not searchable for location | Mentions Empire State Building, NYC, nighttime; searchable for "NYC street night" | Includes landmark, nighttime details, street-level elements, Gemini Figure 16 geolocation context, and enough visual detail to reconstruct the scene without viewing the image |

<br><br>

## doc05-R20 -- Internet meme

**Figure reference:** Figure 17, page 83
**Content type:** other
**Annotation difficulty:** Medium
**Dimensions:** 1521x2046 pixels

### Visual Inventory [-> Completeness]

- **Content type description:** "Daily Struggle" or "Running Away Balloon"
  internet meme format
- **Visual elements:**
  - Cartoon stick figure person reaching toward a floating object
  - Yellow circle/balloon labeled "Game at 300 FPS"
  - Pink circle labeled "75 hz Monitor" pulling the figure back
  - The meme format conveys being tempted by something unattainable or
    impractical
- **Text visible:**
  - "Game at 300 FPS" on the yellow balloon
  - "75 hz Monitor" on the pink circle
- **Composition:** Meme image shown in a Prompt box with "Can you explain this
  meme?" The Model Response explains the humor: playing a game at 300 FPS is
  pointless with a 75Hz monitor since the monitor can only display 75 frames
  per second, making the higher framerate useless.

### Verifiable Facts [-> Accuracy]

- FACT: The meme is in the "Running Away Balloon" or "Daily Struggle" format
- FACT: The yellow balloon/circle is labeled "Game at 300 FPS"
- FACT: The pink circle is labeled "75 hz Monitor"
- FACT: The stick figure is reaching toward the balloon
- FACT: The prompt asks "Can you explain this meme?"
- FACT: The model explains that 300 FPS is wasted on a 75Hz monitor
- FACT: The model's explanation centers on the monitor's inability to display more than 75 frames per second
- FACT: The meme uses a cartoon/stick figure art style

### Hallucination Risks [-> Accuracy]

- RISK: A model might call this the wrong meme format (e.g., "Distracted Boyfriend" or "Drake meme")
  REALITY: This is the "Running Away Balloon" or "Daily Struggle" meme format
- RISK: A model might state the FPS value as something other than 300
  REALITY: The text reads "Game at 300 FPS"
- RISK: A model might state the monitor refresh rate as 60Hz instead of 75Hz
  REALITY: The text reads "75 hz Monitor"
- RISK: A model might invent additional text labels not present in the meme
  REALITY: The main labels are "Game at 300 FPS" and "75 hz Monitor"
- RISK: A model might over-explain the meme with technical details about V-Sync, G-Sync, or frame timing not present in the model response
  REALITY: The model's explanation focuses on the basic Hz vs FPS mismatch

### Detail Inventory [-> Specificity]

- "Running Away Balloon" meme format with cartoon stick figure
- Yellow balloon/circle: "Game at 300 FPS"
- Pink circle: "75 hz Monitor"
- The figure reaches toward the high-FPS balloon while held back by the
  low-Hz-monitor circle
- The humor relies on knowledge that a monitor's refresh rate caps the
  visible framerate
- 300 FPS vs 75 Hz represents a ~4x mismatch
- Model response explains the core joke without over-elaborating

### Domain Context [-> Usefulness]

- **Domain:** Internet culture, computer gaming, display technology
- **Surrounding document context:** Figure 17 in the Gemini report,
  demonstrating the model's ability to understand internet meme formats and
  explain humor. Requires recognizing the meme template, reading the text
  labels, and applying domain knowledge about FPS and monitor refresh rates.
- **Technical terminology:**
  - FPS (frames per second): the rate at which a game renders frames
  - Hz (Hertz): the refresh rate of a monitor (how many frames it can display
    per second)
  - The joke: 300 FPS is wasted when the monitor can only display 75 of those
    frames per second
- **Why this image matters:** Tests meme comprehension, which requires
  understanding visual template conventions (what the balloon vs person
  represents), reading embedded text, and applying domain-specific knowledge
  (gaming/display technology) to explain the humor.

### Search Keywords [-> Usefulness]

- Gemini, meme understanding, humor explanation
- FPS, frames per second, Hz, refresh rate, monitor
- Running Away Balloon meme, Daily Struggle meme
- gaming, display technology, framerate
- internet culture, meme format, visual humor

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies the meme format; states wrong FPS or Hz values; misexplains the joke | Correctly reads "300 FPS" and "75 hz Monitor"; explains the Hz vs FPS mismatch; may misname the meme format | All text labels accurate, meme format correctly identified, and the FPS/Hz explanation matches the model response exactly |
| Specificity | "An internet meme about gaming" with no text values or format name | Names the meme format, quotes "Game at 300 FPS" and "75 hz Monitor," explains the Hz vs FPS joke | Identifies the meme format, quotes both labels exactly, describes the balloon/person visual metaphor, explains the 300 vs 75 numerical mismatch, and notes the stick figure art style |
| Completeness | Describes only the image or only the explanation; omits text labels | Covers the visual elements, text labels, prompt question, and model explanation; may omit the meme format name or the visual metaphor | Accounts for the meme format, both text labels, the stick figure reaching for the balloon, the prompt asking for explanation, and the model's FPS/Hz mismatch explanation |
| Usefulness | "A meme" -- no topic, no text content, not searchable | Mentions FPS vs Hz meme, gaming context; searchable for "Gemini meme understanding" | Includes meme format name, both text labels, the FPS/Hz technical explanation, and connects to the paper's demonstration of cultural and technical humor comprehension |

<br><br>

## doc05-R21 -- Chinese family tree diagram

**Figure reference:** Figure 18, page 84
**Content type:** diagram
**Annotation difficulty:** Medium
**Dimensions:** 493x512 pixels

### Visual Inventory [-> Completeness]

- **Components/nodes:** Blue circular icons with face silhouettes representing
  family members across 3 generations (11 total nodes):
  - **Top row (grandparents, 4 nodes):**
    - Left pair: yeye (paternal grandfather), nainai (paternal grandmother)
      -- both have gray hair and glasses
    - Right pair: waipo (maternal grandmother), waigong (maternal
      grandfather) -- both have gray hair and glasses
  - **Middle row (parents, 2 nodes):**
    - baba (father) on the left -- dark hair, blue circle
    - mama (mother) on the right -- dark hair, lighter/white circle
      background
  - **Bottom row (children, 5 nodes, left to right):**
    - didi (younger brother) -- male hairstyle
    - meimei (younger sister) -- female hairstyle
    - wo (me) -- highlighted with a red/coral box border
    - gege (older brother) -- male hairstyle
    - jiejie (older sister) -- female hairstyle with bun
- **Connections:** Light blue lines connecting:
  - Paternal grandparents (yeye, nainai) down to baba
  - Maternal grandparents (waipo, waigong) down to mama
  - Baba and mama via a horizontal bar down to all 5 children
- **Hierarchy or flow direction:** Top-to-bottom generational hierarchy:
  grandparents -> parents -> children
- **Annotations or callouts:**
  - Title: "The Basic Chinese Family Tree" in black text at top
  - Each node labeled with Chinese characters (above) and pinyin
    romanization with tone marks (below)
  - "wo" (me) node highlighted with a red/coral box border to indicate the
    reference perspective
- **Style elements that carry meaning:**
  - Blue circular icons for all family members, with gender-differentiated
    features (hairstyles, accessories)
  - Grandparents distinguished by gray hair and glasses
  - Red/coral border on "wo" (me) vs blue borders on all other children
  - Paternal grandparents on the left, maternal grandparents on the right
  - Light gray background for the overall diagram

### Verifiable Facts [-> Accuracy]

- FACT: The title reads "The Basic Chinese Family Tree"
- FACT: There are 3 generational rows: grandparents, parents, children
- FACT: The paternal grandfather is labeled "yeye"
- FACT: The paternal grandmother is labeled "nainai"
- FACT: The maternal grandmother is labeled "waipo"
- FACT: The maternal grandfather is labeled "waigong"
- FACT: The father is labeled "baba"
- FACT: The mother is labeled "mama"
- FACT: There are 5 children in the bottom row
- FACT: The children are labeled didi, meimei, wo, gege, jiejie
- FACT: "wo" (me) has a red/coral box border distinguishing it from other
  nodes, which all have blue borders
- FACT: All grandparent figures have gray hair and glasses
- FACT: Parent and children figures have dark hair (no glasses)
- FACT: Face icons have gender-differentiated hairstyles
- FACT: Pinyin labels include tone marks (e.g., "yeye" with accent marks)
- FACT: The diagram has a light gray background
- FACT: Connecting lines are light blue

### Hallucination Risks [-> Accuracy]

- RISK: A model might confuse paternal and maternal grandparent labels (e.g., assigning "yeye" to the maternal side)
  REALITY: Yeye and nainai are paternal; waigong and waipo are maternal
- RISK: A model might state there are 4 children instead of 5
  REALITY: There are 5 children: didi, meimei, wo, gege, jiejie
- RISK: A model might add family members not shown (e.g., uncles, aunts, cousins)
  REALITY: Only grandparents, parents, and siblings are shown
- RISK: A model might reverse the age ordering of siblings (e.g., calling gege "younger brother")
  REALITY: Gege means older brother; didi means younger brother
- RISK: A model might claim the Chinese characters are not present and only pinyin is shown
  REALITY: Both Chinese characters and pinyin romanization label each node
- RISK: A model might state the diagram uses different colored circles for
  different genders
  REALITY: All icons use blue circles (one shade); gender is distinguished
  by hairstyle and accessories within the icons, not by circle color. Only
  "wo" has a red/coral border instead of blue.

### Detail Inventory [-> Specificity]

- Title: "The Basic Chinese Family Tree" at top of diagram
- 3 generational tiers with 11 total family member nodes
- Top row: 4 grandparents split into paternal (left) and maternal (right) pairs
- Middle row: baba (father, left) and mama (mother, right)
- Bottom row: 5 children ordered left to right: didi (younger brother),
  meimei (younger sister), wo (me), gege (older brother), jiejie (older sister)
- All nodes are blue circular face silhouettes with gender-differentiated
  hairstyles
- Grandparent figures have gray hair and glasses; parent/child figures have
  dark hair
- "wo" (me) has a distinctive red/coral box border; all other children have
  blue borders
- Each node labeled with Chinese characters (above) and pinyin with tone
  marks (below)
- Light blue connecting lines between generations
- Parents connect to children via a horizontal bar structure
- Paternal side (yeye, nainai) on the left; maternal side (waipo, waigong)
  on the right
- Light gray diagram background
- Small image dimensions (493x512 pixels) -- compact diagram

### Domain Context [-> Usefulness]

- **Domain:** Chinese language, family terminology, cultural knowledge
- **Surrounding document context:** Figure 18 in the Gemini report,
  demonstrating the model's ability to interpret a structured diagram with
  Chinese-language labels and answer questions about familial relationships.
  Tests both visual diagram comprehension and Chinese cultural knowledge.
- **Technical terminology:**
  - Pinyin: romanization system for Standard Mandarin Chinese
  - Chinese family terms differ based on paternal vs maternal lineage (unlike
    English, which uses "grandfather/grandmother" for both sides)
  - Yeye/nainai: paternal grandfather/grandmother
  - Waigong/waipo: maternal grandfather/grandmother
  - Gege/jiejie: older brother/sister; didi/meimei: younger brother/sister
- **Why this image matters:** Demonstrates understanding of a culturally
  specific diagram where the labels are in Chinese and the family terminology
  system differs from English. The model must read the diagram structure,
  understand the Chinese terms, and map them to the correct familial
  relationships.

### Search Keywords [-> Usefulness]

- Gemini, Chinese family tree, family terminology
- yeye, nainai, waigong, waipo, baba, mama
- gege, jiejie, didi, meimei
- pinyin, Chinese characters, kinship terms
- paternal grandmother, maternal grandfather
- diagram comprehension, cultural knowledge

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Confuses paternal and maternal sides; states wrong number of children; misassigns pinyin labels | Correctly maps all grandparent terms to the right sides; identifies 5 children; may miss one sibling label | All 11 family member labels correctly identified, paternal/maternal sides correctly mapped, "wo" red border noted, and sibling age ordering accurate |
| Specificity | "A family tree diagram in Chinese" with no specific labels | Names the grandparent terms (yeye, nainai, waigong, waipo), parents, and some siblings; mentions pinyin | Lists all 11 family members with pinyin labels, notes Chinese characters alongside pinyin, describes the red border on "wo," specifies the left-right paternal/maternal split |
| Completeness | Lists only grandparents or only children; omits the title or the prompt/response | Covers all 3 generations, the title, and the prompt/response; may omit the red border or the exact sibling ordering | Accounts for the title, all 3 generations with all 11 labels, the red border on "wo," the paternal/maternal split, the connecting lines, and the prompt/response content |
| Usefulness | "A Chinese diagram" -- no family terms, no structure described | Mentions Chinese family terminology, paternal vs maternal distinction; searchable for "Chinese family tree" | Includes all pinyin terms with meanings, explains the paternal/maternal distinction, notes the age-based sibling terminology, and connects to the paper's cross-cultural knowledge demonstration |

<br><br>

## doc05-R22 -- Rendered "Opossum Search" website

**Figure reference:** Figure 19, page 86
**Content type:** screenshot
**Annotation difficulty:** Medium
**Dimensions:** 512x271 pixels

### Visual Inventory [-> Completeness]

- **Layout:** A rendered webpage mockup of a search engine called "Opossum
  Search," displayed as a browser-like view with no visible browser chrome
  (no address bar, tabs, or window controls)
- **Header area (dark gray/charcoal background):**
  - Title text: "Opossum Search" in large white serif or sans-serif font,
    centered at top
  - A small photograph of an opossum centered below the title; the opossum
    appears white/light-colored, perched on a white wooden fence at night
    against a dark background; the photo is roughly 100x75 pixels (small
    thumbnail within the page)
- **Search area (white/light gray background):**
  - A text input field spanning most of the width with placeholder text
    "Search the web" in gray
  - A "Search" button to the right of the input field (gray button with
    dark text)
- **Footer (dark gray/black background):**
  - Text: "Powered by Google Search" in white, centered
- **Overall styling:** Clean, minimal design; dark header and footer with
  white/light content area; resembles a simplified Google-style search page
  with custom branding
- **Image quality:** 512x271 pixels -- moderate resolution; the opossum
  photo is small but identifiable; text is legible

### Verifiable Facts [-> Accuracy]

- FACT: The page title reads "Opossum Search"
- FACT: A small photo of an opossum is centered below the title
- FACT: The opossum appears to be on a white fence/railing at night
- FACT: A search input field has placeholder text "Search the web"
- FACT: A "Search" button appears to the right of the input
- FACT: The footer reads "Powered by Google Search"
- FACT: The header and footer have dark gray/black backgrounds
- FACT: The search area has a white/light background
- FACT: The image is 512x271 pixels

### Hallucination Risks [-> Accuracy]

- RISK: A model might describe this as an actual website screenshot
  REALITY: This is a rendered mockup generated from code (shown in the
  surrounding page context); it is not a screenshot of a live website
- RISK: A model might claim search results are visible
  REALITY: The search field is empty and no results are shown
- RISK: A model might describe detailed features of the opossum photo
  REALITY: The opossum thumbnail is very small (~100x75 pixels within
  the 512x271 image); only basic details (animal on fence, nighttime)
  are visible
- RISK: A model might identify specific CSS frameworks or technologies
  REALITY: The styling is visible but the specific technology stack
  cannot be determined from the rendered output alone
- RISK: A model might state the footer says "Powered by Google" without
  "Search"
  REALITY: The full text reads "Powered by Google Search"

### Detail Inventory [-> Specificity]

- Page title: "Opossum Search" (large, white, centered)
- Opossum photo: small thumbnail, white/light-colored animal on white
  wooden fence, nighttime/dark background
- Search input: wide text field, placeholder "Search the web"
- Search button: gray, text "Search," right of input
- Header background: dark gray/charcoal
- Content area: white/light gray
- Footer background: dark gray/black
- Footer text: "Powered by Google Search" (white, centered)
- Overall design: minimal, Google-style search page with custom branding
- Image dimensions: 512x271 pixels
- No browser chrome visible (no URL bar, tabs, or window controls)

### Domain Context [-> Usefulness]

- **Domain:** Web development, code generation, UI rendering
- **Surrounding document context:** This rendered page appears in Figure 19
  of the Gemini 1.0 technical report (arxiv 2312.11805v5), page 86. The
  figure demonstrates Gemini's ability to generate functional HTML/CSS/JS
  code from a text description, then render the result. The prompt asks the
  model to create a search engine page with an opossum theme.
- **Technical terminology:**
  - Rendered code: the visual output produced by executing generated
    HTML/CSS code in a browser
  - Search engine mockup: a non-functional UI that resembles a search
    engine's landing page
- **Why this image matters:** Shows the model can translate a creative text
  prompt into a working webpage with correct layout, styling, and embedded
  media. Tests code generation + visual design + brand theming capabilities.

### Search Keywords [-> Usefulness]

- Opossum Search, search engine, website mockup
- rendered code, HTML, CSS, web page
- Gemini, Figure 19, code generation, UI rendering
- Google Search, Powered by, search box
- web development, frontend, code to UI

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Describes it as a real website screenshot; wrong title text; misreads footer | Correctly identifies "Opossum Search" title, search box, and footer text; correctly notes it's a rendered mockup | All text accurate (title, placeholder, button, footer), correctly identifies opossum photo, notes dark/light color scheme, and that this is rendered code output not a live site |
| Specificity | "A search engine page" with no title or detail | Names "Opossum Search," describes search box and footer, mentions the opossum image | Describes title font color and position, opossum photo content (animal on fence, nighttime), search field placeholder text, button label, header/footer background colors, and overall design style |
| Completeness | Mentions title only; omits the search box, footer, or opossum photo | Covers title, opossum photo, search box, and footer; may miss the color scheme or placeholder text | Accounts for all elements: title, opossum photo (with content description), search input (with placeholder), button, header/footer (with colors), content area, and absence of browser chrome |
| Usefulness | "A webpage" -- not searchable | Mentions Opossum Search, search engine mockup, code generation; searchable for "opossum search engine" | Includes all text content, design description, Gemini Figure 19 context as code-generation demo, and enough detail to understand the complete page layout without viewing the image |

<br><br>

## doc05-R24 -- Rendered combined function plot

**Figure reference:** Figure 22 (rendered output), page 89
**Content type:** chart-simple
**Annotation difficulty:** Easy
**Dimensions:** 512x327 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** Single matplotlib line plot on white background
- **Curve:** One blue line (default matplotlib blue) showing the function
  1000*sin(x) + exp(x)
- **Behavior:** The curve starts near 0 at x=0, rises to a local peak around
  ~1000 near x=1.5-2, dips back toward 0 around x=4-5, then rises
  exponentially reaching approximately 22000 at x=10. The sinusoidal
  oscillation is visible at lower x values but overwhelmed by the
  exponential at higher x.
- **X-axis:** Range 0 to 10, tick marks at 0, 2, 4, 6, 8, 10. No axis label.
- **Y-axis:** Range approximately 0 to ~22000, tick marks at 0, 5000, 10000,
  15000, 20000. No axis label.
- **Frame:** Standard matplotlib box frame on all four sides
- **Background:** White plot area, no grid lines
- **No title, no legend, no annotations**

### Verifiable Facts [-> Accuracy]

- FACT: There is exactly one data series (one blue line)
- FACT: The x-axis spans from 0 to 10 with ticks at even integers
- FACT: The y-axis reaches approximately 20000-22000 at the right edge
- FACT: The curve has a local maximum around x=1.5-2 with value near 1000
- FACT: The curve dips to near 0 (or slightly below) around x=4-5
- FACT: The curve rises steeply (exponentially) from x=6 onward
- FACT: There are no axis labels, title, or legend
- FACT: There is no grid overlay
- FACT: The plot uses a white background with a box frame
- FACT: Y-axis tick labels include 0, 5000, 10000, 15000, 20000

### Hallucination Risks [-> Accuracy]

- RISK: "The chart shows an exponential function" -- REALITY: It shows
  1000*sin(x) + exp(x), a combined function. The sinusoidal component is
  visible as the local peak and dip at low x values. A pure exponential
  would not have that local maximum and dip.
- RISK: "Y-axis label reads 'Value'" or inventing any axis label -- REALITY:
  There are no axis labels on either axis
- RISK: "The curve reaches 25000" -- REALITY: The maximum visible value is
  approximately 22000 at x=10; 20000 is the highest labeled tick
- RISK: "There are two curves" or "multiple data series" -- REALITY: There
  is exactly one blue line
- RISK: "The chart has a title" -- REALITY: No title is present
- RISK: Adding grid lines that don't exist -- REALITY: White background, no
  grid

### Detail Inventory [-> Specificity]

- Single blue line (matplotlib default color #1f77b4)
- Local peak near x~1.5-2 reaching approximately 1000
- Local minimum near x~4-5 close to 0 or slightly negative
- Exponential rise dominating from x~6 onward
- Final value approximately 22000 at x=10
- Y-axis ticks: 0, 5000, 10000, 15000, 20000
- X-axis ticks: 0, 2, 4, 6, 8, 10
- Standard matplotlib box frame (all four sides)
- White background, no grid
- No axis labels, no title, no legend, no annotations
- Tick label font: standard matplotlib default (small, black)

### Domain Context [-> Usefulness]

This is the rendered output of code generated by Gemini in Figure 22. The
prompt (shown in R23, the 2x2 subplot grid) asks the model to take the
function from the top-left subplot (sine), multiply by 1000, and add it to
the bottom-left subplot (exponential), then generate matplotlib code for the
result. This plot is the rendered output of that generated code:
`plt.plot(x, 1000*y1 + y2)` where `y1 = np.sin(x)` and `y2 = np.exp(x)`.

The chart demonstrates Gemini's ability to understand visual mathematical
functions, compose them algebraically, and produce correct executable code.
The correctness of this output can be verified mathematically: the local
peak near x=pi/2 (~1.57) should be approximately 1000*1 + e^1.57 ~ 1005,
and the dip near x=3*pi/2 (~4.71) should be approximately 1000*(-1) +
e^4.71 ~ -1000 + 111 ~ -889, which is consistent with the slight dip below
zero visible in the chart.

### Search Keywords [-> Usefulness]

- matplotlib, line plot, rendered output, code generation
- sine function, exponential function, combined function
- 1000*sin(x) + exp(x), mathematical composition
- Gemini code generation, Figure 22, visual math
- function composition, algebraic combination

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | "An exponential growth chart" -- misses the sinusoidal component entirely; may invent axis labels or a title | Correctly identifies it as a single line plot, notes the curve rises steeply at high x values, correct axis ranges | Identifies the combined sinusoidal + exponential behavior (local peak, dip, then exponential rise), correct axis tick values, correctly notes absence of labels/title/legend/grid |
| Specificity | "A line chart" with no axis values or curve behavior | Describes "curve rising to about 20000" and "x-axis 0 to 10"; mentions blue line | Specifies local peak near x=1.5-2 (~1000), dip near x=4-5, exponential rise from x=6, maximum ~22000 at x=10; identifies all tick mark positions |
| Completeness | Mentions only the curve direction; omits axis ranges, styling, or absence of labels | Covers the curve, both axis ranges, and white background; may miss the local peak/dip or frame details | Accounts for curve shape (peak, dip, rise), both axis tick positions, frame style, white background, absence of grid/labels/title/legend, and single data series |
| Usefulness | "A chart" -- no searchable content | Mentions line plot, exponential behavior, matplotlib styling; findable for "line chart" | Connects to Figure 22 code generation context, identifies 1000*sin(x)+exp(x) function, mentions matplotlib rendered output, findable for "Gemini code generation math plot" |

<br><br>

## doc05-R23 -- 4 matplotlib subplots

**Figure reference:** Figure 22, page 89
**Content type:** chart-complex
**Annotation difficulty:** Medium
**Dimensions:** 512x506 pixels

### Visual Inventory [-> Completeness]

- **Chart type:** 2x2 grid of four matplotlib subplots
- **Panels:**
  - **Top-left:** Sine wave -- smooth blue curve oscillating between -1.00 and
    1.00 over two full periods; x-axis 0 to 10, y-axis ticks at 0.25
    increments from -1.00 to 1.00
  - **Top-right:** Tangent function -- blue curve with 4 visible vertical
    asymptotes (near x ~ 1.6, 4.7, 7.9, and edges); x-axis 0 to 10, y-axis
    from -40 to 20
  - **Bottom-left:** Exponential curve -- blue curve near zero for x < 6, then
    rising sharply; x-axis 0 to 10, y-axis ticks at 0, 5000, 10000, 15000,
    20000
  - **Bottom-right:** 3D surface plot -- smooth surface rendered in a
    viridis-like colormap (blue at low values, green in the middle, yellow at
    high values); colorbar on right side with ticks from 0.00 to 2.00 at 0.25
    increments; x and y axes both 0.0 to 1.0
- **Layout:** Four panels separated by thin white gutters; each panel has a
  thin black border/frame
- **Line style:** All 2D plots use a single solid blue line with no markers
- **Gridlines:** No visible gridlines on the three 2D plots; light gray
  gridlines visible on the 3D surface
- **Labels:** No subplot titles, no axis labels -- only numeric tick values on
  each axis
- **Background:** White background for all four panels

### Verifiable Facts [-> Accuracy]

- FACT: The image contains exactly 4 subplots in a 2x2 grid
- FACT: The top-left subplot shows a sine wave
- FACT: The top-right subplot shows a tangent function with vertical asymptotes
- FACT: The bottom-left subplot shows an exponential curve
- FACT: The bottom-right subplot shows a 3D surface plot
- FACT: The sine wave y-axis ranges from -1.00 to 1.00
- FACT: The tangent plot y-axis ranges from approximately -40 to 20
- FACT: The exponential plot y-axis reaches approximately 20000
- FACT: The 3D surface colorbar ranges from 0.00 to 2.00
- FACT: All three 2D subplots have x-axis ranging from 0 to 10
- FACT: The 3D surface x and y axes both range from 0.0 to 1.0
- FACT: All 2D curves are rendered as solid blue lines
- FACT: No subplot titles or axis labels are present -- only tick values

### Hallucination Risks [-> Accuracy]

- RISK: A model might confuse which function is in which subplot position
  REALITY: Sine is top-left, tangent is top-right, exponential is bottom-left,
  3D surface is bottom-right
- RISK: A model might identify the bottom-left as a polynomial or logarithmic
  curve instead of exponential
  REALITY: The curve shape (flat near zero for small x, sharply rising to
  ~20000) is characteristic of an exponential function
- RISK: A model might state the 3D surface colorbar ranges from 0 to 1
  REALITY: The colorbar clearly shows ticks from 0.00 to 2.00
- RISK: A model might claim axis labels or subplot titles are present
  REALITY: Only numeric tick values appear -- no text labels or titles
- RISK: A model might describe prompt text, code, or a rendered output plot
  that are on the same PDF page but not in this crop
  REALITY: The extracted image contains only the 2x2 subplot grid
- RISK: A model might claim there are more or fewer than 4 asymptotes in the
  tangent plot
  REALITY: 4 vertical asymptotes are visible (approximately at x ~ 1.6, 4.7,
  7.9, and near x ~ 10)

### Detail Inventory [-> Specificity]

- 2x2 matplotlib subplot grid, 512x506 pixels total
- Subplot positions: sine (top-left), tangent (top-right), exponential
  (bottom-left), 3D surface (bottom-right)
- Sine wave: exactly two full periods visible, smooth curve, y-axis fine
  graduation at 0.25 intervals
- Tangent function: 4 vertical asymptotes creating characteristic repeated
  pole pattern, y-axis range much larger on the negative side (-40) than
  positive (20)
- Exponential curve: essentially zero for x < 4, then curves upward steeply;
  y-axis ticks at 5000 intervals
- 3D surface: smooth surface with viridis-like colormap gradient, both ground
  axes 0.0 to 1.0, surface rises toward one corner
- Colorbar: vertical bar on right side of 3D subplot, 0.00 to 2.00 with 0.25
  increments
- All 2D lines are solid blue with no data point markers
- No titles, no axis labels, no legends -- purely numeric tick annotations
- White panel backgrounds, thin black borders, white gutters between panels

### Domain Context [-> Usefulness]

- **Domain:** Mathematical functions, data visualization, matplotlib plotting
- **Surrounding document context:** Figure 22 in the Gemini 1.0 technical
  report (page 89). On the PDF page, this 2x2 subplot grid serves as the
  input image for a multimodal code generation task where the model must
  identify functions from visual plots and compose them mathematically. The
  surrounding page text includes an instruction prompt and the model's code
  response, but none of that text appears in this extracted crop.
- **Technical terminology:**
  - Sine function: periodic oscillation between -1 and 1
  - Tangent function: periodic with vertical asymptotes where cos(x) = 0
  - Exponential function: grows proportional to its current value
  - 3D surface plot: visualization of a function f(x, y) as a colored surface
  - Viridis colormap: perceptually uniform colormap from blue through green to
    yellow
- **Why this image matters:** The 2x2 grid is the visual input that a
  multimodal model must interpret. Annotation quality depends on correctly
  identifying all four function types from their curve shapes alone (no labels
  or titles provide hints). The absence of axis labels makes this a pure visual
  identification task.

### Search Keywords [-> Usefulness]

- matplotlib, subplot, 2x2 grid, Python plotting
- sine wave, tangent function, exponential curve, 3D surface plot
- mathematical function visualization, plot identification
- viridis colormap, function plots, multimodal input
- Gemini, code generation, visual math reasoning

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misidentifies function types (e.g., calls exponential "logarithmic" or tangent "cosecant"); gets subplot positions wrong; states wrong axis ranges | Correctly identifies all 4 functions and their grid positions; axis ranges approximately right; may get colorbar range wrong (e.g., 0-1 instead of 0-2) | All 4 functions correctly identified with positions, axis ranges match visible ticks (sine -1 to 1, tangent -40 to 20, exponential to 20000, colorbar 0-2), notes absence of labels/titles |
| Specificity | "Four math plots" with no function names or axis details | Names all 4 functions with grid positions, gives approximate axis ranges, mentions 3D surface has a colormap | Specifies sine period count, tangent asymptote count, exponential knee location, colorbar range and tick interval, line color, colormap type, absence of titles/labels |
| Completeness | Describes only 2-3 of the 4 subplots; omits the 3D surface or tangent asymptotes | Covers all 4 subplots with function types and approximate ranges; mentions the 2x2 layout | All 4 subplots described with function type, axis ranges, and distinctive features (asymptotes, periods, curve shape, colormap); notes layout, styling (blue lines, no markers), and absence of labels |
| Usefulness | "Some function plots" -- not searchable for any specific function type or visualization term | Names the functions and "matplotlib subplot grid"; a search for "sine tangent exponential" would find it | Explains this is a visual function identification challenge with no text cues, connects to multimodal code generation context; searchable for specific functions, matplotlib, and visual math reasoning |

<br><br>

## doc05-V01 -- Grouped bar chart, normalized performance across capabilities

**Figure reference:** Figure 3, page 9
**Content type:** chart-complex
**Annotation difficulty:** Hard
**Dimensions:** vector (rendered from PDF page at 2x scale)

### Visual Inventory [-> Completeness]

- **Chart type:** Grouped bar chart with 4 bars per group, 6 groups
- **Y-axis:** "Normalized Performance vs Pro" (rotated label); scale from 0.0
  to 1.4, ticks at 0.2 intervals
- **X-axis categories (6 groups, rotated diagonal labels):** Factuality,
  Long-Context, Math/Science, Summarization, Reasoning, Multilinguality
- **Legend (top-right corner, boxed):** Nano 1 (salmon/pink-red), Nano 2
  (golden yellow), Pro (muted green), Ultra (muted blue)
- **Reference line:** Dashed horizontal gray line at y = 1.0 (Pro baseline)
- **Bar heights (approximate):**
  - Factuality: Nano 1 ~0.70, Nano 2 ~0.81, Pro = 1.0, Ultra ~1.08
  - Long-Context: Nano 1 ~0.50, Nano 2 ~0.68, Pro = 1.0, Ultra ~1.25
  - Math/Science: Nano 1 ~0.55, Nano 2 ~0.62, Pro = 1.0, Ultra ~1.32
  - Summarization: Nano 1 ~0.30, Nano 2 ~0.55, Pro = 1.0, Ultra ~1.18
  - Reasoning: Nano 1 ~0.50, Nano 2 ~0.64, Pro = 1.0, Ultra ~1.22
  - Multilinguality: Nano 1 ~0.65, Nano 2 ~0.78, Pro = 1.0, Ultra ~1.10
- **Bar colors:** Soft/muted pastel tones -- salmon-red (Nano 1), golden-yellow
  (Nano 2), sage-green (Pro), periwinkle-blue (Ultra)
- **Page header:** "Gemini: A Family of Highly Capable Multimodal Models"
  appears above two thin horizontal gray lines at the very top of the crop
  (this is a running page header, not a chart title)
- **Background:** White; no gridlines except the dashed reference line at 1.0
- **Bar style:** Solid fill, no outlines, no value labels on bars

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 6 category groups on the x-axis
- FACT: There are exactly 4 bars per group (Nano 1, Nano 2, Pro, Ultra)
- FACT: The y-axis label reads "Normalized Performance vs Pro"
- FACT: All Pro bars reach exactly 1.0 (the normalization baseline)
- FACT: All Ultra bars exceed 1.0 (Ultra outperforms Pro in every category)
- FACT: All Nano 1 and Nano 2 bars are below 1.0
- FACT: Nano 1 is consistently the shortest bar in every group
- FACT: The highest Ultra bar is in Math/Science (~1.32)
- FACT: The lowest Nano 1 bar is in Summarization (~0.30)
- FACT: A dashed horizontal reference line appears at y = 1.0
- FACT: The 6 categories are Factuality, Long-Context, Math/Science,
  Summarization, Reasoning, Multilinguality
- FACT: The legend lists 4 entries: Nano 1, Nano 2, Pro, Ultra
- FACT: The y-axis scale goes from 0.0 to 1.4
- FACT: The x-axis labels are rotated diagonally

### Hallucination Risks [-> Accuracy]

- RISK: A model might invent specific numeric scores (e.g., "Ultra achieves
  1.32 on Math/Science") when only approximate values are readable from bar
  heights
  REALITY: No exact values are labeled on the bars; heights can only be
  estimated from the y-axis gridlines
- RISK: A model might add benchmark names not shown (e.g., "MMLU",
  "HellaSwag", "GSM8K") as if they appear in the chart
  REALITY: Only the 6 high-level category names appear on the x-axis; no
  specific benchmark names are visible
- RISK: A model might claim there is a "Gemini Pro 1.5" or "GPT-4" bar
  REALITY: Only 4 model variants are shown: Nano 1, Nano 2, Pro, Ultra
- RISK: A model might state the y-axis goes to 1.5 or 2.0
  REALITY: The y-axis clearly tops out at 1.4
- RISK: A model might describe this as showing absolute performance scores
  REALITY: The y-axis explicitly says "Normalized Performance vs Pro" -- all
  values are relative to Pro = 1.0
- RISK: A model might claim Ultra underperforms Pro in some category
  REALITY: Ultra exceeds 1.0 in all 6 categories

### Detail Inventory [-> Specificity]

- Grouped bar chart: 4 bars x 6 groups = 24 total bars
- Normalization: all values expressed relative to Pro (= 1.0 baseline)
- Consistent ordering within each group: Nano 1, Nano 2, Pro, Ultra (left to
  right, matching legend order top to bottom)
- Ultra's strongest advantage over Pro: Math/Science (~1.32, or ~32% better)
- Ultra's smallest advantage over Pro: Factuality (~1.08, or ~8% better)
- Nano 1's worst category: Summarization (~0.30, or ~70% below Pro)
- Nano 1's best category: Factuality (~0.70, or ~30% below Pro)
- The gap between Nano 1 and Nano 2 varies by category -- smallest in
  Factuality (~0.11 difference), largest in Summarization (~0.25 difference)
- Dashed reference line at 1.0 visually separates "better than Pro" (above)
  from "worse than Pro" (below)
- Pastel color palette: bars are soft/muted tones, not saturated
- No error bars, confidence intervals, or data point markers
- X-axis labels rotated approximately 45 degrees for readability
- Running page header with title and two thin rules at top of crop (not part
  of the chart itself)

### Domain Context [-> Usefulness]

- **Domain:** AI/ML model benchmarking, large language model evaluation
- **Surrounding document context:** Figure 3 in the Gemini 1.0 technical
  report (page 9). This chart summarizes the Gemini model family's
  performance across 6 broad capability categories. It normalizes all scores
  to Pro = 1.0, making it easy to see how the smaller (Nano) and larger
  (Ultra) variants compare to the mid-tier model.
- **Technical terminology:**
  - Normalized performance: scores divided by Pro's score so Pro = 1.0
  - Nano 1, Nano 2: smaller Gemini model variants for on-device use
  - Pro: mid-tier Gemini model
  - Ultra: largest Gemini model variant
  - Factuality, Long-Context, Math/Science, Summarization, Reasoning,
    Multilinguality: high-level capability categories that aggregate multiple
    individual benchmarks
- **Why this image matters:** This is the summary comparison chart for the
  entire Gemini model family. It establishes the performance hierarchy
  (Ultra > Pro > Nano 2 > Nano 1) and shows where the gaps are largest
  (Math/Science, Long-Context) and smallest (Factuality, Multilinguality).
  High-value for RAG retrieval since users searching for "Gemini model
  comparison" or "Gemini benchmark results" would want this chart.

### Search Keywords [-> Usefulness]

- Gemini, model comparison, benchmark, performance
- Nano 1, Nano 2, Pro, Ultra, model family
- normalized performance, bar chart, capability comparison
- factuality, long-context, math, science, summarization, reasoning,
  multilinguality
- language understanding, model evaluation, grouped bar chart

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Wrong model names or number of categories; claims absolute scores instead of normalized; states Ultra underperforms Pro somewhere | Correctly names all 4 models and 6 categories; states normalization is relative to Pro; gets approximate bar heights roughly right | All 4 models, all 6 categories, normalization to Pro = 1.0, dashed reference line, approximate bar heights correct, notes Ultra always above 1.0 and Nano 1 always lowest |
| Specificity | "A bar chart comparing models" with no model names or category names | Names all 4 models and 6 categories, states Pro = 1.0 baseline, mentions Ultra is highest | Gives approximate bar heights for each model-category pair, identifies strongest/weakest categories per model, notes color mapping, describes the pastel palette, mentions rotated x-axis labels |
| Completeness | Describes only 2-3 models or 2-3 categories; omits the reference line or legend | Covers all 4 models and all 6 categories; mentions the reference line and normalization; notes the legend | All 24 bars accounted for with approximate heights, dashed reference line noted, legend described with color mapping, axis labels and scale described, bar ordering within groups noted |
| Usefulness | "Model performance chart" -- not searchable for specific models or capabilities | Names Gemini model variants and capability categories; searchable for "Gemini benchmark comparison" | Explains the normalization concept (vs Pro), identifies where Ultra has largest/smallest advantages, connects to model family hierarchy; searchable for specific models, categories, and "normalized performance" |

<br><br>

## doc05-V02 -- Negative log likelihood vs sequence position

**Figure reference:** Figure 4, page 11
**Content type:** chart-simple
**Annotation difficulty:** Medium
**Dimensions:** vector (rendered from PDF page at 2x scale)

### Visual Inventory [-> Completeness]

- **Chart type:** Line chart with 2 data series, logarithmic x-axis
- **Y-axis:** Labeled "NLL" (rotated vertically); no numeric tick values visible
  on the y-axis -- only the label and unlabeled tick marks
- **X-axis:** Labeled "Sequence position"; logarithmic scale with 13 ticks: 8,
  16, 32, 64, 128, 256, 512, 1K, 2K, 4K, 8K, 16K, 32K
- **Legend (top-right, inside chart area):** Pro (green line), Ultra (blue line)
- **Lines:**
  - **Pro (green):** Smooth curve starting high at position 8, decreasing
    gradually across the full range, flattening toward the right end (16K-32K)
  - **Ultra (blue):** Smooth curve starting near Pro at position 8 (possibly
    slightly above), then crossing below Pro around position 32-64 and
    remaining below Pro through 32K; also flattens toward the right
- **Crossover:** The two lines are very close at positions 8-16, then Ultra
  drops below Pro around position 32-64; after that, Ultra stays consistently
  below Pro
- **Gridlines:** Faint light gray horizontal gridlines visible; no vertical
  gridlines
- **Axes:** Thin black lines on left (y-axis) and bottom (x-axis); chart area
  open on top and right
- **Background:** White
- **Figure caption (below chart):** "Figure 4 | Negative log likelihood as a
  function of token index across 32K context length on a held-out set of long
  documents."

### Verifiable Facts [-> Accuracy]

- FACT: The chart contains exactly 2 lines (Pro and Ultra)
- FACT: The y-axis label reads "NLL"
- FACT: The x-axis label reads "Sequence position"
- FACT: The x-axis is logarithmic, ranging from 8 to 32K
- FACT: The x-axis has 13 labeled ticks: 8, 16, 32, 64, 128, 256, 512, 1K,
  2K, 4K, 8K, 16K, 32K
- FACT: Pro is represented by a green line and Ultra by a blue line
- FACT: Both lines show a downward trend from left to right (NLL decreases
  with sequence position)
- FACT: Ultra is below Pro for most of the x-axis range (from approximately
  position 32-64 onward)
- FACT: The two lines are very close together at the leftmost positions (8-16)
- FACT: Both lines flatten (become less steep) toward the right end of the
  x-axis
- FACT: No numeric values are shown on the y-axis
- FACT: The figure caption identifies this as "Figure 4"

### Hallucination Risks [-> Accuracy]

- RISK: A model might invent specific NLL values (e.g., "NLL starts at 3.2
  and decreases to 1.1") since no y-axis numbers are visible
  REALITY: The y-axis has no readable numeric labels; only relative
  comparisons (higher/lower, above/below) can be made
- RISK: A model might claim there are more than 2 lines (e.g., Nano 1,
  Nano 2)
  REALITY: Only Pro (green) and Ultra (blue) are shown
- RISK: A model might state the x-axis is linear
  REALITY: The x-axis is clearly logarithmic (8, 16, 32, 64... doubling)
- RISK: A model might claim Ultra is always below Pro
  REALITY: At the leftmost positions (8-16), the lines are very close and
  may overlap or Ultra may start slightly above Pro
- RISK: A model might describe the x-axis range as "0 to 32K"
  REALITY: The x-axis starts at 8 (not 0)
- RISK: A model might add benchmark dataset names (e.g., "PG-19", "Books3")
  REALITY: No dataset names appear in the chart; only the caption mentions
  "held-out set of long documents"

### Detail Inventory [-> Specificity]

- Line chart: 2 data series (Pro, Ultra) over a logarithmic x-axis spanning
  4+ orders of magnitude (8 to 32K)
- Both curves are smooth and monotonically decreasing
- Ultra's steeper initial descent means it gains its advantage over Pro
  primarily in the low-to-mid sequence positions (32-512)
- At high sequence positions (4K-32K), both curves are nearly flat and the
  gap between them narrows
- The convergence at the right end suggests diminishing returns for longer
  context for both models
- Green line color for Pro, blue for Ultra -- consistent with V01's color
  scheme
- No data point markers on either line -- smooth curves only
- Y-axis tick marks present but unlabeled, making absolute NLL values
  unreadable
- Logarithmic x-axis ticks use "K" suffix for thousands (1K, 2K, 4K, 8K,
  16K, 32K)
- Chart area relatively compact; lines are clearly distinguishable by color

### Domain Context [-> Usefulness]

- **Domain:** Language modeling, long-context evaluation, perplexity measurement
- **Surrounding document context:** Figure 4 in the Gemini 1.0 technical
  report (page 11). The surrounding text explains that NLL decreases with
  sequence position up to the full 32K context length, and that longer context
  enables new use cases like retrieval and video understanding.
- **Technical terminology:**
  - NLL (negative log likelihood): a standard measure of language model
    quality; lower is better. Closely related to perplexity.
  - Sequence position / token index: the position of a token within the input
    sequence; NLL at later positions measures how well the model uses earlier
    context
  - 32K context length: the maximum input length supported by these Gemini
    models
  - Long documents: test data consisting of documents long enough to stress
    the full 32K context window
- **Why this image matters:** Demonstrates that Gemini models (especially Ultra)
  effectively use long context -- NLL keeps decreasing even at 16K-32K
  positions, indicating the model benefits from distant context rather than
  plateauing early. This is a key capability claim for the Gemini model family.

### Search Keywords [-> Usefulness]

- Gemini, negative log likelihood, NLL, perplexity
- long context, sequence position, token index, 32K
- Pro, Ultra, model comparison, language modeling
- context length scaling, long document, held-out evaluation
- line chart, logarithmic scale

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Calls the x-axis linear instead of logarithmic; invents specific NLL values; claims more than 2 lines; gets line colors wrong | Correctly identifies 2 lines (Pro, Ultra), logarithmic x-axis, downward NLL trend; notes Ultra is generally below Pro; may claim Ultra is always below | Both lines correctly identified with colors; logarithmic x-axis from 8 to 32K noted; correctly describes the initial convergence near position 8-16 and Ultra's advantage from ~32-64 onward; notes y-axis has no numeric labels |
| Specificity | "A line chart showing NLL" with no model names or axis details | Names Pro and Ultra, states logarithmic x-axis from 8 to 32K, notes downward trend and Ultra below Pro | Lists all 13 x-axis tick values, describes the curve shapes (steep initial descent, flattening at high positions), notes the crossover region, mentions absence of y-axis numeric values, describes line colors |
| Completeness | Describes only one line or omits the x-axis scale; misses the logarithmic nature | Covers both lines, x-axis range and logarithmic scale, y-axis label, legend, and general trend | Both lines described with trajectory, crossover region noted, all axis labels and ticks documented, legend described, gridlines mentioned, figure caption included, absence of y-axis numbers noted |
| Usefulness | "NLL chart" -- not searchable for model names or context length | Mentions Gemini Pro and Ultra, NLL, sequence position, 32K context; searchable for "Gemini long context" | Explains NLL as a model quality metric (lower is better), connects to long-context capability, explains the significance of continued decrease at high positions; searchable for NLL, perplexity, Gemini, long context, 32K |

<br><br>

## doc05-V03 -- Post-training data flywheel flow diagram

**Figure reference:** Figure 7, page 21
**Content type:** diagram
**Annotation difficulty:** Hard
**Dimensions:** vector

### Visual Inventory [-> Completeness]

- **Components/nodes (7 labeled):**
  1. "Gemini pre-training" -- 4-pointed star icon (teal/cyan), light blue
     rectangular box, OUTSIDE the dashed region (far left)
  2. "SFT" -- list/horizontal-lines icon (teal/cyan), light blue rectangular
     box, inside dashed region (top row)
  3. "RLHF" -- refresh/loop icon with two curved arrows (teal/cyan), light
     blue rectangular box, inside dashed region (top row, right of SFT)
  4. "End users" -- person/user icon (teal/cyan), light blue rectangular
     box, OUTSIDE the dashed region (far right)
  5. "Data flywheel" -- circular arrows icon (teal/cyan), in a teal/cyan
     circular border (not rectangular), center of diagram inside dashed
     region
  6. "Demonstration data" -- document icon (teal/cyan), light blue
     rectangular box, bottom-left inside dashed region
  7. "Feedback data" -- document icon (teal/cyan), light blue rectangular
     box, bottom-right inside dashed region
- **Connections (gray arrows):**
  - Gemini pre-training -> SFT (right arrow, enters dashed region)
  - SFT -> RLHF (right arrow)
  - RLHF -> End users (right arrow, exits dashed region)
  - End users -> Feedback data (arrow going back left/down, re-enters
    dashed region)
  - Feedback data -> Data flywheel (left arrow)
  - Demonstration data -> Data flywheel (right arrow)
  - Data flywheel -> SFT (up arrow, closes the loop)
- **Hierarchy or flow direction:** Left-to-right main pipeline (pre-training
  -> SFT -> RLHF -> End users), with a bottom feedback cycle (End users ->
  Feedback data -> Data flywheel -> SFT)
- **Visual grouping:** A light blue dashed rectangle encloses the post-
  training components (SFT, RLHF, Data flywheel, Demonstration data,
  Feedback data). Gemini pre-training and End users sit outside this region.
- **Style elements that carry meaning:**
  - Each node has a teal/cyan icon in a distinct shape
  - Data flywheel is circular (not rectangular) emphasizing its cyclical
    role
  - All icons share the same teal/cyan color scheme
  - Gray directional arrows for connections
  - Light blue rectangular boxes for most nodes
  - Dashed border groups the iterative post-training components
- **Figure caption (visible in crop):** "Figure 7 | **Modeling overview.**
  Post-training utilizes an optimized data flywheel in order to acquire
  human-AI feedback and continually improve on key areas..."
- **Note:** The crop also includes surrounding paragraph text about RLHF
  above the diagram. The diagram itself is the figure content.

### Verifiable Facts [-> Accuracy]

- FACT: The main pipeline flows left to right: "Gemini pre-training" ->
  "SFT" -> "RLHF" -> "End users"
- FACT: The diagram labels show only abbreviations "SFT" and "RLHF" (the
  full expansions are domain knowledge, not visible in the image)
- FACT: A "Data flywheel" component connects user feedback back into the
  training process
- FACT: "Feedback data" receives an arrow from "End users"
- FACT: Both "Demonstration data" and "Feedback data" feed into the "Data
  flywheel"
- FACT: The "Data flywheel" connects back to "SFT" (not to pre-training or
  RLHF)
- FACT: The diagram contains exactly 7 labeled components
- FACT: "Gemini pre-training" has a 4-pointed star icon
- FACT: "RLHF" has a refresh/loop icon (two curved arrows), not a document
  icon
- FACT: "Data flywheel" is in a circular teal border, distinct from the
  rectangular boxes used for the other 6 nodes
- FACT: "End users" has a person icon
- FACT: A dashed rectangle encloses the post-training components (SFT,
  RLHF, Data flywheel, Demonstration data, Feedback data)
- FACT: Gemini pre-training and End users are outside the dashed region

### Hallucination Risks [-> Accuracy]

- RISK: A model might claim the feedback loop goes back to "Gemini pre-training"
  REALITY: The data flywheel feeds back into SFT, not pre-training
- RISK: A model might invent additional training stages (e.g., "DPO" or "reward modeling") not shown
  REALITY: Only three training stages are shown: pre-training, SFT, and RLHF
- RISK: A model might state that Feedback data feeds directly into RLHF
  REALITY: Feedback data goes through the Data flywheel first, which then feeds into SFT
- RISK: A model might claim the diagram shows model deployment or serving infrastructure
  REALITY: The diagram shows only the training pipeline and data feedback cycle
- RISK: A model might state there is a direct connection from End users to SFT
  REALITY: The path from End users to SFT goes through Feedback data -> Data flywheel -> SFT
- RISK: A model might fabricate specific dataset names or training iteration counts
  REALITY: The diagram uses generic labels (Demonstration data, Feedback data) without specific dataset names

### Detail Inventory [-> Specificity]

- Main pipeline: 4 stages in left-to-right sequence (pre-training, SFT,
  RLHF, End users)
- Distinctive icons per node: 4-pointed star (pre-training), list/lines
  (SFT), refresh/loop arrows (RLHF), person (End users), circular arrows
  (Data flywheel), document (Demonstration data and Feedback data)
- All icons are teal/cyan; all boxes are light blue rectangles except Data
  flywheel which has a teal circular border
- Dashed blue rectangle groups the post-training components
- Feedback loop: End users -> Feedback data -> Data flywheel -> back to SFT
- Two data sources feed the flywheel: Demonstration data and Feedback data
- Gray directional arrows for all connections
- The cycle represents iterative improvement: user feedback improves
  training data, which improves the model via SFT
- Pre-training is the starting point and does not receive feedback loop
  input
- Figure caption: "Figure 7 | Modeling overview."
- The diagram is a vector graphic (rendered from page, not rasterized)

### Domain Context [-> Usefulness]

- **Domain:** Machine learning training pipelines, RLHF, model alignment
- **Surrounding document context:** Figure 7 in the Gemini report, appearing in
  the post-training methodology section. Illustrates how user feedback is
  collected and cycled back into training to continuously improve the model.
- **Technical terminology:**
  - Pre-training: initial training on large-scale data
  - SFT (Supervised Fine-Tuning): training on curated demonstration data
  - RLHF (Reinforcement Learning from Human Feedback): aligning model outputs
    with human preferences
  - Data flywheel: iterative process where model usage generates data that
    improves future model versions
  - Demonstration data: human-created examples of desired behavior
  - Feedback data: signals from end users about model quality
- **Why this image matters:** Shows the complete post-training improvement
  cycle for Gemini, establishing that model quality is not static but
  continuously improved through user feedback. The flywheel concept is central
  to understanding how deployed models get better over time.

### Search Keywords [-> Usefulness]

- Gemini, post-training, data flywheel
- SFT, supervised fine-tuning, RLHF
- reinforcement learning from human feedback
- feedback loop, model improvement, alignment
- demonstration data, feedback data, end users
- training pipeline, iterative improvement

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Misorders the pipeline stages or states the feedback loop connects to pre-training instead of SFT; invents stages not shown | Correctly identifies the 4 main stages and the feedback loop back to SFT; may miss one data source or get an arrow direction wrong | All stages, connections, and data sources match exactly; correctly notes that the flywheel feeds back into SFT (not pre-training), and both Demonstration data and Feedback data feed the flywheel |
| Specificity | "A training pipeline diagram" with no stage names | Names pre-training, SFT, RLHF, End users; mentions the feedback loop and data flywheel concept | Lists all 6 components with their icons, traces each connection with direction, distinguishes the two data sources, and explains the flywheel's role in closing the training loop |
| Completeness | Mentions only the main pipeline; omits the feedback loop or the data sources | Covers the main pipeline and the feedback loop; may omit one data source or the icon details | Accounts for all 6 labeled components, the Data flywheel box, all arrows with directions, the two data sources, the icon types, and the overall left-to-right plus cyclical structure |
| Usefulness | "A diagram about model training" -- no specific terms | Mentions SFT, RLHF, data flywheel, Gemini post-training; searchable for "Gemini training pipeline" | Explains the iterative improvement concept, names all stages and data types, relates the flywheel to continuous model improvement, and provides enough ML terminology to be useful for someone studying alignment pipelines |

<br><br>

## doc05-V04 -- Gemini tool-use control loop

**Figure reference:** Figure 8, page 23
**Content type:** diagram
**Annotation difficulty:** Medium
**Dimensions:** vector

### Visual Inventory [-> Completeness]

- **Components/nodes (4 process boxes + 1 decision diamond):**
  1. "Prompt" (starting node, left side)
  2. "Sample from LLM" (process box)
  3. "Sample contains tool code block?" (decision diamond)
  4. "Put execution result back in context" (process box, loop path)
  5. "Respond" (terminal node, right side)
- **Connections:**
  - Prompt -> Sample from LLM
  - Sample from LLM -> decision diamond "Sample contains tool code block?"
  - Decision diamond "NO" (red circle) -> Respond
  - Decision diamond "YES" (green circle) -> Put execution result back in
    context
  - Put execution result back in context -> Sample from LLM (loop back)
- **Hierarchy or flow direction:** Left-to-right main flow with a loop:
  Prompt -> Sample -> Decision -> (if NO) Respond; (if YES) Execute and loop
  back to Sample
- **Style elements that carry meaning:**
  - Green filled circle with white "YES" text for the YES branch
  - Red/coral filled circle with white "NO" text for the NO branch
  - Diamond shape (pink/light red border) for the decision point
  - Rounded-corner rectangular boxes for process steps, each with a
    distinct border color:
    - Purple/violet border: Prompt
    - Blue border: Sample from LLM, Put execution result back in context
    - Orange border: Respond
  - All boxes have no fill (white interior, border only)
  - Gray arrows with arrowheads for connections (Prompt -> Sample from LLM
    arrow appears dashed)
- **Figure caption (visible in crop):** "Figure 8 | A Gemini tool-use
  control loop."
- **Note:** The crop also includes the page header and body text about
  Gemini Apps models below the diagram. The diagram itself is the figure
  content.

### Verifiable Facts [-> Accuracy]

- FACT: The diagram starts with "Prompt" on the left
- FACT: The diagram ends with "Respond" on the right (for the NO path)
- FACT: The decision diamond asks "Sample contains tool code block?"
- FACT: The YES path leads to "Put execution result back in context"
- FACT: The NO path leads directly to "Respond"
- FACT: The YES path creates a loop back to "Sample from LLM"
- FACT: YES is indicated by a green filled circle with white text; NO by a
  red/coral filled circle with white text
- FACT: There are exactly 4 process boxes and 1 decision diamond
- FACT: Each process box has a distinct border color: purple (Prompt), blue
  (Sample from LLM and Put execution result), orange (Respond)
- FACT: The decision diamond has a pink/light red border
- FACT: All boxes have no fill -- white interior with colored borders only
- FACT: The diagram shows a simple control loop, not a multi-branch tree
- FACT: The figure caption reads "Figure 8 | A Gemini tool-use control
  loop."

### Hallucination Risks [-> Accuracy]

- RISK: A model might claim there are multiple decision points or nested conditionals
  REALITY: There is exactly one decision diamond in the entire diagram
- RISK: A model might invent additional boxes like "Parse response" or "Format output"
  REALITY: Only 4 process boxes are shown: Prompt, Sample from LLM, Put execution result back in context, and Respond
- RISK: A model might state the loop has a maximum iteration limit shown in the diagram
  REALITY: No iteration limit is shown; the loop continues until the sample contains no tool code block
- RISK: A model might describe error handling or fallback paths
  REALITY: No error paths are shown; the diagram has only two branches (YES loop, NO respond)
- RISK: A model might claim the "Respond" node feeds back into "Prompt"
  REALITY: "Respond" is a terminal node with no outgoing connections

### Detail Inventory [-> Specificity]

- 5 total nodes: Prompt, Sample from LLM, decision diamond, Put execution
  result back in context, Respond
- Single decision point: "Sample contains tool code block?"
- Two branches: YES (green filled circle, loops) and NO (red filled circle,
  terminates)
- The loop path: YES -> Put execution result back in context -> Sample from
  LLM -> Decision again
- The termination path: NO -> Respond
- Distinct border colors per node: purple (Prompt), blue (Sample from LLM,
  Put execution result), pink/light red (decision diamond), orange (Respond)
- All boxes unfilled (white interior, border only)
- Gray arrows with arrowheads; Prompt -> Sample arrow appears dashed
- Clean, minimal flowchart with no parallel paths or error handling
- Vector graphic rendering
- Color coding: green = continue/yes, red = stop/no
- Figure caption: "Figure 8 | A Gemini tool-use control loop."

### Domain Context [-> Usefulness]

- **Domain:** LLM tool use, function calling, agent architectures
- **Surrounding document context:** Figure 8 in the Gemini report, appearing in
  the section on tool use. Illustrates how Gemini handles tool/function calls:
  the model generates a sample, and if it contains a tool invocation, the tool
  is executed and the result is fed back for another round of generation.
- **Technical terminology:**
  - Tool use / function calling: LLM capability to invoke external functions
  - Code block: structured output that represents a tool call
  - Context: the input/output history fed to the LLM for each generation step
  - Sampling: generating a response from the LLM
- **Why this image matters:** Defines the fundamental control loop for Gemini's
  tool-use capability. This pattern (generate, check for tool call, execute,
  loop) is the standard architecture for LLM agents and establishes how Gemini
  integrates external tools.

### Search Keywords [-> Usefulness]

- Gemini, tool use, function calling, control loop
- LLM agent, tool code block, execution
- sample from LLM, context window, iterative
- flowchart, decision diamond, agent loop
- code execution, tool integration

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Invents additional decision points or process boxes; describes the NO path as looping | Correctly identifies the single decision point, the YES loop, and the NO termination; may misstate a box label | All 5 nodes correctly named, YES/NO paths accurate with correct color coding (green/red), and the loop structure precisely described |
| Specificity | "A flowchart about tool use" with no node names | Names the key nodes (Prompt, Sample from LLM, Respond), describes the YES/NO branching | Lists all 5 nodes with exact labels, describes both paths with color indicators, specifies the loop-back target (Sample from LLM), and notes there is exactly one decision point |
| Completeness | Describes only the linear path (Prompt -> Sample -> Respond); omits the loop | Covers the main path, the decision point, and the loop; may omit the color coding or the "Put execution result back in context" label | Accounts for all 5 nodes, both paths (YES loop and NO terminate), the color coding (green YES, red NO), the diamond shape for the decision, and the loop closure |
| Usefulness | "A flowchart" -- no tool-use context, no node names | Mentions Gemini tool use, the check for tool code blocks, the loop pattern; searchable for "Gemini tool calling" | Explains the tool-use control loop pattern, names all nodes, connects to LLM agent architecture concepts, and provides enough context to understand the iterative generation-execution cycle |

<br><br>

## doc05-V05 -- CoT with uncertainty routing bar chart (MMLU)

**Figure reference:** Figure 9, page 74
**Content type:** chart-simple
**Annotation difficulty:** Medium
**Dimensions:** vector (rendered from PDF page at 2x scale)

### Visual Inventory [-> Completeness]

- **Chart type:** Grouped bar chart with 2 bars per group, 3 groups
- **Y-axis:** Labeled "MMLU accuracy (test split)" (rotated vertically); scale
  from 0 to 90, ticks at 10-unit intervals
- **X-axis categories (3 groups):**
  1. Score Eval
  2. Chain-of-Thought@32
  3. Chain-of-Thought@32 (Uncertainty-Routed)
- **Legend (top center, above chart area):** GPT-4 (gpt-4-0613) in gray,
  Gemini Ultra in blue
- **Bars with exact value labels above each bar:**
  - Score Eval: GPT-4 = 84.21, Gemini Ultra = 83.96
  - Chain-of-Thought@32: GPT-4 = 87.29, Gemini Ultra = 84.99
  - Chain-of-Thought@32 (Uncertainty-Routed): GPT-4 = 87.29,
    Gemini Ultra = 90.04
- **Bar colors:** Light gray for GPT-4, medium blue for Gemini Ultra
- **Gridlines:** Thin horizontal gray gridlines at each 10-unit y-axis tick
- **Background:** White
- **Bar style:** Solid fill, no outlines
- **Y-axis starts at 0** but all bar values are in the 83-90 range, so the
  bottom ~80% of the chart area is empty
- **Figure caption (below chart):** "Figure 9 | Chain-of-Thought with
  uncertainty routing on MMLU."

### Verifiable Facts [-> Accuracy]

- FACT: There are exactly 3 evaluation conditions on the x-axis
- FACT: There are exactly 2 bars per group (GPT-4 and Gemini Ultra)
- FACT: The y-axis label reads "MMLU accuracy (test split)"
- FACT: Score Eval GPT-4 = 84.21
- FACT: Score Eval Gemini Ultra = 83.96
- FACT: Chain-of-Thought@32 GPT-4 = 87.29
- FACT: Chain-of-Thought@32 Gemini Ultra = 84.99
- FACT: Chain-of-Thought@32 (Uncertainty-Routed) GPT-4 = 87.29
- FACT: Chain-of-Thought@32 (Uncertainty-Routed) Gemini Ultra = 90.04
- FACT: GPT-4 scores are identical for Chain-of-Thought@32 and
  Chain-of-Thought@32 (Uncertainty-Routed): both 87.29
- FACT: Gemini Ultra exceeds GPT-4 only in the uncertainty-routed condition
- FACT: The legend identifies GPT-4 as "GPT-4 (gpt-4-0613)"
- FACT: GPT-4 leads Gemini Ultra in Score Eval by 0.25 points (84.21 vs
  83.96)
- FACT: GPT-4 leads Gemini Ultra in Chain-of-Thought@32 by 2.30 points
  (87.29 vs 84.99)
- FACT: Gemini Ultra leads GPT-4 in Uncertainty-Routed by 2.75 points
  (90.04 vs 87.29)

### Hallucination Risks [-> Accuracy]

- RISK: A model might round or misquote the exact bar values (e.g., "84.2"
  instead of "84.21" or "90.0" instead of "90.04")
  REALITY: All 6 values are printed explicitly above the bars with 2 decimal
  places
- RISK: A model might claim Gemini Ultra beats GPT-4 across all conditions
  REALITY: Gemini Ultra only leads in the uncertainty-routed condition; GPT-4
  leads in the other two
- RISK: A model might state the GPT-4 model version as "gpt-4-turbo" or
  "gpt-4-1106"
  REALITY: The legend explicitly says "gpt-4-0613"
- RISK: A model might claim the y-axis starts at 80 (truncated) to emphasize
  differences
  REALITY: The y-axis starts at 0, making the visual differences between bars
  appear small relative to the total bar height
- RISK: A model might describe additional models (e.g., "GPT-3.5", "Gemini
  Pro") as being in the chart
  REALITY: Only GPT-4 and Gemini Ultra are shown
- RISK: A model might confuse "Chain-of-Thought@32" with
  "Chain-of-Thought@32 (Uncertainty-Routed)" since the GPT-4 scores are
  identical (87.29) in both conditions
  REALITY: These are two distinct conditions; GPT-4's identical scores
  reflect that uncertainty routing only changes Gemini Ultra's behavior

### Detail Inventory [-> Specificity]

- Grouped bar chart: 2 models x 3 conditions = 6 total bars
- All 6 bars have explicit numeric value labels above them (2 decimal places)
- Score Eval is the simplest condition: GPT-4 slightly leads (84.21 vs 83.96,
  a 0.25-point gap)
- Chain-of-Thought@32 widens GPT-4's lead (87.29 vs 84.99, a 2.30-point gap)
- Uncertainty-Routed reverses the ranking: Gemini Ultra jumps to 90.04 while
  GPT-4 stays at 87.29 (Gemini leads by 2.75 points)
- GPT-4's score is identical at 87.29 for both Chain-of-Thought@32 conditions,
  indicating uncertainty routing is a Gemini-specific technique
- Gemini Ultra's improvement from Chain-of-Thought@32 to Uncertainty-Routed:
  +5.05 points (84.99 to 90.04)
- The y-axis goes from 0 to 90 with the bars clustered in the 83-90 range --
  the full-scale y-axis makes visual comparison harder since differences are
  small relative to bar heights
- Light gray gridlines at every 10 units
- GPT-4 bars are consistently on the left, Gemini Ultra on the right within
  each group
- X-axis labels for the third category wrap to two lines:
  "Chain-of-Thought@32" on line 1, "(Uncertainty-Routed)" on line 2

### Domain Context [-> Usefulness]

- **Domain:** AI/ML benchmarking, chain-of-thought prompting, uncertainty
  estimation, MMLU evaluation
- **Surrounding document context:** Figure 9 in the Gemini 1.0 technical
  report (page 74). The surrounding text explains the uncertainty-routed
  chain-of-thought approach: when the model is uncertain about an answer
  (based on chain-of-thought samples), it falls back to a different strategy
  rather than committing to a possibly wrong answer.
- **Technical terminology:**
  - MMLU: Massive Multitask Language Understanding -- a benchmark covering 57
    academic subjects
  - Score Eval: direct scoring of model responses
  - Chain-of-Thought@32: generating 32 chain-of-thought reasoning samples and
    selecting the most common answer (majority voting)
  - Uncertainty-Routed: a technique where uncertain answers (based on
    agreement among the 32 samples) are routed to a different evaluation
    strategy
  - gpt-4-0613: the June 2023 version of GPT-4
- **Why this image matters:** This is the chart that supports the headline claim
  "Gemini Ultra exceeds GPT-4 on MMLU" -- but only with the
  uncertainty-routed technique. The chart makes visible that without
  uncertainty routing, GPT-4 actually leads. This nuance is critical for
  accurate annotation.

### Search Keywords [-> Usefulness]

- Gemini Ultra, GPT-4, MMLU, benchmark comparison
- chain-of-thought, uncertainty routing, majority voting
- score eval, CoT@32, uncertainty-routed
- language understanding, test split accuracy
- bar chart, model comparison, 90.04, 87.29

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | Wrong numeric values; claims Gemini Ultra beats GPT-4 in all conditions; wrong model version | Correct bar values for all 6 bars; correctly identifies that Gemini Ultra only leads in uncertainty-routed; names GPT-4 (gpt-4-0613) | All 6 values exact to 2 decimal places; notes GPT-4 scores are identical in both CoT conditions (87.29); correctly calculates point differences between models |
| Specificity | "A bar chart comparing two AI models on a benchmark" | Names both models, all 3 conditions, and the key result (Gemini Ultra 90.04); mentions MMLU | All 6 exact values, all 3 condition names quoted exactly, model version noted, point gaps calculated, notes the full-scale y-axis starting at 0, describes the two-line wrapping of the third x-axis label |
| Completeness | Describes only 1-2 of the 3 conditions; omits one model's values | Covers all 3 conditions and both models' scores; mentions the legend and y-axis label | All 6 bars with values, legend with exact GPT-4 version string, y-axis label and range, x-axis label formatting, gridlines, caption, and the reversal pattern across conditions |
| Usefulness | "MMLU comparison chart" -- no numeric values, no technique names | Names the models, MMLU, and uncertainty routing; searchable for "Gemini MMLU" | Explains what each condition means (scoring, CoT majority voting, uncertainty routing), notes the reversal that Gemini only leads with uncertainty routing, and connects to the headline MMLU claim; searchable for specific techniques and scores |

<br><br>

## doc05-V06 -- Multimodal chart understanding + response

**Figure reference:** Figure 10, page 77
**Content type:** infographic
**Annotation difficulty:** Hard
**Dimensions:** vector (rendered from PDF page at 2x scale)

### Visual Inventory [-> Completeness]

- **Layout:** Two-panel composite figure with distinct sections separated by
  dark gray header bars with white text
- **Panel 1 -- "Prompt" (dark gray header bar, white text):**
  - Chart title: "Share of plastic waste that is recycled, landfilled,
    incinerated and mismanaged, 2019"
  - "Our World in Data" boxed logo/badge in the top-right corner of the chart
  - Subtitle/note: "Mismanaged plastic waste includes materials burned in open
    pits, dumped into seas or open waters, or disposed of in unsanitary
    landfills and dumpsites."
  - 4 regional panels of horizontal bar charts in a 2x2 grid:
    - **World:** Landfilled 49%, Mismanaged 22%, Incinerated 19%, Recycled 9%
    - **United States:** Landfilled 73%, Mismanaged 4%, Incinerated 19%,
      Recycled 4%
    - **Europe:** Landfilled 44%, Mismanaged 6%, Incinerated 38%, Recycled 12%
    - **Asia (excl. China and India):** Landfilled 39%, Mismanaged 34%,
      Incinerated 19%, Recycled 8%
  - Bar colors: dark red (Landfilled), teal/green (Mismanaged), blue
    (Incinerated), orange (Recycled) -- consistent across all 4 panels
  - Data source line: "Data source: OECD (2023)" (left) and
    "OurWorldInData.org/plastic-pollution | CC BY" (right)
  - OECD region definition footnotes in small text at bottom of prompt section
  - Prompt instruction text: "Spot a data point that stands out in these
    charts and what that implicates. Then produce a detailed markdown table
    for all the data shown."
- **Panel 2 -- "Model Response (rendered Markdown)" (dark gray header bar,
  white text):**
  - Text response: identifies United States' landfilled plastic waste at 73%
    as the standout data point; explains the implication (US not recycling or
    incinerating as much as other regions)
  - Rendered markdown table with 5 columns: Country/Region, Landfilled (%),
    Mismanaged (%), Incinerated (%), Recycled (%)
  - 4 data rows: World, United States, Europe, Asia (excl. China and India)
  - Table values match the chart data
- **Figure caption (below both panels):** "Figure 10 | Solving a problem
  requiring multimodal chart understanding. The model has to read the text,
  understand the connections between different data points and reason over them
  to recommend an interesting point and follow the instructions to generate a
  markdown table (shown correctly rendered)."
- **Source line:** "Source: Our World In Data (Ritchie et al., 2023)."

### Verifiable Facts [-> Accuracy]

- FACT: The chart title is "Share of plastic waste that is recycled, landfilled, incinerated and mismanaged, 2019"
- FACT: Data is attributed to "Our World in Data" and sourced from "OECD (2023)"
- FACT: There are exactly 4 regional panels: World, United States, Europe, and Asia excl. China and India
- FACT: Each panel shows 4 categories: Landfilled, Mismanaged, Incinerated, Recycled
- FACT: World Landfilled is 49%
- FACT: United States Landfilled is 73%
- FACT: Europe Incinerated is 38%
- FACT: Asia excl. China and India Landfilled is 39%
- FACT: Asia excl. China and India Mismanaged is 34%
- FACT: World Recycled is 9%
- FACT: United States Recycled is 4%
- FACT: Europe Recycled is 12%
- FACT: The model identifies US landfilled at 73% as the standout data point
- FACT: The model produces a markdown table with 4 data rows and 5 columns
- FACT: The data year is 2019
- FACT: The prompt asks to "spot a data point that stands out" and produce a "detailed markdown table"

### Hallucination Risks [-> Accuracy]

- RISK: A model might add regions not shown (e.g., "Africa" or "South America")
  REALITY: Only 4 regions are shown: World, United States, Europe, and Asia excl. China and India
- RISK: A model might report percentage values that do not add up to 100% for each region
  REALITY: The 4 categories for each region should sum to approximately 100% (some rounding variation possible)
- RISK: A model might state the data is from a different year (e.g., 2020 or 2018)
  REALITY: The chart explicitly states 2019
- RISK: A model might claim Asia includes China and India
  REALITY: The label explicitly says "Asia excl. China and India"
- RISK: A model might fabricate a fifth waste category not shown in the chart
  REALITY: Only 4 categories: Landfilled, Mismanaged, Incinerated, Recycled
- RISK: A model might state Europe has the highest recycling rate when it shows 12%
  REALITY: Europe does have the highest recycling rate among the 4 regions (12%), but a model should not overstate this without noting it is still relatively low

### Detail Inventory [-> Specificity]

- Two-panel composite: Prompt section (chart + instruction) and Model Response
  section (text analysis + rendered table)
- Dark gray header bars with white text label each section
- Chart title with year (2019) and subject (plastic waste management)
- "Our World in Data" boxed logo/badge in top-right of chart
- Source attribution on two lines: "Data source: OECD (2023)" and
  "OurWorldInData.org/plastic-pollution | CC BY"
- 4 regional panels in 2x2 grid with 4 categories each (16 total data points)
- Specific percentages for all 16 data points:
  - World: 49%, 22%, 19%, 9%
  - United States: 73%, 4%, 19%, 4%
  - Europe: 44%, 6%, 38%, 12%
  - Asia (excl. China and India): 39%, 34%, 19%, 8%
- Horizontal bar chart format with consistent color coding: dark red
  (Landfilled), teal/green (Mismanaged), blue (Incinerated), orange (Recycled)
- Percentage values printed to the right of each bar
- OECD region definition footnotes in small text at bottom of prompt section
- Prompt asks two things: identify a standout data point and produce a table
- Model response identifies US 73% landfilled as the standout and explains the
  implication (US not recycling/incinerating as much as other regions)
- Model produces a correctly rendered markdown table reproducing all the data
- Table columns: Country/Region, Landfilled (%), Mismanaged (%), Incinerated
  (%), Recycled (%)
- Figure caption below both panels references "Figure 10" and describes the
  task as multimodal chart understanding
- Additional source line: "Source: Our World In Data (Ritchie et al., 2023)."

### Domain Context [-> Usefulness]

- **Domain:** Environmental science, waste management, data visualization
- **Surrounding document context:** Figure 10 in the Gemini report,
  demonstrating multimodal chart understanding. The model must read data from
  horizontal bar charts, identify a notable pattern, provide analysis, and
  reproduce the data in structured table format.
- **Technical terminology:**
  - Landfilled: waste disposed in landfills
  - Mismanaged: waste not properly collected or disposed (including littering,
    open dumping)
  - Incinerated: waste burned, potentially with energy recovery
  - Recycled: waste processed for reuse
  - Our World in Data: research and data publication initiative
  - OECD: Organisation for Economic Co-operation and Development
- **Why this image matters:** Demonstrates advanced chart comprehension: the
  model must read 16 data points from bar charts, perform comparative analysis
  (identifying the standout), and output structured data (Markdown table). This
  combines visual data extraction, analytical reasoning, and structured output
  generation.

### Search Keywords [-> Usefulness]

- Gemini, chart understanding, data extraction
- plastic waste, recycling, landfill, incineration, mismanaged
- Our World in Data, OECD, 2019
- horizontal bar chart, regional comparison
- United States, Europe, Asia, waste management
- markdown table, data visualization, structured output
- environmental data, multimodal comprehension

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | States wrong percentages for multiple regions; adds regions not shown; misattributes the data source or year | Correctly identifies all 4 regions and most percentage values; may misstate 1-2 values or omit the data source | All 16 data points match the chart exactly; correctly states the 2019 year, OECD source, and Our World in Data attribution; identifies the US 73% standout accurately |
| Specificity | "A chart about waste management" with no percentages, no regions, no year | Names the 4 regions, lists several percentages, mentions the 4 waste categories, and the 2019 year | Lists all 16 data points with exact percentages, names the chart title verbatim, cites the data source, describes the horizontal bar format, and notes the model's standout identification and table output |
| Completeness | Describes only the charts or only the model response; omits regions or categories | Covers all 4 regions, the 4 categories, the prompt instruction, and the model's table output; may omit some percentages or the data source | Accounts for all 4 regional panels with all 16 values, the chart title and source attribution, the prompt text (standout + table), and the model response (standout analysis + rendered markdown table with all columns) |
| Usefulness | "A chart about pollution" -- wrong topic framing, no specific data | Mentions plastic waste management, regional comparison, 2019 data; searchable for "plastic waste chart" or "Gemini data extraction" | Includes all regional data, the OECD source, the standout analysis (US landfill dominance), the structured table output, and explains the chart-to-table extraction task within the Gemini multimodal capabilities context |

# Image Analysis: Doc 24 -- 24_fowler_microservices.html

**Document:** `24_fowler_microservices.html`
**Format:** HTML
**Source:** https://martinfowler.com/articles/microservices.html
**Category:** multi-image
**Images:** 6
**Document context:** Martin Fowler's microservices architecture article
with 6 diagrams covering monolith vs microservices comparison, Conway's Law
organization mapping, decentralized data management, and deployment
pipeline patterns.

**Eval subset:** 3 of 6 content images

<br><br>

## doc24-R01 -- Monolith vs microservices architecture comparison

**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory [-> Information Recovery]

- **Diagram type:** Side-by-side conceptual comparison with two rows (concept
  and scaling), monolith on the left and microservices on the right
- **Layout:** 2x2 grid structure. Top row: single-instance concept. Bottom
  row: scaling pattern.

**Top-left (monolith concept):**
- Italic text: "A monolithic application puts all its functionality into a
  single process..."
- A single 3D server box (peach/tan frame with perspective shadow) containing
  one application square with 5 distinct colored shapes inside:
  - Orange amoeba/blob (top-right area)
  - Pink/magenta amoeba (top-center)
  - Cyan/teal angular shape (middle-left)
  - Dark maroon/burgundy circle (bottom-left)
  - Green pentagon-like shape (bottom-right)

**Top-right (microservices concept):**
- Italic text: "A microservices architecture puts each element of
  functionality into a separate service..."
- 4 individual small boxes (no 3D server frame), each containing one colored
  shape:
  - Orange blob (top-left box)
  - Green shape (top-right box)
  - Pink/magenta blob (bottom-left box)
  - Dark maroon circle (bottom-right box, partially visible)

**Bottom-left (monolith scaling):**
- Italic text: "... and scales by replicating the monolith on multiple
  servers"
- 4 identical 3D server boxes in a 2x2 grid, each containing the same 5
  colored shapes as the top-left monolith. All 4 are exact copies
  (horizontal scaling by full replication)

**Bottom-right (microservices scaling):**
- Italic text: "... and scales by distributing these services across
  servers, replicating as needed."
- Multiple small boxes arranged across what appears to be 4 server frames
  in a 2x2 grid. Each server contains a different subset of the colored
  shapes, with some shapes appearing in multiple servers (selective
  replication based on load)

- **Color palette for shapes:** Orange, pink/magenta, cyan/teal, dark
  maroon, green -- consistent across all panels
- **Background:** White
- **Style:** Clean hand-drawn/sketch aesthetic with 3D perspective on server
  boxes

### Verifiable Facts [-> Correctness]

- FACT: The diagram has 4 panels arranged in a 2x2 layout
- FACT: The left column shows monolith architecture; the right shows
  microservices
- FACT: The top row shows single-instance; the bottom row shows scaling
- FACT: The monolith contains 5 colored shapes inside one process box
- FACT: The microservices version separates these into individual boxes
  (one shape per box)
- FACT: Monolith scaling (bottom-left) shows 4 identical complete copies
- FACT: Microservices scaling (bottom-right) shows selective/distributed
  replication
- FACT: All 4 text labels are in italic font
- FACT: Server boxes have 3D perspective with peach/tan shading
- FACT: The 5 shape colors are consistent across all panels

### Hallucination Risks [-> Correctness]

- RISK: Counting exactly 5 microservice boxes on the right
  REALITY: The top-right shows 4 visible separate boxes (one shape may be
  missing or obscured). The exact count of shapes in the microservices
  panels should be verified carefully
- RISK: Describing specific service names (e.g., "user service", "order
  service")
  REALITY: The shapes have no labels. They are abstract colored blobs
  representing generic "elements of functionality"
- RISK: Describing the scaling pattern as "3 servers" or specific counts
  REALITY: The bottom-left shows 4 server copies. The bottom-right shows
  what appears to be 4 servers with distributed service placement
- RISK: Interpreting the shapes as specific architectural components
  REALITY: The shapes are intentionally abstract and unnamed

### Detail Inventory [-> Information Recovery]

- 4 text labels in italic, black font
- Monolith server box: 3D perspective, peach/tan (#F5DEB3 approximate)
  frame, white inner application area
- Microservice boxes: simple squares with thin border, no 3D effect (top
  row) vs. distributed in server frames (bottom row)
- Shape colors: orange (#FF8C00 approximate), pink/magenta (#CC66CC
  approximate), cyan/teal (#00CED1 approximate), dark maroon (#8B0000
  approximate), green (#228B22 approximate)
- Shapes are organic/amoeba-like blobs (not geometric), suggesting the
  informal sketch style common in Fowler's articles
- Bottom-left: 4 servers in 2x2, each with identical 5-shape content
- Bottom-right: 4 servers in 2x2 with different shape subsets per server
- White background, no borders, no arrows between panels

### Domain Context [-> Retrieval Value]

This is the opening diagram from Martin Fowler and James Lewis's landmark
2014 article "Microservices" on martinfowler.com. It introduces the core
architectural distinction:

- Monolith: all functionality in one process, scaled by replicating the
  entire application across multiple servers (horizontal scaling). Every
  server copy includes all components regardless of which ones are under
  load.

- Microservices: each element of functionality is a separate deployable
  service. Scaling is selective -- only the services under load need to be
  replicated, while others can remain as single instances. This enables
  more efficient resource utilization.

The abstract colored shapes deliberately avoid naming specific services,
focusing on the structural pattern rather than implementation details.
This diagram has become one of the most widely referenced illustrations
in software architecture discussions.

### Search Keywords [-> Retrieval Value]

monolith vs microservices, architecture comparison, scaling pattern,
horizontal scaling, selective replication, Martin Fowler, James Lewis,
microservices architecture, deployment pattern, service decomposition,
distributed systems

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A diagram comparing two software architectures" -- no monolith/microservices labels, no scaling description, no shape details. Or: describes the microservices scaling panel as "identical copies" (it shows selective distribution with different shape subsets per server, unlike the monolith's 4 identical copies). Miscounting the 5 colored shapes or inventing specific service names (e.g., "user service", "order service") triggers the hallucination cap -- the shapes are abstract with no labels. | Monolith vs microservices comparison identified. Monolith: 5 shapes in one box, scales by 4 identical copies. Microservices: shapes in separate boxes, scales by distributing selectively. Italic text labels. 3D server frames for monolith scaling. May miss the 2x2 layout structure or the exact shape color enumeration. | 2x2 layout. Top-left: monolith (5 colored shapes in one 3D peach server). Top-right: microservices (4 separate flat boxes, one shape each). Bottom-left: monolith scales by 4 identical copies in 2x2 grid. Bottom-right: microservices scales by distributing shape subsets across 4 servers with selective replication. 4 italic text labels quoted. 5 organic shapes (orange, pink, cyan, maroon, green). No fabricated service names or extra labels. |
| Information Recovery | Identifies as an architecture diagram with colored shapes in boxes. A search for "monolith vs microservices" or "selective scaling" or "service replication" would not match. The 2x2 structure, scaling comparison, and italic text labels are invisible. | Both architectures named, scaling approaches distinguished (full replication vs selective distribution), 5 shapes noted, 3D server frames described, italic labels mentioned. "Monolith microservices comparison" would match. May miss the exact color enumeration, the flat-box vs 3D-frame distinction, or the specific text of all 4 labels. | Complete recovery: 2x2 layout with all 4 italic text labels quoted verbatim. 5 organic amoeba-like shapes in orange/pink/cyan/maroon/green. Monolith panels (3D peach server frames with perspective). Microservices panels (flat boxes top, 3D server frames bottom with distributed subsets). Shape distribution differences between monolith (identical) and microservices (selective) scaling. No arrows between panels. Sketch aesthetic. White background. Any structural element visible in the diagram is findable -- parity principle met. |
| Retrieval Value | "A software architecture diagram" -- no article source, not self-contained. Would not surface for "Fowler microservices" or "monolith scaling comparison" or "service decomposition diagram." | "Core monolith vs microservices comparison from Fowler's article showing full replication vs selective distribution." Searchable but doesn't explain why the scaling difference matters. | Natural prose identifying this as the opening diagram from Fowler/Lewis 2014 "Microservices" article. Explains structural decomposition (one process vs many) and scaling efficiency: monoliths must replicate everything (wasteful for components that don't need scaling), microservices replicate selectively (only the bottleneck service). Abstract shapes deliberately avoid naming specific services. One of the most widely referenced architecture comparison diagrams in the microservices literature. Domain vocabulary embedded (monolith, microservices, service decomposition, selective scaling, horizontal scaling). Self-contained. Findable by "monolith vs microservices scaling diagram" or "Fowler service decomposition comparison." |

<br><br>

## doc24-R02 -- Conway's Law: org structure mapped to system architecture

**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory [-> Information Recovery]

- **Diagram type:** Two-panel conceptual diagram showing the mapping between
  organizational structure (left) and system architecture (right), separated
  by a dashed vertical line

**Left panel -- Organization ("Siloed functional teams..."):**
- 3 groups of stick-figure icons, each labeled with a team name:
  1. "UI specialists" (top-left): cluster of ~5 blue stick figures
  2. "middleware specialists" (center-left): cluster of ~5 green/olive stick
     figures
  3. "DBAs" (bottom-left): cluster of ~5 teal/dark green stick figures
- Label at bottom: "Siloed functional teams..." in italic text

**Right panel -- Architecture:**
- 3-tier vertical stack connected by vertical arrows:
  1. Top: blue document/page icon (representing the UI/presentation layer)
  2. Middle: 3D server box (peach/tan frame, same style as R01) containing
     3 small colored shapes (gray, red/pink heart, green X) representing
     the middleware/application layer
  3. Bottom: database cylinder icon (gray/silver) representing the data
     layer
- Vertical arrows connect the 3 tiers (UI to middleware, middleware to
  database)
- Label at bottom: "... lead to siloed application architectures.
  Because Conway's Law" in italic text

**Connecting element:** Vertical dashed line running between the left and
right panels, implying the causal mapping from org structure to system
architecture

- **Background:** White
- **Style:** Same hand-drawn/sketch aesthetic as R01
- **No arrows** cross from the left panel to the right panel (the mapping
  is implied by vertical alignment: UI specialists align with UI tier,
  middleware specialists with server tier, DBAs with database tier)

### Verifiable Facts [-> Correctness]

- FACT: The diagram has two panels separated by a vertical dashed line
- FACT: The left panel shows 3 labeled groups of stick figures: "UI
  specialists", "middleware specialists", "DBAs"
- FACT: Stick figure colors are: blue (UI), green/olive (middleware),
  teal/dark green (DBAs)
- FACT: The right panel shows a 3-tier architecture: document icon, server
  box, database cylinder
- FACT: The server box in the middle tier contains 3 small colored shapes
- FACT: Vertical arrows connect the 3 architecture tiers
- FACT: The bottom-left label reads "Siloed functional teams..."
- FACT: The bottom-right label reads "... lead to siloed application
  architectures. Because Conway's Law"
- FACT: Both labels are in italic text
- FACT: The 3 organization groups vertically align with the 3 architecture
  tiers (UI team with UI layer, middleware team with server, DBAs with
  database)

### Hallucination Risks [-> Correctness]

- RISK: Describing explicit arrows or lines connecting teams to tiers
  REALITY: No arrows cross the dashed line from left to right. The mapping
  is implied by vertical alignment and the Conway's Law label, not shown
  with explicit connections
- RISK: Counting exact numbers of stick figures per team
  REALITY: Each team appears to have approximately 5 figures, but the
  overlapping sketch-style icons make exact counts uncertain
- RISK: Naming the 3 small shapes in the server box specifically
  REALITY: The shapes are small and abstract (a gray blob, a red/pink
  shape, and a green shape). They appear decorative/illustrative rather
  than meaningful
- RISK: Stating this is a "bad" pattern
  REALITY: The diagram shows the pattern without explicit judgment. The
  negative implication comes from context (Fowler's article argues for
  cross-functional teams instead)

### Detail Inventory [-> Information Recovery]

- Left panel: 3 clusters of ~5 stick figures each, vertically spaced
- Stick figure colors: blue (#4169E1 approximate), green/olive (#6B8E23
  approximate), teal (#2F4F4F approximate)
- Team labels: bold black text, left-aligned
- Right panel: 3-tier stack with vertical arrows
- UI tier: blue document icon with lines suggesting text content
- Server tier: 3D peach/tan box (same style as R01 monolith) with 3 small
  colored shapes inside separate compartments
- Database tier: gray cylinder icon
- Dashed vertical line: gray, runs full height of diagram
- Bottom labels: italic text, "Siloed functional teams..." and
  "... lead to siloed application architectures. Because Conway's Law"
- White background, no grid, no border

### Domain Context [-> Retrieval Value]

This diagram illustrates Conway's Law: "organizations which design systems
are constrained to produce designs which are copies of the communication
structures of these organizations" (Melvin Conway, 1967).

In this example, siloed functional teams (UI, middleware, DBA) naturally
produce a siloed 3-tier architecture (presentation, application, data).
Each team "owns" one tier, and system boundaries align with team
boundaries.

Fowler uses this diagram to argue that the microservices approach requires
a different organizational model: cross-functional teams organized around
business capabilities rather than technical specializations. If you want
microservices, you need "product teams" that own full vertical slices
rather than horizontal layers.

This is a foundational concept in the microservices movement and connects
to the "Inverse Conway Maneuver" -- deliberately restructuring teams to
produce the desired system architecture.

### Search Keywords [-> Retrieval Value]

Conway's Law, organizational structure, system architecture, siloed teams,
three-tier architecture, functional teams, UI specialists, middleware, DBA,
cross-functional teams, Martin Fowler, microservices organization, team
topology, Inverse Conway Maneuver

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A diagram showing teams and architecture layers" -- no Conway's Law reference, no mapping explanation, no team names. Or: describes explicit arrows connecting teams to architecture tiers (the mapping is implied by vertical alignment, not shown with arrows). Inventing team sizes (e.g., "the UI team has 7 people") when the stick figure count is approximate (~5 each) is a precision error. Fabricating additional teams or architecture tiers not shown triggers the hallucination cap. | Conway's Law diagram identified: 3 siloed teams (UI specialists, middleware specialists, DBAs) map to 3-tier architecture (document/UI, server, database). Dashed separator between org and architecture. Bottom labels reference Conway's Law. May miss the color coding or the 3D server box detail. | Two-panel diagram with dashed vertical separator. Left: 3 color-coded teams (blue UI ~5 figures, green middleware ~5, teal DBAs ~5) with bold labels. Right: 3-tier stack (blue document icon, peach 3D server box with 3 colored shapes in compartments, gray database cylinder) with vertical arrows. Mapping implied by vertical alignment, no cross-panel arrows. Two italic bottom labels: "Siloed functional teams..." and "...siloed application architectures. Because Conway's Law". No fabricated explicit mapping arrows. |
| Information Recovery | Identifies as a team and architecture diagram. A search for "Conway's Law" or "UI specialists" or "siloed functional teams" would not match. The team names, tier icons, and the organizational-to-architectural mapping are invisible. | 3 teams named with colors, 3-tier architecture identified, dashed separator described, Conway's Law reference noted. "Conway's Law siloed teams architecture" would match. May miss the exact figure counts, the shapes inside the server box, or the two-line italic label structure. | Complete recovery: left panel (3 labeled teams with ~5 color-coded stick figures each: blue UI, green middleware, teal DBAs), right panel (3-tier stack: blue document icon, peach 3D server with 3 compartmented shapes, gray database cylinder, vertical arrows). Dashed gray vertical separator. Both italic bottom labels quoted. No cross-panel arrows noted. Sketch aesthetic, white background. Any team name, tier icon, or label visible in the diagram is findable -- parity principle met. |
| Retrieval Value | "A team organization diagram" -- no Conway's Law context, not self-contained. Would not surface for "Conway's Law" or "functional team silos" or "3-tier architecture mapping." | "Conway's Law: siloed functional teams produce siloed 3-tier architectures. From Fowler's microservices article." Searchable but doesn't explain the implication for microservices adoption. | Natural prose explaining this as a Conway's Law visualization from Fowler/Lewis 2014 "Microservices" article. Shows how functional team silos (UI/middleware/DBA) naturally produce corresponding 3-tier system architecture silos. The implicit argument: microservices require cross-functional product teams organized around business capabilities rather than technical layers. Connects to the Inverse Conway Maneuver concept (restructure teams to get the architecture you want). Domain vocabulary embedded (Conway's Law, functional silos, 3-tier architecture, cross-functional teams, microservices). Self-contained. Findable by "Conway's Law siloed teams" or "organizational structure system architecture mapping." |

<br><br>

## doc24-R06 -- Micro-deployment: monolith vs microservices infrastructure

**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory [-> Information Recovery]

- **Diagram type:** Side-by-side deployment infrastructure comparison,
  monolith (left) vs microservices (right), separated by a dashed vertical
  line

**Left panel -- Monolith deployment:**
- 3 stick figure icons at top (blue, light blue/cyan, green) representing
  users/clients
- Arrows pointing upward from 3 identical 3D server boxes to the users
- Each server box (peach/tan 3D frame) contains 3 module compartments with
  colored icons:
  - Green X/cross shape (top compartment)
  - Gray/silver blob (middle compartment)
  - Red/pink heart shape (bottom compartment)
- The 3 servers overlap slightly (showing horizontal scaling replicas)
- Label below: "monolith - multiple modules in the same process" in italic

**Right panel -- Microservices deployment:**
- Same 3 stick figure icons at top (blue, light blue/cyan, green)
- Below the users: a blue document/page icon (possibly representing an API
  gateway or service discovery layer)
- Arrow from users down to the document icon, and arrows from the document
  icon down to individual services
- 4 individual small 3D server boxes spread horizontally at the bottom, each
  containing a single module:
  1. Green X/cross shape
  2. Gray/silver blob
  3. Red/pink heart
  4. Red/pink heart (appears to be a second instance of the same service,
     showing selective replication)
- Each small server has its own 3D peach/tan frame
- Label below: "microservices - modules running in different processes" in
  italic

- **Background:** White
- **Dashed separator:** Vertical dashed line between the two panels
- **Style:** Same hand-drawn/sketch aesthetic as other doc24 diagrams

### Verifiable Facts [-> Correctness]

- FACT: The diagram has two panels separated by a vertical dashed line
- FACT: Both panels show the same 3 stick figures (users) at the top in
  blue, light blue, and green
- FACT: The left panel has 3 overlapping server boxes, each containing 3
  colored module compartments
- FACT: The right panel has 4 individual server boxes, each with a single
  module
- FACT: The 3 module types are represented by the same colored shapes:
  green X, gray blob, red/pink heart
- FACT: A blue document/page icon appears between the users and services in
  the right panel
- FACT: The left label reads "monolith - multiple modules in the same
  process"
- FACT: The right label reads "microservices - modules running in different
  processes"
- FACT: Both labels are in italic text
- FACT: The right panel appears to show 2 instances of the red/pink heart
  service (selective replication)

### Hallucination Risks [-> Correctness]

- RISK: Identifying the blue document icon as a specific technology (e.g.,
  "load balancer", "API gateway", "service mesh")
  REALITY: The icon is a generic document/page shape. Its role is implied
  (routing/discovery layer) but not labeled
- RISK: Counting exactly 3 servers on the left
  REALITY: There appear to be 3 overlapping server boxes, but the
  perspective overlap could be interpreted as 2 or 3
- RISK: Stating that the 4th service box on the right is a "different
  service"
  REALITY: It appears to contain the same red/pink heart shape as the 3rd
  box, suggesting service replication rather than a 4th distinct service
- RISK: Describing arrows as showing request flow direction
  REALITY: The arrow directions suggest server-to-user flow, but the exact
  semantic (request vs. response, or just "serves") is not labeled

### Detail Inventory [-> Information Recovery]

- User stick figures: 3 at top of each panel, same blue/cyan/green colors
  as R02
- Left servers: 3 overlapping 3D boxes, peach/tan frames, each with 3
  compartments showing green X, gray blob, red/pink heart
- Right servers: 4 individual small 3D boxes, peach/tan frames, each with
  1 compartment
- Right intermediary: blue document/page icon with lines suggesting text
- Module colors consistent: green (#228B22 approximate), gray (#808080
  approximate), red/pink (#CC3366 approximate)
- Server compartments appear to have small black connectors/plugs on their
  sides (decorative detail suggesting hardware)
- Dashed vertical separator: gray
- Italic labels at bottom of each panel, black text
- White background

### Domain Context [-> Retrieval Value]

This diagram from Fowler's microservices article illustrates the deployment
infrastructure difference between monolith and microservices approaches.

In the monolith model (left), each server instance runs the complete
application with all modules. To scale, you deploy multiple identical
copies of the entire application. Every replica includes every module,
regardless of which module is the bottleneck.

In the microservices model (right), each module runs as an independent
process in its own server/container. A routing layer (represented by the
document icon) directs requests to the appropriate service. Individual
services can be replicated independently -- the diagram shows this with
what appears to be 2 instances of the heart service while the X and
gray services run as single instances.

This connects to the scaling argument from R01: microservices enable
fine-grained resource allocation. If only one service is under heavy load,
only that service needs additional instances, rather than scaling the
entire monolith.

### Search Keywords [-> Retrieval Value]

micro-deployment, monolith deployment, microservices infrastructure,
service scaling, independent deployment, Martin Fowler, process isolation,
API gateway, service discovery, horizontal scaling, deployment comparison,
containerization

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "Diagram showing server boxes with some shapes inside" -- no monolith/microservices distinction, no deployment concept, no user figures. Or: describes the monolith servers as having different modules (each server has the same 3 modules -- green X, gray blob, pink heart -- they are identical replicas). Inventing service names (e.g., "authentication service") for the abstract module shapes triggers the hallucination cap. Describing the blue document icon as a "load balancer" when its role is only implied by position is a domain knowledge fabrication. | Monolith: 3 servers each with 3 modules (green/gray/pink). Microservices: 4 individual servers, one module each, with document/gateway icon. Both serve 3 users. Dashed separator. Italic labels reference process model difference. May miss the heart service appearing replicated on the 4th server or the plug-like connector details on server frames. | Left: 3 overlapping 3D peach servers, each with 3 compartments (green X, gray blob, pink heart) and plug-like connectors. Arrows from servers to 3 user figures. Right: 4 individual 3D servers (1 module each), arrows through blue document/gateway icon to same 3 users. 4th server replicates the heart module (selective scaling). Italic labels: "monolith - multiple modules in the same process" and "microservices - modules running in different processes". Gray dashed separator. No fabricated service names or explicit load balancer label. |
| Information Recovery | Identifies as a server diagram with shapes. A search for "monolith vs microservices deployment" or "independent process" or "selective replication" would not match. The deployment topology, module types, and gateway icon are invisible. | Both deployment models named, 3 modules per monolith server described, 4 microservice servers noted, user figures and gateway icon mentioned, italic labels present. "Monolith microservices deployment comparison" would match. May miss the plug-like connectors, the overlapping 3D server positioning, or the specific module shape descriptions. | Complete recovery: left panel (3 overlapping 3D servers with 3 compartments each, 3 module types with colors/shapes, arrows to 3 user figures). Right panel (4 individual 3D servers with 1 module each, blue document icon intermediary, arrows to 3 users, heart module replicated). Dashed gray separator. Both italic labels quoted. User figure colors (blue/cyan/green). Peach server frames with plug connectors. White background, sketch style. Any element visible in the diagram is findable -- parity principle met. |
| Retrieval Value | "A deployment diagram" -- no article source, not self-contained. Would not surface for "microservices independent deployment" or "monolith full replication" or "fine-grained scaling." | "Monolith (full replication) vs microservices (independent deployment with selective scaling) from Fowler's article." Searchable but doesn't explain why independent deployment matters operationally. | Natural prose explaining this as a deployment infrastructure comparison from the Fowler/Lewis microservices article. Monolith: replicate the entire application (all 3 modules per server, 3 identical copies). Microservices: independent processes with a routing layer, enabling selective replication (heart service x2, others x1). Illustrates two key operational benefits: fine-grained scaling (scale only the bottleneck) and independent deployment (deploy one service without redeploying others). Connects to the R01 scaling argument at the infrastructure level. Domain vocabulary embedded (monolith, microservices, independent deployment, selective scaling, process isolation). Self-contained. Findable by "microservices deployment infrastructure" or "monolith replication vs selective scaling." |

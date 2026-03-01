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

### Visual Inventory [-> Completeness]

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

### Verifiable Facts [-> Accuracy]

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

### Hallucination Risks [-> Accuracy]

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

### Detail Inventory [-> Specificity]

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

### Domain Context [-> Usefulness]

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

### Search Keywords [-> Usefulness]

monolith vs microservices, architecture comparison, scaling pattern,
horizontal scaling, selective replication, Martin Fowler, James Lewis,
microservices architecture, deployment pattern, service decomposition,
distributed systems

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A diagram comparing two software architectures" (no specifics on monolith vs microservices distinction, no scaling description) | "Monolith vs microservices comparison. Monolith: 5 shapes in one box, scales by replicating 4 copies. Microservices: shapes in separate boxes, scales by distributing selectively." | "2x2 layout. Top: monolith (5 colored shapes in one 3D server) vs microservices (4 separate boxes, one shape each). Bottom: monolith scales by 4 identical full copies in 2x2 grid vs microservices scales by distributing shape subsets across 4 servers with selective replication. All text in italic." |
| Specificity | "Colored blobs in boxes" | "5 colored organic shapes (orange, pink, cyan, maroon, green). 3D peach server frames for monolith. Simple boxes for microservices." | "Orange/pink/cyan/maroon/green amoeba-like blobs. Monolith: 3D peach/tan (#F5DEB3) server boxes with perspective. Microservices: flat boxes (top), distributed in server frames (bottom). 4 italic text labels. Sketch aesthetic. No arrows between panels." |
| Completeness | "Architecture comparison" (misses colors, scaling panels, text labels, server frames) | "4 panels: monolith concept + scaling, microservices concept + scaling. 5 colored shapes. 3D server boxes. Italic labels. White background." | "2x2 layout with 4 italic labels. Monolith: 1 server with 5 shapes (top), 4 identical copies in 2x2 (bottom). Microservices: 4 separate boxes (top), 4 servers with distributed shape subsets (bottom). 5 organic colored shapes in orange/pink/cyan/maroon/green. 3D peach server frames. White background, sketch style." |
| Usefulness | "A software architecture diagram" | "Core monolith vs microservices comparison from Fowler's article. Shows key scaling difference: full replication vs selective distribution." | "Opening diagram from Fowler/Lewis 2014 microservices article. Illustrates structural decomposition (one process vs many) and scaling efficiency (replicate everything vs replicate selectively). Abstract shapes avoid specific service naming. One of the most widely referenced architecture comparison diagrams." |

<br><br>

## doc24-R02 -- Conway's Law: org structure mapped to system architecture

**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory [-> Completeness]

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

### Verifiable Facts [-> Accuracy]

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

### Hallucination Risks [-> Accuracy]

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

### Detail Inventory [-> Specificity]

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

### Domain Context [-> Usefulness]

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

### Search Keywords [-> Usefulness]

Conway's Law, organizational structure, system architecture, siloed teams,
three-tier architecture, functional teams, UI specialists, middleware, DBA,
cross-functional teams, Martin Fowler, microservices organization, team
topology, Inverse Conway Maneuver

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A diagram showing teams and architecture layers" (no Conway's Law mention, no mapping explanation) | "Conway's Law diagram: 3 siloed teams (UI, middleware, DBA) map to 3-tier architecture (UI layer, server, database). Dashed line separates org from architecture." | "Two-panel diagram with dashed separator. Left: 3 color-coded teams (blue UI ~5 figures, green middleware ~5, teal DBAs ~5). Right: 3-tier stack (document icon, 3D server box with 3 shapes, database cylinder) with vertical arrows. Mapping is implied by vertical alignment, not explicit arrows. Bottom labels in italic reference Conway's Law." |
| Specificity | "Stick figures and boxes" | "Blue/green/teal stick figure clusters. Document, server, and database icons. Peach/tan 3D server box." | "~5 blue stick figures (UI), ~5 green/olive (middleware), ~5 teal (DBAs). Blue document icon, peach/tan 3D server box with 3 colored shapes in compartments, gray database cylinder. Gray dashed vertical separator. Italic labels. Same sketch aesthetic as R01." |
| Completeness | "Organization and architecture diagram" (misses team names, colors, tier icons, Conway's Law reference, dashed line) | "3 teams (UI/middleware/DBA) with colored stick figures. 3-tier architecture (UI/server/DB). Dashed separator. Conway's Law label. Italic text." | "Left: 3 labeled color-coded teams with ~5 figures each. Right: 3-tier stack with arrows (document/server/cylinder). Dashed vertical separator. Two italic bottom labels ('Siloed functional teams...' and '...siloed application architectures. Because Conway's Law'). No cross-panel arrows. White background, sketch style." |
| Usefulness | "A team organization diagram" | "Illustrates Conway's Law: siloed functional teams produce siloed 3-tier architectures. From Fowler's microservices article, arguing for cross-functional teams instead." | "Conway's Law visualization from Fowler/Lewis microservices article. Shows how functional team silos (UI/middleware/DBA) naturally produce corresponding 3-tier system silos. Implies need for cross-functional product teams to achieve microservices decomposition. Connects to Inverse Conway Maneuver concept." |

<br><br>

## doc24-R06 -- Micro-deployment: monolith vs microservices infrastructure

**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory [-> Completeness]

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

### Verifiable Facts [-> Accuracy]

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

### Hallucination Risks [-> Accuracy]

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

### Detail Inventory [-> Specificity]

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

### Domain Context [-> Usefulness]

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

### Search Keywords [-> Usefulness]

micro-deployment, monolith deployment, microservices infrastructure,
service scaling, independent deployment, Martin Fowler, process isolation,
API gateway, service discovery, horizontal scaling, deployment comparison,
containerization

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Diagram showing server boxes with some shapes inside" (no monolith/microservices distinction, no deployment concept) | "Monolith: 3 servers each with 3 modules (green/gray/pink). Microservices: 4 individual servers, one module each. Both serve 3 users. Dashed separator." | "Left: 3 overlapping 3D servers, each with 3 module compartments (green X, gray blob, pink heart). Arrows to 3 users. Right: 4 individual servers (1 module each), connecting through document/gateway icon to same 3 users. 4th server appears to replicate the heart service. Italic labels describe process model difference." |
| Specificity | "Boxes and stick figures" | "3 colored module types (green X, gray, pink heart). Peach 3D server frames. Blue document icon on right. 3 colored stick figures." | "Left: 3x3D boxes overlapping, each with 3 compartments with plug-like connectors. Right: 4 individual 3D boxes. Blue document/page intermediary icon. User figures in blue/cyan/green. Gray dashed separator. Italic labels at bottom." |
| Completeness | "Server deployment comparison" (misses module types, user figures, gateway icon, labels) | "2 panels: monolith (3 replicas, 3 modules each) vs microservices (4 individual servers). Users, gateway icon, italic labels, dashed separator." | "Left: 3 users, arrows to 3 overlapping servers (3 modules each: green X/gray/pink heart). Right: 3 users, blue document icon, arrows to 4 individual servers (1 module each, heart appears replicated). Dashed separator. Italic labels ('monolith - multiple modules in same process' / 'microservices - modules running in different processes'). White background, sketch style." |
| Usefulness | "A deployment diagram" | "Infrastructure comparison showing monolith (full replication) vs microservices (independent deployment with selective scaling). Gateway/routing layer shown." | "Deployment infrastructure comparison from Fowler article. Monolith: replicate everything (3 full copies). Microservices: independent processes with routing layer, selective replication (heart service x2, others x1). Illustrates fine-grained scaling and independent deployment -- key operational benefits of microservices. Connects to R01 scaling argument." |

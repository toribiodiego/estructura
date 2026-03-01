# Image Analysis: Doc 23 -- 23_nvie_git_branching_model.html

**Document:** `23_nvie_git_branching_model.html`
**Format:** HTML
**Source:** https://nvie.com/posts/a-successful-git-branching-model/
**Category:** multi-image
**Images:** 6
**Document context:** Vincent Driessen's git-flow branching model article
with 6 diagrams illustrating branch topology for feature development,
release preparation, and hotfix workflows.

**Eval subset:** 3 of 6 content images

<br><br>

## doc23-R01 -- Complete git-flow branching model

**Content type:** diagram
**Annotation difficulty:** Medium

### Visual Inventory [-> Information Recovery]

- **Diagram type:** Vertical swim-lane flow diagram showing a git branching
  model, with time flowing downward
- **Time indicator:** Bold italic "Time" label on the left edge with a
  hand-drawn downward arrow (sketch aesthetic)
- **Swim lanes (left to right):** 5 vertical columns separated by light gray
  vertical lines, with column headers at the top:
  1. "feature branches" (regular weight)
  2. "**develop**" (bold)
  3. "release branches" (regular weight)
  4. "hotfixes" (regular weight)
  5. "**master**" (bold)
- **Node types (colored circles representing commits):**
  - Yellow: develop branch commits (~15 nodes)
  - Pink/magenta: feature branch commits (~14 nodes across 2-3 feature
    branches)
  - Green: release branch commits (~6 nodes)
  - Red/coral: hotfix branch commit (1 node)
  - Cyan/light blue: master branch commits (4 nodes, each at a tag point)
- **Tags on master (right side, in rounded gray boxes):**
  - "Tag **0.1**" -- at the top master node
  - "Tag **0.2**" -- at the second master node (after hotfix merge)
  - "Tag **1.0**" -- at the third master node (after release merge)
  - A fourth cyan node at the very bottom (no visible tag)
- **Annotation callouts (speech-bubble style boxes with pointers):**
  1. "Feature for future release" -- pointing to the leftmost feature branch
  2. "Major feature for next release" -- pointing to the second feature
     branch starting area
  3. "Severe bug fixed for production: hotfix **0.2**" -- pointing to the
     hotfix branch area
  4. "Incorporate bugfix in **develop**" -- pointing to the merge from hotfix
     to develop
  5. "From this point on, 'next release' means the release *after* 1.0"
     -- connected by a dashed gray line to the feature branch area
  6. "Start of release branch for **1.0**" -- pointing to where release
     branch forks from develop
  7. "Only bugfixes!" -- pointing to the release branch commit series
  8. "Bugfixes from **rel. branch** may be continuously merged back into
     **develop**" -- pointing to gray arrows from release branch to develop
- **Arrows:**
  - Black arrows between nodes showing commit flow and merge directions
  - Arrows flow downward within branches and diagonally for merges/forks
  - Gray/light arrows from release branch back to develop (continuous merge)
  - Dashed gray line for the "after 1.0" annotation reference
- **Branching topology visible:**
  - Feature branches fork from develop and merge back to develop
  - Hotfix branch forks from master, merges to both master and develop
  - Release branch forks from develop, merges to both master and develop
  - Master only receives merges (from release and hotfix branches)
- **Background:** White
- **Style:** Clean diagram with hand-drawn/sketch aesthetic for the Time
  arrow and border scribble marks at the top-left corner

### Verifiable Facts [-> Correctness]

- FACT: There are exactly 5 swim lanes labeled: feature branches, develop,
  release branches, hotfixes, master
- FACT: "develop" and "master" are in bold text; the other 3 headers are
  regular weight
- FACT: Time flows downward as indicated by a "Time" label with downward
  arrow on the left
- FACT: There are exactly 3 labeled tags on the master branch: 0.1, 0.2,
  and 1.0
- FACT: There is exactly 1 red/coral node (hotfix commit)
- FACT: Yellow circles represent develop commits, pink circles represent
  feature branch commits, green represent release branch commits, and cyan
  represent master commits
- FACT: There are exactly 8 annotation callout boxes
- FACT: The hotfix branch merges into both master (creating Tag 0.2) and
  develop
- FACT: The release branch for 1.0 forks from develop and eventually merges
  into master (creating Tag 1.0)
- FACT: There are gray arrows from the release branch back to develop
  indicating continuous merge-back of bugfixes
- FACT: One annotation reads "Only bugfixes!" pointing to the release branch
- FACT: One annotation uses italic text: "after" in "the release *after* 1.0"
- FACT: The callouts use bold for version numbers and branch names (e.g.,
  "hotfix **0.2**", "**develop**", "**rel. branch**")

### Hallucination Risks [-> Correctness]

- RISK: Counting exact number of nodes per branch
  REALITY: The exact count is hard to verify at this resolution due to
  overlapping and closely-spaced nodes. Approximate counts are: develop ~15,
  feature ~14, release ~6, hotfix ~1, master ~4
- RISK: Describing specific commit messages or content for individual nodes
  REALITY: Nodes are plain colored circles with no labels. No commit IDs,
  messages, or dates are shown on individual nodes
- RISK: Stating there are exactly 2 or 3 feature branches
  REALITY: The feature branch area shows pink nodes that appear to form 2-3
  distinct branch lines, but the exact count depends on interpretation of
  the merge topology
- RISK: Describing this as "Gitflow" with capital F
  REALITY: The diagram shows Vincent Driessen's branching model. The term
  "git-flow" (hyphenated, lowercase) is used in the article. The diagram
  itself does not contain the word "Gitflow"

### Detail Inventory [-> Information Recovery]

- Diagram dimensions: tall vertical format (~575px wide at 2x per HTML width
  attribute)
- Time arrow: hand-drawn sketch style, bold italic "Time" text, top-left
- Column header text: "feature branches" and "release branches" span 2 lines
- Node colors: yellow (#FFD700 approximate), pink (#FF69B4 approximate),
  green (#32CD32 approximate), red/coral (#FF6B6B approximate), cyan
  (#00CED1 approximate)
- Each node has a thin dark outline and slight 3D shadow/highlight
- Arrows: black with arrowhead tips, varying angles for merges vs linear flow
- Tag boxes: rounded corners, gray background, "Tag" in regular weight,
  version number in bold blue
- Annotation callouts: light gray background, rounded corners, pointer/tail
  indicating target area, mixed regular/bold/italic text
- Gray dashed line connects left feature branch area to "after 1.0"
  annotation
- Gray semi-transparent arrows from release branch back to develop
- Sketch marks at top-left corner (decorative, hand-drawn style)
- No grid, no axis, no border except decorative sketch marks

### Domain Context [-> Retrieval Value]

This is the central diagram from Vincent Driessen's influential 2010 blog
post "A successful Git branching model" (nvie.com). It illustrates the
complete git-flow branching strategy that became one of the most widely
adopted Git workflows in software development.

The model defines 5 branch types: master (production releases, tagged),
develop (integration branch for the next release), feature branches
(individual feature work), release branches (release preparation with only
bugfixes), and hotfix branches (emergency production fixes).

Key workflow principles shown in the diagram:
- Feature branches fork from and merge back to develop only
- Release branches fork from develop, receive only bugfixes, and merge to
  both master (tagged) and develop
- Hotfix branches fork from master and merge to both master (tagged) and
  develop
- Master only receives merges, never direct commits
- The "no fast-forward" merge strategy is implicit (merge commits visible)

This model was later partially deprecated by Driessen himself (2020 note
on the article) in favor of simpler models like GitHub Flow for web
applications, though it remains widely used for projects with formal
release cycles.

### Search Keywords [-> Retrieval Value]

git-flow, branching model, Vincent Driessen, nvie, feature branch, release
branch, hotfix, develop, master, merge workflow, branch topology, git
workflow, software release, version tagging, continuous integration

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A diagram showing git branches with colored dots and arrows" -- no branch names, no tags, no workflow topology. Or: misidentifies the branch colors (e.g., calling release branches "blue" when they are green). Inventing branch names not shown in the diagram (e.g., "staging" or "QA") triggers the hallucination cap. Claiming "develop merges directly to master" mischaracterizes the topology -- only release and hotfix branches merge to master. Describing time as flowing upward (it flows downward) is a structural error. | Git-flow diagram with 5 branch types correctly color-mapped: feature (pink), develop (yellow), release (green), hotfix (red), master (cyan). 3 tags (0.1, 0.2, 1.0). Hotfix merges to both master and develop. Time flows downward. May miss specific callout text, the dashed gray reference line, or the gray merge-back arrows from release to develop. | 5-lane vertical diagram with time flowing down. Column headers exact: "feature branches", "develop" (bold), "release branches", "hotfixes", "master" (bold). Feature branches (pink) fork/merge to develop (yellow). Release (green) forks from develop, merges to master (cyan) and develop. Hotfix (red, 1 node) creates Tag 0.2 on master. 3 tag boxes: 0.1, 0.2, 1.0. 8 callout annotations with text (including "Only bugfixes!", "Incorporate bugfix in develop", etc.). Gray arrows for continuous release-to-develop merge-back. Dashed gray reference line. No fabricated branch names or merge paths. |
| Information Recovery | Identifies as a git branching diagram with colors. A search for "git-flow" or "release branches" or "Tag 0.2" would not match. The 5-lane structure, merge topology, callout annotations, and tag versions are invisible. | All 5 branch types named with colors, 3 tags listed, major merge paths described (feature-to-develop, release-to-master, hotfix-to-both). "Git-flow branching model" would match. May miss individual callout annotation text, node counts per lane, the hand-drawn Time arrow aesthetic, or the dashed reference line. | Complete recovery: 5 column headers with bold styling on develop/master. ~40 commit nodes across 5 colors with approximate counts per lane. 3 tag boxes (rounded gray, bold blue version numbers). 8 callout annotations with text content (bold branch names and versions, italic "after 1.0"). Black directional arrows for flow/merge, gray arrows for release-to-develop merge-back, dashed gray reference line. Hand-drawn Time arrow with sketch aesthetic. White background. Any branch, tag, or annotation visible in the diagram is findable -- parity principle met. |
| Retrieval Value | "A software development diagram" -- no model name, not self-contained. Would not surface for "git-flow branching model" or "Driessen release workflow" or "feature branch merge strategy." | "Vincent Driessen's git-flow branching model with 5 branch types and 3 version tags." Searchable but doesn't explain the workflow rules or why the model matters. | Natural prose identifying this as the central diagram from Vincent Driessen's "A successful Git branching model" (2010). Explains the 5-branch workflow: features fork/merge to develop, releases fork from develop and merge to master+develop, hotfixes fork from master and merge to both. Illustrates no-fast-forward merge topology, continuous bugfix merge-back, and semantic versioning (0.1/0.2/1.0). Widely adopted for projects with formal release cycles. Domain vocabulary embedded (git-flow, feature branch, release branch, hotfix, no-fast-forward, semantic versioning). Self-contained. Findable by "git-flow branching diagram" or "Driessen release merge model." |

<br><br>

## doc23-R04 -- Feature branch create-and-merge workflow

**Content type:** diagram
**Annotation difficulty:** Easy

### Visual Inventory [-> Information Recovery]

- **Diagram type:** Vertical 2-lane flow diagram showing a single feature
  branch lifecycle, with time flowing downward
- **Swim lanes (left to right):**
  1. "feature branches" (regular weight, wraps to 2 lines)
  2. "**develop**" (bold)
- **Nodes:**
  - Yellow circles (develop): approximately 7 nodes in a vertical chain
  - Pink/magenta circles (feature branch): 4 nodes in a vertical chain
- **Flow:**
  - Develop branch runs vertically on the right with consecutive yellow
    commits
  - A diagonal arrow forks from the 3rd develop node leftward to create
    the feature branch
  - 4 pink commits on the feature branch
  - A diagonal arrow from the last pink node merges back into the develop
    branch (no-fast-forward merge, creating a merge commit node on develop)
- **Arrows:** Black with arrowhead tips, downward within branches and
  diagonal for fork/merge
- **Separator:** Light gray vertical line between the two lanes
- **Background:** White with sketch-style gray watermark/texture marks
- **Style:** Same hand-drawn aesthetic as doc23-R01

### Verifiable Facts [-> Correctness]

- FACT: There are exactly 2 swim lanes: "feature branches" and "develop"
- FACT: "develop" is in bold text; "feature branches" is regular weight
- FACT: There are exactly 4 pink/magenta nodes on the feature branch
- FACT: The feature branch forks from the develop branch (diagonal arrow
  from develop to feature)
- FACT: The feature branch merges back into develop (diagonal arrow from
  last pink node to develop)
- FACT: The merge creates a merge commit on the develop branch (the develop
  node at the merge point has incoming arrows from both the previous develop
  node and the feature branch)
- FACT: No annotations, labels, or callout boxes are present (unlike R01)
- FACT: No version tags are shown
- FACT: Time flows downward (consistent with R01, though no explicit Time
  label here)

### Hallucination Risks [-> Correctness]

- RISK: Counting exactly 7 yellow nodes
  REALITY: The yellow nodes are closely spaced and the exact count may be
  6-8 depending on how the merge node is counted. Approximately 7 is a
  reasonable estimate
- RISK: Describing specific feature branch names or purposes
  REALITY: No text labels identify the feature branch. The only labels are
  the column headers "feature branches" and "develop"
- RISK: Stating this shows "git merge --no-ff" explicitly
  REALITY: The merge topology is consistent with no-fast-forward merges
  (a merge commit is visible on develop), but the diagram does not include
  any command text

### Detail Inventory [-> Information Recovery]

- Column header "feature branches": regular weight, wraps to 2 lines,
  left-aligned
- Column header "develop": bold, single line, right of center
- Yellow nodes: same style as R01 (~20px diameter, dark outline, 3D highlight)
- Pink nodes: same style (~20px diameter, dark outline, 3D highlight)
- Fork arrow: diagonal from 3rd yellow node to 1st pink node
- Merge arrow: diagonal from 4th pink node to a yellow node on develop
- Approximately 3 develop commits occur between the fork and merge points
  (develop continues advancing while feature work happens)
- Gray vertical separator line between lanes
- Sketch-style gray texture marks along the separator lines
- No grid, no time label, no tags, no annotations
- Narrow format: ~133px wide at 2x per HTML width attribute

### Domain Context [-> Retrieval Value]

This diagram illustrates the simplest workflow in the git-flow model: a
feature branch lifecycle. A developer creates a feature branch from
develop, makes several commits (4 shown), then merges the completed feature
back into develop using a no-fast-forward merge.

Key principles shown:
- Feature branches fork from and merge back to develop only (never master)
- The develop branch continues receiving other commits while the feature
  branch is active (parallel development)
- The merge creates a merge commit on develop, preserving the branch
  topology in the commit graph

This is the building block for the full git-flow model shown in doc23-R01.
In practice, a project may have multiple feature branches active
simultaneously, each following this same fork-work-merge pattern.

### Search Keywords [-> Retrieval Value]

feature branch, git-flow, develop branch, merge workflow, branch topology,
no-fast-forward merge, git branch lifecycle, fork and merge, Vincent
Driessen, nvie

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A diagram with yellow and pink dots connected by lines" -- no branch identification, no flow direction, no fork/merge topology. Or: describes the pink nodes as "release" or "hotfix" branches (they are feature branches). Claiming the feature branch merges directly to master triggers the hallucination cap -- it merges to develop only. Miscounting nodes (e.g., "3 pink nodes" when there are 4) is a count error. Stating time flows upward (it flows downward) is a structural error. | Feature branch workflow identified: pink nodes fork from yellow develop branch, 4 feature commits, merge back to develop. Two lanes with correct headers. Develop advances in parallel. May miss the exact node count on the develop branch or the sketch aesthetic. | 2-lane diagram: develop (yellow, ~7 nodes, bold header) on right, feature branches (pink, 4 nodes, regular header) on left. Feature forks from develop's ~3rd commit via diagonal arrow, merges back via no-ff merge commit (diagonal arrow from last pink to develop). Develop advances ~3 commits in parallel between fork and merge points. No fabricated annotations, tags, or extra branches. |
| Information Recovery | Identifies as a diagram with two columns of colored circles. A search for "feature branch" or "develop" or "fork and merge" would not match. The branch names, merge topology, and parallel development pattern are invisible. | Both branch types named with colors, fork and merge points described, node counts approximate, headers noted. "Feature branch develop merge" would match. May miss the number of develop commits between fork and merge, the gray separator line, or the sketch aesthetic. | Complete recovery: 2 lane headers ("feature branches" regular, "develop" bold). Node counts (~7 yellow + 4 pink). Fork arrow direction (develop to feature) and merge arrow direction (feature to develop). Parallel commit advancement on develop. Gray separator line between lanes. Sketch aesthetic with hand-drawn texture. No annotations, tags, labels, or time indicator. White background. Any structural element visible in the diagram is findable -- parity principle met. |
| Retrieval Value | "A git diagram" -- no workflow context, not self-contained. Would not surface for "git-flow feature branch" or "no-fast-forward merge" or "parallel development workflow." | "Feature branch lifecycle from git-flow: fork from develop, 4 commits, merge back." Searchable but doesn't explain the no-ff merge significance or how this relates to the full git-flow model. | Natural prose identifying this as the simplest git-flow workflow unit: a single feature branch forks from develop, makes 4 commits, and merges back via no-fast-forward merge while develop advances in parallel. Building block for the full model (doc23-R01). Key principle: features only interact with develop, never master. No-ff merge preserves branch topology in the history graph. Domain vocabulary embedded (feature branch, develop, no-fast-forward, git-flow). Self-contained. Findable by "git-flow feature branch workflow" or "feature branch merge develop diagram." |

<br><br>

## doc23-R05 -- Merge comparison: fast-forward vs no-ff

**Content type:** diagram
**Annotation difficulty:** Easy

### Visual Inventory [-> Information Recovery]

- **Diagram type:** Side-by-side comparison of two merge strategies, showing
  the resulting commit graph topology for each
- **Layout:** Two diagrams placed horizontally next to each other, each
  with its own column headers and label

**Left diagram -- no-fast-forward merge:**
- **Headers:** "feature branches" (regular weight, 2 lines) and "**develop**"
  (bold)
- **Nodes:** Yellow circles (develop, ~5) and pink/magenta circles (feature
  branch, 3)
- **Topology:** Feature branch forks from the 2nd develop node (diagonal
  arrow left), 3 pink commits, then merges back to develop (diagonal arrow
  right) creating a merge commit (bottom yellow node)
- **Curly brace:** Gray left-side brace bracketing the 3 pink nodes, labeled
  "feature" in gray italic text
- **Label below:** `git merge --no-ff` in monospace/code font

**Right diagram -- fast-forward (plain) merge:**
- **Header:** "**develop**" (bold) -- only one column
- **Nodes:** All yellow circles (~7) in a single linear vertical chain
- **Topology:** No separate branch visible. The feature commits are
  integrated inline on the develop branch (fast-forward result)
- **Curly brace:** Gray right-side brace bracketing 3 of the middle yellow
  nodes, labeled "feature" in gray italic text -- indicating which commits
  were originally on the feature branch
- **Label below:** `git merge` on line 1, `(plain)` on line 2, in
  monospace/code font

- **Arrows:** Black with arrowheads, downward flow, diagonal for fork/merge
  on left diagram
- **Background:** White with sketch-style gray texture marks on separator
  lines
- **Style:** Same hand-drawn aesthetic as R01 and R04

### Verifiable Facts [-> Correctness]

- FACT: There are exactly 2 diagrams side by side
- FACT: The left diagram is labeled "git merge --no-ff" and the right is
  labeled "git merge (plain)"
- FACT: The left diagram shows 2 swim lanes (feature branches + develop)
  with pink and yellow nodes
- FACT: The right diagram shows only 1 swim lane (develop) with all yellow
  nodes
- FACT: Both diagrams have a gray curly brace labeled "feature" bracketing
  3 nodes
- FACT: The left diagram's feature brace is on the left side; the right
  diagram's is on the right side
- FACT: In the left diagram, the feature branch creates a separate line of
  3 pink commits that merge back to develop
- FACT: In the right diagram, all commits are on a single linear chain
  (no branch topology preserved)
- FACT: The labels use monospace/code font
- FACT: The left diagram has exactly 3 pink/magenta nodes
- FACT: No annotations or callout boxes are present

### Hallucination Risks [-> Correctness]

- RISK: Describing the right diagram as having "no feature commits"
  REALITY: The right diagram still has the feature commits -- they are just
  inline on the develop branch (yellow). The curly brace marks which 3
  yellow nodes were the feature commits
- RISK: Stating the left side is "better" or "recommended"
  REALITY: The diagram does not express a preference. However, the article
  context recommends --no-ff for preserving branch history
- RISK: Describing the font as a specific typeface
  REALITY: The labels appear to be in a monospace/code font but the exact
  typeface is not identifiable

### Detail Inventory [-> Information Recovery]

- Left diagram: 2 column headers, ~5 yellow + 3 pink nodes, fork and merge
  arrows, left curly brace with "feature" label
- Right diagram: 1 column header ("develop" bold), ~7 yellow nodes in
  linear chain, right curly brace with "feature" label
- Curly braces: gray, hand-drawn style, roughly the same vertical extent
  in both diagrams
- "feature" label: gray italic text, positioned outside the brace
- Bottom labels in monospace: "git merge --no-ff" (left), "git merge" /
  "(plain)" on 2 lines (right)
- Yellow nodes: same style as R01/R04
- Pink nodes: same style as R01/R04
- Image width: ~478px at 2x per HTML width attribute
- No time arrow, no tags, no annotations
- White background, sketch-style gray texture on separator lines

### Domain Context [-> Retrieval Value]

This diagram explains the key merge strategy recommendation in the git-flow
model: always use `--no-ff` (no fast-forward) when merging feature branches
into develop.

The left diagram (--no-ff) preserves the branch topology in the commit
history. A reviewer can see that 3 commits were grouped as a feature branch,
and the merge commit marks where the feature was integrated. This makes it
easy to identify, review, and if necessary revert an entire feature as a
single logical unit.

The right diagram (fast-forward/plain merge) loses the branch structure.
The feature commits become indistinguishable from regular develop commits.
There is no merge commit and no record that these commits were ever on a
separate branch.

Driessen recommends --no-ff as the default for all merges in git-flow
because preserving branch topology provides better traceability and
auditability of the development history.

### Search Keywords [-> Retrieval Value]

git merge no-ff, fast-forward merge, no-fast-forward, merge strategy,
branch topology, commit graph, merge commit, git-flow, develop branch,
feature branch merge, Vincent Driessen, nvie, branch history

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "Two branch diagrams showing different merge approaches" -- no strategy names, no topology distinction, no node colors. Or: swaps the labels (calling the left diagram "plain merge" and the right "--no-ff"). Describing both diagrams as having the same topology misses the core visual point. Fabricating git command flags not shown in the image (e.g., "--squash") triggers the hallucination cap. Miscounting feature commits (3 pink nodes in the left diagram) is a count error. | Side-by-side comparison correctly identified: --no-ff merge (left) preserves separate feature branch with pink nodes, plain merge (right) creates linear all-yellow history. Both bracket 3 feature commits with curly braces. Monospace labels below each diagram. May miss the exact node counts or header text details. | Left: 2-lane diagram with "feature branches" and "develop" (bold) headers. 3 pink nodes fork from 2nd develop commit, merge back via merge commit to ~5 yellow develop nodes. Right: 1-lane "develop" (bold) only, ~7 yellow nodes in linear chain. Both use gray curly braces labeled "feature" (gray italic) bracketing 3 commits. Labels in monospace: "git merge --no-ff" vs "git merge (plain)". No fabricated merge strategies or extra labels. |
| Information Recovery | Identifies as two git diagrams side by side. A search for "--no-ff" or "fast-forward" or "feature branch topology" would not match. The merge strategy names, node topology differences, and curly brace annotations are invisible. | Both diagrams described with merge strategy labels, node colors (pink vs all-yellow), curly braces noted, monospace labels quoted. "No-ff merge comparison" would match. May miss the exact fork/merge positions, the header text styling (bold develop), or the gray sketch texture. | Complete recovery: left diagram (2 headers, ~5 yellow + 3 pink nodes, fork arrow, merge arrow, left gray brace "feature"), right diagram (1 header, ~7 yellow linear, right gray brace "feature"). Monospace labels quoted verbatim. Header styling (bold develop). Sketch-style gray texture. Black directional arrows. White background. No annotations or tags. Any structural or text element visible in the comparison is findable -- parity principle met. |
| Retrieval Value | "A git merge diagram" -- no strategy context, not self-contained. Would not surface for "no-fast-forward merge" or "branch topology preservation" or "git-flow merge recommendation." | "Shows why --no-ff is recommended in git-flow: preserves feature branch topology vs linear history loss with fast-forward." Searchable but doesn't explain the practical impact. | Natural prose explaining this as the core git-flow merge recommendation visualization. --no-ff preserves branch topology: 3 feature commits remain grouped by the merge commit, making them easy to identify, review, and revert as a unit. Plain (fast-forward) merge loses this structure, creating a flat linear history where feature boundaries are invisible. Driessen recommends --no-ff as the default for all feature merges. Key for code review workflows and auditability. Domain vocabulary embedded (no-fast-forward, merge commit, branch topology, fast-forward, git-flow). Self-contained. Findable by "no-ff merge comparison" or "git-flow merge topology recommendation." |

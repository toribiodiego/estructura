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

### Visual Inventory [-> Completeness]

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

### Verifiable Facts [-> Accuracy]

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

### Hallucination Risks [-> Accuracy]

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

### Detail Inventory [-> Specificity]

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

### Domain Context [-> Usefulness]

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

### Search Keywords [-> Usefulness]

git-flow, branching model, Vincent Driessen, nvie, feature branch, release
branch, hotfix, develop, master, merge workflow, branch topology, git
workflow, software release, version tagging, continuous integration

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A diagram showing git branches with colored dots and arrows" (no branch names, no tags, no workflow description) | "Git-flow diagram with 5 branch types: feature (pink), develop (yellow), release (green), hotfix (red), master (cyan). Tags 0.1, 0.2, 1.0. Hotfix merges to both master and develop." | "5-lane vertical diagram with time flowing down. Feature branches (pink) fork/merge to develop (yellow). Release branch (green) forks from develop, merges to master (cyan) and develop. Hotfix (red, 1 node) creates Tag 0.2 on master. 3 tags: 0.1/0.2/1.0. 8 callout annotations. Gray arrows show continuous release-to-develop merge-back." |
| Specificity | "Colored circles connected by arrows in columns" | "5 columns: feature/develop/release/hotfixes/master. Yellow, pink, green, red, cyan nodes. Bold labels for develop and master. 3 tag boxes on right." | "Column headers: 'feature branches'/develop (bold)/release branches/hotfixes/master (bold). Node counts: ~15 yellow, ~14 pink, ~6 green, 1 red, 4 cyan. Tag boxes: rounded gray with bold blue version numbers. 8 callouts with mixed bold/italic formatting. Hand-drawn Time arrow with sketch marks." |
| Completeness | "Git branching diagram" (misses branch types, colors, tags, annotations, merge topology) | "Complete git-flow model with 5 branch types, 3 version tags, feature-to-develop merges, hotfix-to-master-and-develop merge, release branch workflow. 8 annotations explain the flow." | "5 swim lanes with headers (2 bold). ~40 commit nodes in 5 colors. 3 tags (0.1/0.2/1.0). 8 annotation callouts with bold branch names and versions. Black directional arrows for flow/merge, gray arrows for release-to-develop merge-back, dashed gray reference line. Time arrow with sketch aesthetic. White background." |
| Usefulness | "A software development diagram" | "Vincent Driessen's git-flow branching model showing the complete workflow for features, releases, and hotfixes. Master receives only merges from release and hotfix branches." | "Central diagram from Driessen's 'A successful Git branching model' (2010). Shows 5-branch workflow: features fork/merge to develop, releases fork from develop and merge to master+develop, hotfixes fork from master and merge to master+develop. Illustrates no-fast-forward merge topology, continuous bugfix merge-back, and semantic versioning tags. Widely adopted for projects with formal release cycles." |

<br><br>

## doc23-R04 -- Feature branch create-and-merge workflow

**Content type:** diagram
**Annotation difficulty:** Easy

### Visual Inventory [-> Completeness]

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

### Verifiable Facts [-> Accuracy]

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

### Hallucination Risks [-> Accuracy]

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

### Detail Inventory [-> Specificity]

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

### Domain Context [-> Usefulness]

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

### Search Keywords [-> Usefulness]

feature branch, git-flow, develop branch, merge workflow, branch topology,
no-fast-forward merge, git branch lifecycle, fork and merge, Vincent
Driessen, nvie

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A diagram with yellow and pink dots connected by lines" (no branch identification, no flow description) | "Feature branch workflow: pink nodes fork from yellow develop branch, make 4 commits, merge back. Two lanes." | "2-lane diagram: develop (yellow, ~7 nodes, bold header) and feature branches (pink, 4 nodes). Feature forks from develop's 3rd commit via diagonal arrow, merges back via no-ff merge commit. Develop advances in parallel during feature work." |
| Specificity | "Two columns of colored circles" | "Yellow circles for develop, pink for feature. ~7 and 4 nodes respectively. Bold 'develop' header. Fork and merge arrows." | "4 pink nodes in left lane, ~7 yellow in right. Fork from 3rd develop node. ~3 develop commits between fork and merge points. Merge arrow creates merge commit on develop. Sketch-style gray texture. Image ~133px wide at 2x." |
| Completeness | "Branch diagram" (misses colors, node counts, merge topology, headers) | "2 lanes (feature/develop), fork and merge arrows, ~11 total nodes, no annotations or tags" | "2 lanes with headers (bold develop, regular feature branches). ~7 yellow + 4 pink nodes. Fork arrow (develop to feature), merge arrow (feature to develop). Gray separator line. Sketch aesthetic. No annotations, tags, labels, or time indicator. White background." |
| Usefulness | "A git diagram" | "Feature branch lifecycle from git-flow: fork from develop, work, merge back with no-fast-forward merge. Parallel development shown." | "Simplest git-flow workflow unit: single feature branch forks from develop, 4 commits, merges back via no-ff. Develop advances in parallel (~3 commits). Building block for full model in R01. Key principle: features only interact with develop, never master." |

<br><br>

## doc23-R05 -- Merge comparison: fast-forward vs no-ff

**Content type:** diagram
**Annotation difficulty:** Easy

### Visual Inventory [-> Completeness]

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

### Verifiable Facts [-> Accuracy]

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

### Hallucination Risks [-> Accuracy]

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

### Detail Inventory [-> Specificity]

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

### Domain Context [-> Usefulness]

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

### Search Keywords [-> Usefulness]

git merge no-ff, fast-forward merge, no-fast-forward, merge strategy,
branch topology, commit graph, merge commit, git-flow, develop branch,
feature branch merge, Vincent Driessen, nvie, branch history

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Two branch diagrams showing different merge approaches" (no strategy names, no topology description) | "Side-by-side comparison: --no-ff merge preserves separate feature branch (pink nodes merge back), plain merge creates linear history (all yellow). Both bracket 3 feature commits." | "Left: 2-lane (feature+develop), 3 pink nodes fork/merge to ~5 yellow, merge commit created. Right: 1-lane (develop), ~7 yellow linear chain, no branch topology. Both use gray curly braces labeled 'feature' bracketing 3 commits. Labels: 'git merge --no-ff' vs 'git merge (plain)' in monospace." |
| Specificity | "Yellow and pink circles in two arrangements" | "3 pink + ~5 yellow nodes (left), ~7 yellow (right). Curly braces mark feature commits. Monospace labels." | "Left: fork from 2nd yellow, 3 pink, merge to bottom yellow. Right: linear chain, brace on right. Gray italic 'feature' labels. Monospace 'git merge --no-ff' and 'git merge (plain)'. ~478px wide at 2x. Sketch-style texture." |
| Completeness | "Merge comparison diagram" (misses strategy names, node counts, brace labels, topology details) | "Two diagrams: --no-ff (2-lane, pink+yellow, merge commit) vs plain (1-lane, all yellow, linear). Feature braces on both. Monospace labels." | "Side-by-side. Left: 2 headers (feature/develop bold), ~5 yellow + 3 pink, fork arrow, merge arrow, left brace 'feature'. Right: 1 header (develop bold), ~7 yellow linear, right brace 'feature'. Monospace labels below. Black arrows, gray sketch texture, white background. No annotations/tags." |
| Usefulness | "A git merge diagram" | "Explains why --no-ff is recommended in git-flow: preserves feature branch topology vs linear history loss with fast-forward." | "Core git-flow recommendation visualization. --no-ff preserves branch topology for traceability: 3 feature commits grouped by merge commit, easy to identify/review/revert as unit. Plain merge loses structure. Driessen recommends --no-ff as default for all merges. Key for code review and auditability workflows." |

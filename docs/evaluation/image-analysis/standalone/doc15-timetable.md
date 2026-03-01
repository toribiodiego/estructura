# Image Analysis: Doc 15 -- 15_timetable.jpg

**Document:** `15_timetable.jpg`
**Format:** JPG
**Source:** https://courses.washington.edu/fish340/Images/timetable.jpg
**Category:** table-image
**Images:** 1
**Document context:** Standalone image of a SWORD class assignment timetable
with color-coded cells indicating different assignment types across a 9-week
schedule.

<br><br>

## doc15-R01 -- Color-coded course timetable

**Figure reference:** (standalone image)
**Content type:** table-image
**Annotation difficulty:** Medium
**Dimensions:** (full image)

### Visual Inventory [-> Information Recovery]

- **Image type:** Color-coded course assignment timetable
- **Title:** "SWORD Deadlines" in bold black text, centered at top
- **Table structure:** 5 columns, 1 header row, 9 data rows (weeks 3-11)
- **Column headers (bold black text, gray background):**
  1. week
  2. due @ 9pm
  3. draft
  4. review
  5. feedback
- **Data rows (week | date | draft | review | feedback):**
  1. 3 | 12-Oct | Intro (light green) | | |
  2. 4 | 19-Oct | | Intro (light blue) | |
  3. 5 | 26-Oct | Methods (light green) | | Intro (light red/pink) |
  4. 6 | 2-Nov | | Methods (light blue) | |
  5. 7 | 9-Nov | Results (light green) | | Methods (light red/pink) |
  6. 8 | 16-Nov | | Results (light blue) | |
  7. 9 | 23-Nov | Discussion (light green) | | Results (light red/pink) |
  8. 10 | 30-Nov | | Discussion (light blue) | |
  9. 11 | 7-Dec | Final (salmon/red bg, red text) | | |
- **Color coding by phase (not by section):**
  - Draft column: light green background
  - Review column: light blue background
  - Feedback column: light red/pink background
  - Final: salmon/red background with bold red text
- **Pattern:** Each section follows a 3-week cycle:
  - Week N: draft due
  - Week N+1: review due
  - Week N+2: feedback due
  - The Final paper breaks this pattern (draft only, week 11)
- **Styling:**
  - Header row: gray background, bold text
  - Data cells: thin black border lines
  - Week and date columns: white background, regular text
  - Assignment cells: colored backgrounds with centered text
  - Empty cells: white background
- **Font:** Sans-serif, black text (except Final which is red)

### Verifiable Facts [-> Correctness]

- FACT: The title reads "SWORD Deadlines"
- FACT: There are exactly 5 columns: week, due @ 9pm, draft, review, feedback
- FACT: Weeks covered: 3 through 11 (9 data rows)
- FACT: Dates range from 12-Oct to 7-Dec
- FACT: Four paper sections appear: Intro, Methods, Results, Discussion
- FACT: A "Final" entry appears in week 11 (7-Dec) in the draft column only
- FACT: Each section spans 3 weeks: draft, then review, then feedback
- FACT: The Intro draft is due week 3 (12-Oct), review week 4 (19-Oct),
  feedback week 5 (26-Oct)
- FACT: Methods draft is due week 5 (26-Oct), review week 6 (2-Nov),
  feedback week 7 (9-Nov)
- FACT: Results draft is due week 7 (9-Nov), review week 8 (16-Nov),
  feedback week 9 (23-Nov)
- FACT: Discussion draft is due week 9 (23-Nov), review week 10 (30-Nov)
- FACT: Discussion feedback does NOT appear in the table
- FACT: "Final" appears only in the draft column of week 11
- FACT: Sections overlap: weeks 5 and 7 have both a draft and feedback due
- FACT: All deadlines are at 9pm (per column header "due @ 9pm")

### Hallucination Risks [-> Correctness]

- RISK: Assuming "SWORD" stands for a specific acronym
  REALITY: The table only shows "SWORD Deadlines" as the title. Without
  additional context, SWORD likely refers to a course assignment framework
  (possibly "Scientific Writing Organized by Research Drafts" or similar),
  but the acronym is not expanded in the image.
- RISK: Stating that Discussion feedback appears in week 11
  REALITY: Week 11 shows "Final" in the draft column only. There is no
  Discussion feedback entry visible in the table.
- RISK: Describing colors inaccurately due to JPEG compression
  REALITY: The JPG compression may slightly alter perceived colors. The
  color categories are clearly distinguishable but exact hex values should
  be considered approximate.
- RISK: Assuming the course is in a specific year
  REALITY: No year is shown. The dates (12-Oct through 7-Dec) indicate a
  fall semester but the specific year is not identifiable.
- RISK: Confusing "review" with "revision"
  REALITY: The column is labeled "review" not "revision" -- these are peer
  review deadlines, not revision deadlines.

### Detail Inventory [-> Information Recovery]

- Title: "SWORD Deadlines" bold, centered, black text
- Header row: gray background, bold text, 5 columns
- Cell borders: thin black lines separating all cells
- Date format: D-Mon (e.g., "12-Oct", "2-Nov", "7-Dec")
- Phase colors: green (draft), blue (review), pink/red (feedback),
  salmon/red (Final)
- "Final" text: bold red font on salmon/red background (distinct from other
  entries which use black text on pastel backgrounds)
- Empty cells: white, no text
- Week column: single or double digit numbers (3-11)
- Font: sans-serif, medium size, black (except Final)
- Clean rendering, standard table layout
- No footnotes, legends, or additional annotations

### Domain Context [-> Retrieval Value]

This timetable is from a university course (source URL:
courses.washington.edu/fish340) implementing the SWORD (Scaffolded Writing
and Rewriting in the Discipline) framework for teaching scientific writing.

The SWORD process structures paper writing into iterative cycles:
1. **Draft** -- student writes a section of their paper
2. **Review** -- peers review the draft and provide feedback
3. **Feedback** -- student receives and processes peer feedback

Four standard scientific paper sections (Introduction, Methods, Results,
Discussion) are each cycled through this draft-review-feedback process over
3 weeks. The cycles overlap: while one section is being reviewed, the next
section's draft is due. The Final paper is due in week 11 after all sections
have been through peer review.

This is from FISH 340, a University of Washington fisheries/biology course.
The 9pm deadline is typical of online submission systems.

### Search Keywords [-> Retrieval Value]

SWORD, timetable, deadlines, peer review, scientific writing, draft, review,
feedback, course schedule, color-coded, university, FISH 340, University of
Washington, Introduction, Methods, Results, Discussion, final paper

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A colorful schedule table" -- no title, no section names, no dates. Or: misidentifies color mapping (says green=review when green=draft). Or: states Discussion feedback appears in week 11 when it is absent. All text is labeled; fabricating a date or section name triggers the hallucination cap. | Title "SWORD Deadlines" correct, 4 sections named, weeks 3-11 and date range correct, 3-week cycle identified, Final noted in week 11. Minor error: gets one date wrong or misses overlap weeks (5 and 7 have both draft and feedback due). | All 5 column headers exact. All 9 rows with correct week numbers, dates, and section placements. Color-to-phase mapping correct (green=draft, blue=review, pink=feedback). 3-week cycle accurate. Overlap weeks identified. Discussion feedback correctly noted as absent. Final's distinct styling (red text, red bg) noted. No fabricated content. |
| Information Recovery | Identifies as a schedule table. May name 1-2 sections. No dates, no week numbers, no color coding explained. A search for "SWORD Methods draft deadline" or "FISH 340 peer review" would not match. | All 4 sections and Final named, week-to-date mapping present, color coding described. 3-week cycle captured. "Intro review week 4" would match. May miss overlapping deadlines or absent Discussion feedback. | Complete recovery: all sections with exact week/date/phase assignments. Overlap pattern documented (wk5: Methods draft + Intro feedback; wk7: Results draft + Methods feedback). Discussion feedback absence noted. Color coding fully described. Any deadline visible in the table is findable -- parity principle met. |
| Retrieval Value | "A class assignment schedule" -- no domain vocabulary, not self-contained. Cannot understand SWORD, the peer review structure, or course context. Would not surface for "peer review schedule" or "scientific writing framework". | Identifies as a UW course SWORD peer review schedule. 4 sections cycle through draft-review-feedback. Partially self-contained but doesn't explain the SWORD framework or why cycles overlap. | Natural prose explaining the SWORD peer review framework: each section gets a draft-review-feedback cycle, cycles overlap so students work on multiple sections simultaneously. Domain vocabulary embedded (SWORD, peer review, scientific writing). Course context noted (UW FISH 340). Self-contained. Findable by "SWORD deadlines", "peer review schedule", or "scientific writing timetable". |

# Image Analysis: Doc 25 -- 25_va_tiu_clinical_manual.docx

**Document:** `25_va_tiu_clinical_manual.docx`
**Format:** DOCX
**Source:** https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiutm.docx
**Category:** multi-image
**Images:** 13
**Document context:** VA CPRS Text Integration Utility (TIU) clinical
software manual with 13 content screenshots showing application windows,
dialog boxes, toolbar captures, and clinical data entry forms. 6 decorative
images (5 small icons + 1 VA seal/emblem) to filter.

**Eval subset:** 4 of 13 content images

<br><br>

## doc25-R08 -- NTRT New Term Request Form in Internet Explorer

**Content type:** screenshot
**Annotation difficulty:** Medium

### Visual Inventory

Screenshot of the NTRT (New Term Rapid Turnaround) web application displayed in
Microsoft Internet Explorer. The window shows a "New Term Request Form" for
requesting new clinical terminology entries. The interface has a dark blue header
with VistA branding, a red navigation bar, a left sidebar with navigation links,
and a main content area containing a form with dropdown fields and a text area.

- **Window chrome:** Title bar reads "NTRT - Microsoft Internet Explorer". Menu
  bar: File, Edit, View, Favorites, Tools, Help. IE toolbar with Back button,
  Search, Favorites, and standard IE6-era icons.
- **Application header:** VistA logo (blue trapezoid shape) at top-left with
  text "VHA OI - Health Systems Design & Development". Dark blue banner with
  "NTRT" in large bold white text and "New Term Rapid Turnaround" in smaller
  white text. Red navigation bar below with links: "Home", "Contact Us",
  "Log Off".
- **Left sidebar:** Two sections with bullet-pointed blue links:
  - "Request" heading (red text): Allergy, Clinical Doc Title *, Vitals, Search
  - "Admin" heading (red text): New User, Edit User
  - VA Department seal (circular emblem) at bottom of sidebar
- **Main content area:** White background form titled "New Term Request Form"
  with "<< Back" link at top-right and "Help" button. Five labeled dropdown
  fields and one text area, all in a centered form layout.
- **Footer:** Row of blue links and a "Reviewed/Updated" date.

### Verifiable Facts

- Window title: "NTRT - Microsoft Internet Explorer"
- Menu bar items: File, Edit, View, Favorites, Tools, Help
- Header text: "NTRT" (large bold) and "New Term Rapid Turnaround" (smaller)
- VistA logo subtitle: "VHA OI - Health Systems Design & Development"
- Red nav bar links: "Home", "Contact Us", "Log Off"
- Left sidebar "Request" links: Allergy, Clinical Doc Title *, Vitals, Search
- Left sidebar "Admin" links: New User, Edit User
- Form title: "New Term Request Form"
- Note below title: "* required field"
- Form fields (all dropdown selectors, all showing "UNASSIGNED"):
  1. SUBJECT MATTER DOMAIN (wide dropdown)
  2. ROLE (narrow dropdown)
  3. SETTING (narrow dropdown)
  4. SERVICE (wide dropdown)
  5. * DOCUMENT TYPE (medium dropdown, asterisk indicates required)
- COMMENTS: empty multi-line text area with vertical scrollbar
- "Submit" button: red background, white text, centered below the form
- "Help" button: gray, positioned at top-right of form area
- "<< Back" link: positioned at far top-right of main content
- Footer links: VA Home Page, OI Home Page, SD&D Home Page, Site Map, Terms of
  Use, Disclaimer, Privacy Statement
- Footer date: "Reviewed/Updated: August 14th, 2006"
- VA Department of Veterans Affairs seal visible in lower-left sidebar

### Hallucination Risks

- **Dropdown values:** All dropdowns show "UNASSIGNED" -- an annotator might
  invent specific option values that would appear in the dropdown lists, or
  describe selected clinical terms that are not visible.
- **CPRS vs NTRT:** The document is a CPRS TIU manual, but this specific
  screenshot shows the NTRT web application (a related but separate system).
  An annotator might describe this as "the main CPRS interface" when it is
  actually a terminology request tool.
- **VistA version:** The VistA logo is visible but no version number is shown.
  An annotator might assign a specific VistA version based on general knowledge.
- **IE version:** The toolbar appearance suggests IE6 or IE7, but the exact
  version is not labeled. An annotator might state a precise version.
- **Form field widths:** The SUBJECT MATTER DOMAIN and SERVICE dropdowns are
  visually wider than ROLE, SETTING, and DOCUMENT TYPE, but this is a layout
  detail, not functional difference. An annotator might infer meaning from the
  width differences.

### Detail Inventory

- **Window chrome details:**
  - Standard IE title bar with blue gradient (Windows XP-era styling)
  - IE toolbar: green Back arrow, grayed-out Forward arrow, Search magnifying
    glass icon, yellow star Favorites icon, media/print/mail icons
  - Address bar not visible (may be hidden)
- **VistA logo:** Blue trapezoid/parallelogram shape with "VistA" in white
  italic text with a red swoosh/checkmark; subtitle text below in small white
  font
- **Color scheme:**
  - Header: dark blue (#003366 or similar)
  - Navigation bar: bright red
  - Sidebar headings: red text
  - Sidebar links: blue text with bullet points
  - Form labels: dark navy/black, bold, right-aligned
  - Dropdown borders: blue/dark outlines
  - Submit button: red with white "Submit" text
  - Footer links: blue
  - Background: white main content, light gray sidebar area
- **Form layout:** Labels right-aligned in left column, form controls
  left-aligned in right column; consistent vertical spacing between fields
- **VA seal:** Circular emblem with eagle, flags, and "DEPARTMENT OF VETERANS
  AFFAIRS / UNITED STATES OF AMERICA" text -- same seal as the document cover
  page image (doc25-R01, now reclassified as decorative)
- **Footer styling:** Small font, links separated by spaces, date in
  monospace-like font

### Domain Context

- NTRT (New Term Rapid Turnaround) is a web-based tool for requesting additions
  to the VA's clinical terminology standardization system
- The form allows clinicians to request new document types, roles, settings, and
  subject matter domains for use in TIU (Text Integration Utility) clinical
  notes
- This screenshot appears in the VA CPRS TIU clinical manual, likely in a
  section about how to request new document definition terms
- VistA (Veterans Health Information Systems and Technology Architecture) is the
  VA's comprehensive health information system
- CPRS (Computerized Patient Record System) is the VistA user interface that
  clinicians interact with
- The "Reviewed/Updated: August 14th, 2006" date places this screenshot in the
  mid-2000s era of VA health IT
- The asterisk on "DOCUMENT TYPE" and "Clinical Doc Title *" in the sidebar
  suggests these are required fields for term requests

### Search Keywords

NTRT, New Term Rapid Turnaround, VistA, CPRS, TIU, clinical terminology,
VA, Veterans Affairs, Internet Explorer, web form, dropdown, document type,
subject matter domain, clinical documentation, health information system,
term request

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A screenshot of a website with a form" -- no application name, no field labels, no dropdown values. Or: describes this as "the CPRS interface" (it is NTRT, a separate web application). Inventing dropdown option values beyond "UNASSIGNED" triggers the hallucination cap -- all 5 dropdowns visibly show "UNASSIGNED" and no other values are readable. Stating an IE version number (e.g., "IE6") is a fabrication -- the toolbar style suggests IE6-era but no version is labeled. | NTRT New Term Request Form in Internet Explorer identified. 5 dropdown fields with correct labels, all showing UNASSIGNED. Red Submit button, VistA branding with logo, sidebar with Request and Admin sections, red nav bar with Home/Contact Us/Log Off. Footer date present. May miss the "* required field" note, the DOCUMENT TYPE asterisk, or the COMMENTS text area. | Window title "NTRT - Microsoft Internet Explorer" exact. All 5 dropdown labels exact (SUBJECT MATTER DOMAIN, ROLE, SETTING, SERVICE, * DOCUMENT TYPE), all showing UNASSIGNED. COMMENTS text area with scrollbar. Help button and "<< Back" link positions noted. VistA logo with "VHA OI - Health Systems Design & Development" subtitle. Red nav bar links (Home, Contact Us, Log Off). Sidebar links fully enumerated (Request: Allergy, Clinical Doc Title *, Vitals, Search; Admin: New User, Edit User). VA seal in sidebar. Footer: 7 links + "Reviewed/Updated: August 14th, 2006". No fabricated dropdown values or IE version. |
| Information Recovery | Identifies as a web form with fields. A search for "NTRT" or "SUBJECT MATTER DOMAIN" or "August 14th, 2006" would not match. The application identity, form field labels, and sidebar navigation structure are all missing. | All 5 field labels recovered, NTRT title and "New Term Rapid Turnaround" identified, VistA branding noted, sidebar sections with links listed, footer date present. "NTRT term request form" would match. May miss the dropdown width differences (SUBJECT MATTER DOMAIN and SERVICE wider), the "* required field" note, or individual footer link text. | Complete recovery: window chrome (title, menu bar items, IE toolbar), VistA header block (logo, subtitle, NTRT title, red nav bar with 3 links), sidebar (2 sections with all 6 links, VA seal), form (title, required field note, all 5 dropdowns with widths, COMMENTS text area, Help button, Back link, Submit button), footer (7 links, date). Any text element visible in the screenshot is findable -- parity principle met. |
| Retrieval Value | "A VA government form" -- no system name, not self-contained. Would not surface for "NTRT term request" or "VistA clinical terminology" or "New Term Rapid Turnaround." | "NTRT terminology request form from the VA CPRS TIU manual; used for requesting new clinical document types in VistA." Searchable terms present but doesn't explain NTRT's role in clinical terminology standardization or the form's relationship to TIU document definitions. | Natural prose identifying the NTRT (New Term Rapid Turnaround) web application for requesting clinical terminology additions. Explains relationship to TIU/CPRS/VistA: term requests here feed into document type definitions available in CPRS clinical notes. Notes mid-2000s VA health IT context from footer date (2006). Domain vocabulary embedded (VistA, NTRT, TIU, clinical terminology, VHA OI). Self-contained. Findable by "NTRT term request form" or "VistA clinical terminology management." |

<br><br>

## doc25-R02 -- CPRS form letter example with annotation circles

**Content type:** screenshot
**Annotation difficulty:** Medium

### Visual Inventory

Screenshot of the VistA CPRS (Computerized Patient Record System) desktop
application showing a clinical note in form letter format. The window has a
patient banner at the top, a left sidebar with a note tree view, and a main
content area displaying the letter text. Three hand-drawn red oval annotation
circles highlight specific parts of the letter (address block, closing, and
confidentiality footer). The application runs in a Windows XP-era window with
standard chrome.

- **Window title bar:** "VistA CPRS in use by:"
- **Menu bar:** File, Edit, View, Action, Options, Tools, Help
- **Patient banner:** Patient demographics, provider info, and action buttons
  across the top
- **Left sidebar:** "Last 100 Signed Notes" tree with one selected item
- **Main content:** Note metadata header followed by a formatted letter with
  VA Medical Center address, body text, closing, and confidentiality notice
- **Red annotation circles:** Three hand-drawn ovals highlighting key parts of
  the form letter template

### Verifiable Facts

- Window title: "VistA CPRS in use by:"
- Menu bar: File, Edit, View, Action, Options, Tools, Help
- **Patient banner fields:**
  - Patient name: CPRSPATIENT,ONE
  - SSN: 000-00-0001
  - DOB: Jan 01,1945 (62)
  - Location: PBS1 Mar 09,07 09:14
  - Provider: CPRSPROVIDER,SEVEN
  - Primary Care Team Unassigned
  - Buttons (right side): Flag, Remote Data, ? (help), No Postings
- **Left sidebar:**
  - Heading: "Last 100 Signed Notes"
  - Tree items: "All unsigned notes for"
  - Selected (blue highlight): "Aug 15,07 FORM LETTER EXAMPLE, E..."
  - Below: "No Matching Documents Found"
- **Visit bar:** "Visit: 03/09/07 FORM LETTER EXAMPLE, EMERGENCY ROOM,"
  and "(Aug 15,07@13:31)" at right
- **Note metadata (monospaced block at top of content area):**
  - LOCAL TITLE: FORM LETTER EXAMPLE
  - DATE OF NOTE: AUG 15, 2007@13:31
  - ENTRY DATE: AUG 15, 2007@13:31:25
  - AUTHOR: CPRSPROVIDER,TEN
  - EXP COSIGNER: (empty)
  - URGENCY: (empty)
  - STATUS: UNSIGNED
- **Letter address block (circled in red):**
  - "Department of Veteran Affairs Medical Center"
  - "12345 Any Street"
  - "Salt Lake City, Utah 84207"
- Date line: "AUG 15, 2007"
- Salutation: "Dear Cprspatient:"
- Body text: paragraph about the Church-Turing thesis (placeholder content about
  computers, versatility, and computational equivalence)
- **Closing (circled in red):** "Sincerely," followed by "CPRS Provider"
- **Confidentiality footer (circled in red):** "Confidential Information" /
  "For Official Use Only"
- Bottom of window: horizontal scrollbar, "/ Templates" tab, "Encounter" label
  partially visible
- Three red hand-drawn oval annotations are NOT part of the CPRS interface --
  they are editorial markup added to the screenshot for the manual

### Hallucination Risks

- **Red circles as UI elements:** The three red annotation ovals are hand-drawn
  editorial markup on the screenshot, not CPRS interface elements. An annotator
  might describe them as error indicators, selection highlights, or validation
  markers within the application itself.
- **Body text as clinical content:** The letter body contains a paragraph about
  the Church-Turing thesis -- this is clearly placeholder/example text, not
  actual clinical content. An annotator might describe it as medical text or
  try to interpret it as having clinical significance.
- **Patient data as real:** All patient data is fictional test data
  (CPRSPATIENT,ONE, 000-00-0001, CPRSPROVIDER,SEVEN). An annotator might not
  note this distinction or might treat it as real PHI.
- **Complete window assumption:** The bottom of the window shows partial UI
  elements (Templates tab, Encounter label) suggesting more tabs/content below
  the visible area. An annotator might describe only what is visible as the
  complete interface.
- **Address accuracy:** The address reads "Department of Veteran Affairs" (not
  "Veterans") -- this may be a deliberate simplification for the example or a
  typo. An annotator might "correct" it to "Veterans Affairs" when the
  screenshot actually shows "Veteran Affairs".

### Detail Inventory

- **Window chrome:** Windows XP-era title bar with blue gradient, standard
  minimize/maximize/close buttons (squares and X) at top-right
- **Patient banner layout:**
  - Left section: patient name on first line, SSN and DOB on second line
  - Center section: location code and date/time on first line, "Provider:"
    with name on second line
  - Right-center: "Primary Care Team Unassigned"
  - Right buttons: "Flag" (with flag icon), "Remote Data", "?" (yellow circle),
    "No Postings"
- **Left sidebar styling:** White background, tree view with expand/collapse
  icons, selected item in blue highlight bar, folder icons next to entries
- **Note metadata:** Monospaced font in a gray/beige header block; field labels
  right-aligned (LOCAL TITLE:, DATE OF NOTE:, etc.), values left-aligned
- **Letter formatting:** Proportional serif-like font for the letter body;
  address block centered; date right-aligned; body text left-justified with
  full justification; closing indented
- **Red annotation circles:**
  - Circle 1 (largest): surrounds the VA Medical Center address block, roughly
    centered in the upper portion of the letter
  - Circle 2 (medium): surrounds "Sincerely, / CPRS Provider" at the left side
  - Circle 3 (medium): surrounds "Confidential Information / For Official Use
    Only" at the lower-right
  - Style: red, hand-drawn appearance (not perfectly geometric), approximately
    2-3px stroke width
- **Color scheme:** Dark blue/navy patient banner background with white text;
  white sidebar and content area; gray metadata header; black letter text
- **Bottom area:** Gray scrollbar, "/ Templates" tab with sheet icon,
  "Encounter" text partially cut off at bottom edge

### Domain Context

- This screenshot demonstrates the TIU Form Letter template functionality in
  CPRS, showing how clinicians can create standardized letters using templates
  that auto-populate with patient and facility information
- The red annotation circles in the manual highlight the three template-
  generated sections of the letter: the facility address block, the provider
  signature line, and the confidentiality notice -- these are the parts that
  TIU templates automatically insert
- CPRS is the primary clinical interface for the VA's VistA health information
  system, used at VA Medical Centers nationwide
- The fictional test data (CPRSPATIENT,ONE, 000-00-0001) follows VA's standard
  test patient naming convention for training and documentation
- The Church-Turing thesis body text is placeholder content used in the example
  to represent where the actual letter content would go
- STATUS: UNSIGNED indicates this note has not yet been electronically signed
  by the provider -- a required step in VA clinical documentation workflow
- The "Salt Lake City, Utah 84207" address corresponds to the VA Salt Lake City
  Health Care System, suggesting this manual was produced there

### Search Keywords

CPRS, VistA, TIU, form letter, clinical note, template, VA Medical Center,
UNSIGNED, electronic signature, patient record, clinical documentation,
CPRSPROVIDER, annotation circles, confidential information, health information
system, Salt Lake City

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A screenshot of a medical records program with some red circles" -- no system name, no patient data, no note metadata, no letter content. Or: describes the 3 red annotation circles as application UI elements (error indicators, selection highlights) rather than editorial markup added to the screenshot for the manual. "Correcting" the address to "Veterans Affairs" when the screenshot visibly reads "Veteran Affairs" is a value error. Fabricating note metadata values not shown in the monospaced header triggers the hallucination cap. | VistA CPRS window identified with FORM LETTER EXAMPLE note dated Aug 15, 2007. Patient CPRSPATIENT,ONE and provider noted. Three red annotation circles correctly identified as editorial markup highlighting address, closing, and confidentiality footer. Address text, Church-Turing thesis placeholder body, STATUS: UNSIGNED. May miss exact SSN (000-00-0001) or some metadata fields. | Window title "VistA CPRS in use by:" exact. All patient banner fields (CPRSPATIENT,ONE, 000-00-0001, Jan 01,1945 (62), PBS1, CPRSPROVIDER,SEVEN). All 7 note metadata fields with values (LOCAL TITLE, DATE OF NOTE, ENTRY DATE, AUTHOR, EXP COSIGNER, URGENCY, STATUS: UNSIGNED). Address block verbatim including "Veteran" (not "Veterans"), "12345 Any Street", "Salt Lake City, Utah 84207". Church-Turing thesis placeholder identified. Red circles correctly described as editorial markup with positions (address, closing, confidentiality). No fabricated metadata values. |
| Information Recovery | Identifies as a medical application with a letter. A search for "CPRSPATIENT,ONE" or "FORM LETTER EXAMPLE" or "Church-Turing" would not match. The patient banner, note metadata, and letter structure are invisible. | Window title, patient name, note title and date, address block, closing and confidentiality text recovered. "CPRS form letter template" would match. May miss sidebar tree text ("Last 100 Signed Notes"), visit bar details, individual patient banner buttons, or the Templates/Encounter tabs at bottom. | Complete recovery: window chrome (title, menu bar with 7 items, XP-era styling), patient banner (all fields and 4 right-side buttons), sidebar (heading, tree items with selection state), visit bar, note metadata (all 7 field-value pairs), letter content (address block, date line, salutation, body, closing, confidentiality footer), 3 red circles with relative positions and sizes, bottom area (scrollbar, Templates tab, Encounter label). Any text element visible in the screenshot is findable -- parity principle met. |
| Retrieval Value | "A VA hospital program screenshot" -- no workflow context, not self-contained. Would not surface for "TIU form letter template" or "CPRS clinical note" or "template auto-population." | "CPRS TIU form letter template demonstration from the VA clinical manual; red circles highlight auto-populated template sections." Searchable terms but doesn't explain what the three circled sections represent (template-generated vs user-authored content) or why this screenshot matters in the manual. | Natural prose explaining CPRS TIU form letter template functionality. Identifies the 3 circled elements as template-generated sections (facility address, provider signature, confidentiality notice) vs user-authored content (the Church-Turing placeholder body). Notes UNSIGNED status as a workflow step (electronic signature required). Test patient naming convention (CPRSPATIENT, 000-00-0001). Salt Lake City VAMC context. Domain vocabulary embedded (CPRS, TIU, VistA, form letter template, electronic signature). Self-contained. Findable by "CPRS form letter example" or "TIU template auto-populated sections." |

<br><br>

## doc25-R07 -- NTRT welcome and login page

**Content type:** screenshot
**Annotation difficulty:** Medium

### Visual Inventory

Screenshot of the NTRT (New Term Rapid Turnaround) web application welcome and
login page displayed in Microsoft Internet Explorer. The page has a prominent VA
Department seal banner at the top, the NTRT acronym and expanded name in the
upper-left corner, a welcome message with introductory text in the center, and a
login form with username and password fields in the lower-left. The overall
layout uses a dark blue and red color scheme consistent with VA branding.

- **Window title bar:** "VA NTRT - New Term Rapid Turnaround - Microsoft
  Internet Explorer"
- **Menu bar:** File, Edit, View, Favorites, Tools, Help
- **IE toolbar:** Back/Forward arrows, Search, Favorites, standard IE icons
- **Upper-left block:** "NTRT" in large bold dark blue, followed by the words
  "New", "Term", "Rapid", "Turnaround" stacked vertically, each on its own
  line, with a horizontal rule beneath
- **Banner area:** Large VA Department of Veterans Affairs circular seal
  centered, with a red and dark blue sweeping wave/banner design behind it
- **Welcome section:** Heading and two lines of introductory text
- **Login form:** Two labeled fields (Login Name, Password) and a Go button in
  the lower-left corner

### Verifiable Facts

- Window title: "VA NTRT - New Term Rapid Turnaround - Microsoft Internet
  Explorer"
- Menu bar: File, Edit, View, Favorites, Tools, Help
- Upper-left text block:
  - "NTRT" in large bold dark blue serif-like font
  - Below: "New" / "Term" / "Rapid" / "Turnaround" (each word on its own line,
    bold dark blue, smaller than NTRT)
  - Horizontal rule separating this block from content below
- Banner: VA Department of Veterans Affairs seal (eagle, flags, stars, rope
  border with "DEPARTMENT OF VETERANS AFFAIRS / UNITED STATES OF AMERICA")
  centered over a red and blue curved banner/wave graphic
- Welcome heading: "Welcome to NTRT"
- First paragraph: "Welcome to the VHA New Term Rapid Turnaround Request (NTRT)
  Web Page."
- Second paragraph (partially cut off at right edge): "This site was developed
  to facilitate requests for new terms from VHA users to the Enterprise
  Refer..." (truncated)
- Login form:
  - "Login Name" label in blue bold text
  - Text input field containing "myaccount"
  - "Password" label in blue bold text
  - Empty text input field
  - "Go" button (small, gray, to the right of the password field)
- Background: white main content area, light beige/gray behind the IE toolbar

### Hallucination Risks

- **Truncated text:** The second paragraph is cut off at the right edge with
  "Enterprise Refer..." -- an annotator might complete this as "Enterprise
  Reference" or "Enterprise Referral" based on context, but the full text is
  not visible in the crop.
- **Login credentials:** The Login Name field shows "myaccount" which is example
  placeholder text. An annotator might describe it as an actual username or
  miss that it is pre-filled example text shown for documentation purposes.
- **VA seal details:** The seal is moderately sized and some fine text on it may
  not be fully legible. An annotator might describe seal details from general
  knowledge of the VA emblem rather than from what is readable at this
  resolution.
- **Page completeness:** The screenshot appears to cut off content at the right
  and bottom edges. An annotator might describe the visible portion as the
  complete page layout.
- **NTRT vs CPRS:** This is the NTRT web application login page, not CPRS
  itself. An annotator familiar with the document context might incorrectly
  describe this as a CPRS login screen.

### Detail Inventory

- **Window chrome:** Windows XP-era IE title bar with blue gradient; standard
  minimize/maximize/close buttons; IE toolbar with green Back arrow, grayed
  Forward arrow, Search magnifying glass, yellow star Favorites
- **NTRT text block:**
  - "NTRT" approximately 36pt bold dark navy serif font
  - Stacked words approximately 14-16pt bold dark navy
  - Thin horizontal rule below the stacked text, spanning roughly the width of
    the text block
- **Banner design:**
  - VA seal approximately 150px diameter, positioned center-left of the banner
  - Red area sweeps from behind the seal to the right edge, tapering to a point
  - Dark blue area curves below and to the left of the seal
  - The overall effect is a patriotic wave/ribbon motif
- **Welcome text:**
  - "Welcome to NTRT" in approximately 18pt dark serif font
  - Body text in approximately 12pt dark serif font
  - Text is left-aligned in the center-right portion of the page
- **Login form:**
  - Positioned at bottom-left corner of the visible page
  - "Login Name" and "Password" labels in blue bold sans-serif
  - Text input fields: white with thin border, approximately 100px wide
  - "myaccount" in the Login Name field appears as typed text (dark, sans-serif)
  - "Go" button: small gray rectangular button with "Go" text
  - No "Remember me" checkbox or "Forgot password" link visible
- **Color palette:**
  - Dark navy blue: NTRT text, page background elements
  - Red: banner wave, accent color
  - Blue: login form labels, hyperlink-style text
  - White: main content background
  - Gray/beige: toolbar area background

### Domain Context

- This is the login page for the NTRT (New Term Rapid Turnaround) system, a
  web-based tool for VA clinical staff to request additions to VistA's
  standardized terminology
- The screenshot appears in the VA CPRS TIU manual to show users how to access
  the NTRT system for requesting new document types and clinical terms
- "Enterprise Refer..." likely continues as "Enterprise Reference" referring to
  the VA Enterprise Reference Terminology, the standardized vocabulary system
  used across VHA facilities
- The "myaccount" placeholder in the Login Name field is example text shown in
  the manual to illustrate where users would enter their credentials
- NTRT is separate from CPRS but supports TIU by allowing clinical staff to
  request new document definition terms that then become available in the CPRS
  clinical note creation workflow
- The page design and IE6/XP-era styling is consistent with mid-2000s VA web
  applications

### Search Keywords

NTRT, New Term Rapid Turnaround, VistA, VHA, login page, welcome page,
VA seal, Department of Veterans Affairs, Enterprise Reference Terminology,
clinical terminology, Internet Explorer, web application, CPRS, TIU,
authentication

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A government website login page" -- no application name, no welcome text, no login field contents. Or: describes this as "the CPRS login screen" (it is NTRT, a separate web application). Completing the truncated text "Enterprise Refer..." as a full phrase (e.g., "Enterprise Reference Terminology") without noting the truncation is a fabrication -- only "Enterprise Refer" is visible. Inventing an IE version number or describing "myaccount" as a real username triggers the hallucination cap. | NTRT welcome page in Internet Explorer identified. Window title correct, VA seal banner described, "Welcome to NTRT" heading and first paragraph quoted, login form with "myaccount" and Go button noted. May miss the stacked NTRT/New/Term/Rapid/Turnaround layout, the second paragraph truncation, or the red/blue wave banner design. | Window title "VA NTRT - New Term Rapid Turnaround - Microsoft Internet Explorer" exact. NTRT stacked text block (acronym + 4 stacked words + horizontal rule). VA seal on red/blue wave banner. Welcome heading quoted, first paragraph verbatim, second paragraph with truncation point noted ("Enterprise Refer..."). Login form: "myaccount" pre-filled in Login Name, empty Password, Go button. Page cut-off at right and bottom edges noted. No fabricated IE version or completed truncated text. |
| Information Recovery | Identifies as a login page with a government seal. A search for "NTRT" or "New Term Rapid Turnaround" or "myaccount" would not match. The application identity, welcome text, and login form structure are invisible. | Window title, NTRT branding, VA seal, welcome text, and login form all recovered. "NTRT welcome login page" would match. May miss the stacked word layout details, the horizontal rule, the red/blue wave design, or the right-edge truncation of the second paragraph. | Complete recovery: window chrome (title, menu bar, IE toolbar), NTRT text block (bold acronym, 4 stacked bold words, horizontal rule), banner (VA seal centered on red/blue curved wave design), welcome section (heading + 2 paragraphs with truncation noted), login form (both labeled fields with contents, Go button position). Color palette documented. Page boundaries noted (right and bottom cut-off). Any text element visible in the screenshot is findable -- parity principle met. |
| Retrieval Value | "A VA website screenshot from a manual" -- no system name, not self-contained. Would not surface for "NTRT login" or "clinical terminology request system" or "VHA New Term Rapid Turnaround." | "NTRT login page from the VA CPRS TIU manual; shows how clinical staff access the terminology request system." Searchable but doesn't explain NTRT's role or the Enterprise Reference Terminology context. | Natural prose identifying the NTRT (New Term Rapid Turnaround) welcome and login page. Explains NTRT as a web tool for VA clinical staff to request terminology additions that feed into VistA's standardized vocabulary. Notes "Enterprise Refer..." likely refers to Enterprise Reference Terminology. Identifies "myaccount" as documentation placeholder, not a real credential. Mid-2000s VA web design (IE6-era). Domain vocabulary embedded (NTRT, VistA, TIU, VHA, Enterprise Reference Terminology). Self-contained. Findable by "NTRT login page" or "VA clinical terminology request access." |

<br><br>

## doc25-R19 -- Terminal emulator display settings dialog

**Content type:** screenshot
**Annotation difficulty:** Medium

### Visual Inventory

Screenshot of a "Set Up Display Settings" dialog window from a terminal
emulator application (likely Attachmate or similar VistA terminal client). The
dialog is organized into 5 labeled sections (Display Memory, Scrolling, Control
Characters, Mouse, Dimensions) with a left sidebar providing "Jump To"
navigation for each section and a "See Also" section with related settings
links. The window has a breadcrumb navigation bar, a main scrollable settings
area with form controls (text fields, checkboxes, radio buttons, dropdowns),
and OK/Cancel buttons at the bottom.

- **Window title bar:** "Display - BKOUT1.rdox"
- **Breadcrumb bar:** Documents >> BKOUT1.rdox >> Terminal Configuration >>
  Display
- **Left sidebar:** "Jump To" section with 6 links and "See Also" section with
  4 links
- **Main content:** 5 settings sections with various form controls
- **Bottom buttons:** OK, Cancel

### Verifiable Facts

- Window title: "Display - BKOUT1.rdox"
- Breadcrumb: Documents >> BKOUT1.rdox >> Terminal Configuration >> Display
- Search box visible in the breadcrumb/toolbar area (empty)
- Navigation buttons: Back, Forward, and breadcrumb path in toolbar
- **Left sidebar "Jump To" links:**
  1. Display Memory
  2. Scrolling
  3. Control Characters
  4. Mouse
  5. Dimensions
  6. Options
- **Left sidebar "See Also" links:**
  1. Select Terminal Type
  2. Set Up Safeguards
  3. Set Up VBA References
  4. Settings for VT
- **Main heading:** "Set Up Display Settings" with a small blue icon to its left
- **Section 1 -- Display Memory:**
  - "Memory blocks (8K/block):" text field with value "500"
  - Checkbox (checked): "Enable scrollback"
  - Checkbox (unchecked): "Compress blank lines"
  - Checkbox (checked): "Save display before clearing"
  - Checkbox (unchecked): "Save from scrolling regions"
- **Section 2 -- Scrolling:**
  - Radio button (unselected): "Smooth scrolling"
  - Radio button (selected): "Jump scrolling"
  - "Jump scroll speed:" dropdown with value "2"
- **Section 3 -- Control Characters:**
  - Radio button (selected): "Interpret control characters"
  - Radio button (unselected): "Display control characters"
- **Section 4 -- Mouse:**
  - "Mouse cursor shape:" dropdown with value "I-Beam"
- **Section 5 -- Dimensions:**
  - "Number of rows:" text field with value "24"
  - "Number of characters per row:" text field with value "255"
- Bottom buttons: "OK" (default/blue-highlighted) and "Cancel" (gray), right-
  aligned
- Help button "?" visible in the title bar

### Hallucination Risks

- **Clinical documentation form:** The catalog describes this as "Full form:
  clinical documentation" but it is a terminal emulator display configuration
  dialog. An annotator might try to interpret these settings as clinical data
  entry fields or describe it as a patient-facing form.
- **Application identification:** The ".rdox" file extension and the UI style
  suggest Attachmate Reflection or a similar terminal emulator, but the exact
  product name is not visible. An annotator might state a specific product name
  with false confidence.
- **VBA References link:** "Set Up VBA References" in the See Also sidebar
  suggests this terminal emulator supports Visual Basic for Applications
  scripting. An annotator might misinterpret "VBA" as a clinical acronym.
- **Default vs configured values:** The current values (500 memory blocks, Jump
  scrolling at speed 2, 24 rows, 255 chars) may be defaults or may be
  custom-configured for VistA. An annotator might assert these are "standard
  VistA settings" without evidence.
- **Options section:** The "Options" link in Jump To suggests a 6th settings
  section exists below the visible area. An annotator might describe the
  visible content as the complete dialog.

### Detail Inventory

- **Window chrome:** Modern Windows (Vista/7-era) window frame with rounded
  title bar, minimize/maximize/close buttons, and "?" help button
- **Breadcrumb bar:** Uses ">>" separators between path segments; segments
  appear as clickable links; Search text field at the right end of the bar
- **Section headers:** Each section name (Display Memory, Scrolling, etc.)
  appears in blue text with a horizontal blue line extending to the right edge,
  creating a ruled section divider
- **Form control styling:**
  - Text fields: white with thin dark border, approximately 80-100px wide
  - Checkboxes: standard Windows checkbox style, square with checkmark when
    selected
  - Radio buttons: standard Windows radio button style, circle with filled dot
    when selected
  - Dropdowns: standard Windows dropdown with down-arrow button at right
  - "500" in the memory blocks field appears selected (highlighted/blue
    background)
- **Left sidebar styling:**
  - "Jump To" heading in dark blue/navy bold text
  - Links in blue, standard hyperlink style
  - "See Also" heading in dark blue/navy bold text
  - Links in blue, slightly smaller than Jump To links
  - Sidebar has a light gray/white background separated from the main content
- **Layout:** Left sidebar approximately 25% width, main content approximately
  75% width, scrollable
- **Section indentation:** Form controls are indented under their section
  headers, labels left-aligned with controls to their right
- **Color scheme:** White background, blue section headers and sidebar headings,
  blue hyperlinks, standard Windows form control colors
- **Dialog dimensions noted in catalog:** 686x851 pixels (portrait orientation,
  taller than wide)

### Domain Context

- This dialog appears in the VA CPRS TIU manual likely in a section about
  configuring the terminal emulator used to connect to VistA
- VistA historically uses character-based terminal interfaces accessed through
  terminal emulators; clinicians and IT staff configure display settings for
  optimal viewing of VistA screens
- The ".rdox" file extension and UI design are consistent with Attachmate
  Reflection, a widely used terminal emulator in VA facilities
- The "Settings for VT" link in See Also refers to VT (Virtual Terminal)
  emulation -- VistA traditionally uses VT100/VT220 terminal protocols
- Key settings for VistA use:
  - 24 rows is the standard VT100 terminal height
  - 255 characters per row is generous (VT100 standard is 80; 255 allows for
    wide VistA screens)
  - Jump scrolling at speed 2 provides responsive screen updates
  - 500 memory blocks (8K each = 4MB) provides substantial scrollback history
  - "Interpret control characters" is required for VT escape sequences to
    render correctly
- BKOUT1 in the filename may refer to a specific VistA connection profile or
  session configuration

### Search Keywords

terminal emulator, display settings, VistA, Attachmate, Reflection, VT100,
scrollback, memory blocks, jump scrolling, control characters, mouse cursor,
terminal configuration, CPRS, rdox, VBA, VHA, screen dimensions, rows,
characters per row

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A settings dialog with checkboxes and dropdowns" -- no application name, no field values, no section names. Or: describes this as a "clinical documentation form" or "patient data entry screen" (the catalog description is misleading; this is a terminal emulator configuration dialog). Inventing specific values for fields not shown (e.g., claiming an Options section has certain settings) triggers the hallucination cap -- only 5 sections are visible. Asserting these are "standard VistA settings" without evidence is a domain knowledge fabrication. | Terminal emulator display settings dialog (BKOUT1.rdox) identified with 5 sections. Key values correct: 500 memory blocks, Jump scrolling at speed 2, Interpret control characters selected, I-Beam mouse cursor, 24 rows x 255 characters. OK/Cancel buttons. May miss checkbox states for minor options (Compress blank lines unchecked, Save from scrolling regions unchecked) or sidebar link lists. | All field values exact: Memory blocks 500 (shown selected/highlighted), Enable scrollback checked, Compress blank lines unchecked, Save display before clearing checked, Save from scrolling regions unchecked. Smooth/Jump radio pair with Jump selected, speed 2. Interpret/Display radio pair with Interpret selected. I-Beam dropdown. 24 rows, 255 chars per row. Breadcrumb "Documents >> BKOUT1.rdox >> Terminal Configuration >> Display" verbatim. All Jump To links (6) and See Also links (4) enumerated. Help "?" in title bar. No fabricated settings values or product version. |
| Information Recovery | Identifies as a settings dialog with some fields. A search for "BKOUT1" or "memory blocks" or "jump scrolling" would not match. The 5-section structure, sidebar navigation, and breadcrumb path are invisible. | All 5 sections named with key values. Sidebar Jump To and See Also links listed. Window title and breadcrumb present. "Terminal emulator display configuration" would match. May miss individual checkbox labels, the "500" selection highlighting, the Search box in the breadcrumb bar, or OK as default/highlighted button. | Complete recovery: window chrome (title "Display - BKOUT1.rdox", "?" help button, Vista/7-era frame), breadcrumb (full path with ">>" separators and Search box), sidebar (Jump To: 6 links, See Also: 4 links including "Settings for VT"), all 5 sections (Display Memory with 4 checkboxes and states, Scrolling with 2 radios and dropdown, Control Characters with 2 radios, Mouse with dropdown, Dimensions with 2 text fields), bottom buttons (OK highlighted, Cancel gray). Blue ruled section headers noted. Any setting or label visible in the dialog is findable -- parity principle met. |
| Retrieval Value | "A Windows dialog box from a VA manual" -- no workflow context, not self-contained. Would not surface for "terminal emulator VistA configuration" or "VT100 display settings" or "Attachmate Reflection." | "Terminal emulator display configuration for VistA connection; 24-row VT terminal with 255-char width and jump scrolling." Searchable terms but doesn't explain why these settings matter for VistA or the .rdox file context. | Natural prose explaining this as a terminal emulator display settings dialog for VistA connections, likely Attachmate Reflection (identified by .rdox extension). Connects 24 rows to VT100 standard, explains 255 chars per row for wide VistA screens, notes Interpret control characters is required for VT escape sequences. 500 memory blocks (8K each = 4MB scrollback). BKOUT1 as connection profile. "Settings for VT" sidebar link confirms VT terminal emulation context. Domain vocabulary embedded (VistA, VT100, terminal emulator, scrollback, .rdox). Self-contained. Findable by "VistA terminal configuration" or "display settings BKOUT1." |

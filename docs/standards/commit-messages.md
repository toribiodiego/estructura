# Commit Messages

All commits must follow these standards for consistency and clarity. The prefix
table and message structure below are the same as konsillix -- estructura commits
should be indistinguishable in style from KVision commits.

For development workflow, see [Contributing Guide](../../CONTRIBUTING.md).

<br><br>

## Core Rules

- Use **exactly one** prefix from the table below (never combine, never omit)
- Write subject in **imperative mood** ("add" not "added" or "adds")
- Keep subject line **at most 72 characters** (hard limit)
- Focus commits on **one logical change** (split mixed concerns into separate
  commits)
- Explain **WHY** in the body, not HOW

<br><br>

## Commit Prefixes

| Prefix | When to use | Example |
|--------|-------------|---------|
| `feat:` | New user-facing functionality | `feat: add page-level annotation fallback for scanned PDFs` |
| `fix:` | Corrects broken behavior | `fix: prevent duplicate image anchors in TXT output` |
| `refactor:` | Restructures code without changing behavior | `refactor: extract annotation caching into separate module` |
| `perf:` | Improves performance measurably | `perf: switch to pypdfium2 backend for constant memory usage` |
| `test:` | Adds or modifies tests only | `test: add unit tests for DoclingRunner timeout handling` |
| `docs:` | Documentation changes only | `docs: update output contract with manifest schema` |
| `style:` | Formatting/linting only (no logic changes) | `style: apply consistent quote style in run_docling.py` |
| `build:` | Build system, CI, or packaging | `build: add Tesseract language packs to dev container` |
| `chore:` | Repo maintenance (deps, configs, cleanup) | `chore: bump google-genai from 1.2.0 to 1.3.0` |
| `wip:` | Incomplete work (squash before merge) | `wip: draft concurrent annotation (needs rate limiting)` |

<br><br>

## Message Structure

```text
<prefix> <imperative verb> <what changed>

<WHY this change was needed -- not HOW it was implemented>
<wrap lines at 72 characters>
```

<br><br>

## Worked Examples

**Feature -- adding pipeline capability:**

```text
feat: add page-level annotation fallback for scanned PDFs

Scanned documents produce zero crop images because Docling detects no
PictureItem regions. Fall back to annotating full page renders so
scanned PDFs still get descriptive captions.
```

**Fix -- correcting broken output:**

```text
fix: prevent duplicate image anchors in TXT output

When a page contains both raster and vector images, the TXT formatter
emitted the same anchor twice. Deduplicate by image ID before writing
anchors to the output file.
```

**Docs -- updating documentation after behavior change:**

```text
docs: update output contract with manifest schema

Add the manifest JSON schema that run_docling.py now emits alongside
Markdown/TXT output. Downstream consumers need the schema to validate
manifest files programmatically.
```

**Build -- modifying the development environment:**

```text
build: add Tesseract language packs to dev container

OCR accuracy tests for non-English fixtures require fra and deu
language data. Add them to the Dockerfile so the dev container
supports multilingual OCR out of the box.
```

<br><br>

## Common Mistakes

**Vague subjects:**

```text
fix: update code
refactor: improve things
docs: update docs
```

Write specific subjects instead:

```text
fix: handle missing GOOGLE_API_KEY gracefully
refactor: split annotation logic from output assembly
docs: add evaluation subset criteria to image catalog
```

**Mixing concerns:**

```text
feat: add rate limiting and fix typo in README and bump Pillow
```

Split into separate commits:

```text
feat: add rate limiting to annotation requests
docs: fix typo in runner protocol description
chore: bump Pillow from 10.2.0 to 10.3.0
```

**Describing HOW instead of WHY:**

```text
refactor: move function from file A to file B

Move annotate_images() from run_docling.py to annotation.py.
```

Explain WHY instead:

```text
refactor: extract annotation logic into dedicated module

run_docling.py has grown to 800 lines. Separating annotation
concerns makes the pipeline entry point easier to follow and
enables unit testing annotation logic independently.
```

<br><br>

## Before Committing

1. Verify prefix matches the change type
2. Check subject line is at most 72 characters
3. Confirm commit focuses on one logical change
4. Run Java tests: `cd src/estructura-java && mvn test`
5. Run a pipeline smoke test if `run_docling.py` changed

<br><br>

[Back to Contributing Guide](../../CONTRIBUTING.md)

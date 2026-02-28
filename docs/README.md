# Documentation

Reference documentation for the estructura image-aware document processing
pipeline. Covers output format contracts, inter-process protocols, sample
outputs, and project standards.

> **Quick links:** [Output Contract](./output-contract.md) ·
> [Runner Protocol](./runner-protocol.md) ·
> [Image Catalog](./image-catalog.md) ·
> [Documentation Standards](./standards/documentation.md)

<br><br>

## Directory Structure

```text
docs/
  README.md                            this file
  output-contract.md                   image anchor format, stable IDs, manifest schema
  runner-protocol.md                   JSON event protocol between Java CLI and Python runner
  image-catalog.md                     master catalog of images across all evaluation fixtures
  samples/
    sample-multiimage.md               example Markdown output with image anchors
    sample-multiimage.txt              example TXT output with image anchors
    sample-textonly.md                  example Markdown output without images
    sample-textonly.txt                 example TXT output without images
  standards/
    documentation.md                   voice, formatting, visual aids, file naming conventions
    pdf-image-inspection.md            two-layer verification methodology for PDF image cataloging
```

<br><br>

## File Descriptions

### Pipeline contracts

| File | Purpose |
|------|---------|
| `output-contract.md` | Defines how image-aware Markdown and TXT outputs represent extracted images. Covers anchor syntax, stable identifiers, ordering rules, and manifest schema. All implementations (Python POC and Java KVision port) must conform. |
| `runner-protocol.md` | Defines the JSON event protocol that `run_docling.py` emits on stdout. Java's `DoclingRunner.parseResult()` reads these events to build `DoclingResult` objects. |

### Reference data

| File | Purpose |
|------|---------|
| `image-catalog.md` | Master catalog of all images, figures, charts, and diagrams across 20 evaluation fixtures. Includes content type classification, difficulty ratings, evaluation subset selection (64 images), gap analysis, and distribution summaries. |

### Samples

| File | Purpose |
|------|---------|
| `samples/sample-multiimage.md` | Example Markdown output showing image anchors interleaved with document text. |
| `samples/sample-multiimage.txt` | Same document in TXT format with image anchors. |
| `samples/sample-textonly.md` | Example Markdown output for a document with no images. |
| `samples/sample-textonly.txt` | Same document in TXT format. |

### Standards

| File | Purpose |
|------|---------|
| `standards/documentation.md` | Documentation standards adapted from konsillix: active voice, `<br><br>` spacing, language-tagged code blocks, inline backtick rules, Mermaid diagram format, kebab-case filenames. |
| `standards/pdf-image-inspection.md` | Two-layer verification methodology (pypdfium2 structural scan + visual page rendering) for cataloging images in PDF fixtures. |

<br><br>

## Related Documentation

- [CONTRIBUTING.md](../CONTRIBUTING.md) -- development workflow, testing, commit conventions
- [fixtures/README.md](../fixtures/README.md) -- test document inventory and evaluation corpus summary

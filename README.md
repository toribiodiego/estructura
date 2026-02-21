# estructura

POC sandbox for image-aware document processing. This repo validates the
pipeline design -- output contract, image extraction, annotation flow,
limits, and degradation behavior -- before porting to the KVision Java
production service.

<br><br>

## Relationship to KVision

KVision is the production Spring Boot service for document transcription.
estructura proves out new features in a lightweight Java + Python wrapper
so design decisions are settled before writing production code. Findings
from this POC map directly to KVision implementation tasks.

<br><br>

## Docker Compose (recommended)

The easiest way to run the full pipeline is with Docker Compose. The `dev` service
builds an image with Java 21, Maven, Python 3, Docling, Tesseract, Pillow, and
the Google AI annotation client pre-installed.

```bash
# Build and start the dev container
docker compose build dev
docker compose up -d dev

# Verify Python dependencies
docker compose exec dev python3 -c "import docling, PIL, google.genai; print('ok')"
```

For annotation mode, copy `.env.example` to `.env` and set your `GOOGLE_API_KEY`.

### Running inside the container

```bash
# Run the Python pipeline directly
docker compose exec dev python3 \
    src/estructura-java/src/main/resources/scripts/run_docling.py \
    fixtures/downloaded/gemini3_pro_model_card.pdf \
    out/test --image-capture --progress

# Run with annotation mode (requires GOOGLE_API_KEY in .env)
docker compose exec dev python3 \
    src/estructura-java/src/main/resources/scripts/run_docling.py \
    fixtures/downloaded/gemini3_pro_model_card.pdf \
    out/test --image-capture --annotate --progress

# Run Java tests
docker compose exec dev bash -c "cd src/estructura-java && mvn test"

# Compile the Java project
docker compose exec dev bash -c "cd src/estructura-java && mvn compile"

# Interactive shell
docker compose exec dev bash
```

<br><br>

## Prerequisites (host install)

- Java 21+
- Maven 3.9+
- Python 3.10+ with Docling and Tesseract installed (or use the dev container)

Install Python dependencies:

```bash
pip install -r requirements.txt
```

This installs the core pipeline (`docling`, `pypdfium2`, `pytesseract`, `Pillow`)
and the vision annotation client (`google-genai` for Google AI Studio / Gemma).

For annotation mode, you also need a `GOOGLE_API_KEY` environment variable with a
valid Google AI Studio API key.

<br><br>

## Build and Run

Compile:

```bash
cd src/estructura-java
mvn compile
```

Run against a local file:

```bash
mvn exec:java -Ddoc.input=/path/to/document.pdf
```

Run against a URL:

```bash
mvn exec:java -Ddoc.input=https://example.com/document.pdf
```

Output files are written to `out/` by default. Override with `-Ddoc.out=<dir>`.

### Run Modes

Use `-Ddoc.mode` to select a preset configuration:

| Mode | Docling | OCR | Tables | Annotations |
|------|---------|-----|--------|-------------|
| (default) | on | on | off | off |
| `docling-only` | on | off | on | off |
| `ocr-only` | off | on | off | off |
| `tables` | on | on | on | off |
| `annotations` | on | on | on | on |

Example:

```bash
mvn exec:java -Ddoc.input=report.pdf -Ddoc.mode=tables
```

### Individual Properties

Fine-grained control beyond mode presets:

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `doc.input` | string | (required) | File path or URL to process |
| `doc.out` | string | `out` | Output directory |
| `doc.mode` | string | (none) | Preset mode (see table above) |
| `doc.docling` | boolean | `true` | Enable/disable Docling stage |
| `doc.ocr` | boolean | `true` | Enable/disable OCR stage |
| `doc.tableStructure` | boolean | `false` | Enable table structure extraction |
| `doc.imageAnnotations` | boolean | `false` | Enable image annotation |
| `doc.progress` | boolean | `false` | Show per-page timing |
| `doc.useCache` | boolean | `false` | Reuse cached Docling results |
| `doc.verbose` | boolean | `false` | Verbose runner output |
| `doc.maxPages` | integer | (none) | Limit pages to process |
| `doc.imageCapture` | boolean | `false` | Enable page image capture and crop extraction |
| `doc.maxImagePages` | integer | `50` | Max pages to capture images from |
| `doc.maxImagesPerPage` | integer | `20` | Max image crops per page |
| `doc.maxTotalImages` | integer | `200` | Max total image crops |
| `doc.dpi` | integer | `120` | OCR resolution |

<br><br>

## Run Tests

```bash
cd src/estructura-java
mvn test
```

The test suite uses a fake Python runner so no Docling installation is needed.

<br><br>

## Project Structure

```
estructura/
  README.md
  requirements.txt                 # Python dependencies
  src/estructura-java/
    pom.xml
    src/
      main/
        java/com/konsilix/kvision/docling/
          DoclingCli.java            # CLI entry point
          DoclingRunner.java         # Subprocess orchestration
          DoclingRunnerOptions.java  # Configuration record
          DoclingResult.java         # Structured output record
          DoclingMetrics.java        # Metrics from the Python runner
          DoclingRunnerException.java
        resources/scripts/
          run_docling.py             # Python Docling + OCR runner
      test/
        java/com/konsilix/kvision/docling/
          DoclingRunnerTest.java     # Unit tests
        resources/scripts/
          fake_docling_runner.py     # Test fake (no Docling needed)
```

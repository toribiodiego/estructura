## Docling OCR Pipeline Quickstart

This module wires a Java entry point (`DoclingOcrDemo`) to a Python helper (`run_docling.py`) so that we can ingest PDFs/images with Docling and run Tesseract for OCR. The Python runner now emits clear timing data so you can measure pipeline performance with a single command.

### Prerequisites

- Docker (Docker Desktop works fine on macOS/Linux/Windows).
- Python dependencies are baked into the container; no local installs needed.
- Create a cache folder on the host so Docling downloads are reused between runs:

```bash
mkdir -p ~/.docling-cache
```

### Build the dev container

```bash
cd /Users/Work/Desktop/konsillix/estructura/src/estructura-java
docker build -t estructura-java-dev .devcontainer
```

The build warms Docling once so later runs avoid first‑run downloads.

### Transcribe a document (recommended command)

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -v "$HOME/.docling-cache":/root/.cache \
  -v "$HOME/.docling-cache":/root/.local/share/docling \
  -w /workspace \
  estructura-java-dev \
  bash -lc 'python3 src/main/resources/scripts/run_docling.py \
      "https://arxiv.org/pdf/1312.5602" \
      out --use-cache'
```

*Replace the URL with any PDF/image path.* Results land under `out/` (markdown, JSON, OCR text, plus `_cache/` holding the normalized PDF).

#### Sample output

```
{"event": "docling_object_created", "docling_version": "unknown"}
{"event": "docling_timing", "seconds": 28.866}
{"event": "ocr_timing", "seconds": 14.331}
{"event": "metrics_summary", "docling": {"enabled": true, "seconds": 28.866}, "ocr": {"enabled": true, "seconds": 14.331, "pages": 9, "dpi": 120}, ...}
METRICS SUMMARY
  Docling: 28.87s
  OCR: 14.33s (pages=9, dpi=120)
  Tables: disabled
  Cache reuse: yes
{"status": "ok", ... "text": "/workspace/out/1312.txt", ...}
```

- `docling_timing` covers Docling’s structural analysis stage.
- `ocr_timing` covers Tesseract end‑to‑end.
- `METRICS …` gives a concise summary for quick comparisons.

If you need per‑page timing events, append `--progress` to the command to emit a JSON line per page (no progress bar).

### Optional knobs & trade-offs

| Option | How to enable | Effect |
| --- | --- | --- |
| Limit pages | `--max-pages 3` | Faster smoke test; useful for huge PDFs. |
| Increase DPI | `--dpi 180` (or higher) | Better OCR quality, but slower render/Tesseract passes. Default is 120. |
| Table structure | `--table-structure` | Enables Docling’s table extraction (slower); default is off. |
| Disable stages | `--no-ocr` or `--no-docling` | Skip OCR or Docling when isolating performance. |
| Verbose logs | `--verbose` | Show Docling INFO logging (hidden by default). |
| Java entry point | `mvn -q exec:java -Ddoc.input=...` | Runs the same pipeline via Java. Use `-Ddoc.useCache=true`, `-Ddoc.dpi=180`, etc. Java consumes the JSON metrics internally; use the Python command when you need to see them live. |

### Testing with the Java entry point

For integration testing or when embedding in Java, run:

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -v "$HOME/.docling-cache":/root/.cache \
  -v "$HOME/.docling-cache":/root/.local/share/docling \
  -w /workspace \
  estructura-java-dev \
  bash -lc 'MAVEN_OPTS="--enable-native-access=ALL-UNNAMED" \
    mvn -q exec:java \
      -Ddoc.input="https://arxiv.org/pdf/1312.5602" \
      -Ddoc.out=out \
      -Ddoc.useCache=true'
```

Add JVM flags to control the pipeline:

| Property | Example | Notes |
| --- | --- | --- |
| `doc.mode` | `-Ddoc.mode=ocr-only` / `docling-only` | Run a single stage. |
| `doc.dpi` | `-Ddoc.dpi=180` | See DPI trade-off above. |
| `doc.maxPages` | `-Ddoc.maxPages=3` | Limit OCR to first N pages. |
| `doc.tableStructure` | `-Ddoc.tableStructure=true` | Match `--table-structure`. |
| `doc.progress` | `-Ddoc.progress=true` | Emit per-page JSON timings. |
| `doc.tableStructure` | `-Ddoc.tableStructure=true` | Match `--table-structure`. |
| `doc.verbose` | `-Ddoc.verbose=true` | Surface Docling INFO logs when debugging. |
| `doc.useCache` | `-Ddoc.useCache=true` | Reuse `_cache/` folder and Docling downloads. |

The Java path writes the same artifacts to `out/`, but it does not echo the JSON metrics; fall back to the Python command when you need to profile interactively.

### Sharing a single copy/paste command

For teammates validating a PDF quickly:

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -v "$HOME/.docling-cache":/root/.cache \
  -v "$HOME/.docling-cache":/root/.local/share/docling \
  -w /workspace \
  estructura-java-dev \
  bash -lc 'python3 src/main/resources/scripts/run_docling.py \
      "<PUT-PDF-URL-HERE>" out --use-cache'
```

That command transcribes every page, emits timing metrics, and stores all artifacts in `out/`. Adjust the optional flags above if you need different behavior.

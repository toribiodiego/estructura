#!/bin/bash
set -e

# Run Docling extraction on multiple fixture documents sequentially.
# Collects per-document results, writes a summary JSON, and optionally
# zips the output directory.
#
# Works both locally (docker compose exec dev bash scripts/batch-extract.sh)
# and on Colab (submitted via /exec with background: true).
#
# Usage:
#   batch-extract.sh [OPTIONS] <output_dir>
#
#   --filter <spec>    Document filter: "00,02,05", "pdf", "all" (default: all)
#   --flags  <str>     Extra run_docling.py flags (quoted)
#   --zip              Zip output directory when done
#   --lean             Remove JSON and page images from output (keeps batch-summary.json)
#   --drive  <path>    Copy output to Google Drive mount path after completion
#   --help             Show usage
#
# Examples:
#   batch-extract.sh out/batch-001
#   batch-extract.sh --filter 00,07,13 --flags "--image-capture --save-json" out/batch-001
#   batch-extract.sh --filter pdf --zip out/batch-001
#   batch-extract.sh --lean --drive /content/drive/MyDrive/estructura-runs/baseline out/batch-001

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$REPO_ROOT/src/estructura-java/src/main/resources/scripts/run_docling.py"

FILTER=""
FLAGS=""
ZIP=false
LEAN=false
DRIVE_PATH=""
OUTPUT_DIR=""

usage() {
    echo "Usage: $(basename "$0") [OPTIONS] <output_dir>"
    echo ""
    echo "Run Docling extraction on multiple fixture documents."
    echo ""
    echo "Options:"
    echo "  --filter <spec>    Document filter: \"00,02,05\", \"pdf\", \"all\" (default: all)"
    echo "  --flags  <str>     Extra run_docling.py flags (quoted)"
    echo "  --zip              Zip output directory when done"
    echo "  --lean             Remove JSON and page images from output (keeps batch-summary.json)"
    echo "  --drive  <path>    Copy output to Google Drive mount path after completion"
    echo "  --help             Show usage"
    echo ""
    echo "Filter examples:"
    echo "  --filter 00               single document"
    echo "  --filter 00,02,05         multiple documents by number"
    echo "  --filter pdf              all PDFs"
    echo "  --filter pptx             all PPTX files"
    echo "  --filter all              all documents (same as no filter)"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") out/batch-001"
    echo "  $(basename "$0") --filter 00,07,13 --flags \"--image-capture --save-json\" out/batch-001"
    echo "  $(basename "$0") --filter pdf --zip out/batch-001"
    echo "  $(basename "$0") --lean --drive /content/drive/MyDrive/estructura-runs/baseline out/batch-001"
}

# ---- Argument parsing ----
while [[ $# -gt 0 ]]; do
    case "$1" in
        --filter) FILTER="$2"; shift 2 ;;
        --flags)  FLAGS="$2"; shift 2 ;;
        --zip)    ZIP=true; shift ;;
        --lean)   LEAN=true; shift ;;
        --drive)  DRIVE_PATH="$2"; shift 2 ;;
        --help)   usage; exit 0 ;;
        -*)       echo "Unknown option: $1"; usage; exit 1 ;;
        *)
            if [[ -z "$OUTPUT_DIR" ]]; then
                OUTPUT_DIR="$1"; shift
            else
                echo "Unexpected argument: $1"; usage; exit 1
            fi
            ;;
    esac
done

if [[ -z "$OUTPUT_DIR" ]]; then
    echo "Error: output directory is required."
    echo ""
    usage
    exit 1
fi

if [[ "$FILTER" == "all" ]]; then
    FILTER=""
fi

# ---- Filter logic (mirrors download-fixtures.sh) ----
should_process() {
    local name="$1"
    if [[ -z "$FILTER" ]]; then
        return 0
    fi
    local doc_num="${name%%_*}"
    local doc_ext="${name##*.}"
    IFS=',' read -ra filters <<< "$FILTER"
    for f in "${filters[@]}"; do
        f="$(echo "$f" | tr -d ' ')"
        if [[ "$doc_num" == "$f" ]]; then
            return 0
        fi
        if [[ "$doc_ext" == "$f" ]]; then
            return 0
        fi
    done
    return 1
}

# ---- Discover fixtures ----
FIXTURE_DIR="$REPO_ROOT/fixtures/downloaded"
if [[ ! -d "$FIXTURE_DIR" ]]; then
    echo "Error: fixture directory not found: $FIXTURE_DIR"
    echo "Run scripts/download-fixtures.sh first."
    exit 1
fi

# Collect fixture files, sorted by name for predictable ordering
FIXTURES=()
while IFS= read -r -d '' filepath; do
    filename="$(basename "$filepath")"
    if should_process "$filename"; then
        FIXTURES+=("$filepath")
    fi
done < <(find "$FIXTURE_DIR" -type f \( -name "*.pdf" -o -name "*.docx" -o -name "*.pptx" -o -name "*.xlsx" -o -name "*.html" -o -name "*.webp" -o -name "*.png" -o -name "*.jpg" \) -print0 | sort -z)

TOTAL=${#FIXTURES[@]}
if [[ "$TOTAL" -eq 0 ]]; then
    echo "No fixtures matched filter: ${FILTER:-all}"
    echo "Available fixtures in: $FIXTURE_DIR"
    exit 1
fi

# ---- Prepare output ----
mkdir -p "$OUTPUT_DIR"
PROGRESS_FILE="$OUTPUT_DIR/progress.txt"
: > "$PROGRESS_FILE"

echo "Batch extraction: $TOTAL documents"
if [[ -n "$FILTER" ]]; then
    echo "Filter: $FILTER"
fi
echo "Flags: ${FLAGS:-(none)}"
echo "Output: $OUTPUT_DIR"
echo ""

# ---- Per-document results (accumulated for summary) ----
DOC_RESULTS=""
SUCCEEDED=0
FAILED=0
BATCH_START=$(date +%s)

for i in "${!FIXTURES[@]}"; do
    filepath="${FIXTURES[$i]}"
    filename="$(basename "$filepath")"
    doc_num="${filename%%_*}"
    doc_dir="$OUTPUT_DIR/doc${doc_num}"
    seq=$((i + 1))

    mkdir -p "$doc_dir"

    # Run extraction
    doc_start=$(date +%s)
    exit_code=0
    # shellcheck disable=SC2086
    python3 "$SCRIPT" "$filepath" "$doc_dir" $FLAGS \
        > "$doc_dir/run.log" 2>&1 || exit_code=$?
    doc_end=$(date +%s)
    doc_seconds=$((doc_end - doc_start))

    # Parse metrics_summary from run.log
    metrics_json=$(grep -o '{"event": "metrics_summary".*' "$doc_dir/run.log" 2>/dev/null | head -1 || true)

    # Extract key metrics using python3 (no jq dependency)
    crops=0
    pages=0
    if [[ -n "$metrics_json" ]]; then
        crops=$(echo "$metrics_json" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('image_capture', {}).get('crops_extracted', 0))
except: print(0)
" 2>/dev/null || echo 0)
        pages=$(echo "$metrics_json" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('image_capture', {}).get('pages_saved', 0))
except: print(0)
" 2>/dev/null || echo 0)
    fi

    # Status line
    if [[ "$exit_code" -eq 0 ]]; then
        status="OK"
        SUCCEEDED=$((SUCCEEDED + 1))
    else
        status="FAIL(${exit_code})"
        FAILED=$((FAILED + 1))
    fi

    status_line="[$seq/$TOTAL] $status doc${doc_num} -- ${doc_seconds}s, ${crops} crops, ${pages} pages"
    echo "$status_line"
    echo "$status_line" >> "$PROGRESS_FILE"

    # Accumulate per-doc JSON entry
    doc_entry=$(python3 -c "
import json
print(json.dumps({
    'doc_num': '$doc_num',
    'filename': '$filename',
    'exit_code': $exit_code,
    'seconds': $doc_seconds,
    'crops_extracted': $crops,
    'pages_saved': $pages,
    'output_dir': 'doc${doc_num}',
}))
")

    if [[ -z "$DOC_RESULTS" ]]; then
        DOC_RESULTS="$doc_entry"
    else
        DOC_RESULTS="$DOC_RESULTS,$doc_entry"
    fi
done

BATCH_END=$(date +%s)
BATCH_SECONDS=$((BATCH_END - BATCH_START))

# ---- Write batch-summary.json ----
python3 -c "
import json

docs = json.loads('[$DOC_RESULTS]')
total_crops = sum(d['crops_extracted'] for d in docs)
total_pages = sum(d['pages_saved'] for d in docs)

summary = {
    'batch': {
        'total_documents': $TOTAL,
        'succeeded': $SUCCEEDED,
        'failed': $FAILED,
        'total_seconds': $BATCH_SECONDS,
        'total_crops': total_crops,
        'total_pages': total_pages,
    },
    'filter': '${FILTER:-all}',
    'flags': '${FLAGS}',
    'documents': docs,
}

with open('$OUTPUT_DIR/batch-summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
" 2>/dev/null

echo ""
echo "---"
echo "Batch complete: $SUCCEEDED ok, $FAILED failed, ${BATCH_SECONDS}s total"
echo "Summary: $OUTPUT_DIR/batch-summary.json"

# ---- Optional lean cleanup ----
if [[ "$LEAN" == true ]]; then
    find "$OUTPUT_DIR" -name "*.json" ! -name "batch-summary.json" -delete 2>/dev/null
    find "$OUTPUT_DIR" -type d -name "pages" -exec rm -rf {} + 2>/dev/null || true
    echo "Cleaned: removed JSON and page images (--lean)"
fi

# ---- Optional Drive copy ----
if [[ -n "$DRIVE_PATH" ]]; then
    mkdir -p "$DRIVE_PATH"
    cp -r "$OUTPUT_DIR"/* "$DRIVE_PATH/"
    echo "Copied to Drive: $DRIVE_PATH"
fi

# ---- Optional zip ----
if [[ "$ZIP" == true ]]; then
    zip_path="${OUTPUT_DIR}.zip"
    # Use (cd ...) to get clean relative paths in the zip
    parent_dir="$(dirname "$OUTPUT_DIR")"
    base_name="$(basename "$OUTPUT_DIR")"
    (cd "$parent_dir" && zip -rq "$base_name.zip" "$base_name")
    echo "Zipped: $zip_path"
fi

if [[ "$FAILED" -gt 0 ]]; then
    echo ""
    echo "WARNING: $FAILED document(s) failed. Check run.log in each doc directory."
    exit 1
fi

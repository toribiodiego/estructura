#!/bin/bash
set -e

# Download a batch run from Google Drive to the local machine via rclone.
#
# Requires rclone configured with a "gdrive" remote pointing to Google Drive.
# See: rclone config (one-time setup)
#
# Usage:
#   pull-run.sh [OPTIONS] <run-name> [output-dir]
#
#   --include-json      Also download JSON files (excluded by default)
#   --include-pages     Also download page images (excluded by default)
#   --include-markdown  Also download Markdown files (excluded by default)
#   --dry-run           Show what would be downloaded without transferring
#   --help              Show usage
#
# Examples:
#   pull-run.sh 2026-03-04-baseline
#   pull-run.sh --include-json 2026-03-04-baseline out/custom-dir
#   pull-run.sh --include-markdown 2026-03-04-baseline
#   pull-run.sh --dry-run 2026-03-04-baseline

REMOTE="gdrive"
DRIVE_ROOT="estructura-runs"

INCLUDE_JSON=false
INCLUDE_PAGES=false
INCLUDE_MARKDOWN=false
DRY_RUN=false
RUN_NAME=""
OUTPUT_DIR=""

usage() {
    echo "Usage: $(basename "$0") [OPTIONS] <run-name> [output-dir]"
    echo ""
    echo "Download a batch run from Google Drive via rclone."
    echo ""
    echo "Options:"
    echo "  --include-json      Also download JSON files (excluded by default)"
    echo "  --include-pages     Also download page images (excluded by default)"
    echo "  --include-markdown  Also download Markdown files (excluded by default)"
    echo "  --dry-run           Show what would be downloaded without transferring"
    echo "  --help              Show usage"
    echo ""
    echo "Defaults:"
    echo "  Output dir: out/runs/<run-name>"
    echo "  Excludes *.json (except batch-summary.json), *.md, and pages/ by default"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") 2026-03-04-baseline"
    echo "  $(basename "$0") --include-json 2026-03-04-baseline out/custom-dir"
    echo "  $(basename "$0") --include-markdown 2026-03-04-baseline"
    echo "  $(basename "$0") --dry-run 2026-03-04-baseline"
}

# ---- Argument parsing ----
while [[ $# -gt 0 ]]; do
    case "$1" in
        --include-json)     INCLUDE_JSON=true; shift ;;
        --include-pages)   INCLUDE_PAGES=true; shift ;;
        --include-markdown) INCLUDE_MARKDOWN=true; shift ;;
        --dry-run)         DRY_RUN=true; shift ;;
        --help)           usage; exit 0 ;;
        -*)               echo "Unknown option: $1"; usage; exit 1 ;;
        *)
            if [[ -z "$RUN_NAME" ]]; then
                RUN_NAME="$1"; shift
            elif [[ -z "$OUTPUT_DIR" ]]; then
                OUTPUT_DIR="$1"; shift
            else
                echo "Unexpected argument: $1"; usage; exit 1
            fi
            ;;
    esac
done

if [[ -z "$RUN_NAME" ]]; then
    echo "Error: run name is required."
    echo ""
    usage
    exit 1
fi

# ---- Check rclone ----
if ! command -v rclone &>/dev/null; then
    echo "Error: rclone is not installed."
    echo "Install with: brew install rclone"
    echo "Then configure: rclone config (add 'gdrive' remote for Google Drive)"
    exit 1
fi

if ! rclone listremotes 2>/dev/null | grep -q "^${REMOTE}:$"; then
    echo "Error: rclone remote '${REMOTE}' not configured."
    echo "Run: rclone config"
    echo "Create a remote named '${REMOTE}' pointing to Google Drive."
    exit 1
fi

# ---- Resolve paths ----
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="${REMOTE}:${DRIVE_ROOT}/${RUN_NAME}/"

if [[ -z "$OUTPUT_DIR" ]]; then
    OUTPUT_DIR="$REPO_ROOT/out/runs/${RUN_NAME}"
fi

# ---- Build filter rules ----
# rclone processes filter rules in order; first match wins.
FILTERS=()
if [[ "$INCLUDE_JSON" != true ]]; then
    # Keep batch-summary.json, exclude all other JSON
    FILTERS+=(--filter "+ batch-summary.json" --filter "- *.json")
fi
if [[ "$INCLUDE_MARKDOWN" != true ]]; then
    FILTERS+=(--filter "- *.md")
fi
if [[ "$INCLUDE_PAGES" != true ]]; then
    FILTERS+=(--filter "- pages/**")
fi

# ---- Verify source exists ----
echo "Source: ${SOURCE}"
echo "Destination: ${OUTPUT_DIR}"

if ! rclone lsd "${REMOTE}:${DRIVE_ROOT}/" 2>/dev/null | grep -q "${RUN_NAME}"; then
    echo ""
    echo "Error: run '${RUN_NAME}' not found on Drive."
    echo ""
    echo "Available runs:"
    rclone lsd "${REMOTE}:${DRIVE_ROOT}/" 2>/dev/null | awk '{print "  " $NF}' || echo "  (none)"
    exit 1
fi

# ---- Download ----
if [[ "$DRY_RUN" == true ]]; then
    echo ""
    echo "Dry run -- would download:"
    rclone copy "$SOURCE" "$OUTPUT_DIR" "${FILTERS[@]}" --dry-run 2>&1
    exit 0
fi

echo ""
mkdir -p "$OUTPUT_DIR"

start_time=$(date +%s)
rclone copy "$SOURCE" "$OUTPUT_DIR" "${FILTERS[@]}" --progress
end_time=$(date +%s)
elapsed=$((end_time - start_time))

# ---- Verify ----
echo ""
if [[ -f "$OUTPUT_DIR/batch-summary.json" ]]; then
    file_count=$(find "$OUTPUT_DIR" -type f | wc -l | tr -d ' ')
    dir_size=$(du -sh "$OUTPUT_DIR" | cut -f1)
    echo "Download complete: ${file_count} files, ${dir_size}, ${elapsed}s"
    echo "Summary: ${OUTPUT_DIR}/batch-summary.json"
else
    echo "WARNING: batch-summary.json not found in downloaded output."
    echo "The run may be incomplete or the path may be wrong."
fi

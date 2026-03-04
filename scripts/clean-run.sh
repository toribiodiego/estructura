#!/bin/bash
set -e

# Remove completed batch runs from Google Drive via rclone.
#
# Requires rclone configured with a "gdrive" remote pointing to Google Drive.
#
# Usage:
#   clean-run.sh [OPTIONS] [run-name]
#
#   --list    List all runs on Drive with sizes (no deletion)
#   --yes     Skip confirmation prompt
#   --help    Show usage
#
# Examples:
#   clean-run.sh --list
#   clean-run.sh 2026-03-04-baseline
#   clean-run.sh --yes 2026-03-04-baseline

REMOTE="gdrive"
DRIVE_ROOT="estructura-runs"

LIST=false
YES=false
RUN_NAME=""

usage() {
    echo "Usage: $(basename "$0") [OPTIONS] [run-name]"
    echo ""
    echo "Remove completed batch runs from Google Drive."
    echo ""
    echo "Options:"
    echo "  --list    List all runs on Drive with sizes (no deletion)"
    echo "  --yes     Skip confirmation prompt"
    echo "  --help    Show usage"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") --list"
    echo "  $(basename "$0") 2026-03-04-baseline"
    echo "  $(basename "$0") --yes 2026-03-04-baseline"
}

# ---- Argument parsing ----
while [[ $# -gt 0 ]]; do
    case "$1" in
        --list)   LIST=true; shift ;;
        --yes)    YES=true; shift ;;
        --help)   usage; exit 0 ;;
        -*)       echo "Unknown option: $1"; usage; exit 1 ;;
        *)
            if [[ -z "$RUN_NAME" ]]; then
                RUN_NAME="$1"; shift
            else
                echo "Unexpected argument: $1"; usage; exit 1
            fi
            ;;
    esac
done

# ---- Check rclone ----
if ! command -v rclone &>/dev/null; then
    echo "Error: rclone is not installed."
    echo "Install with: brew install rclone"
    exit 1
fi

if ! rclone listremotes 2>/dev/null | grep -q "^${REMOTE}:$"; then
    echo "Error: rclone remote '${REMOTE}' not configured."
    echo "Run: rclone config"
    exit 1
fi

# ---- List mode ----
if [[ "$LIST" == true ]]; then
    echo "Runs on Drive (${REMOTE}:${DRIVE_ROOT}/):"
    echo ""
    runs=$(rclone lsd "${REMOTE}:${DRIVE_ROOT}/" 2>/dev/null || true)
    if [[ -z "$runs" ]]; then
        echo "  (none)"
    else
        while IFS= read -r line; do
            dir_name=$(echo "$line" | awk '{print $NF}')
            dir_size=$(rclone size "${REMOTE}:${DRIVE_ROOT}/${dir_name}" 2>/dev/null | grep "Total size" | sed 's/.*: //' || echo "unknown")
            echo "  ${dir_name}  (${dir_size})"
        done <<< "$runs"
    fi
    exit 0
fi

# ---- Validate ----
if [[ -z "$RUN_NAME" ]]; then
    echo "Error: run name is required (or use --list to see available runs)."
    echo ""
    usage
    exit 1
fi

TARGET="${REMOTE}:${DRIVE_ROOT}/${RUN_NAME}"

# Check if run exists
if ! rclone lsd "${REMOTE}:${DRIVE_ROOT}/" 2>/dev/null | grep -q "${RUN_NAME}"; then
    echo "Error: run '${RUN_NAME}' not found on Drive."
    echo ""
    echo "Available runs:"
    rclone lsd "${REMOTE}:${DRIVE_ROOT}/" 2>/dev/null | awk '{print "  " $NF}' || echo "  (none)"
    exit 1
fi

# Show size before deletion
run_size=$(rclone size "$TARGET" 2>/dev/null | grep "Total size" | sed 's/.*: //' || echo "unknown size")
echo "Run: ${RUN_NAME} (${run_size})"

# ---- Confirm ----
if [[ "$YES" != true ]]; then
    echo ""
    read -r -p "Delete '${RUN_NAME}' from Drive? [y/N] " confirm
    if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
        echo "Cancelled."
        exit 0
    fi
fi

# ---- Delete ----
echo "Deleting ${TARGET}..."
rclone purge "$TARGET"
echo "Deleted: ${RUN_NAME}"

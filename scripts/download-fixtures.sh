#!/bin/bash
set -e

# Download test fixtures for the estructura image-aware pipeline POC.
# Documents are sourced from KVision's test infrastructure (public URLs).
#
# Usage:
#   ./scripts/download-fixtures.sh          # all 13 documents
#   ./scripts/download-fixtures.sh --quick   # baseline set only (5 docs)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$REPO_ROOT/fixtures/downloaded"

QUICK=false
if [[ "$1" == "--quick" ]]; then
    QUICK=true
fi

mkdir -p "$DEST"
cd "$DEST"

TOTAL=0
FAILED=0
SKIPPED=0

download() {
    local name="$1"
    local url="$2"
    local sha256="$3"  # empty string if no checksum available

    TOTAL=$((TOTAL + 1))

    if [[ -f "$name" ]]; then
        if [[ -n "$sha256" ]]; then
            local actual
            actual=$(shasum -a 256 "$name" | cut -d' ' -f1)
            if [[ "$actual" == "$sha256" ]]; then
                echo "  [skip] $name (already exists, checksum ok)"
                SKIPPED=$((SKIPPED + 1))
                return 0
            else
                echo "  [warn] $name exists but checksum mismatch, re-downloading"
            fi
        else
            echo "  [skip] $name (already exists)"
            SKIPPED=$((SKIPPED + 1))
            return 0
        fi
    fi

    echo "  [get]  $name"
    if ! curl -fSL --retry 2 --retry-delay 3 -o "$name" "$url"; then
        echo "  [FAIL] $name -- download failed"
        FAILED=$((FAILED + 1))
        rm -f "$name"
        return 0
    fi

    if [[ -n "$sha256" ]]; then
        local actual
        actual=$(shasum -a 256 "$name" | cut -d' ' -f1)
        if [[ "$actual" != "$sha256" ]]; then
            echo "  [FAIL] $name -- checksum mismatch"
            echo "         expected: $sha256"
            echo "         actual:   $actual"
            FAILED=$((FAILED + 1))
            return 0
        fi
    fi

    echo "  [ok]   $name ($(du -h "$name" | cut -f1))"
}

# ---- Baseline set (5 documents) ----
echo "Downloading baseline fixtures..."
echo ""

download "gemini3_pro_model_card.pdf" \
    "https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf" \
    ""

download "epa_sample_letter.pdf" \
    "https://19january2021snapshot.epa.gov/sites/static/files/2016-02/documents/epa_sample_letter_sent_to_commissioners_dated_february_29_2015.pdf" \
    ""

download "medrxiv_llama4_benchmark.docx" \
    "https://www.medrxiv.org/content/medrxiv/early/2025/10/07/2025.10.05.25337350/DC1/embed/media-1.docx?download=true" \
    ""

download "policy_gradient_rl_lecture.pptx" \
    "https://www.cs.princeton.edu/courses/archive/spring17/cos598F/lectures/RL.pptx" \
    ""

download "medrxiv_llm_imaging_eval.xlsx" \
    "https://www.medrxiv.org/content/medrxiv/early/2025/10/29/2025.10.27.25338904/DC3/embed/media-3.xlsx?download=true" \
    ""

# ---- OCR and mixed-content set (2 additional documents) ----
echo ""
echo "Downloading OCR and mixed-content fixtures..."
echo ""

download "xerox_mfp_scan_forestburg.pdf" \
    "https://files.gabbart.com/1605/scanned_from_a_xerox_multifunction_printer.pdf" \
    ""

download "archive_newspaper_1948.pdf" \
    "https://archive.org/download/cupl_003575/cupl_003575_access.pdf" \
    ""

# TODO: Add image-bearing DOCX when a suitable public URL is identified.
# Current medrxiv DOCX is text-only (11 KB). Need a DOCX with embedded
# figures/photos to test non-PDF image extraction. Candidates: DOE OSTI
# technical reports, KVision Task 12.7 benchmark set.

# ---- Extended set (6 additional documents) ----
if [[ "$QUICK" == false ]]; then
    echo ""
    echo "Downloading extended fixtures..."
    echo ""

    download "gpt4_system_card.pdf" \
        "https://cdn.openai.com/papers/gpt-4-system-card.pdf" \
        "ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004"

    download "icml2019_importance_sampling.pdf" \
        "https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/ICML2019-Hanna.pdf" \
        "8160f6e88d54944e9c99571ff6dc759744d33ba9d47178ff7979ac53f5c8b9a3"

    download "imf_economic_impacts_ai.pdf" \
        "https://www.imf.org/-/media/Files/Publications/WP/2024/English/wpiea2024065-print-pdf.ashx" \
        "324b4e2c519940ac69c25061597d6b3828b748570025cb966a3d39bd62350948"

    download "anthropic_economic_index.pdf" \
        "https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf" \
        "42c34a517e9184ff06d5e3ab084e8a70c013c6fda60db4c97407bfbd582fde42"

    download "gemini_multimodal_report.pdf" \
        "https://arxiv.org/pdf/2312.11805v5.pdf" \
        "8ca95b27851b09c335fa2abe9b84cec5848195a5914eec7fb0b635ba2d8fe4fe"

    download "arxiv_2206_01062.pdf" \
        "https://arxiv.org/pdf/2206.01062.pdf" \
        ""
fi

echo ""
echo "---"
echo "Downloaded to: $DEST"
echo ""
ls -lh "$DEST" 2>/dev/null | awk 'NR>1 {printf "  %-6s %s\n", $5, $9}'
echo ""
echo "Total size: $(du -sh "$DEST" | cut -f1)"
echo "Results: $TOTAL attempted, $((TOTAL - FAILED - SKIPPED)) downloaded, $SKIPPED skipped, $FAILED failed"

if [[ "$FAILED" -gt 0 ]]; then
    echo ""
    echo "WARNING: $FAILED download(s) failed. Re-run to retry."
    exit 1
fi

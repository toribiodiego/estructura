#!/bin/bash
set -e

# Download test fixtures for the estructura image-aware pipeline POC.
# Documents are sourced from KVision's test infrastructure (public URLs).
# Files are organized into category subdirectories under fixtures/downloaded/.
#
# Usage:
#   ./scripts/download-fixtures.sh          # all 23 documents
#   ./scripts/download-fixtures.sh --quick  # baseline set only (5 docs)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$REPO_ROOT/fixtures/downloaded"

QUICK=false
if [[ "$1" == "--quick" ]]; then
    QUICK=true
fi

# Create category subdirectories
mkdir -p "$DEST/multi-image"
mkdir -p "$DEST/vector-heavy"
mkdir -p "$DEST/text-heavy"
mkdir -p "$DEST/scanned"
mkdir -p "$DEST/text-only"
mkdir -p "$DEST/table-image"
mkdir -p "$REPO_ROOT/fixtures/other"

TOTAL=0
FAILED=0
SKIPPED=0

download() {
    local category="$1"
    local name="$2"
    local url="$3"
    local sha256="$4"  # empty string if no checksum available

    local dest_dir="$DEST/$category"
    local filepath="$dest_dir/$name"

    TOTAL=$((TOTAL + 1))

    if [[ -f "$filepath" ]]; then
        if [[ -n "$sha256" ]]; then
            local actual
            actual=$(shasum -a 256 "$filepath" | cut -d' ' -f1)
            if [[ "$actual" == "$sha256" ]]; then
                echo "  [skip] $category/$name (already exists, checksum ok)"
                SKIPPED=$((SKIPPED + 1))
                return 0
            else
                echo "  [warn] $category/$name exists but checksum mismatch, re-downloading"
            fi
        else
            echo "  [skip] $category/$name (already exists)"
            SKIPPED=$((SKIPPED + 1))
            return 0
        fi
    fi

    echo "  [get]  $category/$name"
    if ! curl -fSL --retry 2 --retry-delay 3 -o "$filepath" "$url"; then
        echo "  [FAIL] $category/$name -- download failed"
        FAILED=$((FAILED + 1))
        rm -f "$filepath"
        return 0
    fi

    if [[ -n "$sha256" ]]; then
        local actual
        actual=$(shasum -a 256 "$filepath" | cut -d' ' -f1)
        if [[ "$actual" != "$sha256" ]]; then
            echo "  [FAIL] $category/$name -- checksum mismatch"
            echo "         expected: $sha256"
            echo "         actual:   $actual"
            FAILED=$((FAILED + 1))
            return 0
        fi
    fi

    echo "  [ok]   $category/$name ($(du -h "$filepath" | cut -f1))"
}

# ---- Baseline set (5 documents) ----
echo "Downloading baseline fixtures..."
echo ""

download "text-heavy" "00_gemini3_pro_model_card.pdf" \
    "https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf" \
    ""

download "scanned" "07_epa_sample_letter.pdf" \
    "https://19january2021snapshot.epa.gov/sites/static/files/2016-02/documents/epa_sample_letter_sent_to_commissioners_dated_february_29_2015.pdf" \
    ""

download "text-only" "10_medrxiv_llama4_benchmark.docx" \
    "https://www.medrxiv.org/content/medrxiv/early/2025/10/07/2025.10.05.25337350/DC1/embed/media-1.docx?download=true" \
    ""

download "multi-image" "11_policy_gradient_rl_lecture.pptx" \
    "https://www.cs.princeton.edu/courses/archive/spring17/cos598F/lectures/RL.pptx" \
    ""

# Non-evaluation fixtures (fixtures/other/)
OTHER_DIR="$REPO_ROOT/fixtures/other"

if [[ ! -f "$OTHER_DIR/medrxiv_llm_imaging_eval.xlsx" ]]; then
    echo "  [get]  other/medrxiv_llm_imaging_eval.xlsx"
    curl -fSL --retry 2 --retry-delay 3 \
        -o "$OTHER_DIR/medrxiv_llm_imaging_eval.xlsx" \
        "https://www.medrxiv.org/content/medrxiv/early/2025/10/07/2025.10.05.25337350/DC1/embed/media-2.xlsx?download=true" \
        || echo "  [FAIL] other/medrxiv_llm_imaging_eval.xlsx -- download failed"
else
    echo "  [skip] other/medrxiv_llm_imaging_eval.xlsx (already exists)"
fi

# ---- OCR and mixed-content set (3 additional documents) ----
echo ""
echo "Downloading OCR and mixed-content fixtures..."
echo ""

download "scanned" "08_xerox_mfp_scan_forestburg.pdf" \
    "https://files.gabbart.com/1605/scanned_from_a_xerox_multifunction_printer.pdf" \
    ""

download "scanned" "09_archive_newspaper_1948.pdf" \
    "https://archive.org/download/cupl_003575/cupl_003575_access.pdf" \
    ""

# ---- Extended set (6 additional documents) ----
if [[ "$QUICK" == false ]]; then
    echo ""
    echo "Downloading extended fixtures..."
    echo ""

    download "vector-heavy" "01_gpt4_system_card.pdf" \
        "https://cdn.openai.com/papers/gpt-4-system-card.pdf" \
        "ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004"

    download "multi-image" "02_icml2019_importance_sampling.pdf" \
        "https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/ICML2019-Hanna.pdf" \
        "8160f6e88d54944e9c99571ff6dc759744d33ba9d47178ff7979ac53f5c8b9a3"

    download "text-heavy" "03_imf_economic_impacts_ai.pdf" \
        "https://www.imf.org/-/media/Files/Publications/WP/2024/English/wpiea2024065-print-pdf.ashx" \
        "324b4e2c519940ac69c25061597d6b3828b748570025cb966a3d39bd62350948"

    download "vector-heavy" "04_anthropic_economic_index.pdf" \
        "https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf" \
        "42c34a517e9184ff06d5e3ab084e8a70c013c6fda60db4c97407bfbd582fde42"

    download "multi-image" "05_gemini_multimodal_report.pdf" \
        "https://arxiv.org/pdf/2312.11805v5.pdf" \
        "8ca95b27851b09c335fa2abe9b84cec5848195a5914eec7fb0b635ba2d8fe4fe"

    download "multi-image" "06_arxiv_2206_01062.pdf" \
        "https://arxiv.org/pdf/2206.01062.pdf" \
        ""

    download "multi-image" "12_minnstate_fy2025_budget.pptx" \
        "https://www.minnstate.edu/system/finance/budget/docs/fy2025-operating-budget-second-reading-june-2024-final.pptx" \
        ""

    download "table-image" "13_artpro_table.webp" \
        "https://standupsurfshop.com.au/wp-content/uploads/2023/09/ARTPRO-Table.webp" \
        ""

    download "table-image" "14_simple_table.png" \
        "https://raw.githubusercontent.com/eihli/image-table-ocr/master/resources/test_data/simple.png" \
        ""

    download "table-image" "15_timetable.jpg" \
        "https://courses.washington.edu/fish340/Images/timetable.jpg" \
        ""

    download "multi-image" "16_cambridge_mitoball_biology.docx" \
        "https://www.repository.cam.ac.uk/bitstreams/a5e95699-d0d4-49e1-a471-e7dc381cdbac/download" \
        ""

    download "text-heavy" "17_arxiv_fractional_brownian_sde.pdf" \
        "https://arxiv.org/pdf/2306.08324.pdf" \
        ""

    download "multi-image" "18_ibm_microservices_redbook.pdf" \
        "https://www.redbooks.ibm.com/redbooks/pdfs/sg248275.pdf" \
        ""

    download "multi-image" "19_cris_electronic_screens_2023.docx" \
        "https://www.energyrating.gov.au/sites/default/files/2023-06/Cost%20Recovery%20Impact%20Statement%20-%20Electronic%20Screens%20-%202023.docx" \
        ""

    download "multi-image" "20_illinois_workforce_dashboard.xlsx" \
        "https://www.illinoisworknet.com/WIOA/Resources/Documents/6.%20Dashboard%20for%20the%20Local%20Workforce%20Board%20-%20TEMPLATE.xlsx" \
        ""

    download "multi-image" "21_praxie_project_portfolio.xlsx" \
        "https://praxie.com/wp-content/uploads/2021/08/Project-Portfolio-Management-Template.xlsx" \
        ""

    download "multi-image" "22_nasa_global_warming.html" \
        "https://science.nasa.gov/earth/climate-change/global-warming/" \
        ""
fi

echo ""
echo "---"
echo "Downloaded to: $DEST"
echo ""
echo "Directory layout:"
for dir in multi-image vector-heavy text-heavy scanned text-only table-image; do
    count=$(find "$DEST/$dir" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "  $dir/ ($count files)"
done
echo ""
echo "Total size: $(du -sh "$DEST" | cut -f1)"
echo "Results: $TOTAL attempted, $((TOTAL - FAILED - SKIPPED)) downloaded, $SKIPPED skipped, $FAILED failed"

if [[ "$FAILED" -gt 0 ]]; then
    echo ""
    echo "WARNING: $FAILED download(s) failed. Re-run to retry."
    exit 1
fi

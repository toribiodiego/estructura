FROM ghcr.io/graalvm/jdk-community:25

# System tools + OCR engine + Maven
RUN microdnf install -y \
    tesseract tesseract-langpack-eng \
    git wget unzip python3-pip maven tar gzip \
    curl ca-certificates \
    && microdnf clean all

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /workspace

# --- Python stack (Docling w/ PDF support only, plus Tesseract OCR pipeline) ---
RUN python3 -m pip install --upgrade pip setuptools wheel && \
    python3 -m pip install \
    "docling[pdf]" \
    "pypdfium2>=4.30.0" \
    "pytesseract>=0.3.10"

# Warm Docling caches to avoid large downloads on first run
RUN curl -L --retry 3 --output /tmp/docling_warmup.pdf \
        https://filesamples.com/samples/document/pdf/sample3.pdf && \
    python3 - <<'PY'
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

opts = PdfPipelineOptions()
opts.do_ocr = False
opts.do_table_structure = False
opts.generate_page_images = False

conv = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
)
conv.convert("/tmp/docling_warmup.pdf")
PY

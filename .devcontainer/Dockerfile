FROM maven:3.9-eclipse-temurin-21

# System tools + OCR engine
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr tesseract-ocr-eng \
    python3 python3-pip python3-venv \
    git wget unzip curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /workspace

# Python stack (Docling with PDF support, plus Tesseract OCR pipeline)
RUN python3 -m pip install --break-system-packages \
    "docling[pdf]" \
    "pypdfium2>=4.30.0" \
    "pytesseract>=0.3.10" \
    "Pillow" \
    "google-genai"

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

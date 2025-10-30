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

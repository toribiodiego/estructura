FROM ghcr.io/graalvm/jdk-community:25

# OCR + tools + Maven from distro + curl + certs
RUN microdnf install -y \
    tesseract tesseract-langpack-eng \
    git wget unzip python3-pip maven tar gzip \
    curl ca-certificates \
    && microdnf clean all

WORKDIR /workspace

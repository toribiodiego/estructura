#!/usr/bin/env python3
import json
import mimetypes
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlretrieve

PDF_EXTS = {".pdf"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif"}

def ensure_local_file(src: str, dst_dir: Path) -> Path:
    p = urlparse(src)
    if p.scheme in ("http", "https"):
        name = os.path.basename(p.path) or f"doc_{int(time.time())}"
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / name
        filename, headers = urlretrieve(src, dst)
        downloaded = Path(filename)
        if downloaded.stat().st_size == 0:
            raise RuntimeError(f"Downloaded zero-byte file from {src}")

        suffix = downloaded.suffix.lower()
        if not suffix or suffix not in PDF_EXTS | IMAGE_EXTS:
            content_type = headers.get_content_type() if headers else None
            guessed = (mimetypes.guess_extension(content_type or "") or "").lower()
            if guessed in PDF_EXTS | IMAGE_EXTS:
                suffix = guessed
            else:
                # Treat unrecognized extensions as PDF by default.
                suffix = ".pdf"

        target = downloaded if downloaded.suffix.lower() == suffix else downloaded.with_suffix(suffix)
        if target != downloaded:
            downloaded.rename(target)
        return target
    path = Path(src).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(str(path))
    return path

def convert_image_to_pdf(image_path: Path, dst_dir: Path) -> Path:
    from PIL import Image

    dst_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = dst_dir / (image_path.stem + ".pdf")
    with Image.open(image_path) as img:
        rgb = img.convert("RGB")
        rgb.save(pdf_path, "PDF", resolution=220.0)
    return pdf_path

def ensure_local_document(src: str, dst_dir: Path) -> Path:
    local_path = ensure_local_file(src, dst_dir)
    suffix = local_path.suffix.lower()
    if suffix in PDF_EXTS:
        return local_path
    if suffix in IMAGE_EXTS:
        return convert_image_to_pdf(local_path, dst_dir)
    raise ValueError(f"Unsupported document type: {local_path.suffix or 'unknown'}")

def require(pkgs):
    missing = []
    for mod, pip_name in pkgs:
        try:
            __import__(mod)
        except Exception:
            missing.append(pip_name)
    if missing:
        print(
            "Missing dependencies. Install with:\n"
            f"    pip install {' '.join(repr(p) for p in missing)}\n",
            file=sys.stderr
        )
        sys.exit(2)

def ocr_tesseract_pdf_to_text(pdf_path: Path, dpi: int = 220, lang: str = "eng") -> str:
    """
    Render each PDF page with pypdfium2 and run Tesseract (pytesseract).
    Returns concatenated plain text.
    """
    import pypdfium2 as pdfium
    import pytesseract
    from PIL import Image

    text_pages = []
    doc = pdfium.PdfDocument(pdf_path.as_posix())
    n = len(doc)
    for i in range(n):
        page = doc[i]
        # Render to bitmap
        bitmap = page.render(scale=dpi / 72.0).to_pil()  # 72 dpi base → scale up
        # Ensure grayscale for OCR (often good enough)
        if bitmap.mode != "L":
            bitmap = bitmap.convert("L")
        page_text = pytesseract.image_to_string(bitmap, lang=lang)
        text_pages.append(page_text.strip())
    return "\n\n".join(text_pages).strip()

def main():
    if len(sys.argv) < 3:
        print("usage: run_docling.py <pdf_or_url> <out_dir>", file=sys.stderr)
        sys.exit(2)

    src = sys.argv[1]
    out_dir = Path(sys.argv[2]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Require Docling (PDF only) + our Tesseract pipeline deps
    require([
        ("docling", "docling[pdf]"),
        ("pypdfium2", "pypdfium2"),
        ("pytesseract", "pytesseract"),
    ])

    # Localize input under a cache folder
    pdf_cache = out_dir / "_cache"
    pdf_path = ensure_local_document(src, pdf_cache)

    # ---- Docling (no OCR): structure/markdown proof + object creation proof ----
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.do_ocr = False                 # we do OCR ourselves with Tesseract
    opts.do_table_structure = True
    opts.generate_page_images = False

    conv = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )

    # Proof-of-life that Docling object exists
    import docling as _dl
    print(json.dumps({
        "event": "docling_object_created",
        "docling_version": getattr(_dl, "__version__", "unknown")
    }), flush=True)

    res = conv.convert(pdf_path.as_posix())

    # Markdown via Docling (no OCR)
    md = res.document.export_to_markdown()

    # ---- Tesseract OCR → plain-text transcript ----
    # (works for scanned PDFs; also OK for born-digital but slower)
    txt = ocr_tesseract_pdf_to_text(pdf_path, dpi=220, lang="eng")

    # ---- Write artifacts ----
    md_path   = out_dir / (pdf_path.stem + ".md")
    json_path = out_dir / (pdf_path.stem + ".json")
    txt_path  = out_dir / (pdf_path.stem + ".txt")

    md_path.write_text(md, encoding="utf-8")
    # JSON best-effort (API shape may differ by version)
    try:
        json_path.write_text(res.document.model_dump_json(indent=2), encoding="utf-8")
    except Exception:
        pass
    txt_path.write_text(txt, encoding="utf-8")

    # Short snippet so Java logs show transcription clearly
    base = txt if txt.strip() else md
    lines = base.strip().splitlines()
    snippet = "\n".join(lines[:8])[:600]

    print(json.dumps({
        "status": "ok",
        "input": str(pdf_path),
        "markdown": str(md_path),
        "json": str(json_path),
        "text": str(txt_path),
        "snippet": snippet
    }), flush=True)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

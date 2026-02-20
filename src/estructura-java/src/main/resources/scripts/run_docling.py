#!/usr/bin/env python3
import argparse
import json
import logging
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
            file=sys.stderr,
        )
        sys.exit(2)


def ocr_tesseract_pdf_to_text(
    pdf_path: Path,
    dpi: int = 120,
    lang: str = "eng",
    max_pages: int | None = None,
    progress: bool = False,
) -> tuple[str, int, float]:
    """
    Render each PDF page with pypdfium2 and run Tesseract (pytesseract).
    Returns concatenated plain text.
    """
    import pypdfium2 as pdfium
    import pytesseract
    from PIL import Image

    text_pages = []
    doc = pdfium.PdfDocument(pdf_path.as_posix())
    n_total = len(doc)
    n = min(n_total, max_pages) if max_pages is not None else n_total

    total_render = 0.0
    total_ocr = 0.0

    for i in range(n):
        page = doc[i]
        t_start = time.perf_counter()
        bitmap = page.render(scale=dpi / 72.0).to_pil()  # 72 dpi base → scale up
        if bitmap.mode != "L":
            bitmap = bitmap.convert("L")
        render_elapsed = time.perf_counter() - t_start

        t_ocr_start = time.perf_counter()
        page_text = pytesseract.image_to_string(bitmap, lang=lang)
        ocr_elapsed = time.perf_counter() - t_ocr_start

        total_render += render_elapsed
        total_ocr += ocr_elapsed

        text_pages.append(page_text.strip())
        if progress:
            print(
                json.dumps(
                    {
                        "event": "ocr_page_timing",
                        "page": i + 1,
                        "total_pages": n_total,
                        "render_seconds": round(render_elapsed, 3),
                        "ocr_seconds": round(ocr_elapsed, 3),
                    }
                ),
                flush=True,
            )

    return "\n\n".join(text_pages).strip(), n, total_render + total_ocr


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Docling + Tesseract runner")
    parser.add_argument("src", help="Path or URL to PDF/image")
    parser.add_argument("out_dir", help="Output directory")
    parser.add_argument("--dpi", type=int, default=int(os.environ.get("DOCLING_OCR_DPI", "120")))
    parser.add_argument("--ocr", dest="run_ocr", action="store_true", default=True)
    parser.add_argument("--no-ocr", dest="run_ocr", action="store_false", help="Skip OCR stage")
    parser.add_argument("--docling", dest="run_docling", action="store_true", default=True)
    parser.add_argument("--no-docling", dest="run_docling", action="store_false", help="Skip Docling conversion")
    parser.add_argument("--max-pages", type=int, default=None, help="Limit OCR to first N pages")
    parser.add_argument("--progress", action="store_true", help="Emit per-page timing events")
    parser.add_argument("--use-cache", action="store_true", help="Reuse existing cached PDF if present")
    parser.add_argument(
        "--table-structure",
        dest="table_structure",
        action="store_true",
        help="Enable Docling table structure analysis",
    )
    parser.add_argument("--no-table-structure", dest="table_structure", action="store_false")
    parser.set_defaults(table_structure=False)
    parser.add_argument("--verbose", action="store_true", help="Include Docling INFO logs")
    parser.add_argument(
        "--output",
        choices=["markdown", "text"],
        default="markdown",
        help="Output format: markdown (.md) or text (.txt). Default: markdown",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None):
    args = parse_args(sys.argv[1:] if argv is None else argv)

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(message)s")

    src = args.src
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Require Docling (PDF only) + our Tesseract pipeline deps
    require(
        [
            ("docling", "docling[pdf]"),
            ("pypdfium2", "pypdfium2"),
            ("pytesseract", "pytesseract"),
        ]
    )

    # Localize input under a cache folder
    pdf_cache = out_dir / "_cache"
    ensure_cache = args.use_cache and pdf_cache.exists()
    if ensure_cache:
        try:
            desired_stem = Path(urlparse(src).path).stem or Path(src).stem
            candidates = list(pdf_cache.glob(f"{desired_stem}*")) if desired_stem else []
            if candidates:
                pdf_path = candidates[0]
            else:
                pdf_path = ensure_local_document(src, pdf_cache)
        except Exception:
            pdf_path = ensure_local_document(src, pdf_cache)
    else:
        pdf_path = ensure_local_document(src, pdf_cache)

    # ---- Docling (no OCR): structure/markdown proof + object creation proof ----
    md = ""
    res_json = None
    docling_version = "unknown"
    docling_seconds = None

    if args.run_docling:
        docling_start = time.perf_counter()
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import DocumentConverter, PdfFormatOption

        opts = PdfPipelineOptions()
        opts.do_ocr = False  # we do OCR ourselves with Tesseract
        opts.do_table_structure = args.table_structure
        opts.generate_page_images = False

        conv = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})

        import docling as _dl

        docling_version = getattr(_dl, "__version__", "unknown")
        print(
            json.dumps(
                {
                    "event": "docling_object_created",
                    "docling_version": docling_version,
                }
            ),
            flush=True,
        )

        res = conv.convert(pdf_path.as_posix())
        if args.output == "markdown":
            md = res.document.export_to_markdown()
        try:
            res_json = res.document.model_dump_json(indent=2)
        except Exception:
            res_json = None
        docling_seconds = round(time.perf_counter() - docling_start, 3)
        print(json.dumps({"event": "docling_timing", "seconds": docling_seconds}), flush=True)

    else:
        print(json.dumps({"event": "docling_skipped"}), flush=True)

    # ---- Tesseract OCR → plain-text transcript ----
    # (works for scanned PDFs; also OK for born-digital but slower)
    txt = ""
    pages_processed = 0
    ocr_seconds = None
    if args.run_ocr:
        ocr_start = time.perf_counter()
        txt, pages_processed, _ = ocr_tesseract_pdf_to_text(
            pdf_path,
            dpi=args.dpi,
            lang="eng",
            max_pages=args.max_pages,
            progress=args.progress,
        )
        ocr_seconds = round(time.perf_counter() - ocr_start, 3)
        print(json.dumps({"event": "ocr_timing", "seconds": ocr_seconds}), flush=True)
    else:
        print(json.dumps({"event": "ocr_skipped"}), flush=True)

    # ---- Write artifacts ----
    md_path = out_dir / (pdf_path.stem + ".md")
    json_path = out_dir / (pdf_path.stem + ".json")
    txt_path = out_dir / (pdf_path.stem + ".txt")

    if args.output == "markdown" and args.run_docling and md:
        md_path.write_text(md, encoding="utf-8")
    if args.run_docling and res_json:
        json_path.write_text(res_json, encoding="utf-8")
    if args.output == "text" and args.run_ocr and txt:
        txt_path.write_text(txt, encoding="utf-8")

    # Short snippet so Java logs show transcription clearly
    base = txt if txt.strip() else md
    lines = base.strip().splitlines() if base else []
    if not lines:
        snippet = "Snippet unavailable: Docling/OCR output was empty."
    else:
        snippet = "\n".join(lines[:8])[:600]

    metrics_summary = {
        "event": "metrics_summary",
        "docling": {
            "enabled": args.run_docling,
            "seconds": docling_seconds,
        },
        "ocr": {
            "enabled": args.run_ocr,
            "seconds": ocr_seconds,
            "pages": pages_processed,
            "dpi": args.dpi,
        },
        "options": {
            "table_structure": args.table_structure,
            "max_pages": args.max_pages,
            "cache_used": args.use_cache,
        },
    }
    print(json.dumps(metrics_summary), flush=True)

    print("METRICS SUMMARY", flush=True)
    docling_msg = "  Docling: skipped" if docling_seconds is None else f"  Docling: {docling_seconds:.2f}s"
    ocr_msg = (
        "  OCR: skipped"
        if ocr_seconds is None
        else f"  OCR: {ocr_seconds:.2f}s (pages={pages_processed}, dpi={args.dpi})"
    )
    tables_msg = "  Tables: enabled" if args.table_structure else "  Tables: disabled"
    cache_msg = f"  Cache reuse: {'yes' if args.use_cache else 'no'}"
    if args.max_pages:
        cache_msg += f" (max_pages={args.max_pages})"
    print(docling_msg, flush=True)
    print(ocr_msg, flush=True)
    print(tables_msg, flush=True)
    print(cache_msg, flush=True)

    print(
        json.dumps(
            {
                "status": "ok",
                "input": str(pdf_path),
                "markdown": str(md_path) if args.output == "markdown" and args.run_docling else None,
                "json": str(json_path) if args.run_docling else None,
                "text": str(txt_path) if args.output == "text" and args.run_ocr else None,
                "snippet": snippet,
            }
        ),
        flush=True,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlretrieve

def ensure_local_pdf(src: str, dst_dir: Path) -> Path:
    p = urlparse(src)
    if p.scheme in ("http", "https"):
        name = os.path.basename(p.path) or f"doc_{int(time.time())}.pdf"
        if not name.lower().endswith(".pdf"):
            name += ".pdf"
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / name
        urlretrieve(src, dst)
        # sanity: file must be non-empty
        if dst.stat().st_size == 0:
            raise RuntimeError(f"Downloaded zero-byte file from {src}")
        return dst
    path = Path(src).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(str(path))
    return path

def main():
    if len(sys.argv) < 3:
        print("usage: run_docling.py <pdf_or_url> <out_dir>", file=sys.stderr)
        sys.exit(2)

    src = sys.argv[1]
    out_dir = Path(sys.argv[2]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Lazy install if missing (or preinstall in Dockerfile for speed)
    try:
        import docling  # noqa: F401
    except ImportError:
        import subprocess, sys as _sys
        subprocess.check_call([_sys.executable, "-m", "pip", "install", "--quiet", "docling"])

    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorOptions, AcceleratorDevice
    from docling.document_converter import DocumentConverter, PdfFormatOption

    pdf_path = ensure_local_pdf(src, Path("docs"))

    opts = PdfPipelineOptions()
    opts.do_ocr = True
    opts.do_table_structure = False
    opts.generate_page_images = True
    opts.images_scale = 2.0
    opts.accelerator_options = AcceleratorOptions(num_threads=None, device=AcceleratorDevice.CPU)

    conv = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})
    res = conv.convert(pdf_path)

    md_path = out_dir / (pdf_path.stem + ".md")
    md_path.write_text(res.document.export_to_markdown(), encoding="utf-8")

    json_path = out_dir / (pdf_path.stem + ".json")
    json_path.write_text(res.document.model_dump_json(indent=2), encoding="utf-8")

    print(json.dumps({
        "status": "ok",
        "input": str(pdf_path),
        "markdown": str(md_path),
        "json": str(json_path),
    }))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

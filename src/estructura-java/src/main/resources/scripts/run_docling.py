#!/usr/bin/env python3
import argparse
import json
import logging
import mimetypes
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlretrieve

PDF_EXTS = {".pdf"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif"}
OFFICE_EXTS = {".docx", ".pptx", ".xlsx"}
ALL_KNOWN_EXTS = PDF_EXTS | IMAGE_EXTS | OFFICE_EXTS

ANNOTATION_PROMPT = (
    "Describe this figure from a document. Focus on what information "
    "it conveys (data trends, relationships, structure). Be concise "
    "(1-3 sentences). If it is a chart, mention the type and key "
    "findings. If it is a diagram, describe the components and "
    "relationships."
)


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
        if not suffix or suffix not in ALL_KNOWN_EXTS:
            content_type = headers.get_content_type() if headers else None
            guessed = (mimetypes.guess_extension(content_type or "") or "").lower()
            if guessed in ALL_KNOWN_EXTS:
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
    if suffix in OFFICE_EXTS:
        return local_path  # Docling handles DOCX/PPTX/XLSX natively
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


def annotate_stub(image_id: str, page: int, seq: int) -> str:
    """Return a placeholder caption for offline/testing use."""
    return f"[Placeholder: figure on page {page}, region {seq}]"


MIN_CROP_SIZE = 50
MAX_CROP_SIDE = 1024


def preprocess_crop(image_path: Path, image_id: str):
    """Load and preprocess a crop image for annotation.

    Returns a PIL Image ready for annotation, or None if the crop is too
    small (below MIN_CROP_SIZE on either dimension). Resizes crops whose
    longest side exceeds MAX_CROP_SIDE to reduce API token usage. Logs
    original and final dimensions for every crop.
    """
    from PIL import Image

    if not image_path.exists():
        logging.warning("Crop file missing for %s: %s", image_id, image_path)
        return None

    img = Image.open(image_path)
    orig_w, orig_h = img.size

    if orig_w < MIN_CROP_SIZE or orig_h < MIN_CROP_SIZE:
        logging.warning(
            "Crop %s too small (%dx%d, min %dx%d) -- skipping annotation",
            image_id, orig_w, orig_h, MIN_CROP_SIZE, MIN_CROP_SIZE,
        )
        return None

    longest = max(orig_w, orig_h)
    if longest > MAX_CROP_SIDE:
        scale = MAX_CROP_SIDE / longest
        new_w = int(orig_w * scale)
        new_h = int(orig_h * scale)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        logging.info(
            "Crop %s resized from %dx%d to %dx%d",
            image_id, orig_w, orig_h, new_w, new_h,
        )
    else:
        logging.info("Crop %s dimensions %dx%d (no resize needed)", image_id, orig_w, orig_h)

    return img


def annotate_gemma(img, image_id: str, model: str, api_key: str) -> str:
    """Annotate a preprocessed crop image via Google AI Studio.

    Accepts an already-loaded PIL Image (from preprocess_crop), sends it
    with ANNOTATION_PROMPT to the model, and returns the caption text.
    Retries up to 3 times with exponential backoff for transient errors.
    Falls back to a placeholder caption on permanent failure.
    """
    from google import genai

    client = genai.Client(api_key=api_key)

    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        start = time.perf_counter()
        try:
            response = client.models.generate_content(
                model=model,
                contents=[ANNOTATION_PROMPT, img],
            )
            elapsed = time.perf_counter() - start
            caption = response.text.strip()
            logging.info("Annotated %s in %.2fs (attempt %d)", image_id, elapsed, attempt)
            return caption
        except Exception as exc:
            elapsed = time.perf_counter() - start
            exc_str = str(exc).lower()
            retryable = any(
                kw in exc_str
                for kw in (
                    "429", "500", "503",
                    "rate", "resource exhausted",
                    "deadline", "timeout", "unavailable", "internal",
                )
            )
            if retryable and attempt < max_attempts:
                wait = 2 ** (attempt - 1)  # 1s, 2s
                logging.warning(
                    "Transient error annotating %s (attempt %d/%d, %.2fs): %s. "
                    "Retrying in %ds...",
                    image_id, attempt, max_attempts, elapsed, exc, wait,
                )
                time.sleep(wait)
            else:
                logging.warning(
                    "Annotation failed for %s after %d attempt(s) (%.2fs): %s. "
                    "Using placeholder.",
                    image_id, attempt, elapsed, exc,
                )
                return f"[Annotation failed: {image_id}]"

    return f"[Annotation failed: {image_id}]"


def annotate_image(
    image_path: Path,
    image_id: str,
    page: int,
    seq: int,
    mode: str,
    model: str | None = None,
    api_key: str | None = None,
) -> str:
    """Dispatch annotation to the appropriate backend based on mode.

    Preprocesses the crop (min-size filter, optional resize) before routing
    to annotate_stub() for offline/testing or annotate_gemma() for real
    vision model annotation via Google AI Studio.
    """
    img = preprocess_crop(image_path, image_id)
    if img is None:
        return f"[Crop too small or missing: {image_id}]"

    if mode == "stub":
        return annotate_stub(image_id, page, seq)
    elif mode == "gemma":
        return annotate_gemma(img, image_id, model, api_key)
    else:
        raise ValueError(f"Unknown annotation mode: {mode}")


def assemble_interleaved_output(
    document,
    figure_map: dict[int, str],
    annotations: dict[str, str],
    output_format: str,
) -> str:
    """Build output with image anchors interleaved at figure positions.

    Iterates the Docling document model in reading order, emitting text
    paragraphs and image anchors at their source positions. For PictureItems
    present in figure_map, inserts an anchor with the caption from
    annotations (or "[No caption available]" if absent).
    """
    from docling_core.types.doc.document import PictureItem, TableItem

    parts: list[str] = []
    is_md = output_format == "markdown"

    for item, level in document.iterate_items():
        if isinstance(item, PictureItem):
            image_id = figure_map.get(id(item))
            if image_id is None:
                continue
            rel_crop = "images/crops/" + image_id.removeprefix("img-") + ".png"
            caption = annotations.get(image_id, "[No caption available]")
            if is_md:
                parts.append(f"![{image_id}]({rel_crop})")
                parts.append(f"*{caption}*")
            else:
                parts.append(f"[IMAGE: {image_id} | {rel_crop}]\n  {caption}")

        elif isinstance(item, TableItem):
            try:
                parts.append(item.export_to_markdown(doc=document))
            except Exception:
                text = getattr(item, "text", "")
                if text:
                    parts.append(text)

        else:
            text = getattr(item, "text", "")
            if not text:
                continue
            label_str = str(getattr(item, "label", "")).lower()
            if is_md:
                if "title" in label_str:
                    parts.append("# " + text)
                elif "header" in label_str:
                    heading_level = min(level + 1, 6)
                    parts.append("#" * heading_level + " " + text)
                elif "list" in label_str:
                    marker = getattr(item, "enumeration_marker", "-") or "-"
                    parts.append(f"{marker} {text}")
                elif "code" in label_str:
                    parts.append(f"```\n{text}\n```")
                else:
                    parts.append(text)
            else:
                parts.append(text)

    return "\n\n".join(parts)


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
    parser.add_argument("src", help="Path or URL to PDF, DOCX, PPTX, XLSX, or image")
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
    parser.add_argument(
        "--image-capture",
        dest="image_capture",
        action="store_true",
        help="Enable page image capture for image-aware pipeline",
    )
    parser.add_argument("--no-image-capture", dest="image_capture", action="store_false")
    parser.set_defaults(image_capture=False)
    parser.add_argument(
        "--max-image-pages",
        type=int,
        default=50,
        help="Max pages to capture images from (default: 50)",
    )
    parser.add_argument(
        "--max-images-per-page",
        type=int,
        default=20,
        help="Max image crops per page (default: 20)",
    )
    parser.add_argument(
        "--max-total-images",
        type=int,
        default=200,
        help="Max total image crops across all pages (default: 200)",
    )
    parser.add_argument(
        "--annotate",
        nargs="?",
        const="stub",
        default=None,
        choices=["stub", "gemma"],
        help="Annotation mode: stub (placeholder captions) or gemma (Google AI Studio). "
        "Implicitly enables --image-capture. Default when flag present: stub",
    )
    parser.add_argument(
        "--gemma-model",
        default="gemma-3-27b-it",
        help="Gemma model ID for annotation (default: gemma-3-27b-it)",
    )
    parser.add_argument(
        "--save-json",
        dest="save_json",
        action="store_true",
        help="Export DoclingDocument structure as JSON alongside output",
    )
    parser.set_defaults(save_json=False)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None):
    args = parse_args(sys.argv[1:] if argv is None else argv)

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(message)s")

    # Annotation implies image capture (crops are required for annotation)
    if args.annotate is not None:
        args.image_capture = True

    # Validate API key for gemma mode
    google_api_key = None
    if args.annotate == "gemma":
        google_api_key = os.environ.get("GOOGLE_API_KEY", "").strip()
        if not google_api_key:
            print(
                "Error: --annotate gemma requires GOOGLE_API_KEY environment variable.\n"
                "Get an API key at https://aistudio.google.com/apikey",
                file=sys.stderr,
            )
            return 1

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
    doc_cache = out_dir / "_cache"
    ensure_cache = args.use_cache and doc_cache.exists()
    if ensure_cache:
        try:
            desired_stem = Path(urlparse(src).path).stem or Path(src).stem
            candidates = list(doc_cache.glob(f"{desired_stem}*")) if desired_stem else []
            if candidates:
                doc_path = candidates[0]
            else:
                doc_path = ensure_local_document(src, doc_cache)
        except Exception:
            doc_path = ensure_local_document(src, doc_cache)
    else:
        doc_path = ensure_local_document(src, doc_cache)

    is_pdf = doc_path.suffix.lower() in PDF_EXTS

    # ---- Docling: structure/markdown extraction ----
    md = ""
    txt = ""
    docling_version = "unknown"
    docling_seconds = None
    page_images_count = 0
    crops_count = 0
    crop_failures = 0
    annotations: dict[str, str] = {}
    figure_map: dict[int, str] = {}  # id(PictureItem) -> image_id
    images_annotated = 0
    annotation_failures = 0
    total_annotation_seconds = 0.0

    if args.run_docling:
        docling_start = time.perf_counter()
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import DocumentConverter, PdfFormatOption

        opts = PdfPipelineOptions()
        opts.do_ocr = (args.output == "markdown")  # RapidOCR populates document model for Markdown; TXT uses Tesseract
        opts.do_table_structure = args.table_structure
        opts.generate_page_images = args.image_capture
        opts.generate_picture_images = args.image_capture
        opts.images_scale = 2.0

        # Docling handles DOCX/PPTX/XLSX natively; only PDF needs custom options.
        conv = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})

        from importlib.metadata import version as _pkg_version

        docling_version = _pkg_version("docling")
        print(
            json.dumps(
                {
                    "event": "docling_object_created",
                    "docling_version": docling_version,
                }
            ),
            flush=True,
        )

        res = conv.convert(doc_path.as_posix())
        docling_seconds = round(time.perf_counter() - docling_start, 3)
        print(json.dumps({"event": "docling_timing", "seconds": docling_seconds}), flush=True)

        # ---- Page image capture (PDF only) ----
        if args.image_capture and is_pdf:
            pages_dir = out_dir / "images" / "pages"
            pages_dir.mkdir(parents=True, exist_ok=True)
            captured_pages: set[int] = set()
            pages_limit_hit = False
            for page_no in sorted(res.document.pages.keys()):
                if len(captured_pages) >= args.max_image_pages:
                    if not pages_limit_hit:
                        logging.warning(
                            "Max image pages limit reached (%d). Skipping remaining pages.",
                            args.max_image_pages,
                        )
                        pages_limit_hit = True
                    break
                page = res.document.pages[page_no]
                if page.image is not None:
                    img_path = pages_dir / f"page_{page_no:03d}.png"
                    page.image.pil_image.save(img_path, "PNG")
                    page_images_count += 1
                    captured_pages.add(page_no)
            print(json.dumps({"event": "page_images_captured", "count": page_images_count}), flush=True)

            # ---- Crop extraction from PictureItem images ----
            from docling_core.types.doc.document import PictureItem

            crops_dir = out_dir / "images" / "crops"
            crops_dir.mkdir(parents=True, exist_ok=True)
            page_seq: dict[int, int] = {}  # page_no -> next sequence number
            manifest_entries: list[tuple[str, int, int, str, str]] = []  # (id, page, seq, bbox_str, rel_path)
            total_limit_hit = False
            per_page_limit_pages: set[int] = set()  # pages where per-page limit was hit

            for item, _level in res.document.iterate_items():
                if not isinstance(item, PictureItem):
                    continue
                if not item.prov:
                    continue

                prov = item.prov[0]
                pg = prov.page_no

                # Skip pages not captured (beyond max-image-pages limit)
                if pg not in captured_pages:
                    continue

                # Check total limit
                if crops_count + crop_failures >= args.max_total_images:
                    if not total_limit_hit:
                        logging.warning(
                            "Max total images limit reached (%d). Skipping remaining figures.",
                            args.max_total_images,
                        )
                        total_limit_hit = True
                    continue

                # Check per-page limit
                seq = page_seq.get(pg, 1)
                if seq > args.max_images_per_page:
                    if pg not in per_page_limit_pages:
                        logging.warning(
                            "Max images per page limit reached (%d) for page %d. Skipping.",
                            args.max_images_per_page,
                            pg,
                        )
                        per_page_limit_pages.add(pg)
                    continue

                # Use Docling's pre-cropped image (generate_picture_images=True)
                if item.image is None:
                    continue
                try:
                    crop_img = item.image.pil_image
                except Exception:
                    continue

                # Build bbox string from provenance for manifest
                page_data = res.document.pages.get(pg)
                if page_data is not None:
                    bbox = prov.bbox.to_top_left_origin(page_data.size.height)
                    bbox_str = f"{bbox.l:.1f},{bbox.t:.1f},{bbox.r:.1f},{bbox.b:.1f}"
                else:
                    bbox_str = "0.0,0.0,0.0,0.0"

                page_seq[pg] = seq + 1
                image_id = f"img-p{pg:03d}-{seq:02d}"
                figure_map[id(item)] = image_id
                rel_crop = f"images/crops/p{pg:03d}-{seq:02d}.png"
                crop_path = crops_dir / f"p{pg:03d}-{seq:02d}.png"

                try:
                    crop_img.save(crop_path, "PNG")
                    crops_count += 1
                except Exception as exc:
                    crop_failures += 1
                    logging.warning("Crop failed for page %d seq %d: %s", pg, seq, exc)

                # Record in manifest regardless of crop success (per output contract)
                manifest_entries.append((image_id, pg, seq, bbox_str, rel_crop))

            # ---- Write manifest ----
            manifest_path = out_dir / "images" / "manifest.txt"
            with manifest_path.open("w", encoding="utf-8") as mf:
                mf.write("# id | page | bbox_left,bbox_top,bbox_right,bbox_bottom | crop_path\n")
                for img_id, pg, _seq, bbox_s, rel_path in manifest_entries:
                    mf.write(f"{img_id} | {pg} | {bbox_s} | {rel_path}\n")

            print(json.dumps({"event": "crops_extracted", "count": crops_count, "failures": crop_failures}), flush=True)

            # ---- Annotate extracted images ----
            if args.annotate is not None and manifest_entries:
                for img_id, pg, img_seq, _bbox_s, rel_path in manifest_entries:
                    crop_path = out_dir / rel_path
                    ann_start = time.perf_counter()
                    caption = annotate_image(
                        crop_path,
                        img_id,
                        pg,
                        img_seq,
                        mode=args.annotate,
                        model=args.gemma_model,
                        api_key=google_api_key,
                    )
                    ann_elapsed = time.perf_counter() - ann_start
                    total_annotation_seconds += ann_elapsed
                    annotations[img_id] = caption
                    failed = caption.startswith("[")
                    if failed:
                        annotation_failures += 1
                    else:
                        images_annotated += 1
                    print(json.dumps({"event": "annotation_timing", "image_id": img_id, "seconds": round(ann_elapsed, 3), "failed": failed}), flush=True)

        elif args.image_capture and not is_pdf:
            # ---- Non-PDF image extraction (PPTX/DOCX/XLSX) ----
            # Docling's SimplePipeline populates PictureItem.image directly
            # from embedded images. No page rendering needed.
            from docling_core.types.doc.document import PictureItem

            crops_dir = out_dir / "images" / "crops"
            crops_dir.mkdir(parents=True, exist_ok=True)
            page_seq: dict[int, int] = {}
            manifest_entries: list[tuple[str, int, int, str, str]] = []
            total_limit_hit = False
            per_page_limit_pages: set[int] = set()

            for item, _level in res.document.iterate_items():
                if not isinstance(item, PictureItem):
                    continue
                if not item.prov:
                    continue

                prov = item.prov[0]
                pg = prov.page_no

                # Check total limit
                if crops_count + crop_failures >= args.max_total_images:
                    if not total_limit_hit:
                        logging.warning(
                            "Max total images limit reached (%d). Skipping remaining figures.",
                            args.max_total_images,
                        )
                        total_limit_hit = True
                    continue

                # Check per-page limit
                seq = page_seq.get(pg, 1)
                if seq > args.max_images_per_page:
                    if pg not in per_page_limit_pages:
                        logging.warning(
                            "Max images per page limit reached (%d) for page %d. Skipping.",
                            args.max_images_per_page,
                            pg,
                        )
                        per_page_limit_pages.add(pg)
                    continue

                if item.image is None:
                    continue
                try:
                    crop_img = item.image.pil_image
                except Exception:
                    continue

                bbox_str = f"{prov.bbox.l:.1f},{prov.bbox.t:.1f},{prov.bbox.r:.1f},{prov.bbox.b:.1f}"

                page_seq[pg] = seq + 1
                image_id = f"img-p{pg:03d}-{seq:02d}"
                figure_map[id(item)] = image_id
                rel_crop = f"images/crops/p{pg:03d}-{seq:02d}.png"
                crop_path = crops_dir / f"p{pg:03d}-{seq:02d}.png"

                try:
                    crop_img.save(crop_path, "PNG")
                    crops_count += 1
                except Exception as exc:
                    crop_failures += 1
                    logging.warning("Crop failed for page %d seq %d: %s", pg, seq, exc)

                manifest_entries.append((image_id, pg, seq, bbox_str, rel_crop))

            # Write manifest
            if manifest_entries:
                manifest_path = out_dir / "images" / "manifest.txt"
                with manifest_path.open("w", encoding="utf-8") as mf:
                    mf.write("# id | page | bbox_left,bbox_top,bbox_right,bbox_bottom | crop_path\n")
                    for img_id, pg, _seq, bbox_s, rel_path in manifest_entries:
                        mf.write(f"{img_id} | {pg} | {bbox_s} | {rel_path}\n")

            print(json.dumps({"event": "crops_extracted", "count": crops_count, "failures": crop_failures}), flush=True)

            # Annotate extracted images
            if args.annotate is not None and manifest_entries:
                for img_id, pg, img_seq, _bbox_s, rel_path in manifest_entries:
                    crop_path = out_dir / rel_path
                    ann_start = time.perf_counter()
                    caption = annotate_image(
                        crop_path,
                        img_id,
                        pg,
                        img_seq,
                        mode=args.annotate,
                        model=args.gemma_model,
                        api_key=google_api_key,
                    )
                    ann_elapsed = time.perf_counter() - ann_start
                    total_annotation_seconds += ann_elapsed
                    annotations[img_id] = caption
                    failed = caption.startswith("[")
                    if failed:
                        annotation_failures += 1
                    else:
                        images_annotated += 1
                    print(json.dumps({"event": "annotation_timing", "image_id": img_id, "seconds": round(ann_elapsed, 3), "failed": failed}), flush=True)

        # ---- Assemble output (interleaved when figures were processed) ----
        if figure_map:
            if args.output == "markdown":
                md = assemble_interleaved_output(res.document, figure_map, annotations, "markdown")
            elif args.output == "text" and not is_pdf:
                txt = assemble_interleaved_output(res.document, figure_map, annotations, "text")
        else:
            if args.output == "markdown":
                md = re.sub(r"^<!-- image -->\n*", "", res.document.export_to_markdown(), flags=re.MULTILINE)
            elif args.output == "text" and not is_pdf:
                txt = re.sub(r"^<!-- image -->\n*", "", res.document.export_to_markdown(), flags=re.MULTILINE)

    else:
        print(json.dumps({"event": "docling_skipped"}), flush=True)
        if args.image_capture:
            print(json.dumps({"event": "image_capture_skipped", "reason": "docling disabled"}), flush=True)

    # ---- Tesseract OCR -> plain-text transcript (PDF only) ----
    pages_processed = 0
    ocr_seconds = None
    if args.run_ocr and is_pdf:
        ocr_start = time.perf_counter()
        txt, pages_processed, _ = ocr_tesseract_pdf_to_text(
            doc_path,
            dpi=args.dpi,
            lang="eng",
            max_pages=args.max_pages,
            progress=args.progress,
        )
        ocr_seconds = round(time.perf_counter() - ocr_start, 3)
        print(json.dumps({"event": "ocr_timing", "seconds": ocr_seconds}), flush=True)
    elif args.run_ocr and not is_pdf:
        print(json.dumps({"event": "ocr_skipped", "reason": "non-pdf input"}), flush=True)
    else:
        print(json.dumps({"event": "ocr_skipped"}), flush=True)

    # Append image anchors to OCR text when figures were extracted (PDF + text mode)
    if figure_map and args.output == "text" and is_pdf and txt:
        anchor_lines = []
        for image_id in sorted(figure_map.values()):
            rel_crop = "images/crops/" + image_id.removeprefix("img-") + ".png"
            caption = annotations.get(image_id, "[No caption available]")
            anchor_lines.append(f"[IMAGE: {image_id} | {rel_crop}]\n  {caption}")
        if anchor_lines:
            txt = txt.rstrip() + "\n\n" + "\n\n".join(anchor_lines) + "\n"

    # ---- Write artifacts ----
    md_path = out_dir / (doc_path.stem + ".md")
    txt_path = out_dir / (doc_path.stem + ".txt")

    if args.output == "markdown" and args.run_docling and md:
        md_path.write_text(md, encoding="utf-8")
    if args.output == "text" and txt:
        txt_path.write_text(txt, encoding="utf-8")

    if args.save_json and args.run_docling:
        json_path = out_dir / (doc_path.stem + ".json")
        json_path.write_text(json.dumps(res.document.export_to_dict(), default=str), encoding="utf-8")
        print(json.dumps({"event": "json_exported", "path": str(json_path)}), flush=True)

    metrics_summary = {
        "event": "metrics_summary",
        "docling": {
            "enabled": args.run_docling,
            "seconds": docling_seconds,
        },
        "ocr": {
            "enabled": args.run_ocr and is_pdf,
            "seconds": ocr_seconds,
            "pages": pages_processed,
            "dpi": args.dpi,
        },
        "options": {
            "table_structure": args.table_structure,
            "image_capture": args.image_capture,
            "max_pages": args.max_pages,
            "max_image_pages": args.max_image_pages,
            "max_images_per_page": args.max_images_per_page,
            "max_total_images": args.max_total_images,
            "cache_used": args.use_cache,
        },
        "image_capture": {
            "enabled": args.image_capture,
            "pages_saved": page_images_count,
            "crops_extracted": crops_count,
            "crop_failures": crop_failures,
        },
        "annotation": {
            "enabled": args.annotate is not None,
            "mode": args.annotate,
            "images_annotated": images_annotated,
            "annotation_failures": annotation_failures,
            "total_annotation_seconds": round(total_annotation_seconds, 3),
            "avg_annotation_seconds": (
                round(total_annotation_seconds / (images_annotated + annotation_failures), 3)
                if (images_annotated + annotation_failures) > 0
                else None
            ),
        },
    }
    print(json.dumps(metrics_summary), flush=True)

    print("METRICS SUMMARY", flush=True)
    docling_msg = "  Docling: skipped" if docling_seconds is None else f"  Docling: {docling_seconds:.2f}s"
    if args.run_ocr and not is_pdf:
        ocr_msg = "  OCR: skipped (non-PDF input)"
    elif ocr_seconds is None:
        ocr_msg = "  OCR: skipped"
    else:
        ocr_msg = f"  OCR: {ocr_seconds:.2f}s (pages={pages_processed}, dpi={args.dpi})"
    tables_msg = "  Tables: enabled" if args.table_structure else "  Tables: disabled"
    if args.image_capture and is_pdf:
        capture_msg = f"  Image capture: {page_images_count} pages, {crops_count} crops"
        if crop_failures > 0:
            capture_msg += f", {crop_failures} failures"
        capture_msg += (
            f" (limits: pages={args.max_image_pages}"
            f", per_page={args.max_images_per_page}"
            f", total={args.max_total_images})"
        )
    elif args.image_capture and crops_count > 0:
        capture_msg = f"  Image capture: {crops_count} crops (embedded images)"
        if crop_failures > 0:
            capture_msg += f", {crop_failures} failures"
    elif args.image_capture:
        capture_msg = "  Image capture: no images found"
    else:
        capture_msg = "  Image capture: disabled"
    if args.annotate is not None:
        total_ann = images_annotated + annotation_failures
        if total_ann > 0:
            avg = total_annotation_seconds / total_ann
            ann_msg = (
                f"  Annotation: {images_annotated} annotated"
                f", {annotation_failures} failures"
                f", {total_annotation_seconds:.2f}s total"
                f", {avg:.2f}s avg ({args.annotate} mode)"
            )
        else:
            ann_msg = f"  Annotation: no images to annotate ({args.annotate} mode)"
    else:
        ann_msg = "  Annotation: disabled"
    cache_msg = f"  Cache reuse: {'yes' if args.use_cache else 'no'}"
    if args.max_pages:
        cache_msg += f" (max_pages={args.max_pages})"
    print(docling_msg, flush=True)
    print(ocr_msg, flush=True)
    print(tables_msg, flush=True)
    print(capture_msg, flush=True)
    print(ann_msg, flush=True)
    print(cache_msg, flush=True)

    print(
        json.dumps(
            {
                "status": "ok",
                "input": str(doc_path),
                "markdown": str(md_path) if args.output == "markdown" and args.run_docling else None,
                "text": str(txt_path) if args.output == "text" and txt else None,
                "json": str(out_dir / (doc_path.stem + ".json")) if args.save_json and args.run_docling else None,
            }
        ),
        flush=True,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

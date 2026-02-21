#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output_dir")
    parser.add_argument("--dpi", type=int, default=None)
    parser.add_argument("--no-docling", action="store_true")
    parser.add_argument("--no-ocr", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--use-cache", action="store_true")
    parser.add_argument("--table-structure", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--image-annotations", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--image-capture", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--max-pages", type=int, default=None)
    parser.add_argument("--max-image-pages", type=int, default=50)
    parser.add_argument("--max-images-per-page", type=int, default=20)
    parser.add_argument("--max-total-images", type=int, default=200)
    parser.add_argument("--output", choices=["markdown", "text"], default="markdown")

    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    stem = input_path.stem
    if "exit1" in stem:
        print("simulated failure", file=sys.stderr)
        return 1

    if "badstatus" in stem:
        print(json.dumps({"event": "docling_object_created", "docling_version": "test-version"}))
        print(json.dumps({"status": "error", "message": "forced failure"}))
        return 0

    if args.no_docling:
        print(json.dumps({"event": "docling_skipped"}))
    else:
        if args.output == "markdown":
            md_path = out_dir / f"{stem}.md"
            md_path.write_text("# fake markdown", encoding="utf-8")
        print(json.dumps({"event": "docling_object_created", "docling_version": "test-version"}))

    if args.no_ocr:
        print(json.dumps({"event": "ocr_skipped"}))
    else:
        if args.output == "text":
            txt_path = out_dir / f"{stem}.txt"
            txt_path.write_text("fake transcript", encoding="utf-8")
        if args.progress:
            print(
                json.dumps(
                    {
                        "event": "ocr_page_timing",
                        "page": 1,
                        "total_pages": 1,
                        "render_seconds": 0.0,
                        "ocr_seconds": 0.0,
                    }
                )
            )
        print(json.dumps({"event": "ocr_timing", "seconds": 0.1}))

    metrics_summary = {
        "event": "metrics_summary",
        "docling": {
            "enabled": not args.no_docling,
            "seconds": 0.2 if not args.no_docling else None,
        },
        "ocr": {
            "enabled": not args.no_ocr,
            "seconds": 0.1 if not args.no_ocr else None,
            "pages": 1 if not args.no_ocr else 0,
            "dpi": args.dpi,
        },
        "options": {
            "table_structure": args.table_structure,
            "image_annotations": args.image_annotations,
            "image_capture": args.image_capture,
            "max_pages": args.max_pages,
            "max_image_pages": args.max_image_pages,
            "max_images_per_page": args.max_images_per_page,
            "max_total_images": args.max_total_images,
            "cache_used": args.use_cache,
        },
    }
    print(json.dumps(metrics_summary))
    print("METRICS SUMMARY")
    print("  Docling: skipped" if args.no_docling else "  Docling: 0.20s")
    print("  OCR: skipped" if args.no_ocr else f"  OCR: 0.10s (pages=1, dpi={args.dpi})")
    print("  Tables: disabled")
    cache_msg = f"  Cache reuse: {'yes' if args.use_cache else 'no'}"
    if args.max_pages:
        cache_msg += f" (max_pages={args.max_pages})"
    print(cache_msg)

    print(
        json.dumps(
            {
                "status": "ok",
                "input": str(input_path),
                "markdown": str(out_dir / f"{stem}.md") if args.output == "markdown" and not args.no_docling else None,
                "text": str(out_dir / f"{stem}.txt") if args.output == "text" and not args.no_ocr else None,
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: fake_docling_runner.py <input> <output_dir>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    stem = input_path.stem
    if "exit1" in stem:
        print("simulated failure", file=sys.stderr)
        return 1

    if "badstatus" in stem:
        print(json.dumps({"event": "docling_object_created", "docling_version": "test-version"}))
        print(json.dumps({"status": "error", "message": "forced failure"}))
        return 0

    md_path = out_dir / f"{stem}.md"
    json_path = out_dir / f"{stem}.json"
    txt_path = out_dir / f"{stem}.txt"

    md_path.write_text("# fake markdown", encoding="utf-8")
    json_path.write_text("{}", encoding="utf-8")
    txt_path.write_text("fake transcript", encoding="utf-8")

    print(json.dumps({"event": "docling_object_created", "docling_version": "test-version"}))
    print(json.dumps({
        "status": "ok",
        "input": str(input_path),
        "markdown": str(md_path),
        "json": str(json_path),
        "text": str(txt_path),
        "snippet": "fake transcript"
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Compare two markdown files and report quality metrics.

Supports two modes:
  - Self-consistency: compare any two markdown outputs (e.g., two pipeline configs)
  - Golden-reference: compare pipeline output against a golden reference file

Metrics reported:
  - Character-level edit similarity (rapidfuzz.fuzz.ratio)
  - Token-level similarity (rapidfuzz.fuzz.token_sort_ratio)
  - Heading structure comparison (count by level, text overlap)
  - Table block count
  - Line/word/character counts

Usage:
  python3 scripts/compare-quality.py file_a.md file_b.md
  python3 scripts/compare-quality.py file_a.md file_b.md --mode golden-reference
  python3 scripts/compare-quality.py file_a.md file_b.md --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def parse_headings(text: str) -> list[tuple[int, str]]:
    """Extract (level, text) tuples from markdown headings."""
    headings = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            headings.append((len(m.group(1)), m.group(2).strip()))
    return headings


def count_tables(text: str) -> int:
    """Count markdown table blocks by separator rows (|---|)."""
    return len(re.findall(r"^\|[-| :]+\|$", text, re.MULTILINE))


def text_stats(text: str) -> dict:
    """Compute line, word, and character counts."""
    lines = text.splitlines()
    words = text.split()
    return {
        "lines": len(lines),
        "words": len(words),
        "characters": len(text),
    }


def heading_overlap(headings_a: list[tuple[int, str]], headings_b: list[tuple[int, str]]) -> float:
    """Compute Jaccard overlap of heading texts."""
    texts_a = {h[1].lower() for h in headings_a}
    texts_b = {h[1].lower() for h in headings_b}
    if not texts_a and not texts_b:
        return 1.0
    if not texts_a or not texts_b:
        return 0.0
    return len(texts_a & texts_b) / len(texts_a | texts_b)


def heading_counts(headings: list[tuple[int, str]]) -> dict[int, int]:
    """Count headings by level."""
    counts: dict[int, int] = {}
    for level, _ in headings:
        counts[level] = counts.get(level, 0) + 1
    return counts


def compare(text_a: str, text_b: str) -> dict:
    """Run all comparison metrics on two texts."""
    from rapidfuzz import fuzz

    headings_a = parse_headings(text_a)
    headings_b = parse_headings(text_b)

    return {
        "edit_similarity": round(fuzz.ratio(text_a, text_b), 2),
        "token_similarity": round(fuzz.token_sort_ratio(text_a, text_b), 2),
        "headings": {
            "file_a": heading_counts(headings_a),
            "file_b": heading_counts(headings_b),
            "overlap": round(heading_overlap(headings_a, headings_b), 4),
        },
        "tables": {
            "file_a": count_tables(text_a),
            "file_b": count_tables(text_b),
        },
        "stats": {
            "file_a": text_stats(text_a),
            "file_b": text_stats(text_b),
        },
    }


def format_heading_counts(counts: dict[int, int]) -> str:
    """Format heading counts as 'H1:2, H2:5, H3:1'."""
    if not counts:
        return "(none)"
    return ", ".join(f"H{k}:{v}" for k, v in sorted(counts.items()))


def print_report(results: dict, path_a: str, path_b: str, mode: str) -> None:
    """Print a human-readable text report."""
    label_a = "Output" if mode == "golden-reference" else "File A"
    label_b = "Golden" if mode == "golden-reference" else "File B"

    print(f"Quality Comparison Report ({mode})")
    print("=" * 60)
    print(f"  {label_a}: {path_a}")
    print(f"  {label_b}: {path_b}")
    print()

    print("Text Similarity")
    print("-" * 40)
    print(f"  Edit similarity (char):   {results['edit_similarity']:.2f}%")
    print(f"  Token similarity:         {results['token_similarity']:.2f}%")
    print()

    print("Heading Structure")
    print("-" * 40)
    print(f"  {label_a}: {format_heading_counts(results['headings']['file_a'])}")
    print(f"  {label_b}: {format_heading_counts(results['headings']['file_b'])}")
    print(f"  Heading text overlap:     {results['headings']['overlap']:.1%}")
    print()

    print("Table Blocks")
    print("-" * 40)
    print(f"  {label_a}: {results['tables']['file_a']}")
    print(f"  {label_b}: {results['tables']['file_b']}")
    print()

    print("Document Size")
    print("-" * 40)
    sa = results["stats"]["file_a"]
    sb = results["stats"]["file_b"]
    print(f"  {label_a}: {sa['lines']} lines, {sa['words']} words, {sa['characters']} chars")
    print(f"  {label_b}: {sb['lines']} lines, {sb['words']} words, {sb['characters']} chars")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compare two markdown files and report quality metrics",
    )
    parser.add_argument("file_a", help="First markdown file (or pipeline output)")
    parser.add_argument("file_b", help="Second markdown file (or golden reference)")
    parser.add_argument(
        "--mode",
        choices=["self-consistency", "golden-reference"],
        default="self-consistency",
        help="Comparison mode (default: self-consistency)",
    )
    parser.add_argument(
        "--json",
        dest="json_output",
        action="store_true",
        help="Output results as JSON instead of text report",
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    path_a = Path(args.file_a)
    path_b = Path(args.file_b)

    if not path_a.is_file():
        print(f"Error: {path_a} not found", file=sys.stderr)
        return 1
    if not path_b.is_file():
        print(f"Error: {path_b} not found", file=sys.stderr)
        return 1

    text_a = path_a.read_text(encoding="utf-8")
    text_b = path_b.read_text(encoding="utf-8")

    results = compare(text_a, text_b)

    if args.json_output:
        output = {
            "mode": args.mode,
            "file_a": str(path_a),
            "file_b": str(path_b),
            **results,
        }
        print(json.dumps(output, indent=2))
    else:
        print_report(results, str(path_a), str(path_b), args.mode)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Download verified paper PDFs into local/papers/.

Usage:
    python scripts/download_papers.py [--dry-run]

URLs are the open-access PDF links verified in research/bibliography.bib
and research/literature/cadence/verified_literature_review.md.
"""
from __future__ import annotations

import argparse
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "local" / "papers"

PAPERS = [
    ("kiernan_2023", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10255839/pdf/"),
    ("benson_2019", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6480623/pdf/"),
    ("mason_2022", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9807497/pdf/"),
    ("prasanth_2021", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8069962/pdf/"),
    ("lin_2025", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12158269/pdf/"),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    DEST.mkdir(parents=True, exist_ok=True)
    for name, url in PAPERS:
        dest = DEST / f"{name}.pdf"
        if args.dry_run:
            print(f"DRY-RUN: would download {url} -> {dest}")
            continue
        print(f"downloading {url} -> {dest}")
        try:
            urllib.request.urlretrieve(url, dest)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}", file=sys.stderr)
            return 1
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

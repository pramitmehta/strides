"""Download registered datasets into local/datasets/ with checksum verification.

Usage:
    python scripts/download_datasets.py [--dataset zenodo_16541185] [--dry-run]

Reads research/datasets/dataset-register.yaml. Downloads only entries whose
source_url/archive are populated. Verifies MD5 when provided. Writes to
local/datasets/<dataset_id>/ (gitignored).
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "research" / "datasets" / "dataset-register.yaml"
DEST_ROOT = ROOT / "local" / "datasets"


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"  downloading {url} -> {dest}")
    urllib.request.urlretrieve(url, dest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", help="dataset id to download (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="print plan only")
    args = parser.parse_args()

    data = yaml.safe_load(REGISTER.read_text())
    datasets = data.get("datasets", [])
    if args.dataset:
        datasets = [d for d in datasets if d["id"] == args.dataset]
        if not datasets:
            print(f"unknown dataset: {args.dataset}", file=sys.stderr)
            return 2

    for ds in datasets:
        print(f"[{ds['id']}] {ds.get('title')}")
        ds_dir = DEST_ROOT / ds["id"]
        ds_dir.mkdir(parents=True, exist_ok=True)

        # Zenodo single-archive case
        archive = ds.get("archive")
        md5 = ds.get("archive_md5")
        if archive and ds.get("source_url", "").startswith("https://zenodo.org"):
            # Derive download URL from Zenodo record files endpoint is not in register;
            # user must populate 'download_url' for automated fetch.
            url = ds.get("download_url")
            if not url:
                print("  no download_url in register; skipping (add manually)")
                continue
            dest = ds_dir / archive
            if args.dry_run:
                print(f"  DRY-RUN: would download {url} -> {dest}")
                continue
            download(url, dest)
            if md5:
                actual = md5_file(dest)
                if actual != md5:
                    print(f"  CHECKSUM MISMATCH: expected {md5}, got {actual}", file=sys.stderr)
                    return 1
                print(f"  checksum OK ({actual})")

        # Multi-file / other sources: require explicit download_urls list
        for entry in ds.get("download_urls", []) or []:
            url = entry["url"]
            name = entry.get("filename", os.path.basename(url))
            dest = ds_dir / name
            expected = entry.get("md5")
            if args.dry_run:
                print(f"  DRY-RUN: would download {url} -> {dest}")
                continue
            download(url, dest)
            if expected:
                actual = md5_file(dest)
                if actual != expected:
                    print(f"  CHECKSUM MISMATCH: expected {expected}, got {actual}", file=sys.stderr)
                    return 1
                print(f"  checksum OK ({actual})")

    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

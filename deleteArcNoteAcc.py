#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


PATTERNS = (
    re.compile(rb"(,(?:false|true)),\s*-?\d+(?:\.\d+)?(?=\))"),
)


def iter_aff_files(target: Path):
    if target.is_file():
        if target.suffix.lower() != ".aff":
            raise ValueError(f"not an .aff file: {target}")
        yield target
        return

    if not target.is_dir():
        raise ValueError(f"path does not exist: {target}")

    yield from sorted(target.rglob("*.aff"))


def process_file(path: Path, dry_run: bool = False) -> int:
    data = path.read_bytes()
    updated = data
    total = 0

    for pattern in PATTERNS:
        updated, count = pattern.subn(rb"\1", updated)
        total += count

    if total and not dry_run:
        path.write_bytes(updated)

    return total


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Remove only the accuracy suffix numbers from AFF arc parameters: "
            "false,3.00 -> false, true,6.00 -> true, false,-1.5 -> false."
        )
    )
    parser.add_argument("path", help="Directory containing .aff files, or one .aff file")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing files")
    args = parser.parse_args()

    target = Path(args.path)
    files = list(iter_aff_files(target))
    if not files:
        print("No .aff files found.")
        return 0

    changed_files = 0
    total_removed = 0
    for aff_file in files:
        removed = process_file(aff_file, args.dry_run)
        if removed:
            changed_files += 1
            total_removed += removed
        print(f"{aff_file}: removed {removed}")

    mode = "dry-run" if args.dry_run else "written"
    print(f"Done ({mode}). Files scanned: {len(files)}, files changed: {changed_files}, suffixes removed: {total_removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

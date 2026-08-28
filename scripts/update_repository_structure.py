#!/usr/bin/env python3
"""Regenerate the deterministic repository structure snapshot."""

from __future__ import annotations

from pathlib import Path
import sys

from validate import STRUCTURE_SNAPSHOT_PATH, render_repository_structure


def main() -> int:
    repository_root = Path(__file__).resolve().parents[1]
    snapshot_path = repository_root / STRUCTURE_SNAPSHOT_PATH
    try:
        snapshot = render_repository_structure(repository_root)
        with snapshot_path.open("w", encoding="utf-8", newline="\n") as snapshot_file:
            snapshot_file.write(snapshot)
    except (OSError, RuntimeError, UnicodeError) as error:
        print(f"Repository structure update failed: {error}", file=sys.stderr)
        return 1
    print(f"Updated {STRUCTURE_SNAPSHOT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

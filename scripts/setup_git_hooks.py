#!/usr/bin/env python3
"""Opt in to this repository's version-controlled Git hooks."""

from __future__ import annotations

import argparse
import stat
import subprocess
import sys
from pathlib import Path


def configure_hooks(repository_root: Path, *, force: bool = False) -> None:
    repository_root = repository_root.resolve()
    hook_path = repository_root / ".githooks" / "pre-commit"
    if not hook_path.is_file():
        raise RuntimeError(f"hook does not exist: {hook_path}")

    result = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or Path(result.stdout.strip()).resolve() != repository_root:
        raise RuntimeError(f"not the root of a Git repository: {repository_root}")

    existing = subprocess.run(
        ["git", "-C", str(repository_root), "config", "--local", "--get", "core.hooksPath"],
        check=False,
        capture_output=True,
        text=True,
    )
    if existing.returncode not in {0, 1}:
        raise RuntimeError(existing.stderr.strip() or "could not read core.hooksPath")
    existing_path = existing.stdout.strip() if existing.returncode == 0 else ""
    if existing_path and existing_path != ".githooks" and not force:
        raise RuntimeError(
            f"core.hooksPath is already {existing_path!r}; rerun with --force to replace it"
        )

    subprocess.run(
        ["git", "-C", str(repository_root), "config", "--local", "core.hooksPath", ".githooks"],
        check=True,
    )
    executable_mode = hook_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    hook_path.chmod(executable_mode)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace a different existing core.hooksPath value",
    )
    arguments = parser.parse_args()
    repository_root = Path(__file__).resolve().parents[1]
    try:
        configure_hooks(repository_root, force=arguments.force)
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"Git hook setup failed: {error}", file=sys.stderr)
        return 1
    print("Git hooks configured: core.hooksPath=.githooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

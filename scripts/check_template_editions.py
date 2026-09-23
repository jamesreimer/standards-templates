#!/usr/bin/env python3
"""Validate template edition transitions against verified Git comparison context.

This standards-domain check shares the snapshot validator's effective candidate
inventory. It does not classify the meaning of content changes.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from validate_local import (
    STABLE_TEMPLATE_ID_DECLARATION_RE,
    TEMPLATE_ID_RE,
    markdown_without_fenced_code,
    read_domain_input,
    template_edition,
)

BASELINE = "76382fb84cb9d43340c508145b83c2c1dbdff8c4"
CORRECTION_RE = re.compile(
    r"^Edition correction: `([a-z0-9]+(?:-[a-z0-9]+)*)` at `([0-9a-f]{40})`[ \t]*$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class Template:
    content: bytes
    edition: tuple[int, int] | None


@dataclass(frozen=True)
class Comparison:
    base: str
    # Pushes can contain several independently merged authoritative states.
    commits: tuple[str, ...] = ()
    declarations: str = ""


def git(root: Path, *args: str) -> str:
    return git_bytes(root, *args).decode("utf-8").strip()


def git_bytes(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.PIPE)


def revision(root: Path, value: str) -> str:
    return git(root, "rev-parse", "--verify", "--end-of-options", f"{value}^{{commit}}")


def parents(root: Path, commit: str) -> list[str]:
    return git(root, "show", "-s", "--format=%P", commit).split()


def merge_base(root: Path, left: str, right: str) -> str:
    bases = git(root, "merge-base", "--all", left, right).splitlines()
    if len(bases) != 1:
        raise ValueError("comparison has no unique merge-base")
    return bases[0]


def event_sha(root: Path, value) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError("event revision must be a full commit SHA")
    return revision(root, value)


def comparison_context(root: Path, env: dict[str, str], explicit_base: str | None) -> Comparison:
    if git(root, "rev-parse", "--is-shallow-repository") != "false":
        raise ValueError("full history is required for edition and lineage validation")
    head = revision(root, "HEAD")
    if env.get("GITHUB_ACTIONS") == "true":
        if explicit_base:
            raise ValueError("an explicit local base cannot override CI context")
        event_path = env.get("GITHUB_EVENT_PATH")
        if not event_path:
            raise ValueError("CI event context is missing")
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
        if not isinstance(event, dict):
            raise ValueError("CI event must be an object")
        if event_sha(root, env.get("GITHUB_SHA")) != head:
            raise ValueError("checked-out HEAD disagrees with GITHUB_SHA")
        name = env.get("GITHUB_EVENT_NAME")
        if name == "pull_request":
            pr = event["pull_request"]
            base = event_sha(root, pr["base"]["sha"])
            pr_head = event_sha(root, pr["head"]["sha"])
            if head == pr_head:
                if (
                    merge_base(root, base, head) != base
                    or merge_base(root, "origin/main", head) != base
                ):
                    raise ValueError(
                        "PR head is not constructed on the supplied base; update branch"
                    )
            else:
                if parents(root, head) != [base, pr_head]:
                    raise ValueError("PR merge parents disagree with supplied base/head metadata")
            declarations = git(root, "log", "--format=%B", f"{base}..{pr_head}")
            return Comparison(base, declarations=declarations)
        if name == "push":
            if event_sha(root, event["after"]) != head:
                raise ValueError("push after revision disagrees with checked-out HEAD")
            base = event_sha(root, event["before"])
            chain = git(root, "rev-list", "--first-parent", head).splitlines()
            if base not in chain or base == head:
                raise ValueError("push before is not an earlier first-parent ancestor")
            commits = tuple(reversed(chain[: chain.index(base)]))
            previous = base
            for commit in commits:
                if parents(root, commit) != [previous]:
                    raise ValueError("push contains a non-squash authoritative state")
                previous = commit
            return Comparison(base, commits)
        raise ValueError(f"unsupported CI event: {name!r}")
    base = revision(root, explicit_base) if explicit_base else merge_base(root, "origin/main", head)
    if merge_base(root, base, head) != base:
        raise ValueError("local comparison base is not an ancestor of HEAD")
    declarations = git(root, "log", "--format=%B", f"{base}..{head}")
    declarations += "\n" + env.get("TEMPLATE_EDITION_CORRECTIONS", "")
    return Comparison(base, declarations=declarations)


def templates_from_files(files: dict[str, bytes], *, allow_missing: bool) -> dict[str, Template]:
    ids = set()
    for path in files:
        parts = path.split("/")
        if (
            len(parts) != 3
            or parts[0] != "templates"
            or parts[2] not in {"README.md", "standard.md"}
        ):
            raise ValueError(f"unsupported template inventory path: {path}")
        if not TEMPLATE_ID_RE.fullmatch(parts[1]):
            raise ValueError(f"invalid template ID: {parts[1]}")
        ids.add(parts[1])
    result = {}
    for template_id in sorted(ids):
        directory = f"templates/{template_id}"
        try:
            readme = files[f"{directory}/README.md"].decode("utf-8")
            content = files[f"{directory}/standard.md"]
        except KeyError as error:
            raise ValueError(f"{directory}: both README.md and standard.md are required") from error
        ids_in_readme = STABLE_TEMPLATE_ID_DECLARATION_RE.findall(
            markdown_without_fenced_code(readme)
        )
        if ids_in_readme != [template_id]:
            raise ValueError(f"{directory}: stable template ID must match the directory")
        try:
            edition = template_edition(readme, allow_missing=allow_missing)
        except ValueError as error:
            raise ValueError(f"{directory}/README.md: {error}") from error
        result[template_id] = Template(content, edition)
    return result


def snapshot(root: Path, commit: str) -> dict[str, Template]:
    files = {}
    entries = git_bytes(root, "ls-tree", "-rz", commit, "--", "templates/")
    for entry in filter(None, entries.split(b"\0")):
        metadata, path = entry.split(b"\t", 1)
        mode, kind, blob = metadata.split()
        if mode not in {b"100644", b"100755"} or kind != b"blob":
            raise ValueError("template snapshot contains a non-regular file")
        files[path.decode("utf-8")] = git_bytes(root, "cat-file", "blob", blob.decode("ascii"))
    return templates_from_files(files, allow_missing=True)


def candidate(root: Path) -> dict[str, Template]:
    domain = read_domain_input(root)
    return templates_from_files(
        {
            path: (root / path).read_bytes()
            for path in domain.files
            if path.startswith("templates/")
        },
        allow_missing=False,
    )


def correction_declarations(text: str) -> dict[str, str]:
    result = {}
    for line in text.splitlines():
        if not line.startswith("Edition correction:"):
            continue
        match = CORRECTION_RE.fullmatch(line)
        if match is None:
            raise ValueError("malformed Edition correction declaration")
        template_id, commit = match.groups()
        if template_id in result and result[template_id] != commit:
            raise ValueError(f"conflicting correction declarations for {template_id}")
        result[template_id] = commit
    return result


def verify_correction(root: Path, base: str, template_id: str, old: Template, source: str) -> None:
    chain = git(root, "rev-list", "--first-parent", base).splitlines()
    if source not in chain:
        raise ValueError(f"{template_id}: correction source is not an authoritative ancestor")
    source_id = template_id
    # Follow verified exact moves backwards to the named historical transition.
    # A current path need not have existed when its content was misclassified.
    current = snapshot(root, base)
    for commit in chain[1 : chain.index(source) + 1]:
        previous = snapshot(root, commit)
        if source_id not in previous:
            matches = [
                item
                for item in set(previous) - set(current)
                if previous[item] == current[source_id]
            ]
            if len(matches) != 1:
                raise ValueError(f"{template_id}: correction lineage cannot be verified")
            source_id = matches[0]
        current = previous
    source_parents = parents(root, source)
    if len(source_parents) != 1:
        raise ValueError(f"{template_id}: correction source must identify one earlier transition")
    before = snapshot(root, source_parents[0]).get(source_id)
    after = snapshot(root, source).get(source_id)
    if (
        before is None
        or after is None
        or before.edition is None
        or after.edition is None
        or before.content == after.content
        or after.edition != (before.edition[0], before.edition[1] + 1)
        or old.edition is None
        or old.edition[0] != after.edition[0]
        or old.edition[1] < after.edition[1]
    ):
        raise ValueError(
            f"{template_id}: correction source is not an editorial transition in this edition"
        )


def check_transitions(
    root: Path,
    base: str,
    before: dict[str, Template],
    after: dict[str, Template],
    declarations: str = "",
) -> list[str]:
    findings = []
    corrections = correction_declarations(declarations)
    removed = set(before) - set(after)
    added = set(after) - set(before)
    pairs = {template_id: template_id for template_id in set(before) & set(after)}
    for new in sorted(added):
        matches = [old for old in removed if before[old].content == after[new].content]
        if len(matches) > 1 or (
            matches and sum(after[item].content == after[new].content for item in added) > 1
        ):
            findings.append(f"{new}: ambiguous exact-content lineage pairing; review required")
        elif matches:
            pairs[new] = matches[0]
    paired_old = set(pairs.values())
    unmatched_removed = removed - paired_old
    baseline = None
    for new, current in sorted(after.items()):
        if current.edition is None:
            findings.append(f"{new}: candidate edition is missing")
            continue
        if new in added:
            history = git(
                root, "log", "--first-parent", "--format=%H", base, "--", f"templates/{new}/"
            )
            if history:
                findings.append(
                    f"{new}: historical template ID cannot start a new lineage; review required"
                )
                continue
        if new not in pairs:
            if unmatched_removed:
                findings.append(
                    f"{new}: unmatched addition with removals; changed move requires lineage review"
                )
            if current.edition != (1, 0):
                findings.append(f"{new}: new template must start at 1.0")
            continue
        old_id = pairs[new]
        previous = before[old_id]
        if previous.edition is None:
            if baseline is None:
                revision(root, BASELINE)
                if merge_base(root, BASELINE, base) != BASELINE:
                    raise ValueError(
                        "bootstrap base does not descend from the approved v1.0.0 baseline"
                    )
                baseline = snapshot(root, BASELINE)
            original = baseline.get(old_id)
            intervening = git(
                root,
                "log",
                "--format=%H",
                f"{BASELINE}..{base}",
                "--",
                f"templates/{old_id}/standard.md",
            )
            if (
                original is None
                or original.content != previous.content
                or previous.content != current.content
                or current.edition != (1, 0)
                or intervening
            ):
                findings.append(
                    f"{new}: bootstrap requires unchanged v1.0.0 baseline content at 1.0"
                )
            continue
        if old_id != new:
            if previous.edition != current.edition:
                findings.append(f"{new}: exact move must carry {old_id}'s edition unchanged")
            continue
        n, m = previous.edition
        if previous.content != current.content:
            if current.edition not in {(n, m + 1), (n + 1, 0)}:
                findings.append(
                    f"{new}: changed standard.md requires the exact next edition transition"
                )
        elif current.edition != previous.edition:
            if m < 1 or current.edition != (n + 1, 0) or new not in corrections:
                findings.append(
                    f"{new}: unchanged content permits only a declared upward correction from N.M (M >= 1) to (N+1).0"
                )
            else:
                verify_correction(root, base, new, previous, corrections[new])
    return findings


def validate(root: Path, env: dict[str, str], explicit_base: str | None = None) -> list[str]:
    context = comparison_context(root, env, explicit_base)
    working = candidate(root)
    before = snapshot(root, context.base)
    if not context.commits:
        return check_transitions(root, context.base, before, working, context.declarations)
    base = context.base
    findings = []
    for commit in context.commits:
        after = snapshot(root, commit)
        findings.extend(
            check_transitions(
                root, base, before, after, git(root, "show", "-s", "--format=%B", commit)
            )
        )
        base, before = commit, after
    if before != working:
        raise ValueError("push working template state differs from checked commit")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base", help="explicit local comparison revision; never overrides CI")
    args = parser.parse_args()
    try:
        findings = validate(args.root.resolve(), dict(os.environ), args.base)
    except (
        OSError,
        UnicodeError,
        ValueError,
        KeyError,
        TypeError,
        subprocess.SubprocessError,
    ) as error:
        print(f"Template edition validation could not complete: {error}", file=sys.stderr)
        return 1
    for finding in findings:
        print(finding, file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

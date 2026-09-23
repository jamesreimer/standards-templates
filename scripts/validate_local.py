#!/usr/bin/env python3
"""Standards-domain checks for this repository.

Generic mechanical checks are composed separately through pre-commit.
This independently executable module holds only what is specific to a library
of standards templates: template directory structure, stable template identity,
local requirement schemes and their
references, catalog membership, human-facing title agreement, and BCP 14
keyword spelling.

Nothing here should be a general repository-mechanics check. If a check would
apply to any repository, it belongs upstream in the template instead.
"""

from __future__ import annotations

import argparse
import re
import stat
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

TEMPLATES_DIRECTORY = "templates"
CATALOG_PATH = "CATALOG.md"
EXPECTED_TEMPLATE_FILES = {"README.md", "standard.md"}

TEMPLATE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STABLE_TEMPLATE_ID_DECLARATION_RE = re.compile(
    r"^Stable template ID: `([^`\n]+)`[ \t]*$", re.MULTILINE
)
TEMPLATE_EDITION_RE = re.compile(r"Template edition: `([1-9][0-9]*)\.(0|[1-9][0-9]*)`[ \t]*")


def template_edition(content: str, *, allow_missing: bool = False):
    """Parse the canonical metadata paragraph without weakening stable-ID checks."""
    visible = markdown_without_fenced_code(content)
    declarations = [line for line in visible.splitlines() if "Template edition:" in line]
    if not declarations and allow_missing:
        return None
    if len(declarations) != 1:
        raise ValueError("template README must contain exactly one template edition declaration")
    match = TEMPLATE_EDITION_RE.fullmatch(declarations[0])
    if match is None:
        raise ValueError("template edition must use N.M with N >= 1, M >= 0, no leading zeros")
    # Use original paragraphs: masking fences must not hide intervening content.
    paragraphs = re.split(r"\n(?:[ \t]*\n)+", content.strip())
    stable = list(STABLE_TEMPLATE_ID_DECLARATION_RE.finditer(visible))
    if len(stable) != 1:
        raise ValueError("template edition requires exactly one stable template ID")
    stable_line = stable[0].group()
    try:
        position = paragraphs.index(stable_line)
    except ValueError as error:
        raise ValueError(
            "stable ID and template edition must be separate metadata paragraphs"
        ) from error
    if position + 1 >= len(paragraphs) or paragraphs[position + 1] != declarations[0]:
        raise ValueError(
            "template edition must be the next separate paragraph after stable template ID"
        )
    return int(match[1]), int(match[2])


LOCAL_REQUIREMENT_SCHEME_DECLARATION_RE = re.compile(
    r"^`([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-NNN)` identifies a local requirement "
    r"synthesized by this template\b",
    re.MULTILINE,
)
LOCAL_REQUIREMENT_DEFINITION_RE = re.compile(
    r"^\*\*([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+) — [^*\n]+\.\*\*", re.MULTILINE
)
LOCAL_REQUIREMENT_REFERENCE_RE = re.compile(r"^([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)-([0-9]{3})$")
CATALOG_ENTRY_HEADING_RE = re.compile(r"^`([^`]+)`$")
CATALOG_TITLE_RE = re.compile(r"^\*\*([^\n]+)\*\*[ \t]*$", re.MULTILINE)
README_TITLE_RE = re.compile(
    r"^Human-facing title:[ \t]*\n(?:[ \t]*\n)*>[ \t]*\*\*([^\n]+?)\*\*[ \t]*$",
    re.MULTILINE,
)
HEADING_RE = re.compile(r"^(#{1,6})(?:[ \t]+|$)(.*)$")
FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})(.*)$")
TOKEN_RE = re.compile(r"(?<![A-Z0-9_])[A-Z0-9]+(?![A-Z0-9_])")

BCP14_SINGLE_FORMS = ("MUST", "SHOULD", "MAY", "SHALL", "REQUIRED", "RECOMMENDED", "OPTIONAL")
BCP14_PHRASE_FORMS = ("MUST NOT", "SHOULD NOT", "SHALL NOT", "NOT RECOMMENDED")


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    line: int


@dataclass(frozen=True)
class MarkdownLine:
    number: int
    text: str
    prose: str


def strip_inline_code(line: str) -> str:
    """Replace backtick-delimited inline code spans with spaces."""
    characters = list(line)
    index = 0
    while index < len(line):
        if line[index] != "`":
            index += 1
            continue
        run_end = index
        while run_end < len(line) and line[run_end] == "`":
            run_end += 1
        delimiter = line[index:run_end]
        closing = line.find(delimiter, run_end)
        if closing == -1:
            index = run_end
            continue
        for position in range(index, closing + len(delimiter)):
            characters[position] = " "
        index = closing + len(delimiter)
    return "".join(characters)


def scan_inline_code_spans(line: str) -> list:
    """Return exact contents of closed backtick-delimited inline code spans."""
    spans = []
    index = 0
    while index < len(line):
        if line[index] != "`":
            index += 1
            continue
        run_end = index
        while run_end < len(line) and line[run_end] == "`":
            run_end += 1
        delimiter = line[index:run_end]
        closing = line.find(delimiter, run_end)
        if closing == -1:
            index = run_end
            continue
        spans.append(line[run_end:closing])
        index = closing + len(delimiter)
    return spans


def is_closing_fence(line: str, character: str, minimum_length: int) -> bool:
    escaped = re.escape(character)
    return bool(re.match(rf"^[ \t]{{0,3}}{escaped}{{{minimum_length},}}[ \t]*$", line))


def scan_markdown_lines(content: str) -> list:
    """Return non-fenced lines with inline code masked.

    This is the lexical layer the standards-domain checks share. It does not
    attempt to implement all of CommonMark.
    """
    lines = []
    fence_character = None
    fence_length = 0
    for line_number, line in enumerate(content.splitlines(), 1):
        if fence_character is not None:
            if is_closing_fence(line, fence_character, fence_length):
                fence_character = None
                fence_length = 0
            continue
        fence_match = FENCE_RE.match(line)
        if fence_match:
            fence = fence_match.group(1)
            fence_character = fence[0]
            fence_length = len(fence)
            continue
        lines.append(MarkdownLine(line_number, line, strip_inline_code(line)))
    return lines


def markdown_without_fenced_code(content: str) -> str:
    """Mask fenced lines using the domain scanner, preserving source line numbers."""
    lines = ["\n" if line.endswith("\n") else "" for line in content.splitlines(keepends=True)]
    for line in scan_markdown_lines(content):
        ending = "\n" if lines[line.number - 1].endswith("\n") else ""
        lines[line.number - 1] = line.text + ending
    return "".join(lines)


def scan_headings(content: str) -> list:
    """Return headings outside fenced code, with trailing hashes removed."""
    headings = []
    for markdown_line in scan_markdown_lines(content):
        heading_match = HEADING_RE.match(markdown_line.text)
        if heading_match:
            text = re.sub(r"[ \t]+#+[ \t]*$", "", heading_match.group(2)).strip()
            headings.append(Heading(len(heading_match.group(1)), text, markdown_line.number))
    return headings


def damerau_levenshtein(left: str, right: str) -> int:
    """Return optimal-string-alignment distance for short keyword candidates."""
    rows = len(left) + 1
    columns = len(right) + 1
    distances = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        distances[row][0] = row
    for column in range(columns):
        distances[0][column] = column

    for row in range(1, rows):
        for column in range(1, columns):
            substitution_cost = 0 if left[row - 1] == right[column - 1] else 1
            distances[row][column] = min(
                distances[row - 1][column] + 1,
                distances[row][column - 1] + 1,
                distances[row - 1][column - 1] + substitution_cost,
            )
            if (
                row > 1
                and column > 1
                and left[row - 1] == right[column - 2]
                and left[row - 2] == right[column - 1]
            ):
                distances[row][column] = min(
                    distances[row][column], distances[row - 2][column - 2] + 1
                )
    return distances[-1][-1]


def is_single_near_miss(candidate: str, canonical: str) -> bool:
    if candidate == canonical or not candidate:
        return False
    if len(canonical) <= 4:
        return candidate in {canonical[:-1], canonical + canonical[-1]}
    if (
        candidate[:3] != canonical[:3]
        or candidate[-1] != canonical[-1]
        or abs(len(candidate) - len(canonical)) > 1
    ):
        return False
    return damerau_levenshtein(candidate, canonical) == 1


def is_phrase_word_near_miss(candidate: str, canonical: str) -> bool:
    if is_single_near_miss(candidate, canonical):
        return True
    return (
        canonical == "NOT"
        and len(candidate) == len(canonical)
        and candidate.startswith("N")
        and any(character.isdigit() for character in candidate)
        and damerau_levenshtein(candidate, canonical) == 1
    )


def is_phrase_near_miss(candidate: str, canonical: str) -> bool:
    candidate_words = candidate.split()
    canonical_words = canonical.split()
    if candidate == canonical or len(candidate_words) != len(canonical_words):
        return False
    return sum(
        damerau_levenshtein(candidate_word, canonical_word)
        for candidate_word, canonical_word in zip(candidate_words, canonical_words)
    ) == 1 and all(
        is_phrase_word_near_miss(candidate_word, canonical_word) or candidate_word == canonical_word
        for candidate_word, canonical_word in zip(candidate_words, canonical_words)
    )


class StandardsChecks:
    """Run the standards-domain checks over one repository."""

    def __init__(self, context) -> None:
        self.context = context
        self.findings = []
        self.template_ids = []
        self.catalog_titles = {}
        self.requirement_prefixes = set()
        self.requirement_definitions = {}

    def _add(self, path: str, line: int, reason: str) -> None:
        self.findings.append((path, line, reason))

    def _text(self, relative_path: str):
        return self.context.text.get(relative_path)

    def run(self) -> list:
        self._check_template_structure()
        self._check_stable_template_ids()
        self._check_template_editions()
        self._check_requirement_ids()
        self._check_requirement_references()
        self._check_catalog_membership()
        self._check_template_titles()
        self._check_bcp14_near_misses()
        return self.findings

    def _check_template_structure(self) -> None:
        entries = {}
        for relative_path in self.context.files:
            if not relative_path.startswith(f"{TEMPLATES_DIRECTORY}/"):
                continue
            parts = relative_path.split("/")
            if len(parts) == 2:
                self._add(
                    relative_path, 0, "templates directory may contain template directories only"
                )
                continue
            entries.setdefault(parts[1], set()).add(parts[2] if len(parts) > 2 else "")

        if not entries:
            self._add(TEMPLATES_DIRECTORY, 0, "templates directory is missing")
            return

        for template_id in sorted(entries):
            directory = f"{TEMPLATES_DIRECTORY}/{template_id}"
            self.template_ids.append(template_id)
            if not TEMPLATE_ID_RE.fullmatch(template_id):
                self._add(
                    directory,
                    0,
                    "template ID must use lowercase ASCII alphanumerics "
                    "separated by single hyphens",
                )
            present = entries[template_id]
            for missing_name in sorted(EXPECTED_TEMPLATE_FILES - present):
                self._add(f"{directory}/{missing_name}", 0, "required template file is missing")
            for unexpected_name in sorted(present - EXPECTED_TEMPLATE_FILES):
                self._add(
                    f"{directory}/{unexpected_name}", 0, "unexpected entry in template directory"
                )

    def _check_stable_template_ids(self) -> None:
        for template_id in self.template_ids:
            readme_path = f"{TEMPLATES_DIRECTORY}/{template_id}/README.md"
            readme_text = self._text(readme_path)
            if readme_text is None:
                continue
            structural_text = markdown_without_fenced_code(readme_text)
            declarations = STABLE_TEMPLATE_ID_DECLARATION_RE.findall(structural_text)
            if len(declarations) != 1:
                self._add(
                    readme_path,
                    0,
                    "template README must contain exactly one stable template ID "
                    f"declaration using the repository convention; found {len(declarations)}",
                )
                continue
            if declarations[0] != template_id:
                self._add(
                    readme_path,
                    0,
                    f"declares stable template ID {declarations[0]!r}; "
                    f"expected directory ID {template_id!r}",
                )

    def _check_template_editions(self) -> None:
        for template_id in self.template_ids:
            path = f"{TEMPLATES_DIRECTORY}/{template_id}/README.md"
            content = self._text(path)
            if content is not None:
                try:
                    template_edition(content)
                except ValueError as error:
                    self._add(path, 0, str(error))

    def _check_requirement_ids(self) -> None:
        for template_id in self.template_ids:
            standard_path = f"{TEMPLATES_DIRECTORY}/{template_id}/standard.md"
            standard_text = self._text(standard_path)
            if standard_text is None:
                continue
            structural_text = markdown_without_fenced_code(standard_text)
            schemes = LOCAL_REQUIREMENT_SCHEME_DECLARATION_RE.findall(structural_text)
            self.requirement_prefixes.update(
                scheme[: -len("-NNN")] for scheme in schemes if scheme.endswith("-NNN")
            )
            if len(schemes) > 1:
                self._add(
                    standard_path,
                    0,
                    f"declares {len(schemes)} local requirement ID schemes {schemes!r}; "
                    "expected at most one declaration using 'PREFIX-NNN'",
                )
                continue
            if not schemes:
                continue

            scheme = schemes[0]
            prefix = scheme[: -len("-NNN")]
            expected_id_re = re.compile(rf"^{re.escape(prefix)}-[0-9]{{3}}$")
            definition_ids = []
            for match in LOCAL_REQUIREMENT_DEFINITION_RE.finditer(structural_text):
                requirement_id = match.group(1)
                line_number = structural_text.count("\n", 0, match.start()) + 1
                if not expected_id_re.fullmatch(requirement_id):
                    self._add(
                        standard_path,
                        line_number,
                        f"requirement definition label {requirement_id!r} does not match "
                        f"declared scheme {scheme!r}; expected prefix {prefix!r} "
                        "with exactly three decimal digits",
                    )
                    continue
                definition_ids.append((requirement_id, line_number))
                self.requirement_definitions.setdefault(requirement_id, []).append(
                    (standard_path, line_number)
                )

            id_counts = Counter(requirement_id for requirement_id, _ in definition_ids)
            for requirement_id, count in sorted(id_counts.items()):
                if count > 1:
                    duplicate_line = [
                        line_number
                        for candidate_id, line_number in definition_ids
                        if candidate_id == requirement_id
                    ][1]
                    self._add(
                        standard_path,
                        duplicate_line,
                        f"duplicate local requirement ID {requirement_id!r}; "
                        f"declared scheme is {scheme!r}",
                    )

    def _check_requirement_references(self) -> None:
        for template_id in self.template_ids:
            standard_path = f"{TEMPLATES_DIRECTORY}/{template_id}/standard.md"
            standard_text = self._text(standard_path)
            if standard_text is None:
                continue
            for markdown_line in scan_markdown_lines(standard_text):
                for code_span in scan_inline_code_spans(markdown_line.text):
                    reference_match = LOCAL_REQUIREMENT_REFERENCE_RE.fullmatch(code_span)
                    if reference_match is None:
                        continue
                    if reference_match.group(1) not in self.requirement_prefixes:
                        continue
                    definitions = self.requirement_definitions.get(code_span, [])
                    if len(definitions) == 1:
                        continue
                    if not definitions:
                        reason = (
                            f"unresolved local requirement reference {code_span!r}; no valid "
                            f"definition exists for declared prefix "
                            f"{reference_match.group(1)!r}"
                        )
                    else:
                        reason = (
                            f"local requirement reference {code_span!r} resolves to "
                            f"{len(definitions)} definitions; expected exactly one"
                        )
                    self._add(standard_path, markdown_line.number, reason)

    def _check_catalog_membership(self) -> None:
        catalog_text = self._text(CATALOG_PATH)
        if catalog_text is None:
            self._add(CATALOG_PATH, 0, "catalog is missing or unreadable")
            return

        structural_text = markdown_without_fenced_code(catalog_text)
        headings = scan_headings(catalog_text)
        templates_headings = [
            heading for heading in headings if heading.level == 2 and heading.text == "Templates"
        ]
        if not templates_headings:
            self._add(CATALOG_PATH, 0, "catalog is missing the Templates section")
            return
        if len(templates_headings) != 1:
            self._add(
                CATALOG_PATH,
                0,
                "catalog must contain exactly one Templates section; "
                f"found {len(templates_headings)}",
            )
            return

        templates_index = headings.index(templates_headings[0])
        section_headings = []
        next_h2 = None
        for heading in headings[templates_index + 1 :]:
            if heading.level == 2:
                next_h2 = heading
                break
            section_headings.append(heading)

        entry_headings = []
        current_h3 = None
        current_h4 = None
        for heading in section_headings:
            if heading.level == 3:
                current_h3 = (
                    heading if CATALOG_ENTRY_HEADING_RE.fullmatch(heading.text) is None else None
                )
                current_h4 = None
                continue
            entry_match = CATALOG_ENTRY_HEADING_RE.fullmatch(heading.text)
            if heading.level == 4:
                current_h4 = heading
                if current_h3 is not None and entry_match is not None:
                    entry_headings.append((heading, entry_match.group(1)))
                continue
            if (
                heading.level == 5
                and current_h3 is not None
                and current_h4 is not None
                and CATALOG_ENTRY_HEADING_RE.fullmatch(current_h4.text) is None
                and entry_match is not None
            ):
                entry_headings.append((heading, entry_match.group(1)))

        entry_ids = [template_id for _, template_id in entry_headings]
        for template_id, count in sorted(Counter(entry_ids).items()):
            if count != 1:
                self._add(
                    CATALOG_PATH,
                    0,
                    f"template {template_id!r} appears {count} times in the catalog",
                )

        directory_ids = set(self.template_ids)
        catalog_ids = set(entry_ids)
        for template_id in sorted(directory_ids - catalog_ids):
            self._add(
                CATALOG_PATH, 0, f"template directory {template_id!r} is missing from the catalog"
            )
        for template_id in sorted(catalog_ids - directory_ids):
            self._add(CATALOG_PATH, 0, f"catalog entry {template_id!r} has no template directory")

        structural_lines = structural_text.splitlines(keepends=True)
        section_end_line = next_h2.line - 1 if next_h2 is not None else len(structural_lines)
        for index, (entry_heading, template_id) in enumerate(entry_headings):
            entry_end_line = (
                entry_headings[index + 1][0].line - 1
                if index + 1 < len(entry_headings)
                else section_end_line
            )
            entry_body = "".join(structural_lines[entry_heading.line : entry_end_line])
            title_match = CATALOG_TITLE_RE.search(entry_body)
            if not title_match:
                self._add(
                    CATALOG_PATH,
                    0,
                    f"catalog entry {template_id!r} is missing its human-facing title",
                )
                continue
            self.catalog_titles[template_id] = title_match.group(1).strip()

    def _check_template_titles(self) -> None:
        for template_id in self.template_ids:
            directory = f"{TEMPLATES_DIRECTORY}/{template_id}"
            readme_text = self._text(f"{directory}/README.md")
            standard_text = self._text(f"{directory}/standard.md")

            readme_title = None
            if readme_text is not None:
                title_match = README_TITLE_RE.search(markdown_without_fenced_code(readme_text))
                if title_match:
                    readme_title = title_match.group(1).strip()
                else:
                    self._add(
                        f"{directory}/README.md",
                        0,
                        "cannot find the human-facing title using the repository convention",
                    )

            standard_title = None
            if standard_text is not None:
                h1_headings = [
                    heading for heading in scan_headings(standard_text) if heading.level == 1
                ]
                if len(h1_headings) == 1:
                    standard_title = h1_headings[0].text

            available_titles = {
                "template README": readme_title,
                "standard H1": standard_title,
                "catalog": self.catalog_titles.get(template_id),
            }
            distinct_titles = {title for title in available_titles.values() if title is not None}
            if len(distinct_titles) > 1:
                details = ", ".join(
                    f"{source}={title!r}"
                    for source, title in available_titles.items()
                    if title is not None
                )
                self._add(directory, 0, f"human-facing template titles do not agree ({details})")

    def _check_bcp14_near_misses(self) -> None:
        for relative_path, content in sorted(self.context.text.items()):
            if not relative_path.endswith(".md"):
                continue
            for markdown_line in scan_markdown_lines(content):
                self._check_bcp14_line(relative_path, markdown_line)

    def _check_bcp14_line(self, relative_path: str, markdown_line) -> None:
        prose = markdown_line.prose
        prose = re.sub(r"!?\[([^\]]*)\]\([^)]+\)", r"\1", prose)
        prose = re.sub(r"<https?://[^>]+>", " ", prose, flags=re.IGNORECASE)
        prose = re.sub(r"https?://\S+", " ", prose, flags=re.IGNORECASE)
        tokens = list(TOKEN_RE.finditer(prose))
        consumed_indices = set()

        for index in range(len(tokens) - 1):
            between = prose[tokens[index].end() : tokens[index + 1].start()]
            if not re.fullmatch(r"\s+", between):
                continue
            candidate = f"{tokens[index].group()} {tokens[index + 1].group()}"
            if candidate in BCP14_PHRASE_FORMS:
                continue
            if any(is_phrase_near_miss(candidate, canonical) for canonical in BCP14_PHRASE_FORMS):
                self._add(
                    relative_path,
                    markdown_line.number,
                    f"malformed BCP 14 keyword near-miss {candidate!r}; spelling only was checked",
                )
                consumed_indices.update({index, index + 1})

        for index, token_match in enumerate(tokens):
            if index in consumed_indices:
                continue
            candidate = token_match.group()
            if candidate in BCP14_SINGLE_FORMS:
                continue
            if any(is_single_near_miss(candidate, canonical) for canonical in BCP14_SINGLE_FORMS):
                self._add(
                    relative_path,
                    markdown_line.number,
                    f"malformed BCP 14 keyword near-miss {candidate!r}; spelling only was checked",
                )


@dataclass(frozen=True)
class DomainInput:
    files: tuple[str, ...]
    text: dict[str, str]


def read_domain_input(root: Path):
    """Read the effective candidate inventory after inspecting all path metadata."""
    root = root.resolve()
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    files = tuple(sorted(set(filter(None, result.stdout.decode("utf-8").split("\0")))))
    # Direct invocation must also fail closed. Finish metadata inspection before
    # opening domain content, including any ancestor replaced by a symlink.
    inspected = set()
    for relative in files:
        path = root / relative
        for component in [*reversed(path.parents), path]:
            if component == root or root not in component.parents or component in inspected:
                continue
            inspected.add(component)
            mode = component.lstat().st_mode
            if stat.S_ISLNK(mode):
                raise OSError(f"{component.relative_to(root)}: symbolic link is not allowed")
            if not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
                raise OSError(f"{component.relative_to(root)}: unsupported input type")
    text = {
        relative: (root / relative).read_text(encoding="utf-8")
        for relative in files
        if relative.endswith(".md")
    }
    return DomainInput(files, text)


def validate_repository(root: Path):
    """Validate domain semantics; input/runtime failures propagate to the CLI."""
    return StandardsChecks(read_domain_input(root)).run()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        findings = validate_repository(args.root)
    except (OSError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"Standards validation could not complete: {error}", file=sys.stderr)
        return 1
    for path, line, reason in findings:
        print(f"{path}:{line}: {reason}", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

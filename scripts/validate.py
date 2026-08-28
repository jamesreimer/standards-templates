#!/usr/bin/env python3
"""Validate mechanical repository invariants without third-party dependencies.

The BCP 14 check is deliberately narrow: it detects close spelling mistakes in
uppercase canonical forms found in Markdown prose. It ignores lowercase prose,
fenced code, inline code, and larger identifiers, and it never infers normative
intent or judges whether a keyword has the correct semantic strength.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import html
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote


TEMPLATE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_ENTRY_RE = re.compile(r"^### `([^`]+)`[ \t]*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})(?:[ \t]+|$)(.*)$")
FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})(.*)$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
TOKEN_RE = re.compile(r"(?<![A-Z0-9_])[A-Z0-9]+(?![A-Z0-9_])")

TEMPLATE_METADATA_NAME = "template" + ".yaml"
EXPECTED_TEMPLATE_FILES = {"README.md", "standard.md"}
JUNK_FILE_NAMES = {".DS_Store", "Thumbs.db"}
IGNORED_DIRECTORY_NAMES = {".git", ".venv"}
TEXT_FILE_NAMES = {".editorconfig", ".gitattributes", ".gitignore", "LICENSE"}
TEXT_FILE_SUFFIXES = {".cfg", ".ini", ".json", ".md", ".py", ".toml", ".txt", ".yaml", ".yml"}
STRUCTURE_SNAPSHOT_PATH = "repository-structure.txt"
STRUCTURE_UPDATE_COMMAND = "python3 scripts/update_repository_structure.py"

BCP14_SINGLE_FORMS = (
    "MUST",
    "SHOULD",
    "MAY",
    "SHALL",
    "REQUIRED",
    "RECOMMENDED",
    "OPTIONAL",
)
BCP14_PHRASE_FORMS = (
    "MUST NOT",
    "SHOULD NOT",
    "SHALL NOT",
    "NOT RECOMMENDED",
)


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    reason: str

    def __str__(self) -> str:
        location = f"{self.path}:{self.line}" if self.line else self.path
        return f"{location}: {self.reason}"


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    slug: str
    line: int


@dataclass(frozen=True)
class MarkdownLink:
    destination: str
    line: int


@dataclass
class MarkdownDocument:
    headings: list[Heading]
    links: list[MarkdownLink]

    @property
    def anchors(self) -> set[str]:
        return {heading.slug for heading in self.headings}


class RepositoryValidator:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.findings: list[Finding] = []
        self.text_files: dict[Path, str] = {}
        self.markdown_documents: dict[Path, MarkdownDocument] = {}
        self.template_directories: dict[str, Path] = {}
        self.catalog_titles: dict[str, str] = {}

    def validate(self) -> list[Finding]:
        self._scan_repository_files()
        self._validate_repository_structure_snapshot()
        self._validate_markdown_documents()
        self._validate_template_structure()
        self._validate_catalog_membership()
        self._validate_template_titles()
        self._validate_markdown_links()
        return sorted(set(self.findings))

    def _relative(self, path: Path) -> str:
        try:
            relative = path.resolve().relative_to(self.root)
        except ValueError:
            return str(path)
        return str(relative) if str(relative) != "." else "."

    def _add(self, path: Path, reason: str, line: int = 0) -> None:
        self.findings.append(Finding(self._relative(path), line, reason))

    def _scan_repository_files(self) -> None:
        if not self.root.is_dir():
            self._add(self.root, "repository root does not exist")
            return

        for path in self._repository_files_for_validation():
            file_name = path.name
            relative_parts = path.relative_to(self.root).parts
            if "__pycache__" in relative_parts or file_name in JUNK_FILE_NAMES or path.suffix.lower() == ".pyc":
                self._add(path, "junk artifact file is not allowed")
                continue
            if file_name == TEMPLATE_METADATA_NAME:
                self._add(path, "template metadata files are not allowed")
            if not self._is_text_file(path):
                continue

            try:
                content = path.read_bytes().decode("utf-8")
            except UnicodeDecodeError as error:
                self._add(path, f"text file is not valid UTF-8 ({error})")
                continue

            self.text_files[path.resolve()] = content
            if not content.endswith("\n"):
                self._add(path, "text file must end with a newline")
            if TEMPLATE_METADATA_NAME in content:
                self._add(path, "references the prohibited template metadata filename")

    def _repository_files_for_validation(self) -> list[Path]:
        if (self.root / ".git").exists():
            result = subprocess.run(
                ["git", "-C", str(self.root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if result.returncode == 0:
                return sorted(
                    self.root / Path(relative_path.decode("utf-8"))
                    for relative_path in result.stdout.split(b"\0")
                    if relative_path
                )
            self._add(self.root, "could not enumerate repository files with Git")
            return []

        repository_files: list[Path] = []
        for current, directory_names, file_names in os.walk(self.root):
            current_path = Path(current)
            directory_names.sort()
            file_names.sort()

            retained_directories: list[str] = []
            for directory_name in directory_names:
                directory_path = current_path / directory_name
                if directory_name == "__pycache__":
                    self._add(directory_path, "junk artifact directory is not allowed")
                    continue
                if directory_name in IGNORED_DIRECTORY_NAMES:
                    continue
                retained_directories.append(directory_name)
            directory_names[:] = retained_directories

            for file_name in file_names:
                path = current_path / file_name
                if file_name in JUNK_FILE_NAMES or path.suffix.lower() == ".pyc":
                    self._add(path, "junk artifact file is not allowed")
                    continue
                repository_files.append(path)
        return repository_files

    @staticmethod
    def _is_text_file(path: Path) -> bool:
        return path.name in TEXT_FILE_NAMES or path.suffix.lower() in TEXT_FILE_SUFFIXES

    def _validate_markdown_documents(self) -> None:
        for path, content in sorted(self.text_files.items()):
            if path.suffix.lower() != ".md":
                continue
            document = self._parse_markdown(path, content)
            self.markdown_documents[path] = document
            self._validate_bcp14_near_misses(path, content)

    def _validate_repository_structure_snapshot(self) -> None:
        snapshot_path = (self.root / STRUCTURE_SNAPSHOT_PATH).resolve()
        actual = self.text_files.get(snapshot_path)
        if actual is None:
            self._add(
                snapshot_path,
                f"repository structure snapshot is missing or unreadable; run {STRUCTURE_UPDATE_COMMAND}",
            )
            return
        try:
            expected = render_repository_structure(self.root)
        except RuntimeError as error:
            self._add(snapshot_path, f"could not generate expected repository structure: {error}")
            return
        if actual != expected:
            self._add(
                snapshot_path,
                "repository structure differs from the committed snapshot; "
                f"if intentional, run {STRUCTURE_UPDATE_COMMAND}; "
                "otherwise restore the unexpected paths",
            )

    def _parse_markdown(self, path: Path, content: str) -> MarkdownDocument:
        headings: list[Heading] = []
        links: list[MarkdownLink] = []
        slug_counts: Counter[str] = Counter()
        used_slugs: set[str] = set()
        previous_heading_level = 0
        fence_character: str | None = None
        fence_length = 0
        fence_start_line = 0

        for line_number, line in enumerate(content.splitlines(), 1):
            if fence_character is not None:
                if self._is_closing_fence(line, fence_character, fence_length):
                    fence_character = None
                    fence_length = 0
                    fence_start_line = 0
                continue

            fence_match = FENCE_RE.match(line)
            if fence_match:
                fence = fence_match.group(1)
                fence_character = fence[0]
                fence_length = len(fence)
                fence_start_line = line_number
                continue

            heading_match = HEADING_RE.match(line)
            if heading_match:
                level = len(heading_match.group(1))
                heading_text = re.sub(r"[ \t]+#+[ \t]*$", "", heading_match.group(2)).strip()
                base_slug = github_heading_slug(heading_text)
                slug = unique_heading_slug(base_slug, slug_counts, used_slugs)
                headings.append(Heading(level, heading_text, slug, line_number))
                if previous_heading_level == 0 and level != 1:
                    self._add(path, f"first heading must be H1, found H{level}", line_number)
                elif previous_heading_level and level > previous_heading_level + 1:
                    self._add(
                        path,
                        f"heading level skips from H{previous_heading_level} to H{level}",
                        line_number,
                    )
                previous_heading_level = level

            prose_line = strip_inline_code(line)
            for link_match in LINK_RE.finditer(prose_line):
                destination = parse_link_destination(link_match.group(1))
                if destination:
                    links.append(MarkdownLink(destination, line_number))

        if fence_character is not None:
            self._add(path, "fenced code block is not closed", fence_start_line)

        h1_count = sum(heading.level == 1 for heading in headings)
        if h1_count != 1:
            self._add(path, f"Markdown document must contain exactly one H1; found {h1_count}")

        return MarkdownDocument(headings, links)

    @staticmethod
    def _is_closing_fence(line: str, character: str, minimum_length: int) -> bool:
        escaped = re.escape(character)
        return bool(re.match(rf"^[ \t]{{0,3}}{escaped}{{{minimum_length},}}[ \t]*$", line))

    def _validate_template_structure(self) -> None:
        templates_root = self.root / "templates"
        if not templates_root.is_dir():
            self._add(templates_root, "templates directory is missing")
            return

        for child in sorted(templates_root.iterdir()):
            if not child.is_dir():
                self._add(child, "templates directory may contain template directories only")
                continue

            template_id = child.name
            self.template_directories[template_id] = child
            if not TEMPLATE_ID_RE.fullmatch(template_id):
                self._add(child, "template ID must use lowercase ASCII alphanumerics separated by single hyphens")

            actual_entries = {entry.name for entry in child.iterdir()}
            for missing_name in sorted(EXPECTED_TEMPLATE_FILES - actual_entries):
                self._add(child / missing_name, "required template file is missing")
            for unexpected_name in sorted(actual_entries - EXPECTED_TEMPLATE_FILES):
                self._add(child / unexpected_name, "unexpected entry in template directory")

    def _validate_catalog_membership(self) -> None:
        catalog_path = (self.root / "CATALOG.md").resolve()
        catalog_text = self.text_files.get(catalog_path)
        if catalog_text is None:
            self._add(catalog_path, "catalog is missing or unreadable")
            return

        section_match = re.search(r"^## Templates[ \t]*$", catalog_text, re.MULTILINE)
        if not section_match:
            self._add(catalog_path, "catalog is missing the Templates section")
            return
        next_section = re.search(r"^## [^#].*$", catalog_text[section_match.end() :], re.MULTILINE)
        section_end = section_match.end() + next_section.start() if next_section else len(catalog_text)
        templates_section = catalog_text[section_match.end() : section_end]
        entry_matches = list(CATALOG_ENTRY_RE.finditer(templates_section))
        entry_ids = [entry.group(1) for entry in entry_matches]
        entry_counts = Counter(entry_ids)

        for template_id, count in sorted(entry_counts.items()):
            if count != 1:
                self._add(catalog_path, f"template {template_id!r} appears {count} times in the catalog")

        directory_ids = set(self.template_directories)
        catalog_ids = set(entry_ids)
        for template_id in sorted(directory_ids - catalog_ids):
            self._add(catalog_path, f"template directory {template_id!r} is missing from the catalog")
        for template_id in sorted(catalog_ids - directory_ids):
            self._add(catalog_path, f"catalog entry {template_id!r} has no template directory")

        for index, entry in enumerate(entry_matches):
            template_id = entry.group(1)
            start = entry.end()
            end = entry_matches[index + 1].start() if index + 1 < len(entry_matches) else len(templates_section)
            entry_body = templates_section[start:end]
            title_match = re.search(r"^\*\*([^\n]+)\*\*[ \t]*$", entry_body, re.MULTILINE)
            if not title_match:
                self._add(catalog_path, f"catalog entry {template_id!r} is missing its human-facing title")
                continue
            self.catalog_titles[template_id] = title_match.group(1).strip()

    def _validate_template_titles(self) -> None:
        for template_id, directory in sorted(self.template_directories.items()):
            readme_path = (directory / "README.md").resolve()
            standard_path = (directory / "standard.md").resolve()
            readme_text = self.text_files.get(readme_path)
            standard_document = self.markdown_documents.get(standard_path)

            readme_title: str | None = None
            if readme_text is not None:
                title_match = re.search(
                    r"^Human-facing title:[ \t]*\n(?:[ \t]*\n)*>[ \t]*\*\*([^\n]+?)\*\*[ \t]*$",
                    readme_text,
                    re.MULTILINE,
                )
                if title_match:
                    readme_title = title_match.group(1).strip()
                else:
                    self._add(readme_path, "cannot find the human-facing title using the repository convention")

            standard_title: str | None = None
            if standard_document is not None:
                h1_headings = [heading for heading in standard_document.headings if heading.level == 1]
                if len(h1_headings) == 1:
                    standard_title = h1_headings[0].text

            catalog_title = self.catalog_titles.get(template_id)
            available_titles = {
                "template README": readme_title,
                "standard H1": standard_title,
                "catalog": catalog_title,
            }
            distinct_titles = {title for title in available_titles.values() if title is not None}
            if len(distinct_titles) > 1:
                details = ", ".join(
                    f"{source}={title!r}" for source, title in available_titles.items() if title is not None
                )
                self._add(directory, f"human-facing template titles do not agree ({details})")

    def _validate_markdown_links(self) -> None:
        for source_path, document in sorted(self.markdown_documents.items()):
            for link in document.links:
                destination = html.unescape(link.destination).strip()
                if is_external_destination(destination):
                    continue

                path_part, separator, fragment = destination.partition("#")
                path_part = unquote(path_part.partition("?")[0])
                if path_part.startswith("/"):
                    target_path = (self.root / path_part.lstrip("/")).resolve()
                elif path_part:
                    target_path = (source_path.parent / path_part).resolve()
                else:
                    target_path = source_path

                try:
                    target_path.relative_to(self.root)
                except ValueError:
                    self._add(source_path, f"local link escapes the repository: {destination}", link.line)
                    continue

                if not target_path.exists():
                    self._add(source_path, f"local link target does not exist: {destination}", link.line)
                    continue

                if not separator:
                    continue
                if target_path.is_dir():
                    self._add(source_path, f"cannot validate an anchor on a directory link: {destination}", link.line)
                    continue
                if target_path.suffix.lower() != ".md":
                    self._add(source_path, f"anchor target is not a Markdown document: {destination}", link.line)
                    continue

                target_document = self.markdown_documents.get(target_path)
                if target_document is None:
                    self._add(source_path, f"anchor target is unreadable: {destination}", link.line)
                    continue
                anchor = unquote(fragment).lower()
                if not anchor or anchor not in target_document.anchors:
                    self._add(source_path, f"Markdown anchor does not exist: {destination}", link.line)

    def _validate_bcp14_near_misses(self, path: Path, content: str) -> None:
        fence_character: str | None = None
        fence_length = 0

        for line_number, line in enumerate(content.splitlines(), 1):
            if fence_character is not None:
                if self._is_closing_fence(line, fence_character, fence_length):
                    fence_character = None
                    fence_length = 0
                continue

            fence_match = FENCE_RE.match(line)
            if fence_match:
                fence = fence_match.group(1)
                fence_character = fence[0]
                fence_length = len(fence)
                continue

            prose = strip_inline_code(line)
            prose = re.sub(r"!?\[([^\]]*)\]\([^)]+\)", r"\1", prose)
            prose = re.sub(r"<https?://[^>]+>", " ", prose, flags=re.IGNORECASE)
            prose = re.sub(r"https?://\S+", " ", prose, flags=re.IGNORECASE)
            tokens = list(TOKEN_RE.finditer(prose))
            consumed_indices: set[int] = set()

            for index in range(len(tokens) - 1):
                between = prose[tokens[index].end() : tokens[index + 1].start()]
                if not re.fullmatch(r"\s+", between):
                    continue
                candidate = f"{tokens[index].group()} {tokens[index + 1].group()}"
                if candidate in BCP14_PHRASE_FORMS:
                    continue
                if any(is_phrase_near_miss(candidate, canonical) for canonical in BCP14_PHRASE_FORMS):
                    self._add(
                        path,
                        f"malformed BCP 14 keyword near-miss {candidate!r}; spelling only was checked",
                        line_number,
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
                        path,
                        f"malformed BCP 14 keyword near-miss {candidate!r}; spelling only was checked",
                        line_number,
                    )


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


def visible_repository_files(root: Path) -> list[Path]:
    """Return visible tracked and unignored files used by the structure snapshot."""
    root = root.resolve()
    if (root / ".git").exists():
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(detail or "Git could not enumerate repository files")
        return sorted(
            root / Path(relative_path.decode("utf-8"))
            for relative_path in result.stdout.split(b"\0")
            if relative_path
        )

    files: list[Path] = []
    for current, directory_names, file_names in os.walk(root):
        current_path = Path(current)
        directory_names[:] = sorted(
            directory_name
            for directory_name in directory_names
            if directory_name not in IGNORED_DIRECTORY_NAMES | {"__pycache__"}
        )
        for file_name in sorted(file_names):
            path = current_path / file_name
            if file_name in JUNK_FILE_NAMES or path.suffix.lower() == ".pyc":
                continue
            files.append(path)
    return files


def render_repository_structure(root: Path) -> str:
    """Render the exact deterministic format stored in the structure snapshot."""
    root = root.resolve()
    file_paths = {
        path.resolve().relative_to(root).as_posix()
        for path in visible_repository_files(root)
    }
    file_paths.add(STRUCTURE_SNAPSHOT_PATH)

    directory_paths: set[str] = set()
    for file_path in file_paths:
        parent = Path(file_path).parent
        while parent != Path("."):
            directory_paths.add(f"{parent.as_posix()}/")
            parent = parent.parent

    entries = sorted(directory_paths | file_paths)
    header = (
        f"# Generated by {STRUCTURE_UPDATE_COMMAND}\n"
        "# Regenerate after intentional repository structure changes.\n\n"
    )
    return header + "\n".join(entries) + "\n"


def parse_link_destination(raw_destination: str) -> str:
    destination = raw_destination.strip()
    if destination.startswith("<"):
        closing = destination.find(">")
        return destination[1:closing] if closing != -1 else ""
    return destination.split(maxsplit=1)[0] if destination else ""


def is_external_destination(destination: str) -> bool:
    return bool(destination.startswith("//") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", destination))


def github_heading_slug(heading_text: str) -> str:
    """Return the GitHub-style base slug needed by this repository's headings."""
    value = html.unescape(heading_text.strip())
    value = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("`", "").replace("*", "")
    slug_characters: list[str] = []
    for character in value.lower():
        if character.isspace():
            slug_characters.append("-")
        elif character in {"-", "_"}:
            slug_characters.append(character)
        elif unicodedata.category(character).startswith(("P", "S")):
            continue
        else:
            slug_characters.append(character)
    return "".join(slug_characters)


def unique_heading_slug(base_slug: str, counts: Counter[str], used_slugs: set[str]) -> str:
    candidate = base_slug
    if candidate in used_slugs:
        suffix = counts[base_slug] or 1
        while f"{base_slug}-{suffix}" in used_slugs:
            suffix += 1
        candidate = f"{base_slug}-{suffix}"
        counts[base_slug] = suffix + 1
    else:
        counts[base_slug] = 1
    used_slugs.add(candidate)
    return candidate


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
                distances[row][column] = min(distances[row][column], distances[row - 2][column - 2] + 1)
    return distances[-1][-1]


def is_single_near_miss(candidate: str, canonical: str) -> bool:
    if candidate == canonical or not candidate or candidate[0] != canonical[0]:
        return False
    distance = damerau_levenshtein(candidate, canonical)
    if len(canonical) <= 4:
        return distance == 1 and (candidate.startswith(canonical) or canonical.startswith(candidate))
    return distance == 1


def is_phrase_near_miss(candidate: str, canonical: str) -> bool:
    if candidate == canonical or candidate[0] != canonical[0]:
        return False
    return abs(len(candidate) - len(canonical)) <= 1 and damerau_levenshtein(candidate, canonical) == 1


def validate_repository(root: Path) -> list[Finding]:
    return RepositoryValidator(root).validate()


def main() -> int:
    repository_root = Path(__file__).resolve().parents[1]
    findings = validate_repository(repository_root)
    if findings:
        for finding in findings:
            print(finding, file=sys.stderr)
        print(f"Validation failed: {len(findings)} error(s).", file=sys.stderr)
        return 1

    template_count = sum(1 for child in (repository_root / "templates").iterdir() if child.is_dir())
    markdown_count = sum(path.suffix.lower() == ".md" for path in repository_root.rglob("*.md"))
    print(f"Validation passed: {template_count} templates, {markdown_count} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

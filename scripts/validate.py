#!/usr/bin/env python3
"""Validate mechanical repository invariants without third-party dependencies.

The BCP 14 check is deliberately narrow: it detects close spelling mistakes in
uppercase canonical forms found in Markdown prose. Short forms only permit a
missing or duplicated final character; longer forms must share their first
three and final characters before edit distance is considered. The check
ignores lowercase prose, fenced code, inline code, and larger identifiers, and
it never infers normative intent or judges whether a keyword has the correct
semantic strength.
"""

from __future__ import annotations

import html
import os
import posixpath
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

TEMPLATE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STABLE_TEMPLATE_ID_DECLARATION_RE = re.compile(
    r"^Stable template ID: `([^`\n]+)`[ \t]*$", re.MULTILINE
)
LOCAL_REQUIREMENT_SCHEME_DECLARATION_RE = re.compile(
    r"^`([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-NNN)` identifies a local requirement "
    r"synthesized by this template\b",
    re.MULTILINE,
)
LOCAL_REQUIREMENT_DEFINITION_RE = re.compile(
    r"^\*\*([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+) — [^*\n]+\.\*\*", re.MULTILINE
)
LOCAL_REQUIREMENT_REFERENCE_RE = re.compile(r"^([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)-([0-9]{3})$")
ORDINARY_PATH_COMPONENT_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ORDINARY_FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+(?:-[a-z0-9]+)*)*$")
PYTHON_FILENAME_RE = re.compile(r"^(?:[a-z][a-z0-9]*(?:_[a-z0-9]+)*|__init__)\.py$")
CATALOG_ENTRY_RE = re.compile(r"^### `([^`]+)`[ \t]*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})(?:[ \t]+|$)(.*)$")
FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})(.*)$")
TOKEN_RE = re.compile(r"(?<![A-Z0-9_])[A-Z0-9]+(?![A-Z0-9_])")
REFERENCE_DEFINITION_RE = re.compile(r"^[ \t]{0,3}\[([^\]\n]+)\]:[ \t]*(.*)$")
REFERENCE_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]+)\]\[([^\]\n]*)\]")

TEMPLATE_METADATA_NAME = "template" + ".yaml"
EXPECTED_TEMPLATE_FILES = {"README.md", "standard.md"}
JUNK_FILE_NAMES = {".DS_Store", "Thumbs.db"}
IGNORED_DIRECTORY_NAMES = {".git", ".venv"}
TEXT_FILE_NAMES = {".editorconfig", ".gitattributes", ".gitignore", "LICENSE"}
TEXT_FILE_SUFFIXES = {".cfg", ".ini", ".json", ".md", ".py", ".toml", ".txt", ".yaml", ".yml"}
STRUCTURE_SNAPSHOT_PATH = "repository-structure.txt"
STRUCTURE_UPDATE_COMMAND = "python3 scripts/update_repository_structure.py"
ROOT_PATH_NAME_EXCEPTIONS = {
    "ADOPTION.md",
    "AGENTS.md",
    "CATALOG.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "MAINTAINING.md",
    "NAMING.md",
    "README.md",
    "SECURITY.md",
}
ROOT_TOOL_FILE_NAMES = {
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    ".markdownlint-cli2.jsonc",
}
TOOL_OWNED_ROOT_DIRECTORIES = {".github", ".githooks", ".vscode"}
PYTHON_OWNED_ROOT_DIRECTORIES = {"scripts", "tests"}

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


@dataclass(frozen=True)
class MarkdownLine:
    number: int
    text: str
    prose: str


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
        self.local_requirement_definitions: dict[str, list[tuple[Path, int]]] = {}
        self.local_requirement_prefixes: set[str] = set()
        self.repository_files: set[str] = set()
        self.repository_directories: set[str] = {"."}

    def validate(self) -> list[Finding]:
        self._scan_repository_files()
        self._validate_repository_path_names()
        self._validate_repository_structure_snapshot()
        self._validate_markdown_documents()
        self._validate_template_structure()
        self._validate_stable_template_ids()
        self._validate_local_requirement_ids()
        self._validate_local_requirement_references()
        self._validate_catalog_membership()
        self._validate_template_titles()
        self._validate_markdown_links()
        return sorted(set(self.findings))

    def _relative(self, path: Path) -> str:
        try:
            relative = path.relative_to(self.root)
        except ValueError:
            return str(path)
        return str(relative) if str(relative) != "." else "."

    def _add(self, path: Path, reason: str, line: int = 0) -> None:
        self.findings.append(Finding(self._relative(path), line, reason))

    def _scan_repository_files(self) -> None:
        if not self.root.is_dir():
            self._add(self.root, "repository root does not exist")
            return

        repository_paths = self._repository_files_for_validation()
        for path in repository_paths:
            relative_path = path.relative_to(self.root).as_posix()
            self.repository_files.add(relative_path)
            parent = Path(relative_path).parent
            while parent != Path("."):
                self.repository_directories.add(parent.as_posix())
                parent = parent.parent

        for path in repository_paths:
            file_name = path.name
            relative_parts = path.relative_to(self.root).parts
            if (
                "__pycache__" in relative_parts
                or file_name in JUNK_FILE_NAMES
                or path.suffix.lower() == ".pyc"
            ):
                self._add(path, "junk artifact file is not allowed")
                continue
            if file_name == TEMPLATE_METADATA_NAME:
                self._add(path, "template metadata files are not allowed")
            if path.is_symlink():
                self._add(path, "symbolic links are not allowed; the link target was not read")
                continue
            if not self._is_text_file(path):
                continue

            try:
                content = path.read_bytes().decode("utf-8")
            except UnicodeDecodeError as error:
                self._add(path, f"text file is not valid UTF-8 ({error})")
                continue
            except OSError as error:
                self._add(path, f"repository file could not be read ({error.strerror or error})")
                continue

            self.text_files[path] = content
            if not content.endswith("\n"):
                self._add(path, "text file must end with a newline")
            if TEMPLATE_METADATA_NAME in content:
                self._add(path, "references the prohibited template metadata filename")

    def _repository_files_for_validation(self) -> list[Path]:
        if (self.root / ".git").exists():
            result = subprocess.run(
                [
                    "git",
                    "-C",
                    str(self.root),
                    "ls-files",
                    "--cached",
                    "--others",
                    "--exclude-standard",
                    "-z",
                ],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if result.returncode == 0:
                try:
                    relative_paths = [
                        relative_path.decode("utf-8")
                        for relative_path in result.stdout.split(b"\0")
                        if relative_path
                    ]
                except UnicodeDecodeError as error:
                    self._add(
                        self.root,
                        f"Git returned a repository path that is not valid UTF-8 ({error})",
                    )
                    return []
                return sorted(self.root / Path(relative_path) for relative_path in relative_paths)
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
                if directory_path.is_symlink():
                    repository_files.append(directory_path)
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

    def _validate_repository_path_names(self) -> None:
        for relative_path in sorted(self.repository_directories - {"."}):
            self._validate_repository_path_name(relative_path, is_directory=True)
        for relative_path in sorted(self.repository_files):
            self._validate_repository_path_name(relative_path, is_directory=False)

    def _validate_repository_path_name(self, relative_path: str, *, is_directory: bool) -> None:
        parts = Path(relative_path).parts
        if not parts:
            return

        name = parts[-1]
        if parts[0] in TOOL_OWNED_ROOT_DIRECTORIES:
            return
        if len(parts) == 1 and name in ROOT_TOOL_FILE_NAMES | ROOT_PATH_NAME_EXCEPTIONS:
            return

        if parts[0] == "templates":
            if len(parts) == 2 and is_directory:
                return
            if len(parts) == 3 and not is_directory and name in EXPECTED_TEMPLATE_FILES:
                return

        if not is_directory and parts[0] in PYTHON_OWNED_ROOT_DIRECTORIES and name.endswith(".py"):
            if not PYTHON_FILENAME_RE.fullmatch(name):
                self._add(
                    self.root / relative_path,
                    f"path component {name!r} must use lowercase ASCII snake_case "
                    "with a lowercase .py extension in this Python-owned directory",
                )
            return

        expected_pattern = ORDINARY_PATH_COMPONENT_RE if is_directory else ORDINARY_FILENAME_RE
        if not expected_pattern.fullmatch(name):
            self._add(
                self.root / relative_path,
                f"path component {name!r} must use lowercase ASCII alphanumeric words "
                "separated by single hyphens, with a lowercase extension when applicable",
            )

    def _validate_markdown_documents(self) -> None:
        for path, content in sorted(self.text_files.items()):
            if path.suffix.lower() != ".md":
                continue
            document = self._parse_markdown(path, content)
            self.markdown_documents[path] = document
            self._validate_bcp14_near_misses(path, content)

    def _validate_repository_structure_snapshot(self) -> None:
        snapshot_path = self.root / STRUCTURE_SNAPSHOT_PATH
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
        markdown_lines, fence_start_line = scan_markdown_lines(content)
        reference_definitions: dict[str, MarkdownLink] = {}
        reference_uses: list[tuple[str, int]] = []

        for markdown_line in markdown_lines:
            line_number = markdown_line.number
            line = markdown_line.text

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

            prose_line = markdown_line.prose
            definition_match = REFERENCE_DEFINITION_RE.match(prose_line)
            if definition_match:
                label = normalize_reference_label(definition_match.group(1))
                destination = parse_link_destination(definition_match.group(2))
                if not destination:
                    self._add(
                        path,
                        f"malformed reference-style link definition: {definition_match.group(1)}",
                        line_number,
                    )
                elif label in reference_definitions:
                    self._add(
                        path,
                        f"duplicate reference-style link definition: {definition_match.group(1)}",
                        line_number,
                    )
                else:
                    reference_definitions[label] = MarkdownLink(destination, line_number)
                continue

            for raw_destination in scan_inline_link_destinations(prose_line):
                destination = parse_link_destination(raw_destination)
                if destination:
                    links.append(MarkdownLink(destination, line_number))

            for reference_match in REFERENCE_LINK_RE.finditer(prose_line):
                label_text = reference_match.group(2) or reference_match.group(1)
                reference_uses.append((normalize_reference_label(label_text), line_number))

        if fence_start_line:
            self._add(path, "fenced code block is not closed", fence_start_line)

        for label, line_number in reference_uses:
            definition = reference_definitions.get(label)
            if definition is None:
                self._add(
                    path, f"reference-style link definition does not exist: {label}", line_number
                )
                continue
            links.append(definition)

        h1_count = sum(heading.level == 1 for heading in headings)
        if h1_count != 1:
            self._add(path, f"Markdown document must contain exactly one H1; found {h1_count}")

        return MarkdownDocument(headings, links)

    def _validate_template_structure(self) -> None:
        templates_root = self.root / "templates"
        if templates_root.is_symlink():
            return
        if not templates_root.is_dir():
            self._add(templates_root, "templates directory is missing")
            return

        for child in sorted(templates_root.iterdir()):
            if child.is_symlink():
                continue
            if not child.is_dir():
                self._add(child, "templates directory may contain template directories only")
                continue

            template_id = child.name
            self.template_directories[template_id] = child
            if not TEMPLATE_ID_RE.fullmatch(template_id):
                self._add(
                    child,
                    "template ID must use lowercase ASCII alphanumerics separated by single hyphens",
                )

            actual_entries = {entry.name for entry in child.iterdir()}
            for missing_name in sorted(EXPECTED_TEMPLATE_FILES - actual_entries):
                self._add(child / missing_name, "required template file is missing")
            for unexpected_name in sorted(actual_entries - EXPECTED_TEMPLATE_FILES):
                self._add(child / unexpected_name, "unexpected entry in template directory")

    def _validate_stable_template_ids(self) -> None:
        for template_id, directory in sorted(self.template_directories.items()):
            readme_path = directory / "README.md"
            readme_text = self.text_files.get(readme_path)
            if readme_text is None:
                continue

            structural_text = markdown_without_fenced_code(readme_text)
            declarations = STABLE_TEMPLATE_ID_DECLARATION_RE.findall(structural_text)
            if len(declarations) != 1:
                self._add(
                    readme_path,
                    "template README must contain exactly one stable template ID declaration "
                    f"using the repository convention; found {len(declarations)}",
                )
                continue

            declared_id = declarations[0]
            if declared_id != template_id:
                self._add(
                    readme_path,
                    f"declares stable template ID {declared_id!r}; "
                    f"expected directory ID {template_id!r}",
                )

    def _validate_local_requirement_ids(self) -> None:
        for directory in sorted(self.template_directories.values()):
            standard_path = directory / "standard.md"
            standard_text = self.text_files.get(standard_path)
            if standard_text is None:
                continue

            structural_text = markdown_without_fenced_code(standard_text)
            schemes = LOCAL_REQUIREMENT_SCHEME_DECLARATION_RE.findall(structural_text)
            self.local_requirement_prefixes.update(
                scheme.removesuffix("-NNN") for scheme in schemes
            )
            if len(schemes) > 1:
                self._add(
                    standard_path,
                    f"declares {len(schemes)} local requirement ID schemes {schemes!r}; "
                    "expected at most one declaration using 'PREFIX-NNN'",
                )
                continue
            if not schemes:
                continue

            scheme = schemes[0]
            prefix = scheme.removesuffix("-NNN")
            expected_id_re = re.compile(rf"^{re.escape(prefix)}-[0-9]{{3}}$")
            definition_ids: list[tuple[str, int]] = []
            for match in LOCAL_REQUIREMENT_DEFINITION_RE.finditer(structural_text):
                requirement_id = match.group(1)
                line_number = structural_text.count("\n", 0, match.start()) + 1
                if not expected_id_re.fullmatch(requirement_id):
                    self._add(
                        standard_path,
                        f"requirement definition label {requirement_id!r} does not match "
                        f"declared scheme {scheme!r}; expected prefix {prefix!r} "
                        "with exactly three decimal digits",
                        line_number,
                    )
                    continue
                definition_ids.append((requirement_id, line_number))
                self.local_requirement_definitions.setdefault(requirement_id, []).append(
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
                        f"duplicate local requirement ID {requirement_id!r}; "
                        f"declared scheme is {scheme!r}",
                        duplicate_line,
                    )

    def _validate_local_requirement_references(self) -> None:
        for directory in sorted(self.template_directories.values()):
            standard_path = directory / "standard.md"
            standard_text = self.text_files.get(standard_path)
            if standard_text is None:
                continue

            markdown_lines, _ = scan_markdown_lines(standard_text)
            for markdown_line in markdown_lines:
                for code_span in scan_inline_code_spans(markdown_line.text):
                    reference_match = LOCAL_REQUIREMENT_REFERENCE_RE.fullmatch(code_span)
                    if reference_match is None:
                        continue
                    prefix = reference_match.group(1)
                    if prefix not in self.local_requirement_prefixes:
                        continue

                    definitions = self.local_requirement_definitions.get(code_span, [])
                    if len(definitions) == 1:
                        continue
                    if not definitions:
                        reason = (
                            f"unresolved local requirement reference {code_span!r}; "
                            f"no valid definition exists for declared prefix {prefix!r}"
                        )
                    else:
                        reason = (
                            f"local requirement reference {code_span!r} resolves to "
                            f"{len(definitions)} definitions; expected exactly one"
                        )
                    self._add(standard_path, reason, markdown_line.number)

    def _validate_catalog_membership(self) -> None:
        catalog_path = self.root / "CATALOG.md"
        catalog_text = self.text_files.get(catalog_path)
        if catalog_text is None:
            self._add(catalog_path, "catalog is missing or unreadable")
            return

        structural_text = markdown_without_fenced_code(catalog_text)
        section_match = re.search(r"^## Templates[ \t]*$", structural_text, re.MULTILINE)
        if not section_match:
            self._add(catalog_path, "catalog is missing the Templates section")
            return
        next_section = re.search(
            r"^## [^#].*$", structural_text[section_match.end() :], re.MULTILINE
        )
        section_end = (
            section_match.end() + next_section.start() if next_section else len(catalog_text)
        )
        templates_section = structural_text[section_match.end() : section_end]
        entry_matches = list(CATALOG_ENTRY_RE.finditer(templates_section))
        entry_ids = [entry.group(1) for entry in entry_matches]
        entry_counts = Counter(entry_ids)

        for template_id, count in sorted(entry_counts.items()):
            if count != 1:
                self._add(
                    catalog_path, f"template {template_id!r} appears {count} times in the catalog"
                )

        directory_ids = set(self.template_directories)
        catalog_ids = set(entry_ids)
        for template_id in sorted(directory_ids - catalog_ids):
            self._add(
                catalog_path, f"template directory {template_id!r} is missing from the catalog"
            )
        for template_id in sorted(catalog_ids - directory_ids):
            self._add(catalog_path, f"catalog entry {template_id!r} has no template directory")

        for index, entry in enumerate(entry_matches):
            template_id = entry.group(1)
            start = entry.end()
            end = (
                entry_matches[index + 1].start()
                if index + 1 < len(entry_matches)
                else len(templates_section)
            )
            entry_body = templates_section[start:end]
            title_match = re.search(r"^\*\*([^\n]+)\*\*[ \t]*$", entry_body, re.MULTILINE)
            if not title_match:
                self._add(
                    catalog_path, f"catalog entry {template_id!r} is missing its human-facing title"
                )
                continue
            self.catalog_titles[template_id] = title_match.group(1).strip()

    def _validate_template_titles(self) -> None:
        for template_id, directory in sorted(self.template_directories.items()):
            readme_path = directory / "README.md"
            standard_path = directory / "standard.md"
            readme_text = self.text_files.get(readme_path)
            standard_document = self.markdown_documents.get(standard_path)

            readme_title: str | None = None
            if readme_text is not None:
                structural_text = markdown_without_fenced_code(readme_text)
                title_match = re.search(
                    r"^Human-facing title:[ \t]*\n(?:[ \t]*\n)*>[ \t]*\*\*([^\n]+?)\*\*[ \t]*$",
                    structural_text,
                    re.MULTILINE,
                )
                if title_match:
                    readme_title = title_match.group(1).strip()
                else:
                    self._add(
                        readme_path,
                        "cannot find the human-facing title using the repository convention",
                    )

            standard_title: str | None = None
            if standard_document is not None:
                h1_headings = [
                    heading for heading in standard_document.headings if heading.level == 1
                ]
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
                    f"{source}={title!r}"
                    for source, title in available_titles.items()
                    if title is not None
                )
                self._add(directory, f"human-facing template titles do not agree ({details})")

    def _validate_markdown_links(self) -> None:
        for source_path, document in sorted(self.markdown_documents.items()):
            for link in document.links:
                destination = html.unescape(link.destination).strip()
                if is_external_destination(destination):
                    continue

                path_part, separator, fragment = destination.partition("#")
                path_part = unquote(path_part.partition("?")[0]).replace("\\", "/")
                source_relative = source_path.relative_to(self.root).as_posix()
                if path_part.startswith("/"):
                    target_relative = posixpath.normpath(path_part.lstrip("/"))
                elif path_part:
                    target_relative = posixpath.normpath(
                        posixpath.join(posixpath.dirname(source_relative), path_part)
                    )
                else:
                    target_relative = source_relative

                if target_relative == ".." or target_relative.startswith("../"):
                    self._add(
                        source_path, f"local link escapes the repository: {destination}", link.line
                    )
                    continue

                if (
                    target_relative not in self.repository_files
                    and target_relative not in self.repository_directories
                ):
                    self._add(
                        source_path, f"local link target does not exist: {destination}", link.line
                    )
                    continue

                target_path = self.root / Path(target_relative)

                if not separator:
                    continue
                if target_relative in self.repository_directories:
                    self._add(
                        source_path,
                        f"cannot validate an anchor on a directory link: {destination}",
                        link.line,
                    )
                    continue
                if target_path.suffix.lower() != ".md":
                    self._add(
                        source_path,
                        f"anchor target is not a Markdown document: {destination}",
                        link.line,
                    )
                    continue

                target_document = self.markdown_documents.get(target_path)
                if target_document is None:
                    self._add(source_path, f"anchor target is unreadable: {destination}", link.line)
                    continue
                anchor = unquote(fragment)
                if not anchor or anchor not in target_document.anchors:
                    self._add(
                        source_path, f"Markdown anchor does not exist: {destination}", link.line
                    )

    def _validate_bcp14_near_misses(self, path: Path, content: str) -> None:
        markdown_lines, _ = scan_markdown_lines(content)
        for markdown_line in markdown_lines:
            line_number = markdown_line.number
            prose = markdown_line.prose
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
                if any(
                    is_phrase_near_miss(candidate, canonical) for canonical in BCP14_PHRASE_FORMS
                ):
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
                if any(
                    is_single_near_miss(candidate, canonical) for canonical in BCP14_SINGLE_FORMS
                ):
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


def scan_inline_code_spans(line: str) -> list[str]:
    """Return exact contents of closed backtick-delimited inline code spans."""
    spans: list[str] = []
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


def scan_markdown_lines(content: str) -> tuple[list[MarkdownLine], int]:
    """Return non-fenced lines with inline code masked and any open fence line.

    This is the repository-specific lexical layer shared by structural
    extraction, headings, links, and BCP 14 checks. It intentionally does not
    attempt to implement all of CommonMark.
    """
    lines: list[MarkdownLine] = []
    fence_character: str | None = None
    fence_length = 0
    fence_start_line = 0

    for line_number, line in enumerate(content.splitlines(), 1):
        if fence_character is not None:
            if is_closing_fence(line, fence_character, fence_length):
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

        lines.append(MarkdownLine(line_number, line, strip_inline_code(line)))

    return lines, fence_start_line


def markdown_without_fenced_code(content: str) -> str:
    """Mask fenced lines while preserving offsets used by structural regexes."""
    visible_line_numbers = {line.number for line in scan_markdown_lines(content)[0]}
    return "".join(
        line if line_number in visible_line_numbers else "\n" if line.endswith("\n") else ""
        for line_number, line in enumerate(content.splitlines(keepends=True), 1)
    )


def scan_inline_link_destinations(line: str) -> list[str]:
    """Extract inline-link destinations with balanced-parenthesis handling."""
    destinations: list[str] = []
    index = 0
    while index < len(line):
        label_start = line.find("[", index)
        if label_start == -1:
            break
        label_end = line.find("]", label_start + 1)
        if label_end == -1 or label_end + 1 >= len(line) or line[label_end + 1] != "(":
            index = label_start + 1
            continue

        destination_start = label_end + 2
        index = destination_start
        depth = 1
        escaped = False
        while index < len(line):
            character = line[index]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0:
                    destinations.append(line[destination_start:index])
                    index += 1
                    break
            index += 1
    return destinations


def normalize_reference_label(label: str) -> str:
    """Normalize the supported GitHub-style reference label subset."""
    return " ".join(label.strip().split()).casefold()


def visible_repository_files(root: Path) -> list[Path]:
    """Return visible tracked and unignored files used by the structure snapshot."""
    root = root.resolve()
    if (root / ".git").exists():
        result = subprocess.run(
            [
                "git",
                "-C",
                str(root),
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "-z",
            ],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(detail or "Git could not enumerate repository files")
        try:
            relative_paths = [
                relative_path.decode("utf-8")
                for relative_path in result.stdout.split(b"\0")
                if relative_path
            ]
        except UnicodeDecodeError as error:
            raise RuntimeError(
                f"Git returned a repository path that is not valid UTF-8 ({error})"
            ) from error
        return sorted(root / Path(relative_path) for relative_path in relative_paths)

    files: list[Path] = []
    for current, directory_names, file_names in os.walk(root):
        current_path = Path(current)
        retained_directories: list[str] = []
        for directory_name in sorted(directory_names):
            directory_path = current_path / directory_name
            if directory_name in IGNORED_DIRECTORY_NAMES | {"__pycache__"}:
                continue
            if directory_path.is_symlink():
                files.append(directory_path)
                continue
            retained_directories.append(directory_name)
        directory_names[:] = retained_directories
        for file_name in sorted(file_names):
            path = current_path / file_name
            if file_name in JUNK_FILE_NAMES or path.suffix.lower() == ".pyc":
                continue
            files.append(path)
    return files


def render_repository_structure(root: Path) -> str:
    """Render the exact deterministic format stored in the structure snapshot."""
    root = root.resolve()
    file_paths = {path.relative_to(root).as_posix() for path in visible_repository_files(root)}
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
    value = strip_underscore_emphasis(value)
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


def strip_underscore_emphasis(value: str) -> str:
    """Remove underscore emphasis delimiters without removing intraword underscores."""
    emphasis = re.compile(r"(?<![\w])(_{1,2})(?=\S)(.+?)(?<=\S)\1(?![\w])")
    previous = None
    while value != previous:
        previous = value
        value = emphasis.sub(r"\2", value)
    return value


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
    distance = damerau_levenshtein(candidate, canonical)
    return distance == 1


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

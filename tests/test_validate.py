from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPOSITORY_ROOT / "scripts" / "validate.py"
SPEC = importlib.util.spec_from_file_location("repository_validate", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load repository validator")
VALIDATE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATE
SPEC.loader.exec_module(VALIDATE)

HOOK_SETUP_PATH = REPOSITORY_ROOT / "scripts" / "setup_git_hooks.py"
HOOK_SPEC = importlib.util.spec_from_file_location("repository_setup_git_hooks", HOOK_SETUP_PATH)
if HOOK_SPEC is None or HOOK_SPEC.loader is None:
    raise RuntimeError("could not load Git hook setup")
HOOK_SETUP = importlib.util.module_from_spec(HOOK_SPEC)
HOOK_SPEC.loader.exec_module(HOOK_SETUP)

TEMPLATE_METADATA_NAME = "template" + ".yaml"


class RepositoryValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self._create_valid_fixture()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _write(self, relative_path: str, content: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).lstrip("\n"), encoding="utf-8")
        return path

    def _create_valid_fixture(self) -> None:
        self._write(
            "README.md",
            """
            # Fixture Repository

            Ordinary prose should, must, and may remain ordinary English.
            """,
        )
        self._write(
            "CATALOG.md",
            """
            # Template Catalog

            ## Templates

            ### `example-template`

            **Example Standard**
            """,
        )
        self._write(
            "templates/example-template/README.md",
            """
            # Example Template

            Stable template ID: `example-template`

            Human-facing title:

            > **Example Standard**

            ## Source document

            See [the standard](standard.md).
            """,
        )
        self._write(
            "templates/example-template/standard.md",
            """
            # Example Standard

            ## Scope

            A durable artifact MUST retain reviewable history.
            """,
        )
        self._refresh_structure_snapshot()

    def _refresh_structure_snapshot(self) -> None:
        snapshot = VALIDATE.render_repository_structure(self.root)
        (self.root / VALIDATE.STRUCTURE_SNAPSHOT_PATH).write_text(snapshot, encoding="utf-8")

    def _write_local_requirement_standard(self, body: str) -> None:
        self._write(
            "templates/example-template/standard.md",
            f"# Example Standard\n\n## Requirements\n\n{textwrap.dedent(body).strip()}\n",
        )

    def _add_template(self, template_id: str, title: str, standard_body: str) -> None:
        self._write(
            f"templates/{template_id}/README.md",
            f"""
            # {title} Template

            Stable template ID: `{template_id}`

            Human-facing title:

            > **{title}**
            """,
        )
        self._write(
            f"templates/{template_id}/standard.md",
            f"# {title}\n\n## Requirements\n\n{textwrap.dedent(standard_body).strip()}\n",
        )
        with (self.root / "CATALOG.md").open("a", encoding="utf-8") as handle:
            handle.write(f"\n### `{template_id}`\n\n**{title}**\n")
        self._refresh_structure_snapshot()

    def _findings(self) -> list:
        return VALIDATE.validate_repository(self.root)

    def _messages(self) -> str:
        return "\n".join(str(finding) for finding in self._findings())

    def assertValid(self) -> None:
        findings = self._findings()
        self.assertEqual([], findings, "\n".join(str(finding) for finding in findings))

    def test_known_good_repository_passes(self) -> None:
        self.assertValid()

    def test_repository_path_naming_accepts_owned_and_ordinary_conventions(self) -> None:
        for path in (
            "docs/example-guide.md",
            "assets/example.txt",
            "web-standards-assessment-guidance.md",
            ".github/workflows/validate.yml",
            ".github/pull_request_template.md",
            ".vscode/settings.json",
            ".githooks/pre-commit",
            "scripts/example_tool.py",
            "tests/test_example.py",
        ):
            self._write(path, "# Example\n" if path.endswith(".md") else "example\n")
        for path in (
            "ADOPTION.md",
            "AGENTS.md",
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "CONTRIBUTING.md",
            "MAINTAINING.md",
            "NAMING.md",
            "SECURITY.md",
        ):
            self._write(path, f"# {path}\n")
        self._write("LICENSE", "License\n")
        self._write(".markdownlint-cli2.jsonc", "{}\n")
        self._refresh_structure_snapshot()
        self.assertValid()

    def test_repository_path_naming_rejects_ordinary_invalid_names(self) -> None:
        invalid_paths = (
            "WEB_GUIDANCE.md",
            "web_guidance.md",
            "Project_Docs/example.md",
            "project.docs/example.md",
            "docs/ordinary_file.txt",
            "docs/example guide.md",
            "docs/example--guide.md",
            "docs/-example.md",
            "docs/example-.md",
            "docs/example.MD",
        )
        for path in invalid_paths:
            with self.subTest(path=path):
                self._write(path, "# Invalid\n" if path.endswith(".md") else "invalid\n")
                self._refresh_structure_snapshot()
                messages = self._messages()
                invalid_directory = (
                    path.split("/")[0]
                    if path
                    in (
                        "Project_Docs/example.md",
                        "project.docs/example.md",
                    )
                    else None
                )
                expected_path = invalid_directory or path
                self.assertIn(expected_path, messages)
                self.assertIn(
                    "lowercase ASCII alphanumeric words separated by single hyphens", messages
                )
                target = self.root / path
                target.unlink()
                if invalid_directory:
                    target.parent.rmdir()

    def test_root_exception_does_not_allow_arbitrary_uppercase_markdown(self) -> None:
        self._write("UNLISTED_GUIDANCE.md", "# Unlisted Guidance\n")
        self._refresh_structure_snapshot()
        self.assertIn("UNLISTED_GUIDANCE.md: path component", self._messages())

    def test_root_exception_does_not_apply_below_root(self) -> None:
        self._write("docs/README.md", "# Nested Readme\n")
        self._refresh_structure_snapshot()
        self.assertIn("docs/README.md: path component", self._messages())

    def test_arbitrary_dot_directory_is_not_tool_owned(self) -> None:
        self._write(".custom/settings.json", "{}\n")
        self._refresh_structure_snapshot()
        self.assertIn(".custom: path component", self._messages())

    def test_python_filename_must_use_python_snake_case(self) -> None:
        self._write("scripts/Example_Tool.py", "example = True\n")
        self._refresh_structure_snapshot()
        messages = self._messages()
        self.assertIn("scripts/Example_Tool.py", messages)
        self.assertIn("lowercase ASCII snake_case", messages)

    def test_repository_path_naming_scans_existing_tracked_paths(self) -> None:
        self._write("docs/legacy_Name.md", "# Legacy Name\n")
        self._refresh_structure_snapshot()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        self.assertIn("docs/legacy_Name.md: path component", self._messages())

    def test_template_missing_readme_fails(self) -> None:
        (self.root / "templates/example-template/README.md").unlink()
        self.assertIn("required template file is missing", self._messages())

    def test_matching_stable_template_id_passes(self) -> None:
        self.assertValid()

    def test_missing_stable_template_id_declaration_fails(self) -> None:
        readme = self.root / "templates/example-template/README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace(
                "Stable template ID: `example-template`\n\n", ""
            ),
            encoding="utf-8",
        )
        self.assertIn("exactly one stable template ID declaration", self._messages())

    def test_duplicate_stable_template_id_declarations_fail(self) -> None:
        readme = self.root / "templates/example-template/README.md"
        with readme.open("a", encoding="utf-8") as handle:
            handle.write("\nStable template ID: `example-template`\n")
        messages = self._messages()
        self.assertIn("exactly one stable template ID declaration", messages)
        self.assertIn("found 2", messages)

    def test_mismatched_stable_template_id_reports_actual_and_expected(self) -> None:
        readme = self.root / "templates/example-template/README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace(
                "Stable template ID: `example-template`",
                "Stable template ID: `different-template`",
            ),
            encoding="utf-8",
        )
        messages = self._messages()
        self.assertIn("declares stable template ID 'different-template'", messages)
        self.assertIn("expected directory ID 'example-template'", messages)

    def test_examples_and_mentions_are_not_stable_template_id_declarations(self) -> None:
        readme = self.root / "templates/example-template/README.md"
        with readme.open("a", encoding="utf-8") as handle:
            handle.write(
                "\nAn unrelated mention of `different-template` remains prose.\n\n"
                "```markdown\nStable template ID: `example-template`\n```\n"
            )
        self.assertValid()

    def test_standard_without_local_requirement_scheme_passes(self) -> None:
        self.assertValid()

    def test_unique_matching_local_requirement_definitions_pass(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-001 — First requirement.** The artifact MUST remain reviewable.

            **WEB-TEST-002 — Second requirement.** The artifact MUST remain stable.
            """
        )
        self.assertValid()

    def test_duplicate_local_requirement_id_fails(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — First requirement.** The artifact MUST remain reviewable.

            **WEB-TEST-005 — Repeated requirement.** The artifact MUST remain stable.
            """
        )
        messages = self._messages()
        self.assertIn("duplicate local requirement ID 'WEB-TEST-005'", messages)
        self.assertIn("declared scheme is 'WEB-TEST-NNN'", messages)

    def test_wrong_prefix_local_requirement_definition_fails(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-OTHER-005 — Wrong prefix.** The artifact MUST remain reviewable.
            """
        )
        messages = self._messages()
        self.assertIn("requirement definition label 'WEB-OTHER-005'", messages)
        self.assertIn("declared scheme 'WEB-TEST-NNN'", messages)
        self.assertIn("expected prefix 'WEB-TEST'", messages)

    def test_malformed_same_prefix_requirement_definition_fails(self) -> None:
        for requirement_id in ("WEB-TEST-01", "WEB-TEST-0001", "WEB-TEST-ABC"):
            with self.subTest(requirement_id=requirement_id):
                self._write_local_requirement_standard(
                    f"""
                    `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

                    **{requirement_id} — Malformed ID.** The artifact MUST remain reviewable.
                    """
                )
                messages = self._messages()
                self.assertIn(f"requirement definition label '{requirement_id}'", messages)
                self.assertIn("exactly three decimal digits", messages)

    def test_requirement_mentions_do_not_count_as_definitions(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** The artifact MUST remain reviewable.

            A later reference to `WEB-TEST-005` does not define it again.
            WCAG 1.1.1 remains an external identifier.
            """
        )
        self.assertValid()

    def test_fenced_requirement_examples_do_not_count(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** The artifact MUST remain reviewable.

            ```markdown
            `WEB-OTHER-NNN` identifies a local requirement synthesized by this template.
            **WEB-TEST-005 — Example only.** Example text.
            **WEB-TEST-01 — Malformed example.** Example text.
            ```
            """
        )
        self.assertValid()

    def test_local_requirement_numbering_gaps_and_nonzero_start_pass(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — First declared requirement.** The artifact MUST remain reviewable.

            **WEB-TEST-009 — Later declared requirement.** The artifact MUST remain stable.
            """
        )
        self.assertValid()

    def test_local_requirement_count_is_not_fixed(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-731 — Only requirement.** The artifact MUST remain reviewable.
            """
        )
        self.assertValid()

    def test_multiple_local_requirement_scheme_declarations_fail(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            `WEB-OTHER-NNN` identifies a local requirement synthesized by this template.
            """
        )
        messages = self._messages()
        self.assertIn("declares 2 local requirement ID schemes", messages)
        self.assertIn("expected at most one", messages)

    def test_same_standard_inline_requirement_reference_passes(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** The artifact MUST remain reviewable.

            This conclusion relies on `WEB-TEST-005`.
            """
        )
        self.assertValid()

    def test_cross_standard_inline_requirement_reference_passes(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** Apply `WEB-OTHER-007` where relevant.
            """
        )
        self._add_template(
            "other-template",
            "Other Standard",
            """
            `WEB-OTHER-NNN` identifies a local requirement synthesized by this template.

            **WEB-OTHER-007 — Other requirement.** The artifact MUST remain stable.
            """,
        )
        self.assertValid()

    def test_unresolved_inline_requirement_reference_reports_id_and_source(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** Apply `WEB-TEST-999` where relevant.
            """
        )
        messages = self._messages()
        self.assertIn("templates/example-template/standard.md", messages)
        self.assertIn("unresolved local requirement reference 'WEB-TEST-999'", messages)
        self.assertIn("declared prefix 'WEB-TEST'", messages)

    def test_requirement_scheme_placeholder_is_not_a_reference(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** The artifact MUST remain reviewable.

            The local scheme is `WEB-TEST-NNN`.
            """
        )
        self.assertValid()

    def test_ordinary_requirement_prose_mention_is_not_a_reference(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** WEB-TEST-999 is mentioned as prose.
            """
        )
        self.assertValid()

    def test_fenced_inline_requirement_reference_is_not_checked(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** The artifact MUST remain reviewable.

            ```markdown
            An example cites `WEB-TEST-999`.
            ```
            """
        )
        self.assertValid()

    def test_unknown_prefix_inline_requirement_token_is_not_checked(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** The example cites `WEB-UNKNOWN-001`.
            """
        )
        self.assertValid()

    def test_external_identifier_is_not_a_local_requirement_reference(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — Requirement.** External identifiers include `WCAG 1.1.1`.
            """
        )
        self.assertValid()

    def test_readme_requirement_token_is_out_of_scope(self) -> None:
        readme = self.root / "templates/example-template/README.md"
        with readme.open("a", encoding="utf-8") as handle:
            handle.write("\nAn example cites `WEB-TEST-999`.\n")
        self.assertValid()

    def test_reference_to_duplicate_definition_does_not_resolve(self) -> None:
        self._write_local_requirement_standard(
            """
            `WEB-TEST-NNN` identifies a local requirement synthesized by this template.

            **WEB-TEST-005 — First definition.** The artifact MUST remain reviewable.

            **WEB-TEST-005 — Duplicate definition.** See `WEB-TEST-005`.
            """
        )
        messages = self._messages()
        self.assertIn("duplicate local requirement ID 'WEB-TEST-005'", messages)
        self.assertIn("reference 'WEB-TEST-005' resolves to 2 definitions", messages)

    def test_dangling_relative_link_fails(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Missing](missing.md)\n")
        self.assertIn("local link target does not exist", self._messages())

    def test_missing_reference_style_local_link_fails(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\nSee [missing][target].\n\n[target]: missing.md\n")
        self.assertIn("local link target does not exist", self._messages())

    def test_valid_reference_style_local_link_passes(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\nSee [catalog][catalog-ref].\n\n[catalog-ref]: CATALOG.md\n")
        self.assertValid()

    def test_reference_style_anchor_is_validated(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\nSee [section][section-ref].\n\n[section-ref]: CATALOG.md#absent\n")
        self.assertIn("Markdown anchor does not exist", self._messages())

    def test_fenced_reference_definition_is_not_active(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write(
                "\nSee [catalog][catalog-ref].\n\n```markdown\n[catalog-ref]: CATALOG.md\n```\n"
            )
        self.assertIn("reference-style link definition does not exist", self._messages())

    def test_malformed_reference_definition_fails_cleanly(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[broken]:\n")
        self.assertIn("malformed reference-style link definition", self._messages())

    def test_missing_markdown_anchor_fails(self) -> None:
        self._write("guide.md", "# Guide\n\n## Present\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Absent](guide.md#absent)\n")
        self.assertIn("Markdown anchor does not exist", self._messages())

    def test_markdown_anchor_case_must_match(self) -> None:
        self._write("guide.md", "# Guide\n\n## Some Heading\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Wrong case](guide.md#Some-Heading)\n")
        self._refresh_structure_snapshot()
        self.assertIn("Markdown anchor does not exist", self._messages())

    def test_markdown_anchor_exact_case_passes(self) -> None:
        self._write("guide.md", "# Guide\n\n## Some Heading\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Exact case](guide.md#some-heading)\n")
        self._refresh_structure_snapshot()
        self.assertValid()

    def test_repository_path_case_must_match(self) -> None:
        with (self.root / "CATALOG.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Wrong case](readme.md)\n")
        self.assertIn("local link target does not exist", self._messages())

    def test_balanced_parenthesis_link_destination_passes(self) -> None:
        self._write(".github/file_(one).md", "# Parenthesized File\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Example](.github/file_(one).md)\n")
        self._refresh_structure_snapshot()
        self.assertValid()

    def test_heading_underscore_emphasis_and_literal_underscore_anchors_pass(self) -> None:
        self._write("guide.md", "# Guide\n\n## _Scope_\n\n## value_name\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Scope](guide.md#scope) and [name](guide.md#value_name).\n")
        self._refresh_structure_snapshot()
        self.assertValid()

    def test_duplicate_heading_suffix_anchors_pass(self) -> None:
        self._write("guide.md", "# Guide\n\n## Repeat\n\n## Repeat\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[First](guide.md#repeat) and [second](guide.md#repeat-1).\n")
        self._refresh_structure_snapshot()
        self.assertValid()

    def test_unbalanced_code_fence_fails(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n```text\nnot closed\n")
        self.assertIn("fenced code block is not closed", self._messages())

    def test_invalid_heading_hierarchy_fails(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n### Skipped level\n")
        self.assertIn("heading level skips from H1 to H3", self._messages())

    def test_invalid_template_id_fails(self) -> None:
        invalid_directory = self.root / "templates/Example_template"
        (self.root / "templates/example-template").rename(invalid_directory)
        readme_path = invalid_directory / "README.md"
        readme_path.write_text(
            readme_path.read_text(encoding="utf-8").replace("example-template", "Example_template"),
            encoding="utf-8",
        )
        catalog_path = self.root / "CATALOG.md"
        catalog_path.write_text(
            catalog_path.read_text(encoding="utf-8").replace(
                "example-template", "Example_template"
            ),
            encoding="utf-8",
        )
        self.assertIn("template ID must use lowercase ASCII", self._messages())

    def test_unexpected_template_metadata_fails(self) -> None:
        self._write(f"templates/example-template/{TEMPLATE_METADATA_NAME}", "deprecated: true\n")
        messages = self._messages()
        self.assertIn("template metadata files are not allowed", messages)
        self.assertIn("unexpected entry in template directory", messages)

    def test_malformed_bcp14_keyword_near_misses_fail(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write(
                "\nMUSTT MUS SHOUD SHOULDD SHOULD N0T MAYY REQUIERD RECOMENDED "
                "OPTIONL MUST N0T NOT RECOMENDED SHALL N0T\n"
            )
        messages = self._messages()
        for malformed in (
            "MUSTT",
            "MUS",
            "SHOUD",
            "SHOULDD",
            "SHOULD N0T",
            "MAYY",
            "REQUIERD",
            "RECOMENDED",
            "OPTIONL",
            "MUST N0T",
            "NOT RECOMENDED",
            "SHALL N0T",
        ):
            with self.subTest(malformed=malformed):
                self.assertIn(repr(malformed), messages)

    def test_similar_uppercase_words_are_not_bcp14_near_misses(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\nSHELL MAYO MUSTS MUSTY REQUIRE OPTION\n")
        self.assertValid()

    def test_legitimate_prose_acronyms_identifiers_and_code_are_not_flagged(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write(
                "\nLowercase should, must, and may are ordinary prose.\n"
                "API CI RFC HTTP are unrelated acronyms.\n"
                "MUST MUST NOT SHOULD SHOULD NOT MAY SHALL SHALL NOT REQUIRED "
                "RECOMMENDED NOT RECOMMENDED OPTIONAL are canonical forms.\n"
                "`MUST_RETRY_FLAG` and `SHOUD` are inline code.\n\n"
                "```text\nMUSTT\nSHOULD N0T\n### Not a heading\n```\n"
            )
        self.assertValid()

    def test_missing_catalog_membership_fails(self) -> None:
        self._write("CATALOG.md", "# Template Catalog\n\n## Templates\n")
        self.assertIn("is missing from the catalog", self._messages())

    def test_fenced_catalog_entry_does_not_count(self) -> None:
        self._write(
            "CATALOG.md",
            "# Template Catalog\n\n## Templates\n\n```markdown\n### `example-template`\n\n**Example Standard**\n```\n",
        )
        self.assertIn("is missing from the catalog", self._messages())

    def test_fenced_catalog_title_does_not_count(self) -> None:
        self._write(
            "CATALOG.md",
            "# Template Catalog\n\n## Templates\n\n### `example-template`\n\n```markdown\n**Example Standard**\n```\n",
        )
        self.assertIn("is missing its human-facing title", self._messages())

    def test_fenced_readme_title_does_not_count(self) -> None:
        self._write(
            "templates/example-template/README.md",
            "# Example Template\n\nStable template ID: `example-template`\n\n```markdown\n"
            "Human-facing title:\n\n> **Example Standard**\n```\n",
        )
        self.assertIn("cannot find the human-facing title", self._messages())

    def test_catalog_entry_without_directory_fails(self) -> None:
        with (self.root / "CATALOG.md").open("a", encoding="utf-8") as handle:
            handle.write("\n### `missing-template`\n\n**Missing Standard**\n")
        self.assertIn("has no template directory", self._messages())

    def test_title_mismatch_fails(self) -> None:
        catalog_path = self.root / "CATALOG.md"
        catalog_path.write_text(
            catalog_path.read_text(encoding="utf-8").replace(
                "Example Standard", "Different Standard"
            ),
            encoding="utf-8",
        )
        self.assertIn("human-facing template titles do not agree", self._messages())

    def test_invalid_utf8_text_fails(self) -> None:
        path = self.root / "notes.txt"
        path.write_bytes(b"\xff\n")
        self.assertIn("text file is not valid UTF-8", self._messages())

    def test_missing_tracked_file_produces_finding(self) -> None:
        self._write("tracked-note.txt", "tracked\n")
        self._refresh_structure_snapshot()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        (self.root / "tracked-note.txt").unlink()
        self.assertIn("tracked-note.txt: repository file could not be read", self._messages())

    def test_external_symlink_is_rejected_without_reading_target(self) -> None:
        with tempfile.TemporaryDirectory() as external_directory:
            external_target = Path(external_directory) / "external.md"
            external_target.write_bytes(b"\xff\n")
            (self.root / "external.md").symlink_to(external_target)
            self._refresh_structure_snapshot()
            messages = self._messages()
        self.assertIn("symbolic links are not allowed; the link target was not read", messages)
        self.assertNotIn("not valid UTF-8", messages)

    def test_internal_symlink_is_rejected(self) -> None:
        (self.root / "catalog-link.md").symlink_to(self.root / "CATALOG.md")
        self._refresh_structure_snapshot()
        self.assertIn(
            "symbolic links are not allowed; the link target was not read", self._messages()
        )

    def test_missing_final_newline_fails(self) -> None:
        (self.root / "notes.txt").write_text("missing newline", encoding="utf-8")
        self.assertIn("text file must end with a newline", self._messages())

    def test_stale_repository_structure_snapshot_fails(self) -> None:
        self._write("new-file.txt", "new structure\n")
        messages = self._messages()
        self.assertIn("repository structure differs from the committed snapshot", messages)
        self.assertIn("python3 scripts/update_repository_structure.py", messages)
        self.assertIn("restore the unexpected paths", messages)

    def test_junk_artifact_fails(self) -> None:
        (self.root / ".DS_Store").write_bytes(b"junk")
        self.assertIn("junk artifact file is not allowed", self._messages())

    def test_bytecode_cache_artifact_fails(self) -> None:
        cache_directory = self.root / "__pycache__"
        cache_directory.mkdir()
        (cache_directory / "module.pyc").write_bytes(b"junk")
        self.assertIn("junk artifact directory is not allowed", self._messages())


class GitHookSetupTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        hook = self.root / ".githooks" / "pre-commit"
        hook.parent.mkdir()
        hook.write_text("#!/bin/sh\n", encoding="utf-8")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _hooks_path(self) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.root), "config", "--local", "--get", "core.hooksPath"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def test_unset_hooks_path_is_configured(self) -> None:
        HOOK_SETUP.configure_hooks(self.root)
        self.assertEqual(".githooks", self._hooks_path())

    def test_existing_repository_hooks_path_is_idempotent(self) -> None:
        subprocess.run(
            ["git", "-C", str(self.root), "config", "--local", "core.hooksPath", ".githooks"],
            check=True,
        )
        HOOK_SETUP.configure_hooks(self.root)
        self.assertEqual(".githooks", self._hooks_path())

    def test_conflicting_hooks_path_is_preserved_and_refused(self) -> None:
        subprocess.run(
            ["git", "-C", str(self.root), "config", "--local", "core.hooksPath", "custom-hooks"],
            check=True,
        )
        with self.assertRaisesRegex(RuntimeError, "--force"):
            HOOK_SETUP.configure_hooks(self.root)
        self.assertEqual("custom-hooks", self._hooks_path())

    def test_force_replaces_conflicting_hooks_path(self) -> None:
        subprocess.run(
            ["git", "-C", str(self.root), "config", "--local", "core.hooksPath", "custom-hooks"],
            check=True,
        )
        HOOK_SETUP.configure_hooks(self.root, force=True)
        self.assertEqual(".githooks", self._hooks_path())


if __name__ == "__main__":
    unittest.main()

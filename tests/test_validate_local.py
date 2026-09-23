"""Unit tests for the standards-domain checks in scripts/validate_local.py.

The released generic suites run separately. This module covers domain semantics
and their independent command boundary.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_local import (  # noqa: E402
    damerau_levenshtein,
    is_single_near_miss,
    markdown_without_fenced_code,
    scan_headings,
    scan_inline_code_spans,
    validate_repository,
)

TEMPLATE_README = """# {title}

Human-facing title:

> **{title}**

Stable template ID: `{template_id}`

Template edition: `1.0`
"""

CATALOG = """# Template Catalog

## Templates

### Group

#### `{template_id}`

**{title}**
"""


class StandardsTestCase(unittest.TestCase):
    """Build a throwaway standards repository and run the validator over it."""

    def build(self, templates, catalog=None, extra=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)

        for template_id, files in templates.items():
            template_root = root / "templates" / template_id
            template_root.mkdir(parents=True, exist_ok=True)
            for name, content in files.items():
                (template_root / name).write_text(content, encoding="utf-8")

        if catalog is not None:
            (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        for relative_path, content in (extra or {}).items():
            path = root / relative_path
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        subprocess.run(["git", "init", "-q", str(root)], check=True)
        return root

    def local_reasons(self, root):
        return [reason for _, _, reason in validate_repository(root)]

    def simple(self, template_id="example-template", title="Example Standard", standard=None):
        return {
            template_id: {
                "README.md": TEMPLATE_README.format(template_id=template_id, title=title),
                "standard.md": standard if standard is not None else f"# {title}\n",
            }
        }


class TemplateStructureTests(StandardsTestCase):
    def test_well_formed_template_passes(self):
        root = self.build(
            self.simple(),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))

    def test_missing_standard_file_fails(self):
        templates = self.simple()
        del templates["example-template"]["standard.md"]
        root = self.build(
            templates,
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertIn("required template file is missing", self.local_reasons(root))

    def test_unexpected_entry_in_template_directory_fails(self):
        templates = self.simple()
        templates["example-template"]["notes.md"] = "# Notes\n"
        root = self.build(
            templates,
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertIn("unexpected entry in template directory", self.local_reasons(root))

    def test_invalid_template_id_fails(self):
        root = self.build(
            self.simple(template_id="Bad_Id"),
            catalog=CATALOG.format(template_id="Bad_Id", title="Example Standard"),
        )
        self.assertIn(
            "template ID must use lowercase ASCII alphanumerics separated by single hyphens",
            self.local_reasons(root),
        )

    def test_missing_templates_directory_fails(self):
        root = self.build({}, catalog="# Template Catalog\n\n## Templates\n")
        self.assertIn("templates directory is missing", self.local_reasons(root))


class StableTemplateIdTests(StandardsTestCase):
    def test_missing_declaration_fails(self):
        templates = self.simple()
        templates["example-template"]["README.md"] = "# Example Standard\n"
        root = self.build(
            templates,
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(
            any("exactly one stable template ID" in reason for reason in self.local_reasons(root))
        )

    def test_mismatched_declaration_reports_both_ids(self):
        templates = self.simple()
        templates["example-template"]["README.md"] = TEMPLATE_README.format(
            template_id="other-template", title="Example Standard"
        )
        root = self.build(
            templates,
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertIn(
            "declares stable template ID 'other-template'; "
            "expected directory ID 'example-template'",
            self.local_reasons(root),
        )

    def test_fenced_declaration_does_not_count(self):
        templates = self.simple()
        templates["example-template"]["README.md"] = (
            "# Example Standard\n\nHuman-facing title:\n\n> **Example Standard**\n\n"
            "```\nStable template ID: `example-template`\n```\n"
        )
        root = self.build(
            templates,
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(any("found 0" in reason for reason in self.local_reasons(root)))


class RequirementIdTests(StandardsTestCase):
    SCHEME = (
        "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
        "**EX-001 — First requirement.**\n\n"
    )

    def standard_with(self, body):
        return f"# Example Standard\n\n{body}"

    def test_matching_requirement_definition_passes(self):
        root = self.build(
            self.simple(standard=self.standard_with(self.SCHEME)),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))

    def test_wrong_prefix_definition_fails(self):
        body = (
            "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
            "**ZZ-001 — Wrong prefix.**\n\n"
        )
        root = self.build(
            self.simple(standard=self.standard_with(body)),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(
            any("does not match declared scheme" in reason for reason in self.local_reasons(root))
        )

    def test_duplicate_requirement_id_fails(self):
        body = self.SCHEME + "**EX-001 — Duplicated.**\n\n"
        root = self.build(
            self.simple(standard=self.standard_with(body)),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(
            any("duplicate local requirement ID" in reason for reason in self.local_reasons(root))
        )

    def test_multiple_scheme_declarations_fail(self):
        body = (
            "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
            "`ZZ-NNN` identifies a local requirement synthesized by this template.\n\n"
        )
        root = self.build(
            self.simple(standard=self.standard_with(body)),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(
            any("local requirement ID schemes" in reason for reason in self.local_reasons(root))
        )

    def test_standard_without_scheme_passes(self):
        root = self.build(
            self.simple(standard="# Example Standard\n\nOrdinary prose.\n"),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))


class RequirementReferenceTests(StandardsTestCase):
    def test_resolved_reference_passes(self):
        body = (
            "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
            "**EX-001 — First requirement.**\n\nSee `EX-001` above.\n"
        )
        root = self.build(
            self.simple(standard=f"# Example Standard\n\n{body}"),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))

    def test_unresolved_reference_fails(self):
        body = (
            "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
            "**EX-001 — First requirement.**\n\nSee `EX-404` above.\n"
        )
        root = self.build(
            self.simple(standard=f"# Example Standard\n\n{body}"),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(
            any(
                "unresolved local requirement reference 'EX-404'" in reason
                for reason in self.local_reasons(root)
            )
        )

    def test_unknown_prefix_token_is_not_checked(self):
        body = (
            "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
            "**EX-001 — First requirement.**\n\nSee `ZZ-404` which is external.\n"
        )
        root = self.build(
            self.simple(standard=f"# Example Standard\n\n{body}"),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))

    def test_prose_mention_without_code_span_is_not_a_reference(self):
        body = (
            "`EX-NNN` identifies a local requirement synthesized by this template.\n\n"
            "**EX-001 — First requirement.**\n\nSee EX-404 in prose.\n"
        )
        root = self.build(
            self.simple(standard=f"# Example Standard\n\n{body}"),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))


class CatalogTests(StandardsTestCase):
    def test_missing_catalog_fails(self):
        root = self.build(self.simple())
        self.assertIn("catalog is missing or unreadable", self.local_reasons(root))

    def test_missing_templates_section_fails(self):
        root = self.build(self.simple(), catalog="# Template Catalog\n\n## Other\n")
        self.assertIn("catalog is missing the Templates section", self.local_reasons(root))

    def test_template_missing_from_catalog_fails(self):
        root = self.build(self.simple(), catalog="# Template Catalog\n\n## Templates\n")
        self.assertIn(
            "template directory 'example-template' is missing from the catalog",
            self.local_reasons(root),
        )

    def test_catalog_entry_without_directory_fails(self):
        root = self.build(
            self.simple(),
            catalog=(
                CATALOG.format(template_id="example-template", title="Example Standard")
                + "\n#### `ghost-template`\n\n**Ghost Standard**\n"
            ),
        )
        self.assertIn(
            "catalog entry 'ghost-template' has no template directory", self.local_reasons(root)
        )

    def test_duplicate_catalog_entry_fails(self):
        root = self.build(
            self.simple(),
            catalog=(
                CATALOG.format(template_id="example-template", title="Example Standard")
                + "\n#### `example-template`\n\n**Example Standard**\n"
            ),
        )
        self.assertIn(
            "template 'example-template' appears 2 times in the catalog", self.local_reasons(root)
        )

    def test_catalog_entry_missing_title_fails(self):
        root = self.build(
            self.simple(),
            catalog="# Template Catalog\n\n## Templates\n\n### Group\n\n#### `example-template`\n",
        )
        self.assertIn(
            "catalog entry 'example-template' is missing its human-facing title",
            self.local_reasons(root),
        )

    def test_entry_outside_templates_section_does_not_count(self):
        root = self.build(
            self.simple(),
            catalog=(
                CATALOG.format(template_id="example-template", title="Example Standard")
                + "\n## Appendix\n\n#### `ghost-template`\n\n**Ghost**\n"
            ),
        )
        reasons = self.local_reasons(root)
        self.assertNotIn("catalog entry 'ghost-template' has no template directory", reasons)


class TemplateTitleTests(StandardsTestCase):
    def test_agreeing_titles_pass(self):
        root = self.build(
            self.simple(),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertEqual([], self.local_reasons(root))

    def test_disagreeing_titles_fail(self):
        root = self.build(
            self.simple(standard="# Different Standard\n"),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertTrue(
            any(
                "human-facing template titles do not agree" in reason
                for reason in self.local_reasons(root)
            )
        )

    def test_missing_readme_title_convention_fails(self):
        templates = self.simple()
        templates["example-template"]["README.md"] = (
            "# Example Standard\n\nStable template ID: `example-template`\n"
        )
        root = self.build(
            templates,
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )
        self.assertIn(
            "cannot find the human-facing title using the repository convention",
            self.local_reasons(root),
        )


class Bcp14Tests(StandardsTestCase):
    def near_miss_repo(self, prose):
        return self.build(
            self.simple(),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
            extra={"notes.md": f"# Notes\n\n{prose}\n"},
        )

    def test_misspelled_keyword_fails(self):
        root = self.near_miss_repo("The system MUSTT do this.")
        self.assertTrue(any("MUSTT" in reason for reason in self.local_reasons(root)))

    def test_misspelled_phrase_fails(self):
        root = self.near_miss_repo("The system MUST NOTT do this.")
        self.assertTrue(any("NOT" in reason for reason in self.local_reasons(root)))

    def test_correct_keywords_pass(self):
        root = self.near_miss_repo("The system MUST do this and SHOULD NOT do that.")
        self.assertEqual([], self.local_reasons(root))

    def test_unrelated_acronym_passes(self):
        root = self.near_miss_repo("The HTTP and JSON payloads are fine.")
        self.assertEqual([], self.local_reasons(root))

    def test_fenced_keyword_is_not_checked(self):
        root = self.build(
            self.simple(),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
            extra={"notes.md": "# Notes\n\n```\nMUSTT\n```\n"},
        )
        self.assertEqual([], self.local_reasons(root))


class HelperTests(unittest.TestCase):
    def test_damerau_levenshtein_counts_transposition_as_one(self):
        self.assertEqual(1, damerau_levenshtein("MSUT", "MUST"))

    def test_single_near_miss_detects_doubled_final_character(self):
        self.assertTrue(is_single_near_miss("MUSTT", "MUST"))

    def test_single_near_miss_rejects_unrelated_word(self):
        self.assertFalse(is_single_near_miss("JSON", "MUST"))

    def test_scan_inline_code_spans_returns_span_contents(self):
        self.assertEqual(["EX-001"], scan_inline_code_spans("See `EX-001` here."))

    def test_scan_headings_ignores_fenced_headings(self):
        headings = scan_headings("# Real\n\n```\n## Fenced\n```\n\n## Also Real\n")
        self.assertEqual([(1, "Real"), (2, "Also Real")], [(h.level, h.text) for h in headings])


class IndependentCommandTests(StandardsTestCase):
    def valid_root(self):
        return self.build(
            self.simple(),
            catalog=CATALOG.format(template_id="example-template", title="Example Standard"),
        )

    def command(self, root):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_local.py"), "--root", str(root)],
            capture_output=True,
            text=True,
        )

    def test_direct_cli_success_and_domain_failure(self):
        root = self.valid_root()
        self.assertEqual(0, self.command(root).returncode)
        (root / "templates/example-template/standard.md").unlink()
        result = self.command(root)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("required template file is missing", result.stderr)

    def test_invalid_utf8_fails_closed(self):
        root = self.valid_root()
        (root / "notes.md").write_bytes(b"\xff")
        self.assertNotEqual(0, self.command(root).returncode)

    def test_missing_tracked_input_fails_closed(self):
        root = self.valid_root()
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        (root / "CATALOG.md").unlink()
        result = self.command(root)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("could not complete", result.stderr)

    def test_missing_git_repository_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertNotEqual(0, self.command(Path(directory)).returncode)

    def test_symlink_and_symlink_ancestor_fail_closed(self):
        root = self.valid_root()
        (root / "notes.md").symlink_to("CATALOG.md")
        self.assertIn("symbolic link", self.command(root).stderr)
        (root / "notes.md").unlink()
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        template = root / "templates/example-template"
        template.rename(root / "moved-template")
        template.symlink_to(root / "moved-template", target_is_directory=True)
        self.assertIn("symbolic link", self.command(root).stderr)

    def test_ignored_markdown_is_not_domain_input(self):
        root = self.valid_root()
        (root / ".gitignore").write_text("ignored.md\n", encoding="utf-8")
        (root / "ignored.md").write_bytes(b"\xff")
        self.assertEqual(0, self.command(root).returncode)

    def test_fence_mask_preserves_lines_and_nested_delimiters(self):
        content = "before\n````md\n```\nMUSTT\n```\n````\nafter\n"
        self.assertEqual("before\n\n\n\n\n\nafter\n", markdown_without_fenced_code(content))
        self.assertEqual("before\n\n\n", markdown_without_fenced_code("before\n~~~\nMUSTT\n"))


if __name__ == "__main__":
    unittest.main()

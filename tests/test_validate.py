from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import textwrap
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPOSITORY_ROOT / "scripts" / "validate.py"
SPEC = importlib.util.spec_from_file_location("repository_validate", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load repository validator")
VALIDATE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATE
SPEC.loader.exec_module(VALIDATE)

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

    def _findings(self) -> list:
        return VALIDATE.validate_repository(self.root)

    def _messages(self) -> str:
        return "\n".join(str(finding) for finding in self._findings())

    def assertValid(self) -> None:
        findings = self._findings()
        self.assertEqual([], findings, "\n".join(str(finding) for finding in findings))

    def test_known_good_repository_passes(self) -> None:
        self.assertValid()

    def test_template_missing_readme_fails(self) -> None:
        (self.root / "templates/example-template/README.md").unlink()
        self.assertIn("required template file is missing", self._messages())

    def test_dangling_relative_link_fails(self) -> None:
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Missing](missing.md)\n")
        self.assertIn("local link target does not exist", self._messages())

    def test_missing_markdown_anchor_fails(self) -> None:
        self._write("guide.md", "# Guide\n\n## Present\n")
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Absent](guide.md#absent)\n")
        self.assertIn("Markdown anchor does not exist", self._messages())

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
        catalog_path = self.root / "CATALOG.md"
        catalog_path.write_text(
            catalog_path.read_text(encoding="utf-8").replace("example-template", "Example_template"),
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
            handle.write("\nMUSTT SHOUD SHOULD N0T REQUIERD RECOMENDED\n")
        messages = self._messages()
        for malformed in ("MUSTT", "SHOUD", "SHOULD N0T", "REQUIERD", "RECOMENDED"):
            with self.subTest(malformed=malformed):
                self.assertIn(repr(malformed), messages)

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

    def test_catalog_entry_without_directory_fails(self) -> None:
        with (self.root / "CATALOG.md").open("a", encoding="utf-8") as handle:
            handle.write("\n### `missing-template`\n\n**Missing Standard**\n")
        self.assertIn("has no template directory", self._messages())

    def test_title_mismatch_fails(self) -> None:
        catalog_path = self.root / "CATALOG.md"
        catalog_path.write_text(
            catalog_path.read_text(encoding="utf-8").replace("Example Standard", "Different Standard"),
            encoding="utf-8",
        )
        self.assertIn("human-facing template titles do not agree", self._messages())

    def test_invalid_utf8_text_fails(self) -> None:
        path = self.root / "notes.txt"
        path.write_bytes(b"\xff\n")
        self.assertIn("text file is not valid UTF-8", self._messages())

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


if __name__ == "__main__":
    unittest.main()

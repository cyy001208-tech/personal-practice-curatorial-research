from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "inventory_project_archive.py"


class InventoryPrivacyTests(unittest.TestCase):
    def run_inventory(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_default_json_uses_logical_root_labels(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "project.md").write_text("evidence", encoding="utf-8")

            result = self.run_inventory(str(root), "--format", "json")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn(str(root), result.stdout)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["authorized_roots"], ["root-01"])
            self.assertEqual(payload["records"][0]["root"], "root-01")

    def test_absolute_roots_require_explicit_opt_in(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "project.md").write_text("evidence", encoding="utf-8")

            result = self.run_inventory(
                str(root),
                "--format",
                "json",
                "--include-absolute-roots",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["authorized_roots"], [str(root)])
            self.assertEqual(payload["records"][0]["root"], str(root))

    def test_default_root_error_does_not_echo_private_input(self) -> None:
        missing = "/private/client-project/does-not-exist"

        result = self.run_inventory(missing, "--format", "json")

        self.assertEqual(result.returncode, 1)
        self.assertNotIn(missing, result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["authorized_roots"], ["root-01"])
        self.assertIn("root-01", payload["root_errors"][0])


if __name__ == "__main__":
    unittest.main()

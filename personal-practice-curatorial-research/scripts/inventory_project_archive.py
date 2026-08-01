#!/usr/bin/env python3
"""Create a metadata-only inventory of an authorized project archive."""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".cache",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "backup",
    "backups",
    "build",
    "dist",
    "node_modules",
    "temp",
    "tmp",
    "vendor",
    "venv",
}

SECRET_NAMES = {
    ".env",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "credentials",
    "credentials.json",
    "id_dsa",
    "id_ed25519",
    "id_rsa",
    "secrets.json",
}

SECRET_SUFFIXES = {".jks", ".kdbx", ".p12", ".pfx", ".pem"}

MEDIUM_BY_SUFFIX = {
    ".bib": "bibliography",
    ".csv": "table",
    ".docx": "document",
    ".htm": "web-text",
    ".html": "web-text",
    ".ipynb": "notebook",
    ".jpeg": "image",
    ".jpg": "image",
    ".json": "structured-text",
    ".jsonl": "structured-text",
    ".md": "text",
    ".mov": "video",
    ".mp3": "audio",
    ".mp4": "video",
    ".odp": "presentation",
    ".ods": "spreadsheet",
    ".odt": "document",
    ".pdf": "pdf",
    ".png": "image",
    ".pptx": "presentation",
    ".rst": "text",
    ".svg": "vector-image",
    ".tex": "text",
    ".tif": "image",
    ".tiff": "image",
    ".toml": "structured-text",
    ".tsv": "table",
    ".txt": "text",
    ".wav": "audio",
    ".webp": "image",
    ".xlsx": "spreadsheet",
    ".xml": "structured-text",
    ".yaml": "structured-text",
    ".yml": "structured-text",
}

CODE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".java",
    ".js",
    ".jsx",
    ".m",
    ".mm",
    ".php",
    ".py",
    ".r",
    ".rb",
    ".rs",
    ".scss",
    ".sh",
    ".sql",
    ".swift",
    ".ts",
    ".tsx",
}

CONVERSION_SUFFIXES = {
    ".doc",
    ".key",
    ".kth",
    ".numbers",
    ".pages",
    ".ppt",
    ".xls",
}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Inventory project files without extracting their contents. Hidden files, "
            "likely secrets, symlinks, backup folders, caches, and build products are "
            "excluded by default."
        )
    )
    parser.add_argument("roots", nargs="+", help="Authorized files or directories.")
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "csv"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument("--output", help="Optional destination; stdout is the default.")
    parser.add_argument(
        "--max-size-mb",
        type=float,
        default=250.0,
        help="Mark larger files for manual review (default: 250 MB).",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden non-secret files and directories.",
    )
    parser.add_argument(
        "--include-unsupported",
        action="store_true",
        help="List files without an assigned local reader.",
    )
    parser.add_argument(
        "--include-absolute-roots",
        action="store_true",
        help=(
            "Include resolved absolute root paths in the output. Off by default "
            "because inventories may later enter public editorial packages."
        ),
    )
    return parser.parse_args()


def hidden(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts)


def classify(path: Path, size: int, max_size: int) -> tuple[str, str, str]:
    name = path.name.lower()
    suffix = path.suffix.lower()
    if name in SECRET_NAMES or suffix in SECRET_SUFFIXES:
        return "excluded", "likely-secret", "Do not ingest by default"
    if suffix in CONVERSION_SUFFIXES:
        return "manual-review", "conversion-needed", "Convert or inspect locally"
    if size > max_size:
        return "manual-review", "oversized", "Review before content extraction"
    if suffix in MEDIUM_BY_SUFFIX:
        return "candidate", MEDIUM_BY_SUFFIX[suffix], "Use the appropriate local reader"
    if suffix in CODE_SUFFIXES:
        return "candidate", "source-code", "Read as text when relevant"
    return "unsupported", "unknown", "No reader assigned"


def group_for(relative: Path) -> str:
    return relative.parts[0] if len(relative.parts) > 1 else "(root)"


def inspect_file(
    root: Path,
    path: Path,
    max_size: int,
    include_hidden: bool,
    root_label: str,
) -> dict[str, Any] | None:
    try:
        relative = path.relative_to(root)
    except ValueError:
        return None
    if path.is_symlink():
        return {
            "project_group": group_for(relative),
            "relative_path": str(relative),
            "status": "excluded",
            "medium": "symlink",
            "size_bytes": None,
            "modified_utc": None,
            "note": "Symlinks are not followed",
            "root": root_label,
        }
    if not include_hidden and hidden(relative):
        return None
    try:
        stat = path.stat()
    except OSError as exc:
        return {
            "project_group": group_for(relative),
            "relative_path": str(relative),
            "status": "unreadable",
            "medium": "unknown",
            "size_bytes": None,
            "modified_utc": None,
            "note": str(exc),
            "root": root_label,
        }
    status, medium, note = classify(path, stat.st_size, max_size)
    return {
        "project_group": group_for(relative),
        "relative_path": str(relative),
        "status": status,
        "medium": medium,
        "size_bytes": stat.st_size,
        "modified_utc": datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat(),
        "note": note,
        "root": root_label,
    }


def collect(
    args: argparse.Namespace,
) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    displayed_roots: list[str] = []
    max_size = int(args.max_size_mb * 1024 * 1024)

    for root_index, raw_root in enumerate(args.roots, start=1):
        logical_root = f"root-{root_index:02d}"
        try:
            selected = Path(raw_root).expanduser().resolve(strict=True)
        except OSError as exc:
            displayed_root = str(raw_root) if args.include_absolute_roots else logical_root
            displayed_roots.append(displayed_root)
            detail = str(exc) if args.include_absolute_roots else exc.__class__.__name__
            errors.append(f"{displayed_root}: could not resolve authorized root ({detail})")
            continue
        displayed_root = (
            str(selected) if args.include_absolute_roots else logical_root
        )
        displayed_roots.append(displayed_root)

        if selected.is_file():
            root = selected.parent
            row = inspect_file(
                root,
                selected,
                max_size,
                args.include_hidden,
                displayed_root,
            )
            if row and (args.include_unsupported or row["status"] != "unsupported"):
                row["project_group"] = "(single-file)"
                rows.append(row)
            continue

        root = selected
        for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
            current = Path(dirpath)
            retained: list[str] = []
            for dirname in dirnames:
                candidate = current / dirname
                relative = candidate.relative_to(root)
                if candidate.is_symlink():
                    continue
                if dirname.lower() in IGNORE_DIRS:
                    continue
                if not args.include_hidden and hidden(relative):
                    continue
                retained.append(dirname)
            dirnames[:] = retained

            for filename in filenames:
                row = inspect_file(
                    root,
                    current / filename,
                    max_size,
                    args.include_hidden,
                    displayed_root,
                )
                if row is None:
                    continue
                if not args.include_unsupported and row["status"] == "unsupported":
                    continue
                rows.append(row)

    rows.sort(
        key=lambda row: (
            row["root"],
            row["project_group"].lower(),
            row["relative_path"].lower(),
        )
    )
    for index, row in enumerate(rows, start=1):
        row["file_id"] = f"F{index:04d}"
    return rows, errors, displayed_roots


def render_markdown(
    rows: list[dict[str, Any]], errors: list[str], roots: list[str]
) -> str:
    counts = Counter(row["status"] for row in rows)
    groups = len({(row["root"], row["project_group"]) for row in rows})
    lines = [
        "# Project Archive Inventory",
        "",
        f"- Generated: {datetime.now(tz=timezone.utc).isoformat()}",
        f"- Authorized roots: {', '.join(roots)}",
        f"- Project groups: {groups}",
        f"- Candidate files: {counts.get('candidate', 0)}",
        f"- Manual review: {counts.get('manual-review', 0)}",
        f"- Excluded or unreadable: {counts.get('excluded', 0) + counts.get('unreadable', 0)}",
        f"- Unsupported listed: {counts.get('unsupported', 0)}",
        "",
    ]
    if errors:
        lines.extend(["## Root errors", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    lines.extend(
        [
            "## Files",
            "",
            "| ID | Group | Relative path | Status | Medium | Size bytes | Modified UTC | Note |",
            "|---|---|---|---|---|---:|---|---|",
        ]
    )
    for row in rows:
        cells = [
            row["file_id"],
            row["project_group"],
            row["relative_path"],
            row["status"],
            row["medium"],
            "" if row["size_bytes"] is None else str(row["size_bytes"]),
            row["modified_utc"] or "",
            row["note"],
        ]
        escaped = [str(cell).replace("|", "\\|").replace("\n", " ") for cell in cells]
        lines.append("| " + " | ".join(escaped) + " |")
    lines.append("")
    return "\n".join(lines)


def render_csv(rows: list[dict[str, Any]]) -> str:
    columns = [
        "file_id",
        "project_group",
        "relative_path",
        "status",
        "medium",
        "size_bytes",
        "modified_utc",
        "note",
        "root",
    ]
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns)
    writer.writeheader()
    writer.writerows({column: row.get(column) for column in columns} for row in rows)
    return buffer.getvalue()


def render(
    rows: list[dict[str, Any]],
    errors: list[str],
    args: argparse.Namespace,
    displayed_roots: list[str],
) -> str:
    if args.format == "json":
        return (
            json.dumps(
                {
                    "generated_utc": datetime.now(tz=timezone.utc).isoformat(),
                    "authorized_roots": displayed_roots,
                    "records": rows,
                    "root_errors": errors,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n"
        )
    if args.format == "csv":
        return render_csv(rows)
    return render_markdown(rows, errors, displayed_roots)


def main() -> int:
    args = arguments()
    if args.max_size_mb <= 0:
        print("--max-size-mb must be greater than zero", file=sys.stderr)
        return 2
    rows, errors, displayed_roots = collect(args)
    output = render(rows, errors, args, displayed_roots)
    if args.output:
        destination = Path(args.output).expanduser()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 1 if errors and not rows else 0


if __name__ == "__main__":
    raise SystemExit(main())

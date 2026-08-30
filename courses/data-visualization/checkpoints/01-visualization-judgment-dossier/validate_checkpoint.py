#!/usr/bin/env python3
"""Validate the DA-730 Checkpoint 1 folder contract."""

from __future__ import annotations

import argparse
import binascii
import re
import struct
import tempfile
import zlib
from pathlib import Path


FIGURES = ("comparison", "distribution", "rate", "uncertainty")
ANALYSIS_EXTENSIONS = (".R", ".py", ".ipynb", ".twb", ".pbix")
MARKDOWN_HEADINGS = {
    "README.md": (
        "# Checkpoint 1: visualization judgment dossier",
        "## Audience and decision",
        "## Findings",
        "## Reproduce this dossier",
        "## Folder map",
    ),
    "selection-matrix.md": (
        "# Selection matrix",
        "| Figure | Decision | Reader task | Data structure | Display chosen | Alternative rejected | What could be hidden |",
    ),
    "critique-and-repair.md": (
        "# Critique and repair",
        "## Original problem",
        "## Evidence from Modules 01 through 06",
        "## Repair",
        "## Remaining limit",
    ),
    "accessibility-check.md": (
        "# Accessibility check",
        "## Color and contrast",
        "## Redundant cues",
        "## Text alternatives",
        "## Reading order and labels",
        "## Checks completed",
    ),
    "decision-brief.md": (
        "# Decision brief",
        "## Audience",
        "## Finding",
        "## Decision",
        "## Uncertainty",
        "## Material limitation",
    ),
    "ai-use.md": (
        "# AI-use record",
        "## Tool and model",
        "## Work delegated",
        "## Prompts or instructions",
        "## Verification",
        "## Human decisions",
    ),
}
SOURCE_KEYS = (
    "publisher",
    "landing_page",
    "retrieved_at",
    "released",
    "data_path",
    "analysis_path",
    "figure_path",
    "sha256",
    "transformations",
    "known_limits",
)
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD)\b|\[[^\]\r\n]+\](?!\()", re.IGNORECASE)
CODE_PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|REPLACE_ME)\b", re.IGNORECASE)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("not a PNG")
    return struct.unpack(">II", data[16:24])


def source_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^([a-z][a-z0-9_]*)\s*:\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")
    return fields


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"Checkpoint folder not found: {root}"]

    for relative, required in MARKDOWN_HEADINGS.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing {relative}.")
            continue
        text = read_text(path)
        if len(text.strip()) < 120:
            errors.append(f"{relative} is too short to meet its contract.")
        for item in required:
            if item not in text:
                errors.append(f"{relative} is missing required content: {item}")
        if PLACEHOLDER.search(text):
            errors.append(f"{relative} still contains an unfinished placeholder.")

    matrix_path = root / "selection-matrix.md"
    if matrix_path.is_file():
        matrix = read_text(matrix_path)
        for name in FIGURES:
            if f"`{name}.png`" not in matrix:
                errors.append(f"selection-matrix.md is missing `{name}.png`.")

    accessibility_path = root / "accessibility-check.md"
    if accessibility_path.is_file():
        accessibility = read_text(accessibility_path)
        for name in FIGURES:
            if f"`{name}.png`" not in accessibility:
                errors.append(f"accessibility-check.md is missing `{name}.png`.")

    brief_path = root / "decision-brief.md"
    if brief_path.is_file():
        brief_words = re.findall(r"\b[\w'-]+\b", read_text(brief_path))
        if not 500 <= len(brief_words) <= 900:
            errors.append(f"decision-brief.md must contain 500 to 900 words; found {len(brief_words)}.")

    landing_pages: set[str] = set()
    for name in FIGURES:
        figure = root / "figures" / f"{name}.png"
        if not figure.is_file():
            errors.append(f"Missing figures/{name}.png.")
        else:
            try:
                width, height = png_dimensions(figure)
                if width < 600 or height < 400:
                    errors.append(f"figures/{name}.png is {width}x{height}; minimum is 600x400.")
                if figure.stat().st_size < 1024:
                    errors.append(f"figures/{name}.png is too small to be a completed display.")
            except ValueError:
                errors.append(f"figures/{name}.png is not a valid PNG.")

        matches = [root / "analysis" / f"{name}{extension}" for extension in ANALYSIS_EXTENSIONS]
        existing = [path for path in matches if path.is_file()]
        if len(existing) != 1:
            errors.append(f"analysis/{name} must have exactly one editable source file.")
        elif existing[0].stat().st_size < 80:
            errors.append(f"{existing[0].relative_to(root)} is too short to reproduce the figure.")
        elif existing[0].suffix.lower() != ".pbix" and CODE_PLACEHOLDER.search(read_text(existing[0])):
            errors.append(f"{existing[0].relative_to(root)} still contains an unfinished placeholder.")

        record = root / "source-records" / f"{name}-source.yml"
        if not record.is_file():
            errors.append(f"Missing source-records/{name}-source.yml.")
            continue
        record_text = read_text(record)
        fields = source_fields(record_text)
        for key in SOURCE_KEYS:
            if key not in fields:
                errors.append(f"source-records/{name}-source.yml is missing `{key}`.")
        if PLACEHOLDER.search(record_text):
            errors.append(f"source-records/{name}-source.yml contains an unfinished placeholder.")
        landing_page = fields.get("landing_page", "")
        if not landing_page.startswith("https://"):
            errors.append(f"source-records/{name}-source.yml needs a full HTTPS landing_page.")
        else:
            landing_pages.add(landing_page)
        sha256 = fields.get("sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", sha256):
            errors.append(f"source-records/{name}-source.yml needs a lowercase SHA-256 checksum.")
        expected_analysis = f"analysis/{name}"
        expected_figure = f"figures/{name}.png"
        if not fields.get("analysis_path", "").startswith(expected_analysis):
            errors.append(f"source-records/{name}-source.yml points to the wrong analysis base name.")
        if fields.get("figure_path") != expected_figure:
            errors.append(f"source-records/{name}-source.yml points to the wrong figure.")

    if len(landing_pages) < 2:
        errors.append("The dossier must use at least two distinct public landing pages.")

    return errors


def png_chunk(kind: bytes, data: bytes) -> bytes:
    body = kind + data
    return struct.pack(">I", len(data)) + body + struct.pack(">I", binascii.crc32(body) & 0xFFFFFFFF)


def write_test_png(path: Path, width: int = 800, height: int = 600) -> None:
    rows = bytearray()
    for y in range(height):
        rows.append(0)
        for x in range(width):
            rows.extend(((x + y) % 256, (2 * x + y) % 256, (x + 2 * y) % 256))
    payload = b"\x89PNG\r\n\x1a\n"
    payload += png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    payload += png_chunk(b"IDAT", zlib.compress(bytes(rows), 6))
    payload += png_chunk(b"IEND", b"")
    path.write_bytes(payload)


def self_check() -> int:
    with tempfile.TemporaryDirectory(prefix="da730-cp1-") as folder:
        root = Path(folder)
        (root / "figures").mkdir()
        (root / "analysis").mkdir()
        (root / "source-records").mkdir()

        for relative, required in MARKDOWN_HEADINGS.items():
            body = "\n\n".join(required)
            body += "\n\nThis completed record names a clinical reader, source, finding, decision, check, and reproducible command."
            if relative == "decision-brief.md":
                body += "\n\n" + " ".join(["evidence"] * 510)
            (root / relative).write_text(body, encoding="utf-8")

        matrix = root / "selection-matrix.md"
        matrix.write_text(
            read_text(matrix)
            + "\n"
            + "\n".join(f"| `{name}.png` | Review | Compare | Table | Plot | Table | Tail |" for name in FIGURES),
            encoding="utf-8",
        )
        accessibility = root / "accessibility-check.md"
        accessibility.write_text(
            read_text(accessibility)
            + "\n"
            + "\n".join(f"`{name}.png` passes the recorded text and contrast checks." for name in FIGURES),
            encoding="utf-8",
        )

        for index, name in enumerate(FIGURES):
            write_test_png(root / "figures" / f"{name}.png")
            (root / "analysis" / f"{name}.R").write_text(
                "input <- read.csv('released-data.csv')\nstopifnot(nrow(input) > 0)\nplot(input[[1]], input[[2]])\n",
                encoding="utf-8",
            )
            (root / "source-records" / f"{name}-source.yml").write_text(
                f'''publisher: "Public health publisher {index}"
landing_page: "https://example.org/datasets/{index}"
retrieved_at: "2026-08-29"
released: "2026-08-13"
data_path: "released-data.csv"
analysis_path: "analysis/{name}.R"
figure_path: "figures/{name}.png"
sha256: "{'a' * 64}"
transformations:
  - "Selected the documented teaching rows."
known_limits:
  - "This display is descriptive."
''',
                encoding="utf-8",
            )

        valid_errors = validate(root)
        if valid_errors:
            print("Self-check failed on a valid fixture:")
            print("\n".join(f"- {error}" for error in valid_errors))
            return 1

        (root / "figures" / "rate.png").unlink()
        invalid_errors = validate(root)
        if not any("Missing figures/rate.png" in error for error in invalid_errors):
            print("Self-check failed to reject a missing required figure.")
            return 1

    print("Checkpoint validator self-check passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    if args.self_check:
        return self_check()
    if args.checkpoint is None:
        parser.error("provide a checkpoint folder or --self-check")

    errors = validate(args.checkpoint.resolve())
    if errors:
        print(f"Checkpoint failed with {len(errors)} issue(s):")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print("Checkpoint passed the DA-730 Week 3 structural contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the DA-730 Checkpoint 2 folder contract."""

from __future__ import annotations

import argparse
import binascii
import csv
import re
import struct
import tempfile
import zlib
from pathlib import Path


ARTIFACTS = (
    "accessible-display",
    "time-display",
    "comparison-display",
    "place-display",
    "structure-display",
    "dashboard",
)
EXPECTED_TABLE_ROWS = {
    "accessible-display": 65,
    "time-display": 94,
    "comparison-display": 500,
    "place-display": 100,
    "structure-display": 7,
    "dashboard": 3,
}
ANALYSIS_EXTENSIONS = (".R", ".py", ".ipynb", ".twb", ".pbix", ".ps1")
MARKDOWN_HEADINGS = {
    "README.md": (
        "# Checkpoint 2: applied visualization portfolio",
        "## Review decision",
        "## Portfolio findings",
        "## Reproduce this portfolio",
        "## Folder map",
        "## Known limits",
    ),
    "portfolio-index.md": (
        "# Portfolio index",
        "| Artifact | Module | Reader | Decision or task | Source population | Finding | Supported action | Material limit |",
        "## Readiness argument",
    ),
    "view-purpose-audit.md": (
        "# View-purpose audit",
        "| Artifact | Question answered | Unit and denominator | Time window | Visual structure | Exact-value fallback | Action enabled | Why another artifact cannot answer it |",
        "## Dashboard five-view audit",
        "| Dashboard view | Question answered | Measure | Unit | Window | Action enabled | Unique role |",
        "## View removed or revised",
    ),
    "critique-and-repair.md": (
        "# Critique and repair",
        "## Original display and reader task",
        "## Decision-contract failure",
        "## Evidence from Modules 07 through 12",
        "## Repair implemented",
        "## Verification",
        "## Remaining limit",
    ),
    "accessibility-report.md": (
        "# Accessibility report",
        "## Scope and readers",
        "## Color and contrast",
        "## Redundant cues",
        "## Reading order and hierarchy",
        "## Exact tables and text alternatives",
        "## Interaction and export",
        "## Checks completed",
        "## Remaining barriers",
    ),
    "decision-brief.md": (
        "# Decision brief",
        "## Review panel",
        "## Readiness finding",
        "## Evidence across the portfolio",
        "## Requested decision",
        "## Conditions or revisions",
        "## Material limitation",
    ),
    "capstone-proposal.md": (
        "# Capstone proposal",
        "## Working title",
        "## Decision owner and audience",
        "## Decision question",
        "## Source and rights",
        "## Population, unit, and time window",
        "## Measures and definitions",
        "## Planned analysis and displays",
        "## Accessibility plan",
        "## Reproducibility plan",
        "## Ethics, equity, and privacy",
        "## Expected limitation",
        "## Deliverables and review date",
        "## Approval requested",
    ),
    "ai-use.md": (
        "# AI-use record",
        "## Tool and model",
        "## Work delegated",
        "## Prompts or instructions",
        "## Generated artifacts used",
        "## Number and definition verification",
        "## Accessibility verification",
        "## Human decisions",
        "## Final responsibility statement",
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
    "table_path",
    "alt_text_path",
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


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def validate_table(path: Path, expected_rows: int) -> str | None:
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.reader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        return f"could not be read as CSV: {exc}"
    if not rows or len(rows[0]) < 3:
        return "needs a header with at least three fields"
    actual_rows = len(rows) - 1
    if actual_rows != expected_rows:
        return f"must contain {expected_rows} released rows; found {actual_rows}"
    if any(len(row) != len(rows[0]) for row in rows[1:]):
        return "contains rows with inconsistent field counts"
    return None


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"Checkpoint folder not found: {root}"]

    markdown: dict[str, str] = {}
    for relative, required in MARKDOWN_HEADINGS.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing {relative}.")
            continue
        text = read_text(path)
        markdown[relative] = text
        if len(text.strip()) < 180:
            errors.append(f"{relative} is too short to meet its contract.")
        for item in required:
            if item not in text:
                errors.append(f"{relative} is missing required content: {item}")
        if PLACEHOLDER.search(text):
            errors.append(f"{relative} still contains an unfinished instruction.")

    brief = markdown.get("decision-brief.md")
    if brief is not None:
        count = word_count(brief)
        if not 600 <= count <= 1000:
            errors.append(f"decision-brief.md must contain 600 to 1000 words; found {count}.")

    proposal = markdown.get("capstone-proposal.md")
    if proposal is not None:
        count = word_count(proposal)
        if not 700 <= count <= 1200:
            errors.append(f"capstone-proposal.md must contain 700 to 1200 words; found {count}.")

    for relative in ("portfolio-index.md", "view-purpose-audit.md", "accessibility-report.md"):
        text = markdown.get(relative, "")
        for name in ARTIFACTS:
            if f"`{name}.png`" not in text:
                errors.append(f"{relative} is missing `{name}.png`.")

    landing_pages: set[str] = set()
    for name in ARTIFACTS:
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
        else:
            analysis = existing[0]
            if analysis.stat().st_size < 80:
                errors.append(f"{analysis.relative_to(root)} is too short to reproduce the artifact.")
            elif analysis.suffix.lower() != ".pbix" and CODE_PLACEHOLDER.search(read_text(analysis)):
                errors.append(f"{analysis.relative_to(root)} still contains an unfinished instruction.")

        table = root / "evidence-tables" / f"{name}.csv"
        if not table.is_file():
            errors.append(f"Missing evidence-tables/{name}.csv.")
        else:
            table_error = validate_table(table, EXPECTED_TABLE_ROWS[name])
            if table_error:
                errors.append(f"evidence-tables/{name}.csv {table_error}.")

        alternative = root / "alt-text" / f"{name}.md"
        if not alternative.is_file():
            errors.append(f"Missing alt-text/{name}.md.")
        else:
            alt_text = read_text(alternative)
            if len(alt_text.strip()) < 160:
                errors.append(f"alt-text/{name}.md is too short to preserve the artifact meaning.")
            if PLACEHOLDER.search(alt_text):
                errors.append(f"alt-text/{name}.md still contains an unfinished instruction.")

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
            errors.append(f"source-records/{name}-source.yml contains an unfinished instruction.")
        landing_page = fields.get("landing_page", "")
        if not landing_page.startswith("https://"):
            errors.append(f"source-records/{name}-source.yml needs a full HTTPS landing_page.")
        else:
            landing_pages.add(landing_page)
        if not re.fullmatch(r"[0-9a-f]{64}", fields.get("sha256", "")):
            errors.append(f"source-records/{name}-source.yml needs a lowercase SHA-256 checksum.")
        if not fields.get("analysis_path", "").startswith(f"analysis/{name}"):
            errors.append(f"source-records/{name}-source.yml points to the wrong analysis base name.")
        if fields.get("figure_path") != f"figures/{name}.png":
            errors.append(f"source-records/{name}-source.yml points to the wrong figure.")
        if fields.get("table_path") != f"evidence-tables/{name}.csv":
            errors.append(f"source-records/{name}-source.yml points to the wrong evidence table.")
        if fields.get("alt_text_path") != f"alt-text/{name}.md":
            errors.append(f"source-records/{name}-source.yml points to the wrong accessible alternative.")

    if len(landing_pages) < 4:
        errors.append("The portfolio must preserve at least four distinct public landing pages.")

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
    with tempfile.TemporaryDirectory(prefix="da730-cp2-") as folder:
        root = Path(folder)
        for directory in ("figures", "analysis", "evidence-tables", "source-records", "alt-text"):
            (root / directory).mkdir()

        for relative, required in MARKDOWN_HEADINGS.items():
            body = "\n\n".join(required)
            body += "\n\nThis completed record names the reader, source, definition, finding, action, limit, and verification."
            if relative == "decision-brief.md":
                body += "\n\n" + " ".join(["evidence"] * 620)
            if relative == "capstone-proposal.md":
                body += "\n\n" + " ".join(["proposal"] * 730)
            (root / relative).write_text(body, encoding="utf-8")

        for relative in ("portfolio-index.md", "view-purpose-audit.md", "accessibility-report.md"):
            path = root / relative
            path.write_text(
                read_text(path)
                + "\n"
                + "\n".join(f"`{name}.png` has a completed reader, source, action, and access record." for name in ARTIFACTS),
                encoding="utf-8",
            )

        for index, name in enumerate(ARTIFACTS):
            write_test_png(root / "figures" / f"{name}.png")
            (root / "analysis" / f"{name}.R").write_text(
                "input <- read.csv('released-data.csv')\nstopifnot(nrow(input) > 0)\nplot(input[[1]], input[[2]])\n",
                encoding="utf-8",
            )
            with (root / "evidence-tables" / f"{name}.csv").open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(("id", "value", "status"))
                for row in range(EXPECTED_TABLE_ROWS[name]):
                    writer.writerow((row + 1, row, "reported"))
            (root / "alt-text" / f"{name}.md").write_text(
                f"# {name}\n\n" + " ".join(["accessible evidence"] * 90),
                encoding="utf-8",
            )
            (root / "source-records" / f"{name}-source.yml").write_text(
                f'''publisher: "Public health publisher {index}"
landing_page: "https://example.org/datasets/{index}"
retrieved_at: "2026-08-30"
released: "2026-08-13"
data_path: "released-data.csv"
analysis_path: "analysis/{name}.R"
figure_path: "figures/{name}.png"
table_path: "evidence-tables/{name}.csv"
alt_text_path: "alt-text/{name}.md"
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

        (root / "figures" / "dashboard.png").unlink()
        invalid_errors = validate(root)
        if not any("Missing figures/dashboard.png" in error for error in invalid_errors):
            print("Self-check failed to reject a missing required figure.")
            return 1

    print("Checkpoint 2 validator self-check passed.")
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

    print("Checkpoint passed the DA-730 Week 6 structural contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

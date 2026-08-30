#!/usr/bin/env python3
"""Validate the DA-730 final decision-story capstone folder."""

from __future__ import annotations

import argparse
import binascii
import csv
import hashlib
import re
import shutil
import struct
import tempfile
import zlib
from pathlib import Path


DATA_FILES = {
    "ma_ed_public_reporting_dashboard_2026.csv": (186, 31, "fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd"),
    "ed_dashboard_measure_dictionary_2026.csv": (3, 18, "2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412"),
    "cms_ma_ed_dashboard_source_2026.csv": (186, 15, "f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b"),
}
TABLE_FIELDS = (
    "measure_id", "display_label", "score_raw", "score_numeric", "unit", "sample",
    "value_status", "footnote", "period_start", "period_end", "cms_release_date",
    "source_lag_days_at_release", "ma_reported_n", "ma_median", "ma_rank_unfavorable",
    "scenario_threshold", "threshold_crossed", "threshold_origin", "monitoring_use",
    "action_if_crossed",
)
MARKDOWN_HEADINGS = {
    "README.md": (
        "# DA-730 final decision-story capstone", "## Release status", "## Audiences and authority",
        "## Decision", "## Evidence and finding", "## Supported action", "## Unsupported actions",
        "## Reproduce this release", "## Folder map", "## Review and disposition", "## Known limits",
    ),
    "decision-brief.md": (
        "# Decision brief", "## Audience and authority", "## Finding", "## Evidence",
        "## Requested decision", "## Action owner and next review", "## Uncertainty or freshness",
        "## Material limitation", "## Unsupported conclusion",
    ),
    "alt-text.md": (
        "# Accessible alternatives", "## Primary executive figure", "## Supporting technical figure",
        "## Equivalent access check",
    ),
    "transformation-record.md": (
        "# Transformation record", "## Inputs and fingerprints", "## Source selection",
        "## Filters and exclusions", "## Definitions and recodes", "## Calculations and references",
        "## Thresholds and action rules", "## Figure construction", "## Audience adaptation",
        "## Manual review and exports", "## Known limits",
    ),
    "audience-adaptation-record.md": (
        "# Audience-adaptation record", "## Audience authority", "## Adaptation table",
        "## Cross-version audit",
    ),
    "reproducibility-check.md": (
        "# Reproducibility check", "## Test environment", "## Input verification",
        "## Commands run", "## Outputs verified", "## Visual and accessibility inspection",
        "## Validator result", "## Reproduction result",
    ),
    "critique-response.md": (
        "# Critique response", "## Review source", "## Original problem", "## Likely reader error",
        "## Decision affected", "## Repair implemented", "## Evidence invariants",
        "## Accessibility check", "## Reviewer response", "## Remaining limit",
    ),
    "ai-use.md": (
        "# AI-use record", "## Tools, models, and dates", "## Work delegated",
        "## Material prompts or instructions", "## Generated artifacts used",
        "## Number and definition verification", "## Source and rights verification",
        "## Cross-audience verification", "## Accessibility verification", "## Human decisions",
        "## Final responsibility statement",
    ),
    "review-disposition.md": (
        "# Final review disposition", "## Review record", "## Decision rationale",
        "## Conditions or revisions", "## Release boundary",
    ),
    "defense/questions-and-responses.md": (
        "# Defense questions and responses",
        "## 1. What decision does this release support?",
        "## 2. Why is the 23-percent OP-22 value not a current performance rating?",
        "## 3. What do the 3-percent median and 10-percent trigger mean?",
        "## 4. What changed across the two audiences, and what could not change?",
        "## 5. Why is the supporting figure necessary?",
        "## 6. How can another analyst reproduce and audit the release?",
        "## 7. How does the release provide equivalent access?",
        "## 8. How was AI assistance checked?",
        "## 9. What evidence would be needed before an intervention decision?",
        "## 10. What is the strongest remaining limitation?",
    ),
}
SOURCE_EXPECTED = {
    "landing_page": "https://data.cms.gov/provider-data/dataset/yv7e-xc69",
    "teaching_data_path": "data/ma_ed_public_reporting_dashboard_2026.csv",
    "teaching_data_rows": "186",
    "teaching_data_columns": "31",
    "teaching_data_sha256": DATA_FILES["ma_ed_public_reporting_dashboard_2026.csv"][2],
    "measure_dictionary_path": "data/ed_dashboard_measure_dictionary_2026.csv",
    "measure_dictionary_rows": "3",
    "measure_dictionary_columns": "18",
    "measure_dictionary_sha256": DATA_FILES["ed_dashboard_measure_dictionary_2026.csv"][2],
    "source_selection_path": "data/cms_ma_ed_dashboard_source_2026.csv",
    "source_selection_rows": "186",
    "source_selection_columns": "15",
    "source_selection_sha256": DATA_FILES["cms_ma_ed_dashboard_source_2026.csv"][2],
    "analysis_path": "analysis/analysis.R",
    "primary_figure_path": "figure-primary.png",
    "supporting_figure_path": "figure-supporting.png",
    "accessible_table_path": "accessible-table.csv",
    "alt_text_path": "alt-text.md",
}
ANALYSIS_EXTENSIONS = (".R", ".py", ".ipynb", ".twb", ".pbix", ".ps1")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|REPLACE_ME)\b", re.IGNORECASE)
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or ()), list(reader)


def source_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^([a-z][a-z0-9_]*)\s*:\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")
    return fields


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("not a PNG")
    return struct.unpack(">II", data[16:24])


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"Final checkpoint folder not found: {root}"]

    markdown: dict[str, str] = {}
    for relative, headings in MARKDOWN_HEADINGS.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing {relative}.")
            continue
        text = read_text(path)
        markdown[relative] = text
        if len(text.strip()) < 220:
            errors.append(f"{relative} is too short to meet its contract.")
        for heading in headings:
            if heading not in text:
                errors.append(f"{relative} is missing required content: {heading}")
        if PLACEHOLDER.search(text):
            errors.append(f"{relative} still contains an unfinished instruction.")

    limits = {
        "README.md": (350, 1300),
        "decision-brief.md": (600, 900),
        "alt-text.md": (300, 900),
        "transformation-record.md": (450, 1500),
        "audience-adaptation-record.md": (350, 1200),
        "reproducibility-check.md": (350, 1200),
        "critique-response.md": (350, 1000),
        "ai-use.md": (350, 1200),
        "defense/questions-and-responses.md": (600, 1500),
    }
    for relative, (minimum, maximum) in limits.items():
        if relative in markdown:
            count = word_count(markdown[relative])
            if not minimum <= count <= maximum:
                errors.append(f"{relative} must contain {minimum} to {maximum} words; found {count}.")

    invariant_docs = ("decision-brief.md", "alt-text.md", "audience-adaptation-record.md")
    for relative in invariant_docs:
        text = markdown.get(relative, "").lower()
        for token in ("23 percent", "53", "590", "definition and current-data review"):
            if token not in text:
                errors.append(f"{relative} does not preserve required invariant: {token}")

    for name, (expected_rows, expected_columns, expected_hash) in DATA_FILES.items():
        path = root / "data" / name
        if not path.is_file():
            errors.append(f"Missing data/{name}.")
            continue
        try:
            header, rows = csv_rows(path)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"data/{name} could not be read as CSV: {exc}")
            continue
        if len(rows) != expected_rows or len(header) != expected_columns:
            errors.append(f"data/{name} must be {expected_rows} rows by {expected_columns} columns; found {len(rows)} by {len(header)}.")
        if sha256(path) != expected_hash:
            errors.append(f"data/{name} does not match the released SHA-256 fingerprint.")

    table = root / "accessible-table.csv"
    if not table.is_file():
        errors.append("Missing accessible-table.csv.")
    else:
        try:
            header, rows = csv_rows(table)
            if tuple(header) != TABLE_FIELDS:
                errors.append("accessible-table.csv does not have the exact 20-field release schema.")
            if len(rows) != 3:
                errors.append(f"accessible-table.csv must contain three selected-facility rows; found {len(rows)}.")
            by_measure = {row.get("measure_id", ""): row for row in rows}
            if set(by_measure) != {"EDV", "OP_18b", "OP_22"}:
                errors.append("accessible-table.csv must contain EDV, OP_18b, and OP_22 exactly once.")
            op22 = by_measure.get("OP_22", {})
            expected_op22 = {
                "score_numeric": "23", "unit": "percent", "sample": "19211",
                "source_lag_days_at_release": "590", "ma_reported_n": "53", "ma_median": "3",
                "scenario_threshold": "10", "threshold_crossed": "yes",
                "monitoring_use": "historical_public_reporting_review_only",
            }
            for field, value in expected_op22.items():
                if op22.get(field) != value:
                    errors.append(f"accessible-table.csv OP_22 {field} must be {value!r}.")
            if "not a CMS benchmark" not in op22.get("threshold_origin", ""):
                errors.append("accessible-table.csv must identify the OP_22 trigger as non-CMS.")
            op18 = by_measure.get("OP_18b", {})
            for field, value in {"score_numeric": "188", "sample": "422", "source_lag_days_at_release": "317", "ma_reported_n": "54", "ma_median": "211.5", "scenario_threshold": "240", "threshold_crossed": "no"}.items():
                if op18.get(field) != value:
                    errors.append(f"accessible-table.csv OP_18b {field} must be {value!r}.")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"accessible-table.csv could not be read: {exc}")

    figure_hashes: list[str] = []
    for name in ("figure-primary.png", "figure-supporting.png"):
        path = root / name
        if not path.is_file():
            errors.append(f"Missing {name}.")
            continue
        try:
            width, height = png_dimensions(path)
            if width < 1000 or height < 600:
                errors.append(f"{name} is {width}x{height}; minimum is 1000x600.")
            if path.stat().st_size < 10_000:
                errors.append(f"{name} is too small to be a completed figure.")
            figure_hashes.append(sha256(path))
        except ValueError:
            errors.append(f"{name} is not a valid PNG.")
    if len(figure_hashes) == 2 and len(set(figure_hashes)) != 2:
        errors.append("The primary and supporting figures must not be identical.")

    analysis_files = [root / "analysis" / f"analysis{extension}" for extension in ANALYSIS_EXTENSIONS]
    existing_analysis = [path for path in analysis_files if path.is_file()]
    if len(existing_analysis) != 1:
        errors.append("analysis/ must contain exactly one editable file named analysis with an approved extension.")
    else:
        analysis = existing_analysis[0]
        if analysis.stat().st_size < 200:
            errors.append(f"{analysis.relative_to(root)} is too short to reproduce the evidence.")
        elif analysis.suffix.lower() != ".pbix" and PLACEHOLDER.search(read_text(analysis)):
            errors.append(f"{analysis.relative_to(root)} contains an unfinished instruction.")

    source = root / "source-record.yml"
    if not source.is_file():
        errors.append("Missing source-record.yml.")
    else:
        text = read_text(source)
        fields = source_fields(text)
        if PLACEHOLDER.search(text):
            errors.append("source-record.yml contains an unfinished instruction.")
        for field, expected in SOURCE_EXPECTED.items():
            if fields.get(field) != expected:
                errors.append(f"source-record.yml {field} must be {expected!r}.")
        for field in ("landing_page", "complete_csv_url", "data_dictionary_url", "measure_periods_url"):
            if not fields.get(field, "").startswith("https://"):
                errors.append(f"source-record.yml {field} must be a complete HTTPS URL.")

    slides = root / "defense" / "slides.pdf"
    if not slides.is_file():
        errors.append("Missing defense/slides.pdf.")
    else:
        content = slides.read_bytes()
        if len(content) < 300 or not content.startswith(b"%PDF-") or b"/Type /Page" not in content or not content.rstrip().endswith(b"%%EOF"):
            errors.append("defense/slides.pdf is not a nonempty PDF with at least one page marker.")

    review = source_fields(markdown.get("review-disposition.md", ""))
    for field in ("reviewer", "reviewer_role", "review_date", "official_half_term_end_date", "score", "defense_result", "clinical_review", "accessibility_review", "reproducibility_review", "disposition"):
        if not review.get(field):
            errors.append(f"review-disposition.md is missing {field}.")
    for field in ("review_date", "official_half_term_end_date"):
        if review.get(field) and not DATE.fullmatch(review[field]):
            errors.append(f"review-disposition.md {field} must use YYYY-MM-DD.")
    try:
        if float(review.get("score", "")) < 80:
            errors.append("review-disposition.md score must be at least 80 for release.")
    except ValueError:
        errors.append("review-disposition.md score must be numeric.")
    for field in ("defense_result", "clinical_review", "accessibility_review", "reproducibility_review"):
        if review.get(field, "").lower() != "pass":
            errors.append(f"review-disposition.md {field} must be pass for release.")
    if review.get("disposition", "").lower() not in {"approve", "approve with conditions"}:
        errors.append("review-disposition.md disposition must be approve or approve with conditions for release.")

    reproducibility = markdown.get("reproducibility-check.md", "").lower()
    for _, _, fingerprint in DATA_FILES.values():
        if fingerprint not in reproducibility:
            errors.append("reproducibility-check.md is missing an input SHA-256 fingerprint.")
    if "pass" not in reproducibility:
        errors.append("reproducibility-check.md must record a passing result.")

    return errors


def png_chunk(kind: bytes, data: bytes) -> bytes:
    body = kind + data
    return struct.pack(">I", len(data)) + body + struct.pack(">I", binascii.crc32(body) & 0xFFFFFFFF)


def write_test_png(path: Path, offset: int) -> None:
    width, height = 1000, 600
    rows = bytearray()
    for y in range(height):
        rows.append(0)
        for x in range(width):
            rows.extend(((x + offset) % 256, (y + offset) % 256, (x + y + offset) % 256))
    payload = b"\x89PNG\r\n\x1a\n"
    payload += png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    payload += png_chunk(b"IDAT", zlib.compress(bytes(rows), 6))
    payload += png_chunk(b"IEND", b"")
    path.write_bytes(payload)


def write_test_pdf(path: Path) -> None:
    padding = b"% accessible defense fixture " + b"evidence " * 40 + b"\n"
    path.write_bytes(
        b"%PDF-1.4\n1 0 obj<</Type /Catalog /Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type /Pages /Kids[3 0 R]/Count 1>>endobj\n"
        b"3 0 obj<</Type /Page /Parent 2 0 R /MediaBox[0 0 612 792]>>endobj\n"
        + padding + b"trailer<</Root 1 0 R>>\n%%EOF"
    )


def self_check() -> int:
    package = Path(__file__).resolve().parent
    repo = package.parents[3]
    upstream = repo / "courses" / "data-visualization" / "modules" / "12-dashboards-multi-view-composition" / "data"
    with tempfile.TemporaryDirectory(prefix="da730-final-") as folder:
        root = Path(folder)
        (root / "analysis").mkdir()
        (root / "data").mkdir()
        (root / "defense").mkdir()

        for name in DATA_FILES:
            shutil.copy2(upstream / name, root / "data" / name)
        shutil.copy2(package / "template" / "source-record.yml", root / "source-record.yml")
        (root / "analysis" / "analysis.R").write_text(
            "input <- read.csv('../data/ma_ed_public_reporting_dashboard_2026.csv')\nstopifnot(nrow(input) == 186)\nselected <- input[input$selected_hospital == 'yes', ]\nstopifnot(nrow(selected) == 3)\nprint(c('figure-primary.png', 'figure-supporting.png', 'accessible-table.csv'))\n",
            encoding="utf-8",
        )

        _, teaching = csv_rows(root / "data" / "ma_ed_public_reporting_dashboard_2026.csv")
        selected = [row for row in teaching if row["selected_hospital"] == "yes"]
        with (root / "accessible-table.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=TABLE_FIELDS)
            writer.writeheader()
            writer.writerows({field: row[field] for field in TABLE_FIELDS} for row in selected)

        write_test_png(root / "figure-primary.png", 7)
        write_test_png(root / "figure-supporting.png", 29)
        write_test_pdf(root / "defense" / "slides.pdf")

        filler = "The completed evidence preserves 23 percent across 53 reporting peers and a 590 day historical boundary while supporting definition and current-data review. "
        for relative, headings in MARKDOWN_HEADINGS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            if relative == "review-disposition.md":
                body = "\n\n".join(headings) + "\n\nreviewer: \"Faculty Reviewer\"\nreviewer_role: \"DA-730 faculty\"\nreview_date: \"2026-12-18\"\nofficial_half_term_end_date: \"2026-12-18\"\nscore: \"90\"\ndefense_result: \"pass\"\nclinical_review: \"pass\"\naccessibility_review: \"pass\"\nreproducibility_review: \"pass\"\ndisposition: \"approve\"\n\n" + filler * 12
            else:
                body = "\n\n".join(headings) + "\n\n" + filler * 28
                if relative == "reproducibility-check.md":
                    body += "\n\npass\n" + "\n".join(value[2] for value in DATA_FILES.values())
            path.write_text(body, encoding="utf-8")

        valid_errors = validate(root)
        if valid_errors:
            print("Self-check failed on a valid fixture:")
            print("\n".join(f"- {error}" for error in valid_errors))
            return 1

        (root / "figure-supporting.png").unlink()
        invalid_errors = validate(root)
        if not any("Missing figure-supporting.png" in error for error in invalid_errors):
            print("Self-check failed to reject a missing supporting figure.")
            return 1

    print("Final checkpoint validator self-check passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    if args.checkpoint is None:
        parser.error("provide a final checkpoint folder or --self-check")

    errors = validate(args.checkpoint.resolve())
    if errors:
        print(f"Final checkpoint failed with {len(errors)} issue(s):")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Final checkpoint passed the DA-730 release contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

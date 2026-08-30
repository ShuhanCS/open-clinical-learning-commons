#!/usr/bin/env python3
"""Build the DA-730 Module 07 accessibility teaching table."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = MODULE_ROOT.parent / "06-uncertainty-variation-small-numbers" / "data" / "ma_hf_readmission_uncertainty_2026.csv"
DEFAULT_OUTPUT = MODULE_ROOT / "data" / "accessibility_hf_readmission_2026.csv"
SOURCE_SHA256 = "33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727"

ENCODINGS = {
    "better": {
        "display_label": "Better than national",
        "display_symbol": "B",
        "display_shape": "square",
        "display_shape_code": "15",
        "display_line_type": "solid",
        "display_color_hex": "#1B7837",
    },
    "no different": {
        "display_label": "No different from national",
        "display_symbol": "N",
        "display_shape": "circle",
        "display_shape_code": "16",
        "display_line_type": "solid",
        "display_color_hex": "#2166AC",
    },
    "worse": {
        "display_label": "Worse than national",
        "display_symbol": "W",
        "display_shape": "triangle",
        "display_shape_code": "17",
        "display_line_type": "solid",
        "display_color_hex": "#B2182B",
    },
    "too few": {
        "display_label": "Too few cases",
        "display_symbol": "T",
        "display_shape": "x",
        "display_shape_code": "4",
        "display_line_type": "dashed",
        "display_color_hex": "#4D4D4D",
    },
    "not available": {
        "display_label": "Not available",
        "display_symbol": "NA",
        "display_shape": "plus",
        "display_shape_code": "3",
        "display_line_type": "dotted",
        "display_color_hex": "#111111",
    },
}

OUTPUT_FIELDS = (
    "facility_id",
    "facility_name",
    "city",
    "county",
    "measure_id",
    "measure_name",
    "denominator",
    "score",
    "lower_estimate",
    "higher_estimate",
    "start_date",
    "end_date",
    "estimate_status",
    "source_comparison_group",
    "display_status",
    "display_label",
    "display_symbol",
    "display_shape",
    "display_shape_code",
    "display_line_type",
    "display_color_hex",
    "contrast_on_white",
    "contrast_on_black",
    "reading_order",
    "short_alt_row",
    "footnote_text",
    "source_release",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative_luminance(color: str) -> float:
    values = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in values]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first: str, second: str) -> float:
    first_luminance = relative_luminance(first)
    second_luminance = relative_luminance(second)
    light = max(first_luminance, second_luminance)
    dark = min(first_luminance, second_luminance)
    return (light + 0.05) / (dark + 0.05)


def display_status(row: dict[str, str]) -> str:
    if row["estimate_status"] == "reported":
        return row["source_comparison_group"]
    if row["estimate_status"] == "too_few":
        return "too few"
    return "not available"


def alt_row(row: dict[str, str], label: str) -> str:
    if row["estimate_status"] == "reported":
        return (
            f'{row["facility_name"]}: score {row["score"]}, source interval '
            f'{row["lower_estimate"]} to {row["higher_estimate"]}, denominator '
            f'{row["denominator"]}, {label.lower()}.'
        )
    return f'{row["facility_name"]}: {label.lower()}; no score or source interval is displayed.'


def sort_key(row: dict[str, str]) -> tuple[int, float, str]:
    if row["estimate_status"] == "reported":
        return (0, -float(row["score"]), row["facility_name"])
    if row["estimate_status"] == "too_few":
        return (1, 0, row["facility_name"])
    return (2, 0, row["facility_name"])


def build(source: Path, output: Path) -> None:
    if not source.is_file():
        raise SystemExit(f"Source file not found: {source}")
    actual_sha = sha256(source)
    if actual_sha != SOURCE_SHA256:
        raise SystemExit(f"Module 06 source checksum changed: {actual_sha}")

    with source.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 65 or len({row["facility_id"] for row in rows}) != 65:
        raise SystemExit("Expected 65 unique Massachusetts hospital rows.")

    rows.sort(key=sort_key)
    released: list[dict[str, str]] = []
    for reading_order, row in enumerate(rows, start=1):
        status = display_status(row)
        if status not in ENCODINGS:
            raise SystemExit(f"No accessibility encoding for source status: {status}")
        encoding = ENCODINGS[status]
        color = encoding["display_color_hex"]
        output_row = {field: row.get(field, "") for field in OUTPUT_FIELDS}
        output_row.update(encoding)
        output_row["display_status"] = status
        output_row["contrast_on_white"] = f'{contrast_ratio(color, "#FFFFFF"):.2f}'
        output_row["contrast_on_black"] = f'{contrast_ratio(color, "#000000"):.2f}'
        output_row["reading_order"] = str(reading_order)
        output_row["short_alt_row"] = alt_row(row, encoding["display_label"])
        released.append(output_row)

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(released)

    print(f"Wrote {len(released)} accessibility rows to {output}")
    print(f"SHA-256: {sha256(output)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()

"""Validate the FND-1 Module 06 accessible-figure release or submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

import render_figures


MODULE_ROOT = Path(__file__).resolve().parent
INPUTS = {
    "data/missingness-profile.csv": (29, 12, 4_362, "46e9c4dd268db223fac3cd0f01e65e050a3d44f6a28e0babcfb7bd5b552b5ba5"),
    "data/rates.csv": (6, 13, 1_893, "2398b283e449d6f876a3a3ea123e7905c637ba222f56c6aa03882cfc158942f3"),
    "data/denominator-registry.csv": (27, 12, 10_094, "e13bd0e1cf0716b912476fd81c7e4dd8bc827b2df468421aa2efc33f1f234be6"),
    "data/resolved-analytic-table.csv": (374, 29, 121_787, "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"),
}
TABLES = {
    "tables/quality-missingness.csv": (8, 12, 1_672, "52e6960cda5d4981a647683ea202e47a1a1ad5afde0e91fb8900adf0b0521134"),
    "tables/descriptive-rates.csv": (6, 13, 1_893, "2398b283e449d6f876a3a3ea123e7905c637ba222f56c6aa03882cfc158942f3"),
    "tables/quarterly-index-counts.csv": (20, 9, 3_631, "0f5e2f8d9b163ad4b68a8f73505fdd4b34f44936eec4fb0c88c3853f58d86fb6"),
}
ARTIFACTS = {
    "figures/quality-missingness.png": (169_864, "dd91d7c84fe73f1a29e4c8301b6be18e329bc03a8652927f620ff130fb6f51b6"),
    "figures/quality-missingness.svg": (71_065, "71346d9b200f00021323539961c4440f6a6fb212459b58e9ae7959a1e4b8d30f"),
    "figures/descriptive-rates.png": (132_463, "11b5edc3781248a22e2359355778be638ffde0977a899c0f8b215665416d3038"),
    "figures/descriptive-rates.svg": (68_139, "480ca1cf69a6591127bf8ad8c064bce52dde49a783aeb4dc9b524c1c9ee04c99"),
    "figures/quarterly-index-counts.png": (188_721, "9befa6d9604ed26abdaf28b07afc335cc7ad5eaa3c368b9bf2d7401dffa546e7"),
    "figures/quarterly-index-counts.svg": (76_002, "2ee876e3b141a7a0ffa6f6558ac05b3127fd5c11eb22143835b5692ffdc4700c"),
    "alt-text/quality-missingness.md": (1_020, "04ebe8ce093df334888dc71864cb6563e31474ffac5a158a3fcdb07db7530943"),
    "alt-text/descriptive-rates.md": (1_001, "e71b03951ed7fe8b43036dba4118d007913119330f6997970847077964dcda86"),
    "alt-text/quarterly-index-counts.md": (934, "b1e2ef4134760308f3bd72b6711aa41319456715d939bcd9505302502dfae0a7"),
    "figure-registry.csv": (3_191, "5cdd846d9318d6dc8c2f3da41a6be6ce172b7c91d6465dc085e9f3790732d62b"),
}
STEMS = ("quality-missingness", "descriptive-rates", "quarterly-index-counts")
SUBMISSION_FILES = (
    "VERSION", "README.md", "source-record.yml", "figure-spec.md", "render_figures.py",
    *INPUTS, *TABLES, *ARTIFACTS, "accessibility-check.md", "transformation-record.md",
    "reproducibility-check.md", "ai-use.md",
)
RELEASE_FILES = (
    "assessment.md", "instructor-notes.md", "release.json", "render-report.json",
    "validate_figures.py", "learner-template/README.md",
)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def validate(root: Path, submission: bool = False) -> tuple[int, list[str]]:
    checks = 0
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            errors.append(message)

    for name in SUBMISSION_FILES + (() if submission else RELEASE_FILES):
        check((root / name).is_file(), f"Missing required file: {name}")
    if errors:
        return checks, errors

    check((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "VERSION must be 0.1.0.")
    input_rows: dict[str, list[dict[str, str]]] = {}
    for name, (row_count, field_count, byte_count, digest) in INPUTS.items():
        path = root / name
        fields, rows = read_csv(path)
        input_rows[name] = rows
        check(len(rows) == row_count, f"{name} row count changed.")
        check(len(fields) == field_count, f"{name} field count changed.")
        check(path.stat().st_size == byte_count, f"{name} byte count changed.")
        check(render_figures.sha256(path) == digest, f"{name} SHA-256 changed.")

    source = input_rows["data/resolved-analytic-table.csv"]
    registry_input = input_rows["data/denominator-registry.csv"]
    check(len({row["patient_id"] for row in source}) == 374, "Patient grain changed.")
    check(len({row["index_encounter_id"] for row in source}) == 374, "Index grain changed.")
    check(all(row["source_release"] == "synthea-csv-apr2020" for row in source), "Source release changed.")
    check(all(row["cohort_definition_version"] == "0.1.0" for row in source), "Cohort version changed.")
    check({row["result_id"] for row in registry_input if row["result_id"].startswith("RT")} == {f"RT{n:02d}" for n in range(1, 7)}, "Rate registry changed.")
    retained = {item for row in registry_input for item in row["retained_conditions"].split("|") if item.startswith("N")}
    check(retained == {f"N{n:02d}" for n in range(1, 9)}, "N01 through N08 coverage changed.")

    actual_tables: dict[str, list[dict[str, str]]] = {}
    for name, (row_count, field_count, byte_count, digest) in TABLES.items():
        path = root / name
        fields, rows = read_csv(path)
        actual_tables[name] = rows
        check(len(rows) == row_count, f"{name} row count changed.")
        check(len(fields) == field_count, f"{name} field count changed.")
        check(path.stat().st_size == byte_count, f"{name} byte count changed.")
        check(render_figures.sha256(path) == digest, f"{name} SHA-256 changed.")

    expected_tables = {
        "tables/quality-missingness.csv": render_figures.quality_table(input_rows["data/missingness-profile.csv"]),
        "tables/descriptive-rates.csv": input_rows["data/rates.csv"],
        "tables/quarterly-index-counts.csv": render_figures.quarterly_table(source),
    }
    for name, expected_rows in expected_tables.items():
        for row_number, (actual, expected) in enumerate(zip(actual_tables[name], expected_rows, strict=True), start=1):
            for field, value in expected.items():
                check(actual[field] == str(value), f"{name} row {row_number} changed: {field}")

    quality = actual_tables["tables/quality-missingness.csv"]
    rates = actual_tables["tables/descriptive-rates.csv"]
    quarters = actual_tables["tables/quarterly-index-counts.csv"]
    check(all(row["figure_id"] == "F01" for row in quality), "F01 table ID changed.")
    check(all(int(row["accepted_denominator"]) == 374 for row in quality), "F01 accepted denominator changed.")
    check(all(int(row["defective_denominator"]) == 379 for row in quality), "F01 defective denominator changed.")
    check([int(row["numerator"]) for row in rates] == [111, 92, 4, 15, 36, 8], "F02 numerators changed.")
    check(all(int(row["denominator"]) == 374 for row in rates), "F02 denominators changed.")
    check([row["quarter_label"] for row in quarters] == [f"{year} Q{quarter}" for year in range(2015, 2020) for quarter in range(1, 5)], "F03 quarter continuity changed.")
    check(sum(int(row["total_index_n"]) for row in quarters) == 374, "F03 total does not equal 374.")
    check(sum(int(row["emergency_index_n"]) for row in quarters) == 314, "F03 emergency total does not equal 314.")
    check(sum(int(row["inpatient_index_n"]) for row in quarters) == 60, "F03 inpatient total does not equal 60.")

    for name, (byte_count, digest) in ARTIFACTS.items():
        path = root / name
        check(path.stat().st_size == byte_count, f"{name} byte count changed.")
        check(render_figures.sha256(path) == digest, f"{name} SHA-256 changed.")

    for stem in STEMS:
        png = root / f"figures/{stem}.png"
        check(png.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", f"{stem} PNG signature changed.")
        with Image.open(png) as image:
            check(image.format == "PNG", f"{stem} is not PNG.")
            check(image.size == (2100, 1200), f"{stem} PNG dimensions changed.")
            dpi = image.info.get("dpi", (0, 0))
            check(all(abs(value - 300) < 0.1 for value in dpi), f"{stem} PNG is not 300 DPI.")
            check(image.info.get("Software") == "Open Clinical Learning Commons", f"{stem} PNG software metadata changed.")
        svg_root = ET.parse(root / f"figures/{stem}.svg").getroot()
        check(svg_root.tag.endswith("svg"), f"{stem} SVG root changed.")
        check(svg_root.attrib.get("width") == "504pt", f"{stem} SVG width changed.")
        check(svg_root.attrib.get("height") == "288pt", f"{stem} SVG height changed.")
        check(svg_root.attrib.get("viewBox") == "0 0 504 288", f"{stem} SVG viewBox changed.")

    registry_fields, figure_registry = read_csv(root / "figure-registry.csv")
    check(len(figure_registry) == 3, "Figure registry must have three rows.")
    check(len(registry_fields) == 25, "Figure registry field count changed.")
    check([row["figure_id"] for row in figure_registry] == ["F01", "F02", "F03"], "Figure ID order changed.")
    for row, stem in zip(figure_registry, STEMS, strict=True):
        check(row["table_path"] == f"tables/{stem}.csv", f"{row['figure_id']} table path changed.")
        check(row["png_path"] == f"figures/{stem}.png", f"{row['figure_id']} PNG path changed.")
        check(row["svg_path"] == f"figures/{stem}.svg", f"{row['figure_id']} SVG path changed.")
        check(row["alt_text_path"] == f"alt-text/{stem}.md", f"{row['figure_id']} alt-text path changed.")
        for kind in ("table", "png", "svg", "alt_text"):
            check(row[f"{kind}_sha256"] == render_figures.sha256(root / row[f"{kind}_path"]), f"{row['figure_id']} {kind} hash link changed.")
        check(row["width_pixels"] == "2100" and row["height_pixels"] == "1200", f"{row['figure_id']} registered dimensions changed.")
        check(row["dpi"] == "300.00" and row["canvas_inches"] == "7x4", f"{row['figure_id']} registered canvas changed.")
        check(row["palette"] == "#0072B2|#E69F00|#000000", f"{row['figure_id']} palette changed.")
        check(bool(row["question"] and row["title"] and row["units"] and row["caption"]), f"{row['figure_id']} communication contract is incomplete.")
        check(Path(row["table_path"]).name in row["caption"], f"{row['figure_id']} caption does not name its exact table.")
        check(bool(row["redundant_cue"]), f"{row['figure_id']} redundant cue missing.")
        check(row["zero_baseline"] == "yes", f"{row['figure_id']} zero baseline changed.")
        check(bool(row["claim_limit"]), f"{row['figure_id']} claim limit missing.")
    check(figure_registry[1]["uncertainty"] == "Wilson 95 percent from Module 05", "F02 uncertainty definition changed.")
    check(all(figure_registry[index]["uncertainty"] == "none; no approved estimate" for index in (0, 2)), "Unsupported uncertainty added to F01 or F03.")

    alt_requirements = {
        "quality-missingness": ("343 of 374", "379-row", "structurally correct", "tables/quality-missingness.csv"),
        "descriptive-rates": ("111 of 374", "4 of 374", "Wilson 95-percent", "tables/descriptive-rates.csv"),
        "quarterly-index-counts": ("2015 Q1", "2019 Q3", "314", "tables/quarterly-index-counts.csv"),
    }
    for stem, phrases in alt_requirements.items():
        text = (root / f"alt-text/{stem}.md").read_text(encoding="utf-8")
        for heading in ("Purpose:", "Structure:", "Main values:", "Finding and limit:"):
            check(heading in text, f"{stem} alternative missing {heading}")
        for phrase in phrases:
            check(phrase in text, f"{stem} alternative missing exact fact: {phrase}")

    accessibility = (root / "accessibility-check.md").read_text(encoding="utf-8")
    for phrase in ("Grayscale", "50-percent width", "200-percent zoom", "Reading order", "Structured text alternatives", "5.185:1", "2.252:1", "21.000:1"):
        check(phrase.lower() in accessibility.lower(), f"Accessibility record missing: {phrase}")
    handoff_text = "\n".join((root / name).read_text(encoding="utf-8") for name in ("README.md", "figure-spec.md", "transformation-record.md"))
    for condition in (f"N{n:02d}" for n in range(1, 9)):
        check(condition in handoff_text, f"Week 6 handoff missing {condition}.")
    check("accept with conditions" in handoff_text.lower(), "Allowed panel disposition missing.")

    text_files = [root / name for name in SUBMISSION_FILES if name.endswith((".md", ".yml"))]
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {path.relative_to(root)}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {path.relative_to(root)}.")
        if submission:
            check("REPLACE" not in text, f"Unresolved prompt in {path.relative_to(root)}.")
    check(not any((root / "figures").glob("*.jp*g")), "JPEG output is not allowed.")
    renderer_text = (root / "render_figures.py").read_text(encoding="utf-8").lower()
    for forbidden in ("projection=\"3d\"", "shadow=true", "gradient"):
        check(forbidden not in renderer_text, f"Unsupported chart configuration found: {forbidden}")
    check("font.size\": 9" in renderer_text and "fontsize=7" not in renderer_text, "Minimum configured type size changed.")

    with tempfile.TemporaryDirectory(prefix="fnd1-module06-validate-") as temp_dir:
        target = Path(temp_dir) / "release"
        render_figures.render(
            root / "data/missingness-profile.csv", root / "data/rates.csv",
            root / "data/denominator-registry.csv", root / "data/resolved-analytic-table.csv", target,
        )
        for name in (*TABLES, *ARTIFACTS, "render-report.json"):
            check((target / name).read_bytes() == (root / name).read_bytes(), f"Clean render changed {name}.")
        try:
            render_figures.render(
                root / "data/missingness-profile.csv", root / "data/rates.csv",
                root / "data/denominator-registry.csv", root / "data/resolved-analytic-table.csv", target,
            )
        except FileExistsError:
            check(True, "Existing target refused.")
        else:
            check(False, "Renderer did not refuse an existing target.")

    if not submission:
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.34.0", "Commons release changed.")
        check(release["decision"]["reference"] == "accept with conditions", "Reference disposition changed.")
        check(release["upstream"]["module_04_status"] == "accept with conditions", "Module 04 status changed.")
        check(release["upstream"]["module_05_status"] == "accept with conditions", "Module 05 status changed.")
    return checks, errors


def self_check() -> None:
    checks, errors = validate(MODULE_ROOT)
    assert not errors, errors
    with tempfile.TemporaryDirectory(prefix="fnd1-module06-invalid-") as temp_dir:
        fixture = Path(temp_dir) / "submission"
        shutil.copytree(MODULE_ROOT / "learner-template", fixture)
        incomplete_checks, incomplete_errors = validate(fixture, submission=True)
        assert incomplete_errors and any("Missing required file" in error for error in incomplete_errors)
        assert incomplete_checks > 0
    print(f"FND-1 Module 06 validator self-check passed: {checks} release checks and incomplete submission rejection.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=MODULE_ROOT)
    parser.add_argument("--submission", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    checks, errors = validate(args.root.resolve(), submission=args.submission)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(f"FND-1 Module 06 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-1 Module 06 validation passed: {checks} checks.")


if __name__ == "__main__":
    main()

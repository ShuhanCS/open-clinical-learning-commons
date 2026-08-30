"""Validate the FND-1 Module 05 descriptive release or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_descriptive


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUTS = {
    "variable-profile.csv": (17, 18, 3_116, "9d9bd1f8db71ebfdf3b775de13eb4450e30db9d52f8c71b2be0bf66918341f73"),
    "cross-tabs.csv": (12, 13, 2_304, "97628ab9fd557e8fb87203e98db4082c4d754c1d8966fdc8fc5b574167808f6f"),
    "rates.csv": (6, 13, 1_893, "2398b283e449d6f876a3a3ea123e7905c637ba222f56c6aa03882cfc158942f3"),
    "stratified-table.csv": (2, 18, 762, "a98abab5616039d8ded9e1c26845fb102b1dff33b6f5491dae38d42cde54a62b"),
    "denominator-registry.csv": (27, 12, 10_094, "e13bd0e1cf0716b912476fd81c7e4dd8bc827b2df468421aa2efc33f1f234be6"),
    "descriptive-checks.csv": (18, 5, 732, "9fb7970cda77bf1be25639265a762eab97a227106824b9f913f208000d99a1fa"),
}
SUBMISSION_FILES = (
    "VERSION", "README.md", "source-record.yml", "data-spec.md", "build_descriptive.py",
    "data/resolved-analytic-table.csv", "data/quality-rule-results.csv",
    "notebooks/05-descriptive-results.ipynb", "outputs/variable-profile.csv",
    "outputs/cross-tabs.csv", "outputs/rates.csv", "outputs/stratified-table.csv",
    "outputs/denominator-registry.csv", "outputs/descriptive-checks.csv",
    "interpretation-memo.md", "transformation-record.md", "reproducibility-check.md", "ai-use.md",
)
RELEASE_FILES = (
    "assessment.md", "instructor-notes.md", "release.json", "validate_descriptive.py",
    "outputs/build-report.json", "learner-template/README.md",
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
    source_path = root / "data/resolved-analytic-table.csv"
    quality_path = root / "data/quality-rule-results.csv"
    check(source_path.stat().st_size == build_descriptive.SOURCE_BYTES, "Source byte count changed.")
    check(build_descriptive.sha256(source_path) == build_descriptive.SOURCE_SHA256, "Source SHA-256 changed.")
    check(quality_path.stat().st_size == build_descriptive.QUALITY_BYTES, "Quality-results byte count changed.")
    check(build_descriptive.sha256(quality_path) == build_descriptive.QUALITY_SHA256, "Quality-results SHA-256 changed.")
    fields, source = read_csv(source_path)
    _, quality = read_csv(quality_path)
    check(len(source) == 374, "Source row count changed.")
    check(len(fields) == 29, "Source field count changed.")
    check(len({row["patient_id"] for row in source}) == 374, "Patient grain changed.")
    check(len({row["index_encounter_id"] for row in source}) == 374, "Index grain changed.")
    check(all(row["source_release"] == "synthea-csv-apr2020" for row in source), "Source release label changed.")
    check(all(row["cohort_definition_version"] == "0.1.0" for row in source), "Cohort version changed.")
    check(len(quality) == 28 and all(row["detection_status"] == "pass" for row in quality), "Upstream rule status changed.")
    check({row["issue_id"] for row in quality if row["issue_id"].startswith("N")} == {f"N{n:02d}" for n in range(1, 9)}, "Retained rule set changed.")

    actual: dict[str, list[dict[str, str]]] = {}
    for name, (row_count, field_count, byte_count, digest) in OUTPUTS.items():
        path = root / "outputs" / name
        output_fields, actual[name] = read_csv(path)
        check(len(actual[name]) == row_count, f"{name} row count changed.")
        check(len(output_fields) == field_count, f"{name} field count changed.")
        check(path.stat().st_size == byte_count, f"{name} byte count changed.")
        check(build_descriptive.sha256(path) == digest, f"{name} SHA-256 changed.")

    expected_profiles = build_descriptive.profile_rows(source)
    expected_cross_tabs = build_descriptive.cross_tab_rows(source)
    expected_rates = build_descriptive.rate_rows(source)
    expected_strata = build_descriptive.stratum_rows(source)
    expected_registry = build_descriptive.registry_rows(expected_profiles, expected_cross_tabs, expected_rates, expected_strata)
    expected_checks = build_descriptive.check_rows(source, quality, expected_profiles, expected_cross_tabs, expected_rates, expected_strata, expected_registry)
    expected = {
        "variable-profile.csv": expected_profiles, "cross-tabs.csv": expected_cross_tabs,
        "rates.csv": expected_rates, "stratified-table.csv": expected_strata,
        "denominator-registry.csv": expected_registry, "descriptive-checks.csv": expected_checks,
    }
    for name, rows in expected.items():
        for row_number, (actual_row, expected_row) in enumerate(zip(actual[name], rows, strict=True), start=1):
            for field, value in expected_row.items():
                check(actual_row[field] == str(value), f"{name} row {row_number} changed: {field}")

    profiles = actual["variable-profile.csv"]
    cross_tabs = actual["cross-tabs.csv"]
    rates = actual["rates.csv"]
    strata = actual["stratified-table.csv"]
    registry = actual["denominator-registry.csv"]
    release_checks = actual["descriptive-checks.csv"]
    check([row["result_id"] for row in profiles] == [f"VP{n:02d}" for n in range(1, 18)], "Profile result order changed.")
    check(all(int(row["available_n"]) + int(row["missing_n"]) == 374 for row in profiles), "Profile counts do not reconcile.")
    for result_id in ("CT01", "CT02"):
        rows = [row for row in cross_tabs if row["result_id"] == result_id]
        check(sum(int(row["n"]) for row in rows) == 374, f"{result_id} does not conserve the cohort.")
        for row_category in {row["row_category"] for row in rows}:
            row_cells = [row for row in rows if row["row_category"] == row_category]
            check(sum(int(row["n"]) for row in row_cells) == int(row_cells[0]["row_denominator"]), f"{result_id} row count does not reconcile: {row_category}")
            check(abs(sum(float(row["row_percent"]) for row in row_cells) - 100) < 0.00001, f"{result_id} row percent does not reconcile: {row_category}")
    check([int(row["numerator"]) for row in rates] == [111, 92, 4, 15, 36, 8], "Rate numerators changed.")
    check(all(int(row["denominator"]) == 374 for row in rates), "Rate denominator changed.")
    check(sum(int(row["n"]) for row in strata) == 374, "Stratum counts do not reconcile.")
    check(len({row["result_id"] for row in registry}) == 27, "Registry IDs are not unique.")
    conditions = {condition for row in registry for condition in row["retained_conditions"].split("|") if condition}
    check(conditions == {f"N{n:02d}" for n in range(1, 9)}, "Registry condition coverage changed.")
    check(all(row["status"] == "pass" for row in release_checks), "A descriptive release check failed.")

    notebook = json.loads((root / "notebooks/05-descriptive-results.ipynb").read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    ids = [cell.get("id") for cell in cells]
    notebook_text = "\n".join("".join(cell.get("source", [])) for cell in cells)
    check(notebook.get("nbformat") == 4, "Notebook must use nbformat 4.")
    check(len(cells) == 9, "Notebook cell count changed.")
    check(all(ids) and len(ids) == len(set(ids)), "Notebook cell IDs are missing or duplicated.")
    for phrase in ("Verify source and grain", "Compare summaries and denominators", "Reconcile cross-tabs, rates, and strata", "Module 06 handoff decision"):
        check(phrase in notebook_text, f"Notebook section missing: {phrase}")

    text_files = [root / name for name in SUBMISSION_FILES if name.endswith((".md", ".yml"))]
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {path.name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {path.name}.")
        if submission:
            check("REPLACE" not in text, f"Unresolved prompt in {path.name}.")
    memo = (root / "interpretation-memo.md").read_text(encoding="utf-8")
    for result_id in ("VP02", "VP09", "VP14", "CT01", "RT05", "ST01", "ST02"):
        check(result_id in memo, f"Interpretation memo does not cite {result_id}.")
    check("accept with conditions" in memo.lower(), "Allowed disposition missing from memo.")

    if submission:
        check("REPLACE" not in (root / "notebooks/05-descriptive-results.ipynb").read_text(encoding="utf-8"), "Unresolved notebook prompt.")
    else:
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.33.0", "Commons release changed.")
        check(release["decision"]["reference"] == "accept with conditions", "Reference disposition changed.")
    return checks, errors


def self_check() -> None:
    checks, errors = validate(MODULE_ROOT)
    assert not errors, errors
    with tempfile.TemporaryDirectory(prefix="fnd1-module05-invalid-") as temp_dir:
        fixture = Path(temp_dir) / "submission"
        shutil.copytree(MODULE_ROOT / "learner-template", fixture)
        incomplete_checks, incomplete_errors = validate(fixture, submission=True)
        assert incomplete_errors and any("Missing required file" in error for error in incomplete_errors)
        assert incomplete_checks > 0
    print(f"FND-1 Module 05 validator self-check passed: {checks} release checks and incomplete submission rejection.")


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
        raise SystemExit(f"FND-1 Module 05 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-1 Module 05 validation passed: {checks} checks.")


if __name__ == "__main__":
    main()

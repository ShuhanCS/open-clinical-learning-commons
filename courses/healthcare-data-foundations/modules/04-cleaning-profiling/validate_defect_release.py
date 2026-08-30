"""Validate the FND-1 Module 04 data-quality release or learner submission."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sqlite3
import tempfile
from collections import Counter
from pathlib import Path

import profile_quality


MODULE_ROOT = Path(__file__).resolve().parent
DATA_FILES = {
    "accepted-analytic-table.csv": (374, 29, 121_787, "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"),
    "defective-analytic-table.csv": (379, 29, 123_211, "7800c1d24093b93ce40634afe652e574a1ed2775eba8a742c0bd00bf3596a02d"),
    "defect-manifest.csv": (68, 8, 7_230, "72abd0330db86df49476512740a6d47222426d40b7e2a5f94b0cedafea38aa46"),
    "quality-rules.csv": (28, 13, 8_785, "aa2f6b58e93ec156c3f99e2159817c8c6cb8cf8f60d650dfae5e2d01a3175e0d"),
}
OUTPUT_FILES = {
    "quality-profile.csv": (29, 14, 2_257, "0cefe9d28feedc9a7f53b4bae45e84f5a2c06f5f94f743b21faf26a9083266fc"),
    "missingness-profile.csv": (29, 12, 4_362, "46e9c4dd268db223fac3cd0f01e65e050a3d44f6a28e0babcfb7bd5b552b5ba5"),
    "quality-rule-results.csv": (28, 11, 3_607, "c301cd46d6058329d72cc2b71649f5bb1ccf9fbff43f6c97e8b2fc008f791c06"),
    "quality-risk-log.csv": (28, 12, 7_860, "3788abf4f8abd0bd9a294380d6eca73815fa209816a57dfcc00df40a93225057"),
    "resolution-log.csv": (28, 7, 4_468, "48d4c7259840c16f5667eb23191885787bd056680e0bae7bba4b16120a271c51"),
    "resolved-analytic-table.csv": (374, 29, 121_787, "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"),
}
SUBMISSION_FILES = (
    "VERSION", "README.md", "data-spec.md", "data-dictionary.csv",
    "data/accepted-analytic-table.csv", "data/defective-analytic-table.csv",
    "data/defect-manifest.csv", "data/quality-rules.csv", "data/fnd1-quality-defects.sqlite",
    "notebooks/04-data-quality.ipynb", "outputs/quality-profile.csv",
    "outputs/missingness-profile.csv", "outputs/quality-rule-results.csv",
    "outputs/quality-risk-log.csv", "outputs/resolution-log.csv",
    "outputs/resolved-analytic-table.csv", "stop-fix-proceed.md",
    "transformation-record.md", "reproducibility-check.md", "ai-use.md",
)
RELEASE_ONLY_FILES = (
    "build_defect_release.py", "profile_quality.py", "validate_defect_release.py",
    "assessment.md", "instructor-notes.md", "release.json", "data/build-report.json",
    "outputs/profile-report.json", "learner-template/README.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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

    required = SUBMISSION_FILES + (() if submission else RELEASE_ONLY_FILES)
    for name in required:
        check((root / name).is_file(), f"Missing required file: {name}")
    if errors:
        return checks, errors

    check((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "VERSION must be 0.1.0.")
    dictionary_fields, dictionary = read_csv(root / "data-dictionary.csv")
    check(len(dictionary) == 29, "Data dictionary must have 29 rows.")
    check(dictionary_fields == ["position", "field_name", "timing", "data_type", "nullable", "allowed_values_or_rule", "description"], "Data dictionary headers changed.")

    loaded: dict[str, tuple[list[str], list[dict[str, str]]]] = {}
    for name, (rows, fields, size, digest) in DATA_FILES.items():
        path = root / "data" / name
        loaded[name] = read_csv(path)
        check(len(loaded[name][1]) == rows, f"{name} row count changed.")
        check(len(loaded[name][0]) == fields, f"{name} field count changed.")
        check(path.stat().st_size == size, f"{name} byte count changed.")
        check(sha256(path) == digest, f"{name} SHA-256 changed.")

    accepted_fields, accepted = loaded["accepted-analytic-table.csv"]
    defective_fields, defective = loaded["defective-analytic-table.csv"]
    _, manifest = loaded["defect-manifest.csv"]
    _, rules = loaded["quality-rules.csv"]
    check(accepted_fields == defective_fields, "Accepted and defective fields differ.")
    check([row["field_name"] for row in dictionary] == accepted_fields, "Dictionary order differs from analytic table.")
    check(len({row["patient_id"] for row in accepted}) == 374, "Accepted patient grain changed.")
    check(len({row["index_encounter_id"] for row in accepted}) == 374, "Accepted index grain changed.")
    check(len({row["patient_id"] for row in defective}) == 374, "Defective distinct-patient count changed.")
    duplicate_count = sum(count - 1 for count in Counter(tuple(row[field] for field in defective_fields) for row in defective).values())
    check(duplicate_count == 5, "Defective exact-duplicate count changed.")
    check(len({row["case_id"] for row in manifest}) == 56, "Manifest case count changed.")
    check({row["issue_id"] for row in manifest} == {f"D{number:02d}" for number in range(1, 21)}, "Manifest defect families changed.")
    check({row["issue_id"] for row in rules} == {f"D{number:02d}" for number in range(1, 21)} | {f"N{number:02d}" for number in range(1, 9)}, "Rule registry changed.")

    accepted_by_patient = {row["patient_id"]: row for row in accepted}
    defective_by_patient = {row["patient_id"]: row for row in defective}
    for change in manifest:
        check(change["patient_id"] in accepted_by_patient, f"Manifest patient missing upstream: {change['change_id']}")
        if change["operation"] == "append_exact_duplicate":
            count = sum(row == accepted_by_patient[change["patient_id"]] for row in defective)
            check(count == 2, f"Duplicate case does not append one exact row: {change['change_id']}")
        else:
            field = change["field_name"]
            check(accepted_by_patient[change["patient_id"]][field] == change["original_value"], f"Manifest original mismatch: {change['change_id']}")
            check(defective_by_patient[change["patient_id"]][field] == change["defect_value"], f"Manifest defect mismatch: {change['change_id']}")

    for rule in rules:
        observed = profile_quality.detect(rule["issue_id"], accepted, defective, accepted_fields)
        check(observed == int(rule["expected_count"]), f"Rule count changed: {rule['issue_id']}")

    database = root / "data" / "fnd1-quality-defects.sqlite"
    check(database.stat().st_size == 385_024, "SQLite byte count changed.")
    check(sha256(database) == "3b9cbf4ba7920f85a8af524902f2e7d35b3e837e5dd6b94deb4f20a156644275", "SQLite SHA-256 changed.")
    connection = sqlite3.connect(f"file:{database.as_posix()}?mode=ro", uri=True)
    try:
        check(connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok", "SQLite integrity check failed.")
        for table, expected in (("accepted_analytic_table", 374), ("defective_analytic_table", 379), ("defect_manifest", 68), ("quality_rules", 28), ("release_metadata", 4)):
            check(connection.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0] == expected, f"SQLite {table} count changed.")
        check(connection.execute("PRAGMA user_version").fetchone()[0] == 1, "SQLite user_version changed.")
    finally:
        connection.close()

    output_rows: dict[str, list[dict[str, str]]] = {}
    for name, (rows, fields, size, digest) in OUTPUT_FILES.items():
        path = root / "outputs" / name
        output_fields, output_rows[name] = read_csv(path)
        check(len(output_rows[name]) == rows, f"{name} row count changed.")
        check(len(output_fields) == fields, f"{name} field count changed.")
        check(path.stat().st_size == size, f"{name} byte count changed.")
        check(sha256(path) == digest, f"{name} SHA-256 changed.")
    result_rows = output_rows["quality-rule-results.csv"]
    check(all(row["detection_status"] == "pass" for row in result_rows), "Not all quality-rule results pass.")
    issue_sets = [set(row["issue_id"] for row in output_rows[name]) for name in ("quality-rule-results.csv", "quality-risk-log.csv", "resolution-log.csv")]
    check(issue_sets[0] == issue_sets[1] == issue_sets[2], "Rule, risk, and resolution issue IDs differ.")
    check((root / "outputs/resolved-analytic-table.csv").read_bytes() == (root / "data/accepted-analytic-table.csv").read_bytes(), "Resolved table differs from accepted source.")
    check(sum(row["disposition"] == "correct" for row in output_rows["resolution-log.csv"]) == 20, "Seeded resolution count changed.")
    check(sum(row["disposition"] == "retain with condition" for row in output_rows["resolution-log.csv"]) == 8, "Retained-condition count changed.")

    notebook = json.loads((root / "notebooks/04-data-quality.ipynb").read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    ids = [cell.get("id") for cell in cells]
    notebook_text = "\n".join("".join(cell.get("source", [])) for cell in cells)
    check(notebook.get("nbformat") == 4, "Notebook must use nbformat 4.")
    check(len(cells) == 9, "Notebook cell count changed.")
    check(all(ids) and len(ids) == len(set(ids)), "Notebook cell IDs are missing or duplicated.")
    for phrase in ("Verify source and grain", "Inspect missingness and rules", "Interpret risk and resolution", "Readiness decision"):
        check(phrase in notebook_text, f"Notebook section missing: {phrase}")

    markdown_files = [root / name for name in SUBMISSION_FILES if name.endswith(".md")]
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {path.name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {path.name}.")
        if submission:
            check("[REPLACE" not in text, f"Unresolved learner prompt in {path.name}.")
    if submission:
        check("[REPLACE" not in (root / "notebooks/04-data-quality.ipynb").read_text(encoding="utf-8"), "Unresolved learner prompt in notebook.")
        decision_text = (root / "stop-fix-proceed.md").read_text(encoding="utf-8").lower()
        check(any(label in decision_text for label in ("stop", "fix", "proceed", "proceed with conditions")), "Submission decision is missing.")
    else:
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.32.0", "Commons release changed.")
        check(release["decision"]["reference_final"] == "proceed with conditions", "Reference decision changed.")

    return checks, errors


def self_check() -> None:
    checks, errors = validate(MODULE_ROOT)
    assert not errors, errors
    with tempfile.TemporaryDirectory(prefix="fnd1-module04-invalid-") as temp_dir:
        fixture = Path(temp_dir) / "submission"
        shutil.copytree(MODULE_ROOT / "learner-template", fixture)
        incomplete_checks, incomplete_errors = validate(fixture, submission=True)
        assert incomplete_errors and any("Missing required file" in error for error in incomplete_errors)
        assert incomplete_checks > 0
    print(f"FND-1 Module 04 validator self-check passed: {checks} release checks and incomplete submission rejection.")


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
        raise SystemExit(f"FND-1 Module 04 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-1 Module 04 validation passed: {checks} checks.")


if __name__ == "__main__":
    main()

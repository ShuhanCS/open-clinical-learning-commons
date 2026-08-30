"""Profile the FND-1 Module 04 defect layer and write the reference quality evidence."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path

import build_defect_release


MODULE_ROOT = Path(__file__).resolve().parent
DATA_ROOT = MODULE_ROOT / "data"
DICTIONARY = MODULE_ROOT.parents[0] / "03-cohorts-analytic-tables" / "data-dictionary.csv"
NUMERIC_FIELDS = {
    "age_at_index", "prior_365d_encounter_count", "prior_365d_acute_count",
    "prior_365d_condition_count", "prior_365d_medication_count",
    "next_30d_days_after_index_stop", "acute_return_90d", "death_90d", "followup_90d_complete",
}
ALLOWED_MISSING = {
    "death_date", "index_description", "index_reason_code", "index_reason_description",
    "next_30d_encounter_id", "next_30d_start", "next_30d_days_after_index_stop",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_timestamp(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def detect(issue_id: str, accepted: list[dict[str, str]], defective: list[dict[str, str]], fields: list[str]) -> int:
    if issue_id == "D01":
        counts = Counter(tuple(row[field] for field in fields) for row in defective)
        return sum(count - 1 for count in counts.values())
    if issue_id == "D02": return sum(not row["index_encounter_id"] for row in defective)
    if issue_id == "D03": return sum(int(row["age_at_index"]) < 18 for row in defective)
    if issue_id == "D04": return sum(int(row["age_at_index"]) > 120 for row in defective)
    if issue_id == "D05": return sum(parse_timestamp(row["index_start"]) is None for row in defective)
    if issue_id == "D06":
        return sum(bool(parse_timestamp(row["index_start"]) and parse_timestamp(row["index_stop"]) and parse_timestamp(row["index_stop"]) < parse_timestamp(row["index_start"])) for row in defective)
    if issue_id == "D07": return sum(row["index_class"].lower() not in {"emergency", "inpatient"} for row in defective)
    if issue_id == "D08": return sum(row["index_class"] != row["index_class"].lower() and row["index_class"].lower() in {"emergency", "inpatient"} for row in defective)
    if issue_id == "D09": return sum(int(row["prior_365d_encounter_count"]) < 0 for row in defective)
    if issue_id == "D10": return sum(int(row["prior_365d_encounter_count"]) >= 0 and int(row["prior_365d_acute_count"]) > int(row["prior_365d_encounter_count"]) for row in defective)
    if issue_id == "D11": return sum(not row["gender"] for row in defective)
    if issue_id == "D12": return sum(bool(row["gender"]) and row["gender"] not in {"M", "F"} for row in defective)
    if issue_id == "D13": return sum(row["next_30d_state"] == "No encounter recorded" and any(row[field] for field in ("next_30d_encounter_id", "next_30d_start", "next_30d_days_after_index_stop")) for row in defective)
    if issue_id == "D14": return sum(row["next_30d_state"] != "No encounter recorded" and any(not row[field] for field in ("next_30d_encounter_id", "next_30d_start", "next_30d_days_after_index_stop")) for row in defective)
    if issue_id == "D15": return sum(bool(row["next_30d_days_after_index_stop"]) and float(row["next_30d_days_after_index_stop"]) <= 0 for row in defective)
    if issue_id == "D16": return sum(bool(row["next_30d_days_after_index_stop"]) and float(row["next_30d_days_after_index_stop"]) > 30 for row in defective)
    if issue_id == "D17": return sum(row["acute_return_90d"] not in {"0", "1"} for row in defective)
    if issue_id == "D18": return sum(row["death_90d"] == "1" and row["endpoint_90d"] != "Death" for row in defective)
    if issue_id == "D19": return sum(row["source_release"] != "synthea-csv-apr2020" for row in defective)
    if issue_id == "D20": return sum(row["cohort_definition_version"] != "0.1.0" for row in defective)
    if issue_id == "N01": return sum(not row["death_date"] for row in accepted)
    if issue_id == "N02": return sum(not row["index_reason_code"] and not row["index_reason_description"] for row in accepted)
    if issue_id == "N03": return sum(row["next_30d_state"] == "No encounter recorded" and all(not row[field] for field in ("next_30d_encounter_id", "next_30d_start", "next_30d_days_after_index_stop")) for row in accepted)
    if issue_id == "N04": return sum(int(row["age_at_index"]) >= 100 for row in accepted)
    if issue_id == "N05": return sum(int(row["prior_365d_encounter_count"]) > 100 for row in accepted)
    if issue_id == "N06": return sum(int(row["prior_365d_medication_count"]) > 100 for row in accepted)
    if issue_id == "N07":
        counts = Counter(row["race"] for row in accepted)
        return sum(count for count in counts.values() if count < 10)
    if issue_id == "N08": return sum(row["next_30d_state"] == "Urgent care" or row["endpoint_90d"] == "Death" for row in accepted)
    raise ValueError(f"Unknown quality rule: {issue_id}")


def profile(data_root: Path, dictionary_path: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    fields, accepted = read_csv(data_root / "accepted-analytic-table.csv")
    defect_fields, defective = read_csv(data_root / "defective-analytic-table.csv")
    _, manifest = read_csv(data_root / "defect-manifest.csv")
    _, rules = read_csv(data_root / "quality-rules.csv")
    _, dictionary = read_csv(dictionary_path)
    if fields != defect_fields or len(dictionary) != len(fields):
        raise ValueError("Source, defect, or dictionary field contract changed.")

    target.mkdir(parents=True)
    result_rows = []
    observed: dict[str, int] = {}
    for rule in rules:
        count = detect(rule["issue_id"], accepted, defective, fields)
        observed[rule["issue_id"]] = count
        result_rows.append({
            "issue_id": rule["issue_id"], "category": rule["category"], "table_scope": rule["table_scope"],
            "field_name": rule["field_name"], "observed_count": count, "expected_count": rule["expected_count"],
            "affected_denominator": len(defective) if rule["table_scope"] == "defective" else len(accepted),
            "severity": rule["severity"], "blocking": rule["blocking"],
            "detection_status": "pass" if count == int(rule["expected_count"]) else "fail",
            "interpretation": rule["teaching_purpose"],
        })
    if any(row["detection_status"] != "pass" for row in result_rows):
        raise ValueError("One or more quality-rule counts changed.")
    write_csv(target / "quality-rule-results.csv", list(result_rows[0]), result_rows)

    dictionary_by_field = {row["field_name"]: row for row in dictionary}
    changes = Counter(row["field_name"] for row in manifest)
    profile_rows = []
    missing_rows = []
    for field in fields:
        values = [row[field] for row in defective]
        present = [value for value in values if value != ""]
        accepted_missing = sum(row[field] == "" for row in accepted)
        defective_missing = len(values) - len(present)
        issue_ids = [row["issue_id"] for row in rules if field in row["field_name"].split("|")]
        numeric = []
        if field in NUMERIC_FIELDS:
            try:
                numeric = [float(value) for value in present]
            except ValueError:
                numeric = []
        failing = [issue for issue in issue_ids if issue.startswith("D") and observed[issue] > 0]
        natural = [issue for issue in issue_ids if issue.startswith("N") and observed[issue] > 0]
        profile_rows.append({
            "position": dictionary_by_field[field]["position"], "field_name": field,
            "timing": dictionary_by_field[field]["timing"], "declared_type": dictionary_by_field[field]["data_type"],
            "row_count": len(defective), "non_missing_count": len(present), "missing_count": defective_missing,
            "missing_percent": f"{100 * defective_missing / len(defective):.6f}",
            "distinct_non_missing": len(set(present)),
            "minimum": f"{min(numeric):g}" if numeric else "", "maximum": f"{max(numeric):g}" if numeric else "",
            "seeded_manifest_changes": changes[field] + (5 if field == "patient_id" else 0),
            "detected_issue_ids": "|".join(issue_ids),
            "quality_status": "fail" if failing else ("review" if natural or defective_missing else "pass"),
        })
        missing_rows.append({
            "position": dictionary_by_field[field]["position"], "field_name": field,
            "timing": dictionary_by_field[field]["timing"], "accepted_rows": len(accepted),
            "accepted_missing": accepted_missing, "accepted_missing_percent": f"{100 * accepted_missing / len(accepted):.6f}",
            "defective_rows": len(defective), "defective_missing": defective_missing,
            "defective_missing_percent": f"{100 * defective_missing / len(defective):.6f}",
            "delta_missing": defective_missing - accepted_missing,
            "structurally_allowed": "yes" if field in ALLOWED_MISSING else "no",
            "interpretation": "Interpret with the field and state contract; do not convert blanks to zero." if field in ALLOWED_MISSING else "A seeded blank in this required field must be resolved from the accepted source.",
        })
    write_csv(target / "quality-profile.csv", list(profile_rows[0]), profile_rows)
    write_csv(target / "missingness-profile.csv", list(missing_rows[0]), missing_rows)

    risk_rows = []
    resolution_rows = []
    for rule in rules:
        issue = rule["issue_id"]
        is_defect = issue.startswith("D")
        risk_rows.append({
            "issue_id": issue,
            "table_name": "defective_analytic_table" if is_defect else "accepted_analytic_table",
            "field_name": rule["field_name"], "rule": rule["rule"], "observed_count": observed[issue],
            "affected_denominator": len(defective) if is_defect else len(accepted), "severity": rule["severity"],
            "likely_cause": rule["likely_cause"], "analytic_consequence": rule["analytic_consequence"],
            "proposed_response": rule["expected_response"], "owner": rule["owner"],
            "status": "open seeded issue" if is_defect else "documented condition",
        })
        resolution_rows.append({
            "issue_id": issue, "disposition": "correct" if is_defect else "retain with condition",
            "action": rule["expected_response"], "rows_affected": observed[issue], "owner": rule["owner"],
            "verification": "Resolved table matches accepted release byte for byte." if is_defect else "Accepted source value remains unchanged and condition remains visible.",
            "status": "resolved" if is_defect else "retained condition",
        })
    write_csv(target / "quality-risk-log.csv", list(risk_rows[0]), risk_rows)
    write_csv(target / "resolution-log.csv", list(resolution_rows[0]), resolution_rows)
    shutil.copy2(data_root / "accepted-analytic-table.csv", target / "resolved-analytic-table.csv")

    report = {
        "status": "pass",
        "version": "0.1.0",
        "profiles": {"quality_rows": len(profile_rows), "missingness_rows": len(missing_rows)},
        "rules": {"rows": len(result_rows), "passing": sum(row["detection_status"] == "pass" for row in result_rows)},
        "logs": {"risk_rows": len(risk_rows), "resolution_rows": len(resolution_rows)},
        "resolved": {
            "rows": len(accepted), "fields": len(fields),
            "bytes": (target / "resolved-analytic-table.csv").stat().st_size,
            "sha256": build_defect_release.sha256(target / "resolved-analytic-table.csv"),
        },
    }
    for name in ("quality-profile.csv", "missingness-profile.csv", "quality-rule-results.csv", "quality-risk-log.csv", "resolution-log.csv"):
        path = target / name
        report.setdefault("outputs", {})[name] = {"bytes": path.stat().st_size, "sha256": build_defect_release.sha256(path)}
    with (target / "profile-report.json").open("w", encoding="utf-8", newline="") as handle:
        handle.write(json.dumps(report, indent=2) + "\n")
    return report


def self_check() -> None:
    assert parse_timestamp("2019-01-01T00:00:00Z") is not None
    assert parse_timestamp("not-a-timestamp") is None
    with tempfile.TemporaryDirectory(prefix="fnd1-module04-profile-") as temp_dir:
        target = Path(temp_dir) / "outputs"
        report = profile(DATA_ROOT, DICTIONARY, target)
        assert report["rules"]["passing"] == 28
        try:
            profile(DATA_ROOT, DICTIONARY, target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Profiler did not protect an existing target.")
    print("FND-1 Module 04 profiler self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DATA_ROOT)
    parser.add_argument("--dictionary", type=Path, default=DICTIONARY)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.target:
        parser.error("--target is required")
    try:
        report = profile(args.data_dir.resolve(), args.dictionary.resolve(), args.target.resolve())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Profiling failed: {exc}\n")
    print(
        "FND-1 Module 04 quality profiling passed: "
        f"{report['rules']['passing']} rules and {report['resolved']['rows']} resolved rows."
    )


if __name__ == "__main__":
    main()

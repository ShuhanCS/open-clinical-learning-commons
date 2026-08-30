#!/usr/bin/env python3
"""Validate the DA-730 Module 11 synthetic transition releases."""

from __future__ import annotations

import csv
import hashlib
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FILES = {
    "patients": DATA / "synthea_patients_transition_source_2020.csv",
    "encounters": DATA / "synthea_encounters_transition_source_2020.csv",
    "cohort": DATA / "synthea_acute_transition_cohort_2020.csv",
    "edges": DATA / "synthea_transition_edges_2020.csv",
}
EXPECTED = {
    "patients": (1171, 6, "a208fe4ff6fc9dc5cee4a201043a2f059943b8c058fdb191e19b0f9ffbb821bf"),
    "encounters": (53346, 9, "00298bf68f89dee9734cf133c516ad6b7efe95c8cd15a9458e7fb09c1dca56ce"),
    "cohort": (374, 25, "b3f1cf69a54fd2f38dfe6debfd009ebb1c7d2b1ef7b42d7b35c989a9f068f3ca"),
    "edges": (15, 9, "13ee29b6fb6e16235cb3b9509d72f95a6b478024a7322d011bb04a4e8064fa8d"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def main() -> None:
    passed = 0

    def check(condition: bool, message: str) -> None:
        nonlocal passed
        if not condition:
            raise AssertionError(message)
        passed += 1

    loaded: dict[str, tuple[list[str], list[dict[str, str]]]] = {}
    for name, path in FILES.items():
        check(path.exists(), f"Missing {name} release")
        fields, rows = read_csv(path)
        loaded[name] = fields, rows
        expected_rows, expected_columns, expected_hash = EXPECTED[name]
        check(len(rows) == expected_rows, f"Unexpected {name} row count")
        check(len(fields) == expected_columns, f"Unexpected {name} column count")
        check(sha256(path) == expected_hash, f"Unexpected {name} SHA-256")

    patient_fields, patients = loaded["patients"]
    encounter_fields, encounters = loaded["encounters"]
    cohort_fields, cohort = loaded["cohort"]
    _, edges = loaded["edges"]
    patient_ids = {row["patient_id"] for row in patients}
    cohort_ids = [row["patient_id"] for row in cohort]

    check(len(patient_ids) == len(patients), "Patient IDs must be unique")
    check(not ({"first", "last", "ssn", "address", "passport"} & {field.lower() for field in patient_fields}), "Direct identifier-like fields were retained")
    check(all(row["patient_id"] in patient_ids for row in encounters), "Encounter patient is absent from patient release")
    check(all(row["patient_id"] in patient_ids for row in cohort), "Cohort patient is absent from patient release")
    check(len(set(cohort_ids)) == len(cohort_ids), "Cohort must contain one index event per patient")
    check(set(row["encounter_class"] for row in encounters) == {"ambulatory", "emergency", "inpatient", "outpatient", "urgentcare", "wellness"}, "Encounter classes changed")
    check(all(row["start"].endswith("Z") and row["stop"].endswith("Z") for row in encounters), "Encounter timestamps must be UTC")
    check(all(datetime.fromisoformat(row["stop"].replace("Z", "+00:00")) >= datetime.fromisoformat(row["start"].replace("Z", "+00:00")) for row in encounters), "Encounter duration is negative")
    check(all(int(row["age_at_index"]) >= 18 for row in cohort), "Cohort includes a minor")
    check(all("2015-01-01" <= row["index_start"][:10] <= "2019-12-31" for row in cohort), "Index date is outside the declared window")
    check(set(row["index_class"] for row in cohort) == {"Emergency", "Inpatient"}, "Index classes changed")
    check(set(row["next_30d_state"] for row in cohort) == {"Scheduled care", "Urgent care", "Acute return", "No encounter recorded"}, "Next-state vocabulary changed")
    check(set(row["endpoint_90d"] for row in cohort) == {"No acute return within 90 days", "Acute return within 90 days", "Death within 90 days"}, "Endpoint vocabulary changed")
    check(all(row["death_90d"] == "no" or row["endpoint_90d"] == "Death within 90 days" for row in cohort), "Death endpoint precedence changed")
    check(all(row["next_30d_encounter_id"] or row["next_30d_state"] == "No encounter recorded" for row in cohort), "Missing next encounter ID")
    check(all((not row["next_30d_encounter_id"]) or 0 < float(row["next_30d_days_after_index_stop"]) <= 30 for row in cohort), "Next encounter falls outside 30 days")
    check(all(row["transition_path"] == f"{row['index_class']} -> {row['next_30d_state']}" for row in cohort), "Transition path label changed")

    index_counts = Counter(row["index_class"] for row in cohort)
    next_counts = Counter(row["next_30d_state"] for row in cohort)
    endpoint_counts = Counter(row["endpoint_90d"] for row in cohort)
    path_counts = Counter(row["transition_path"] for row in cohort)
    check(index_counts == {"Emergency": 314, "Inpatient": 60}, "Index counts changed")
    check(next_counts == {"No encounter recorded": 263, "Scheduled care": 92, "Acute return": 15, "Urgent care": 4}, "Next-state counts changed")
    check(endpoint_counts == {"No acute return within 90 days": 330, "Acute return within 90 days": 36, "Death within 90 days": 8}, "Endpoint counts changed")
    check(sum(row["acute_return_90d"] == "yes" for row in cohort) == 36, "Acute-return count changed")
    check(sum(row["death_90d"] == "yes" for row in cohort) == 8, "Death count changed")
    check(all(int(row["path_count"]) == path_counts[row["transition_path"]] for row in cohort), "Repeated path count changed")
    check(all(row["path_count"] == row["path_denominator"] for row in cohort), "Path denominator changed")
    check(set(row["cohort_acute_return_pct"] for row in cohort) == {"9.6"}, "Overall acute-return percentage changed")
    check(sum(row["priority_screen"] == "yes" for row in cohort) == 38, "Priority-screen patient count changed")
    check({row["transition_path"] for row in cohort if row["priority_screen"] == "yes"} == {"Inpatient -> No encounter recorded"}, "Priority path changed")
    check(path_counts["Emergency -> No encounter recorded"] == 225, "Largest path count changed")
    check(path_counts["Inpatient -> No encounter recorded"] == 38, "Reference audit path count changed")
    check({row["path_acute_return_pct"] for row in cohort if row["transition_path"] == "Inpatient -> No encounter recorded"} == {"15.8"}, "Reference path rate changed")

    check(sum(int(row["patient_count"]) for row in edges if row["stage_from"] == "Index encounter") == len(cohort), "First edge stage does not conserve patients")
    check(sum(int(row["patient_count"]) for row in edges if row["stage_from"] == "Next encounter within 30 days") == len(cohort), "Second edge stage does not conserve patients")
    check(set(row["cohort_denominator"] for row in edges) == {"374"}, "Edge cohort denominator changed")
    check(all(int(row["patient_count"]) <= int(row["node_from_denominator"]) for row in edges), "Edge exceeds source node")
    for stage in {row["stage_from"] for row in edges}:
        stage_rows = [row for row in edges if row["stage_from"] == stage]
        for node in {row["node_from"] for row in stage_rows}:
            node_rows = [row for row in stage_rows if row["node_from"] == node]
            check(sum(int(row["patient_count"]) for row in node_rows) == int(node_rows[0]["node_from_denominator"]), f"Edges do not conserve node {node}")

    check(all(date.fromisoformat(row["birth_date"]) < date.fromisoformat(row["index_start"][:10]) for row in cohort), "Birth occurs after index")
    check(all(row["sex"] in {"M", "F"} for row in patients), "Unexpected sex value")
    check(all(row["race"] for row in patients), "Missing race value")
    check(all(row["ethnicity"] for row in patients), "Missing ethnicity value")
    check(all(field in cohort_fields for field in ("path_denominator", "cohort_acute_return_pct", "priority_screen")), "Decision fields are missing")
    check(len({row["encounter_id"] for row in encounters}) == len(encounters), "Encounter IDs must be unique")
    check(len(edges) == len({(row["stage_from"], row["node_from"], row["stage_to"], row["node_to"]) for row in edges}), "Duplicate edge row")
    check(sum(path_counts.values()) == len(cohort), "Paths do not conserve cohort")

    print(f"Module 11 synthetic transition data passed {passed} checks.")


if __name__ == "__main__":
    main()

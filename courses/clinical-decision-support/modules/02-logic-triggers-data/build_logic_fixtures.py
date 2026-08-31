"""Build or verify the deterministic APP-4 Module 02 rule fixtures."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data" / "synthetic-release" / "fhir" / "Patient.ndjson.gz"
TARGET = ROOT / "data" / "commons"
RELEASE_ID = "CGH-GIM-01-SYNTHETIC-2026-08-31-v1"
DECISION_TIME = "2026-08-31T15:00:00Z"
FIELDS = [
    "case_id", "patient_id", "encounter_id", "request_id", "service_id", "hook",
    "hook_version", "user_id", "decision_time", "input_state", "diabetes_state",
    "prior_hba1c_days", "terminology_state", "unit_state", "score_fixture",
    "threshold_fixture", "duplicate_of", "response_transport", "expected_result",
    "expected_reason", "condition_class",
]
CASES = [
    ("C01", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "0.19", "0.20", "", "delivered", "no_card", "below_mock_threshold", "normal negative"),
    ("C02", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "0.20", "0.20", "", "delivered", "candidate_card", "at_or_above_mock_threshold", "mock threshold boundary"),
    ("C03", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "candidate_card", "at_or_above_mock_threshold", "normal positive"),
    ("C04", "CGH-GIM-01", "patient-view", "1.0", "missing", "absent", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "required_input_missing", "missing"),
    ("C05", "CGH-GIM-01", "patient-view", "1.0", "stale", "absent", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "required_input_stale", "stale"),
    ("C06", "CGH-GIM-01", "patient-view", "1.0", "inconsistent", "unknown", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "input_inconsistent", "inconsistent"),
    ("C07", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "0.42", "0.20", "C03", "delivered", "no_card", "duplicate_request", "duplicate"),
    ("C08", "CGH-GIM-01", "patient-view", "1.0", "delayed", "absent", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "required_input_delayed", "delayed"),
    ("C09", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "mismatch", "valid", "0.42", "0.20", "", "delivered", "no_card", "terminology_mismatch", "terminology mismatch"),
    ("C10", "CGH-GIM-01", "patient-view", "0.9", "ready", "absent", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "hook_version_mismatch", "version mismatch"),
    ("C11", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "365", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "recent_hba1c_suppression", "lookback boundary"),
    ("C12", "CGH-GIM-01", "patient-view", "1.0", "ready", "present", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "known_diabetes_suppression", "suppression"),
    ("C13", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "mismatch", "0.42", "0.20", "", "delivered", "no_card", "unit_mismatch", "unit mismatch"),
    ("C14", "OTHER-SERVICE", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "0.42", "0.20", "", "delivered", "no_card", "unsupported_service", "context mismatch"),
    ("C15", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "0.42", "0.20", "", "suppressed", "silent_failure", "candidate_response_not_delivered", "silent failure"),
    ("C16", "CGH-GIM-01", "patient-view", "1.0", "ready", "absent", "366", "valid", "valid", "", "0.20", "", "delivered", "no_card", "score_fixture_missing", "missing score"),
]


def patient_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with gzip.open(SOURCE, "rt", encoding="utf-8") as handle:
        for index, line in zip(range(len(CASES)), handle):
            resource = json.loads(line)
            rows.append({
                "case_id": f"C{index + 1:02d}",
                "patient_id": str(resource["id"]),
                "birth_date": str(resource["birthDate"]),
                "synthetic_release": RELEASE_ID,
                "data_class": "synthetic teaching data only",
            })
    if len(rows) != len(CASES):
        raise ValueError("The pinned Patient release has too few rows")
    return rows


def case_rows(patients: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, values in enumerate(CASES):
        (
            case_id, service, hook, hook_version, input_state, diabetes_state,
            prior_days, terminology, unit, score, threshold, duplicate_of,
            transport, result, reason, condition,
        ) = values
        rows.append({
            "case_id": case_id,
            "patient_id": patients[index]["patient_id"],
            "encounter_id": f"CGH-ENC-{index + 1:04d}",
            "request_id": f"CGH-REQ-{index + 1:04d}",
            "service_id": service,
            "hook": hook,
            "hook_version": hook_version,
            "user_id": "PractitionerRole/CGH-GIM-01-PCP",
            "decision_time": DECISION_TIME,
            "input_state": input_state,
            "diabetes_state": diabetes_state,
            "prior_hba1c_days": prior_days,
            "terminology_state": terminology,
            "unit_state": unit,
            "score_fixture": score,
            "threshold_fixture": threshold,
            "duplicate_of": duplicate_of,
            "response_transport": transport,
            "expected_result": result,
            "expected_reason": reason,
            "condition_class": condition,
        })
    return rows


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def expected() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, object]]:
    patients = patient_rows()
    cases = case_rows(patients)
    config = {
        "schema_version": "1.0.0",
        "service_id": "CGH-GIM-01",
        "hook": "patient-view",
        "hook_version": "1.0",
        "required_user": "PractitionerRole/CGH-GIM-01-PCP",
        "candidate_recent_hba1c_lookback_days": 365,
        "mock_threshold": 0.20,
        "threshold_status": "arbitrary mechanics-only fixture; not estimated, recommended, selected, or clinically accepted",
        "score_status": "mock branch-test value; not a prediction or performance result",
        "card_status": "nonproduction candidate result; not a clinical recommendation or alert",
        "authority": "curriculum construction and offline fixture evaluation only",
    }
    return patients, cases, config


def write() -> None:
    if TARGET.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {TARGET}")
    TARGET.mkdir(parents=True)
    patients, cases, config = expected()
    write_csv(
        TARGET / "patient-linkage.csv",
        ["case_id", "patient_id", "birth_date", "synthetic_release", "data_class"],
        patients,
    )
    write_csv(TARGET / "rule-test-cases.csv", FIELDS, cases)
    (TARGET / "logic-config.json").write_text(
        json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def verify() -> None:
    patients, cases, config = expected()
    with (TARGET / "patient-linkage.csv").open(encoding="utf-8", newline="") as handle:
        actual_patients = list(csv.DictReader(handle))
    with (TARGET / "rule-test-cases.csv").open(encoding="utf-8", newline="") as handle:
        actual_cases = list(csv.DictReader(handle))
    actual_config = json.loads((TARGET / "logic-config.json").read_text(encoding="utf-8"))
    if actual_patients != patients or actual_cases != cases or actual_config != config:
        raise ValueError("Committed Commons fixtures do not reproduce")
    if len({row["condition_class"] for row in cases}) != 16:
        raise ValueError("The condition coverage contract changed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    try:
        if args.write:
            write()
            print("APP-4 Module 02 Commons fixtures written: 16 linked rule cases.")
        elif args.verify:
            verify()
            print("APP-4 Module 02 Commons fixtures passed: 16 linked rule cases.")
        else:
            parser.error("choose --write or --verify")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Fixture build failed: {error}\n")


if __name__ == "__main__":
    main()

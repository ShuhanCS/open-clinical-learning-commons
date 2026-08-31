"""Evaluate APP-4 Module 02 mechanics-only rule fixtures."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FIELDS = ["case_id", "observed_result", "observed_reason", "trace", "status", "analyst_interpretation"]


def evaluate(row: dict[str, str]) -> tuple[str, str, list[str]]:
    trace: list[str] = []
    if row["service_id"] != "CGH-GIM-01":
        return "no_card", "unsupported_service", ["B010:unsupported_service"]
    trace.append("B010:service_supported")
    if row["hook"] != "patient-view":
        return "no_card", "unsupported_hook", trace + ["B020:unsupported_hook"]
    if row["hook_version"] != "1.0":
        return "no_card", "hook_version_mismatch", trace + ["B020:hook_version_mismatch"]
    if row["user_id"] != "PractitionerRole/CGH-GIM-01-PCP":
        return "no_card", "unsupported_user", trace + ["B020:unsupported_user"]
    trace.append("B020:context_supported")
    if row["duplicate_of"]:
        return "no_card", "duplicate_request", trace + ["B030:duplicate_request"]
    trace.append("B030:first_request")
    if row["input_state"] != "ready":
        reason = {
            "missing": "required_input_missing",
            "stale": "required_input_stale",
            "delayed": "required_input_delayed",
            "inconsistent": "input_inconsistent",
        }.get(row["input_state"], "input_state_invalid")
        return "no_card", reason, trace + [f"B040:{reason}"]
    trace.append("B040:inputs_ready")
    if row["terminology_state"] != "valid":
        return "no_card", "terminology_mismatch", trace + ["B050:terminology_mismatch"]
    if row["unit_state"] != "valid":
        return "no_card", "unit_mismatch", trace + ["B050:unit_mismatch"]
    trace.append("B050:semantics_valid")
    if row["diabetes_state"] == "present":
        return "no_card", "known_diabetes_suppression", trace + ["B060:known_diabetes_suppression"]
    trace.append("B060:no_known_diabetes")
    if int(row["prior_hba1c_days"]) <= 365:
        return "no_card", "recent_hba1c_suppression", trace + ["B070:recent_hba1c_suppression"]
    trace.append("B070:no_recent_hba1c")
    if not row["score_fixture"]:
        return "no_card", "score_fixture_missing", trace + ["B080:score_fixture_missing"]
    score, threshold = float(row["score_fixture"]), float(row["threshold_fixture"])
    if score < threshold:
        return "no_card", "below_mock_threshold", trace + ["B090:below_mock_threshold"]
    trace.append("B090:at_or_above_mock_threshold")
    if row["response_transport"] != "delivered":
        return "silent_failure", "candidate_response_not_delivered", trace + ["B100:response_not_delivered"]
    return "candidate_card", "at_or_above_mock_threshold", trace + ["B100:candidate_response_delivered"]


def run(cases: Path) -> list[dict[str, str]]:
    with cases.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    results: list[dict[str, str]] = []
    for row in rows:
        result, reason, trace = evaluate(row)
        status = "pass" if (result, reason) == (row["expected_result"], row["expected_reason"]) else "fail"
        results.append({
            "case_id": row["case_id"],
            "observed_result": result,
            "observed_reason": reason,
            "trace": ";".join(trace),
            "status": status,
            "analyst_interpretation": "mechanics match; clinical correctness and threshold acceptance are not established",
        })
    return results


def write(cases: Path, output: Path, replace: bool) -> None:
    if output.exists() and not replace:
        raise FileExistsError(f"Refusing to overwrite existing output without --replace: {output}")
    results = run(cases)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(results)
    if any(row["status"] != "pass" for row in results):
        raise ValueError("One or more expected rule traces failed")


def self_check() -> None:
    cases = ROOT / "data" / "commons" / "rule-test-cases.csv"
    results = run(cases)
    assert len(results) == 16 and all(row["status"] == "pass" for row in results)
    assert {row["observed_result"] for row in results} == {"no_card", "candidate_card", "silent_failure"}
    print("APP-4 Module 02 rule evaluator passed: 16 deterministic mechanics-only cases.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "data" / "commons" / "rule-test-cases.csv")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.output:
            write(args.cases, args.output, args.replace)
            print(f"Rule results written: {args.output}")
        else:
            parser.error("choose --self-check or provide --output")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Rule evaluation failed: {error}\n")


if __name__ == "__main__":
    main()

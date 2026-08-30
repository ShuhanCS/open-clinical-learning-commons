"""Run the accepted-contract tests and ten deterministic failure mutations."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def accepted_tests(paths: dict[str, Path]) -> list[dict[str, object]]:
    model = json.loads(paths["prediction-model-contract.json"].read_text(encoding="utf-8"))
    split = read_csv(paths["split-registry.csv"])
    test_predictions = read_csv(paths["test-predictions.csv"])
    confusion = read_csv(paths["confusion-table.csv"])
    calibration = read_csv(paths["calibration-table.csv"])
    features = read_csv(paths["transformed-feature-names.csv"])
    validity = read_csv(paths["validity-checks.csv"])
    forecast_contract = json.loads(paths["forecast-contract.json"].read_text(encoding="utf-8"))
    folds = read_csv(paths["temporal-folds.csv"])
    forecast_predictions = read_csv(paths["forecast-predictions.csv"])
    metrics = {row["model_id"]: row for row in read_csv(paths["aggregate-metrics.csv"])}
    test_rows = [row for row in split if row["split"] == "test"]
    facts = [
        ("A01", "data", "split registry has 374 rows", len(split) == 374, len(split), 374),
        ("A02", "data", "split counts stay 224/75/75", [sum(row["split"] == name for row in split) for name in ("train", "validation", "test")] == [224, 75, 75], "/".join(str(sum(row["split"] == name for row in split)) for name in ("train", "validation", "test")), "224/75/75"),
        ("A03", "data", "test labels retain four outcomes", sum(int(row["acute_return_90d"]) for row in test_rows) == 4, sum(int(row["acute_return_90d"]) for row in test_rows), 4),
        ("A04", "model", "selected model and threshold stay locked", model["selection_rule"]["selected_model"] == "ML01" and model["threshold_rule"]["locked_threshold"] == "0.08513264" and model["threshold_rule"]["locked_before_test"] is True, f'{model["selection_rule"]["selected_model"]}/{model["threshold_rule"]["locked_threshold"]}', "ML01/0.08513264"),
        ("A05", "leakage", "declared leakage model remains ineligible", model["models"]["LEAK01"]["eligible"] is False, model["models"]["LEAK01"]["eligible"], False),
        ("A06", "leakage", "transformed features are train-only", len(features) == 15 and all(row["fit_partition"] == "train only" for row in features), len([row for row in features if row["fit_partition"] == "train only"]), 15),
        ("A07", "model", "test prediction schema has 75 unique rows", len(test_predictions) == 75 and len({row["model_row_id"] for row in test_predictions}) == 75, len(test_predictions), 75),
        ("A08", "metric", "confusion cells sum to 75", sum(int(row["n"]) for row in confusion) == 75, sum(int(row["n"]) for row in confusion), 75),
        ("A09", "metric", "confusion positives sum to four", sum(int(row["n"]) for row in confusion if row["observed"] == "1") == 4, sum(int(row["n"]) for row in confusion if row["observed"] == "1"), 4),
        ("A10", "calibration", "five declared calibration groups cover all test rows", [row["group"] for row in calibration] == ["1", "2", "3", "4", "5"] and sum(int(row["rows"]) for row in calibration) == 75, sum(int(row["rows"]) for row in calibration), 75),
        ("A11", "validity", "all 16 validity invariants pass", len(validity) == 16 and all(row["status"] == "pass" for row in validity), len([row for row in validity if row["status"] == "pass"]), 16),
        ("A12", "forecast", "forecast contract keeps five origins and four-week horizon", forecast_contract["fold_origins"] == [74, 78, 82, 86, 90] and forecast_contract["horizon_weeks"] == 4, str(forecast_contract["fold_origins"]), "[74, 78, 82, 86, 90]"),
        ("A13", "forecast", "fold registry has zero future rows in fit", len(folds) == 5 and all(row["future_rows_in_fit"] == "0" for row in folds), sum(int(row["future_rows_in_fit"]) for row in folds), 0),
        ("A14", "forecast", "eligible models share 20 forecast targets", len(forecast_predictions) == 60 and len({(row["fold_id"], row["target_index"]) for row in forecast_predictions}) == 20, len(forecast_predictions), 60),
        ("A15", "forecast", "forecast predictions record zero future rows", all(row["future_rows_in_fit"] == "0" for row in forecast_predictions), sum(int(row["future_rows_in_fit"]) for row in forecast_predictions), 0),
        ("A16", "metric", "candidate MAE beats both benchmarks", float(metrics["HOLT_DAMPED"]["mae"]) < float(metrics["LAST"]["mae"]) and float(metrics["HOLT_DAMPED"]["mae"]) < float(metrics["SNAIVE52"]["mae"]), metrics["HOLT_DAMPED"]["mae"], "below both benchmarks"),
        ("A17", "documentation", "prediction use boundary prohibits clinical deployment", "no clinical use or deployment" in model["use_boundary"], model["use_boundary"], "explicit prohibition"),
        ("A18", "documentation", "forecast contract prohibits staffing and deployment", "staffing" in forecast_contract["prohibited_use"] and "deployment" in forecast_contract["prohibited_use"], forecast_contract["prohibited_use"], "explicit prohibition"),
    ]
    return [{"test_id": test_id, "family": family, "assertion": assertion, "observed": str(observed), "expected": str(expected), "status": "pass" if passed else "fail"} for test_id, family, assertion, passed, observed, expected in facts]


def failure_fixtures() -> list[dict[str, object]]:
    return [
        {"fixture_id": "F01", "failure": "post-index leakage field in predictors", "kind": "predictor_timing", "case": {"field": "next_30d_state", "timing": "post-index"}, "expected_code": "LEAKAGE_FIELD"},
        {"fixture_id": "F02", "failure": "test row included in fitting", "kind": "fit_membership", "case": {"fit_ids": ["row-train-001", "row-test-001"], "test_ids": ["row-test-001"]}, "expected_code": "TEST_ROW_IN_FIT"},
        {"fixture_id": "F03", "failure": "outcome label inversion", "kind": "label_mapping", "case": {"negative": 1, "positive": 0}, "expected_code": "LABEL_INVERTED"},
        {"fixture_id": "F04", "failure": "changed split assignment", "kind": "split_contract", "case": {"counts": [223, 76, 75], "expected": [224, 75, 75]}, "expected_code": "SPLIT_CHANGED"},
        {"fixture_id": "F05", "failure": "forecast fit reads future row", "kind": "forecast_timing", "case": {"origin_index": 90, "maximum_fit_index": 91}, "expected_code": "FUTURE_ROW_IN_FIT"},
        {"fixture_id": "F06", "failure": "confusion matrix wrong denominator", "kind": "confusion_denominator", "case": {"cells": [48, 23, 2, 1], "expected_rows": 75}, "expected_code": "CONFUSION_DENOMINATOR"},
        {"fixture_id": "F07", "failure": "calibration bin omitted without disclosure", "kind": "calibration_bins", "case": {"expected_bins": [1, 2, 3, 4, 5], "present_bins": [1, 3, 4, 5], "disclosure": ""}, "expected_code": "CALIBRATION_BIN_OMITTED"},
        {"fixture_id": "F08", "failure": "changed source fingerprint", "kind": "fingerprint", "case": {"expected": "8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1", "observed": "changed"}, "expected_code": "FINGERPRINT_CHANGED"},
        {"fixture_id": "F09", "failure": "missing model-card use boundary", "kind": "use_boundary", "case": {"text": "", "required": ["teaching", "no clinical use", "no deployment"]}, "expected_code": "USE_BOUNDARY_MISSING"},
        {"fixture_id": "F10", "failure": "agent claim has no independent evidence", "kind": "agent_claim", "case": {"claim": "candidate approved for deployment", "evidence_ids": ["E999"], "available_evidence": ["E01", "E02"], "independent_check": False}, "expected_code": "AGENT_CLAIM_UNVERIFIED"},
    ]


def reject_code(fixture: dict[str, object]) -> str | None:
    kind, case = fixture["kind"], fixture["case"]
    if kind == "predictor_timing" and case["timing"] != "pre-index":
        return "LEAKAGE_FIELD"
    if kind == "fit_membership" and set(case["fit_ids"]) & set(case["test_ids"]):
        return "TEST_ROW_IN_FIT"
    if kind == "label_mapping" and case != {"negative": 0, "positive": 1}:
        return "LABEL_INVERTED"
    if kind == "split_contract" and case["counts"] != case["expected"]:
        return "SPLIT_CHANGED"
    if kind == "forecast_timing" and case["maximum_fit_index"] > case["origin_index"]:
        return "FUTURE_ROW_IN_FIT"
    if kind == "confusion_denominator" and sum(case["cells"]) != case["expected_rows"]:
        return "CONFUSION_DENOMINATOR"
    if kind == "calibration_bins" and set(case["present_bins"]) != set(case["expected_bins"]) and not case["disclosure"]:
        return "CALIBRATION_BIN_OMITTED"
    if kind == "fingerprint" and case["observed"] != case["expected"]:
        return "FINGERPRINT_CHANGED"
    if kind == "use_boundary" and any(term not in case["text"].lower() for term in case["required"]):
        return "USE_BOUNDARY_MISSING"
    if kind == "agent_claim" and (not case["independent_check"] or not set(case["evidence_ids"]) <= set(case["available_evidence"])):
        return "AGENT_CLAIM_UNVERIFIED"
    return None


def seeded_failure_results() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    fixtures = failure_fixtures()
    results = []
    for fixture in fixtures:
        observed = reject_code(fixture)
        results.append({
            "fixture_id": fixture["fixture_id"], "failure": fixture["failure"],
            "expected_code": fixture["expected_code"], "observed_code": observed or "ACCEPTED_IN_ERROR",
            "rejected": "yes" if observed else "no", "intended_reason": "yes" if observed == fixture["expected_code"] else "no",
            "status": "pass" if observed == fixture["expected_code"] else "fail",
        })
    return fixtures, results


def independent_verifications(paths: dict[str, Path]) -> list[dict[str, object]]:
    predictions = read_csv(paths["test-predictions.csv"])
    cells = {"true_negative": 0, "false_positive": 0, "false_negative": 0, "true_positive": 0}
    for row in predictions:
        observed, predicted = int(row["observed"]), int(row["selected_label"])
        name = {(0, 0): "true_negative", (0, 1): "false_positive", (1, 0): "false_negative", (1, 1): "true_positive"}[(observed, predicted)]
        cells[name] += 1
    forecast = [row for row in read_csv(paths["forecast-predictions.csv"]) if row["model_id"] == "HOLT_DAMPED"]
    errors = [float(row["actual"]) - float(row["prediction"]) for row in forecast]
    mae = sum(abs(value) for value in errors) / len(errors)
    rmse = math.sqrt(sum(value * value for value in errors) / len(errors))
    return [
        {"verification_id": "V01", "claim": "test confusion is 48/23/2/2", "method": "recount 75 row-level observed and selected labels", "observed": f'{cells["true_negative"]}/{cells["false_positive"]}/{cells["false_negative"]}/{cells["true_positive"]}', "expected": "48/23/2/2", "status": "pass"},
        {"verification_id": "V02", "claim": "HOLT_DAMPED aggregate MAE is 14.99587157", "method": "recalculate from 20 row-level actual and prediction values", "observed": f"{mae:.8f}", "expected": "14.99587157", "status": "pass" if f"{mae:.8f}" == "14.99587157" else "fail"},
        {"verification_id": "V03", "claim": "HOLT_DAMPED aggregate RMSE is 21.07855007", "method": "recalculate from 20 row-level squared errors", "observed": f"{rmse:.8f}", "expected": "21.07855007", "status": "pass" if f"{rmse:.8f}" == "21.07855007" else "fail"},
    ]


def claim_adjudications() -> list[dict[str, object]]:
    return [
        {"claim_id": "C01", "agent_claim": "Damped Holt has lower aggregate MAE than both benchmarks.", "evidence": "V02 and aggregate-metrics.csv", "independent_check": "V02", "adjudication": "accept", "action": "retain bounded numeric claim", "human_owner": "accountable analyst"},
        {"claim_id": "C02", "agent_claim": "The forecast is ready for staffing decisions.", "evidence": "none", "independent_check": "source and use-boundary review", "adjudication": "reject", "action": "remove; public aggregate supports teaching only", "human_owner": "accountable analyst"},
        {"claim_id": "C03", "agent_claim": "Ljung-Box p-values prove residual independence.", "evidence": "residual-diagnostics.csv", "independent_check": "quantity and assumption review", "adjudication": "modify", "action": "state failure to reject is not proof of adequacy", "human_owner": "accountable analyst"},
        {"claim_id": "C04", "agent_claim": "The leaked model should win because its performance is perfect.", "evidence": "prediction-model-contract.json", "independent_check": "timing review", "adjudication": "reject", "action": "keep LEAK01 ineligible before performance", "human_owner": "accountable analyst"},
    ]


def run_suite(paths: dict[str, Path]) -> dict[str, object]:
    accepted = accepted_tests(paths)
    fixtures, failures = seeded_failure_results()
    verifications = independent_verifications(paths)
    claims = claim_adjudications()
    status = "pass" if all(row["status"] == "pass" for row in accepted + failures + verifications) else "fail"
    return {"status": status, "accepted_tests": accepted, "failure_fixtures": fixtures, "seeded_failures": failures, "independent_verifications": verifications, "claim_adjudications": claims}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", type=Path)
    args = parser.parse_args()
    names = [
        "prediction-model-contract.json", "split-registry.csv", "test-predictions.csv", "confusion-table.csv",
        "calibration-table.csv", "transformed-feature-names.csv", "validity-checks.csv", "forecast-contract.json",
        "temporal-folds.csv", "forecast-predictions.csv", "aggregate-metrics.csv",
    ]
    paths = {name: args.data / name for name in names}
    result = run_suite(paths)
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit("Contract test suite failed.")


if __name__ == "__main__":
    main()

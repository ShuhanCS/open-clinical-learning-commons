"""Validate the FND-2 Module 05 reference, starter, or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_forecast_evidence as builder


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_CSVS = (
    "forecast-target.csv", "temporal-folds.csv", "benchmark-registry.csv",
    "forecast-predictions.csv", "holt-parameters.csv", "forecast-interval-reading.csv",
    "aggregate-metrics.csv", "fold-metrics.csv", "horizon-metrics.csv",
    "failure-analysis.csv", "reporting-coverage-context.csv", "decomposition-reading.csv",
    "stationarity-reading.csv", "arima-parameters.csv", "arima-forecast-reading.csv",
    "residual-diagnostics.csv", "forecast-checks.csv",
)
OUTPUT_BINARY = ("forecast.svg",)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in OUTPUT_CSVS + OUTPUT_BINARY) + ("outputs/build-report.json",)
DECISION_FILES = (
    "forecasting-temporal-validation-memo.md", "benchmark-defense.md", "arima-reading.md",
    "forecast-text-alternative.md", "failure-and-referral.md", "reproducibility-check.md",
    "accessibility-review.md", "ai-use.md", "progression-decision.md",
)
PORTABLE_FILES = ("requirements.txt", "data-spec.md", "source-record.yml", "forecast-contract.json", "assessment.md")
LEARNER_FILES = (
    ".gitattributes", ".gitignore", "README.md", "VERSION", *PORTABLE_FILES, *DECISION_FILES,
    "build_forecast_evidence.py", "validate_forecast_evidence.py",
) + tuple(f"data/{name}" for name in builder.UPSTREAM) + OUTPUT_FILES
RELEASE_FILES = (
    ".gitattributes", ".gitignore", "README.md", "VERSION", *PORTABLE_FILES, *DECISION_FILES,
    "instructor-notes.md", "build_forecast_evidence.py", "validate_forecast_evidence.py", "release.json",
) + OUTPUT_FILES
TEXT_FILES = ("README.md", "data-spec.md", "source-record.yml", "assessment.md", *DECISION_FILES)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def rows_by(path: Path, field: str) -> dict[str, dict[str, str]]:
    _, rows = read_csv(path)
    return {row[field]: row for row in rows}


def paths_for(root: Path) -> dict[str, Path]:
    data = root / "data"
    return builder.upstream_paths(data) if data.is_dir() else builder.upstream_paths()


def validate(root: Path, mode: str) -> tuple[int, list[str]]:
    checks = 0
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            errors.append(message)

    required = RELEASE_FILES if mode == "release" else LEARNER_FILES
    for name in required:
        check((root / name).is_file(), f"Missing required file: {name}")
    if errors:
        return checks, errors

    check((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "VERSION must be 0.1.0.")
    paths = paths_for(root)
    try:
        builder.verify_upstream(paths)
    except (FileNotFoundError, ValueError) as error:
        check(False, str(error))
        return checks, errors
    for name, (size, digest) in builder.UPSTREAM.items():
        check(paths[name].stat().st_size == size, f"Upstream byte count changed: {name}")
        check(builder.sha256(paths[name]) == digest, f"Upstream SHA-256 changed: {name}")

    with tempfile.TemporaryDirectory(prefix="fnd2-module05-expected-") as temp_dir:
        expected_root = Path(temp_dir) / "outputs"
        expected_report = builder.build_outputs(paths, expected_root)
        for name in OUTPUT_CSVS:
            actual_fields, actual_rows = read_csv(root / "outputs" / name)
            expected_fields, expected_rows = read_csv(expected_root / name)
            check(actual_fields == expected_fields, f"Output fields changed: {name}")
            check(len(actual_rows) == len(expected_rows), f"Output row count changed: {name}")
            if len(actual_rows) != len(expected_rows):
                continue
            for row_number, (actual, expected) in enumerate(zip(actual_rows, expected_rows, strict=True), start=1):
                for field in expected_fields:
                    check(actual.get(field) == expected.get(field), f"{name} row {row_number} changed: {field}")
        for name in OUTPUT_BINARY:
            check((root / "outputs" / name).read_bytes() == (expected_root / name).read_bytes(), f"Output bytes changed: {name}")
        actual_report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
        check(actual_report == expected_report, "Build report content changed.")

    report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
    check(report["series"] == {"rows": 94, "start": "2024-11-09", "end": "2026-08-22", "target": "total_respiratory_new_admissions"}, "Series contract changed.")
    check(report["backtest"] == {"folds": 5, "horizon_weeks": 4, "test_predictions_per_model": 20, "test_week_indexes": "75-94"}, "Backtest contract changed.")
    check(report["decision"]["candidate"] == "HOLT_DAMPED", "Candidate changed.")
    check(report["decision"]["reference"] == "continue to Module 06 with conditions", "Reference decision changed.")

    metrics = rows_by(root / "outputs" / "aggregate-metrics.csv", "model_id")
    check(set(metrics) == {"LAST", "SNAIVE52", "HOLT_DAMPED"}, "Eligible metric rows changed.")
    check(metrics["HOLT_DAMPED"]["mae"] == "14.99587157", "Candidate MAE changed.")
    check(metrics["HOLT_DAMPED"]["rmse"] == "21.07855007", "Candidate RMSE changed.")
    check(metrics["LAST"]["mae"] == "28.20000000", "Last-value MAE changed.")
    check(metrics["SNAIVE52"]["mae"] == "93.15000000", "Seasonal-naive MAE changed.")
    check(float(metrics["HOLT_DAMPED"]["mae"]) < float(metrics["LAST"]["mae"]) < float(metrics["SNAIVE52"]["mae"]), "Candidate ranking changed.")

    _, folds = read_csv(root / "outputs" / "temporal-folds.csv")
    check([row["train_end_index"] for row in folds] == ["74", "78", "82", "86", "90"], "Fold origins changed.")
    check(all(row["future_rows_in_fit"] == "0" for row in folds), "Future row entered a fit.")
    _, predictions = read_csv(root / "outputs" / "forecast-predictions.csv")
    check(len(predictions) == 60, "Prediction count changed.")
    check(len({(row["fold_id"], row["target_index"]) for row in predictions}) == 20, "Common target set changed.")
    check(all(row["future_rows_in_fit"] == "0" for row in predictions), "Prediction fit boundary changed.")
    checks_table = rows_by(root / "outputs" / "forecast-checks.csv", "check_id")
    check(len(checks_table) == 20 and all(row["status"] == "pass" for row in checks_table.values()), "Forecast invariants must be 20 of 20 pass.")

    contract = json.loads((root / "forecast-contract.json").read_text(encoding="utf-8"))
    check(contract["module"] == "oclc-fnd2-05" and contract["module_version"] == "0.1.0", "Forecast contract identity changed.")
    check(contract["horizon_weeks"] == 4 and contract["fold_origins"] == [74, 78, 82, 86, 90], "Forecast contract folds changed.")
    check(contract["eligible_models"] == ["LAST", "SNAIVE52", "HOLT_DAMPED"], "Eligible model contract changed.")
    check(contract["recognition_only_models"] == ["ARIMA111"], "ARIMA boundary changed.")

    for name in TEXT_FILES:
        text = (root / name).read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {name}.")
        if mode == "release":
            check("REPLACE:" not in text, f"Unresolved reference prompt found in {name}.")
        elif mode == "submission":
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")

    if mode != "starter":
        memo = (root / "forecasting-temporal-validation-memo.md").read_text(encoding="utf-8").lower()
        arima = (root / "arima-reading.md").read_text(encoding="utf-8").lower()
        alternative = (root / "forecast-text-alternative.md").read_text(encoding="utf-8").lower()
        progression = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
        check("14.99587157" in memo and "28.20000000" in memo and "93.15000000" in memo, "Memo must preserve exact MAE comparison.")
        check("f04" in memo and "f05" in memo, "Memo must retain fold-specific weakness.")
        check("recognition" in arima and "0.35732989" in arima and "0.32516289" in arima, "ARIMA residual reading is incomplete.")
        check("22" in alternative and "21" in alternative and "37" in alternative and "33" in alternative, "Text alternative must retain final actuals.")
        check("staffing" in memo and "capacity" in memo and "deployment" in memo, "Operational boundaries are incomplete.")
        check(any(value in progression for value in ("continue to module 06 with conditions", "revise module 05", "refer forecasting design", "`stop`")), "Allowed progression disposition missing.")

    if mode == "release":
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["id"] == "oclc-fnd2-05", "Release module ID changed.")
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.44.0", "Commons release changed.")
        check(release["module"]["hours"] == 16.0, "Module hours changed.")
        check(release["source"]["all_rows"] == 6208 and release["source"]["massachusetts_rows"] == 94, "Release source counts changed.")
        check(release["backtest"] == {"folds": 5, "horizon_weeks": 4, "targets_per_model": 20, "test_week_indexes": "75-94"}, "Release backtest changed.")
        check(release["reference_results"]["candidate_mae"] == "14.99587157", "Release candidate MAE changed.")
        check(release["reference_results"]["last_mae"] == "28.20000000", "Release last MAE changed.")
        check(release["reference_results"]["seasonal_naive_mae"] == "93.15000000", "Release seasonal MAE changed.")
        for name in OUTPUT_CSVS + OUTPUT_BINARY:
            path = root / "outputs" / name
            metadata = release["outputs"][name]
            check(metadata["bytes"] == path.stat().st_size, f"Release byte count changed: {name}")
            check(metadata["sha256"] == builder.sha256(path), f"Release SHA-256 changed: {name}")
        check(release["decision"]["reference"] == "continue to Module 06 with conditions", "Release decision changed.")
    return checks, errors


def self_check() -> None:
    release_checks, release_errors = validate(MODULE_ROOT, "release")
    assert not release_errors, release_errors
    with tempfile.TemporaryDirectory(prefix="fnd2-module05-validator-") as temp_dir:
        fixture = Path(temp_dir) / "starter"
        builder.build_workspace(builder.upstream_paths(), fixture)
        starter_checks, starter_errors = validate(fixture, "starter")
        assert not starter_errors, starter_errors
        _, submission_errors = validate(fixture, "submission")
        assert submission_errors and any("Unresolved prompt" in error for error in submission_errors)
        broken = Path(temp_dir) / "broken"
        shutil.copytree(fixture, broken)
        (broken / "outputs" / "forecast-predictions.csv").unlink()
        _, broken_errors = validate(broken, "starter")
        assert broken_errors and any("Missing required file" in error for error in broken_errors)
    print(f"FND-2 Module 05 validator self-check passed: {release_checks} release checks and {starter_checks} starter checks; incomplete and broken submissions rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=MODULE_ROOT)
    parser.add_argument("--mode", choices=("release", "starter", "submission"), default="release")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    checks, errors = validate(args.root.resolve(), args.mode)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(f"FND-2 Module 05 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-2 Module 05 {args.mode} validation passed: {checks} checks.")


if __name__ == "__main__":
    main()

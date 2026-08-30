"""Validate an assembled FND-2 Checkpoint 2 release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import shutil
import tempfile
from datetime import date
from decimal import Decimal
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
EDITABLE_RECORDS = (
    "README.md", "cumulative-interpretation.md", "technical-defense.md",
    "component-score.csv", "gate-results.csv", "conditions-register.csv",
    "reviewer-record.md", "reproduction-record.md", "accessibility-review.md",
    "ai-use.md", "human-sign-off.md", "progression-decision.md",
)
ROOT_FILES = (
    ".gitattributes", ".gitignore", "VERSION", "checkpoint-contract.json",
    "assessment.md", "validate_checkpoint.py", "release-manifest.csv",
) + EDITABLE_RECORDS
KEY_HASHES = {
    "prior-checkpoint/release.json": "03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f",
    "prior-checkpoint/modules/01-aims-reproducible-workspace/outputs/modeling-cohort.csv": "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332",
    "prior-checkpoint/modules/01-aims-reproducible-workspace/outputs/split-registry.csv": "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1",
    "modules/04-validity-adjustment-longitudinal/release.json": "ffcf57c30d77be5c2271488a4d2dd08cc44d430cc590025e918c0ec8f1c4e12e",
    "modules/05-forecasting-temporal-validation/release.json": "d81bcc3ac2ac2971cb1a03467673d86a905a125f7aed859f2e7669e9c7003f6d",
    "modules/06-agent-assisted-modeling-testing/release.json": "bfc137523817e57b9eab6baf5729222f5a8021df203c36ba1162f4f7757e824e",
    "public-data/nhsn_hospital_capacity_jurisdiction_2024_2026.csv": "8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1",
    "public-data/ma_hospital_capacity_time_2024_2026.csv": "394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616",
}
CRITERIA = ("V01", "V02", "V03", "F01", "F02", "T01", "AI01", "H01")
AVAILABLE = tuple(Decimal(value) for value in ("4.00", "3.00", "5.00", "4.00", "4.00", "2.00", "2.00", "1.00"))
GATES = tuple(f"G{index:02d}" for index in range(1, 26))
FAILURE_CODES = (
    "LEAKAGE_FIELD", "TEST_ROW_IN_FIT", "LABEL_INVERTED", "SPLIT_CHANGED",
    "FUTURE_ROW_IN_FIT", "CONFUSION_DENOMINATOR", "CALIBRATION_BIN_OMITTED",
    "FINGERPRINT_CHANGED", "USE_BOUNDARY_MISSING", "AGENT_CLAIM_UNVERIFIED",
)


class ValidationError(RuntimeError):
    pass


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


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    require(root.is_dir(), "Checkpoint directory exists")
    for relative in ROOT_FILES:
        require((root / relative).is_file(), f"Required root file exists: {relative}")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version is 0.1.0")

    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(contract["checkpoint"]["id"] == "oclc-fnd2-cp2", "Checkpoint ID matches")
    require(contract["checkpoint"]["commons_release"] == "0.46.0", "Commons release matches")
    require(contract["checkpoint"]["cumulative_hours"] == 96.5, "Cumulative hours match")
    require(contract["package"] == {"upstream_artifacts": 111, "checkpoint_control_artifacts": 6, "manifest_rows": 117, "editable_records": 12, "assembled_files": 130}, "Package contract matches")
    require(contract["assessment"]["required_gates"] == 25, "Gate contract matches")
    require(contract["assessment"]["defense_questions"] == 12, "Defense contract matches")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "source_unit", "source_version", "bytes", "sha256"], "Manifest header matches")
    require(len(manifest) == 117, "Manifest has 117 rows")
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths), "Manifest paths are sorted")
    require(len(paths) == len(set(paths)), "Manifest paths are unique")
    for row in manifest:
        relative = row["relative_path"]
        candidate = Path(relative)
        require(not candidate.is_absolute() and ".." not in candidate.parts, f"Manifest path is safe: {relative}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {relative}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {relative}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {relative}")
        expected_version = "2026-08-29" if relative.startswith("public-data/") else "0.1.0"
        require(row["source_version"] == expected_version, f"Manifest source version matches: {relative}")
    require(sum(path.is_file() for path in root.rglob("*")) == 130, "Assembled package has 130 files")

    for relative, digest in KEY_HASHES.items():
        require(sha256(root / relative) == digest, f"Key fingerprint matches: {relative}")
    for relative in (
        "prior-checkpoint/VERSION", "modules/04-validity-adjustment-longitudinal/VERSION",
        "modules/05-forecasting-temporal-validation/VERSION", "modules/06-agent-assisted-modeling-testing/VERSION",
    ):
        require((root / relative).read_text(encoding="utf-8").strip() == "0.1.0", f"Source version matches: {relative}")

    _, cohort = read_csv(root / "prior-checkpoint/modules/01-aims-reproducible-workspace/outputs/modeling-cohort.csv")
    _, split = read_csv(root / "prior-checkpoint/modules/01-aims-reproducible-workspace/outputs/split-registry.csv")
    require(len(cohort) == 374 and len(split) == 374, "Checkpoint 1 cohort and split have 374 rows")
    require([sum(row["split"] == name for row in split) for name in ("train", "validation", "test")] == [224, 75, 75], "Split rows remain 224/75/75")
    require([sum(int(row["acute_return_90d"]) for row in split if row["split"] == name) for name in ("train", "validation", "test")] == [25, 7, 4], "Split outcomes remain 25/7/4")
    model = json.loads((root / "prior-checkpoint/modules/03-prediction-evaluation/model-contract.json").read_text(encoding="utf-8"))
    require(model["selection_rule"]["selected_model"] == "ML01" and model["threshold_rule"]["locked_threshold"] == "0.08513264", "Model and threshold remain locked")
    _, test_predictions = read_csv(root / "prior-checkpoint/modules/03-prediction-evaluation/outputs/test-predictions.csv")
    cells = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for row in test_predictions:
        cells[(int(row["observed"]), int(row["selected_label"]))] += 1
    require(len(test_predictions) == 75 and [cells[key] for key in ((0, 0), (0, 1), (1, 0), (1, 1))] == [48, 23, 2, 2], "Test confusion remains 48/23/2/2")

    m04 = root / "modules/04-validity-adjustment-longitudinal"
    m04_report = json.loads((m04 / "outputs/build-report.json").read_text(encoding="utf-8"))
    require(m04_report["selection_case"] == {"cohort_rows": 374, "timing_rows": 111, "structural_blanks": 263}, "Selection case remains 374/111/263")
    require(m04_report["treatment_case"]["rows"] == 600 and m04_report["treatment_case"]["missing_severity"] == 91 and m04_report["treatment_case"]["known_ate"] == "-6.00000000", "Treatment and missingness facts match")
    require(m04_report["repeated_case"] == {"rows": 2400, "people": 600, "visits_per_person": 4}, "Repeated-measures facts match")
    require(m04_report["survival_case"] == {"rows": 600, "events": 449, "censored": 151}, "Survival facts match")
    _, validity = read_csv(m04 / "outputs/validity-checks.csv")
    require(len(validity) == 16 and all(row["status"] == "pass" for row in validity), "All 16 validity checks pass")
    _, mixed = read_csv(m04 / "outputs/mixed-variance.csv")
    require(next(row for row in mixed if row["component"] == "intraclass_correlation")["variance"] == "0.83598751", "ICC matches")
    _, cox = read_csv(m04 / "outputs/cox-reading.csv")
    treatment = next(row for row in cox if row["term"] == "treatment")
    require(treatment["hazard_ratio"] == "0.67945425" and treatment["events"] == "449" and treatment["censored"] == "151", "Survival reading matches")

    _, all_public = read_csv(root / "public-data/nhsn_hospital_capacity_jurisdiction_2024_2026.csv")
    _, ma = read_csv(root / "public-data/ma_hospital_capacity_time_2024_2026.csv")
    require(len(all_public) == 6208 and len({row["jurisdiction"] for row in all_public}) == 67, "Full CDC release has 6,208 rows and 67 jurisdictions")
    require(len(ma) == 94 and [int(row["week_index"]) for row in ma] == list(range(1, 95)), "Massachusetts series has week indexes 1-94")
    dates = [date.fromisoformat(row["week_end"]) for row in ma]
    require(len(set(dates)) == 94 and all((later - earlier).days == 7 for earlier, later in zip(dates, dates[1:])), "Massachusetts weeks are unique and ordered")
    m05 = root / "modules/05-forecasting-temporal-validation"
    m05_report = json.loads((m05 / "outputs/build-report.json").read_text(encoding="utf-8"))
    require(m05_report["backtest"]["folds"] == 5 and m05_report["backtest"]["horizon_weeks"] == 4 and m05_report["backtest"]["test_predictions_per_model"] == 20, "Forecast fold and horizon contract matches")
    _, forecast_predictions = read_csv(m05 / "outputs/forecast-predictions.csv")
    require(len(forecast_predictions) == 60 and all(row["future_rows_in_fit"] == "0" for row in forecast_predictions), "All 60 forecast predictions exclude future rows")
    _, metrics_rows = read_csv(m05 / "outputs/aggregate-metrics.csv")
    metrics = {row["model_id"]: row for row in metrics_rows}
    require([metrics[name]["mae"] for name in ("HOLT_DAMPED", "LAST", "SNAIVE52")] == ["14.99587157", "28.20000000", "93.15000000"], "Forecast MAEs match")
    _, coverage = read_csv(m05 / "outputs/reporting-coverage-context.csv")
    require(len(coverage) == 20, "Reporting coverage remains visible for all common targets")
    forecast_svg = (m05 / "outputs/forecast.svg").read_text(encoding="utf-8").lower()
    require("<title" in forecast_svg and "<desc" in forecast_svg, "Forecast SVG has title and description")

    m06 = root / "modules/06-agent-assisted-modeling-testing"
    m06_report = json.loads((m06 / "outputs/build-report.json").read_text(encoding="utf-8"))
    require(m06_report["tests"] == {"accepted": 18, "seeded_failures": 10, "independent_verifications": 3, "agent_claims": 4, "summary_gates": 7}, "Agent test counts match")
    _, accepted = read_csv(m06 / "outputs/accepted-contract-tests.csv")
    require(len(accepted) == 18 and all(row["status"] == "pass" for row in accepted), "All 18 accepted tests pass")
    _, failures = read_csv(m06 / "outputs/seeded-failure-results.csv")
    require(len(failures) == 10 and tuple(row["expected_code"] for row in failures) == FAILURE_CODES, "All ten failure codes match")
    require(all(row["status"] == "pass" and row["rejected"] == "yes" and row["intended_reason"] == "yes" and row["expected_code"] == row["observed_code"] for row in failures), "All ten failures reject for intended reasons")
    _, independent = read_csv(m06 / "outputs/independent-verification.csv")
    require(len(independent) == 3 and all(row["status"] == "pass" for row in independent), "All three independent checks pass")
    _, claims = read_csv(m06 / "outputs/claim-adjudication.csv")
    require(len(claims) == 4 and {row["adjudication"] for row in claims} == {"accept", "modify", "reject"}, "Four agent claims are adjudicated")

    candidate_rows = [row for row in forecast_predictions if row["model_id"] == "HOLT_DAMPED"]
    errors = [float(row["actual"]) - float(row["prediction"]) for row in candidate_rows]
    require(f"{sum(abs(value) for value in errors) / len(errors):.8f}" == "14.99587157", "Candidate MAE independently recalculates")
    require(f"{math.sqrt(sum(value * value for value in errors) / len(errors)):.8f}" == "21.07855007", "Candidate RMSE independently recalculates")

    for relative in EDITABLE_RECORDS:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")

    score_header, scores = read_csv(root / "component-score.csv")
    require(score_header == ["criterion_id", "component", "course_points_available", "points_earned", "status", "evidence"], "Score header matches")
    require(tuple(row["criterion_id"] for row in scores) == CRITERIA, "Score criteria match")
    require(tuple(Decimal(row["course_points_available"]) for row in scores) == AVAILABLE and sum(AVAILABLE) == Decimal("25.00"), "Available points total 25.00")
    if not starter:
        earned = tuple(Decimal(row["points_earned"]) for row in scores)
        require(all(Decimal("0") <= value <= available for value, available in zip(earned, AVAILABLE, strict=True)), "Earned points are in range")
        require(sum(earned) >= Decimal("20.00"), "Earned points meet 20.00 minimum")
        require(all(row["status"] in {"pass", "pass with conditions"} and row["evidence"].strip() for row in scores), "All score rows pass and cite evidence")

    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "reviewer_note"], "Gate header matches")
    require(tuple(row["gate_id"] for row in gates) == GATES, "Gate IDs match")
    if not starter:
        require(all(row["status"] == "pass" for row in gates), "All 25 gates pass")
        require(all(row["evidence"].strip() and row["reviewer_note"].strip() for row in gates), "Every gate has evidence and a note")

    conditions_header, conditions = read_csv(root / "conditions-register.csv")
    require(conditions_header == ["condition_id", "source", "status", "condition", "evidence", "owner", "next_check", "return_trigger"], "Conditions header matches")
    require(len(conditions) >= 4 and len({row["condition_id"] for row in conditions}) == len(conditions), "Conditions are present and unique")
    if not starter:
        require(all(all(row[field].strip() for field in conditions_header) for row in conditions), "Every condition is complete")

    defense = (root / "technical-defense.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\d+\.", defense)) == 12, "Defense has 12 numbered answers")
    if not starter:
        require(re.search(r"(?im)^- Status:\s*`?adequate`?\s*$", defense) is not None, "Defense is adequate")

    cumulative = (root / "cumulative-interpretation.md").read_text(encoding="utf-8").lower()
    if not starter:
        phrases = (
            "374", "224/75/75", "0.08513264", "48 true negatives", "23 false positives",
            "263 structural blanks", "-6.00000000", "91 missing", "0.83598751", "449 events",
            "151 censored", "6,208", "94 rows", "14.99587157", "28.20000000",
            "93.15000000", "18 accepted", "ten seeded", "three independent", "four claims", "deployment",
        )
        for phrase in phrases:
            require(phrase in cumulative, f"Cumulative interpretation includes: {phrase}")

    signoff = (root / "human-sign-off.md").read_text(encoding="utf-8").lower()
    if not starter:
        require("accountability statement" in signoff and "human" in signoff and "accept with conditions" in signoff, "Human sign-off is explicit")
        require("not a learner signature" in signoff or ("learner name" in signoff and "reviewer name" in signoff), "Sign-off scope is explicit")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
    if not starter:
        disposition_match = re.search(r"(?m)^- disposition:\s*`?(accept with conditions|accept|revise|refer)`?\s*$", progression)
        permission_match = re.search(r"(?m)^- module 07 permission:\s*`?(permitted|not permitted)`?\s*$", progression)
        require(disposition_match is not None, "Progression disposition is allowed")
        require(permission_match is not None, "Module 07 permission is explicit")
        allowed = disposition_match.group(1) in {"accept", "accept with conditions"}
        require((permission_match.group(1) == "permitted") == allowed, "Permission matches disposition")
        require("117" in progression and "48/23/2/2" in progression, "Progression preserves manifest and test counts")

    report = {
        "status": "pass", "mode": "starter" if starter else "complete",
        "checks_passed": len(checks), "manifest_rows": len(manifest), "course_points": "25.00",
    }
    print(f"FND-2 Checkpoint 2 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import assemble_checkpoint

    roots = (
        assemble_checkpoint.REFERENCE_CP1, assemble_checkpoint.REFERENCE_M04,
        assemble_checkpoint.REFERENCE_M05, assemble_checkpoint.REFERENCE_M06,
        assemble_checkpoint.REFERENCE_PUBLIC,
    )
    with tempfile.TemporaryDirectory(prefix="fnd2-checkpoint2-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, starter = base / "reference", base / "starter"
        assemble_checkpoint.assemble(reference, roots, reference=True)
        complete_report = validate(reference)
        assemble_checkpoint.assemble(starter, roots, reference=False)
        starter_report = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "Record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted prompted starter as complete")

        broken = base / "broken"
        shutil.copytree(reference, broken)
        (broken / "public-data/ma_hospital_capacity_time_2024_2026.csv").unlink()
        try:
            validate(broken)
        except ValidationError as error:
            assert "Manifest file exists" in str(error)
        else:
            raise AssertionError("Validator accepted missing immutable evidence")

        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        score_path = bad_score / "component-score.csv"
        score_path.write_text(score_path.read_text(encoding="utf-8").replace("V01,Validity aims and causal structure,4.00,4.00", "V01,Validity aims and causal structure,4.00,5.00"), encoding="utf-8", newline="")
        try:
            validate(bad_score)
        except ValidationError as error:
            assert "Earned points are in range" in str(error)
        else:
            raise AssertionError("Validator accepted out-of-range score")

        failed_gate = base / "failed-gate"
        shutil.copytree(reference, failed_gate)
        gate_path = failed_gate / "gate-results.csv"
        gate_path.write_text(gate_path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="")
        try:
            validate(failed_gate)
        except ValidationError as error:
            assert "All 25 gates pass" in str(error)
        else:
            raise AssertionError("Validator accepted a failed gate")

        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        progression_path = bad_progression / "progression-decision.md"
        progression_path.write_text(progression_path.read_text(encoding="utf-8").replace("- Module 07 permission: `permitted`", "- Module 07 permission: `not permitted`"), encoding="utf-8", newline="")
        try:
            validate(bad_progression)
        except ValidationError as error:
            assert "Permission matches disposition" in str(error)
        else:
            raise AssertionError("Validator accepted inconsistent progression")
    print(f"FND-2 Checkpoint 2 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken packages rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path, default=PACKAGE_ROOT)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        validate(args.checkpoint.resolve(), starter=args.starter)
    except (OSError, ValueError, KeyError, StopIteration, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

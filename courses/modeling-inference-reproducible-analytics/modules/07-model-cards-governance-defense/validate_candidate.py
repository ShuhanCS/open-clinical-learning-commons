"""Validate an assembled FND-2 Module 07 governed analytics candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
RECORD_FILES = (
    "README.md", "CHANGELOG.md", "release-notes.md", "environment-and-commands.md",
    "evidence-index.csv", "model-card.md", "performance-appendix.csv",
    "subgroup-equity-review.md", "monitoring-plan.csv", "drift-retraining-versioning.md",
    "rollback-stop-retirement.md", "model-use-recommendation.md", "reproducibility-audit.md",
    "accessibility-review.md", "ai-use.md", "human-sign-off.md", "handoff-brief.md",
    "technical-defense.md", "component-score.csv", "gate-results.csv",
    "release-checklist.csv", "conditions-register.csv", "reviewer-record.md",
    "progression-decision.md",
)
ROOT_FILES = (
    ".gitattributes", ".gitignore", "VERSION", "governance-contract.json",
    "assessment.md", "validate_candidate.py", "release-manifest.csv",
) + RECORD_FILES
SUPPLEMENT_HASHES = {
    "evidence/provenance/fnd1-final-release.json": "7afffdaeb0470d2ffc918570a0a2400a255ebe3f1a47cb467ab9e862dff32dd8",
    "evidence/provenance/fnd1-handoff-acceptance.md": "50b1a279cbcdf4ca642bbd4189e543a158cb3a1f7f26457216041ce216752a28",
    "evidence/provenance/fnd2-module01-source-record.yml": "f3ef7bb8ecbd892b70810a44f37ac146d7fde9b587e557ac145c732cf41cfc2b",
    "evidence/provenance/fnd2-module01-data-spec.md": "083f34ea5e58c2b5143bfa1efc3266150aee8f3a15515dcb677acf5d10642f19",
    "evidence/provenance/fnd2-module03-test-metrics.csv": "9d43a8085e835cbf368962acc37b0bed00bdfacf68e73ce87d0b359dee490bc9",
    "evidence/provenance/fnd2-module03-subgroup-metrics.csv": "7f95ec1f99a1f9f9bae6af566798a4f3aab9107681fe7e79c1ce27a821e07d24",
    "evidence/provenance/fnd2-module03-prediction-report.md": "8559a9b97a1cf540cf122577afeb16dfb7363aae5ddd9165ac7d26c34c8d8de7",
}
CRITERIA = ("M01", "R01", "E01", "V01", "G01", "H01")
AVAILABLE = tuple(Decimal(value) for value in ("5.00", "6.00", "7.00", "5.00", "6.00", "6.00"))
GATES = tuple(f"G{index:02d}" for index in range(1, 19))
PACKAGE_DISPOSITIONS = {"accept", "accept with conditions", "revise", "refer"}
MODEL_USES = {"teaching use only", "silent prospective validation only", "revise before further validation", "stop model use"}


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

    require(root.is_dir(), "Candidate directory exists")
    for relative in ROOT_FILES:
        require((root / relative).is_file(), f"Required root file exists: {relative}")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Candidate version is 0.1.0")
    contract = json.loads((root / "governance-contract.json").read_text(encoding="utf-8"))
    require(contract["module"]["id"] == "oclc-fnd2-07" and contract["module"]["commons_release"] == "0.47.0", "Module identity matches")
    require(contract["package"] == {"checkpoint_files": 130, "supplementary_files": 7, "module_control_files": 6, "manifest_rows": 143, "editable_records": 24, "assembled_files": 168}, "Package contract matches")
    require(contract["assessment"]["required_gates"] == 18 and contract["assessment"]["defense_questions"] == 10 and contract["assessment"]["monitoring_signals"] == 10, "Assessment contract matches")

    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"], "Manifest header matches")
    require(len(manifest) == 143, "Manifest has 143 rows")
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths) and len(paths) == len(set(paths)), "Manifest paths are sorted and unique")
    for row in manifest:
        relative = row["relative_path"]
        candidate = Path(relative)
        require(not candidate.is_absolute() and ".." not in candidate.parts, f"Manifest path is safe: {relative}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {relative}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {relative}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {relative}")
        require(row["source_version"] == "0.1.0" and row["role"].strip(), f"Manifest provenance matches: {relative}")
    require(sum(path.is_file() for path in root.rglob("*")) == 168, "Candidate has 168 files")
    for relative, digest in SUPPLEMENT_HASHES.items():
        require(sha256(root / relative) == digest, f"Supplementary fingerprint matches: {relative}")

    cp2 = root / "evidence/checkpoint2"
    require(sum(path.is_file() for path in cp2.rglob("*")) == 130, "Nested Checkpoint 2 has 130 files")
    require(sha256(cp2 / "release-manifest.csv") == "16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc", "Nested Checkpoint 2 manifest matches")
    nested = subprocess.run([sys.executable, str(cp2 / "validate_checkpoint.py"), str(cp2)], capture_output=True, text=True, check=False)
    require(nested.returncode == 0, "Nested Checkpoint 2 validation passes")

    _, test_predictions = read_csv(cp2 / "prior-checkpoint/modules/03-prediction-evaluation/outputs/test-predictions.csv")
    cells = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for row in test_predictions:
        cells[(int(row["observed"]), int(row["selected_label"]))] += 1
    require(len(test_predictions) == 75 and [cells[key] for key in ((0, 0), (0, 1), (1, 0), (1, 1))] == [48, 23, 2, 2], "Test confusion independently remains 48/23/2/2")
    _, metrics = read_csv(root / "evidence/provenance/fnd2-module03-test-metrics.csv")
    metric = {(row["model_id"], row["metric"]): row for row in metrics}
    require(metric[("ML01", "roc_auc")]["point"] == "0.58802817" and metric[("ML01", "brier")]["point"] == "0.05097579", "Model test metrics match")
    require(metric[("ML01", "roc_auc")]["lower95_stratified_bootstrap"] == "0.26760563" and metric[("ML01", "roc_auc")]["upper95_stratified_bootstrap"] == "0.91549296", "ROC uncertainty matches")
    _, subgroups = read_csv(root / "evidence/provenance/fnd2-module03-subgroup-metrics.csv")
    require(len(subgroups) == 10 and sum(row["suppressed"] == "yes" for row in subgroups) == 5, "Five of ten subgroup rows remain suppressed")
    _, forecast = read_csv(cp2 / "modules/05-forecasting-temporal-validation/outputs/forecast-predictions.csv")
    candidate_rows = [row for row in forecast if row["model_id"] == "HOLT_DAMPED"]
    errors = [float(row["actual"]) - float(row["prediction"]) for row in candidate_rows]
    require(f"{sum(abs(value) for value in errors) / len(errors):.8f}" == "14.99587157", "Forecast MAE independently recalculates")
    require(f"{math.sqrt(sum(value * value for value in errors) / len(errors)):.8f}" == "21.07855007", "Forecast RMSE independently recalculates")
    _, accepted = read_csv(cp2 / "modules/06-agent-assisted-modeling-testing/outputs/accepted-contract-tests.csv")
    _, failures = read_csv(cp2 / "modules/06-agent-assisted-modeling-testing/outputs/seeded-failure-results.csv")
    require(len(accepted) == 18 and all(row["status"] == "pass" for row in accepted), "All 18 accepted tests pass")
    require(len(failures) == 10 and all(row["status"] == "pass" and row["rejected"] == "yes" and row["intended_reason"] == "yes" for row in failures), "All ten failures reject as intended")

    for relative in RECORD_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")

    score_header, scores = read_csv(root / "component-score.csv")
    require(score_header == ["criterion_id", "component", "course_points_available", "points_earned", "status", "evidence"], "Score header matches")
    require(tuple(row["criterion_id"] for row in scores) == CRITERIA, "Score criteria match")
    require(tuple(Decimal(row["course_points_available"]) for row in scores) == AVAILABLE and sum(AVAILABLE) == Decimal("35.00"), "Available points total 35.00")
    if not starter:
        earned = tuple(Decimal(row["points_earned"]) for row in scores)
        require(all(Decimal("0") <= value <= available for value, available in zip(earned, AVAILABLE, strict=True)), "Earned points are in range")
        require(sum(earned) >= Decimal("28.00"), "Earned points meet 28.00 minimum")
        require(all(row["status"] in {"pass", "pass with conditions"} and row["evidence"].strip() for row in scores), "All score rows pass and cite evidence")

    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "reviewer_note"] and tuple(row["gate_id"] for row in gates) == GATES, "Gate contract matches")
    if not starter:
        require(all(row["status"] == "pass" and row["evidence"].strip() and row["reviewer_note"].strip() for row in gates), "All 18 gates pass with evidence")

    monitor_header, monitoring = read_csv(root / "monitoring-plan.csv")
    require(monitor_header == ["signal_id", "signal", "denominator", "window", "review_trigger", "owner", "action", "stop_condition"], "Monitoring header matches")
    require([row["signal_id"] for row in monitoring] == [f"S{index:02d}" for index in range(1, 11)], "Monitoring has ten ordered signals")
    if not starter:
        require(all(all(row[field].strip() for field in monitor_header) for row in monitoring), "Every monitoring signal is complete")

    appendix_header, appendix = read_csv(root / "performance-appendix.csv")
    require(appendix_header == ["measure", "value", "denominator_or_scope", "interval_or_comparator", "evidence_path", "interpretation_limit"], "Performance appendix header matches")
    if not starter:
        require(len(appendix) == 17 and all(all(row[field].strip() for field in appendix_header) for row in appendix), "Performance appendix has 17 complete rows")
    checklist_header, checklist = read_csv(root / "release-checklist.csv")
    require(checklist_header == ["check_id", "check", "status", "evidence", "owner"] and len(checklist) == 8, "Release checklist contract matches")
    if not starter:
        require(all(row["status"] == "pass" and row["evidence"].strip() and row["owner"].strip() for row in checklist), "Release checklist passes")
    condition_header, conditions = read_csv(root / "conditions-register.csv")
    require(condition_header == ["condition_id", "source", "status", "condition", "owner", "next_check", "verification", "escalation_trigger"] and len(conditions) >= 4, "Condition contract matches")
    if not starter:
        require(all(all(row[field].strip() for field in condition_header) for row in conditions), "Every condition is complete")

    defense = (root / "technical-defense.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\d+\.", defense)) == 10, "Defense has ten numbered answers")
    if not starter:
        require(re.search(r"(?im)^- Status:\s*`?adequate`?\s*$", defense) is not None, "Defense is adequate")
    model_card = (root / "model-card.md").read_text(encoding="utf-8").lower()
    if not starter:
        for phrase in ("synthetic", "four outcomes", "48 tn", "23 fp", "0.08513264", "five of ten", "teaching", "no model or forecast action", "deployment"):
            require(phrase in model_card, f"Model card includes: {phrase}")
    release_notes = (root / "release-notes.md").read_text(encoding="utf-8").lower()
    if not starter:
        require("fnd2-governed-candidate-v0.1.0" in release_notes and "not created before final-checkpoint acceptance" in release_notes, "Proposed tag remains uncreated")

    use_text = (root / "model-use-recommendation.md").read_text(encoding="utf-8").lower()
    progression = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
    if not starter:
        use_package = re.search(r"(?m)^- package disposition:\s*`?([^`\r\n]+)`?\s*$", use_text)
        use_model = re.search(r"(?m)^- model-use recommendation:\s*`?([^`\r\n]+)`?\s*$", use_text)
        prog_package = re.search(r"(?m)^- package disposition:\s*`?([^`\r\n]+)`?\s*$", progression)
        prog_model = re.search(r"(?m)^- model-use recommendation:\s*`?([^`\r\n]+)`?\s*$", progression)
        permission = re.search(r"(?m)^- final-checkpoint permission:\s*`?(permitted|not permitted)`?\s*$", progression)
        require(all((use_package, use_model, prog_package, prog_model, permission)), "Package use and progression lines are present")
        package_value, model_value = use_package.group(1).strip(), use_model.group(1).strip()
        require(package_value in PACKAGE_DISPOSITIONS and model_value in MODEL_USES, "Package and model-use values are allowed")
        require(prog_package.group(1).strip() == package_value and prog_model.group(1).strip() == model_value, "Decision records agree")
        allowed = package_value in {"accept", "accept with conditions"}
        require((permission.group(1) == "permitted") == allowed, "Final-checkpoint permission matches package disposition")
        require(package_value != model_value, "Package disposition and model-use recommendation are separate")

    signoff = (root / "human-sign-off.md").read_text(encoding="utf-8").lower()
    if not starter:
        require("accountability statement" in signoff and "accept with conditions" in signoff and "teaching use only" in signoff, "Human sign-off scope is explicit")
    report = {"status": "pass", "mode": "starter" if starter else "complete", "checks_passed": len(checks), "manifest_rows": 143, "course_points": "35.00"}
    print(f"FND-2 Module 07 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import assemble_candidate

    with tempfile.TemporaryDirectory(prefix="fnd2-module07-validate-") as temp_dir:
        base = Path(temp_dir)
        checkpoint = base / "checkpoint2"
        assemble_candidate.assemble_reference_checkpoint(checkpoint)
        reference, starter = base / "reference", base / "starter"
        assemble_candidate.assemble(checkpoint, reference, reference=True)
        complete_report = validate(reference)
        assemble_candidate.assemble(checkpoint, starter, reference=False)
        starter_report = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "Record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted prompted starter as complete")

        cases = []
        broken = base / "broken"
        shutil.copytree(reference, broken)
        (broken / "evidence/provenance/fnd2-module03-subgroup-metrics.csv").unlink()
        cases.append((broken, "Manifest file exists"))
        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        path = bad_score / "component-score.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("M01,Aim target time model and baseline,5.00,5.00", "M01,Aim target time model and baseline,5.00,6.00"), encoding="utf-8", newline="")
        cases.append((bad_score, "Earned points are in range"))
        bad_gate = base / "bad-gate"
        shutil.copytree(reference, bad_gate)
        path = bad_gate / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="")
        cases.append((bad_gate, "All 18 gates pass"))
        bad_monitor = base / "bad-monitor"
        shutil.copytree(reference, bad_monitor)
        path = bad_monitor / "monitoring-plan.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",data steward,", ",,"), encoding="utf-8", newline="")
        cases.append((bad_monitor, "Every monitoring signal is complete"))
        bad_decision = base / "bad-decision"
        shutil.copytree(reference, bad_decision)
        path = bad_decision / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Model-use recommendation: `teaching use only`", "- Model-use recommendation: `stop model use`"), encoding="utf-8", newline="")
        cases.append((bad_decision, "Decision records agree"))
        for candidate, expected in cases:
            try:
                validate(candidate)
            except ValidationError as error:
                assert expected in str(error), str(error)
            else:
                raise AssertionError(f"Validator accepted invalid candidate: {candidate.name}")
    print(f"FND-2 Module 07 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken candidates rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path, default=PACKAGE_ROOT)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        validate(args.candidate.resolve(), starter=args.starter)
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

"""Validate APP-2 Module 06 learner and reference workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
OUTPUT_FILES = (
    "upstream-inventory.csv", "analysis-checks.csv", "improvement-evidence.csv",
    "partner-question-register.csv", "transparent-weight-cells.csv", "split-registry.csv",
    "model-predictions.csv", "model-performance.csv", "calibration-bins.csv",
    "threshold-errors.csv", "response-weight-diagnostics.csv", "estimate-recovery.csv",
    "subgroup-model-audit.csv", "feature-importance.csv", "failure-cases.csv",
    "invariant-checks.csv", "build-report.json",
)
CONTROL_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "module06-contract.json",
    "feature-contract.csv", "partner-contract.csv", "environment.yml", "assessment.md",
    "build_partnered_improvement_ml.py", "build_workspace.py", "validate_workspace.py",
)
WORK_FILES = (
    "README.md", "engagement-status.md", "patient-partner-session.md",
    "interpretation-disagreement.csv", "improvement-brief.md", "driver-diagram.csv",
    "workflow.csv", "measure-registry.csv", "burden-access-review.md",
    "feedback-accountability.md", "ml-comparison.md", "failure-case-review.md",
    "responsible-claims.md", "reproducibility-check.md", "ai-use.md",
    "gate-results.csv", "progression-decision.md",
)
IMMUTABLE_FILES = CONTROL_FILES + tuple(f"outputs/{name}" for name in OUTPUT_FILES)
EXPECTED_SHAPES = {
    "upstream-inventory.csv": (13, 7),
    "analysis-checks.csv": (22, 5),
    "improvement-evidence.csv": (10, 6),
    "partner-question-register.csv": (12, 5),
    "transparent-weight-cells.csv": (13, 10),
    "split-registry.csv": (1255, 6),
    "model-predictions.csv": (377, 12),
    "model-performance.csv": (2, 15),
    "calibration-bins.csv": (10, 9),
    "threshold-errors.csv": (2, 10),
    "response-weight-diagnostics.csv": (3, 13),
    "estimate-recovery.csv": (12, 9),
    "subgroup-model-audit.csv": (26, 13),
    "feature-importance.csv": (8, 5),
    "failure-cases.csv": (22, 10),
    "invariant-checks.csv": (30, 5),
}
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b")
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")


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


def markdown_field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    root = root.resolve()
    source_package = root == MODULE_ROOT.resolve() and (root / "reference").is_dir()
    record_root = root / "template" if source_package and starter else (root / "reference" if source_package else root)
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    require(root.is_dir(), "Workspace directory exists")
    require(all((root / name).is_file() for name in CONTROL_FILES), "All immutable controls are present")
    require(all((root / "outputs" / name).is_file() for name in OUTPUT_FILES), "All generated evidence is present")
    require(all((record_root / name).is_file() for name in WORK_FILES), "All work records are present")

    if not source_package:
        expected = set(IMMUTABLE_FILES) | set(WORK_FILES) | {"release-manifest.csv"}
        actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        require(actual == expected, "Workspace has exactly 46 expected files")
        header, manifest = read_csv(root / "release-manifest.csv")
        require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
        require(len(manifest) == 28, "Manifest has 28 immutable rows")
        require([row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest paths are complete and sorted")
        for row in manifest:
            path = root / row["relative_path"]
            require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    source = (root / "source-record.yml").read_text(encoding="utf-8")
    source_values = (
        "module_id: oclc-app2-06", "commons_release: 0.61.0", "rows: 1255",
        "96e7b493aabf51bdb6c6072e2175ebe560a8ab211287983c6b38e851244e8d4a",
        "eb593a7883c10ff8b83456a4b66b7c8132a3a787d1151d1baf4093d21f10a0af",
        "dad581097558df657c8ffffb048e071bc51179c4e63e76b946b76661b32647fe",
        "real_patient_text_rows: 0", "actual_patient_partner_statements: 0",
        "comment_text_modeling: prohibited", "model_deployment: prohibited",
    )
    require(all(value in source for value in source_values), "Source identities and protection limits match")

    contract = json.loads((root / "module06-contract.json").read_text(encoding="utf-8"))
    require(contract["analysis_id"] == "app2-partnered-improvement-response-ml-v1", "Analysis identity matches")
    require(contract["module"] == {"id": "oclc-app2-06", "version": "0.1.0", "commons_release": "0.61.0", "week": 6, "hours": 16.0, "application_hours": 8.0, "ml_hours": 8.0, "course_points": 0, "checkpoint_points": 45}, "Module hours and points match")
    require(contract["eligible_features"] == ["age_band", "other_language_at_home", "income_group"], "Exactly three eligible fields match")
    require(contract["split"] == {"method": "train_test_split", "test_size": 0.3, "stratify": "response_status", "random_state": 20260830}, "Split contract matches")
    forest = contract["machine_learning_model"]
    require((forest["class"], forest["n_estimators"], forest["max_depth"], forest["min_samples_leaf"], forest["max_features"], forest["random_state"], forest["n_jobs"]) == ("RandomForestClassifier", 200, 3, 25, None, 20260830, 1), "Bounded random-forest contract matches")
    require(contract["factor_bounds"] == {"lower": 1.0, "upper": 3.0} and contract["response_threshold"] == 0.60, "Factor bounds and threshold match")
    require(contract["weight_stability"] == {"minimum_ess_ratio": 0.85, "maximum_largest_weight_share_percent": 3.0}, "Weight stability contract matches")
    require(contract["ml_changes_decision_if"] == {"minimum_composite_absolute_bias_improvement_pp": 0.5, "maximum_item_absolute_bias_worsening_pp": 0.25, "maximum_ml_minus_transparent_brier": 0.005, "all_weight_stability_rules_pass": True, "all_required_evidence_complete": True, "all_gates_pass": True}, "ML decision rule matches")

    feature_header, features = read_csv(root / "feature-contract.csv")
    require(feature_header == ["feature", "source", "eligible", "role", "transformation", "reason"] and len(features) == 22, "Feature contract has 22 rows")
    require([row["feature"] for row in features if row["eligible"] == "yes"] == contract["eligible_features"], "Only three fields are eligible")
    require(next(row for row in features if row["feature"] == "comment_text")["role"] == "prohibited", "Comment text is prohibited")
    require(all(row["eligible"] == "no" for row in features if row["feature"] in {"assigned_mode", "response_probability", "q22_truth", "q23_truth", "race_ethnicity", "insurance_coverage"}), "Generator truth and audit fields are excluded")

    partner_header, partner = read_csv(root / "partner-contract.csv")
    require(len(partner_header) == 6 and len(partner) == 12, "Partner contract has 12 requirements")
    require(all(row["required_before_session"] == "yes" for row in partner), "Every partner requirement is pre-session")
    require(all("pending" in row["alpha_status"] for row in partner), "Every alpha partner requirement remains pending")
    environment = (root / "environment.yml").read_text(encoding="utf-8")
    require(all(value in environment for value in ("python=3.12", "numpy=2.0.2", "pandas=3.0.3", "scikit-learn=1.9.0")), "Environment versions match")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require("awards no additional course points" in assessment and len(re.findall(r"(?m)^\d+\. ", assessment)) == 24, "Assessment has zero points and 24 gates")

    text_paths = [root / name for name in CONTROL_FILES if Path(name).suffix in {".md", ".json", ".yml", ".csv"}]
    record_paths = {record_root / name for name in WORK_FILES}
    text_paths += list(record_paths)
    for path in text_paths:
        content = path.read_text(encoding="utf-8")
        require("\u2013" not in content and "\u2014" not in content, f"Plain ASCII dashes: {path.name}")
        require(not PERSONAL_PATH.search(content), f"No personal absolute path: {path.name}")
        if starter and path in record_paths:
            require(bool(PLACEHOLDER.search(content)), f"Starter prompt is present: {path.name}")
        if not starter and path in record_paths:
            require(not PLACEHOLDER.search(content), f"Reference record is complete: {path.name}")

    tables: dict[str, list[dict[str, str]]] = {}
    for name, (rows_expected, fields_expected) in EXPECTED_SHAPES.items():
        header, rows = read_csv(root / "outputs" / name)
        require((len(rows), len(header)) == (rows_expected, fields_expected), f"Output shape matches: {name}")
        tables[name] = rows

    require(all(row["status"] == "accepted exact input" for row in tables["upstream-inventory.csv"]), "All 13 upstream inputs are accepted")
    require(all(row["status"] == "pass" for row in tables["analysis-checks.csv"]), "All 22 analysis checks pass")
    require(all(row["status"] == "pass" for row in tables["invariant-checks.csv"]), "All 30 invariants pass")

    split = tables["split-registry.csv"]
    require(sum(row["split"] == "training" for row in split) == 878 and sum(row["split"] == "evaluation" for row in split) == 377, "Split has 878 training and 377 evaluation rows")
    require(sum(row["split"] == "training" and row["response_status"] == "respondent" for row in split) == 547, "Training has 547 respondents")
    require(sum(row["split"] == "evaluation" and row["response_status"] == "respondent" for row in split) == 235, "Evaluation has 235 respondents")
    require(len({row["frame_record_id"] for row in split}) == 1255, "Split identities are unique")

    cells = tables["transparent-weight-cells.csv"]
    require(len(cells) == 13 and sum(row["bound_hit"] == "yes" for row in cells) == 1, "Transparent benchmark has 13 cells and one training cap hit")
    require(all(1.0 <= float(row["bounded_response_factor"]) <= 3.0 for row in cells), "Transparent cell factors are bounded")

    performance = {row["method"]: row for row in tables["model-performance.csv"]}
    require(set(performance) == {"transparent_benchmark", "bounded_random_forest"}, "Exactly two comparison methods are reported")
    require(performance["transparent_benchmark"]["base_weighted_brier"] == "0.22962545" and performance["bounded_random_forest"]["base_weighted_brier"] == "0.23135127", "Held-out Brier scores match")
    require(performance["transparent_benchmark"]["base_weighted_auc"] == "0.54335192" and performance["bounded_random_forest"]["base_weighted_auc"] == "0.53869891", "Held-out AUC values match")
    require((performance["transparent_benchmark"]["false_positive"], performance["transparent_benchmark"]["false_negative"], performance["bounded_random_forest"]["false_positive"], performance["bounded_random_forest"]["false_negative"]) == ("88", "51", "85", "55"), "Held-out response errors match")
    require(len(tables["calibration-bins.csv"]) == 10 and {row["calibration_group"] for row in tables["calibration-bins.csv"]} == {"1", "2", "3", "4", "5"}, "Both methods have five calibration groups")

    diagnostics = {row["method"]: row for row in tables["response-weight-diagnostics.csv"]}
    require(all(row["stability_status"] == "pass" for row in diagnostics.values()), "All three weight diagnostics pass")
    require(diagnostics["transparent_benchmark"]["factor_cap_hits"] == "3" and diagnostics["bounded_random_forest"]["factor_cap_hits"] == "0", "Evaluation factor-cap counts match")
    require(float(diagnostics["transparent_benchmark"]["effective_n_ratio"]) >= 0.85 and float(diagnostics["bounded_random_forest"]["effective_n_ratio"]) >= 0.85, "Adjusted effective sample sizes pass")

    recovery = {(row["measure"], row["estimator"]): row for row in tables["estimate-recovery.csv"]}
    require(recovery[("teaching_composite", "transparent_adjusted")]["absolute_bias_pp"] == "2.48289986", "Transparent composite bias matches")
    require(recovery[("teaching_composite", "bounded_ml_adjusted")]["absolute_bias_pp"] == "2.39922466", "ML composite bias matches")
    require(recovery[("Q22", "bounded_ml_adjusted")]["answered_n"] == "174" and recovery[("Q23", "bounded_ml_adjusted")]["answered_n"] == "179", "Item-specific answered denominators match")
    require(all(row["claim_limit"].endswith("not an official score") for row in tables["estimate-recovery.csv"]), "Known-truth claims remain bounded")

    subgroup = tables["subgroup-model-audit.csv"]
    unsupported = [row for row in subgroup if row["support_status"].startswith("suppress")]
    require(len(unsupported) == 8, "Four groups per method remain suppressed")
    require(all(row["base_weighted_brier"] == row["mean_predicted_response"] == row["observed_response"] == row["mean_respondent_factor"] == "" for row in unsupported), "Unsupported subgroup metrics remain blank")
    require(all(row["predictor_status"] == "audit only" for row in subgroup if row["dimension"] in {"insurance_coverage", "race_ethnicity"}), "Insurance and race remain audit only")

    importance = tables["feature-importance.csv"]
    require(abs(sum(float(row["importance"]) for row in importance) - 1.0) < 1e-7, "Feature importances sum to one")
    require({row["feature"] for row in importance} == {"age_band", "other_language_at_home", "income_group"}, "Importance output contains only eligible fields")
    require(len(tables["failure-cases.csv"]) == 22 and all(row["required_review"] for row in tables["failure-cases.csv"]), "All 22 failure cases have required review")

    report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
    require(report["status"] == "pass" and report["split"] == {"training_rows": 878, "training_respondents": 547, "evaluation_rows": 377, "evaluation_respondents": 235}, "Build report status and split match")
    require(report["comparison"] == {"composite_absolute_bias_improvement_pp": "0.08367520", "maximum_item_absolute_bias_worsening_pp": "-0.04991741", "ml_minus_transparent_brier": "0.00172582", "weight_stability": "pass", "ml_changes_response_adjustment_decision": "no"}, "Prespecified ML comparison result matches")
    require(report["partnership"]["actual_patient_partner_statements"] == 0 and report["points"] == {"module04": 25, "module05": 20, "module06": 0, "week6_total": 45}, "Partnership boundary and points match")

    if source_package:
        from build_partnered_improvement_ml import build
        with tempfile.TemporaryDirectory(prefix="app2-module06-validate-build-") as temp_dir:
            rebuilt = Path(temp_dir) / "outputs"
            build(COURSE_ROOT, rebuilt)
            require(all((root / "outputs" / name).read_bytes() == (rebuilt / name).read_bytes() for name in OUTPUT_FILES), "Committed evidence matches a fresh deterministic build")

    if starter:
        report_result = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 46}
        print(f"APP-2 Module 06 starter validation passed: {len(checks)} checks.")
        return report_result

    engagement = (record_root / "engagement-status.md").read_text(encoding="utf-8")
    require(markdown_field(engagement, "Record type") == "simulated curriculum reference, not actual patient engagement", "Engagement record is a labelled simulation")
    require(markdown_field(engagement, "Actual patient or caregiver statements in this package") == "0", "No actual partner statement is claimed")
    require(markdown_field(engagement, "Named patient or caregiver partner") == "pending before alpha", "Named partner remains an alpha condition")
    session = (record_root / "patient-partner-session.md").read_text(encoding="utf-8")
    require("simulated curriculum session" in session and "not an actual partner decision" in session, "Partner session retains simulation boundary")

    _, disagreements = read_csv(record_root / "interpretation-disagreement.csv")
    require(len(disagreements) == 8 and all(row["data_class"] == "simulated_reference" for row in disagreements), "Eight simulated interpretation records are labelled")
    require(all(row["disagreement"] in {"yes", "no"} and row["revision"] and row["owner"] for row in disagreements), "Disagreement revisions and owners are complete")
    _, drivers = read_csv(record_root / "driver-diagram.csv")
    require(len(drivers) == 14 and drivers[0]["level"] == "aim", "Driver diagram has one aim and 13 linked rows")
    _, workflow = read_csv(record_root / "workflow.csv")
    require(len(workflow) == 12 and all(row["owner"] and row["access_alternative"] and row["failure_response"] and row["stop_rule"] for row in workflow), "Twelve workflow steps have owners access and stop rules")
    _, measures = read_csv(record_root / "measure-registry.csv")
    require(len(measures) == 14 and {row["type"] for row in measures} == {"implementation", "process", "response", "outcome", "access", "balancing", "accountability", "safety"}, "Measure registry covers eight required types")
    require(all(row["numerator"] and row["denominator"] and row["missingness_rule"] and row["failure_response"] for row in measures), "Every measure has denominator missingness and failure response")

    ml_review = (record_root / "ml-comparison.md").read_text(encoding="utf-8")
    require(markdown_field(ml_review, "ML Brier score") == "0.23135127" and markdown_field(ml_review, "Transparent Brier score") == "0.22962545", "ML review cites exact Brier results")
    require(markdown_field(ml_review, "Decision") == "ML does not change the response-adjustment decision because the composite improvement is below 0.50 percentage points", "ML review applies the prespecified rule")
    failure_review = (record_root / "failure-case-review.md").read_text(encoding="utf-8")
    require(all(value in failure_review for value in ("22 held-out rows", "88 false positives", "51 false negatives", "85 false positives", "55 false negatives", "comment-text")), "Failure review covers exact errors and prohibited text modeling")
    claims = (record_root / "responsible-claims.md").read_text(encoding="utf-8")
    require(all(value in claims for value in ("cannot be described as patient testimony", "may not state that either method is fair", "targeting", "deployment")), "Responsible claims retain partnership model and deployment limits")

    _, gates = read_csv(record_root / "gate-results.csv")
    require(len(gates) == 24 and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 25)], "All 24 gates are present in order")
    require(all(row["status"] == "pass" and row["evidence"] for row in gates), "All construction gates pass with evidence")
    progression = (record_root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Week 6 score") == "45.00 of 45.00", "Week 6 score is 45 of 45")
    require(markdown_field(progression, "Module 06 points") == "0", "Module 06 adds no points")
    require(markdown_field(progression, "Progression") == "continue with conditions", "Progression is continue with conditions")
    require(markdown_field(progression, "ML changes response-adjustment decision") == "no", "ML does not change the decision")
    require(markdown_field(progression, "Teaching adjustment") == "retain transparent benchmark", "Transparent benchmark remains")
    require(markdown_field(progression, "Patient-partner status") == "simulated reference only; named actual partner review required before alpha", "Actual partner remains required")

    result = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 46 if not source_package else None}
    print(f"APP-2 Module 06 reference validation passed: {len(checks)} checks.")
    return result


def self_check() -> None:
    from build_workspace import assemble

    source = validate(MODULE_ROOT)
    with tempfile.TemporaryDirectory(prefix="app2-module06-validator-") as temp_dir:
        root = Path(temp_dir)
        reference, learner = root / "reference", root / "learner"
        assemble(reference, reference=True)
        assemble(learner)
        complete = validate(reference)
        starter = validate(learner, starter=True)

        changed = root / "changed"
        shutil.copytree(reference, changed)
        with (changed / "outputs" / "model-performance.csv").open("a", encoding="utf-8") as handle:
            handle.write("changed\n")
        try:
            validate(changed)
        except ValidationError as error:
            assert "Manifest bytes" in str(error)
        else:
            raise AssertionError("Changed model evidence was accepted")

        failed = root / "failed-gate"
        shutil.copytree(reference, failed)
        gate_path = failed / "gate-results.csv"
        gate_path.write_text(gate_path.read_text(encoding="utf-8").replace("G20,prespecified ML decision used,ml-comparison.md,pass", "G20,prespecified ML decision used,ml-comparison.md,fail", 1), encoding="utf-8", newline="\n")
        try:
            validate(failed)
        except ValidationError as error:
            assert "construction gates" in str(error)
        else:
            raise AssertionError("Failed gate was accepted")

        invalid = root / "invalid-progression"
        shutil.copytree(reference, invalid)
        progression_path = invalid / "progression-decision.md"
        progression_path.write_text(progression_path.read_text(encoding="utf-8").replace("`continue with conditions`", "`continue`", 1), encoding="utf-8", newline="\n")
        try:
            validate(invalid)
        except ValidationError as error:
            assert "continue with conditions" in str(error)
        else:
            raise AssertionError("Invalid progression was accepted")

        assert source["status"] == complete["status"] == starter["status"] == "pass"
    print("APP-2 Module 06 validator self-check passed: source, copied, starter, mutation, gate, and progression routes.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=MODULE_ROOT)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        print(json.dumps(validate(args.root, starter=args.starter), indent=2))
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

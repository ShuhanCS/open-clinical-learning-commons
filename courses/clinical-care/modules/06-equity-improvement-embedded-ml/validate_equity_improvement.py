"""Validate APP-1 Module 06 equity, improvement, and bounded-ML workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "equity-contract.csv", "model-contract.json",
    "feature-contract.csv", "environment.yml", "assessment.md", "build_equity_improvement.py",
    "build_workspace.py", "validate_equity_improvement.py",
)
WORK_FILES = (
    "README.md", "equity-review.md", "pathway-display.md", "improvement-brief.md", "driver-diagram.csv",
    "improvement-measures.csv", "ml-comparison.md", "failure-case-review.md", "reproducibility-check.md",
    "ai-use.md", "progression-decision.md",
)
OUTPUTS = {
    "analysis-checks.csv": (20, 5, 806, "733055dc9db2afb1c18cd8d182160d1841655908b61f01f89ff0ce686033f205"),
    "bootstrap-comparison.csv": (2, 8, 313, "f79acaf078eb518c895163fdfae1ddc1f138a300b2567e1e630ed44a753cc4f3"),
    "build-report.json": (None, None, 2330, "bf478aee4813ba6de13014c895f1843c17f87b627083e8651120666ccb92032e"),
    "calibration-bins.csv": (10, 7, 1184, "738557bcb5220b8531fe7f6ef49f017181f9262bd9b0331873482c1f3cae5b1f"),
    "equity-summary.csv": (12, 19, 3299, "8c83ea852b2b15a53386fa9bb9cff8960d8392ecc8b12202fce563ad7169831d"),
    "failure-cases.csv": (17, 11, 2775, "c674c581aa8d983a9d7db74f65d27934116fd0cfe1d8f0c607494f3d7e7eab24"),
    "feature-importance.csv": (4, 4, 386, "2e7d59f4117575d43834b77e4c9df7b8ab0b4d4f352289c40b49f1282518e8bd"),
    "model-performance.csv": (2, 17, 415, "0196c19a7069d003508f13e6361d7b97d920a511c88d2b58101598d5579a611b"),
    "model-predictions.csv": (143, 8, 14000, "69d99d4e3f84aa08af59685fa296643776ce62d552c3ef8bc7396ca9efad7da1"),
    "pathway-edges.csv": (10, 5, 328, "0170f7aa366edabd4392ff8ad8be658afb49ec7e8c7fb5c785cd4bc35242f86b"),
    "pathway-figure.svg": (None, None, 3263, "a72e8684c16a78f5b5b02c82ec7c8e5ffe824bad228081fbef2f37d4f0c5a1a5"),
    "pathway-nodes.csv": (11, 5, 1016, "8cbd40831657807bd855e7c107438f889fae6406605d3a952161a31c83b9506b"),
    "split-registry.csv": (476, 6, 42615, "32f8afb8b311c52743e170787b45e6e2b4906d885398e6e51074a4e5e0ee4bdf"),
    "subgroup-model-audit.csv": (24, 12, 4469, "a907964f736a608c8a351c6220e24453443c71fa1d50f40907097084f055a747"),
    "threshold-errors.csv": (8, 7, 843, "62f9988be22ae8b528b597e068060ef85e86a034b06ef64aea20761f8cd8de38"),
}
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}


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
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    required = set(IMMUTABLE_FILES) | set(WORK_FILES)
    is_source_package = root == MODULE_ROOT.resolve() and (root / "template").is_dir()
    require(root.is_dir(), "Workspace directory exists")
    require(all((root / name).is_file() for name in required), "All fixed and work files are present")
    if not is_source_package:
        expected_files = required | {"workspace-manifest.csv"}
        if not starter:
            expected_files |= {f"outputs/{name}" for name in OUTPUTS}
        actual_files = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        require(actual_files == expected_files, f"Workspace has exactly {23 if starter else 38} expected files")
        header, manifest = read_csv(root / "workspace-manifest.csv")
        require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
        require(len(manifest) == 11 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest has 11 sorted immutable rows")
        for row in manifest:
            path = root / row["relative_path"]
            require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    source = (root / "source-record.yml").read_text(encoding="utf-8")
    source_values = (
        "commons_release: 0.54.0", "rows: 476", "fields: 26", "fields: 49", "fields: 12",
        "7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e",
        "c5d372e777ff3b190859e7c418b87c4f165776b84fb86346db700fa39f516a6e",
        "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5",
        "e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e",
    )
    require(all(value in source for value in source_values), "Source identities and accepted handoff match")
    contract = json.loads((root / "model-contract.json").read_text(encoding="utf-8"))
    require(contract["analysis_id"] == "app1-equity-improvement-ml-v1" and contract["prediction_time"] == "day-30 landmark", "Analysis identity and prediction time match")
    require(contract["features"] == ["age_decade_from_40", "any_prior_acute", "prior_365d_condition_count", "index_inpatient"], "Four transparent features remain fixed")
    require(contract["split"] == {"order": ["index_start", "patient_id"], "training_rows": 333, "evaluation_rows": 143, "evaluation_events": 17, "randomness": "none"}, "Time-ordered split remains fixed")
    forest = contract["machine_learning_model"]
    require((forest["n_estimators"], forest["max_depth"], forest["min_samples_leaf"], forest["max_features"], forest["random_state"], forest["n_jobs"]) == (200, 3, 15, None, 20260830, 1), "Bounded random-forest contract matches")
    require(contract["threshold"] == 0.20 and contract["bootstrap"] == {"replicates": 1000, "seed": 20260830, "method": "paired stratified person resampling"}, "Threshold and bootstrap match")
    require(contract["equity_support"]["merge_small_groups"] == "prohibited" and contract["equity_support"]["ranking"] == "prohibited", "Group merging and ranking remain prohibited")

    equity_header, equity_contract = read_csv(root / "equity-contract.csv")
    require(len(equity_header) == 13 and len(equity_contract) == 12, "Equity contract has 12 fixed groups")
    require([row["group"] for row in equity_contract] == ["18-44", "45-64", "65+", "F", "M", "asian", "black", "native", "other", "white", "hispanic", "nonhispanic"], "Equity groups remain in fixed order")
    require(all((row["process_minimum_people"], row["process_minimum_numerator"], row["process_minimum_complement"]) == ("30", "5", "5") for row in equity_contract), "Process support rule matches")
    feature_header, features = read_csv(root / "feature-contract.csv")
    require(feature_header == ["feature", "source_field", "transformation", "eligible", "role", "reason"] and len(features) == 12, "Feature contract header and rows match")
    require([row["feature"] for row in features if row["eligible"] == "yes"] == contract["features"], "Exactly four features are eligible")
    require(all(row["eligible"] == "no" for row in features if row["feature"] in {"landmark_exposure", "teaching_site_id", "expected_probability", "gender", "race", "ethnicity", "event_indicator", "post_landmark_fields"}), "Leaked and audit-only fields remain prohibited")

    environment = (root / "environment.yml").read_text(encoding="utf-8")
    require(all(value in environment for value in ("python=3.12", "numpy=2.0.2", "pandas=3.0.3", "scikit-learn=1.9.0", "statsmodels=0.14.6")), "Environment versions match")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require("awards no additional course points" in assessment and len(re.findall(r"(?m)^\d+\. ", assessment)) == 24, "Assessment has zero extra points and 24 gates")

    text_files = [name for name in required if Path(name).suffix.lower() in {".md", ".json", ".yml", ".csv"}]
    for name in text_files:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if starter and name in WORK_FILES:
            require(bool(PLACEHOLDER.search(text)), f"Starter prompt is present: {name}")
        if not starter and name in WORK_FILES:
            require(not PLACEHOLDER.search(text), f"Work file is complete: {name}")
    if starter:
        require(not (root / "outputs").exists(), "Starter has no prebuilt outputs")
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 23}
        print(f"APP-1 Module 06 starter validation passed: {len(checks)} checks.")
        return report

    output_root = root / "outputs"
    require(all((output_root / name).is_file() for name in OUTPUTS), "All 15 outputs are present")
    tables: dict[str, list[dict[str, str]]] = {}
    for name, (expected_rows, expected_fields, expected_bytes, expected_hash) in OUTPUTS.items():
        path = output_root / name
        require(path.stat().st_size == expected_bytes, f"Output bytes match: {name}")
        require(sha256(path) == expected_hash, f"Output SHA-256 matches: {name}")
        if path.suffix == ".csv":
            header, rows = read_csv(path)
            require(len(rows) == expected_rows and len(header) == expected_fields, f"Output shape matches: {name}")
            tables[name] = rows

    require(all(row["status"] == "pass" for row in tables["analysis-checks.csv"]), "All 20 analysis checks pass")
    checks_by_id = {row["check_id"]: row for row in tables["analysis-checks.csv"]}
    require((checks_by_id["CHK01"]["observed"], checks_by_id["CHK02"]["observed"], checks_by_id["CHK03"]["observed"]) == ("476", "87", "129"), "Population outcome and follow-up counts match")
    require((checks_by_id["CHK05"]["observed"], checks_by_id["CHK06"]["observed"], checks_by_id["CHK07"]["observed"], checks_by_id["CHK08"]["observed"]) == ("333", "70", "143", "17"), "Training and evaluation counts match")

    equity = {(row["dimension"], row["group"]): row for row in tables["equity-summary.csv"]}
    require(equity[("age_band", "18-44")]["followup_proportion"] == "0.24637681" and equity[("age_band", "65+")]["followup_proportion"] == "0.35064935", "Age process summaries match")
    require(equity[("source_recorded_gender", "F")]["followup_numerator"] == "74" and equity[("source_recorded_gender", "M")]["followup_numerator"] == "55", "Source-recorded gender counts match")
    require(equity[("source_recorded_race", "native")]["followup_proportion"] == "" and equity[("source_recorded_race", "other")]["followup_proportion"] == "", "Small race process estimates remain suppressed")
    require(equity[("source_recorded_race", "asian")]["outcome_proportion"] == "" and equity[("source_recorded_race", "black")]["observed_expected_ratio"] == "1.33806044", "Outcome support and O/E result match")
    require(all(row["field_missing"] == "0" for row in equity.values()) and sum(row["outcome_support"].startswith("suppress") for row in equity.values()) == 3, "Missingness and outcome suppression are explicit")

    nodes = {row["node_id"]: row for row in tables["pathway-nodes.csv"]}
    require([nodes[f"N{i:02d}"]["count"] for i in range(1, 8)] == ["476", "129", "347", "25", "104", "62", "285"], "Observed pathway counts reconcile")
    require(all(nodes[f"N{i:02d}"]["evidence_status"] == "prospective collection" and nodes[f"N{i:02d}"]["count"] == "" for i in range(8, 12)), "Unobserved prospective states remain blank")
    edges = tables["pathway-edges.csv"]
    require(sum(int(row["count"]) for row in edges[:2]) == 476 and all(row["count"] == "" for row in edges[6:]), "Pathway edges conserve people and separate proposed collection")
    svg = (output_root / "pathway-figure.svg").read_text(encoding="utf-8")
    require(all(value in svg for value in ("aria-labelledby=\"title desc\"", "<title", "<desc", "476", "129", "347", "not observed", "pathway-nodes.csv", "pathway-edges.csv")), "Pathway figure is accessible and routes to exact tables")

    split = tables["split-registry.csv"]
    require(len({row["patient_id"] for row in split}) == 476 and [row["split_order"] for row in split] == [str(i) for i in range(1, 477)], "Split registry conserves ordered people")
    require(sum(row["split"] == "training" for row in split) == 333 and sum(row["split"] == "evaluation" for row in split) == 143, "Split registry sizes match")
    require(sum(int(row["event_indicator"]) for row in split if row["split"] == "evaluation") == 17, "Evaluation event count matches")
    predictions = tables["model-predictions.csv"]
    require(len({row["patient_id"] for row in predictions}) == 143 and all(row["threshold"] == "0.20000000" for row in predictions), "Predictions cover fixed evaluation rows at one threshold")

    performance = {row["model"]: row for row in tables["model-performance.csv"]}
    expected_performance = {
        "transparent": ("0.09609243", "0.66363212", "0.34684826", "-0.85765595", "0.98604197", "109", "17", "9", "8", "25", "44"),
        "bounded_rf": ("0.10745654", "0.62371615", "0.37750998", "-1.04707642", "0.64579740", "77", "49", "6", "11", "60", "67"),
    }
    for model, expected in expected_performance.items():
        row = performance[model]
        observed = tuple(row[key] for key in ("brier", "roc_auc", "log_loss", "calibration_intercept", "calibration_slope", "tn", "fp", "fn", "tp", "flagged", "weighted_error_cost"))
        require(observed == expected, f"Held-out performance matches: {model}")
    bootstrap = {row["metric"]: row for row in tables["bootstrap-comparison.csv"]}
    require((bootstrap["brier"]["point_difference"], bootstrap["brier"]["lower95"], bootstrap["brier"]["upper95"]) == ("0.01136411", "-0.00489999", "0.02602160"), "Paired Brier comparison matches")
    require((bootstrap["roc_auc"]["point_difference"], bootstrap["roc_auc"]["lower95"], bootstrap["roc_auc"]["upper95"]) == ("-0.03991597", "-0.16059757", "0.11721522") and all(row["replicates"] == "1000" for row in bootstrap.values()), "Paired AUC comparison and replicates match")
    calibration = tables["calibration-bins.csv"]
    require(sum(int(row["rows"]) for row in calibration if row["model"] == "transparent") == 143 and sum(int(row["rows"]) for row in calibration if row["model"] == "bounded_rf") == 143, "Calibration bins conserve evaluation rows")
    thresholds = tables["threshold-errors.csv"]
    require(sum(int(row["weighted_cost"]) for row in thresholds if row["model"] == "transparent") == 44 and sum(int(row["weighted_cost"]) for row in thresholds if row["model"] == "bounded_rf") == 67, "Threshold error costs reconcile")
    require(all("educational sensitivity" in row["cost_status"] for row in thresholds), "Error costs remain educational")

    subgroups = tables["subgroup-model-audit.csv"]
    require(sum(row["support"] == "report with boundary" for row in subgroups) == 12 and sum(row["support"].startswith("suppress") for row in subgroups) == 12, "Supported and suppressed model-audit rows match")
    require(all(row["brier"] == row["roc_auc"] == "" for row in subgroups if row["support"].startswith("suppress")), "Unsupported model metrics stay blank")
    subgroup = {(row["dimension"], row["group"], row["model"]): row for row in subgroups}
    require(subgroup[("source_recorded_gender", "F", "transparent")]["brier"] == "0.07740934" and subgroup[("source_recorded_gender", "F", "bounded_rf")]["brier"] == "0.10356741", "Supported gender audit matches")
    require(subgroup[("source_recorded_race", "white", "transparent")]["roc_auc"] == "0.71983409" and subgroup[("source_recorded_race", "white", "bounded_rf")]["roc_auc"] == "0.73755656", "Supported race audit matches")
    features_output = tables["feature-importance.csv"]
    require([row["feature"] for row in features_output] == contract["features"] and [row["importance"] for row in features_output] == ["0.35570506", "0.00000000", "0.33334882", "0.31094612"], "Bounded-RF feature importances match")
    failures = tables["failure-cases.csv"]
    require(sum(row["error_type"] == "false_negative" and row["model"] == "transparent" for row in failures) == 9 and sum(row["error_type"] == "false_negative" and row["model"] == "bounded_rf" for row in failures) == 6, "Every false negative is present")
    require({(row["model"], row["count"]) for row in failures if row["error_type"] == "false_positive_aggregate"} == {("transparent", "17"), ("bounded_rf", "49")}, "Aggregate false-positive burden matches")

    build_report = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(build_report["module"] == "oclc-app1-06" and build_report["commons_release"] == "0.54.0" and build_report["analysis_checks"] == 20, "Build report identity matches")
    require(build_report["reference_findings"]["ml_changes_improvement_decision"] == "no" and build_report["reference_findings"]["implementation_authorization"] == "not authorized", "Build report preserves decision boundaries")

    equity_review = (root / "equity-review.md").read_text(encoding="utf-8").lower()
    require(all(value in equity_review for value in ("question retained", "0.24637681", "0.35064935", "native (6 people)", "asian outcome", "not evidence that any group received unfair care")), "Equity review has exact evidence and bounded conclusion")
    pathway = (root / "pathway-display.md").read_text(encoding="utf-8").lower()
    require(all(value in pathway for value in ("476", "129", "347", "25", "104", "62", "285", "does not show whether follow-up was offered", "without relying on color")), "Pathway alternative is complete")
    improvement = (root / "improvement-brief.md").read_text(encoding="utf-8").lower()
    require(all(value in improvement for value in ("capacity-aware scheduling", "patient preference", "0.27993975", "not authorized", "model deployment")), "Improvement brief is feasible and bounded")
    driver_header, drivers = read_csv(root / "driver-diagram.csv")
    require(driver_header == ["driver_id", "level", "parent", "statement", "measure_link", "candidate_change", "status", "claim_limit"] and len(drivers) == 11, "Driver diagram has an aim and ten drivers")
    measure_header, measures = read_csv(root / "improvement-measures.csv")
    require(len(measure_header) == 12 and len(measures) == 7 and {row["role"] for row in measures} == {"implementation", "process", "outcome", "access", "balancing", "safety"}, "Improvement registry covers every required measure role")
    require(all(row["reference_status"].startswith("not available retrospectively") or "not attributable" in row["interpretation"] for row in measures), "Prospective measures are not fabricated from retrospective data")
    ml = (root / "ml-comparison.md").read_text(encoding="utf-8").lower()
    require(all(value in ml for value in ("0.09609243", "0.10745654", "32 false positives", "35 flags", "0.01136411", "does ml change the improvement decision: `no`", "clinical model deployment: `prohibited`")), "ML comparison has exact evidence and decision")
    failure = (root / "failure-case-review.md").read_text(encoding="utf-8").lower()
    require(all(value in failure for value in ("9 for the transparent", "6 for the bounded", "17 for the transparent", "49 for the random", "no clinical story", "deployment failure")), "Failure-case review is complete")
    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require(all(value in reproducibility for value in ("15 files", "two complete builds match byte for byte", "changed-cohort result: `rejected`", "leaked-feature result: `rejected`", "split randomness: `none`")), "Reproduction and mutation results are complete")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in ai_fields), "AI-use record has every accountable field")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Module 06 gate result") == "24 of 24 pass" and markdown_field(progression, "Week 6 cumulative score") == "45.00 of 45.00", "Gates and cumulative score match")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 07 permission")
    require(disposition in ALLOWED_PROGRESSION and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction")), "Module 07 permission matches progression")
    require(markdown_field(progression, "Clinical implementation") == "prohibited" and markdown_field(progression, "Model deployment") == "prohibited", "Implementation and deployment remain prohibited")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) >= 8, "Progression has at least eight owned conditions")

    report = {"status": "pass", "mode": "complete", "checks_passed": len(checks), "assembled_files": 38 if not is_source_package else None}
    print(f"APP-1 Module 06 complete validation passed: {len(checks)} checks.")
    return report


def rejected(action, expected_message: str) -> None:
    try:
        action()
    except (ValidationError, ValueError, OSError) as error:
        if expected_message not in str(error):
            raise AssertionError(f"Expected {expected_message!r}, got {error!r}") from error
    else:
        raise AssertionError(f"Mutation was accepted; expected {expected_message!r}")


def self_check() -> None:
    import build_equity_improvement
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app1-module06-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner = base / "reference", base / "learner"
        build_workspace.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_equity_improvement.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_workspace.assemble(learner)
        starter = validate(learner, starter=True)

        changed_output = base / "changed-output"
        shutil.copytree(reference, changed_output)
        path = changed_output / "outputs/model-performance.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("0.09609243", "0.19609243", 1), encoding="utf-8", newline="\n")
        rejected(lambda: validate(changed_output), "Output SHA-256 matches: model-performance.csv")

        changed_contract = base / "changed-contract"
        shutil.copytree(reference, changed_contract)
        path = changed_contract / "model-contract.json"
        path.write_text(path.read_text(encoding="utf-8").replace('"training_rows": 333', '"training_rows": 332', 1), encoding="utf-8", newline="\n")
        rejected(lambda: validate(changed_contract), "Manifest SHA-256 matches: model-contract.json")

        invalid_progression = base / "invalid-progression"
        shutil.copytree(reference, invalid_progression)
        path = invalid_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("45.00 of 45.00", "46.00 of 45.00", 1), encoding="utf-8", newline="\n")
        rejected(lambda: validate(invalid_progression), "Gates and cumulative score match")

        mutated_cohort = base / "analysis-cohort.csv"
        shutil.copy2(build_equity_improvement.DEFAULT_COHORT, mutated_cohort)
        with mutated_cohort.open("a", encoding="utf-8") as handle:
            handle.write("changed\n")
        rejected(lambda: build_equity_improvement.build(mutated_cohort, build_equity_improvement.DEFAULT_CARE, build_equity_improvement.DEFAULT_EXPECTED, base / "mutated-build"), "analysis cohort fingerprint changed")

    print(f"APP-1 Module 06 validator self-check passed: {complete['checks_passed']} complete checks and {starter['checks_passed']} starter checks; copied and mutation routes verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.workspace:
            parser.error("workspace is required unless --self-check is used")
        validate(args.workspace, starter=args.starter)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

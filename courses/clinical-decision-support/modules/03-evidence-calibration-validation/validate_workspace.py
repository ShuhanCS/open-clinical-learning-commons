"""Validate an APP-4 Module 03 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import re
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORD_FILES = (
    "evidence-release.md", "cohort-target-contract.csv", "survey-design-audit.csv",
    "model-specification.csv", "performance-interpretation.md", "calibration-audit.csv",
    "threshold-consequence-audit.csv", "decision-curve-interpretation.md",
    "transport-stress-audit.csv", "subgroup-support-audit.csv", "evidence-limitations.md",
    "week3-component-release.md", "claim-boundary.csv", "ai-use.md",
    "progression-decision.md",
)
EXPECTED_EVIDENCE_MANIFEST = "b226b33cc0ba2cec0efe2a5046357b10431941e0c9e286f9be889de05321c9a3"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else Path.open
    if path.suffix == ".gz":
        with opener(path, "rt", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    with opener(path, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_builder():
    path = ROOT / "build_workspace.py"
    spec = importlib.util.spec_from_file_location("app4_module03_builder", path)
    if spec is None or spec.loader is None:
        raise ValueError("Cannot load the Module 03 workspace builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_manifest(workspace: Path) -> list[dict[str, str]]:
    manifest = read_csv(workspace / "release-manifest.csv")
    if len(manifest) != 102:
        raise ValueError(f"Expected 102 immutable rows, found {len(manifest)}")
    for row in manifest:
        path = workspace / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]):
            raise ValueError(f"Immutable bytes changed: {row['relative_path']}")
        if sha256(path) != row["sha256"]:
            raise ValueError(f"Immutable hash changed: {row['relative_path']}")
    if sum(path.is_file() for path in workspace.rglob("*")) != 118:
        raise ValueError("Workspace file count changed")
    return manifest


def validate_inheritance(workspace: Path) -> None:
    root = workspace / "inherited" / "module02"
    module02 = json.loads((root / "decision-contract.json").read_text(encoding="utf-8"))
    source = module02["synthetic_release"]
    if (
        source["fhir_files"], source["resource_rows"], source["duplicate_resource_ids_within_file"],
        source["rule_cases"],
    ) != (25, 811803, 11109, 16):
        raise ValueError("Module 02 synthetic inheritance changed")
    if module02["fixtures"]["threshold"] != "0.20 arbitrary mechanics-only fixture, not estimated, recommended, selected, or accepted":
        raise ValueError("Module 02 threshold boundary changed")
    if any(module02["authority"][key] != "prohibited" for key in (
        "clinical_threshold_acceptance", "real_patient_scoring", "clinical_alerting",
        "clinical_action", "implementation", "deployment",
    )):
        raise ValueError("Module 02 authority boundary changed")
    module01 = json.loads((root / "inherited" / "module01" / "decision-contract.json").read_text(encoding="utf-8"))
    public = module01["public_release"]
    if (
        public["complete_xpt_files"], public["source_rows"], public["field_inventory_rows"],
        public["duplicate_seqn_rows"],
    ) != (16, 145563, 442, 0):
        raise ValueError("Module 01 public inheritance changed")


def validate_evidence(workspace: Path) -> dict[str, object]:
    root = workspace / "data" / "evidence"
    evidence_manifest = root / "evidence-manifest.csv"
    if sha256(evidence_manifest) != EXPECTED_EVIDENCE_MANIFEST:
        raise ValueError("Evidence manifest identity changed")
    manifest = read_csv(evidence_manifest)
    if len(manifest) != 17:
        raise ValueError("Evidence manifest must contain 17 files")
    for row in manifest:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise ValueError(f"Evidence output changed: {row['relative_path']}")
        if len(read_csv(path)) != int(row["rows"]) if not path.name.endswith(".json") else int(row["rows"]) != 1:
            raise ValueError(f"Evidence row count changed: {row['relative_path']}")
    report = json.loads((root / "build-report.json").read_text(encoding="utf-8"))
    if (
        report["source_files"], report["source_component_rows"], report["age_eligible_rows"],
        report["model_rows"], report["model_events"],
    ) != (16, 145563, 14892, 7544, 328):
        raise ValueError("Evidence release totals changed")
    if report["accepted_threshold"] is not None or report["module02_mock_threshold"]["status"] != "rejected mechanics fixture; not an evidence candidate":
        raise ValueError("Threshold authority changed")
    expected_partitions = {
        "development": (3652, 156),
        "temporal_holdout": (1806, 97),
        "transport_stress": (2086, 75),
    }
    for partition, expected in expected_partitions.items():
        actual = report["partitions"][partition]
        if (actual["rows"], actual["events"]) != expected:
            raise ValueError(f"Partition changed: {partition}")
    invariants = read_csv(root / "invariants.csv")
    if len(invariants) != 20 or any(row["status"] != "pass" for row in invariants):
        raise ValueError("Evidence invariants failed")
    predictions = read_csv(root / "predictions.csv.gz")
    if len(predictions) != 7544 or sum(int(row["outcome_hba1c_ge_6_5"]) for row in predictions) != 328:
        raise ValueError("Prediction cohort changed")
    if any(not 0 < float(row["model_probability"]) < 1 for row in predictions):
        raise ValueError("Model probabilities left the open unit interval")
    performance = read_csv(root / "performance.csv")
    if len(performance) != 6:
        raise ValueError("Performance table changed")
    holdout = next(row for row in performance if row["partition"] == "temporal_holdout" and row["model"] == "transparent_weighted_logit")
    transport = next(row for row in performance if row["partition"] == "transport_stress" and row["model"] == "transparent_weighted_logit")
    if (holdout["weighted_roc_auc"], holdout["weighted_brier"], transport["weighted_roc_auc"], transport["weighted_brier"]) != (
        "0.68783144", "0.02811126", "0.68422573", "0.03175435",
    ):
        raise ValueError("Evaluation performance changed")
    calibration = read_csv(root / "calibration.csv")
    if len(calibration) != 3:
        raise ValueError("Calibration table changed")
    thresholds = read_csv(root / "threshold-audit.csv")
    candidates = {"0.02000000", "0.03000000", "0.04000000", "0.05000000", "0.07500000", "0.10000000"}
    if len(thresholds) != 21 or {row["threshold"] for row in thresholds if row["threshold_status"].startswith("evidence candidate")} != candidates:
        raise ValueError("Candidate threshold set changed")
    if sum(row["threshold"] == "0.20000000" and row["threshold_status"].startswith("rejected") for row in thresholds) != 3:
        raise ValueError("Mock threshold is not rejected in every partition")
    subgroups = read_csv(root / "subgroup-support.csv")
    if len(subgroups) != 48:
        raise ValueError("Subgroup table changed")
    for row in subgroups:
        suppressed = row["support_status"].startswith("suppress")
        if suppressed and (row["weighted_brier"] or row["weighted_roc_auc"]):
            raise ValueError("Suppressed subgroup performance was populated")
        if row["threshold_metrics"] != "not calculated because no threshold is accepted":
            raise ValueError("Subgroup threshold authority changed")
    bootstrap = read_csv(root / "bootstrap-intervals.csv")
    if len(bootstrap) != 48 or any(row["valid_replicates"] != "500" or row["requested_replicates"] != "500" for row in bootstrap):
        raise ValueError("Bootstrap release changed")
    if len(read_csv(root / "net-benefit.csv")) != 63 or len(read_csv(root / "transport-comparison.csv")) != 13:
        raise ValueError("Decision or transport evidence changed")
    return report


def validate_records(workspace: Path, mode: str) -> None:
    for relative in RECORD_FILES:
        path = workspace / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        text = path.read_text(encoding="utf-8")
        if mode == "complete" and "REPLACE" in text:
            raise ValueError(f"Complete record contains placeholder: {relative}")
        if mode == "starter" and "REPLACE" not in text:
            raise ValueError(f"Starter record appears copied or completed: {relative}")
        if ":\\Users\\" in text or ":/Users/" in text:
            raise ValueError(f"Personal local path found: {relative}")
    if mode == "starter":
        return
    release = (workspace / "evidence-release.md").read_text(encoding="utf-8")
    for value in (EXPECTED_EVIDENCE_MANIFEST, "14,892", "7,544", "328", "20 of 20 pass"):
        if value not in release:
            raise ValueError(f"Evidence release omits {value}")
    cohort = read_csv(workspace / "cohort-target-contract.csv")
    if len(cohort) != 9 or not any(row["element"] == "outcome" and "not diagnosis" in row["claim_limit"] for row in cohort):
        raise ValueError("Cohort or non-diagnosis contract is incomplete")
    survey = read_csv(workspace / "survey-design-audit.csv")
    if len(survey) != 4 or not any(row["weight_rule"].startswith("cycle-specific WTPH2YR") for row in survey):
        raise ValueError("Survey-design audit is incomplete")
    model = read_csv(workspace / "model-specification.csv")
    if len(model) != 10 or not any(row["element"] == "retuning" and row["status"] == "prohibited" for row in model):
        raise ValueError("Model specification permits retuning")
    performance = (workspace / "performance-interpretation.md").read_text(encoding="utf-8")
    for value in ("0.68783144", "0.68422573", "does not show enough by itself to choose a threshold"):
        if value not in performance:
            raise ValueError(f"Performance interpretation omits {value}")
    calibration = read_csv(workspace / "calibration-audit.csv")
    if len(calibration) != 4 or not any(row["partition"] == "transport_stress" and row["calibration_slope"] == "0.81620710" for row in calibration):
        raise ValueError("Calibration audit changed")
    thresholds = read_csv(workspace / "threshold-consequence-audit.csv")
    if len(thresholds) != 7 or sum("not selected or accepted" in row["status"] for row in thresholds) != 6:
        raise ValueError("Threshold audit does not preserve all candidates")
    if not any(row["threshold"] == "0.20000000" and row["reference_decision"].startswith("reject") for row in thresholds):
        raise ValueError("Threshold audit does not reject the mock value")
    decision_curve = (workspace / "decision-curve-interpretation.md").read_text(encoding="utf-8")
    if "cannot establish patient benefit" not in decision_curve or "does not authorize an alert" not in decision_curve:
        raise ValueError("Decision-curve claim boundary is incomplete")
    transport = read_csv(workspace / "transport-stress-audit.csv")
    if len(transport) != 11 or any(not row["prohibited_inference"] for row in transport):
        raise ValueError("Transport stress audit is incomplete")
    subgroups = read_csv(workspace / "subgroup-support-audit.csv")
    if len(subgroups) != 14 or sum(row["support_status"] == "suppress performance" for row in subgroups) < 5:
        raise ValueError("Subgroup support audit is incomplete")
    limitations = (workspace / "evidence-limitations.md").read_text(encoding="utf-8")
    if len(re.findall(r"(?m)^\d+\.", limitations)) != 13:
        raise ValueError("Evidence limitations are incomplete")
    week3 = (workspace / "week3-component-release.md").read_text(encoding="utf-8")
    if "Module 04 may not begin" not in week3 or "No threshold has been selected or accepted" not in week3:
        raise ValueError("Week 3 handoff bypasses its gate")
    claims = read_csv(workspace / "claim-boundary.csv")
    if len(claims) != 12 or sum(row["status"] == "prohibited" for row in claims) < 8:
        raise ValueError("Claim boundary is incomplete")
    ai = (workspace / "ai-use.md").read_text(encoding="utf-8")
    if "no diagnosis, threshold selection or acceptance" not in ai or "independent checks" not in ai.lower():
        raise ValueError("AI-use record is incomplete")
    progression = (workspace / "progression-decision.md").read_text(encoding="utf-8")
    if "`continue with conditions`" not in progression or "Do not begin Module 04" not in progression:
        raise ValueError("Progression decision bypasses Checkpoint 01")
    all_text = "\n".join((workspace / relative).read_text(encoding="utf-8") for relative in RECORD_FILES)
    forbidden = (
        r"(?i)accepted clinical threshold:\s*0\.\d+",
        r"(?i)the model diagnoses diabetes",
        r"(?i)authorized for (clinical use|deployment|real-patient scoring)",
    )
    if any(re.search(pattern, all_text) for pattern in forbidden):
        raise ValueError("Assessed records claim prohibited authority")


def validate(workspace: Path, mode: str) -> dict[str, object]:
    workspace = workspace.resolve()
    if mode not in {"complete", "starter"}:
        raise ValueError("Mode must be complete or starter")
    validate_manifest(workspace)
    validate_inheritance(workspace)
    report = validate_evidence(workspace)
    validate_records(workspace, mode)
    return {
        "status": "pass",
        "mode": mode,
        "checks": 224 if mode == "complete" else 174,
        "immutable_rows": 102,
        "evidence_files": 17,
        "model_rows": report["model_rows"],
        "model_events": report["model_events"],
    }


def expect_failure(workspace: Path, mode: str, phrase: str) -> None:
    try:
        validate(workspace, mode)
    except (OSError, ValueError) as error:
        if phrase.lower() not in str(error).lower():
            raise AssertionError(f"Expected failure containing {phrase!r}, received {error!r}") from error
    else:
        raise AssertionError(f"Validation unexpectedly passed; expected {phrase!r}")


def self_check() -> None:
    builder = load_builder()
    with tempfile.TemporaryDirectory(prefix="app4-module03-validate-") as temporary:
        base = Path(temporary)
        complete, starter = base / "complete", base / "starter"
        builder.assemble(complete, reference=True)
        builder.assemble(starter)
        complete_report = validate(complete, "complete")
        starter_report = validate(starter, "starter")

        immutable = complete / "data" / "evidence" / "performance.csv"
        original = immutable.read_bytes()
        immutable.write_bytes(original + b"changed")
        expect_failure(complete, "complete", "immutable")
        immutable.write_bytes(original)

        copied = starter / "evidence-release.md"
        starter_original = copied.read_bytes()
        copied.write_bytes((complete / "evidence-release.md").read_bytes())
        expect_failure(starter, "starter", "copied")
        copied.write_bytes(starter_original)

        missing = complete / "calibration-audit.csv"
        missing_original = missing.read_bytes()
        missing.unlink()
        expect_failure(complete, "complete", "file count")
        missing.write_bytes(missing_original)

        progression = complete / "progression-decision.md"
        progression_original = progression.read_text(encoding="utf-8")
        progression.write_text(progression_original + "\nAccepted clinical threshold: 0.04\n", encoding="utf-8")
        expect_failure(complete, "complete", "prohibited authority")
        progression.write_text(progression_original, encoding="utf-8")

        performance = complete / "performance-interpretation.md"
        performance_original = performance.read_text(encoding="utf-8")
        performance.write_text(performance_original + "\nThe model diagnoses diabetes.\n", encoding="utf-8")
        expect_failure(complete, "complete", "prohibited authority")
        performance.write_text(performance_original, encoding="utf-8")

        model = complete / "model-specification.csv"
        model_original = model.read_text(encoding="utf-8")
        model.write_text(model_original.replace("retuning,none on temporal holdout or transport,prohibited", "retuning,on temporal holdout,accepted"), encoding="utf-8")
        expect_failure(complete, "complete", "retuning")
        model.write_text(model_original, encoding="utf-8")

        week3 = complete / "week3-component-release.md"
        week3_original = week3.read_text(encoding="utf-8")
        week3.write_text(week3_original + "\nAuthorized for deployment.\n", encoding="utf-8")
        expect_failure(complete, "complete", "prohibited authority")
        week3.write_text(week3_original, encoding="utf-8")

        assert validate(complete, "complete")["status"] == "pass"
        assert complete_report["checks"] == 224 and starter_report["checks"] == 174
    print("APP-4 Module 03 validator self-check passed: complete, starter, mutation, copy, threshold, diagnosis, retuning, and deployment routes.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--mode", choices=("complete", "starter"))
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace and args.mode:
            print(json.dumps(validate(args.workspace, args.mode), indent=2))
        else:
            parser.error("provide --workspace and --mode, or choose --self-check")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

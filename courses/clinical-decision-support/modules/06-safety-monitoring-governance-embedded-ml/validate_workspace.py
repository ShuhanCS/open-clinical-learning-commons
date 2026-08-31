"""Validate an APP-4 Module 06 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from build_evidence import OUTPUT_FILES, read_csv as evidence_csv, verify as verify_evidence
from build_workspace import CONTROL_FILES, MODULE05_EXPECTED, RECORD_FILES, assemble


PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD)\b|(?:^|,)incomplete(?:,|$)", re.MULTILINE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
CSV_CONTRACTS = {
    "hazard-review.csv": (("hazard_id", "control_adequacy", "residual_risk", "owner_confirmation", "disposition", "status"), 22),
    "monitoring-plan.csv": (("measure_id", "source_review", "cadence_review", "owner_review", "threshold_origin_review", "unavailable_state_review", "human_action_review", "status"), 20),
    "incident-escalation-review.csv": (("rule_id", "trigger_review", "owner_review", "escalation_review", "fallback_review", "automatic_action", "status"), 12),
    "fallback-stop-restart-retirement.csv": (("rule_id", "fallback", "stop_condition", "restart_evidence", "retirement_condition", "decision_owner", "status"), 12),
    "governance-accountability.csv": (("role", "accountable_for", "decision_right", "evidence_required", "escalates_to", "status"), 8),
    "threshold-burden-review.csv": (("partition", "threshold", "threshold_role", "burden_review", "missed_case_review", "decision", "status"), 12),
    "subgroup-drift-review.csv": (("review_id", "partition_or_scope", "evidence", "support_boundary", "decision", "status"), 4),
    "checkpoint-score-carryforward.csv": (("criterion_id", "criterion", "points_available", "points_awarded", "evidence", "status"), 4),
    "gate-results.csv": (("gate_id", "domain", "status", "evidence", "noncompensable_reason"), 22),
}
MARKDOWN_FIELDS = {
    "safety-case.md": {
        "Disposition": "continue with conditions", "Hazards reviewed": "22 of 22",
        "Inherited Module 05 hazards": "17 of 17 preserved", "Monitoring measures": "20 of 20 complete",
        "Escalation rules": "12 of 12 human owned", "Automatic actions": "0",
        "Residual authority boundary": "nonproduction curriculum construction only",
    },
    "silent-failure-monitoring.md": {
        "Definition": "a received request with no response, no terminal trace, and no human notice",
        "Independent ledgers": "request, response, terminal trace, and human notice",
        "Trigger": "one or more reconciled silent failures", "Owner": "patient-safety owner",
        "Rate claim": "none; the seeded event does not estimate a clinical silent-failure rate",
    },
    "ml-contract-review.md": {
        "Contract status": "frozen before evaluation", "Common rows": "7,544",
        "Random state": "7400600", "Search or tuning": "none", "Accepted threshold": "none",
    },
    "model-comparison.md": {
        "Transparent decision": "retain transparent model", "Replacement rules": "8 of 11 pass",
        "Failed rules": "R03, R04, and R08", "Temporal-holdout AUC difference": "-0.00743486",
        "Transport-stress AUC difference": "-0.01928938", "Worst supported subgroup AUC degradation": "0.10385240",
        "Accepted threshold": "none", "Clinical authority": "none",
    },
    "leakage-interpretability-review.md": {
        "Leakage tests": "12 of 12 pass", "Model fits": "one fixed development-only fit",
        "Holdout-guided tuning": "none", "Predictor importances": "three global impurity importances sum to 1.00000000",
    },
    "progression-checkpoint02-handoff.md": {
        "Progression": "continue with conditions", "Module 06 points": "0.00",
        "Module 06 gates": "22 of 22 pass", "Week 6 score": "25.00 of 25.00, counted once",
        "Accepted threshold": "none", "ML decision": "retain transparent model; 8 of 11 replacement rules pass",
        "Checkpoint 02 permission": "permitted for cumulative Week 6 curriculum assembly only",
        "Clinical and production authority": "prohibited",
    },
}


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
    match = re.search(rf"^- {re.escape(label)}: `([^`]+)`\.$", text, flags=re.MULTILINE)
    return match.group(1) if match else None


def validate(workspace: Path, complete: bool = False) -> dict[str, object]:
    workspace = workspace.resolve()
    checks = 0

    def require(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise ValueError(message)

    require(workspace.is_dir(), "Workspace does not exist")
    manifest_path = workspace / "release-manifest.csv"
    require(manifest_path.is_file(), "release-manifest.csv is missing")
    fields, manifest = read_csv(manifest_path)
    require(fields == ["relative_path", "bytes", "sha256", "role", "source_release"], "Release manifest schema changed")
    require(len(manifest) == 369, "Expected 369 immutable manifest rows")
    require(len({row["relative_path"] for row in manifest}) == 369, "Immutable manifest paths must be unique")
    for row in manifest:
        path = workspace / row["relative_path"]
        require(path.is_file(), f"Immutable file missing: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable byte count changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable hash changed: {row['relative_path']}")
    files = sum(path.is_file() for path in workspace.rglob("*") if "__pycache__" not in path.parts)
    require(files == 387, "Expected 387 assembled files")
    require(all((workspace / path).is_file() for path in CONTROL_FILES + OUTPUT_FILES + RECORD_FILES), "Required module file missing")

    module05 = workspace / "upstream/module05"
    upstream_manifest = module05 / "release-manifest.csv"
    require(upstream_manifest.is_file(), "Module 05 release manifest missing")
    require(upstream_manifest.stat().st_size == MODULE05_EXPECTED["manifest_bytes"], "Module 05 manifest bytes changed")
    require(sha256(upstream_manifest) == MODULE05_EXPECTED["manifest_sha256"], "Module 05 manifest hash changed")
    _, upstream_rows = read_csv(upstream_manifest)
    require(len(upstream_rows) == 324, "Expected 324 Module 05 immutable rows")
    require(sum(path.is_file() for path in module05.rglob("*") if "__pycache__" not in path.parts) == 341, "Expected complete 341-file Module 05 workspace")
    module05_release = json.loads((module05 / "release.json").read_text(encoding="utf-8"))
    require(module05_release["sandbox"]["cases"] == 31, "All 31 Module 05 cases must remain")
    require(module05_release["sandbox"]["silent_failures_detected"] == 1, "Detected silent failure must remain")
    require(module05_release["sandbox"]["accessibility_defects_blocked"] == 1, "Blocked accessibility defect must remain")
    require(module05_release["design"] == {"id": "panel-t003", "threshold": "0.03000000", "threshold_status": "unaccepted sandbox fixture", "accepted_threshold": None}, "Module 05 design or threshold role changed")
    _, inherited_gates = read_csv(module05 / "gate-results.csv")
    require(len(inherited_gates) == 20 and all(row["status"] == "pass" for row in inherited_gates), "All 20 Module 05 gates must remain")
    _, inherited_failures = read_csv(module05 / "failure-mode-register.csv")
    require([row["failure_id"] for row in inherited_failures] == [f"FM{index:02d}" for index in range(1, 18)], "All 17 Module 05 failures must remain")

    verify_evidence(workspace / "outputs")
    report = json.loads((workspace / "outputs/build-report.json").read_text(encoding="utf-8"))
    release = json.loads((workspace / "release.json").read_text(encoding="utf-8"))
    contract = json.loads((workspace / "decision-contract.json").read_text(encoding="utf-8"))
    ml_contract = json.loads((workspace / "ml-contract.json").read_text(encoding="utf-8"))
    require(release["module"] == {"id": "oclc-app4-06", "title": "Safety case, monitoring, governance, and embedded machine learning", "version": "0.1.0", "commons_release": "0.83.0", "hours": 16.0, "course_points": 0}, "Module release identity changed")
    require(release["workspace"] == {"immutable_manifest_rows": 369, "editable_records": 17, "assembled_files": 387}, "Workspace release contract changed")
    require(release["evidence"]["ml_decision"] == "retain transparent model" and release["evidence"]["replacement_rules_passed"] == 8, "Module release ML decision changed")
    require(contract["assessment"] == {"gates": 22, "points_added": 0, "checkpoint_score": "25.00 of 25.00, counted once", "passing_disposition": "continue with conditions"}, "Assessment contract changed")
    require(contract["protected_design"]["id"] == "panel-t003" and contract["protected_design"]["accepted_threshold"] is None, "Protected design or threshold changed")
    require(all(value == "prohibited" for value in contract["authority"].values()), "Authority contract expanded")
    require(ml_contract["challenger"] == {"class": "sklearn.ensemble.GradientBoostingClassifier", "n_estimators": 80, "learning_rate": 0.05, "max_depth": 2, "min_samples_leaf": 50, "subsample": 1.0, "random_state": 7400600, "search_or_tuning": "none"}, "Fixed challenger settings changed")
    require(ml_contract["candidate_thresholds"] == [0.02, 0.03, 0.04, 0.05, 0.075, 0.1], "Candidate thresholds changed")
    require(report["challenger"]["replacement_rules_passed"] == 8 and report["challenger"]["decision"] == "retain transparent model", "Generated challenger decision changed")

    record_texts = {}
    for relative in RECORD_FILES:
        text = (workspace / relative).read_text(encoding="utf-8")
        record_texts[relative] = text
        require(not PERSONAL_PATH.search(text), f"Personal filesystem path found in {relative}")
    if not complete:
        require(all(PLACEHOLDER.search(record_texts[relative]) for relative in RECORD_FILES), "Every learner record must remain visibly incomplete")
    else:
        require(all(not PLACEHOLDER.search(text) for text in record_texts.values()), "Complete reference contains a placeholder")
        for relative, (expected_fields, expected_rows) in CSV_CONTRACTS.items():
            actual_fields, rows = read_csv(workspace / relative)
            require(tuple(actual_fields) == expected_fields, f"Record schema changed: {relative}")
            require(len(rows) == expected_rows, f"Record row count changed: {relative}")
            require(all(row["status"] == "pass" for row in rows), f"Record contains a failed review: {relative}")
        for relative, expected in MARKDOWN_FIELDS.items():
            text = record_texts[relative]
            for label, value in expected.items():
                require(markdown_field(text, label) == value, f"{relative} changed field: {label}")
        _, hazards = read_csv(workspace / "hazard-review.csv")
        require([row["hazard_id"] for row in hazards] == [f"H{index:02d}" for index in range(1, 23)], "Hazard review is incomplete")
        _, measures = read_csv(workspace / "monitoring-plan.csv")
        require([row["measure_id"] for row in measures] == [f"M{index:02d}" for index in range(1, 21)], "Monitoring plan is incomplete")
        require(all(row["owner_review"].endswith("confirmed") for row in measures), "Every monitoring measure needs a confirmed owner")
        _, escalations = read_csv(workspace / "incident-escalation-review.csv")
        require([row["rule_id"] for row in escalations] == [f"E{index:02d}" for index in range(1, 13)] and all(row["automatic_action"] == "none" for row in escalations), "Human escalation review changed")
        _, life_cycle = read_csv(workspace / "fallback-stop-restart-retirement.csv")
        require([row["rule_id"] for row in life_cycle] == [f"E{index:02d}" for index in range(1, 13)] and all("automatically" not in " ".join(row.values()) for row in life_cycle), "Fallback, stop, restart, or retirement review changed")
        _, governance = read_csv(workspace / "governance-accountability.csv")
        require({row["role"] for row in governance} == {"clinical owner", "patient-safety owner", "data steward", "model steward", "equity steward", "accessibility owner", "service owner", "governance council"}, "Governance roles changed")
        _, thresholds = read_csv(workspace / "threshold-burden-review.csv")
        require({row["threshold"] for row in thresholds} == {"0.02000000", "0.03000000", "0.04000000", "0.05000000", "0.07500000", "0.10000000"}, "Threshold review changed")
        require(all(row["decision"] == "not selected or accepted" for row in thresholds), "A threshold was selected or accepted")
        _, score = read_csv(workspace / "checkpoint-score-carryforward.csv")
        require(sum(float(row["points_awarded"]) for row in score) == 25 and score[0]["points_awarded"] == "25.00", "Week 6 points must be 25 counted once")
        _, subgroup_review = read_csv(workspace / "subgroup-drift-review.csv")
        require(any("0.10385240" in row["evidence"] and row["decision"] == "replacement rule R08 fails" for row in subgroup_review), "Subgroup replacement failure changed")
        _, gates = read_csv(workspace / "gate-results.csv")
        require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 23)] and all(row["status"] == "pass" for row in gates), "All 22 Module 06 gates must pass")
        rules = evidence_csv(workspace / "outputs/replacement-rules.csv")
        require([row["rule_id"] for row in rules if row["status"] == "fail"] == ["R03", "R04", "R08"], "Replacement failures changed")
        ai = record_texts["ai-use.md"]
        require("Human-owned decisions" in ai and "accepting a threshold" in ai and "Prohibited agent actions" in ai, "AI accountability boundary changed")
        reproducibility = record_texts["reproducibility-check.md"]
        require(markdown_field(reproducibility, "Deliberate failure routes") == "22 rejected routes", "Failure-route count changed")

    return {
        "status": "pass",
        "mode": "reference" if complete else "learner",
        "checks": checks,
        "manifest_rows": len(manifest),
        "module05_files": 341,
        "records": len(RECORD_FILES),
        "hazards": 22,
        "monitoring_measures": 20,
        "replacement_rules_passed": 8 if complete else 0,
        "module06_gates_passed": 22 if complete else 0,
        "week6_points": 25 if complete else 0,
    }


def clone_tree(source: Path, target: Path) -> None:
    shutil.copytree(source, target, copy_function=os.link)


def break_link(path: Path) -> None:
    data = path.read_bytes()
    path.unlink()
    path.write_bytes(data)


def replace(path: Path, old: str, new: str) -> None:
    break_link(path)
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"Mutation source missing in {path.name}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def expect_failure(reference: Path, base: Path, name: str, mutate) -> None:
    case = base / name
    clone_tree(reference, case)
    mutate(case)
    try:
        validate(case, complete=True)
    except (ValueError, OSError, KeyError, json.JSONDecodeError):
        return
    raise AssertionError(f"Validator accepted deliberate failure: {name}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module06-validator-") as temporary:
        base = Path(temporary)
        reference, learner = base / "reference", base / "learner"
        assemble(reference, reference=True)
        assemble(learner)
        complete_report = validate(reference, complete=True)
        starter_report = validate(learner)
        copied = base / "copied-reference"
        shutil.copytree(reference, copied)
        completed = subprocess.run(
            [sys.executable, str(copied / "validate_workspace.py"), "--workspace", str(copied), "--complete"],
            capture_output=True, text=True, check=False,
        )
        if completed.returncode != 0:
            raise AssertionError(f"Copied validation failed: {completed.stderr}")
        failures = base / "failures"
        failures.mkdir()
        routes = (
            ("missing-record", lambda root: (root / "safety-case.md").unlink()),
            ("own-immutable", lambda root: replace(root / "outputs/invariant-checks.csv", "I22", "I23")),
            ("module05-manifest", lambda root: replace(root / "upstream/module05/release-manifest.csv", "324", "325")),
            ("nested-file", lambda root: (root / "upstream/module05/upstream/module04/VERSION").unlink()),
            ("hazard-count", lambda root: replace(root / "hazard-review.csv", "H22", "H23")),
            ("hidden-failure", lambda root: replace(root / "upstream/module05/failure-mode-register.csv", "FM15", "FM18")),
            ("hazard-status", lambda root: replace(root / "hazard-review.csv", "continue with conditions,pass", "continue with conditions,fail")),
            ("silent-ledger", lambda root: replace(root / "silent-failure-monitoring.md", "request, response, terminal trace, and human notice", "service log only")),
            ("monitoring-count", lambda root: replace(root / "monitoring-plan.csv", "M20", "M21")),
            ("monitor-owner", lambda root: replace(root / "monitoring-plan.csv", "clinical owner confirmed", "owner missing")),
            ("automatic-action", lambda root: replace(root / "incident-escalation-review.csv", ",none,pass", ",automatic alert,pass")),
            ("fallback-stop", lambda root: replace(root / "fallback-stop-restart-retirement.csv", "stop affected evaluation", "continue automatically")),
            ("governance-role", lambda root: replace(root / "governance-accountability.csv", "governance council,progression", "automated agent,progression")),
            ("model-tuning", lambda root: replace(root / "ml-contract.json", '"search_or_tuning": "none"', '"search_or_tuning": "grid search"')),
            ("model-output", lambda root: replace(root / "outputs/model-performance.csv", "0.68039658", "0.78039658")),
            ("threshold-accepted", lambda root: replace(root / "threshold-burden-review.csv", "not selected or accepted", "accepted")),
            ("challenger-accepted", lambda root: replace(root / "model-comparison.md", "retain transparent model", "replace with challenger")),
            ("subgroup-hidden", lambda root: replace(root / "subgroup-drift-review.csv", "0.10385240", "0.00385240")),
            ("score-inflation", lambda root: replace(root / "checkpoint-score-carryforward.csv", "0.00,0.00,required zero-point gates", "25.00,25.00,added points")),
            ("failed-gate", lambda root: replace(root / "gate-results.csv", "G22,progression and authority,pass", "G22,progression and authority,fail")),
            ("ai-authority", lambda root: replace(root / "ai-use.md", "accepting a threshold", "selecting an accepted threshold")),
            ("progression-authority", lambda root: replace(root / "progression-checkpoint02-handoff.md", "permitted for cumulative Week 6 curriculum assembly only", "permitted for production deployment")),
        )
        for name, mutate in routes:
            expect_failure(reference, failures, name, mutate)
        if complete_report["week6_points"] != 25 or complete_report["module06_gates_passed"] != 22:
            raise AssertionError("Complete reference summary changed")
        if starter_report["week6_points"] != 0 or starter_report["module06_gates_passed"] != 0:
            raise AssertionError("Learner starter was treated as complete")
    print(
        "APP-4 Module 06 validator self-check passed: "
        f"{complete_report['checks']} reference checks, {starter_report['checks']} learner checks, "
        "copied validation, and 22 rejected failure routes."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--complete", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            print(json.dumps(validate(args.workspace, complete=args.complete), indent=2, sort_keys=True))
        else:
            parser.error("choose --workspace or --self-check")
    except (OSError, ValueError, KeyError, AssertionError, ImportError, json.JSONDecodeError) as error:
        parser.exit(1, f"Workspace validation failed: {error}\n")


if __name__ == "__main__":
    main()

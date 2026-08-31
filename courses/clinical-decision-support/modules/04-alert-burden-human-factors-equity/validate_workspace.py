"""Validate an APP-4 Module 04 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from build_workflow import THRESHOLDS, fmt, read_gzip_csv, verify as verify_workflow
from build_workspace import (
    CHECKPOINT_EXPECTED,
    CONTROLS,
    GENERATED_FILES,
    NESTED_MANIFESTS,
    RECORD_FILES,
    assemble,
    sha256,
)


EXPECTED_THRESHOLD_TEXT = [fmt(value) for value in THRESHOLDS]
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer", "stop"}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def markdown_field(text: str, label: str) -> str | None:
    match = re.search(rf"^- {re.escape(label)}: `([^`]+)`\.$", text, flags=re.MULTILINE)
    return None if match is None else match.group(1)


def validate(root: Path, learner: bool = False) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValueError(message)
        checks.append(message)

    require(root.is_dir(), "Workspace root exists")
    required_top = set(CONTROLS) | set(GENERATED_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(all((root / relative).is_file() for relative in required_top), "Every top-level module file exists")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(
        manifest_header == ["relative_path", "bytes", "sha256", "role", "source_release"],
        "Release manifest header matches",
    )
    require(len(manifest) == 285, "Release manifest contains 285 immutable rows")
    require(len({row["relative_path"] for row in manifest}) == len(manifest), "Release manifest paths are unique")
    manifest_paths = {row["relative_path"] for row in manifest}
    require(set(CONTROLS).issubset(manifest_paths), "Release manifest covers all module controls")
    require(set(GENERATED_FILES).issubset(manifest_paths), "Release manifest covers all workflow evidence")
    upstream_paths = {path for path in manifest_paths if path.startswith("upstream/checkpoint01/")}
    require(len(upstream_paths) == 263, "Release manifest freezes all 263 Checkpoint 01 files")
    require(
        Counter(row["role"] for row in manifest)
        == Counter({"immutable module control": 12, "immutable synthetic workflow evidence": 10, "immutable accepted Week 3 checkpoint artifact": 263}),
        "Release manifest roles match the module contract",
    )
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Manifest hash matches: {row['relative_path']}")
    actual_files = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual_files == manifest_paths | set(RECORD_FILES) | {"release-manifest.csv"}, "Workspace contains only declared files")
    require(len(actual_files) == 302, "Workspace contains 302 files")

    checkpoint_root = root / "upstream/checkpoint01"
    candidate_manifest_path = checkpoint_root / "candidate-manifest.csv"
    require(candidate_manifest_path.stat().st_size == CHECKPOINT_EXPECTED["candidate_manifest_bytes"], "Checkpoint candidate-manifest bytes match")
    require(sha256(candidate_manifest_path) == CHECKPOINT_EXPECTED["candidate_manifest_sha256"], "Checkpoint candidate-manifest hash matches")
    candidate_header, candidate_rows = read_csv(candidate_manifest_path)
    require(
        candidate_header == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"],
        "Checkpoint candidate-manifest header matches",
    )
    require(len(candidate_rows) == 245, "Checkpoint candidate manifest contains 245 rows")
    for row in candidate_rows:
        path = checkpoint_root / row["relative_path"]
        require(path.is_file(), f"Checkpoint candidate exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Checkpoint candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Checkpoint candidate hash matches: {row['relative_path']}")

    nested_total = 0
    for relative, (expected_rows, expected_hash) in NESTED_MANIFESTS.items():
        nested_path = checkpoint_root / relative
        require(sha256(nested_path) == expected_hash, f"Accepted nested manifest hash matches: {relative}")
        nested_header, nested_rows = read_csv(nested_path)
        require(nested_header[:3] == ["relative_path", "bytes", "sha256"], f"Accepted nested manifest header matches: {relative}")
        require(len(nested_rows) == expected_rows, f"Accepted nested manifest row count matches: {relative}")
        module_root = nested_path.parent
        for row in nested_rows:
            path = module_root / row["relative_path"]
            require(path.is_file(), f"Nested immutable file exists: {relative}:{row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Nested immutable bytes match: {relative}:{row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Nested immutable hash matches: {relative}:{row['relative_path']}")
        nested_total += len(nested_rows)
    require(nested_total == 204, "All 204 nested immutable rows are verified")

    checkpoint_contract = json.loads((checkpoint_root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(checkpoint_contract["checkpoint_id"] == "oclc-app4-cp01" and checkpoint_contract["version"] == "0.1.0" and checkpoint_contract["commons_release"] == "0.80.0", "Checkpoint identity matches")
    require(checkpoint_contract["course_points"] == 40, "Checkpoint preserves 40 Week 3 points")
    require(checkpoint_contract["accepted_component_files"] == 245 and checkpoint_contract["accepted_immutable_rows"] == 204, "Checkpoint preserves accepted file counts")
    require(checkpoint_contract["thresholds"]["evidence_candidates"] == list(THRESHOLDS), "Checkpoint preserves six evidence candidates")
    require(checkpoint_contract["thresholds"]["accepted"] is None and "rejected mechanics fixture" in checkpoint_contract["thresholds"]["module02_mock"], "Checkpoint preserves no accepted threshold and rejected 0.20 fixture")
    require(checkpoint_contract["progression"]["module04_permission"] == "permitted for curriculum construction" and checkpoint_contract["progression"]["module05_permission"] == "prohibited until Module 04 passes", "Checkpoint progression boundary matches")
    require(all(value == "prohibited" for value in checkpoint_contract["authority"].values()), "Checkpoint clinical and deployment authority remains prohibited")

    workflow = verify_workflow(root)
    require(workflow["patient_rows"] == 1000 and workflow["encounter_rows"] == 1200, "Workflow frame and encounter counts match")
    require(workflow["candidate_rows"] == 7200 and workflow["design_rows"] == 13, "Workflow candidate and design counts match")
    require(workflow["session_rows"] == 720 and workflow["equity_rows"] == 108, "Workflow session and equity counts match")
    require(list(workflow["candidate_cards"].keys()) == EXPECTED_THRESHOLD_TEXT and list(workflow["candidate_cards"].values()) == [116, 12, 3, 3, 0, 0], "Workflow candidate-card counts match")
    require(workflow["output_manifest_sha256"] == "4ab020f4862fe06ea3c877d7302afa988b7069ce5922ddb2f578841d22838911", "Workflow output-manifest digest matches")

    contract = json.loads((root / "decision-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app4-04", "title": "Alert burden, human factors, and equity", "version": "0.1.0", "commons_release": "0.81.0", "course": "APP-4: Data for Clinical Decision Support", "week": 4, "hours": 16.5, "course_points": 25}, "Module decision identity matches")
    require(contract["upstream"]["candidate_manifest_sha256"] == CHECKPOINT_EXPECTED["candidate_manifest_sha256"] and contract["upstream"]["nested_immutable_rows"] == 204, "Decision contract binds the Week 3 handoff")
    require(contract["thresholds"]["evidence_candidates"] == list(THRESHOLDS) and contract["thresholds"]["candidate_cards"] == [116, 12, 3, 3, 0, 0], "Decision contract binds all candidate counts")
    require(contract["thresholds"]["accepted"] is None and contract["thresholds"]["agent_selection"] == "prohibited", "Decision contract denies threshold and agent selection")
    require(contract["designs"] == {"interruptive_banner": 6, "passive_context_panel": 6, "no_alert": 1, "generated_selection": None, "human_reference_recommendation": "panel-t003 for sandbox mechanics only"}, "Decision contract covers every design and human recommendation")
    require(contract["assessment"] == {"points": 25, "required_records": 16, "noncompensable_gates": 20}, "Assessment contract matches")
    require(contract["progression"]["reference"] == "continue with conditions" and contract["progression"]["module05_permission"] == "permitted for nonproduction sandbox construction", "Decision contract permits only Module 05 sandbox construction")
    require(all(value == "prohibited" for value in contract["authority"].values()), "Module clinical and deployment authority remains prohibited")

    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    require(release["status"] == "runnable release candidate" and release["module"]["id"] == "oclc-app4-04" and release["module"]["version"] == "0.1.0" and release["module"]["commons_release"] == "0.81.0", "Release identity matches")
    require(release["upstream"]["candidate_manifest_sha256"] == CHECKPOINT_EXPECTED["candidate_manifest_sha256"] and release["upstream"]["nested_immutable_rows"] == 204, "Release preserves checkpoint identity")
    require(release["workflow"]["candidate_event_rows"] == 7200 and release["workflow"]["candidate_cards"] == [116, 12, 3, 3, 0, 0], "Release workflow facts match")
    require(release["reference_decision"]["progression"] == "continue with conditions" and release["reference_decision"]["sandbox_design"] == "panel-t003" and release["reference_decision"]["accepted_threshold"] is None, "Release keeps the sandbox recommendation bounded")
    require(release["workspace"] == {"immutable_manifest_rows": 285, "editable_records": 16, "assembled_files": 302}, "Release workspace contract matches")
    require(all(value == "prohibited" for value in release["authority"].values()), "Release denies every clinical and deployment authority route")

    report = json.loads((root / "build-report.json").read_text(encoding="utf-8"))
    require(report["accepted_threshold"] is None and report["human_design_selection"] is None, "Generated evidence selects neither threshold nor design")
    require(report["module02_mock_threshold"] == {"value": "0.20000000", "status": "rejected mechanics fixture; excluded from Module 04 evidence"}, "Build report excludes the 0.20 fixture")
    require(all(value == "prohibited" for value in report["authority"].values()), "Build report denies clinical and deployment authority")

    candidate_rows = read_gzip_csv(root / "data/workflow/candidate-events.csv.gz")
    require({row["threshold"] for row in candidate_rows} == set(EXPECTED_THRESHOLD_TEXT), "Candidate events contain all six evidence candidates")
    require(all(row["threshold"] != "0.20000000" for row in candidate_rows), "Candidate events exclude the 0.20 fixture")
    require(all(row["threshold_status"] == "evidence candidate, not selected or accepted" for row in candidate_rows), "Every candidate event remains unaccepted")
    require(all("not an alert" in row["claim_limit"] for row in candidate_rows), "Every candidate event denies alert status")
    encounter_rows = read_gzip_csv(root / "data/workflow/encounter-opportunities.csv.gz")
    require(all(row["explicit_synthetic"] == "true" for row in encounter_rows), "Every encounter opportunity is explicitly synthetic")
    require(all(row["offline_teaching_score"] == "" for row in encounter_rows if row["candidate_frame_status"] == "eligible" and row["input_state"] != "ready"), "Unavailable encounter inputs remain unscored")
    design_header, designs = read_csv(root / "outputs/design-comparison.csv")
    require(len(designs) == 13 and Counter(row["design"] for row in designs) == Counter({"interruptive candidate banner": 6, "less interruptive passive contextual panel": 6, "no alert": 1}), "Design evidence compares banners, passive panels, and no alert")
    require({row["threshold"] for row in designs if row["threshold"]} == set(EXPECTED_THRESHOLD_TEXT), "Design evidence covers every threshold")
    require(all(row["design_status"] == "comparison only, not selected by generated evidence" for row in designs), "Generated design evidence makes no selection")
    equity_header, equity_rows = read_csv(root / "outputs/equity-slices.csv")
    require(len(equity_rows) == 108, "Equity evidence contains 108 slices")
    require(all(row["candidate_card_rate"] == "" for row in equity_rows if row["support_status"].startswith("suppress")), "Unsupported equity rates remain blank")
    require(all("not population prevalence" in row["claim_limit"] for row in equity_rows), "Every equity slice carries its claim limit")

    if learner:
        for relative in RECORD_FILES:
            require("REPLACE" in (root / relative).read_text(encoding="utf-8"), f"Learner starter remains incomplete: {relative}")
        return {"status": "pass", "mode": "learner", "checks": len(checks)}

    for relative in RECORD_FILES:
        require("REPLACE" not in (root / relative).read_text(encoding="utf-8"), f"Reference record is complete: {relative}")

    task = (root / "workflow-task-analysis.md").read_text(encoding="utf-8")
    for phrase in ("Primary user", "Workflow moment", "Expected action", "Nonaction", "Patient consequence", "Hidden work", "Stop authority", "Evidence boundary", "Module 05 sandbox"):
        require(phrase in task, f"Task analysis covers {phrase}")
    require(task.count("| 1 |") == 1 and task.count("| 7 |") == 1, "Task analysis contains seven ordered steps")

    csv_contracts = {
        "role-handoff-map.csv": (["role_id", "role", "decision_right", "input", "handoff", "hidden_work", "can_pause", "status"], 8, [f"R{number:02d}" for number in range(1, 9)]),
        "timing-interruption-review.csv": (["review_id", "moment_or_task", "scripted_evidence", "risk", "reference_design", "control", "owner", "status"], 8, [f"T{number:02d}" for number in range(1, 9)]),
        "burden-assumption-register.csv": (["assumption_id", "assumption", "value", "evidence", "status", "sensitivity", "claim_limit"], 10, [f"A{number:02d}" for number in range(1, 11)]),
        "usability-review.csv": (["heuristic_id", "heuristic", "finding", "risk", "required_control", "owner", "status"], 10, [f"U{number:02d}" for number in range(1, 11)]),
        "automation-bias-controls.csv": (["control_id", "risk", "control", "human_owner", "test_evidence", "status", "claim_limit"], 10, [f"AB{number:02d}" for number in range(1, 11)]),
        "access-equity-privacy-review.csv": (["review_id", "dimension_or_issue", "evidence", "status", "required_action", "prohibited_inference", "owner"], 12, [f"E{number:02d}" for number in range(1, 13)]),
    }
    id_fields = {
        "role-handoff-map.csv": "role_id",
        "timing-interruption-review.csv": "review_id",
        "burden-assumption-register.csv": "assumption_id",
        "usability-review.csv": "heuristic_id",
        "automation-bias-controls.csv": "control_id",
        "access-equity-privacy-review.csv": "review_id",
    }
    for relative, (expected_header, expected_rows, expected_ids) in csv_contracts.items():
        header, rows = read_csv(root / relative)
        require(header == expected_header, f"{relative} header matches")
        require(len(rows) == expected_rows, f"{relative} row count matches")
        require([row[id_fields[relative]] for row in rows] == expected_ids, f"{relative} identifiers are ordered")
        require(all(all(value.strip() for value in row.values()) for row in rows), f"{relative} contains no blank cells")
    _, role_rows = read_csv(root / "role-handoff-map.csv")
    require(all(row["can_pause"] == "true" for row in role_rows), "Every named role can pause the fictional concept")
    _, timing_rows = read_csv(root / "timing-interruption-review.csv")
    require(all(row["status"] in {"pass", "conditioned"} for row in timing_rows), "Every timing review has a passing or conditioned status")
    _, assumption_rows = read_csv(root / "burden-assumption-register.csv")
    require(all("not " in row["claim_limit"] for row in assumption_rows), "Every burden assumption denies an observed or clinical claim")
    _, usability_rows = read_csv(root / "usability-review.csv")
    require(all(row["status"] in {"pass", "conditioned"} for row in usability_rows), "Every usability item has a passing or conditioned status")
    _, automation_rows = read_csv(root / "automation-bias-controls.csv")
    require(all(row["status"] in {"pass", "conditioned"} for row in automation_rows), "Every automation-bias control has a passing or conditioned status")
    _, access_rows = read_csv(root / "access-equity-privacy-review.csv")
    require(any(row["dimension_or_issue"] == "Spanish language access" and row["status"] == "support rule not met" for row in access_rows), "Spanish language support limitation remains explicit")
    require(any(row["dimension_or_issue"] == "patient targeting" and row["status"] == "prohibited" for row in access_rows), "Patient targeting remains prohibited")

    design_review = (root / "candidate-design-review.md").read_text(encoding="utf-8")
    for threshold in EXPECTED_THRESHOLD_TEXT:
        require(threshold in design_review, f"Candidate design review covers {threshold}")
    for phrase in ("No alert", "panel-t003", "remains an unaccepted sandbox fixture", "no real-patient scoring", "no clinical threshold acceptance", "no clinical alerting", "no silent-mode evaluation", "no implementation", "no deployment"):
        require(phrase in design_review, f"Candidate design review includes {phrase}")
    require("0.20000000" not in design_review, "Candidate design evidence does not promote the 0.20 fixture")

    communication = (root / "patient-communication-hidden-work.md").read_text(encoding="utf-8")
    for phrase in ("qualified language", "screen-reader", "low-vision", "motor-access", "cognitive-support", "20.00 task minutes", "not measured labor", "No patient communication record authorizes"):
        require(phrase in communication, f"Patient communication record includes {phrase}")
    stops = (root / "override-stop-conditions.md").read_text(encoding="utf-8")
    require(all(f"S{number:02d}" in stops for number in range(1, 9)), "Override record contains eight stop conditions")
    for phrase in ("Human override", "Patient recourse", "Pause owners", "Default fallback", "Passing Module 04 does not satisfy"):
        require(phrase in stops, f"Override record includes {phrase}")
    evidence_release = (root / "workflow-evidence-release.md").read_text(encoding="utf-8")
    for phrase in (CHECKPOINT_EXPECTED["candidate_manifest_sha256"], "Nested immutable rows: 204", "Candidate event rows: 7,200", "Candidate cards by threshold: 116, 12, 3, 3, 0, and 0", "Accepted clinical threshold: none", "not observed burden"):
        require(phrase in evidence_release, f"Workflow evidence release includes {phrase}")

    score_header, score_rows = read_csv(root / "module-score.csv")
    require(score_header == ["criterion_id", "criterion", "possible_points", "earned_points", "status", "evidence"], "Module score header matches")
    require([row["criterion_id"] for row in score_rows] == [f"S{number:02d}" for number in range(1, 11)] + ["total"], "Module score criteria are complete and ordered")
    require(sum(float(row["possible_points"]) for row in score_rows[:-1]) == 25.0 and sum(float(row["earned_points"]) for row in score_rows[:-1]) == 25.0, "Module score sums to 25.00 of 25.00")
    require(score_rows[-1]["possible_points"] == "25.00" and score_rows[-1]["earned_points"] == "25.00" and score_rows[-1]["status"] == "complete", "Module score total is exact")
    require(all(row["status"] == "complete" for row in score_rows), "Every Module 04 score criterion is complete")

    gate_header, gate_rows = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "domain", "status", "evidence", "noncompensable_reason"], "Gate header matches")
    require([row["gate_id"] for row in gate_rows] == [f"G{number:02d}" for number in range(1, 21)], "All 20 gates are ordered")
    require(all(row["status"] == "pass" for row in gate_rows), "All 20 noncompensable gates pass")
    require(all(row["evidence"] and row["noncompensable_reason"] for row in gate_rows), "Every gate has evidence and a noncompensable reason")

    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8")
    for phrase in ("python build_workflow.py --self-check", "python build_workspace.py --self-check", "python validate_workspace.py --self-check", CHECKPOINT_EXPECTED["candidate_manifest_sha256"], "4ab020f4862fe06ea3c877d7302afa988b7069ce5922ddb2f578841d22838911", "20 of 20 pass", "not yet signed"):
        require(phrase in reproduction, f"Reproducibility record includes {phrase}")
    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    for phrase in ("Human-owned decisions", "Protected evidence", "Prohibited agent action", "may not select or accept a clinical threshold", "fill a suppressed equity cell", "score a real patient", "named workflow"):
        require(phrase in ai_use, f"AI-use record includes {phrase}")

    progression = (root / "progression-module05-handoff.md").read_text(encoding="utf-8")
    disposition = markdown_field(progression, "Progression")
    require(disposition in ALLOWED_PROGRESSION, "Progression uses an allowed disposition")
    require(disposition == "continue with conditions", "Reference progression continues with conditions")
    require(markdown_field(progression, "Module 04 score") == "25.00 of 25.00, carried into the Week 6 checkpoint exactly once", "Progression carries the Module 04 score once")
    require(markdown_field(progression, "Module 04 gates") == "20 of 20 pass" and markdown_field(progression, "Failed gates") == "none", "Progression records all passing gates")
    require(markdown_field(progression, "Sandbox design") == "panel-t003" and markdown_field(progression, "Sandbox design role") == "passive contextual panel fixture for mechanics testing only", "Progression records the sandbox design role")
    require(markdown_field(progression, "Sandbox threshold role") == "0.03000000 remains unaccepted and is used only to create bounded synthetic test cases" and markdown_field(progression, "Accepted clinical threshold") == "none", "Progression keeps the sandbox threshold unaccepted")
    require(markdown_field(progression, "Module 05 permission") == "permitted for nonproduction sandbox construction", "Progression permits only Module 05 sandbox construction")
    for label in ("Real-patient scoring", "Clinical alerting or action", "Silent-mode evaluation", "Implementation or production connection", "Deployment"):
        require(markdown_field(progression, label) == "prohibited", f"Progression prohibits {label}")
    for phrase in ("complete Module 04 release manifest", "normal, boundary, repeat, missing, stale, inconsistent, delayed, terminology, version, and silent-failure cases", "must not connect to a live system", "stop or refer"):
        require(phrase in progression, f"Module 05 handoff includes {phrase}")

    return {"status": "pass", "mode": "reference", "checks": len(checks)}


def clone_hardlinks(source: Path, target: Path) -> None:
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        destination = target / relative
        if path.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            destination.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.link(path, destination)
            except OSError:
                shutil.copy2(path, destination)


def replace_text(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"Mutation anchor missing in {path}: {old}")
    path.unlink()
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def remove_csv_row(path: Path, anchor: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    filtered = [line for line in lines if anchor not in line]
    if len(filtered) != len(lines) - 1:
        raise AssertionError(f"Expected one CSV row containing {anchor}")
    path.unlink()
    path.write_text("\n".join(filtered) + "\n", encoding="utf-8", newline="\n")


def expect_rejected(root: Path, label: str) -> None:
    try:
        validate(root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError):
        return
    raise AssertionError(f"Validator accepted deliberate failure route: {label}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module04-validator-") as temporary:
        base = Path(temporary)
        reference, learner = base / "reference", base / "learner"
        reference_report = assemble(reference, reference=True)
        learner_report = assemble(learner)
        complete = validate(reference)
        starter = validate(learner, learner=True)
        if reference_report["manifest_sha256"] != learner_report["manifest_sha256"]:
            raise AssertionError("Learner and reference manifests differ")

        copied = subprocess.run(
            [sys.executable, str(reference / "validate_workspace.py"), "--root", str(reference)],
            capture_output=True,
            text=True,
            check=False,
        )
        if copied.returncode != 0 or "reference validation passed" not in copied.stdout:
            raise AssertionError(f"Copied validator failed: {copied.stdout}{copied.stderr}")

        routes: list[tuple[str, callable]] = [
            ("missing record", lambda root: (root / "workflow-task-analysis.md").unlink()),
            ("immutable output mutation", lambda root: replace_text(root / "outputs/design-comparison.csv", "banner-t002", "banner-mutated")),
            ("checkpoint candidate manifest mutation", lambda root: replace_text(root / "upstream/checkpoint01/candidate-manifest.csv", "oclc-app4-01", "oclc-app4-x1")),
            ("nested immutable manifest mutation", lambda root: replace_text(root / "upstream/checkpoint01/candidate/module-01/release-manifest.csv", "immutable", "mutated")),
            ("missing checkpoint artifact", lambda root: (root / "upstream/checkpoint01/checkpoint-contract.json").unlink()),
            ("task boundary removed", lambda root: replace_text(root / "workflow-task-analysis.md", "nonproduction Module 05 sandbox", "clinical rollout")),
            ("threshold omitted", lambda root: replace_text(root / "candidate-design-review.md", "0.10000000", "0.09900000")),
            ("banner substituted", lambda root: replace_text(root / "candidate-design-review.md", "Design: `panel-t003`", "Design: `banner-t003`")),
            ("score changed", lambda root: replace_text(root / "module-score.csv", "S10,\"reproduction, AI record, decision, and handoff\",1.50,1.50", "S10,\"reproduction, AI record, decision, and handoff\",1.50,0.50")),
            ("gate failed", lambda root: replace_text(root / "gate-results.csv", "G20,progression and authority,pass", "G20,progression and authority,fail")),
            ("pause right removed", lambda root: replace_text(root / "role-handoff-map.csv", ",true,fictional role pending named review", ",false,fictional role pending named review")),
            ("timing status failed", lambda root: replace_text(root / "timing-interruption-review.csv", ",conditioned\n", ",fail\n")),
            ("burden claim expanded", lambda root: replace_text(root / "burden-assumption-register.csv", "not a staffing or capacity estimate", "observed local staffing evidence")),
            ("usability row removed", lambda root: remove_csv_row(root / "usability-review.csv", "U10,")),
            ("automation control removed", lambda root: remove_csv_row(root / "automation-bias-controls.csv", "AB10,")),
            ("access review removed", lambda root: remove_csv_row(root / "access-equity-privacy-review.csv", "E12,")),
            ("stop condition removed", lambda root: replace_text(root / "override-stop-conditions.md", "| S08 |", "| X08 |")),
            ("AI authority expanded", lambda root: replace_text(root / "ai-use.md", "may not select or accept a clinical threshold", "may select a clinical threshold")),
            ("Module 05 authority expanded", lambda root: replace_text(root / "progression-module05-handoff.md", "permitted for nonproduction sandbox construction", "permitted for clinical implementation")),
            ("deployment authority expanded", lambda root: replace_text(root / "progression-module05-handoff.md", "- Deployment: `prohibited`.", "- Deployment: `permitted`.")),
        ]
        for index, (label, mutate) in enumerate(routes, start=1):
            case = base / f"failure-{index:02d}"
            clone_hardlinks(reference, case)
            mutate(case)
            expect_rejected(case, label)
        expect_rejected(learner, "learner starter submitted as complete")

    print(f"APP-4 Module 04 reference validation passed: {complete['checks']} checks.")
    print(f"APP-4 Module 04 learner validation passed: {starter['checks']} checks.")
    print(
        "APP-4 Module 04 validator self-check passed: "
        f"{complete['checks']} reference checks and {starter['checks']} learner checks; "
        "copied validation and 20 failure routes verified."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.root:
            result = validate(args.root, learner=args.learner)
            print(f"APP-4 Module 04 {result['mode']} validation passed: {result['checks']} checks.")
        else:
            parser.error("--root is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

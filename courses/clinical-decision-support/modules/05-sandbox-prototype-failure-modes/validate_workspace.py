"""Validate an APP-4 Module 05 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from build_sandbox import OUTPUT_FILES, read_jsonl_gzip, verify as verify_sandbox
from build_workspace import (
    CONTROLS,
    GENERATED_FILES,
    MODULE04_EXPECTED,
    NESTED_MANIFESTS,
    RECORD_FILES,
    assemble,
)


CSV_CONTRACTS = {
    "request-prefetch-contract.csv": (
        ("element", "shape", "required", "validation", "failure_behavior", "authority"), 12
    ),
    "response-card-contract.csv": (
        ("response_kind", "http_status", "body_shape", "summary_and_detail", "human_notice", "suggestions_or_links", "meaning", "claim_limit"), 9
    ),
    "test-matrix-review.csv": (
        ("category", "case_count", "expected_behavior", "review_status", "claim_limit"), 21
    ),
    "traceability-audit.csv": (
        ("ledger", "grain", "expected_rows", "observed_rows", "reconciliation", "status", "meaning"), 5
    ),
    "visible-failure-review.csv": (
        ("case_id", "failure", "transport", "human_notice", "terminal_trace", "control", "status", "claim_limit"), 12
    ),
    "latency-version-review.csv": (
        ("case_id", "domain", "fixture", "expected_control", "observed", "status", "claim_limit"), 5
    ),
    "accessibility-review.csv": (
        ("check", "scope", "expected", "observed", "status", "claim_limit"), 6
    ),
    "failure-mode-register.csv": (
        ("failure_id", "case_id", "failure", "cause", "detection", "visible_to_human", "control", "module06_owner", "status"), 17
    ),
    "checkpoint-score-carryforward.csv": (
        ("component", "source_points", "module05_points", "checkpoint02_points_so_far", "rule", "status"), 3
    ),
    "gate-results.csv": (
        ("gate_id", "domain", "status", "evidence", "noncompensable_reason"), 20
    ),
}
MARKDOWN_CONTRACTS = {
    "prototype-architecture.md": (
        "local evaluator",
        "no listener",
        "threshold remains unaccepted",
        "Module 06 curriculum construction only",
    ),
    "silent-failure-review.md": (
        "M05-F15",
        "response body is absent",
        "terminal trace is absent",
        "human notice is absent",
        "independent ledgers",
        "does not estimate a clinical silent-failure rate",
    ),
    "prototype-release.md": (
        "APP4-M05-LOCAL-SANDBOX-2026-08-31-v1",
        "31",
        "184",
        "61",
        "e34f75bdcba3d2474912f587b54f81b7038b65790c51435bb10810d40643c97f",
        "Accepted clinical threshold: `none`",
    ),
    "reproducibility-check.md": (
        "31 cases",
        "324 immutable rows",
        "341 assembled files",
        "Silent-failure route: detected exactly once",
        "Accessibility defect: detected and blocked exactly once",
    ),
    "ai-use.md": (
        "Human-owned decisions",
        "accepting a threshold",
        "using real data",
        "The final disposition remains human-owned",
    ),
    "progression-module06-handoff.md": (
        "continue with conditions",
        "20 of 20 pass",
        "25.00 of 25.00, exactly once",
        "0.03000000`, unaccepted",
        "permitted for nonproduction safety, monitoring, governance, and fixed-challenger curriculum construction",
        "Silent-mode evaluation: `prohibited`",
        "Deployment: `prohibited`",
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


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
    manifest = read_csv(manifest_path)
    require(len(manifest) == 324, "Expected 324 immutable manifest rows")
    require(len({row["relative_path"] for row in manifest}) == 324, "Immutable paths must be unique")
    for row in manifest:
        path = workspace / row["relative_path"]
        require(path.is_file(), f"Immutable file missing: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable byte count changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable hash changed: {row['relative_path']}")
    files = sum(path.is_file() for path in workspace.rglob("*") if "__pycache__" not in path.parts)
    require(files == 341, "Expected 341 assembled files")
    require(all((workspace / relative).is_file() for relative in CONTROLS + GENERATED_FILES), "Module control or generated evidence missing")
    require(all((workspace / relative).is_file() for relative in RECORD_FILES), "Assessment record missing")

    module04_root = workspace / "upstream/module04"
    module04_manifest = module04_root / "release-manifest.csv"
    require(module04_manifest.is_file(), "Module 04 release manifest missing")
    require(module04_manifest.stat().st_size == MODULE04_EXPECTED["manifest_bytes"], "Module 04 manifest bytes changed")
    require(sha256(module04_manifest) == MODULE04_EXPECTED["manifest_sha256"], "Module 04 manifest hash changed")
    module04_rows = read_csv(module04_manifest)
    require(len(module04_rows) == 285, "Expected 285 Module 04 manifest rows")
    for row in module04_rows:
        path = module04_root / row["relative_path"]
        require(path.is_file(), f"Module 04 immutable file missing: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Module 04 immutable bytes changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Module 04 immutable hash changed: {row['relative_path']}")

    nested_total = 0
    for relative, (expected_rows, expected_hash) in NESTED_MANIFESTS.items():
        path = module04_root / relative
        require(path.is_file(), f"Nested manifest missing: {relative}")
        require(sha256(path) == expected_hash, f"Nested manifest changed: {relative}")
        rows = read_csv(path)
        require(len(rows) == expected_rows, f"Nested manifest rows changed: {relative}")
        nested_total += len(rows)
        nested_root = path.parent
        for row in rows:
            nested = nested_root / row["relative_path"]
            require(nested.is_file(), f"Nested immutable file missing: {relative}:{row['relative_path']}")
            require(nested.stat().st_size == int(row["bytes"]), f"Nested immutable bytes changed: {relative}:{row['relative_path']}")
            require(sha256(nested) == row["sha256"], f"Nested immutable hash changed: {relative}:{row['relative_path']}")
    require(nested_total == 204, "Expected 204 nested Week 3 immutable rows")

    sandbox = verify_sandbox(workspace)
    require(sandbox["cases"] == 31, "Expected 31 sandbox cases")
    require(sandbox["prefetch_resources"] == 184, "Expected 184 prefetch resources")
    require(sandbox["responses"] == 31, "Expected 31 response envelopes")
    require(sandbox["trace_events"] == 61, "Expected 61 trace events")
    require(sandbox["passing_tests"] == 31, "All 31 sandbox tests must pass")
    require(sandbox["silent_failures_detected"] == 1, "Expected one detected silent failure")
    require(sandbox["accessibility_defects_blocked"] == 1, "Expected one blocked accessibility defect")
    require(sandbox["output_manifest_sha256"] == "e34f75bdcba3d2474912f587b54f81b7038b65790c51435bb10810d40643c97f", "Sandbox output digest changed")

    contract = json.loads((workspace / "decision-contract.json").read_text(encoding="utf-8"))
    release = json.loads((workspace / "release.json").read_text(encoding="utf-8"))
    report = json.loads((workspace / "build-report.json").read_text(encoding="utf-8"))
    require(contract["module"]["id"] == "oclc-app4-05", "Module ID changed")
    require(contract["module"]["version"] == "0.1.0", "Module version changed")
    require(contract["module"]["commons_release"] == "0.82.0", "Commons release changed")
    require(contract["module"]["course_points"] == 0, "Module 05 must remain zero point")
    require(contract["prototype"]["design"] == "panel-t003", "Sandbox design changed")
    require(contract["prototype"]["threshold"] == "0.03000000", "Sandbox threshold changed")
    require(contract["prototype"]["accepted_threshold"] is None, "A clinical threshold was accepted")
    require(contract["prototype"]["network_listener"] is False, "Network listener is prohibited")
    require(contract["prototype"]["network_client"] is False, "Network client is prohibited")
    require(contract["prototype"]["fhir_server"] is None, "FHIR server connection is prohibited")
    require(contract["test_contract"]["cases"] == 31, "Test contract case count changed")
    require(contract["test_contract"]["silent_failure_definition"] == "a received request with no response, no terminal trace, and no human notice", "Silent-failure definition changed")
    require(release["workspace"] == {"immutable_manifest_rows": 324, "editable_records": 16, "assembled_files": 341}, "Workspace release contract changed")
    require(release["assessment"]["module_points"] == 0, "Release points changed")
    require(release["assessment"]["module04_score_carried_once"] == "25.00 of 25.00", "Module 04 score carryforward changed")
    require(report["runtime"] == {"external_python_dependencies": [], "fhir_server": None, "network_client": False, "network_listener": False}, "Runtime boundary changed")
    for authority, value in release["authority"].items():
        require(value == "prohibited", f"Authority expanded: {authority}")

    requests = read_jsonl_gzip(workspace / "data/sandbox/requests.ndjson.gz")
    responses = read_jsonl_gzip(workspace / "data/sandbox/responses.ndjson.gz")
    require(all(item["request"]["context"]["explicitSynthetic"] is True for item in requests), "Every request must be explicitly synthetic")
    require(all("fhirServer" not in item["request"] for item in requests), "FHIR server endpoint found")
    require(all(str(item["request"]["context"]["patientId"]).startswith("SP") for item in requests), "Non-synthetic patient identity found")
    for response in responses:
        body = response.get("body")
        if not body or "cards" not in body:
            continue
        for card in body["cards"]:
            require(not card.get("suggestions"), "Clinical suggestion found")
            require(not card.get("links"), "External link found")

    incomplete_records = 0
    for relative in RECORD_FILES:
        text = (workspace / relative).read_text(encoding="utf-8")
        incomplete_records += "INCOMPLETE" in text
        if complete:
            require("INCOMPLETE" not in text, f"Reference record incomplete: {relative}")
            require("TODO" not in text and "TBD" not in text and "REPLACE" not in text, f"Placeholder found: {relative}")
    if complete:
        require(incomplete_records == 0, "Complete submission contains incomplete records")
    else:
        require(incomplete_records == len(RECORD_FILES), "Learner starter must keep every record incomplete")

    for relative, (headers, expected_rows) in CSV_CONTRACTS.items():
        with (workspace / relative).open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            require(tuple(reader.fieldnames or ()) == headers, f"CSV header changed: {relative}")
        if complete:
            require(len(rows) == expected_rows, f"Reference row count changed: {relative}")
            require(all("INCOMPLETE" not in value for row in rows for value in row.values()), f"Incomplete CSV value: {relative}")
        else:
            require(len(rows) >= 1, f"Learner CSV has no starter row: {relative}")

    if complete:
        for relative, phrases in MARKDOWN_CONTRACTS.items():
            text = (workspace / relative).read_text(encoding="utf-8")
            for phrase in phrases:
                require(phrase in text, f"Required statement missing from {relative}: {phrase}")
        matrix = read_csv(workspace / "test-matrix-review.csv")
        require(sum(int(row["case_count"]) for row in matrix) == 31, "Reviewed case counts must total 31")
        require(all(row["review_status"] == "pass" for row in matrix), "Every reviewed category must pass")
        trace = read_csv(workspace / "traceability-audit.csv")
        require({row["ledger"] for row in trace} == {"request ledger", "response ledger", "terminal trace", "human notice", "silence detector"}, "Trace ledgers incomplete")
        visible = read_csv(workspace / "visible-failure-review.csv")
        require({row["case_id"] for row in visible} == {"M05-F01", "M05-F02", "M05-F03", "M05-F04", "M05-F06", "M05-F07", "M05-F08", "M05-F09", "M05-F10", "M05-F13", "M05-F14", "M05-F17"}, "Visible-failure set changed")
        latency = read_csv(workspace / "latency-version-review.csv")
        require(any(row["case_id"] == "M05-F17" and "UNKNOWN-MODEL" in row["fixture"] for row in latency), "Model-version review changed")
        access = read_csv(workspace / "accessibility-review.csv")
        require(any(row["check"] == "malformed fixture M05-F16" and row["observed"] == "defect detected and HTTP 422 returned" for row in access), "Accessibility defect review changed")
        failures = read_csv(workspace / "failure-mode-register.csv")
        require({row["failure_id"] for row in failures} == {f"FM{index:02d}" for index in range(1, 18)}, "Failure register incomplete")
        require(all(row["status"] == "pass" for row in failures), "Failure register contains a failed review")
        score = read_csv(workspace / "checkpoint-score-carryforward.csv")
        require([row["checkpoint02_points_so_far"] for row in score] == ["25.00", "25.00", "25.00"], "Checkpoint score carryforward changed")
        require(all(row["module05_points"] == "0.00" for row in score), "Module 05 added points")
        gates = read_csv(workspace / "gate-results.csv")
        require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 21)], "Gate IDs changed")
        require(all(row["status"] == "pass" for row in gates), "A noncompensable gate failed")
        progression = (workspace / "progression-module06-handoff.md").read_text(encoding="utf-8")
        for prohibited in (
            "Silent-mode evaluation: `prohibited`",
            "Real-patient scoring: `prohibited`",
            "Clinical alerting or action: `prohibited`",
            "Implementation or production connection: `prohibited`",
            "Deployment: `prohibited`",
        ):
            require(prohibited in progression, f"Progression authority missing: {prohibited}")

    return {
        "status": "pass",
        "mode": "complete" if complete else "learner",
        "checks": checks,
        "manifest_rows": len(manifest),
        "module04_manifest_rows": len(module04_rows),
        "nested_immutable_rows": nested_total,
        "records": len(RECORD_FILES),
        "cases": sandbox["cases"],
        "gates_passed": 20 if complete else 0,
        "progression": "continue with conditions" if complete else "not assessed",
    }


def break_link(path: Path) -> None:
    payload = path.read_bytes()
    path.unlink()
    path.write_bytes(payload)


def clone_tree(source: Path, target: Path) -> None:
    try:
        shutil.copytree(source, target, copy_function=os.link)
    except OSError:
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)


def expect_failure(reference: Path, base: Path, name: str, mutate) -> None:
    clone = base / name
    clone_tree(reference, clone)
    mutate(clone)
    try:
        validate(clone, complete=True)
    except (OSError, ValueError, KeyError, json.JSONDecodeError):
        return
    raise AssertionError(f"Validator accepted deliberate failure: {name}")


def replace(path: Path, old: str, new: str) -> None:
    break_link(path)
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"Failure mutation source not found in {path.name}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module05-validator-") as temporary:
        base = Path(temporary)
        learner, reference = base / "learner", base / "reference"
        assemble(learner)
        assemble(reference, reference=True)
        learner_report = validate(learner)
        reference_report = validate(reference, complete=True)

        copied = subprocess.run(
            [sys.executable, str(reference / "validate_workspace.py"), "--workspace", str(reference), "--complete"],
            capture_output=True,
            text=True,
            check=False,
        )
        if copied.returncode != 0 or '"status": "pass"' not in copied.stdout:
            raise AssertionError(f"Copied validator failed: {copied.stdout}{copied.stderr}")

        failures = base / "failures"
        failures.mkdir()
        expect_failure(reference, failures, "missing-record", lambda root: (root / "prototype-architecture.md").unlink())
        expect_failure(reference, failures, "own-immutable", lambda root: replace(root / "outputs/test-results.csv", ",pass,", ",fail,"))
        expect_failure(reference, failures, "module04-manifest", lambda root: replace(root / "upstream/module04/release-manifest.csv", "285", "286"))
        expect_failure(reference, failures, "nested-manifest", lambda root: replace(root / "upstream/module04/upstream/checkpoint01/candidate/module-03/release-manifest.csv", "relative_path", "changed_path"))
        expect_failure(reference, failures, "nested-file", lambda root: (root / "upstream/module04/upstream/checkpoint01/candidate/module-02/VERSION").unlink())
        expect_failure(reference, failures, "architecture-network", lambda root: replace(root / "prototype-architecture.md", "no listener", "a network listener"))
        expect_failure(reference, failures, "matrix-count", lambda root: replace(root / "test-matrix-review.csv", "normal positive,11", "normal positive,10"))
        expect_failure(reference, failures, "trace-ledger", lambda root: replace(root / "traceability-audit.csv", "silence detector", "single service log"))
        expect_failure(reference, failures, "visible-case", lambda root: replace(root / "visible-failure-review.csv", "M05-F17", "M05-F15"))
        expect_failure(reference, failures, "silent-rule", lambda root: replace(root / "silent-failure-review.md", "terminal trace is absent", "terminal trace is present"))
        expect_failure(reference, failures, "version-review", lambda root: replace(root / "latency-version-review.csv", "UNKNOWN-MODEL", "APP4-M03-LOGIT-2026-08-31-v1"))
        expect_failure(reference, failures, "accessibility-review", lambda root: replace(root / "accessibility-review.csv", "defect detected and HTTP 422 returned", "defect released"))
        expect_failure(reference, failures, "failure-register", lambda root: replace(root / "failure-mode-register.csv", "FM15", "FM18"))
        expect_failure(reference, failures, "score", lambda root: replace(root / "checkpoint-score-carryforward.csv", "25.00,0.00,25.00", "25.00,5.00,30.00"))
        expect_failure(reference, failures, "gate", lambda root: replace(root / "gate-results.csv", "G20,progression and authority,pass", "G20,progression and authority,fail"))
        expect_failure(reference, failures, "ai-authority", lambda root: replace(root / "ai-use.md", "accepting a threshold", "selecting an accepted threshold"))
        expect_failure(reference, failures, "progression", lambda root: replace(root / "progression-module06-handoff.md", "continue with conditions", "deploy"))
        expect_failure(reference, failures, "prototype-threshold", lambda root: replace(root / "prototype-release.md", "Accepted clinical threshold: `none`", "Accepted clinical threshold: `0.03`"))
        expect_failure(reference, failures, "module06-permission", lambda root: replace(root / "progression-module06-handoff.md", "permitted for nonproduction safety, monitoring, governance, and fixed-challenger curriculum construction", "permitted for production implementation"))
        try:
            validate(learner, complete=True)
        except ValueError:
            pass
        else:
            raise AssertionError("Validator accepted the learner starter as complete")

    print(
        "APP-4 Module 05 validator self-check passed: "
        f"{reference_report['checks']} reference checks, {learner_report['checks']} learner checks, "
        "copied validation, and 20 rejected failure routes."
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
    except (OSError, ValueError, KeyError, AssertionError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

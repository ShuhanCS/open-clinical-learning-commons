"""Validate an APP-4 Module 02 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORD_FILES = (
    "use-case-logic-release.md", "logic-specification.csv", "input-contract.csv",
    "trigger-suppression-matrix.csv", "rule-test-results.csv", "terminology-map.csv",
    "synthetic-release-interpretation.md", "logic-change-control.md",
    "patient-workflow-consequence-map.csv", "claim-boundary.csv", "ai-use.md",
    "progression-decision.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_evaluator(workspace: Path):
    spec = importlib.util.spec_from_file_location("app4_module02_evaluator", workspace / "evaluate_rules.py")
    if spec is None or spec.loader is None:
        raise ValueError("Cannot load rule evaluator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_manifest(workspace: Path) -> list[dict[str, str]]:
    manifest_path = workspace / "release-manifest.csv"
    rows = read_csv(manifest_path)
    if len(rows) != 73:
        raise ValueError(f"Expected 73 immutable manifest rows, found {len(rows)}")
    for row in rows:
        path = workspace / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]):
            raise ValueError(f"Immutable bytes changed: {row['relative_path']}")
        if sha256(path) != row["sha256"]:
            raise ValueError(f"Immutable hash changed: {row['relative_path']}")
    if sum(path.is_file() for path in workspace.rglob("*")) != 86:
        raise ValueError("Workspace file count changed")
    return rows


def validate_synthetic(workspace: Path) -> dict[str, int]:
    root = workspace / "data" / "synthetic-release"
    manifest = read_csv(root / "source-manifest.csv")
    if len(manifest) != 25:
        raise ValueError("Synthetic source manifest must contain 25 files")
    total_rows = duplicate_ids = failures = compressed_bytes = 0
    for row in manifest:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["compressed_bytes"]):
            raise ValueError(f"Synthetic source bytes changed: {row['relative_path']}")
        if sha256(path) != row["sha256"]:
            raise ValueError(f"Synthetic source hash changed: {row['relative_path']}")
        ids: list[str] = []
        resource_types: set[str] = set()
        actual_rows = 0
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            if row["relative_path"].endswith(".json.gz"):
                resource = json.load(handle)
                actual_rows = 1
                resource_types.add(str(resource.get("resourceType", "")))
                if resource.get("id") is not None:
                    ids.append(str(resource["id"]))
            else:
                for line in handle:
                    try:
                        resource = json.loads(line)
                        actual_rows += 1
                        resource_types.add(str(resource.get("resourceType", "")))
                        if resource.get("id") is not None:
                            ids.append(str(resource["id"]))
                    except json.JSONDecodeError:
                        failures += 1
        actual_type = next(iter(resource_types)) if len(resource_types) == 1 else "mixed"
        actual_duplicates = len(ids) - len(set(ids))
        if actual_rows != int(row["rows"]) or actual_type != row["resource_type"]:
            raise ValueError(f"Synthetic source profile changed: {row['relative_path']}")
        if actual_duplicates != int(row["duplicate_ids"]):
            raise ValueError(f"Synthetic duplicate count changed: {row['relative_path']}")
        total_rows += actual_rows
        duplicate_ids += actual_duplicates
        compressed_bytes += path.stat().st_size
    if (total_rows, duplicate_ids, failures, compressed_bytes) != (811803, 11109, 0, 100178478):
        raise ValueError("Synthetic release totals changed")
    release = json.loads((root / "synthetic-release.json").read_text(encoding="utf-8"))
    if release["resource_rows"] != total_rows or release["duplicate_resource_ids_within_file"] != duplicate_ids:
        raise ValueError("Synthetic release record disagrees with files")
    return {"rows": total_rows, "duplicates": duplicate_ids, "failures": failures}


def validate_inheritance(workspace: Path) -> None:
    contract = json.loads(
        (workspace / "inherited" / "module01" / "decision-contract.json").read_text(encoding="utf-8")
    )
    public = contract["public_release"]
    expected = (16, 4, 34221200, 3149043, 145563, 442, 0)
    actual = (
        public["complete_xpt_files"], public["cycles"], public["raw_bytes"], public["gzip_bytes"],
        public["source_rows"], public["field_inventory_rows"], public["duplicate_seqn_rows"],
    )
    if actual != expected:
        raise ValueError("Module 01 public release inheritance changed")
    authority = contract["authority"]
    if any(authority[key] != "prohibited" for key in (
        "model_fitting", "threshold_selection", "alert_firing", "real_patient_scoring",
        "clinical_action", "implementation", "deployment",
    )):
        raise ValueError("Module 01 authority boundary changed")


def validate_fixtures(workspace: Path) -> list[dict[str, str]]:
    root = workspace / "data" / "commons"
    patients = read_csv(root / "patient-linkage.csv")
    cases = read_csv(root / "rule-test-cases.csv")
    config = json.loads((root / "logic-config.json").read_text(encoding="utf-8"))
    if len(patients) != 16 or len(cases) != 16:
        raise ValueError("Expected 16 linked patients and 16 rule cases")
    if [row["case_id"] for row in patients] != [row["case_id"] for row in cases]:
        raise ValueError("Patient linkage and cases disagree")
    if [row["patient_id"] for row in patients] != [row["patient_id"] for row in cases]:
        raise ValueError("Synthetic patient identities changed")
    if len({row["condition_class"] for row in cases}) != 16:
        raise ValueError("Rule condition coverage changed")
    if config["mock_threshold"] != 0.20 or "not estimated" not in config["threshold_status"]:
        raise ValueError("Mock threshold authority boundary changed")
    return cases


def validate_records(workspace: Path, mode: str, cases: list[dict[str, str]]) -> None:
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
    release_text = (workspace / "use-case-logic-release.md").read_text(encoding="utf-8")
    if "not been clinically selected, estimated, recommended, or accepted" not in release_text:
        raise ValueError("Use-case release does not bound the mock threshold")
    interpretation = (workspace / "synthetic-release-interpretation.md").read_text(encoding="utf-8")
    for value in ("811,803", "11,109", "Windows-1252", "canonical UTF-8"):
        if value not in interpretation:
            raise ValueError(f"Synthetic interpretation omits {value}")
    claim_rows = read_csv(workspace / "claim-boundary.csv")
    if len(claim_rows) != 12 or sum(row["status"] == "prohibited" for row in claim_rows) < 7:
        raise ValueError("Claim boundary is incomplete")
    if any(
        "threshold" in row["claim"].lower()
        and "accept" in row["claim"].lower()
        and row["status"] == "allowed"
        for row in claim_rows
    ):
        raise ValueError("Submission claims prohibited threshold authority")
    progression = (workspace / "progression-decision.md").read_text(encoding="utf-8")
    required = (
        "continue with conditions", "Module 03 curriculum construction: `permitted`",
        "Clinical-threshold selection or acceptance: `prohibited`",
        "Real-patient scoring: `prohibited`", "Deployment: `prohibited`",
    )
    if any(value not in progression for value in required):
        raise ValueError("Progression or authority boundary changed")
    results = read_csv(workspace / "rule-test-results.csv")
    expected = load_evaluator(workspace).run(workspace / "data" / "commons" / "rule-test-cases.csv")
    if results != expected or len(results) != len(cases) or any(row["status"] != "pass" for row in results):
        raise ValueError("Rule test results do not reproduce")
    logic = read_csv(workspace / "logic-specification.csv")
    if len(logic) != 11 or {row["reason_code"] for row in logic} != {
        "unsupported_service", "context_not_supported", "duplicate_request", "input_not_ready",
        "semantic_mismatch", "known_diabetes_suppression", "recent_hba1c_suppression",
        "score_fixture_missing", "below_mock_threshold", "at_or_above_mock_threshold",
        "candidate_response_not_delivered",
    }:
        raise ValueError("Logic branch contract changed")
    if any(
        phrase in "\n".join((workspace / name).read_text(encoding="utf-8").lower() for name in RECORD_FILES)
        for phrase in (
            "approved for deployment", "authorized for clinical use", "real-patient scoring is allowed",
        )
    ):
        raise ValueError("Submission claims prohibited authority")


def validate(workspace: Path, mode: str) -> dict[str, object]:
    workspace = workspace.resolve()
    validate_manifest(workspace)
    validate_inheritance(workspace)
    synthetic = validate_synthetic(workspace)
    cases = validate_fixtures(workspace)
    validate_records(workspace, mode, cases)
    return {
        "status": "pass", "mode": mode, "manifest_rows": 73, "assembled_files": 86,
        "synthetic_rows": synthetic["rows"], "duplicate_ids": synthetic["duplicates"],
        "rule_cases": len(cases), "editable_records": 12,
    }


def expect_rejection(action, label: str) -> None:
    try:
        action()
    except (OSError, ValueError, json.JSONDecodeError):
        return
    raise AssertionError(f"Validator accepted {label}")


def self_check() -> None:
    from build_workspace import assemble

    with tempfile.TemporaryDirectory(prefix="app4-module02-validate-") as temporary:
        base = Path(temporary)
        complete, starter = base / "complete", base / "starter"
        assemble(complete, reference=True)
        assemble(starter)
        complete_report = validate(complete, "complete")
        validate_manifest(starter)
        validate_inheritance(starter)
        starter_cases = validate_fixtures(starter)
        validate_records(starter, "starter", starter_cases)
        complete_cases = validate_fixtures(complete)
        assert complete_report["synthetic_rows"] == 811803 and len(starter_cases) == 16

        source = complete / "data" / "commons" / "logic-config.json"
        original = source.read_bytes()
        source.write_bytes(original + b" ")
        expect_rejection(lambda: validate_manifest(complete), "mutated immutable source")
        source.write_bytes(original)

        record = complete / "use-case-logic-release.md"
        original_text = record.read_text(encoding="utf-8")
        record.write_text(original_text + "\nREPLACE\n", encoding="utf-8")
        expect_rejection(lambda: validate_records(complete, "complete", complete_cases), "placeholder in complete package")
        record.write_text(original_text, encoding="utf-8")

        copied = starter / "logic-specification.csv"
        copied_original = copied.read_bytes()
        shutil.copy2(complete / "logic-specification.csv", copied)
        expect_rejection(lambda: validate_records(starter, "starter", starter_cases), "copied reference answer")
        copied.write_bytes(copied_original)

        progression = complete / "progression-decision.md"
        progression_original = progression.read_text(encoding="utf-8")
        progression.write_text(progression_original.replace("Deployment: `prohibited`", "Deployment: `allowed`"), encoding="utf-8")
        expect_rejection(lambda: validate_records(complete, "complete", complete_cases), "deployment authority")
        progression.write_text(progression_original, encoding="utf-8")

        claim = complete / "claim-boundary.csv"
        claim_original = claim.read_text(encoding="utf-8")
        claim.write_text(claim_original + "CL13,clinical threshold accepted,allowed,fixture tests,faculty\n", encoding="utf-8")
        expect_rejection(lambda: validate_records(complete, "complete", complete_cases), "clinical threshold authority")
        claim.write_text(claim_original, encoding="utf-8")

        missing = complete / "ai-use.md"
        missing_backup = missing.read_bytes()
        missing.unlink()
        expect_rejection(lambda: validate_records(complete, "complete", complete_cases), "missing assessed record")
        missing.write_bytes(missing_backup)
    print("APP-4 Module 02 validator self-check passed: complete, starter, mutation, copy, authority, and missing-file cases.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--mode", choices=("complete", "starter"), default="complete")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            print(json.dumps(validate(args.workspace, args.mode), indent=2))
        else:
            parser.error("provide --workspace or choose --self-check")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

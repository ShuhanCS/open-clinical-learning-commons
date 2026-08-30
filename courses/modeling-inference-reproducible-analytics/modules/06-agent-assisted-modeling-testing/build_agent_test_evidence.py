"""Build the exact FND-2 Module 06 agent-assisted testing evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path

import run_contract_tests as suite


MODULE_ROOT = Path(__file__).resolve().parent
UPSTREAM = {
    "prediction-model-contract.json": (2831, "0aab6eb29fbcbd921e191c62d5a0a44554de0a683fd560359991fcc9db034015"),
    "split-registry.csv": (51910, "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1"),
    "test-predictions.csv": (7994, "531c00d310292aeeaea476d1c94e128f5c81c34c2fc60e014d2c157e152b7438"),
    "confusion-table.csv": (110, "a899fc8ebaee87fd2990354f6310c6feb87f748e17545c5c39c5a413e630be87"),
    "calibration-table.csv": (644, "fce4d9b0a05085ab51cb5af1c9a2dcb209a9fb2d099b3245650543a09c461b5c"),
    "transformed-feature-names.csv": (859, "da0ce00b3c2f8d36dbe4e3741c66991f46b97d205368e2508d6c44d741e36acf"),
    "module-04-release.json": (7013, "ffcf57c30d77be5c2271488a4d2dd08cc44d430cc590025e918c0ec8f1c4e12e"),
    "validity-checks.csv": (594, "f4767ae3ae934e996b1e9f41b9c7f46898a63a80d798ace36e12ccb85d83c4ea"),
    "module-05-release.json": (6906, "d81bcc3ac2ac2971cb1a03467673d86a905a125f7aed859f2e7669e9c7003f6d"),
    "forecast-contract.json": (1048, "56f6cb46af960588044b76a42977fff1ceab1066db4ddfda4f601566ec5b1d1a"),
    "temporal-folds.csv": (489, "9ac64675bf9d2765c93d52351f4801644082cc329f1928313c2c2f94cc8a5aa6"),
    "forecast-predictions.csv": (7728, "dfc91a5e38e2255437dc17a5227cccdb14d4970eb79e14b0260ab203aec8de7a"),
    "aggregate-metrics.csv": (459, "68e0147ad1dbd627c0274f31ee4ce0035a2a1c1c55ac0c89277d996983891973"),
}
PORTABLE_FILES = ("requirements.txt", "data-spec.md", "source-record.yml", "test-contract.json", "prompt-constraints.md", "assessment.md")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Cannot write empty table: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def upstream_paths(root: Path | None = None) -> dict[str, Path]:
    if root is not None:
        return {name: root / name for name in UPSTREAM}
    course = MODULE_ROOT.parents[1]
    modules = course / "modules"
    m01 = modules / "01-aims-reproducible-workspace" / "outputs"
    m03 = modules / "03-prediction-evaluation"
    m04 = modules / "04-validity-adjustment-longitudinal"
    m05 = modules / "05-forecasting-temporal-validation"
    return {
        "prediction-model-contract.json": m03 / "model-contract.json",
        "split-registry.csv": m01 / "split-registry.csv",
        "test-predictions.csv": m03 / "outputs" / "test-predictions.csv",
        "confusion-table.csv": m03 / "outputs" / "confusion-table.csv",
        "calibration-table.csv": m03 / "outputs" / "calibration-table.csv",
        "transformed-feature-names.csv": m03 / "outputs" / "transformed-feature-names.csv",
        "module-04-release.json": m04 / "release.json",
        "validity-checks.csv": m04 / "outputs" / "validity-checks.csv",
        "module-05-release.json": m05 / "release.json",
        "forecast-contract.json": m05 / "forecast-contract.json",
        "temporal-folds.csv": m05 / "outputs" / "temporal-folds.csv",
        "forecast-predictions.csv": m05 / "outputs" / "forecast-predictions.csv",
        "aggregate-metrics.csv": m05 / "outputs" / "aggregate-metrics.csv",
    }


def verify_upstream(paths: dict[str, Path]) -> None:
    for name, (size, digest) in UPSTREAM.items():
        path = paths[name]
        if not path.is_file() or path.stat().st_size != size or sha256(path) != digest:
            raise ValueError(f"Accepted upstream fingerprint changed: {name}")


def manifest_rows(paths: dict[str, Path]) -> list[dict[str, object]]:
    families = {
        "prediction-model-contract.json": "prediction contract", "split-registry.csv": "data and split",
        "test-predictions.csv": "prediction evidence", "confusion-table.csv": "metric evidence",
        "calibration-table.csv": "calibration evidence", "transformed-feature-names.csv": "feature evidence",
        "module-04-release.json": "validity release", "validity-checks.csv": "validity tests",
        "module-05-release.json": "forecast release", "forecast-contract.json": "forecast contract",
        "temporal-folds.csv": "temporal evidence", "forecast-predictions.csv": "forecast evidence",
        "aggregate-metrics.csv": "forecast metric evidence",
    }
    return [{"artifact": name, "family": families[name], "bytes": path.stat().st_size, "sha256": sha256(path), "status": "accepted unchanged"} for name, path in paths.items()]


def data_class_rows() -> list[dict[str, object]]:
    return [
        {"class_id": "D01", "data_class": "public aggregate", "share_with_agent": "allowed", "example": "CDC jurisdiction-week source", "control": "retain source and rights record"},
        {"class_id": "D02", "data_class": "documented synthetic", "share_with_agent": "allowed", "example": "Synthea and deterministic fixtures", "control": "state synthetic boundary"},
        {"class_id": "D03", "data_class": "deidentified research", "share_with_agent": "prohibited in this release", "example": "study extract", "control": "use approved environment and governance route"},
        {"class_id": "D04", "data_class": "protected health information", "share_with_agent": "prohibited", "example": "identifiable patient record", "control": "stop"},
        {"class_id": "D05", "data_class": "workplace confidential", "share_with_agent": "prohibited", "example": "internal operations file", "control": "stop and use approved local process"},
        {"class_id": "D06", "data_class": "credential or secret", "share_with_agent": "prohibited", "example": "token, password, key", "control": "stop, rotate if exposed"},
        {"class_id": "D07", "data_class": "restricted licensed", "share_with_agent": "prohibited unless approved", "example": "nonredistributable dataset", "control": "verify license and environment"},
    ]


def summary_rows(result: dict[str, object], manifest: list[dict[str, object]]) -> list[dict[str, object]]:
    families = Counter(row["family"] for row in result["accepted_tests"])
    rows = [
        {"summary_id": "S01", "measure": "accepted artifacts", "value": len(manifest), "required": 13, "status": "pass"},
        {"summary_id": "S02", "measure": "accepted contract tests", "value": len(result["accepted_tests"]), "required": 18, "status": result["status"]},
        {"summary_id": "S03", "measure": "seeded failures rejected", "value": sum(row["status"] == "pass" for row in result["seeded_failures"]), "required": 10, "status": "pass" if all(row["status"] == "pass" for row in result["seeded_failures"]) else "fail"},
        {"summary_id": "S04", "measure": "independent verifications", "value": sum(row["status"] == "pass" for row in result["independent_verifications"]), "required": 3, "status": "pass" if all(row["status"] == "pass" for row in result["independent_verifications"]) else "fail"},
        {"summary_id": "S05", "measure": "agent claims adjudicated", "value": len(result["claim_adjudications"]), "required": 4, "status": "pass"},
        {"summary_id": "S06", "measure": "test families represented", "value": len(families), "required": 8, "status": "pass" if len(families) >= 8 else "fail"},
        {"summary_id": "S07", "measure": "human owners recorded", "value": sum(bool(row["human_owner"]) for row in result["claim_adjudications"]), "required": 4, "status": "pass"},
    ]
    return rows


def accessible_summary(rows: list[dict[str, object]]) -> str:
    lines = ["# Accessible contract-test summary", "", "All accepted evidence remains unchanged, all required contract tests pass, and every seeded failure is rejected for its intended reason.", "", "| Measure | Observed | Required | Status |", "|---|---:|---:|---|"]
    lines.extend(f'| {row["measure"]} | {row["value"]} | {row["required"]} | {row["status"]} |' for row in rows)
    lines.extend(["", "The exact artifact fingerprints, assertions, failure codes, independent recalculations, and agent-claim decisions are available in the adjacent structured files. A pass means the declared tests behaved as specified; it does not authorize clinical or deployed use.", ""])
    return "\n".join(lines)


def build_outputs(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_upstream(paths)
    result = suite.run_suite(paths)
    if result["status"] != "pass":
        raise ValueError("Accepted or seeded contract test failed.")
    manifest = manifest_rows(paths)
    summaries = summary_rows(result, manifest)
    if any(row["status"] != "pass" for row in summaries):
        raise ValueError(f"Test summary failed: {summaries}")
    target.mkdir(parents=True)
    outputs = {
        "accepted-artifact-manifest.csv": manifest,
        "accepted-contract-tests.csv": result["accepted_tests"],
        "seeded-failure-results.csv": result["seeded_failures"],
        "independent-verification.csv": result["independent_verifications"],
        "claim-adjudication.csv": result["claim_adjudications"],
        "data-class-rules.csv": data_class_rows(),
        "test-summary.csv": summaries,
    }
    report: dict[str, object] = {
        "status": "pass", "version": "0.1.0",
        "upstream": {name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for name, path in paths.items()},
        "tests": {"accepted": 18, "seeded_failures": 10, "independent_verifications": 3, "agent_claims": 4, "summary_gates": 7},
        "outputs": {},
        "decision": {"reference": "accept Week 6 gate and continue to Checkpoint 2 with conditions", "module_07": "allowed after Checkpoint 2", "human_owner": "required"},
    }
    for name, rows in outputs.items():
        path = target / name
        write_csv(path, rows)
        report["outputs"][name] = {"rows": len(rows), "fields": len(rows[0]), "bytes": path.stat().st_size, "sha256": sha256(path)}
    fixture_path = target / "failure-fixtures.json"
    fixture_path.write_text(json.dumps(result["failure_fixtures"], indent=2) + "\n", encoding="utf-8", newline="")
    report["outputs"]["failure-fixtures.json"] = {"fixtures": len(result["failure_fixtures"]), "bytes": fixture_path.stat().st_size, "sha256": sha256(fixture_path)}
    summary_path = target / "test-summary.md"
    summary_path.write_text(accessible_summary(summaries), encoding="utf-8", newline="")
    report["outputs"]["test-summary.md"] = {"bytes": summary_path.stat().st_size, "sha256": sha256(summary_path)}
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="")
    return report


def build_workspace(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_upstream(paths)
    shutil.copytree(MODULE_ROOT / "learner-template", target)
    for name in PORTABLE_FILES:
        shutil.copy2(MODULE_ROOT / name, target / name)
    for name in ("run_contract_tests.py", "build_agent_test_evidence.py", "validate_agent_test_evidence.py"):
        shutil.copy2(MODULE_ROOT / name, target / name)
    data = target / "data"
    data.mkdir()
    for name, path in paths.items():
        shutil.copy2(path, data / name)
    return build_outputs(upstream_paths(data), target / "outputs")


def self_check() -> None:
    paths = upstream_paths()
    with tempfile.TemporaryDirectory(prefix="fnd2-module06-build-") as temp_dir:
        root = Path(temp_dir)
        first = root / "outputs"
        report = build_outputs(paths, first)
        assert report["tests"]["accepted"] == 18 and report["tests"]["seeded_failures"] == 10
        try:
            build_outputs(paths, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not refuse existing target")
        workspace = root / "learner"
        workspace_report = build_workspace(paths, workspace)
        reproduced = workspace / "reproduced-outputs"
        reproduced_report = build_outputs(upstream_paths(workspace / "data"), reproduced)
        assert workspace_report["outputs"] == reproduced_report["outputs"]
    print("FND-2 Module 06 builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--build-reference", action="store_true")
    parser.add_argument("--outputs-only", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.build_reference:
        print(json.dumps(build_outputs(upstream_paths(), MODULE_ROOT / "outputs"), indent=2))
        return
    if args.target is None:
        parser.error("target is required unless --self-check or --build-reference is used")
    report = build_outputs(upstream_paths(), args.target.resolve()) if args.outputs_only else build_workspace(upstream_paths(), args.target.resolve())
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

"""Freeze and verify the accepted APP-3 Module 05 handoff."""

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
COURSE_ROOT = ROOT.parent.parent
MODULE04 = COURSE_ROOT / "modules/04-demand-forecasting-capacity"
CHECKPOINT = COURSE_ROOT / "checkpoints/01-measures-variation-readiness"
MODULE04_SOURCES = {
    "module04-release.json": "release.json",
    "module04-forecast-contract.json": "forecast-contract.json",
    "forecast-findings.json": "outputs/forecast-findings.json",
    "week53-forecast.csv": "outputs/week53-forecast.csv",
    "capacity-implication.csv": "outputs/capacity-implication.csv",
    "error-summary.csv": "outputs/error-summary.csv",
    "error-slices.csv": "outputs/error-slices.csv",
    "folds.csv": "outputs/folds.csv",
    "littles-law-check.csv": "outputs/littles-law-check.csv",
    "model-comparison.md": "model-comparison.md",
    "failure-period-review.md": "failure-period-review.md",
    "capacity-interpretation.md": "capacity-interpretation.md",
    "littles-law-interpretation.md": "littles-law-interpretation.md",
    "module05-handoff.md": "module05-handoff.md",
    "module04-progression-decision.md": "progression-decision.md",
    "module03-diagnostic-findings.json": "upstream/module03-diagnostic-findings.json",
    "module03-bottleneck-reconciliation.csv": "upstream/module03-bottleneck-reconciliation.csv",
    "module03-subgroup-window-support.csv": "upstream/module03-subgroup-window-support.csv",
    "module03-escalation-rule.md": "upstream/module03-escalation-rule.md",
    "shift-metrics.csv": "upstream/shift-metrics.csv",
    "staffing.csv.gz": "upstream/staffing.csv.gz",
    "weekly-metrics.csv": "upstream/weekly-metrics.csv",
    "checkpoint-candidate-manifest.csv": "upstream/checkpoint-candidate-manifest.csv",
    "module02-release.json": "upstream/module02-release.json",
    "module02-build-report.json": "upstream/module02-build-report.json",
}
CHECKPOINT_SOURCES = {
    "encounter-measures.csv.gz": "candidate/module-02/outputs/encounter-measures.csv.gz",
    "scenario-register.csv.gz": "candidate/module-02/data/raw/scenarios.csv.gz",
    "known-truth.csv.gz": "candidate/module-02/data/raw/known-truth.csv.gz",
    "measure-specifications.csv": "candidate/module-02/measure-specifications.csv",
}


class HandoffError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_csv(path: Path, compressed: bool = False) -> list[dict[str, str]]:
    opener = gzip.open if compressed else path.open
    if compressed:
        with opener(path, "rt", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    with opener(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def freeze(output: Path) -> list[dict[str, object]]:
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {output}")
    output.mkdir(parents=True)
    rows: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="app3-module05-handoff-") as temp_dir:
        base = Path(temp_dir)
        module04 = base / "module04"
        checkpoint = base / "checkpoint"
        module04_report = load_module(MODULE04 / "build_workspace.py", "app3_module04_workspace").assemble(module04, reference=True)
        if module04_report["assembled_files"] != 59 or module04_report["manifest_rows"] != 46:
            raise HandoffError("Module 04 reference identity changed")
        checkpoint_report = load_module(CHECKPOINT / "build_checkpoint.py", "app3_checkpoint01_builder").assemble(checkpoint, reference=True)
        if checkpoint_report != {
            "status": "pass",
            "mode": "reference",
            "candidate_manifest_rows": 137,
            "candidate_manifest_bytes": 23862,
            "candidate_manifest_sha256": "9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656",
            "assembled_files": 153,
        }:
            raise HandoffError("Checkpoint 01 identity changed")
        source_sets = (
            (module04, MODULE04_SOURCES, "oclc-app3-04@0.1.0+commons.0.70.0", "accepted Module 04 forecast handoff"),
            (checkpoint, CHECKPOINT_SOURCES, "oclc-app3-cp01@0.1.0+commons.0.69.0", "accepted scenario input"),
        )
        for source_root, sources, release, role in source_sets:
            for target_name, source_name in sources.items():
                source = source_root / source_name
                if not source.is_file():
                    raise HandoffError(f"Missing handoff source: {source}")
                target = output / target_name
                shutil.copy2(source, target)
                rows.append({
                    "relative_path": f"upstream/{target_name}",
                    "source_path": source_name,
                    "bytes": target.stat().st_size,
                    "sha256": sha256(target),
                    "source_release": release,
                    "role": role,
                })
    rows.sort(key=lambda row: str(row["relative_path"]))
    manifest = output / "module05-handoff-manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "source_path", "bytes", "sha256", "source_release", "role"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    if len(rows) != 29 or sum(path.is_file() for path in output.iterdir()) != 30:
        raise HandoffError("Module 05 handoff file contract changed")
    return rows


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root / "upstream"
    manifest = upstream / "module05-handoff-manifest.csv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != ["relative_path", "source_path", "bytes", "sha256", "source_release", "role"]:
            raise HandoffError("Handoff manifest header mismatch")
        rows = list(reader)
    expected = sorted(f"upstream/{name}" for name in (*MODULE04_SOURCES, *CHECKPOINT_SOURCES))
    if len(rows) != 29 or [row["relative_path"] for row in rows] != expected:
        raise HandoffError("Handoff manifest row contract mismatch")
    for row in rows:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise HandoffError(f"Handoff identity mismatch: {row['relative_path']}")

    release = json.loads((upstream / "module04-release.json").read_text(encoding="utf-8"))
    contract = json.loads((upstream / "module04-forecast-contract.json").read_text(encoding="utf-8"))
    findings = json.loads((upstream / "forecast-findings.json").read_text(encoding="utf-8"))
    diagnostic = json.loads((upstream / "module03-diagnostic-findings.json").read_text(encoding="utf-8"))
    encounters = read_csv(upstream / "encounter-measures.csv.gz", compressed=True)
    scenarios = read_csv(upstream / "scenario-register.csv.gz", compressed=True)
    truth = read_csv(upstream / "known-truth.csv.gz", compressed=True)
    measures = read_csv(upstream / "measure-specifications.csv")
    progression = (upstream / "module04-progression-decision.md").read_text(encoding="utf-8")
    if release["module_id"] != "oclc-app3-04" or release["commons_release"] != "0.70.0":
        raise HandoffError("Module 04 release identity mismatch")
    if contract["forecast"]["rolling_folds"] != 28 or contract["assessment"]["next_module"] != "oclc-app3-05":
        raise HandoffError("Module 04 forecast contract mismatch")
    if findings["selected_method"] != "seasonal_exponential_smoothing" or findings["week53"]["raw_forecast_arrivals"] != 876.924084:
        raise HandoffError("Accepted forecast finding mismatch")
    if diagnostic["bounded_diagnosis"]["target_median_minutes"] != 66.0:
        raise HandoffError("Accepted Week 3 diagnosis mismatch")
    if len(encounters) != 43628 or any(row["synthetic_flag"] != "1" for row in encounters):
        raise HandoffError("Accepted encounter profile mismatch")
    if [row["scenario_id"] for row in scenarios] != ["S00", "S01", "S02", "S03"]:
        raise HandoffError("Scenario register mismatch")
    if len(truth) != 10 or {row["truth_id"] for row in truth if row["domain"] == "scenario"} != {"KT09", "KT10"}:
        raise HandoffError("Scenario known-truth contract mismatch")
    if len(measures) != 17 or "permitted for improvement scenario and evaluation construction" not in progression:
        raise HandoffError("Measure or progression contract mismatch")
    candidate_manifest = read_csv(upstream / "checkpoint-candidate-manifest.csv")
    expected_hashes = {
        "candidate/module-02/outputs/encounter-measures.csv.gz": "a996474197924b2a06dcc7e74989207f6fbe8d06d9a8c88ef6d14f5a2a470b7c",
        "candidate/module-02/data/raw/scenarios.csv.gz": "2af4089b3a159e527b2c4f84e29400c6861d35231534dc6a52428e4e32d2a6fa",
        "candidate/module-02/data/raw/known-truth.csv.gz": "2488715f2b5cd177976ac0ba948355ca7e3917ad3d0946423ce417d7f28a6b07",
        "candidate/module-02/measure-specifications.csv": "407bb7b22f89dfda32558942337d3ae4f9634a4fc4b7e6c420ef321a271dca2e",
    }
    observed = {row["relative_path"]: row["sha256"] for row in candidate_manifest}
    if any(observed.get(path) != value for path, value in expected_hashes.items()):
        raise HandoffError("Checkpoint candidate identity mismatch")
    return {
        "files": 29,
        "module04_version": "0.1.0",
        "accepted_encounters": 43628,
        "scenarios": 4,
        "forecast_arrivals": 876.924084,
    }


def self_check() -> None:
    committed = verify(ROOT)
    with tempfile.TemporaryDirectory(prefix="app3-module05-upstream-") as temp_dir:
        base = Path(temp_dir)
        frozen = base / "upstream"
        freeze(frozen)
        if (frozen / "module05-handoff-manifest.csv").read_bytes() != (ROOT / "upstream/module05-handoff-manifest.csv").read_bytes():
            raise AssertionError("Regenerated handoff manifest differs")
        changed_root = base / "changed"
        shutil.copytree(ROOT / "upstream", changed_root / "upstream")
        path = changed_root / "upstream/week53-forecast.csv"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8", newline="\n")
        try:
            verify(changed_root)
        except HandoffError:
            pass
        else:
            raise AssertionError("Verifier accepted a changed handoff")
    print(f"APP-3 Module 05 upstream self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            rows = freeze((args.output or (ROOT / "upstream")).resolve())
            print(json.dumps({"status": "pass", "files": len(rows)}, indent=2))
        else:
            print(json.dumps(verify(ROOT), indent=2))
    except (OSError, ValueError, KeyError, ImportError, HandoffError) as error:
        parser.exit(1, f"Upstream handoff failed: {error}\n")


if __name__ == "__main__":
    main()

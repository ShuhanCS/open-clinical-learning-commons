"""Freeze and verify the accepted APP-3 Week 3 checkpoint handoff."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COURSE_ROOT = ROOT.parent.parent
CHECKPOINT = COURSE_ROOT / "checkpoints/01-measures-variation-readiness"
CHECKPOINT_SOURCES = {
    "checkpoint-contract.json": "checkpoint-contract.json",
    "checkpoint-candidate-manifest.csv": "candidate-manifest.csv",
    "checkpoint-evidence-index.csv": "evidence-index.csv",
    "checkpoint-readiness-review.md": "measures-variation-readiness-review.md",
    "checkpoint-gates.csv": "checkpoint-gates.csv",
    "checkpoint-defense.md": "checkpoint-defense.md",
    "checkpoint-progression-decision.md": "progression-decision.md",
    "module02-operational-contract.json": "candidate/module-02/operational-contract.json",
    "module02-release.json": "candidate/module-02/release.json",
    "calendar-demand.csv.gz": "candidate/module-02/data/raw/calendar-demand.csv.gz",
    "staffing.csv.gz": "candidate/module-02/data/raw/staffing.csv.gz",
    "shift-metrics.csv": "candidate/module-02/outputs/shift-metrics.csv",
    "weekly-metrics.csv": "candidate/module-02/outputs/weekly-metrics.csv",
    "module02-build-report.json": "candidate/module-02/outputs/build-report.json",
    "module03-diagnostic-contract.json": "candidate/module-03/diagnostic-contract.json",
    "module03-release.json": "candidate/module-03/release.json",
    "module03-diagnostic-findings.json": "candidate/module-03/outputs/diagnostic-findings.json",
    "module03-variation-series.csv": "candidate/module-03/outputs/variation-series.csv",
    "module03-signal-audit.csv": "candidate/module-03/outputs/signal-audit.csv",
    "module03-bottleneck-reconciliation.csv": "candidate/module-03/outputs/bottleneck-reconciliation.csv",
    "module03-subgroup-window-support.csv": "candidate/module-03/outputs/subgroup-window-support.csv",
    "module03-escalation-rule.md": "candidate/module-03/escalation-rule.md",
}


class HandoffError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_checkpoint_builder():
    spec = importlib.util.spec_from_file_location("app3_checkpoint01_builder", CHECKPOINT / "build_checkpoint.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load APP-3 Checkpoint 01 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def freeze(output: Path) -> list[dict[str, object]]:
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {output}")
    output.mkdir(parents=True)
    rows: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="app3-module04-checkpoint-") as temp_dir:
        assembled = Path(temp_dir) / "checkpoint"
        report = load_checkpoint_builder().assemble(assembled, reference=True)
        if report != {
            "status": "pass", "mode": "reference", "candidate_manifest_rows": 137,
            "candidate_manifest_bytes": 23862,
            "candidate_manifest_sha256": "9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656",
            "assembled_files": 153,
        }:
            raise HandoffError("Checkpoint assembly identity changed")
        sources = {"checkpoint-release.json": CHECKPOINT / "release.json"}
        sources.update({name: assembled / source for name, source in CHECKPOINT_SOURCES.items()})
        for target_name, source in sources.items():
            if not source.is_file():
                raise HandoffError(f"Missing checkpoint source: {source}")
            target = output / target_name
            shutil.copy2(source, target)
            rows.append({
                "relative_path": f"upstream/{target_name}",
                "source_path": source.relative_to(CHECKPOINT).as_posix() if source.is_relative_to(CHECKPOINT) else source.name,
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
                "source_release": "oclc-app3-cp01@0.1.0+commons.0.69.0",
                "role": "accepted APP-3 Week 3 handoff",
            })
    rows.sort(key=lambda row: str(row["relative_path"]))
    manifest = output / "checkpoint-handoff-manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "source_path", "bytes", "sha256", "source_release", "role"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    if len(rows) != 23 or sum(path.is_file() for path in output.iterdir()) != 24:
        raise HandoffError("Checkpoint handoff file contract changed")
    return rows


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root / "upstream"
    manifest = upstream / "checkpoint-handoff-manifest.csv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != ["relative_path", "source_path", "bytes", "sha256", "source_release", "role"]:
            raise HandoffError("Checkpoint handoff manifest header mismatch")
        rows = list(reader)
    expected = sorted(["upstream/checkpoint-release.json", *[f"upstream/{name}" for name in CHECKPOINT_SOURCES]])
    if len(rows) != 23 or [row["relative_path"] for row in rows] != expected:
        raise HandoffError("Checkpoint handoff manifest row contract mismatch")
    for row in rows:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise HandoffError(f"Checkpoint handoff identity mismatch: {row['relative_path']}")

    release = json.loads((upstream / "checkpoint-release.json").read_text(encoding="utf-8"))
    contract = json.loads((upstream / "checkpoint-contract.json").read_text(encoding="utf-8"))
    module02 = json.loads((upstream / "module02-build-report.json").read_text(encoding="utf-8"))
    module03 = json.loads((upstream / "module03-diagnostic-findings.json").read_text(encoding="utf-8"))
    progression = (upstream / "checkpoint-progression-decision.md").read_text(encoding="utf-8")
    with (upstream / "shift-metrics.csv").open(encoding="utf-8", newline="") as handle:
        shifts = list(csv.DictReader(handle))
    with (upstream / "weekly-metrics.csv").open(encoding="utf-8", newline="") as handle:
        weeks = list(csv.DictReader(handle))
    if release["checkpoint"]["id"] != "oclc-app3-cp01" or release["checkpoint"]["commons_release"] != "0.69.0":
        raise HandoffError("Checkpoint release identity mismatch")
    if release["package"]["candidate_manifest_sha256"] != "9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656":
        raise HandoffError("Checkpoint candidate manifest identity mismatch")
    if contract["course_points"] != 40 or contract["accepted_component_files"] != 137:
        raise HandoffError("Checkpoint score or candidate contract mismatch")
    if module02["findings"]["accepted_encounters"] != 43628 or module02["findings"]["failed_query_checks"] != 0:
        raise HandoffError("Module 02 accepted findings mismatch")
    if module03["control_charts"]["signal_records"] != 9 or module03["bounded_diagnosis"]["target_median_minutes"] != 66.0:
        raise HandoffError("Module 03 accepted diagnostic mismatch")
    if len(shifts) != 1092 or len(weeks) != 52 or any(row["synthetic_flag"] != "1" for row in shifts):
        raise HandoffError("Accepted demand history mismatch")
    if "Module 04 permission: `permitted for demand forecasting and capacity analysis`" not in progression:
        raise HandoffError("Checkpoint did not permit Module 04")
    return {
        "files": 23,
        "checkpoint_version": "0.1.0",
        "candidate_files": 137,
        "shift_rows": 1092,
        "weeks": 52,
        "accepted_encounters": 43628,
    }


def self_check() -> None:
    committed = verify(ROOT)
    with tempfile.TemporaryDirectory(prefix="app3-module04-upstream-") as temp_dir:
        base = Path(temp_dir)
        frozen = base / "upstream"
        freeze(frozen)
        if (frozen / "checkpoint-handoff-manifest.csv").read_bytes() != (ROOT / "upstream/checkpoint-handoff-manifest.csv").read_bytes():
            raise AssertionError("Regenerated checkpoint handoff manifest differs")
        changed_root = base / "changed"
        shutil.copytree(ROOT / "upstream", changed_root / "upstream")
        path = changed_root / "upstream/shift-metrics.csv"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8", newline="\n")
        try:
            verify(changed_root)
        except HandoffError:
            pass
        else:
            raise AssertionError("Verifier accepted a changed checkpoint handoff")
    print(f"APP-3 Module 04 upstream self-check passed: {json.dumps(committed, sort_keys=True)}")


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

"""Freeze and verify the accepted APP-3 Module 02 handoff."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODULE02 = ROOT.parent / "02-measures-operational-metrics"
SOURCES = {
    "module02-operational-contract.json": "operational-contract.json",
    "module02-release.json": "release.json",
    "operational-source-manifest.csv": "data/operational-source-manifest.csv",
    "safety-events.csv.gz": "data/raw/safety-events.csv.gz",
    "encounter-measures.csv.gz": "outputs/encounter-measures.csv.gz",
    "shift-metrics.csv": "outputs/shift-metrics.csv",
    "weekly-metrics.csv": "outputs/weekly-metrics.csv",
    "safety-diagnostics.csv": "outputs/safety-diagnostics.csv",
    "subgroup-support.csv": "outputs/subgroup-support.csv",
    "query-checks.csv": "outputs/query-checks.csv",
    "build-report.json": "outputs/build-report.json",
    "measure-specifications.csv": "reference/measure-specifications.csv",
    "event-validation.md": "reference/event-validation.md",
    "progression-decision.md": "reference/progression-decision.md",
}


class HandoffError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def freeze(output: Path, source_root: Path = MODULE02) -> list[dict[str, object]]:
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    for target_name, source_name in SOURCES.items():
        source = source_root / source_name
        if not source.is_file():
            raise HandoffError(f"Missing Module 02 source: {source_name}")
        target = output / target_name
        shutil.copy2(source, target)
        rows.append({
            "relative_path": f"upstream/{target_name}", "source_path": source_name,
            "bytes": target.stat().st_size, "sha256": sha256(target),
            "role": "accepted APP-3 Module 02 handoff",
        })
    rows.sort(key=lambda row: str(row["relative_path"]))
    with (output / "module02-handoff-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "source_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def verify(root: Path = ROOT, source_root: Path | None = None) -> dict[str, object]:
    upstream = root / "upstream"
    with (upstream / "module02-handoff-manifest.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != ["relative_path", "source_path", "bytes", "sha256", "role"]:
            raise HandoffError("Module 02 handoff manifest header mismatch")
        rows = list(reader)
    expected = sorted(f"upstream/{name}" for name in SOURCES)
    if len(rows) != 14 or [row["relative_path"] for row in rows] != expected:
        raise HandoffError("Module 02 handoff manifest row contract mismatch")
    for row in rows:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise HandoffError(f"Module 02 handoff identity mismatch: {row['relative_path']}")
        live = source_root / row["source_path"] if source_root else None
        if live and live.is_file() and sha256(live) != row["sha256"]:
            raise HandoffError(f"Live Module 02 source changed: {row['source_path']}")
    contract = json.loads((upstream / "module02-operational-contract.json").read_text(encoding="utf-8"))
    release = json.loads((upstream / "module02-release.json").read_text(encoding="utf-8"))
    report = json.loads((upstream / "build-report.json").read_text(encoding="utf-8"))
    progression = (upstream / "progression-decision.md").read_text(encoding="utf-8")
    if contract["module"]["id"] != "oclc-app3-02" or contract["service"]["id"] != "CGH-ED-01":
        raise HandoffError("Module 02 identity mismatch")
    if release["module_version"] != "0.1.0" or release["commons_release"] != "0.67.0":
        raise HandoffError("Module 02 release mismatch")
    if report["findings"]["accepted_encounters"] != 43628 or report["findings"]["failed_query_checks"] != 0:
        raise HandoffError("Module 02 accepted findings mismatch")
    if "Progression: `continue with conditions`" not in progression or "Module 03 permission: `permitted for curriculum construction`" not in progression:
        raise HandoffError("Module 02 did not permit Module 03 construction")
    return {"files": 14, "module02_version": "0.1.0", "accepted_encounters": 43628, "query_checks": 30}


def self_check() -> None:
    committed = verify(ROOT, MODULE02)
    with tempfile.TemporaryDirectory(prefix="app3-module03-upstream-") as temp_dir:
        base = Path(temp_dir)
        frozen = base / "upstream"
        freeze(frozen)
        if (frozen / "module02-handoff-manifest.csv").read_bytes() != (ROOT / "upstream/module02-handoff-manifest.csv").read_bytes():
            raise AssertionError("Regenerated Module 02 handoff manifest differs")
        changed = base / "changed"
        shutil.copytree(ROOT / "upstream", changed / "upstream")
        path = changed / "upstream/weekly-metrics.csv"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        try:
            verify(changed)
        except HandoffError:
            pass
        else:
            raise AssertionError("Verifier accepted a changed Module 02 handoff")
    print(f"APP-3 Module 03 upstream self-check passed: {json.dumps(committed, sort_keys=True)}")


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
            print(json.dumps(verify(ROOT, MODULE02), indent=2))
    except (OSError, ValueError, KeyError, HandoffError) as error:
        parser.exit(1, f"Upstream handoff failed: {error}\n")


if __name__ == "__main__":
    main()

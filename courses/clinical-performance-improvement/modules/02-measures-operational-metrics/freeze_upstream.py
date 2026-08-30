"""Freeze and verify the accepted APP-3 Module 01 handoff."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODULE01 = ROOT.parent / "01-clinical-performance-decision"
SOURCES = {
    "module01-decision-contract.json": "decision-contract.json",
    "module01-source-inventory.csv": "data/source-inventory.csv",
    "clinical-performance-charter.md": "reference/clinical-performance-charter.md",
    "synthetic-service-declaration.md": "reference/synthetic-service-declaration.md",
    "unit-of-flow.csv": "reference/unit-of-flow.csv",
    "process-boundary.csv": "reference/process-boundary.csv",
    "measure-family.csv": "reference/measure-family.csv",
    "source-feasibility-interpretation.md": "reference/source-feasibility-interpretation.md",
    "claim-boundary.csv": "reference/claim-boundary.csv",
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


def freeze(output: Path, source_root: Path = MODULE01) -> list[dict[str, object]]:
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    for target_name, source_name in SOURCES.items():
        source = source_root / source_name
        if not source.is_file():
            raise HandoffError(f"Missing Module 01 source: {source_name}")
        target = output / target_name
        shutil.copy2(source, target)
        rows.append({
            "relative_path": f"upstream/{target_name}", "source_path": source_name,
            "bytes": target.stat().st_size, "sha256": sha256(target),
            "role": "accepted APP-3 Module 01 handoff",
        })
    rows.sort(key=lambda row: str(row["relative_path"]))
    with (output / "module01-handoff-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "source_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def verify(root: Path = ROOT, source_root: Path | None = None) -> dict[str, object]:
    upstream = root / "upstream"
    manifest_path = upstream / "module01-handoff-manifest.csv"
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != ["relative_path", "source_path", "bytes", "sha256", "role"]:
            raise HandoffError("Module 01 handoff manifest header mismatch")
        rows = list(reader)
    if len(rows) != 10 or [row["relative_path"] for row in rows] != sorted(f"upstream/{name}" for name in SOURCES):
        raise HandoffError("Module 01 handoff manifest row contract mismatch")
    for row in rows:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise HandoffError(f"Module 01 handoff identity mismatch: {row['relative_path']}")
        if source_root and (source_root / row["source_path"]).is_file() and sha256(source_root / row["source_path"]) != row["sha256"]:
            raise HandoffError(f"Live Module 01 source changed: {row['source_path']}")
    contract = json.loads((upstream / "module01-decision-contract.json").read_text(encoding="utf-8"))
    progression = (upstream / "progression-decision.md").read_text(encoding="utf-8")
    if contract["module"]["id"] != "oclc-app3-01" or contract["service"]["id"] != "CGH-ED-01":
        raise HandoffError("Module 01 decision identity mismatch")
    if "Progression: `continue with conditions`" not in progression or "Module 02 permission: `permitted for curriculum construction`" not in progression:
        raise HandoffError("Module 01 did not permit Module 02 construction")
    return {"files": 10, "module01_version": contract["module"]["version"], "progression": "continue with conditions"}


def self_check() -> None:
    committed = verify(ROOT, MODULE01)
    with tempfile.TemporaryDirectory(prefix="app3-module02-upstream-") as temp_dir:
        temp = Path(temp_dir)
        frozen = temp / "upstream"
        freeze(frozen)
        if (frozen / "module01-handoff-manifest.csv").read_bytes() != (ROOT / "upstream/module01-handoff-manifest.csv").read_bytes():
            raise AssertionError("Regenerated Module 01 handoff manifest differs")
        changed = temp / "changed"
        shutil.copytree(ROOT / "upstream", changed / "upstream")
        path = changed / "upstream/clinical-performance-charter.md"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        try:
            verify(changed)
        except HandoffError:
            pass
        else:
            raise AssertionError("Verifier accepted a changed Module 01 handoff")
    print(f"APP-3 Module 02 upstream self-check passed: {json.dumps(committed, sort_keys=True)}")


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
            print(json.dumps({"status": "pass", "files": freeze((args.output or (ROOT / "upstream")).resolve())}, indent=2))
        else:
            print(json.dumps(verify(ROOT, MODULE01), indent=2))
    except (OSError, ValueError, KeyError, HandoffError) as error:
        parser.exit(1, f"Upstream handoff failed: {error}\n")


if __name__ == "__main__":
    main()

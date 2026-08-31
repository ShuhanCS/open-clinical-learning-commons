"""Build an APP-3 Module 04 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONTROL_FILES = (
    ".gitattributes", "VERSION", "assessment.md", "data-spec.md",
    "forecast-contract.json", "release.json", "source-record.yml",
    "freeze_upstream.py", "build_forecast.py", "build_workspace.py",
    "validate_workspace.py", "verify_forecast.R",
)
UPSTREAM_FILES = tuple(f"upstream/{name}" for name in (
    "calendar-demand.csv.gz", "checkpoint-candidate-manifest.csv",
    "checkpoint-contract.json", "checkpoint-defense.md",
    "checkpoint-evidence-index.csv", "checkpoint-gates.csv",
    "checkpoint-handoff-manifest.csv", "checkpoint-progression-decision.md",
    "checkpoint-readiness-review.md", "checkpoint-release.json",
    "module02-build-report.json", "module02-operational-contract.json",
    "module02-release.json", "module03-bottleneck-reconciliation.csv",
    "module03-diagnostic-contract.json", "module03-diagnostic-findings.json",
    "module03-escalation-rule.md", "module03-release.json",
    "module03-signal-audit.csv", "module03-subgroup-window-support.csv",
    "module03-variation-series.csv", "shift-metrics.csv", "staffing.csv.gz",
    "weekly-metrics.csv",
))
RECORD_FILES = (
    "forecast-plan.md", "fold-audit.csv", "model-comparison.md",
    "failure-period-review.md", "capacity-interpretation.md",
    "littles-law-interpretation.md", "accessible-output-review.md",
    "gate-results.csv", "module05-handoff.md", "ai-use.md",
    "progression-decision.md", "reproducibility-check.md",
)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in (
    "folds.csv", "forecast-predictions.csv", "error-summary.csv",
    "error-slices.csv", "week53-forecast.csv", "capacity-implication.csv",
    "littles-law-check.csv", "forecast-findings.json",
    "forecast-error-comparison.svg", "week53-demand-forecast.svg",
))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = ROOT / ("reference" if reference else "template")
    immutable = CONTROL_FILES + UPSTREAM_FILES + (OUTPUT_FILES if reference else ())
    required = list(immutable) + [f"{record_root.name}/{name}" for name in RECORD_FILES]
    missing = [name for name in required if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    manifest = []
    for relative in immutable:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        role = "reference forecast output" if relative.startswith("outputs/") else (
            "immutable checkpoint evidence" if relative.startswith("upstream/") else "immutable Module 04 control"
        )
        manifest.append({
            "relative_path": relative,
            "bytes": destination.stat().st_size,
            "sha256": sha256(destination),
            "role": role,
        })
    for relative in RECORD_FILES:
        copy(record_root / relative, target, relative)
    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    expected_files = 59 if reference else 49
    expected_manifest = 46 if reference else 36
    if files != expected_files or len(manifest) != expected_manifest:
        raise ValueError(f"Workspace contract changed: {files} files and {len(manifest)} manifest rows")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "assembled_files": files,
        "manifest_rows": len(manifest),
        "manifest_sha256": sha256(target / "release-manifest.csv"),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app3-module04-workspace-") as temp_dir:
        base = Path(temp_dir)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        starter = assemble(base / "starter")
        assert first["assembled_files"] == 59 and first["manifest_rows"] == 46
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert starter["assembled_files"] == 49 and starter["manifest_rows"] == 36
        assert "REPLACE" in (base / "starter/forecast-plan.md").read_text(encoding="utf-8")
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-3 Module 04 workspace-builder self-check passed: 49 learner files and 59 reference files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.target:
            print(json.dumps(assemble(args.target, reference=args.reference), indent=2))
        else:
            parser.error("--target is required")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Workspace build failed: {error}\n")


if __name__ == "__main__":
    main()

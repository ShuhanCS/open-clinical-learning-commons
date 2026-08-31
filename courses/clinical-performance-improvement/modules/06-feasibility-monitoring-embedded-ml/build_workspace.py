"""Build an APP-3 Module 06 learner or reference workspace."""

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
    "ml-contract.json", "release.json", "source-record.yml",
    "freeze_upstream.py", "build_evidence.py", "build_workspace.py",
    "validate_workspace.py",
)
UPSTREAM_FILES = tuple(f"upstream/{path.name}" for path in sorted((ROOT / "upstream").iterdir()) if path.is_file())
RECORD_FILES = (
    "feasibility-review.md", "quality-safety-review.md",
    "access-equity-review.md", "workforce-review.md", "dashboard-review.md",
    "escalation-fallback-review.md", "monitoring-stewardship.md",
    "accountability-map.csv", "ml-contract-review.md", "model-comparison.md",
    "failure-review.md", "week6-score.csv", "gate-results.csv",
    "module07-handoff.md", "ai-use.md", "progression-decision.md",
    "reproducibility-check.md",
)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in (
    "upstream-inventory.csv", "feasibility-screen.csv", "monitoring-measures.csv",
    "escalation-fallback.csv", "dashboard-data.csv", "ml-split-registry.csv",
    "ml-predictions.csv", "model-performance.csv", "fold-comparison.csv",
    "model-error-slices.csv", "feature-importance.csv", "failure-cases.csv",
    "leakage-tests.csv", "week53-model-comparison.csv", "decision-change.csv",
    "invariant-checks.csv", "build-report.json", "forecast-comparison.svg",
    "monitoring-dashboard.html",
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
        role = "reference feasibility, monitoring, and ML output" if relative.startswith("outputs/") else (
            "immutable accepted evidence" if relative.startswith("upstream/") else "immutable Module 06 control"
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
    expected_files = 82 if reference else 63
    expected_manifest = 64 if reference else 45
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
    with tempfile.TemporaryDirectory(prefix="app3-module06-workspace-") as temp_dir:
        base = Path(temp_dir)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        starter = assemble(base / "starter")
        assert first["assembled_files"] == 82 and first["manifest_rows"] == 64
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert starter["assembled_files"] == 63 and starter["manifest_rows"] == 45
        assert "REPLACE" in (base / "starter/model-comparison.md").read_text(encoding="utf-8")
        assert not (base / "starter/outputs").exists()
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-3 Module 06 workspace-builder self-check passed: 63 learner files and 82 reference files.")


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

"""Assemble FND-2 Checkpoint 1 from accepted Module 01 through 03 evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parents[3]
COURSE_ROOT = REPO_ROOT / "courses" / "modeling-inference-reproducible-analytics"
REFERENCE = PACKAGE_ROOT / "reference"
TEMPLATE = PACKAGE_ROOT / "template"
REFERENCE_MODULES = (
    COURSE_ROOT / "modules" / "01-aims-reproducible-workspace",
    COURSE_ROOT / "modules" / "02-regression-interpretation",
    COURSE_ROOT / "modules" / "03-prediction-evaluation",
)
MODULE_NAMES = (
    "01-aims-reproducible-workspace",
    "02-regression-interpretation",
    "03-prediction-evaluation",
)
M1_ARTIFACTS = (
    "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "aim-classification-exercises.csv", "aim-and-method-plan.md",
    "estimand-target-registry.csv", "feature-role-contract.csv", "environment-note.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
    "outputs/modeling-cohort.csv", "outputs/split-registry.csv",
    "outputs/baseline-metrics.csv", "outputs/modeling-checks.csv", "outputs/build-report.json",
)
M2_ARTIFACTS = (
    "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "formula-registry.csv", "reference-levels.csv", "interpretation-quantity-guide.csv",
    "regression-interpretation.md", "r-run-record.md", "environment-note.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
    "outputs/linear-subset-registry.csv", "outputs/linear-coefficients.csv",
    "outputs/linear-diagnostics.csv", "outputs/linear-prediction-examples.csv",
    "outputs/logistic-coefficients.csv", "outputs/logistic-diagnostics.csv",
    "outputs/logistic-prediction-examples.csv", "outputs/model-matrix-fields.csv",
    "outputs/model-comparison.csv", "outputs/sparse-cell-checks.csv",
    "outputs/assumption-register.csv", "outputs/r-reading-fixture.csv",
    "outputs/regression-checks.csv", "outputs/build-report.json",
)
M3_ARTIFACTS = (
    "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "model-contract.json", "prediction-evaluation-report.md", "figure-accessibility.md",
    "environment-note.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md",
    "outputs/resampling-results.csv", "outputs/validation-predictions.csv",
    "outputs/validation-comparison.csv", "outputs/model-selection-record.csv",
    "outputs/threshold-table.csv", "outputs/threshold-decision.csv",
    "outputs/test-predictions.csv", "outputs/test-metrics.csv",
    "outputs/confusion-table.csv", "outputs/calibration-table.csv",
    "outputs/subgroup-metrics.csv", "outputs/transformed-feature-names.csv",
    "outputs/leaked-model-failure.csv", "outputs/prediction-checks.csv",
    "outputs/calibration.svg", "outputs/threshold.svg", "outputs/build-report.json",
)
ARTIFACTS = (M1_ARTIFACTS, M2_ARTIFACTS, M3_ARTIFACTS)
CONTROL_FILES = (
    ".gitattributes", ".gitignore", "VERSION", "checkpoint-contract.json",
    "assessment.md", "validate_checkpoint.py",
)
EDITABLE_RECORDS = (
    "README.md", "cumulative-interpretation.md", "technical-defense.md",
    "component-score.csv", "gate-results.csv", "reviewer-record.md",
    "reproduction-record.md", "accessibility-review.md", "ai-use.md",
    "progression-decision.md",
)
KEY_HASHES = {
    (0, "outputs/modeling-cohort.csv"): "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332",
    (0, "outputs/split-registry.csv"): "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1",
    (1, "formula-registry.csv"): "fc69d6146eec729969b571b535c13027e9b875d34dd99637f0dc0d9b934239a6",
    (2, "outputs/test-predictions.csv"): "531c00d310292aeeaea476d1c94e128f5c81c34c2fc60e014d2c157e152b7438",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_files(root: Path, names: tuple[str, ...], label: str) -> None:
    missing = [name for name in names if not (root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"{label} is missing: {', '.join(missing)}")


def verify_modules(roots: tuple[Path, Path, Path]) -> None:
    for index, (root, names) in enumerate(zip(roots, ARTIFACTS, strict=True)):
        require_files(root, names, f"Module {index + 1:02d}")
        if (root / "VERSION").read_text(encoding="utf-8").strip() != "0.1.0":
            raise ValueError(f"Module {index + 1:02d} version must be 0.1.0")
    for (index, relative), digest in KEY_HASHES.items():
        if sha256(roots[index] / relative) != digest:
            raise ValueError(f"Module {index + 1:02d} key fingerprint changed: {relative}")
    m1 = json.loads((roots[0] / "outputs/build-report.json").read_text(encoding="utf-8"))
    if [m1["split"][name]["rows"] for name in ("train", "validation", "test")] != [224, 75, 75]:
        raise ValueError("Module 01 split contract changed")
    if [m1["split"][name]["positives"] for name in ("train", "validation", "test")] != [25, 7, 4]:
        raise ValueError("Module 01 outcome contract changed")
    m3 = json.loads((roots[2] / "outputs/build-report.json").read_text(encoding="utf-8"))
    if m3["selection"]["model_id"] != "ML01" or m3["selection"]["locked_threshold"] != "0.08513264":
        raise ValueError("Module 03 selection contract changed")
    if m3["test_confusion"] != {"true_negative": 48, "false_positive": 23, "false_negative": 2, "true_positive": 2}:
        raise ValueError("Module 03 test confusion contract changed")


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def assemble(target: Path, roots: tuple[Path, Path, Path], reference: bool) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_modules(roots)
    record_root = REFERENCE if reference else TEMPLATE
    require_files(PACKAGE_ROOT, CONTROL_FILES, "Checkpoint controls")
    require_files(record_root, EDITABLE_RECORDS, "Checkpoint records")
    target.mkdir(parents=True)
    immutable: dict[str, tuple[str, str]] = {}

    for name in CONTROL_FILES:
        copy_file(PACKAGE_ROOT / name, target / name)
        immutable[name] = ("Checkpoint 1", "0.1.0")
    for name in EDITABLE_RECORDS:
        copy_file(record_root / name, target / name)

    for index, (root, names, module_name) in enumerate(zip(roots, ARTIFACTS, MODULE_NAMES, strict=True), start=1):
        for name in names:
            relative = f"modules/{module_name}/{name}"
            copy_file(root / name, target / relative)
            immutable[relative] = (f"Module {index:02d}", "0.1.0")

    manifest = target / "release-manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("relative_path", "source_unit", "source_version", "bytes", "sha256"))
        for relative in sorted(immutable):
            path = target / relative
            unit, version = immutable[relative]
            writer.writerow((relative, unit, version, path.stat().st_size, sha256(path)))

    file_count = sum(path.is_file() for path in target.rglob("*"))
    if len(immutable) != 78 or file_count != 89:
        raise ValueError(f"Checkpoint file contract changed: {len(immutable)} manifest rows and {file_count} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "module_artifacts": sum(len(names) for names in ARTIFACTS),
        "manifest_rows": len(immutable),
        "manifest_bytes": manifest.stat().st_size,
        "manifest_sha256": sha256(manifest),
        "assembled_files": file_count,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd2-checkpoint1-assemble-") as temp_dir:
        base = Path(temp_dir)
        first = base / "reference-1"
        second = base / "reference-2"
        learner = base / "learner"
        report = assemble(first, REFERENCE_MODULES, reference=True)
        second_report = assemble(second, REFERENCE_MODULES, reference=True)
        learner_report = assemble(learner, REFERENCE_MODULES, reference=False)
        assert report["manifest_rows"] == 78 and report["assembled_files"] == 89
        assert report["manifest_sha256"] == second_report["manifest_sha256"]
        assert learner_report["mode"] == "learner"
        assert (first / "modules/03-prediction-evaluation/outputs/test-predictions.csv").is_file()
        try:
            assemble(first, REFERENCE_MODULES, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not refuse an existing target")
    print("FND-2 Checkpoint 1 assembler self-check passed: 72 module artifacts, 78 manifest rows, and 89 assembled files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--module01", type=Path)
    parser.add_argument("--module02", type=Path)
    parser.add_argument("--module03", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.target is None:
        parser.error("target is required unless --self-check is used")
    if args.reference:
        roots = REFERENCE_MODULES
    else:
        if not all((args.module01, args.module02, args.module03)):
            parser.error("learner assembly requires --module01, --module02, and --module03")
        roots = tuple(path.resolve() for path in (args.module01, args.module02, args.module03))
    print(json.dumps(assemble(args.target.resolve(), roots, args.reference), indent=2))


if __name__ == "__main__":
    main()

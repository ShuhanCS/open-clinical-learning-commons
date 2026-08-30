"""Assemble FND-2 Checkpoint 2 from accepted Checkpoint 1 and Modules 04-06."""

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
REFERENCE_CP1 = COURSE_ROOT / "checkpoints" / "01-modeling-readiness-release"
REFERENCE_M04 = COURSE_ROOT / "modules" / "04-validity-adjustment-longitudinal"
REFERENCE_M05 = COURSE_ROOT / "modules" / "05-forecasting-temporal-validation"
REFERENCE_M06 = COURSE_ROOT / "modules" / "06-agent-assisted-modeling-testing"
REFERENCE_PUBLIC = REPO_ROOT / "courses" / "data-visualization" / "modules" / "08-time-process-variation" / "data"

CP1_ARTIFACTS = (
    "VERSION", "checkpoint-contract.json", "release.json", "reference/progression-decision.md",
    "modules/01-aims-reproducible-workspace/outputs/modeling-cohort.csv",
    "modules/01-aims-reproducible-workspace/outputs/split-registry.csv",
    "modules/03-prediction-evaluation/model-contract.json",
    "modules/03-prediction-evaluation/outputs/test-predictions.csv",
    "modules/03-prediction-evaluation/outputs/confusion-table.csv",
    "modules/03-prediction-evaluation/outputs/calibration-table.csv",
    "modules/03-prediction-evaluation/outputs/transformed-feature-names.csv",
)
M04_ARTIFACTS = (
    "VERSION", "requirements.txt", "data-spec.md", "source-record.yml", "assessment.md",
    "causal-claim-screen.md", "dag.mmd", "dag-narrative.md",
    "validity-adjustment-longitudinal-memo.md", "mixed-model-reading.md",
    "survival-censoring-reading.md", "specialist-referrals.md", "paired-longitudinal-survival.R",
    "reproducibility-check.md", "accessibility-review.md", "ai-use.md",
    "progression-decision.md", "release.json",
    "outputs/analytic-aim-validity-map.csv", "outputs/dag-nodes.csv", "outputs/dag-edges.csv",
    "outputs/dag.svg", "outputs/overlap-table.csv", "outputs/balance-table.csv",
    "outputs/adjustment-estimates.csv", "outputs/selection-profile.csv",
    "outputs/missingness-profile.csv", "outputs/missingness-mechanisms.csv",
    "outputs/longitudinal-models.csv", "outputs/mixed-variance.csv",
    "outputs/kaplan-meier-table.csv", "outputs/cox-reading.csv",
    "outputs/validity-threat-register.csv", "outputs/validity-checks.csv", "outputs/build-report.json",
)
M05_ARTIFACTS = (
    "VERSION", "requirements.txt", "data-spec.md", "source-record.yml", "forecast-contract.json",
    "assessment.md", "forecasting-temporal-validation-memo.md", "benchmark-defense.md",
    "arima-reading.md", "forecast-text-alternative.md", "failure-and-referral.md",
    "reproducibility-check.md", "accessibility-review.md", "ai-use.md",
    "progression-decision.md", "release.json",
    "outputs/forecast-target.csv", "outputs/temporal-folds.csv", "outputs/benchmark-registry.csv",
    "outputs/forecast-predictions.csv", "outputs/holt-parameters.csv",
    "outputs/forecast-interval-reading.csv", "outputs/aggregate-metrics.csv",
    "outputs/fold-metrics.csv", "outputs/horizon-metrics.csv", "outputs/failure-analysis.csv",
    "outputs/reporting-coverage-context.csv", "outputs/decomposition-reading.csv",
    "outputs/stationarity-reading.csv", "outputs/arima-parameters.csv",
    "outputs/arima-forecast-reading.csv", "outputs/residual-diagnostics.csv",
    "outputs/forecast-checks.csv", "outputs/forecast.svg", "outputs/build-report.json",
)
M06_ARTIFACTS = (
    "VERSION", "requirements.txt", "data-spec.md", "source-record.yml", "test-contract.json",
    "assessment.md", "prompt-constraints.md", "prompt-trace-log.csv", "agent-task-plan.md",
    "agent-critique.md", "claim-adjudication.csv", "independent-verification.md",
    "human-sign-off.md", "reproducibility-check.md", "accessibility-review.md", "ai-use.md",
    "progression-decision.md", "release.json",
    "outputs/accepted-artifact-manifest.csv", "outputs/accepted-contract-tests.csv",
    "outputs/seeded-failure-results.csv", "outputs/independent-verification.csv",
    "outputs/claim-adjudication.csv", "outputs/data-class-rules.csv", "outputs/test-summary.csv",
    "outputs/failure-fixtures.json", "outputs/test-summary.md", "outputs/build-report.json",
)
PUBLIC_ARTIFACTS = (
    "nhsn_hospital_capacity_jurisdiction_2024_2026.csv",
    "ma_hospital_capacity_time_2024_2026.csv",
)
CONTROL_FILES = (
    ".gitattributes", ".gitignore", "VERSION", "checkpoint-contract.json",
    "assessment.md", "validate_checkpoint.py",
)
EDITABLE_RECORDS = (
    "README.md", "cumulative-interpretation.md", "technical-defense.md",
    "component-score.csv", "gate-results.csv", "conditions-register.csv",
    "reviewer-record.md", "reproduction-record.md", "accessibility-review.md",
    "ai-use.md", "human-sign-off.md", "progression-decision.md",
)
RELEASE_HASHES = {
    "checkpoint1": "03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f",
    "module04": "ffcf57c30d77be5c2271488a4d2dd08cc44d430cc590025e918c0ec8f1c4e12e",
    "module05": "d81bcc3ac2ac2971cb1a03467673d86a905a125f7aed859f2e7669e9c7003f6d",
    "module06": "bfc137523817e57b9eab6baf5729222f5a8021df203c36ba1162f4f7757e824e",
}
DATA_HASHES = {
    "modeling": "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332",
    "split": "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1",
    "cdc": "8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1",
    "ma": "394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616",
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


def require_files(root: Path, names: tuple[str, ...], label: str) -> None:
    missing = [name for name in names if not (root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"{label} is missing: {', '.join(missing)}")


def cp1_path(root: Path, name: str) -> Path:
    """Use an assembled CP1 when supplied; the repository keeps reference module evidence at course level."""
    direct = root / name
    return direct if direct.is_file() else COURSE_ROOT / name


def verify_inputs(cp1: Path, m04: Path, m05: Path, m06: Path, public: Path) -> None:
    missing_cp1 = [name for name in CP1_ARTIFACTS if not cp1_path(cp1, name).is_file()]
    if missing_cp1:
        raise FileNotFoundError(f"Checkpoint 1 is missing: {', '.join(missing_cp1)}")
    units = (
        (m04, M04_ARTIFACTS, "Module 04"),
        (m05, M05_ARTIFACTS, "Module 05"), (m06, M06_ARTIFACTS, "Module 06"),
        (public, PUBLIC_ARTIFACTS, "Public data"),
    )
    for root, names, label in units:
        require_files(root, names, label)
    for root, label in ((cp1, "Checkpoint 1"), (m04, "Module 04"), (m05, "Module 05"), (m06, "Module 06")):
        if (root / "VERSION").read_text(encoding="utf-8").strip() != "0.1.0":
            raise ValueError(f"{label} version must be 0.1.0")
    for key, root in (("checkpoint1", cp1), ("module04", m04), ("module05", m05), ("module06", m06)):
        if sha256(root / "release.json") != RELEASE_HASHES[key]:
            raise ValueError(f"{key} release fingerprint changed")
    key_files = {
        "modeling": cp1_path(cp1, "modules/01-aims-reproducible-workspace/outputs/modeling-cohort.csv"),
        "split": cp1_path(cp1, "modules/01-aims-reproducible-workspace/outputs/split-registry.csv"),
        "cdc": public / PUBLIC_ARTIFACTS[0], "ma": public / PUBLIC_ARTIFACTS[1],
    }
    for key, path in key_files.items():
        if sha256(path) != DATA_HASHES[key]:
            raise ValueError(f"{key} data fingerprint changed")
    split = read_csv(key_files["split"])
    if [sum(row["split"] == name for row in split) for name in ("train", "validation", "test")] != [224, 75, 75]:
        raise ValueError("Checkpoint 1 split contract changed")
    m04_report = json.loads((m04 / "outputs/build-report.json").read_text(encoding="utf-8"))
    if m04_report["selection_case"] != {"cohort_rows": 374, "timing_rows": 111, "structural_blanks": 263}:
        raise ValueError("Module 04 selection contract changed")
    if m04_report["repeated_case"] != {"rows": 2400, "people": 600, "visits_per_person": 4}:
        raise ValueError("Module 04 repeated-measures contract changed")
    m05_report = json.loads((m05 / "outputs/build-report.json").read_text(encoding="utf-8"))
    if m05_report["series"]["rows"] != 94 or m05_report["backtest"]["folds"] != 5 or m05_report["backtest"]["horizon_weeks"] != 4:
        raise ValueError("Module 05 temporal contract changed")
    m06_report = json.loads((m06 / "outputs/build-report.json").read_text(encoding="utf-8"))
    if m06_report["tests"] != {"accepted": 18, "seeded_failures": 10, "independent_verifications": 3, "agent_claims": 4, "summary_gates": 7}:
        raise ValueError("Module 06 test contract changed")
    if len(read_csv(key_files["cdc"])) != 6208 or len(read_csv(key_files["ma"])) != 94:
        raise ValueError("Public data row contract changed")


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def assemble(target: Path, roots: tuple[Path, Path, Path, Path, Path], reference: bool) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    cp1, m04, m05, m06, public = roots
    verify_inputs(cp1, m04, m05, m06, public)
    record_root = REFERENCE if reference else TEMPLATE
    require_files(PACKAGE_ROOT, CONTROL_FILES, "Checkpoint controls")
    require_files(record_root, EDITABLE_RECORDS, "Checkpoint records")
    target.mkdir(parents=True)
    immutable: dict[str, tuple[str, str]] = {}

    for name in CONTROL_FILES:
        copy_file(PACKAGE_ROOT / name, target / name)
        immutable[name] = ("Checkpoint 2", "0.1.0")
    for name in EDITABLE_RECORDS:
        copy_file(record_root / name, target / name)

    for name in CP1_ARTIFACTS:
        relative = f"prior-checkpoint/{name}"
        copy_file(cp1_path(cp1, name), target / relative)
        immutable[relative] = ("Checkpoint 1", "0.1.0")

    units = (
        (m04, M04_ARTIFACTS, "modules/04-validity-adjustment-longitudinal", "Module 04", "0.1.0"),
        (m05, M05_ARTIFACTS, "modules/05-forecasting-temporal-validation", "Module 05", "0.1.0"),
        (m06, M06_ARTIFACTS, "modules/06-agent-assisted-modeling-testing", "Module 06", "0.1.0"),
        (public, PUBLIC_ARTIFACTS, "public-data", "CDC NHSN public release", "2026-08-29"),
    )
    for root, names, namespace, source, version in units:
        for name in names:
            relative = f"{namespace}/{name}"
            copy_file(root / name, target / relative)
            immutable[relative] = (source, version)

    manifest = target / "release-manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("relative_path", "source_unit", "source_version", "bytes", "sha256"))
        for relative in sorted(immutable):
            path = target / relative
            source, version = immutable[relative]
            writer.writerow((relative, source, version, path.stat().st_size, sha256(path)))

    file_count = sum(path.is_file() for path in target.rglob("*"))
    if len(immutable) != 117 or file_count != 130:
        raise ValueError(f"Checkpoint file contract changed: {len(immutable)} manifest rows and {file_count} files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "upstream_artifacts": 111, "manifest_rows": len(immutable),
        "manifest_bytes": manifest.stat().st_size, "manifest_sha256": sha256(manifest),
        "assembled_files": file_count,
    }


def self_check() -> None:
    roots = (REFERENCE_CP1, REFERENCE_M04, REFERENCE_M05, REFERENCE_M06, REFERENCE_PUBLIC)
    with tempfile.TemporaryDirectory(prefix="fnd2-checkpoint2-assemble-") as temp_dir:
        base = Path(temp_dir)
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        report = assemble(first, roots, reference=True)
        second_report = assemble(second, roots, reference=True)
        learner_report = assemble(learner, roots, reference=False)
        assert report["manifest_rows"] == 117 and report["assembled_files"] == 130
        assert report["manifest_sha256"] == second_report["manifest_sha256"]
        assert learner_report["mode"] == "learner"
        assert (first / "public-data" / PUBLIC_ARTIFACTS[0]).is_file()
        try:
            assemble(first, roots, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not refuse an existing target")
    print("FND-2 Checkpoint 2 assembler self-check passed: 111 upstream artifacts, 117 manifest rows, and 130 assembled files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--checkpoint1", type=Path)
    parser.add_argument("--module04", type=Path)
    parser.add_argument("--module05", type=Path)
    parser.add_argument("--module06", type=Path)
    parser.add_argument("--public-data", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.target is None:
        parser.error("target is required unless --self-check is used")
    if args.reference:
        roots = (REFERENCE_CP1, REFERENCE_M04, REFERENCE_M05, REFERENCE_M06, REFERENCE_PUBLIC)
    else:
        supplied = (args.checkpoint1, args.module04, args.module05, args.module06, args.public_data)
        if not all(supplied):
            parser.error("learner assembly requires --checkpoint1, --module04, --module05, --module06, and --public-data")
        roots = tuple(path.resolve() for path in supplied)
    print(json.dumps(assemble(args.target.resolve(), roots, args.reference), indent=2))


if __name__ == "__main__":
    main()

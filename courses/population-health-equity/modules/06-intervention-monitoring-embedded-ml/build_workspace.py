"""Build an APP-5 Module 06 learner or reference workspace."""

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
    ".gitattributes", "VERSION", "requirements.txt", "README.md", "assessment.md", "instructor-notes.md",
    "data-spec.md", "intervention-contract.json", "release.json", "source-record.yml", "freeze_upstream.py",
    "generate_monitoring_fixture.py", "build_intervention_monitoring.py", "build_workspace.py", "validate_workspace.py",
)
DATA_FILES = (
    "data/data-dictionary.csv", "data/intervention-contract.csv", "data/monitoring-measures.csv",
    "data/cluster-feature-contract.csv", "data/challenger-variants.csv",
    "data/raw/fictional-monitoring-dry-run.csv.gz", "data/synthetic-source-manifest.csv",
)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in (
    "source-profile.csv", "intervention-readiness.csv", "dry-run-reconciliation.csv", "monitoring-results.csv",
    "escalation-results.csv", "feedback-recourse-results.csv", "cluster-feature-matrix.csv.gz",
    "cluster-assignments.csv.gz", "cluster-profiles.csv", "cluster-support-geography.csv",
    "selected-tract-cluster-review.csv", "challenger-stability.csv", "query-checks.csv", "build-report.json",
))
SQL_FILES = tuple(f"sql/{name}" for name in (
    "01-reconcile-handoff-and-dry-run.sql", "02-monitor-intervention-and-recourse.sql",
    "03-audit-cluster-challenger.sql", "04-audit-gates-points-and-authority.sql",
))
RECORD_FILES = (
    "intervention-and-authority-contract.md", "theory-of-change.csv", "delivery-pathway.csv",
    "population-access-capacity-plan.md", "implementation-measure-registry.csv", "monitoring-plan.csv",
    "readiness-capacity-review.csv", "dry-run-interpretation.md", "benefit-harm-balancing-register.csv",
    "feedback-recourse-plan.md", "incident-escalation-register.csv", "pause-stop-revision-retirement.md",
    "evaluation-proposal.md", "cluster-model-card.md", "cluster-stability-support-review.md",
    "tailoring-questions.md", "responsible-claims-audit.csv", "week6-gate-results.csv",
    "progression-decision.md", "reproducibility-check.md", "ai-use.md",
)
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
EXPECTED_LEARNER_FILES = 389
EXPECTED_LEARNER_MANIFEST_ROWS = 363
EXPECTED_REFERENCE_FILES = 403
EXPECTED_REFERENCE_MANIFEST_ROWS = 377


def upstream_files(root: Path = ROOT) -> tuple[str, ...]:
    manifest = root / "upstream/module05-handoff-manifest.csv"
    if not manifest.is_file():
        return ("upstream/module05-handoff-manifest.csv",)
    with manifest.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return ("upstream/module05-handoff-manifest.csv",) + tuple(f"upstream/{row['relative_path']}" for row in rows)


UPSTREAM_FILES = upstream_files()


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
    source_records = ROOT / ("reference" if reference else "template")
    immutable = CONTROL_FILES + DATA_FILES + UPSTREAM_FILES + (OUTPUT_FILES if reference else ())
    required = list(immutable) + [f"{source_records.name}/{relative}" for relative in SQL_FILES + RECORD_FILES]
    missing = [relative for relative in required if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    manifest = []
    for relative in immutable:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        role = (
            "reference analysis output" if relative.startswith("outputs/")
            else "fictional source and declared monitoring or model input" if relative.startswith("data/")
            else "accepted Module 05 handoff" if relative.startswith("upstream/")
            else "immutable module control"
        )
        manifest.append({"relative_path": relative, "bytes": destination.stat().st_size, "sha256": sha256(destination), "role": role})
    for relative in SQL_FILES + RECORD_FILES:
        copy(source_records / relative, target, relative)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    release_manifest = target / "release-manifest.csv"
    with release_manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    expected_files = EXPECTED_REFERENCE_FILES if reference else EXPECTED_LEARNER_FILES
    expected_manifest = EXPECTED_REFERENCE_MANIFEST_ROWS if reference else EXPECTED_LEARNER_MANIFEST_ROWS
    if files != expected_files or len(manifest) != expected_manifest:
        raise ValueError(f"Workspace contract changed: {files} files and {len(manifest)} manifest rows")
    return {
        "status": "pass", "mode": "reference" if reference else "learner", "assembled_files": files,
        "manifest_rows": len(manifest), "manifest_bytes": release_manifest.stat().st_size,
        "manifest_sha256": sha256(release_manifest),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module06-workspace-") as temporary:
        base = Path(temporary)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        learner = assemble(base / "learner")
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert learner["assembled_files"] == EXPECTED_LEARNER_FILES
        assert "REPLACE" in (base / "learner/cluster-model-card.md").read_text(encoding="utf-8")
        assert "REPLACE" not in (base / "reference-1/cluster-model-card.md").read_text(encoding="utf-8")
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print(f"APP-5 Module 06 workspace-builder self-check passed: {EXPECTED_LEARNER_FILES} learner files and {EXPECTED_REFERENCE_FILES} reference files.")


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
            print(json.dumps(assemble(args.target, reference=args.reference), indent=2, sort_keys=True))
        else:
            parser.error("--target is required unless --self-check is used")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Workspace build failed: {error}\n")


if __name__ == "__main__":
    main()

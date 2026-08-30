"""Assemble the FND-1 Week 3 checkpoint from accepted module evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import shutil
import sqlite3
import tempfile
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parents[3]
TEMPLATE = PACKAGE_ROOT / "template"
REFERENCE = PACKAGE_ROOT / "reference"
ASSETS = PACKAGE_ROOT / "assets"
M1_RELEASE = REPO_ROOT / "courses" / "healthcare-data-foundations" / "modules" / "01-reproducible-workspace"
M2_RELEASE = REPO_ROOT / "courses" / "healthcare-data-foundations" / "modules" / "02-databases-retrieval"
M3_RELEASE = REPO_ROOT / "courses" / "healthcare-data-foundations" / "modules" / "03-cohorts-analytic-tables"
FIRST_EXTRACTS = (
    "table-inventory.csv",
    "encounter-class-counts.csv",
    "observation-linkage.csv",
    "selected-patient-timeline.csv",
    "numeric-observation-sample.csv",
)
M3_OUTPUTS = (
    "eligible-events.csv",
    "index-cohort.csv",
    "cohort-flow.csv",
    "analytic-table.csv",
    "query-checks.csv",
)
CUMULATIVE_RECORDS = (
    "README.md",
    "transformation-record.md",
    "reproducibility-check.md",
    "ai-use.md",
    "component-score.csv",
    "review-disposition.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def csv_rows(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.reader(handle)) - 1


def require_files(root: Path, names: tuple[str, ...], label: str) -> None:
    missing = [name for name in names if not (root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"{label} is missing: {', '.join(missing)}")


def copy(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def write_reference_database_dictionary(target: Path) -> None:
    """Reuse the Module 02 schema and field policy to emit its 177-row dictionary."""
    module_path = M2_RELEASE / "build_database.py"
    spec = importlib.util.spec_from_file_location("fnd1_module02_builder", module_path)
    if not spec or not spec.loader:
        raise ImportError(f"Cannot load Module 02 builder: {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    connection = sqlite3.connect(":memory:")
    try:
        connection.executescript((M2_RELEASE / "schema.sql").read_text(encoding="utf-8"))
        rows = []
        for table in module.LOAD_ORDER:
            columns = module.sql_columns(connection, table)
            has_surrogate = columns[0][0] == "source_row_number"
            for position, (name, sql_type, not_null) in enumerate(columns, start=1):
                source_name = "generated" if name == "source_row_number" else ("Id" if name == "id" else name.upper())
                rows.append({
                    "table_name": table,
                    "database_position": position,
                    "source_field": source_name,
                    "database_field": name,
                    "sqlite_type": sql_type,
                    "required": "yes" if not_null else "no",
                    "identity_like": "yes" if name in module.IDENTITY_LIKE_FIELDS else "no",
                    "cost_or_coverage": "yes" if name in module.COST_FIELDS else "no",
                    "included_in_core_view": "yes" if name in module.CORE_VIEW_FIELDS.get(table, set()) else "no",
                    "description": "Generated stable source-row ordinal." if has_surrogate and name == "source_row_number" else "Synthea source field; use the official CSV data dictionary for domain definition.",
                })
    finally:
        connection.close()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def assemble(
    target: Path,
    module01: Path | None = None,
    module02: Path | None = None,
    module03: Path | None = None,
    reference: bool = False,
) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if reference:
        m1, m2, m3 = M1_RELEASE, M2_RELEASE, M3_RELEASE
        first_extract_root = REFERENCE / "first-extracts"
    else:
        if not module01 or not module02 or not module03:
            raise ValueError("Learner assembly requires Module 01, 02, and 03 paths.")
        m1, m2, m3 = module01, module02, module03
        first_extract_root = m2 / "outputs"

    m1_required = (
        "requirements.txt", "environment-note.md", "version-policy.md",
        "ai-use.md", "reproducibility-check.md",
    )
    m2_required = (
        "data-model.mmd", "schema-description.md", "data-dictionary.csv", "source-manifest.csv",
        "schema.sql", "fhir-json-reading.md", "source-record.yml", "sql/01-first-extracts.sql",
    ) + tuple(f"outputs/{name}" for name in FIRST_EXTRACTS)
    m3_required = (
        "cohort-spec.md", "table-spec.md", "data-dictionary.csv", "source-record.yml",
        "ai-use.md", "reproducibility-check.md", "sql/02-index-cohort.sql",
        "sql/03-analytic-table.sql", "sql/04-validation.sql",
    ) + tuple(f"outputs/{name}" for name in M3_OUTPUTS)

    if reference:
        require_files(m1 / "template", m1_required[:5], "Reference Module 01 records")
        require_files(m2, ("source-manifest.csv", "schema.sql", "source-record.yml", "reference-first-extracts.sql"), "Reference Module 02 release")
        require_files(REFERENCE, ("data-model.mmd", "schema-description.md", "fhir-json-reading.md") + CUMULATIVE_RECORDS + ("environment-note.md", "version-policy.md", "source-system-comparison.md"), "Checkpoint reference records")
        require_files(first_extract_root, FIRST_EXTRACTS, "Reference first extracts")
        require_files(m3, m3_required, "Reference Module 03 release")
        require_files(REFERENCE / "evidence", (
            "module-01-ai-use.md", "module-01-reproducibility-check.md", "module-02-ai-use.md",
            "module-02-validation-notes.md", "module-03-ai-use.md", "module-03-reproducibility-check.md",
        ), "Reference module evidence")
    else:
        require_files(m1, m1_required, "Accepted Module 01 workspace")
        require_files(m2, m2_required, "Accepted Module 02 workspace")
        require_files(m3, m3_required, "Accepted Module 03 submission")
        require_files(TEMPLATE, CUMULATIVE_RECORDS + ("source-system-comparison.md", ".gitattributes"), "Checkpoint templates")

    target.mkdir(parents=True)
    immutable: dict[str, tuple[str, str]] = {}

    def add(source: Path, relative: str, unit: str, version: str, locked: bool = True) -> None:
        copy(source, target / relative)
        if locked:
            immutable[relative] = (unit, version)

    add(TEMPLATE / ".gitattributes", ".gitattributes", "Checkpoint 1", "0.1.0")
    (target / "VERSION").write_text("0.1.0\n", encoding="utf-8")
    immutable["VERSION"] = ("Checkpoint 1", "0.1.0")

    if reference:
        for name in CUMULATIVE_RECORDS:
            add(REFERENCE / name, name, "Checkpoint 1 reference", "0.1.0", locked=False)
        add(REFERENCE / "environment-note.md", "environment-note.md", "Module 01 reference", "0.1.0", locked=False)
        add(REFERENCE / "version-policy.md", "version-policy.md", "Module 01 reference", "0.1.0", locked=False)
        add(M1_RELEASE / "template" / "requirements.txt", "requirements.txt", "Module 01", "0.1.0")
        add(REFERENCE / "data-model.mmd", "schema/data-model.mmd", "Module 02 reference", "0.1.0")
        add(REFERENCE / "schema-description.md", "schema/schema-description.md", "Module 02 reference", "0.1.0")
        add(REFERENCE / "source-system-comparison.md", "schema/source-system-comparison.md", "Checkpoint 1 reference", "0.1.0", locked=False)
        add(REFERENCE / "fhir-json-reading.md", "schema/fhir-json-reading.md", "Module 02 reference", "0.1.0")
        add(M2_RELEASE / "reference-first-extracts.sql", "sql/01-first-extracts.sql", "Module 02", "0.1.0")
        evidence_root = REFERENCE / "evidence"
    else:
        for name in CUMULATIVE_RECORDS:
            add(TEMPLATE / name, name, "Checkpoint 1 template", "0.1.0", locked=False)
        add(m1 / "environment-note.md", "environment-note.md", "Module 01", "0.1.0", locked=False)
        add(m1 / "version-policy.md", "version-policy.md", "Module 01", "0.1.0", locked=False)
        add(m1 / "requirements.txt", "requirements.txt", "Module 01", "0.1.0")
        add(m2 / "data-model.mmd", "schema/data-model.mmd", "Module 02", "0.1.0")
        add(m2 / "schema-description.md", "schema/schema-description.md", "Module 02", "0.1.0")
        add(TEMPLATE / "source-system-comparison.md", "schema/source-system-comparison.md", "Checkpoint 1 template", "0.1.0", locked=False)
        add(m2 / "fhir-json-reading.md", "schema/fhir-json-reading.md", "Module 02", "0.1.0")
        add(m2 / "sql" / "01-first-extracts.sql", "sql/01-first-extracts.sql", "Module 02", "0.1.0")
        evidence_root = None

    add(ASSETS / "schema-diagram.svg", "schema/schema-diagram.svg", "Checkpoint 1", "0.1.0")
    if reference:
        dictionary_path = target / "schema" / "data-dictionary.csv"
        write_reference_database_dictionary(dictionary_path)
        immutable["schema/data-dictionary.csv"] = ("Module 02", "0.1.0")
    else:
        add(m2 / "data-dictionary.csv", "schema/data-dictionary.csv", "Module 02", "0.1.0")
    add(m3 / "data-dictionary.csv", "schema/analytic-data-dictionary.csv", "Module 03", "0.1.0")
    add(m2 / "source-manifest.csv", "schema/source-manifest.csv", "Module 02", "0.1.0")
    add(m2 / "schema.sql", "schema/schema.sql", "Module 02", "0.1.0")
    add(m3 / "cohort-spec.md", "cohort-spec.md", "Module 03", "0.1.0")
    add(m3 / "table-spec.md", "table-spec.md", "Module 03", "0.1.0")
    add(m3 / "source-record.yml", "source-record.yml", "Module 03", "0.1.0")
    for name in ("02-index-cohort.sql", "03-analytic-table.sql", "04-validation.sql"):
        add(m3 / "sql" / name, f"sql/{name}", "Module 03", "0.1.0")
    for name in M3_OUTPUTS:
        add(m3 / "outputs" / name, f"outputs/{name}", "Module 03", "0.1.0")
    for name in FIRST_EXTRACTS:
        add(first_extract_root / name, f"outputs/first-extracts/{name}", "Module 02", "0.1.0")

    evidence_sources = {
        "module-01-ai-use.md": evidence_root / "module-01-ai-use.md" if reference else m1 / "ai-use.md",
        "module-01-reproducibility-check.md": evidence_root / "module-01-reproducibility-check.md" if reference else m1 / "reproducibility-check.md",
        "module-02-ai-use.md": evidence_root / "module-02-ai-use.md" if reference else m2 / "ai-use.md",
        "module-02-validation-notes.md": evidence_root / "module-02-validation-notes.md" if reference else m2 / "validation-notes.md",
        "module-03-ai-use.md": evidence_root / "module-03-ai-use.md" if reference else m3 / "ai-use.md",
        "module-03-reproducibility-check.md": evidence_root / "module-03-reproducibility-check.md" if reference else m3 / "reproducibility-check.md",
    }
    for name, source in evidence_sources.items():
        unit = f"Module {name[7:9]}"
        add(source, f"evidence/{name}", unit, "0.1.0")

    registry_path = target / "outputs" / "first-extracts.csv"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with registry_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("output_name", "row_count", "bytes", "sha256"))
        for name in sorted(FIRST_EXTRACTS):
            path = target / "outputs" / "first-extracts" / name
            writer.writerow((name, csv_rows(path), path.stat().st_size, sha256(path)))
    immutable["outputs/first-extracts.csv"] = ("Checkpoint 1", "0.1.0")

    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("relative_path", "source_unit", "source_version", "bytes", "sha256"))
        for relative in sorted(immutable):
            path = target / relative
            unit, version = immutable[relative]
            writer.writerow((relative, unit, version, path.stat().st_size, sha256(path)))

    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(immutable),
        "first_extracts": len(FIRST_EXTRACTS),
        "cohort_outputs": len(M3_OUTPUTS),
        "target": str(target),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-checkpoint1-assemble-") as temp_dir:
        target = Path(temp_dir) / "checkpoint-1"
        report = assemble(target, reference=True)
        assert report["manifest_rows"] > 25
        assert (target / "outputs" / "analytic-table.csv").is_file()
        try:
            assemble(target, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not protect an existing target.")
    print("FND-1 Checkpoint 1 assembler self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module01", type=Path)
    parser.add_argument("--module02", type=Path)
    parser.add_argument("--module03", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.target:
        parser.error("--target is required")
    if args.reference and any((args.module01, args.module02, args.module03)):
        parser.error("--reference cannot be combined with module paths")
    if not args.reference and not all((args.module01, args.module02, args.module03)):
        parser.error("learner assembly requires --module01, --module02, and --module03")
    try:
        report = assemble(
            args.target.resolve(),
            args.module01.resolve() if args.module01 else None,
            args.module02.resolve() if args.module02 else None,
            args.module03.resolve() if args.module03 else None,
            args.reference,
        )
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Assembly failed: {exc}\n")
    print(
        f"FND-1 Checkpoint 1 {report['mode']} assembly passed: "
        f"{report['manifest_rows']} immutable files registered."
    )


if __name__ == "__main__":
    main()

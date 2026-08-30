"""Build the FND-1 Module 02 SQLite teaching database from the pinned Synthea archive."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import shutil
import sqlite3
import sys
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
TEMPLATE = MODULE_ROOT / "template"
SCHEMA = MODULE_ROOT / "schema.sql"
MANIFEST = MODULE_ROOT / "source-manifest.csv"
QUERY_RUNNER = MODULE_ROOT / "run_queries.py"
SOURCE_URL = "https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip"
EXPECTED_ARCHIVE_BYTES = 8_982_431
EXPECTED_ARCHIVE_SHA256 = "4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a"
LOAD_ORDER = (
    "patients",
    "organizations",
    "providers",
    "payers",
    "encounters",
    "allergies",
    "careplans",
    "conditions",
    "devices",
    "imaging_studies",
    "immunizations",
    "medications",
    "observations",
    "payer_transitions",
    "procedures",
    "supplies",
)
IDENTITY_LIKE_FIELDS = {
    "ssn", "drivers", "passport", "prefix", "first", "last", "suffix", "maiden",
    "birthplace", "address", "city", "zip", "lat", "lon", "name", "phone", "udi",
}
COST_FIELDS = {
    "healthcare_expenses", "healthcare_coverage", "revenue", "amount_covered",
    "amount_uncovered", "base_encounter_cost", "total_claim_cost", "payer_coverage",
    "base_cost", "totalcost",
}
CORE_VIEW_FIELDS = {
    "patients": {"id", "birthdate", "deathdate", "marital", "race", "ethnicity", "gender", "state", "county"},
    "encounters": {"id", "start", "stop", "patient", "encounterclass", "code", "description", "reasoncode", "reasondescription"},
    "observations": {"source_row_number", "date", "patient", "encounter", "code", "description", "value", "units", "type"},
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_manifest() -> list[dict[str, str]]:
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if [row["table_name"] for row in rows] != sorted(LOAD_ORDER):
        raise ValueError("Source manifest must contain the 16 source tables in sorted order.")
    return rows


def sql_columns(connection: sqlite3.Connection, table: str) -> list[tuple[str, str, int]]:
    return [(row[1], row[2], row[3]) for row in connection.execute(f'PRAGMA table_info("{table}")')]


def convert(value: str, sql_type: str) -> object:
    if value == "":
        return None
    if sql_type == "INTEGER":
        return int(value)
    if sql_type == "REAL":
        return float(value)
    return value


def validate_archive(archive_path: Path, manifest: list[dict[str, str]]) -> None:
    if archive_path.stat().st_size != EXPECTED_ARCHIVE_BYTES:
        raise ValueError(f"Unexpected archive size: {archive_path.stat().st_size}")
    digest = sha256(archive_path)
    if digest != EXPECTED_ARCHIVE_SHA256:
        raise ValueError(f"Unexpected archive SHA-256: {digest}")
    with zipfile.ZipFile(archive_path) as archive:
        names = {item.filename for item in archive.infolist() if not item.is_dir()}
        expected = {row["archive_path"] for row in manifest}
        if names != expected:
            raise ValueError(f"Archive members changed: expected {sorted(expected)}, found {sorted(names)}")
        for row in manifest:
            info = archive.getinfo(row["archive_path"])
            if info.file_size != int(row["source_bytes"]):
                raise ValueError(f"Source byte count changed for {row['table_name']}.")
            digest = hashlib.sha256(archive.read(row["archive_path"])).hexdigest()
            if digest != row["source_sha256"]:
                raise ValueError(f"Source fingerprint changed for {row['table_name']}.")


def load_table(
    connection: sqlite3.Connection,
    archive: zipfile.ZipFile,
    manifest_row: dict[str, str],
) -> list[dict[str, object]]:
    table = manifest_row["table_name"]
    columns = sql_columns(connection, table)
    has_surrogate = columns[0][0] == "source_row_number"
    source_columns = columns[1:] if has_surrogate else columns
    expected_header = [name.upper() if name != "id" else "Id" for name, _, _ in source_columns]

    dictionary_rows: list[dict[str, object]] = []
    with archive.open(manifest_row["archive_path"]) as raw:
        text = (line.decode("utf-8-sig") for line in raw)
        reader = csv.DictReader(text)
        if reader.fieldnames != expected_header:
            raise ValueError(f"Header changed for {table}: {reader.fieldnames}")
        placeholders = ", ".join("?" for _ in columns)
        names = ", ".join(f'"{name}"' for name, _, _ in columns)
        statement = f'INSERT INTO "{table}" ({names}) VALUES ({placeholders})'
        batch: list[tuple[object, ...]] = []
        count = 0
        for count, row in enumerate(reader, start=1):
            values = [convert(row[source_name], sql_type) for source_name, (_, sql_type, _) in zip(expected_header, source_columns, strict=True)]
            if has_surrogate:
                values.insert(0, count)
            batch.append(tuple(values))
            if len(batch) == 5000:
                connection.executemany(statement, batch)
                batch.clear()
        if batch:
            connection.executemany(statement, batch)
    if count != int(manifest_row["source_rows"]):
        raise ValueError(f"Row count changed for {table}: {count}")

    for position, (name, sql_type, not_null) in enumerate(columns, start=1):
        source_name = "generated" if name == "source_row_number" else expected_header[position - 2 if has_surrogate else position - 1]
        dictionary_rows.append(
            {
                "table_name": table,
                "database_position": position,
                "source_field": source_name,
                "database_field": name,
                "sqlite_type": sql_type,
                "required": "yes" if not_null else "no",
                "identity_like": "yes" if name in IDENTITY_LIKE_FIELDS else "no",
                "cost_or_coverage": "yes" if name in COST_FIELDS else "no",
                "included_in_core_view": "yes" if name in CORE_VIEW_FIELDS.get(table, set()) else "no",
                "description": "Generated stable source-row ordinal." if name == "source_row_number" else "Synthea source field; use the official CSV data dictionary for domain definition.",
            }
        )
    return dictionary_rows


def write_dictionary(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_fhir_examples(connection: sqlite3.Connection, root: Path) -> dict[str, str]:
    row = connection.execute(
        """
        SELECT p.id, p.birthdate, p.deathdate, p.gender,
               e.id, e.start, e.stop, e.encounterclass, e.code, e.description,
               o.source_row_number, o.date, o.code, o.description, o.value, o.units
        FROM observations o
        JOIN encounters e ON e.id = o.encounter
        JOIN patients p ON p.id = o.patient
        WHERE o.type = 'numeric' AND o.units IS NOT NULL AND o.value IS NOT NULL
        ORDER BY p.id, o.date, o.code, o.source_row_number
        LIMIT 1
        """
    ).fetchone()
    if row is None:
        raise ValueError("No linked numeric observation is available for the FHIR reading example.")
    patient_id, birthdate, deathdate, gender, encounter_id, start, stop, encounter_class, encounter_code, encounter_description, observation_row, observation_date, observation_code, observation_description, value, units = row
    fhir_dir = root / "fhir"
    fhir_dir.mkdir()
    patient = {
        "resourceType": "Patient",
        "id": patient_id,
        "gender": {"M": "male", "F": "female"}.get(gender, "unknown"),
        "birthDate": birthdate,
    }
    if deathdate:
        patient["deceasedDateTime"] = deathdate
    class_code = {
        "ambulatory": "AMB", "outpatient": "AMB", "wellness": "AMB",
        "emergency": "EMER", "inpatient": "IMP", "urgentcare": "ACUTE",
    }[encounter_class]
    encounter = {
        "resourceType": "Encounter",
        "id": encounter_id,
        "status": "finished",
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode", "code": class_code, "display": encounter_class},
        "type": [{"coding": [{"system": "http://snomed.info/sct", "code": encounter_code, "display": encounter_description}]}],
        "subject": {"reference": f"Patient/{patient_id}"},
        "period": {"start": start, "end": stop},
    }
    observation_id = f"synthea-observation-{observation_row}"
    observation = {
        "resourceType": "Observation",
        "id": observation_id,
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": observation_code, "display": observation_description}]},
        "subject": {"reference": f"Patient/{patient_id}"},
        "encounter": {"reference": f"Encounter/{encounter_id}"},
        "effectiveDateTime": observation_date,
        "valueQuantity": {"value": float(value), "unit": units},
    }
    resources = {"patient.json": patient, "encounter.json": encounter, "observation.json": observation}
    for filename, resource in resources.items():
        (fhir_dir / filename).write_text(json.dumps(resource, indent=2) + "\n", encoding="utf-8")
    return {name: resource["id"] for name, resource in resources.items()}


def build(archive_path: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    manifest = read_manifest()
    validate_archive(archive_path, manifest)
    shutil.copytree(TEMPLATE, target)
    shutil.copy2(SCHEMA, target / "schema.sql")
    shutil.copy2(MANIFEST, target / "source-manifest.csv")
    shutil.copy2(QUERY_RUNNER, target / "run_queries.py")
    data_dir = target / "data"
    data_dir.mkdir()
    database = data_dir / "fnd1_synthea_apr2020.sqlite"
    connection = sqlite3.connect(database)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = OFF")
    connection.execute("PRAGMA synchronous = OFF")
    connection.executescript(SCHEMA.read_text(encoding="utf-8"))
    dictionary_rows: list[dict[str, object]] = []
    with zipfile.ZipFile(archive_path) as archive:
        for table in LOAD_ORDER:
            manifest_row = next(row for row in manifest if row["table_name"] == table)
            dictionary_rows.extend(load_table(connection, archive, manifest_row))
            connection.commit()
    connection.executemany(
        "INSERT INTO source_table_manifest VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["table_name"], row["archive_path"], int(row["source_bytes"]),
                int(row["source_rows"]), int(row["source_columns"]), row["source_sha256"],
            )
            for row in manifest
        ],
    )
    connection.execute("PRAGMA user_version = 1")
    connection.commit()
    fhir_ids = write_fhir_examples(connection, target)
    connection.execute("ANALYZE")
    connection.commit()
    table_counts = {table: connection.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0] for table in LOAD_ORDER}
    foreign_key_failures = len(connection.execute("PRAGMA foreign_key_check").fetchall())
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    connection.close()
    write_dictionary(target / "data-dictionary.csv", dictionary_rows)
    report = {
        "status": "pass" if integrity == "ok" and foreign_key_failures == 0 else "fail",
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {"url": SOURCE_URL, "bytes": EXPECTED_ARCHIVE_BYTES, "sha256": EXPECTED_ARCHIVE_SHA256},
        "database": {"path": "data/fnd1_synthea_apr2020.sqlite", "bytes": database.stat().st_size, "sha256": sha256(database), "sqlite": sqlite3.sqlite_version},
        "tables": table_counts,
        "total_source_rows": sum(table_counts.values()),
        "foreign_key_failures": foreign_key_failures,
        "integrity_check": integrity,
        "data_dictionary_rows": len(dictionary_rows),
        "fhir_example_ids": fhir_ids,
        "environment": {"python": sys.version.split()[0], "platform": platform.platform()},
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def self_check() -> None:
    manifest = read_manifest()
    assert len(manifest) == 16
    assert sum(int(row["source_rows"]) for row in manifest) == 471_836
    assert convert("", "TEXT") is None
    assert convert("7", "INTEGER") == 7
    assert convert("3.5", "REAL") == 3.5
    with tempfile.TemporaryDirectory(prefix="fnd1-module02-build-") as temp_dir:
        target = Path(temp_dir)
        try:
            build(Path("missing.zip"), target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target.")
    print("FND-1 Module 02 builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-zip", type=Path, help="Pinned Synthea April 2020 CSV archive")
    parser.add_argument("--download", action="store_true", help="Download the pinned archive into the new target")
    parser.add_argument("--target", type=Path, help="New learner database workspace")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.target is None:
        parser.error("--target is required")
    if bool(args.source_zip) == bool(args.download):
        parser.error("choose exactly one of --source-zip or --download")
    target = args.target.resolve()
    if target.exists():
        parser.exit(1, f"Build failed: refusing to overwrite existing target: {target}\n")
    if args.download:
        target.mkdir(parents=True)
        archive_path = target / "source-cache" / "synthea_sample_data_csv_apr2020.zip"
        archive_path.parent.mkdir()
        print(f"Downloading {SOURCE_URL}")
        urllib.request.urlretrieve(SOURCE_URL, archive_path)
        staging = target.with_name(target.name + "-build")
        try:
            report = build(archive_path, staging)
            for item in staging.iterdir():
                shutil.move(str(item), target / item.name)
            staging.rmdir()
        except Exception as exc:
            parser.exit(1, f"Build failed; partial target retained for inspection: {exc}\n")
    else:
        try:
            report = build(args.source_zip.resolve(), target)
        except Exception as exc:
            parser.exit(1, f"Build failed: {exc}\n")
    print(f"FND-1 Module 02 database build passed: {report['total_source_rows']} rows across 16 source tables.")


if __name__ == "__main__":
    main()

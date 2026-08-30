#!/usr/bin/env python3
"""Build the DA-730 Module 11 synthetic care-transition releases."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
DATA_ROOT = MODULE_ROOT / "data"
SOURCE_URL = "https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip"
EXPECTED_ZIP_SHA256 = "4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a"
OBSERVATION_START = datetime(2015, 1, 1, tzinfo=timezone.utc)
INDEX_END = datetime(2019, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
ACUTE_CLASSES = {"emergency", "inpatient"}

PATIENT_OUTPUT = DATA_ROOT / "synthea_patients_transition_source_2020.csv"
ENCOUNTER_OUTPUT = DATA_ROOT / "synthea_encounters_transition_source_2020.csv"
COHORT_OUTPUT = DATA_ROOT / "synthea_acute_transition_cohort_2020.csv"
EDGE_OUTPUT = DATA_ROOT / "synthea_transition_edges_2020.csv"

PATIENT_FIELDS = ("patient_id", "birth_date", "death_date", "sex", "race", "ethnicity")
ENCOUNTER_FIELDS = (
    "encounter_id",
    "start",
    "stop",
    "patient_id",
    "encounter_class",
    "code",
    "description",
    "reason_code",
    "reason_description",
)
COHORT_FIELDS = (
    "patient_id",
    "birth_date",
    "death_date",
    "age_at_index",
    "sex",
    "race",
    "ethnicity",
    "index_encounter_id",
    "index_start",
    "index_stop",
    "index_class",
    "next_30d_state",
    "next_30d_encounter_id",
    "next_30d_start",
    "next_30d_days_after_index_stop",
    "acute_return_90d",
    "death_90d",
    "endpoint_90d",
    "transition_path",
    "path_count",
    "path_denominator",
    "path_acute_return_count",
    "path_acute_return_pct",
    "cohort_acute_return_pct",
    "priority_screen",
)
EDGE_FIELDS = (
    "stage_from",
    "node_from",
    "stage_to",
    "node_to",
    "patient_count",
    "cohort_denominator",
    "cohort_pct",
    "node_from_denominator",
    "node_from_pct",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def age_on(birth_date: str, when: datetime) -> int:
    born = date.fromisoformat(birth_date)
    return when.year - born.year - ((when.month, when.day) < (born.month, born.day))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_zip_csv(archive: zipfile.ZipFile, name: str) -> list[dict[str, str]]:
    with archive.open(name) as raw:
        return list(csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline="")))


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def select_source(zip_path: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    digest = sha256(zip_path)
    if digest != EXPECTED_ZIP_SHA256:
        raise ValueError(f"Unexpected Synthea ZIP SHA-256: {digest}")
    with zipfile.ZipFile(zip_path) as archive:
        patients_raw = read_zip_csv(archive, "csv/patients.csv")
        encounters_raw = read_zip_csv(archive, "csv/encounters.csv")
    patients = [
        {
            "patient_id": row["Id"],
            "birth_date": row["BIRTHDATE"],
            "death_date": row["DEATHDATE"],
            "sex": row["GENDER"],
            "race": row["RACE"],
            "ethnicity": row["ETHNICITY"],
        }
        for row in patients_raw
    ]
    encounters = [
        {
            "encounter_id": row["Id"],
            "start": row["START"],
            "stop": row["STOP"],
            "patient_id": row["PATIENT"],
            "encounter_class": row["ENCOUNTERCLASS"],
            "code": row["CODE"],
            "description": row["DESCRIPTION"],
            "reason_code": row["REASONCODE"],
            "reason_description": row["REASONDESCRIPTION"],
        }
        for row in encounters_raw
    ]
    patients.sort(key=lambda row: row["patient_id"])
    encounters.sort(key=lambda row: (row["patient_id"], row["start"], row["encounter_id"]))
    return patients, encounters


def next_state(encounter_class: str) -> str:
    if encounter_class in {"ambulatory", "outpatient", "wellness"}:
        return "Scheduled care"
    if encounter_class == "urgentcare":
        return "Urgent care"
    if encounter_class in ACUTE_CLASSES:
        return "Acute return"
    raise ValueError(f"Unmapped encounter class: {encounter_class}")


def build_cohort(
    patients: list[dict[str, str]], encounters: list[dict[str, str]]
) -> list[dict[str, object]]:
    patients_by_id = {row["patient_id"]: row for row in patients}
    encounters_by_patient: dict[str, list[tuple[datetime, datetime, dict[str, str]]]] = defaultdict(list)
    for row in encounters:
        if row["patient_id"] not in patients_by_id:
            raise ValueError(f"Encounter has unknown patient: {row['patient_id']}")
        start = parse_datetime(row["start"])
        stop = parse_datetime(row["stop"])
        if stop < start:
            raise ValueError(f"Encounter stops before it starts: {row['encounter_id']}")
        encounters_by_patient[row["patient_id"]].append((start, stop, row))

    cohort: list[dict[str, object]] = []
    for patient_id, timeline in encounters_by_patient.items():
        patient = patients_by_id[patient_id]
        timeline.sort(key=lambda item: (item[0], item[2]["encounter_id"]))
        eligible = [
            item
            for item in timeline
            if item[2]["encounter_class"] in ACUTE_CLASSES
            and OBSERVATION_START <= item[0] <= INDEX_END
            and age_on(patient["birth_date"], item[0]) >= 18
        ]
        if not eligible:
            continue
        index_start, index_stop, index = eligible[0]
        window_30 = index_stop + timedelta(days=30)
        window_90 = index_stop + timedelta(days=90)
        following = [item for item in timeline if item[2]["encounter_id"] != index["encounter_id"] and item[0] > index_stop]
        within_30 = [item for item in following if item[0] <= window_30]
        first_next = within_30[0] if within_30 else None
        state = next_state(first_next[2]["encounter_class"]) if first_next else "No encounter recorded"
        acute_return = any(item[0] <= window_90 and item[2]["encounter_class"] in ACUTE_CLASSES for item in following)
        death = date.fromisoformat(patient["death_date"]) if patient["death_date"] else None
        died_90 = bool(death and index_stop.date() < death <= window_90.date())
        endpoint = "Death within 90 days" if died_90 else ("Acute return within 90 days" if acute_return else "No acute return within 90 days")
        days = (first_next[0] - index_stop).total_seconds() / 86400 if first_next else None
        cohort.append(
            {
                **patient,
                "age_at_index": age_on(patient["birth_date"], index_start),
                "index_encounter_id": index["encounter_id"],
                "index_start": index["start"],
                "index_stop": index["stop"],
                "index_class": index["encounter_class"].title(),
                "next_30d_state": state,
                "next_30d_encounter_id": first_next[2]["encounter_id"] if first_next else "",
                "next_30d_start": first_next[2]["start"] if first_next else "",
                "next_30d_days_after_index_stop": f"{days:.3f}" if days is not None else "",
                "acute_return_90d": "yes" if acute_return else "no",
                "death_90d": "yes" if died_90 else "no",
                "endpoint_90d": endpoint,
                "transition_path": f"{index['encounter_class'].title()} -> {state}",
            }
        )

    cohort.sort(key=lambda row: (str(row["index_start"]), str(row["patient_id"])))
    path_counts = Counter(str(row["transition_path"]) for row in cohort)
    path_acute = Counter(str(row["transition_path"]) for row in cohort if row["acute_return_90d"] == "yes")
    total = len(cohort)
    total_acute = sum(row["acute_return_90d"] == "yes" for row in cohort)
    overall_pct = 100 * total_acute / total
    for row in cohort:
        path = str(row["transition_path"])
        count = path_counts[path]
        acute_count = path_acute[path]
        rate = 100 * acute_count / count
        row.update(
            {
                "path_count": count,
                "path_denominator": count,
                "path_acute_return_count": acute_count,
                "path_acute_return_pct": f"{rate:.1f}",
                "cohort_acute_return_pct": f"{overall_pct:.1f}",
                "priority_screen": "yes" if count >= 20 and rate > overall_pct else "no",
            }
        )
    return cohort


def build_edges(cohort: list[dict[str, object]]) -> list[dict[str, object]]:
    total = len(cohort)
    transitions = (
        ("Index encounter", "index_class", "Next encounter within 30 days", "next_30d_state"),
        ("Next encounter within 30 days", "next_30d_state", "Ninety-day endpoint", "endpoint_90d"),
    )
    rows: list[dict[str, object]] = []
    for stage_from, field_from, stage_to, field_to in transitions:
        counts = Counter((str(row[field_from]), str(row[field_to])) for row in cohort)
        denominators = Counter(str(row[field_from]) for row in cohort)
        for (node_from, node_to), count in sorted(counts.items()):
            denominator = denominators[node_from]
            rows.append(
                {
                    "stage_from": stage_from,
                    "node_from": node_from,
                    "stage_to": stage_to,
                    "node_to": node_to,
                    "patient_count": count,
                    "cohort_denominator": total,
                    "cohort_pct": f"{100 * count / total:.1f}",
                    "node_from_denominator": denominator,
                    "node_from_pct": f"{100 * count / denominator:.1f}",
                }
            )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-zip", type=Path, help="Pinned Synthea sample ZIP used for a source refresh")
    args = parser.parse_args()

    if args.source_zip:
        patients, encounters = select_source(args.source_zip)
        write_csv(PATIENT_OUTPUT, PATIENT_FIELDS, patients)
        write_csv(ENCOUNTER_OUTPUT, ENCOUNTER_FIELDS, encounters)
    else:
        if not PATIENT_OUTPUT.exists() or not ENCOUNTER_OUTPUT.exists():
            raise FileNotFoundError("Committed source selections are missing; pass --source-zip to create them")
        patients = read_csv(PATIENT_OUTPUT)
        encounters = read_csv(ENCOUNTER_OUTPUT)

    cohort = build_cohort(patients, encounters)
    edges = build_edges(cohort)
    write_csv(COHORT_OUTPUT, COHORT_FIELDS, cohort)
    write_csv(EDGE_OUTPUT, EDGE_FIELDS, edges)
    print(f"Wrote {len(patients):,} patients, {len(encounters):,} encounters, {len(cohort):,} cohort rows, and {len(edges):,} edges.")
    for path, digest in ((PATIENT_OUTPUT, sha256(PATIENT_OUTPUT)), (ENCOUNTER_OUTPUT, sha256(ENCOUNTER_OUTPUT)), (COHORT_OUTPUT, sha256(COHORT_OUTPUT)), (EDGE_OUTPUT, sha256(EDGE_OUTPUT))):
        print(f"{path.name}: {digest}")


if __name__ == "__main__":
    main()

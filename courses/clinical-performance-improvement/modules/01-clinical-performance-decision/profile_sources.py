"""Validate APP-3 Module 01 sources and build deterministic teaching artifacts."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RAW = DATA / "raw"
TIMELY_NAME = "Timely_and_Effective_Care-Hospital.csv.gz"
COMPLICATIONS_NAME = "Complications_and_Deaths-Hospital.csv.gz"
CAPACITY_NAME = "HHS-Capacity-Massachusetts.csv.gz"
TIMELY = {
    "rows": 138084, "columns": 16, "bytes": 34150899,
    "sha256": "1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516",
    "facilities": 4658, "measures": 30, "states": 56,
}
COMPLICATIONS = {
    "rows": 95800, "columns": 18, "bytes": 22963267,
    "sha256": "26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d",
    "facilities": 4790, "measures": 20, "states": 56,
}
CAPACITY = {
    "rows": 1045406, "columns": 128, "bytes": 481497539,
    "sha256": "b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f",
    "facilities": 5172, "weeks": 226, "min_week": "2019/12/29", "max_week": "2024/04/21",
    "ma_rows": 15179, "ma_facilities": 74, "ma_weeks": 214,
    "ma_min_week": "2020/03/22", "ma_max_week": "2024/04/21",
}
TIMELY_HEADER = [
    "Facility ID", "Facility Name", "Address", "City/Town", "State", "ZIP Code",
    "County/Parish", "Telephone Number", "Condition", "Measure ID", "Measure Name",
    "Score", "Sample", "Footnote", "Start Date", "End Date",
]
COMPLICATIONS_HEADER = [
    "Facility ID", "Facility Name", "Address", "City/Town", "State", "ZIP Code",
    "County/Parish", "Telephone Number", "Measure ID", "Measure Name",
    "Compared to National", "Denominator", "Score", "Lower Estimate", "Higher Estimate",
    "Footnote", "Start Date", "End Date",
]
CAPACITY_FIELDS = [
    "hospital_pk", "collection_week", "state", "ccn", "hospital_name", "hospital_subtype",
    "fips_code", "is_metro_micro", "total_beds_7_day_avg", "total_beds_7_day_coverage",
    "inpatient_beds_7_day_avg", "inpatient_beds_7_day_coverage",
    "inpatient_beds_used_7_day_avg", "inpatient_beds_used_7_day_coverage",
    "all_adult_hospital_inpatient_beds_7_day_avg",
    "all_adult_hospital_inpatient_beds_7_day_coverage",
    "all_adult_hospital_inpatient_bed_occupied_7_day_avg",
    "all_adult_hospital_inpatient_bed_occupied_7_day_coverage",
    "total_staffed_adult_icu_beds_7_day_avg",
    "total_staffed_adult_icu_beds_7_day_coverage",
    "staffed_adult_icu_bed_occupancy_7_day_avg",
    "staffed_adult_icu_bed_occupancy_7_day_coverage",
    "previous_day_total_ED_visits_7_day_sum", "is_corrected",
]
ANCHORS = [
    ("A01", "CMS-TIMELY-2026-08-13", "EDV", "emergency department volume", "demand context", 4658, 3826, 832, "2024-01-01 through 2024-12-31"),
    ("A02", "CMS-TIMELY-2026-08-13", "OP_18b", "median emergency visit duration", "timeliness outcome context", 4658, 4081, 577, "2024-10-01 through 2025-09-30"),
    ("A03", "CMS-TIMELY-2026-08-13", "OP_22", "left before being seen", "access and balancing context", 4658, 3821, 837, "2024-01-01 through 2024-12-31"),
    ("A04", "CMS-COMPLICATIONS-2026-08-13", "PSI_90", "patient safety and adverse events composite", "safety context", 4790, 2908, 1882, "2022-07-01 through 2024-06-30"),
    ("A05", "CMS-COMPLICATIONS-2026-08-13", "PSI_04", "death among surgical inpatients with serious treatable complications", "harm-definition context", 4790, 1521, 3269, "2022-07-01 through 2024-06-30"),
    ("A06", "CMS-COMPLICATIONS-2026-08-13", "PSI_03", "pressure ulcer rate", "specific safety-measure context", 4790, 3056, 1734, "2022-07-01 through 2024-06-30"),
    ("A07", "HHS-CAPACITY-2024-05-03", "inpatient_beds_7_day_avg", "staffed inpatient capacity", "capacity context", 15179, 15057, 122, "2020-03-22 through 2024-04-21"),
    ("A08", "HHS-CAPACITY-2024-05-03", "inpatient_beds_used_7_day_avg", "inpatient beds used", "occupancy context", 15179, 14807, 372, "2020-03-22 through 2024-04-21"),
    ("A09", "HHS-CAPACITY-2024-05-03", "total_staffed_adult_icu_beds_7_day_avg", "staffed adult ICU capacity", "specialized-capacity context", 15179, 13877, 1302, "2020-03-22 through 2024-04-21"),
    ("A10", "HHS-CAPACITY-2024-05-03", "previous_day_total_ED_visits_7_day_sum", "weekly emergency visit demand", "demand context", 15179, 10909, 4270, "2020-03-22 through 2024-04-21"),
]


class SourceError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def raw_identity(path: Path, compressed: bool = False) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    opener = gzip.open if compressed else Path.open
    with opener(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(block)
            digest.update(block)
    return size, digest.hexdigest()


def open_text(path: Path, compressed: bool = False):
    if compressed:
        return gzip.open(path, "rt", encoding="utf-8-sig", newline="")
    return path.open("r", encoding="utf-8-sig", newline="")


def profile_cms(path: Path, expected: dict[str, object], header: list[str], compressed: bool = False) -> dict[str, object]:
    size, digest = raw_identity(path, compressed)
    if size != expected["bytes"] or digest != expected["sha256"]:
        raise SourceError(f"Source identity mismatch for {path.name}: {size} bytes, {digest}")
    rows = 0
    facilities: set[str] = set()
    measures: set[str] = set()
    states: set[str] = set()
    with open_text(path, compressed) as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != header:
            raise SourceError(f"Unexpected header for {path.name}")
        for row in reader:
            rows += 1
            facilities.add(row["Facility ID"])
            measures.add(row["Measure ID"])
            states.add(row["State"])
    summary = {"rows": rows, "columns": len(header), "facilities": len(facilities), "measures": len(measures), "states": len(states)}
    for key in summary:
        if summary[key] != expected[key]:
            raise SourceError(f"Unexpected {key} for {path.name}: {summary[key]}")
    return summary


def profile_capacity_full(path: Path) -> tuple[dict[str, object], bytes]:
    if path.stat().st_size != CAPACITY["bytes"] or sha256(path) != CAPACITY["sha256"]:
        raise SourceError("Complete HHS capacity source identity mismatch")
    rows = 0
    facilities: set[str] = set()
    weeks: set[str] = set()
    ma_facilities: set[str] = set()
    corrected: Counter[str] = Counter()
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CAPACITY_FIELDS, lineterminator="\n")
    writer.writeheader()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if len(reader.fieldnames or []) != CAPACITY["columns"] or any(field not in (reader.fieldnames or []) for field in CAPACITY_FIELDS):
            raise SourceError("Complete HHS capacity header mismatch")
        for row in reader:
            rows += 1
            facilities.add(row["hospital_pk"])
            weeks.add(row["collection_week"])
            corrected[row["is_corrected"]] += 1
            if row["state"] == "MA":
                ma_facilities.add(row["hospital_pk"])
                writer.writerow({field: row[field] for field in CAPACITY_FIELDS})
    extract = output.getvalue().encode("utf-8")
    extract_rows = extract.count(b"\n") - 1
    summary = {
        "rows": rows, "columns": CAPACITY["columns"], "facilities": len(facilities),
        "weeks": len(weeks), "min_week": min(weeks), "max_week": max(weeks),
        "ma_rows": extract_rows, "ma_facilities": len(ma_facilities),
        "corrected_false": corrected["false"], "corrected_true": corrected["true"],
    }
    for key in ("rows", "columns", "facilities", "weeks", "min_week", "max_week", "ma_rows", "ma_facilities"):
        if summary[key] != CAPACITY[key]:
            raise SourceError(f"Unexpected HHS capacity {key}: {summary[key]}")
    return summary, extract


def profile_capacity_extract(path: Path) -> dict[str, object]:
    raw_size, raw_hash = raw_identity(path, compressed=True)
    rows = 0
    facilities: set[str] = set()
    weeks: set[str] = set()
    valid = Counter()
    with open_text(path, compressed=True) as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != CAPACITY_FIELDS:
            raise SourceError("Committed HHS capacity extract header mismatch")
        for row in reader:
            rows += 1
            if row["state"] != "MA":
                raise SourceError("HHS capacity extract contains a non-Massachusetts row")
            facilities.add(row["hospital_pk"])
            weeks.add(row["collection_week"])
            for field in ("inpatient_beds_7_day_avg", "inpatient_beds_used_7_day_avg", "total_staffed_adult_icu_beds_7_day_avg", "previous_day_total_ED_visits_7_day_sum"):
                if row[field].strip() not in {"", "-999999"}:
                    valid[field] += 1
    summary = {
        "rows": rows, "columns": len(CAPACITY_FIELDS), "facilities": len(facilities),
        "weeks": len(weeks), "min_week": min(weeks), "max_week": max(weeks),
        "raw_bytes": raw_size, "raw_sha256": raw_hash, "valid": dict(valid),
    }
    if (rows != CAPACITY["ma_rows"] or len(facilities) != CAPACITY["ma_facilities"]
            or len(weeks) != CAPACITY["ma_weeks"] or min(weeks) != CAPACITY["ma_min_week"]
            or max(weeks) != CAPACITY["ma_max_week"]):
        raise SourceError("Committed HHS capacity extract dimensions mismatch")
    return summary


def deterministic_gzip(raw: bytes, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as file_handle:
        with gzip.GzipFile(filename="", mode="wb", fileobj=file_handle, mtime=0) as zipped:
            zipped.write(raw)


def gzip_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as input_handle, target.open("wb") as output_handle:
        with gzip.GzipFile(filename="", mode="wb", fileobj=output_handle, mtime=0) as zipped:
            shutil.copyfileobj(input_handle, zipped, 1024 * 1024)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_profiles(capacity_summary: dict[str, object], extract_summary: dict[str, object]) -> None:
    source_rows = [
        {"source_id": "CMS-TIMELY-2026-08-13", "title": "Timely and Effective Care - Hospital", "publisher": "CMS", "grain": "facility-measure-period", "rows": 138084, "columns": 16, "raw_bytes": 34150899, "raw_sha256": TIMELY["sha256"], "repository_artifact": f"data/raw/{TIMELY_NAME}", "teaching_role": "quality, flow, access, and timeliness definitions", "claim_limit": "public aggregate context; not local operations"},
        {"source_id": "CMS-COMPLICATIONS-2026-08-13", "title": "Complications and Deaths - Hospital", "publisher": "CMS", "grain": "facility-measure-period", "rows": 95800, "columns": 18, "raw_bytes": 22963267, "raw_sha256": COMPLICATIONS["sha256"], "repository_artifact": f"data/raw/{COMPLICATIONS_NAME}", "teaching_role": "safety and adverse-event definitions", "claim_limit": "public aggregate context; not a current local event"},
        {"source_id": "HHS-CAPACITY-2024-05-03", "title": "COVID-19 Reported Patient Impact and Hospital Capacity by Facility", "publisher": "HHS", "grain": "facility-week", "rows": 1045406, "columns": 128, "raw_bytes": 481497539, "raw_sha256": CAPACITY["sha256"], "repository_artifact": f"data/raw/{CAPACITY_NAME}", "teaching_role": "historical capacity, occupancy, coverage, and demand fields", "claim_limit": "historical aggregate context; full binary is external"},
        {"source_id": "CGH-ED-01-DECLARATION", "title": "CGH-ED-01 fictional service declaration", "publisher": "Open Clinical Learning Commons", "grain": "service declaration only", "rows": 0, "columns": 0, "raw_bytes": 0, "raw_sha256": "not applicable", "repository_artifact": "synthetic-service-declaration.md", "teaching_role": "future local operational case", "claim_limit": "no public hospital linkage; operational rows begin in Module 02"},
    ]
    fields = ["source_id", "title", "publisher", "grain", "rows", "columns", "raw_bytes", "raw_sha256", "repository_artifact", "teaching_role", "claim_limit"]
    write_csv(DATA / "source-inventory.csv", fields, source_rows)
    anchor_fields = ["anchor_id", "source_id", "field_or_measure_id", "concept", "evidence_role", "source_rows", "reported_rows", "unavailable_rows", "period_or_range", "decision_use", "claim_limit"]
    anchor_rows = [{
        "anchor_id": a[0], "source_id": a[1], "field_or_measure_id": a[2], "concept": a[3],
        "evidence_role": a[4], "source_rows": a[5], "reported_rows": a[6], "unavailable_rows": a[7],
        "period_or_range": a[8], "decision_use": "define the future local measure family and evidence needed",
        "claim_limit": "does not describe CGH-ED-01 or authorize comparison or action",
    } for a in ANCHORS]
    write_csv(DATA / "measure-family-anchors.csv", anchor_fields, anchor_rows)
    profile_fields = ["metric_id", "metric", "value", "unit", "method", "decision_use"]
    metrics = [
        ("CP01", "complete source rows", capacity_summary["rows"], "facility-weeks", "stream complete accepted CSV", "confirm full-source inspection"),
        ("CP02", "complete source columns", capacity_summary["columns"], "fields", "read complete header", "confirm schema scale"),
        ("CP03", "complete source bytes", CAPACITY["bytes"], "bytes", "file size", "pin exact external binary"),
        ("CP04", "complete source SHA-256", CAPACITY["sha256"], "hash", "SHA-256 complete bytes", "pin exact external binary"),
        ("CP05", "complete source facilities", capacity_summary["facilities"], "facilities", "distinct hospital_pk", "show national scope"),
        ("CP06", "complete source weeks", capacity_summary["weeks"], "weeks", "distinct collection_week", "show longitudinal coverage"),
        ("CP07", "first collection week", capacity_summary["min_week"], "date", "minimum collection_week", "bound historical interpretation"),
        ("CP08", "last collection week", capacity_summary["max_week"], "date", "maximum collection_week", "bound historical interpretation"),
        ("CP09", "corrected false rows", capacity_summary["corrected_false"], "facility-weeks", "count is_corrected=false", "retain correction status"),
        ("CP10", "corrected true rows", capacity_summary["corrected_true"], "facility-weeks", "count is_corrected=true", "retain correction status"),
        ("CP11", "Massachusetts extract rows", extract_summary["rows"], "facility-weeks", "retain every state=MA row", "provide reproducible teaching scale"),
        ("CP12", "Massachusetts extract facilities", extract_summary["facilities"], "facilities", "distinct hospital_pk", "show facility support"),
        ("CP13", "Massachusetts extract columns", extract_summary["columns"], "fields", "fixed decision-relevant field list", "keep the repository artifact bounded"),
        ("CP14", "Massachusetts extract raw bytes", extract_summary["raw_bytes"], "bytes", "decompressed artifact size", "verify exact extract"),
        ("CP15", "Massachusetts extract raw SHA-256", extract_summary["raw_sha256"], "hash", "SHA-256 decompressed artifact", "verify exact extract"),
        ("CP16", "reported inpatient capacity rows", extract_summary["valid"]["inpatient_beds_7_day_avg"], "facility-weeks", "exclude blank and -999999", "assess capacity-field feasibility"),
        ("CP17", "reported inpatient use rows", extract_summary["valid"]["inpatient_beds_used_7_day_avg"], "facility-weeks", "exclude blank and -999999", "assess occupancy-field feasibility"),
        ("CP18", "reported adult ICU capacity rows", extract_summary["valid"]["total_staffed_adult_icu_beds_7_day_avg"], "facility-weeks", "exclude blank and -999999", "assess specialized-capacity feasibility"),
        ("CP19", "reported emergency visit rows", extract_summary["valid"]["previous_day_total_ED_visits_7_day_sum"], "facility-weeks", "exclude blank and -999999", "assess demand-field feasibility"),
        ("CP20", "public patient-level rows", 0, "rows", "source grain audit", "prohibit patient inference"),
    ]
    write_csv(DATA / "capacity-source-profile.csv", profile_fields, [dict(zip(profile_fields, metric)) for metric in metrics])


def build(timely: Path, complications: Path, capacity: Path) -> dict[str, object]:
    profile_cms(timely, TIMELY, TIMELY_HEADER)
    profile_cms(complications, COMPLICATIONS, COMPLICATIONS_HEADER)
    capacity_summary, extract = profile_capacity_full(capacity)
    RAW.mkdir(parents=True, exist_ok=True)
    gzip_file(timely, RAW / TIMELY_NAME)
    gzip_file(complications, RAW / COMPLICATIONS_NAME)
    deterministic_gzip(extract, RAW / CAPACITY_NAME)
    extract_summary = profile_capacity_extract(RAW / CAPACITY_NAME)
    write_profiles(capacity_summary, extract_summary)
    return {"timely_rows": TIMELY["rows"], "complications_rows": COMPLICATIONS["rows"], "capacity_rows": CAPACITY["rows"], "capacity_extract_rows": extract_summary["rows"], "capacity_extract_raw_sha256": extract_summary["raw_sha256"]}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def verify_committed(root: Path = ROOT) -> dict[str, object]:
    data = root / "data"
    profile_cms(data / "raw" / TIMELY_NAME, TIMELY, TIMELY_HEADER, compressed=True)
    profile_cms(data / "raw" / COMPLICATIONS_NAME, COMPLICATIONS, COMPLICATIONS_HEADER, compressed=True)
    extract = profile_capacity_extract(data / "raw" / CAPACITY_NAME)
    _, inventory = read_csv(data / "source-inventory.csv")
    _, anchors = read_csv(data / "measure-family-anchors.csv")
    _, profile = read_csv(data / "capacity-source-profile.csv")
    if len(inventory) != 4 or len(anchors) != 10 or len(profile) != 20:
        raise SourceError("Committed source evidence row counts mismatch")
    values = {row["metric_id"]: row["value"] for row in profile}
    if values.get("CP04") != CAPACITY["sha256"] or values.get("CP15") != extract["raw_sha256"]:
        raise SourceError("Committed capacity profile identity mismatch")
    return {"timely_rows": TIMELY["rows"], "complications_rows": COMPLICATIONS["rows"], "capacity_rows": CAPACITY["rows"], "capacity_extract_rows": extract["rows"], "capacity_extract_raw_sha256": extract["raw_sha256"]}


def self_check() -> None:
    summary = verify_committed()
    with tempfile.TemporaryDirectory(prefix="app3-module01-profile-") as temp_dir:
        changed = Path(temp_dir) / "changed.csv.gz"
        raw = gzip.decompress((RAW / TIMELY_NAME).read_bytes())
        deterministic_gzip(raw.replace(b"Facility ID", b"Facility XX", 1), changed)
        try:
            profile_cms(changed, TIMELY, TIMELY_HEADER, compressed=True)
        except SourceError:
            pass
        else:
            raise AssertionError("Profiler accepted a changed CMS source")
    print(f"APP-3 Module 01 source self-check passed: {json.dumps(summary, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timely-csv", type=Path)
    parser.add_argument("--complications-csv", type=Path)
    parser.add_argument("--capacity-csv", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if args.write:
            if not all((args.timely_csv, args.complications_csv, args.capacity_csv)):
                parser.error("--write requires all three complete source CSV paths")
            print(json.dumps(build(args.timely_csv, args.complications_csv, args.capacity_csv), indent=2))
            return
        print(json.dumps(verify_committed(), indent=2))
    except (OSError, KeyError, ValueError, SourceError) as error:
        parser.exit(1, f"Source profiling failed: {error}\n")


if __name__ == "__main__":
    main()

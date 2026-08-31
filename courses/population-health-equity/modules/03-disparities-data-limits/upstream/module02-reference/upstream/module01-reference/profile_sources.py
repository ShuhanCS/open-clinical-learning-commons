"""Acquire, normalize, profile, and verify APP-5 Module 01 public sources."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RETRIEVED = "2026-08-31"
USER_AGENT = "OpenClinicalLearningCommons/0.87.0 source acquisition"

PLACES_URL = (
    "https://data.cdc.gov/resource/cwsq-ngmh.csv?"
    "$select=year,stateabbr,statedesc,countyname,countyfips,locationname,datasource,"
    "category,measure,data_value_unit,data_value_type,data_value,"
    "data_value_footnote_symbol,data_value_footnote,low_confidence_limit,"
    "high_confidence_limit,totalpopulation,totalpop18plus,geolocation,locationid,"
    "categoryid,measureid,datavaluetypeid,short_question_text&"
    "$where=stateabbr%3D%27MA%27%20AND%20measureid%3D%27DIABETES%27&"
    "$order=locationid&$limit=5000"
)
ACS_URL = (
    "https://www2.census.gov/programs-surveys/acs/summary_file/2024/"
    "table-based-SF/data/5YRData/acsdt5y2024-b01001.dat"
)
SVI_URL = (
    "https://svi2.cdc.gov/webapi/Documents/download?"
    "year=2022&type=csv&category=states&name=MASSACHUSETTS"
)

RAW_IDENTITIES = {
    "places": {"bytes": 426520, "sha256": "55125d80183968c4aaef419ed6171ee0d897254a95c472a8e4b346aa19a35ba3"},
    "acs": {"bytes": 200356282, "sha256": "1637b18a96881b81e050df1cd3d5ac38a33208b9b69b40e1dbeb3c4e13718f0e"},
    "svi": {"bytes": 1189804, "sha256": "9e38e15b91041909fc58bdd56db677d9073598f9f8080048b71d16dd38f8b81e"},
}

RELEASE_FILES = {
    "places": "data/places-diabetes-ma-tract-2025.csv",
    "acs": "data/acs-b01001-ma-tract-2024.csv",
    "svi": "data/svi2022-ma-tract.csv",
}

PINNED_RELEASES: dict[str, dict[str, object]] = {
    "places": {"bytes": 356204, "sha256": "3d55a099be438999fd52b1e34f13589dcf3e260162c56967fa01fb0a80135846"},
    "acs": {"bytes": 576420, "sha256": "bca33aebaa0a9e418d6a5343818aebc1e8b1dc2d355156419e5693d1907fa419"},
    "svi": {"bytes": 1188187, "sha256": "fac1aabd51880624ce728f4a63f01ba6b50959c203c6975400c02daf21329de0"},
}

PLACES_FIELDS = [
    "year", "stateabbr", "statedesc", "countyname", "countyfips", "locationname",
    "datasource", "category", "measure", "data_value_unit", "data_value_type",
    "data_value", "data_value_footnote_symbol", "data_value_footnote",
    "low_confidence_limit", "high_confidence_limit", "totalpopulation",
    "totalpop18plus", "geolocation", "locationid", "categoryid", "measureid",
    "datavaluetypeid", "short_question_text",
]
ACS_SOURCE_FIELDS = ["GEO_ID"] + [
    f"B01001_{kind}{cell:03d}"
    for cell in range(1, 50)
    for kind in ("E", "M")
]
ACS_RELEASE_FIELDS = ["tract_fips"] + ACS_SOURCE_FIELDS

SOURCE_INVENTORY_FIELDS = [
    "source_id", "publisher", "title", "release", "upstream_url", "retrieved",
    "raw_scope", "raw_bytes", "raw_sha256", "raw_rows", "raw_fields",
    "released_path", "released_rows", "released_fields", "released_bytes",
    "released_sha256", "geography", "population_or_universe", "period",
    "uncertainty", "teaching_role", "claim_limit",
]
FIELD_INVENTORY_FIELDS = [
    "source_id", "field_order", "field_name", "source_or_derived", "rows",
    "nonmissing", "missing", "distinct_nonmissing", "negative_sentinel_like",
    "teaching_role",
]
JOIN_FIELDS = [
    "comparison", "left_source", "left_tracts", "right_source", "right_tracts",
    "intersection", "left_only", "right_only", "interpretation",
]
READING_FIELDS = ["source_id", "title", "version_or_release", "url", "teaching_role", "claim_limit"]


class SourceError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, target: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=300) as response, target.open("wb") as handle:
        if response.status != 200:
            raise SourceError(f"Download failed with HTTP {response.status}: {url}")
        shutil.copyfileobj(response, handle, 1024 * 1024)
    if not target.stat().st_size:
        raise SourceError(f"Download returned an empty file: {url}")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceError(message)


def verify_identity(label: str, path: Path, expected: dict[str, object]) -> None:
    require(path.stat().st_size == expected["bytes"], f"{label} byte count changed")
    require(sha256(path) == expected["sha256"], f"{label} SHA-256 changed")


def read_csv(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize_places(raw: Path) -> list[dict[str, str]]:
    fields, rows = read_csv(raw)
    require(fields == PLACES_FIELDS, "PLACES field contract changed")
    require(len(rows) == 1597, f"Expected 1,597 PLACES rows, received {len(rows):,}")
    require(all(row["stateabbr"] == "MA" for row in rows), "PLACES contains an out-of-state row")
    require(all(row["measureid"] == "DIABETES" for row in rows), "PLACES contains a wrong measure")
    require(all(row["datavaluetypeid"] == "CrdPrv" for row in rows), "PLACES value type changed")
    require(all(row["year"] == "2023" for row in rows), "PLACES measure year changed")
    ids = [row["locationid"] for row in rows]
    require(len(ids) == len(set(ids)), "PLACES contains a duplicate tract")
    require(all(len(value) == 11 and value.startswith("25") for value in ids), "PLACES tract key changed")
    rows.sort(key=lambda row: row["locationid"])
    write_csv(ROOT / RELEASE_FILES["places"], PLACES_FIELDS, rows)
    return rows


def normalize_svi(raw: Path) -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = read_csv(raw)
    require(len(fields) == 158 and fields[:8] == ["ST", "STATE", "ST_ABBR", "STCNTY", "COUNTY", "FIPS", "LOCATION", "AREA_SQMI"], "SVI field contract changed")
    require(fields[-4:] == ["EP_TWOMORE", "MP_TWOMORE", "EP_OTHERRACE", "MP_OTHERRACE"], "SVI trailing fields changed")
    require(len(rows) == 1613, f"Expected 1,613 SVI rows, received {len(rows):,}")
    require(all(row["ST"] == "25" and row["ST_ABBR"] == "MA" for row in rows), "SVI contains an out-of-state row")
    ids = [row["FIPS"] for row in rows]
    require(len(ids) == len(set(ids)), "SVI contains a duplicate tract")
    require(all(len(value) == 11 and value.startswith("25") for value in ids), "SVI tract key changed")
    rows.sort(key=lambda row: row["FIPS"])
    write_csv(ROOT / RELEASE_FILES["svi"], fields, rows)
    return fields, rows


def normalize_acs(raw: Path) -> list[dict[str, str]]:
    fields, rows = read_csv(raw, delimiter="|")
    require(fields == ACS_SOURCE_FIELDS, "ACS B01001 field contract changed")
    require(len(rows) == 616690, f"Expected 616,690 ACS source rows, received {len(rows):,}")
    selected = []
    for row in rows:
        geo_id = row["GEO_ID"]
        if geo_id.startswith("1400000US25"):
            selected.append({"tract_fips": geo_id.removeprefix("1400000US"), **row})
    require(len(selected) == 1620, f"Expected 1,620 Massachusetts ACS tract rows, received {len(selected):,}")
    ids = [row["tract_fips"] for row in selected]
    require(len(ids) == len(set(ids)), "ACS contains a duplicate Massachusetts tract")
    require(all(len(value) == 11 and value.startswith("25") for value in ids), "ACS tract key changed")
    selected.sort(key=lambda row: row["tract_fips"])
    write_csv(ROOT / RELEASE_FILES["acs"], ACS_RELEASE_FIELDS, selected)
    return selected


def field_profile(source_id: str, fields: list[str], rows: list[dict[str, str]], role: str, derived: set[str] | None = None) -> list[dict[str, object]]:
    derived = derived or set()
    output = []
    for order, field in enumerate(fields, start=1):
        values = [row[field] for row in rows]
        present = [value for value in values if value != ""]
        negative = sum(value.startswith("-") and value[1:].replace(".", "", 1).isdigit() for value in present)
        output.append({
            "source_id": source_id,
            "field_order": order,
            "field_name": field,
            "source_or_derived": "derived tract key" if field in derived else "source",
            "rows": len(rows),
            "nonmissing": len(present),
            "missing": len(rows) - len(present),
            "distinct_nonmissing": len(set(present)),
            "negative_sentinel_like": negative,
            "teaching_role": role,
        })
    return output


def reading_rows() -> list[dict[str, str]]:
    return [
        {"source_id": "PLACES-2025-METADATA", "title": "PLACES census-tract 2025 release metadata", "version_or_release": "2025 release", "url": "https://data.cdc.gov/api/views/cwsq-ngmh", "teaching_role": "release identity, methods summary, fields, rights, and update history", "claim_limit": "metadata does not make model estimates observed cases"},
        {"source_id": "PLACES-PROGRAM", "title": "CDC PLACES", "version_or_release": "current program page", "url": "https://www.cdc.gov/places/", "teaching_role": "small-area-estimation purpose and methods route", "claim_limit": "PLACES cannot detect local intervention effects"},
        {"source_id": "ACS5-2024-DEVELOPER", "title": "American Community Survey five-year data", "version_or_release": "2020-2024", "url": "https://www.census.gov/data/developers/data-sets/acs-5year.html?lv=true", "teaching_role": "ACS table, geography, estimate, margin, and API guidance", "claim_limit": "ACS values are survey estimates rather than exact counts"},
        {"source_id": "ACS5-2024-B01001", "title": "ACS Detailed Table B01001: Sex by Age", "version_or_release": "2020-2024", "url": "https://data.census.gov/table/ACSDT5Y2024.B01001", "teaching_role": "population and age-structure denominator definitions", "claim_limit": "the table does not contain diabetes events or intervention outcomes"},
        {"source_id": "ACS5-2024-SUMMARY", "title": "ACS B01001 table-based Summary File", "version_or_release": "2020-2024", "url": ACS_URL, "teaching_role": "complete national source used before the Massachusetts tract extract", "claim_limit": "vintage and margins remain attached to derived denominators"},
        {"source_id": "SVI-2022-DOCUMENTATION", "title": "CDC/ATSDR SVI data and documentation", "version_or_release": "2022", "url": "https://atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html", "teaching_role": "field definitions, corrections, ranks, release comparison, and citation", "claim_limit": "ranks are release-relative and area values cannot be assigned to individuals"},
        {"source_id": "SVI-2022-MA", "title": "CDC/ATSDR SVI Massachusetts census-tract CSV", "version_or_release": "2022", "url": SVI_URL, "teaching_role": "complete Massachusetts tract context release", "claim_limit": "SVI alone cannot determine targeting, eligibility, funding, or causation"},
        {"source_id": "TIGER-2024", "title": "TIGER/Line 2024 shapefiles", "version_or_release": "2024", "url": "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html", "teaching_role": "accepted source route for Module 04 geography", "claim_limit": "boundaries do not define community identity, service access, or eligibility"},
        {"source_id": "TIGER-2024-TRACT", "title": "TIGER/Line census-tract download interface", "version_or_release": "2024", "url": "https://www.census.gov/cgi-bin/geo/shapefiles/index.php?layergroup=Census+Tracts&year=2024", "teaching_role": "complete Massachusetts tract geometry acquisition route", "claim_limit": "geometry is acquired and validated in Module 04, not Module 01"},
    ]


def make_profiles(places: list[dict[str, str]], acs: list[dict[str, str]], svi_fields: list[str], svi: list[dict[str, str]]) -> dict[str, object]:
    ids = {
        "places": {row["locationid"] for row in places},
        "acs": {row["tract_fips"] for row in acs},
        "svi": {row["FIPS"] for row in svi},
    }
    require(len(ids["places"] & ids["acs"] & ids["svi"]) == 1597, "Three-source tract intersection changed")
    comparisons = []
    for label, left, right, interpretation in (
        ("PLACES versus SVI", "places", "svi", "All PLACES diabetes tracts have SVI context; 16 SVI tracts have no PLACES diabetes row."),
        ("PLACES versus ACS", "places", "acs", "All PLACES diabetes tracts have ACS B01001 denominators; 23 ACS tracts have no PLACES diabetes row."),
        ("SVI versus ACS", "svi", "acs", "All SVI tracts have ACS B01001 denominators; seven ACS tract records have no SVI row."),
    ):
        intersection = ids[left] & ids[right]
        comparisons.append({
            "comparison": label,
            "left_source": left,
            "left_tracts": len(ids[left]),
            "right_source": right,
            "right_tracts": len(ids[right]),
            "intersection": len(intersection),
            "left_only": len(ids[left] - ids[right]),
            "right_only": len(ids[right] - ids[left]),
            "interpretation": interpretation,
        })
    write_csv(DATA / "join-feasibility.csv", JOIN_FIELDS, comparisons)

    fields = []
    fields.extend(field_profile("cdc-places-tract-2025-ma-diabetes", PLACES_FIELDS, places, "modeled adult diabetes prevalence, interval, population, county, and tract"))
    fields.extend(field_profile("census-acs5-2024-b01001-ma-tract", ACS_RELEASE_FIELDS, acs, "population and age-by-sex denominator estimates and margins", {"tract_fips"}))
    fields.extend(field_profile("cdc-atsdr-svi-2022-ma-tract", svi_fields, svi, "area-level contextual estimates, margins, flags, themes, and relative ranks"))
    write_csv(DATA / "field-inventory.csv", FIELD_INVENTORY_FIELDS, fields)
    write_csv(DATA / "reading-inventory.csv", READING_FIELDS, reading_rows())

    release_stats = {
        label: {
            "bytes": (ROOT / path).stat().st_size,
            "sha256": sha256(ROOT / path),
        }
        for label, path in RELEASE_FILES.items()
    }
    inventory = [
        {"source_id": "cdc-places-tract-2025-ma-diabetes", "publisher": "Centers for Disease Control and Prevention", "title": "PLACES: Local Data for Better Health, Census Tract Data, 2025 release", "release": "2025 release; measure year 2023", "upstream_url": PLACES_URL, "retrieved": RETRIEVED, "raw_scope": "all Massachusetts DIABETES rows returned by the accepted Socrata query", "raw_bytes": RAW_IDENTITIES["places"]["bytes"], "raw_sha256": RAW_IDENTITIES["places"]["sha256"], "raw_rows": 1597, "raw_fields": 24, "released_path": RELEASE_FILES["places"], "released_rows": len(places), "released_fields": len(PLACES_FIELDS), "released_bytes": release_stats["places"]["bytes"], "released_sha256": release_stats["places"]["sha256"], "geography": "Massachusetts 2020 census tract identity carried by PLACES", "population_or_universe": "adults age 18 and older for modeled diagnosed-diabetes prevalence", "period": "BRFSS 2023 with PLACES 2025 release inputs", "uncertainty": "published 95 percent confidence limits", "teaching_role": "modeled surveillance pattern and source feasibility", "claim_limit": "not observed cases, individual risk, causation, program effect, eligibility, or allocation authority"},
        {"source_id": "census-acs5-2024-b01001-ma-tract", "publisher": "U.S. Census Bureau", "title": "2020-2024 ACS five-year Detailed Table B01001, Sex by Age", "release": "2020-2024 five-year release", "upstream_url": ACS_URL, "retrieved": RETRIEVED, "raw_scope": "complete national table-based Summary File before Massachusetts tract extraction", "raw_bytes": RAW_IDENTITIES["acs"]["bytes"], "raw_sha256": RAW_IDENTITIES["acs"]["sha256"], "raw_rows": 616690, "raw_fields": 99, "released_path": RELEASE_FILES["acs"], "released_rows": len(acs), "released_fields": len(ACS_RELEASE_FIELDS), "released_bytes": release_stats["acs"]["bytes"], "released_sha256": release_stats["acs"]["sha256"], "geography": "Massachusetts census tract", "population_or_universe": "total population by sex and age", "period": "2020-2024", "uncertainty": "published 90 percent margins of error for every estimate", "teaching_role": "population structure, denominators, and later standardization", "claim_limit": "survey estimates; no diabetes events, individual records, or intervention outcomes"},
        {"source_id": "cdc-atsdr-svi-2022-ma-tract", "publisher": "CDC and Agency for Toxic Substances and Disease Registry", "title": "CDC/ATSDR Social Vulnerability Index 2022 Massachusetts database", "release": "2022 Massachusetts tract release", "upstream_url": SVI_URL, "retrieved": RETRIEVED, "raw_scope": "complete Massachusetts census-tract CSV", "raw_bytes": RAW_IDENTITIES["svi"]["bytes"], "raw_sha256": RAW_IDENTITIES["svi"]["sha256"], "raw_rows": 1613, "raw_fields": 158, "released_path": RELEASE_FILES["svi"], "released_rows": len(svi), "released_fields": len(svi_fields), "released_bytes": release_stats["svi"]["bytes"], "released_sha256": release_stats["svi"]["sha256"], "geography": "Massachusetts census tract ranked within the state release", "population_or_universe": "area-level ACS-derived population and housing context", "period": "2022 SVI using its documented source vintages", "uncertainty": "published estimates, margins, flags, and relative ranks", "teaching_role": "area context and source-feasibility audit", "claim_limit": "not an individual trait, longitudinal score, causal effect, automatic target, eligibility rule, or funding authority"},
    ]
    write_csv(DATA / "source-inventory.csv", SOURCE_INVENTORY_FIELDS, inventory)

    return {
        "source_rows": {"places": len(places), "acs": len(acs), "svi": len(svi)},
        "source_fields": {"places": len(PLACES_FIELDS), "acs": len(ACS_RELEASE_FIELDS), "svi": len(svi_fields)},
        "field_inventory_rows": len(fields),
        "three_source_intersection": len(ids["places"] & ids["acs"] & ids["svi"]),
        "union_tracts": len(ids["places"] | ids["acs"] | ids["svi"]),
        "profile_hashes": {
            name: sha256(DATA / name)
            for name in ("source-inventory.csv", "field-inventory.csv", "join-feasibility.csv", "reading-inventory.csv")
        },
        "release_stats": release_stats,
    }


def load_releases() -> tuple[list[dict[str, str]], list[dict[str, str]], list[str], list[dict[str, str]]]:
    for label, relative in RELEASE_FILES.items():
        path = ROOT / relative
        require(path.is_file(), f"Missing committed {label} release")
        if PINNED_RELEASES:
            verify_identity(f"committed {label} release", path, PINNED_RELEASES[label])
    places_fields, places = read_csv(ROOT / RELEASE_FILES["places"])
    acs_fields, acs = read_csv(ROOT / RELEASE_FILES["acs"])
    svi_fields, svi = read_csv(ROOT / RELEASE_FILES["svi"])
    require(places_fields == PLACES_FIELDS and len(places) == 1597, "Committed PLACES release changed")
    require(acs_fields == ACS_RELEASE_FIELDS and len(acs) == 1620, "Committed ACS release changed")
    require(len(svi_fields) == 158 and len(svi) == 1613, "Committed SVI release changed")
    return places, acs, svi_fields, svi


def build(acquire: bool = False, temp_root: Path | None = None) -> dict[str, object]:
    if acquire:
        temporary_parent = str(temp_root.resolve()) if temp_root else None
        if temp_root:
            temp_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="app5-module01-sources-", dir=temporary_parent) as temp_dir:
            temp = Path(temp_dir)
            raw_paths = {"places": temp / "places.csv", "acs": temp / "acs.dat", "svi": temp / "svi.csv"}
            for label, url in (("places", PLACES_URL), ("acs", ACS_URL), ("svi", SVI_URL)):
                download(url, raw_paths[label])
                verify_identity(f"downloaded {label} source", raw_paths[label], RAW_IDENTITIES[label])
            places = normalize_places(raw_paths["places"])
            acs = normalize_acs(raw_paths["acs"])
            svi_fields, svi = normalize_svi(raw_paths["svi"])
    else:
        places, acs, svi_fields, svi = load_releases()
    summary = make_profiles(places, acs, svi_fields, svi)
    if PINNED_RELEASES:
        for label, relative in RELEASE_FILES.items():
            verify_identity(f"released {label} source", ROOT / relative, PINNED_RELEASES[label])
    return summary


def self_check() -> None:
    summary = build()
    require(summary["three_source_intersection"] == 1597, "Intersection self-check failed")
    source = ROOT / RELEASE_FILES["places"]
    with tempfile.TemporaryDirectory(prefix="app5-module01-mutation-") as temp_dir:
        changed = Path(temp_dir) / source.name
        shutil.copy2(source, changed)
        raw = bytearray(changed.read_bytes())
        raw[-2] ^= 1
        changed.write_bytes(raw)
        if PINNED_RELEASES:
            try:
                verify_identity("mutated PLACES release", changed, PINNED_RELEASES["places"])
            except SourceError:
                pass
            else:
                raise AssertionError("Source mutation was accepted")
    print(f"APP-5 Module 01 source self-check passed: {json.dumps(summary, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acquire", action="store_true", help="Download accepted sources and replace the released extracts.")
    parser.add_argument("--temp-root", type=Path, help="Optional directory for the 200 MB ACS acquisition temporary file.")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        else:
            print(json.dumps(build(acquire=args.acquire, temp_root=args.temp_root), indent=2))
    except (OSError, ValueError, KeyError, urllib.error.URLError, SourceError) as error:
        parser.exit(1, f"Source profiling failed: {error}\n")


if __name__ == "__main__":
    main()

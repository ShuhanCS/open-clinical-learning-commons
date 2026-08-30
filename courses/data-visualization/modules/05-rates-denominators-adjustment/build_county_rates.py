#!/usr/bin/env python3
"""Build the public-source releases for DA-730 Module 05."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import tempfile
import urllib.request
from pathlib import Path


CDC_URL = (
    "https://data.cdc.gov/resource/fu4u-a9bh.csv?"
    "%24select=year%2Cstateabbr%2Cstatedesc%2Clocationname%2Clocationid%2C"
    "measureid%2Cmeasure%2Cdata_value_type%2Cdatavaluetypeid%2Cdata_value%2C"
    "low_confidence_limit%2Chigh_confidence_limit%2Ctotalpopulation%2C"
    "totalpop18plus%2Cdata_value_footnote_symbol%2Cdata_value_footnote&"
    "%24where=measureid%3D%27DIABETES%27&"
    "%24order=locationid%2Cdatavaluetypeid&%24limit=10000"
)
ACS_URL = (
    "https://www2.census.gov/programs-surveys/acs/summary_file/2024/"
    "table-based-SF/data/5YRData/acsdt5y2024-b01001.dat"
)
TIGER_URL = (
    "https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/"
    "State_County/MapServer/12/query?where=STATE%3D%2737%27&"
    "outFields=GEOID%2CNAME%2CSTATE%2CCOUNTY&returnGeometry=true&outSR=4326&f=geojson"
)

EXPECTED_RAW = {
    "cdc": (989397, "997a122894566fed4efb32a0a9448590eaa5b7642d4be259e41b7378b99dc0e2"),
    "acs": (200356282, "1637b18a96881b81e050df1cd3d5ac38a33208b9b69b40e1dbeb3c4e13718f0e"),
    "tiger": (305389, "7331ff92103679853c25f45a5d901a148801243d033948f32b604c413aa5e62d"),
}

CDC_FIELDS = [
    "year",
    "stateabbr",
    "statedesc",
    "locationname",
    "locationid",
    "measureid",
    "measure",
    "data_value_type",
    "datavaluetypeid",
    "data_value",
    "low_confidence_limit",
    "high_confidence_limit",
    "totalpopulation",
    "totalpop18plus",
    "data_value_footnote_symbol",
    "data_value_footnote",
]

ADULT_CELLS = list(range(7, 26)) + list(range(31, 50))
OLDER_CELLS = list(range(20, 26)) + list(range(44, 50))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url: str, path: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "OpenClinicalLearningCommons/0.16"})
    with urllib.request.urlopen(request, timeout=120) as response, path.open("wb") as target:
        shutil.copyfileobj(response, target)


def validate_raw(label: str, path: Path) -> None:
    expected_bytes, expected_hash = EXPECTED_RAW[label]
    actual = (path.stat().st_size, sha256(path))
    if actual != (expected_bytes, expected_hash):
        raise ValueError(
            f"{label} source changed: expected {expected_bytes} bytes and {expected_hash}, "
            f"received {actual[0]} bytes and {actual[1]}"
        )


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=fieldnames, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def as_int(value: str, field: str) -> int:
    try:
        return int(value)
    except ValueError as error:
        raise ValueError(f"{field} must be an integer, received {value!r}") from error


def as_float(value: str, field: str) -> float:
    try:
        return float(value)
    except ValueError as error:
        raise ValueError(f"{field} must be numeric, received {value!r}") from error


def build_places(raw_path: Path, output_path: Path) -> tuple[list[dict[str, str]], dict[str, dict[str, dict[str, str]]]]:
    with raw_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != CDC_FIELDS:
            raise ValueError(f"CDC fields changed: {reader.fieldnames}")
        rows = list(reader)

    if len(rows) != 6290:
        raise ValueError(f"Expected 6,290 CDC rows, received {len(rows):,}")
    if {row["measureid"] for row in rows} != {"DIABETES"}:
        raise ValueError("CDC extract contains a measure other than DIABETES")

    county_rows = [row for row in rows if len(row["locationid"]) == 5]
    if len(county_rows) != 6288 or len({row["locationid"] for row in county_rows}) != 3144:
        raise ValueError("CDC county contract changed")

    by_county: dict[str, dict[str, dict[str, str]]] = {}
    for row in county_rows:
        by_county.setdefault(row["locationid"], {})[row["datavaluetypeid"]] = row
    if any(set(types) != {"AgeAdjPrv", "CrdPrv"} for types in by_county.values()):
        raise ValueError("Every CDC county must have crude and age-adjusted prevalence")

    write_csv(output_path, CDC_FIELDS, rows)
    return rows, by_county


def derived_sum(row: dict[str, str], cells: list[int], prefix: str) -> tuple[int, int | None, str]:
    estimates = [as_int(row[f"B01001_E{cell:03d}"], f"B01001_E{cell:03d}") for cell in cells]
    margins = [as_int(row[f"B01001_M{cell:03d}"], f"B01001_M{cell:03d}") for cell in cells]
    if any(value < 0 for value in estimates):
        raise ValueError(f"Unexpected ACS estimate sentinel in {prefix}")
    if any(value == -555555555 for value in margins):
        return sum(estimates), None, "not available in one or more component cells"
    if any(value < 0 for value in margins):
        raise ValueError(f"Unexpected ACS margin sentinel in {prefix}")
    return sum(estimates), round(math.sqrt(sum(value * value for value in margins))), "reported"


def build_acs(raw_path: Path, output_path: Path) -> dict[str, dict[str, object]]:
    output_rows: list[dict[str, object]] = []
    with raw_path.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source, delimiter="|")
        required = {"GEO_ID"}
        required.update(f"B01001_{kind}{cell:03d}" for kind in ("E", "M") for cell in set(ADULT_CELLS + OLDER_CELLS))
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"ACS fields changed: {sorted(missing)}")

        for row in reader:
            if not row["GEO_ID"].startswith("0500000US"):
                continue
            county_fips = row["GEO_ID"][-5:]
            adults, adults_moe, adults_moe_status = derived_sum(row, ADULT_CELLS, "adult population")
            older, older_moe, older_moe_status = derived_sum(row, OLDER_CELLS, "older population")
            output_rows.append(
                {
                    "geo_id": row["GEO_ID"],
                    "county_fips": county_fips,
                    "acs_adult_population": adults,
                    "acs_adult_moe90": "" if adults_moe is None else adults_moe,
                    "acs_65plus_population": older,
                    "acs_65plus_moe90": "" if older_moe is None else older_moe,
                    "acs_65plus_share_adult_pct": f"{100 * older / adults:.1f}",
                    "acs_moe_status": (
                        "reported"
                        if adults_moe_status == older_moe_status == "reported"
                        else "not available in one or more component cells"
                    ),
                    "acs_period": "2020-2024",
                    "acs_table": "B01001",
                }
            )

    output_rows.sort(key=lambda row: str(row["county_fips"]))
    if len(output_rows) != 3222 or len({row["county_fips"] for row in output_rows}) != 3222:
        raise ValueError(f"Expected 3,222 ACS county rows, received {len(output_rows):,}")

    fields = [
        "geo_id",
        "county_fips",
        "acs_adult_population",
        "acs_adult_moe90",
        "acs_65plus_population",
        "acs_65plus_moe90",
        "acs_65plus_share_adult_pct",
        "acs_moe_status",
        "acs_period",
        "acs_table",
    ]
    write_csv(output_path, fields, output_rows)
    return {str(row["county_fips"]): row for row in output_rows}


def build_boundaries(raw_path: Path, output_path: Path) -> set[str]:
    with raw_path.open("r", encoding="utf-8") as source:
        payload = json.load(source)
    features = payload.get("features", [])
    if len(features) != 100:
        raise ValueError(f"Expected 100 TIGERweb features, received {len(features)}")

    rows: list[dict[str, object]] = []
    feature_fips: set[str] = set()
    for feature in sorted(features, key=lambda item: item["properties"]["GEOID"]):
        properties = feature["properties"]
        county_fips = str(properties["GEOID"])
        feature_fips.add(county_fips)
        geometry = feature["geometry"]
        if geometry["type"] == "Polygon":
            polygons = [geometry["coordinates"]]
        elif geometry["type"] == "MultiPolygon":
            polygons = geometry["coordinates"]
        else:
            raise ValueError(f"Unsupported geometry type: {geometry['type']}")

        for polygon_index, polygon in enumerate(polygons, start=1):
            for ring_index, ring in enumerate(polygon, start=1):
                if len(ring) < 4:
                    raise ValueError(f"Boundary ring is too short for {county_fips}")
                if ring[0] != ring[-1]:
                    ring = [*ring, ring[0]]
                group = f"{county_fips}-{polygon_index}-{ring_index}"
                for point_index, (longitude, latitude) in enumerate(ring, start=1):
                    rows.append(
                        {
                            "county_fips": county_fips,
                            "county_name": properties["NAME"],
                            "polygon_group": group,
                            "point_order": point_index,
                            "longitude": f"{longitude:.6f}",
                            "latitude": f"{latitude:.6f}",
                        }
                    )

    fields = ["county_fips", "county_name", "polygon_group", "point_order", "longitude", "latitude"]
    write_csv(output_path, fields, rows)
    return feature_fips


def build_teaching_table(
    places: dict[str, dict[str, dict[str, str]]],
    acs: dict[str, dict[str, object]],
    boundary_fips: set[str],
    output_path: Path,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    nc_fips = sorted(fips for fips, types in places.items() if types["CrdPrv"]["stateabbr"] == "NC")
    if len(nc_fips) != 100 or set(nc_fips) != boundary_fips:
        raise ValueError("North Carolina PLACES and TIGERweb county sets do not match")

    for fips in nc_fips:
        crude = places[fips]["CrdPrv"]
        adjusted = places[fips]["AgeAdjPrv"]
        acs_row = acs.get(fips)
        if acs_row is None:
            raise ValueError(f"ACS county missing for {fips}")
        places_adults = as_int(crude["totalpop18plus"], "totalpop18plus")
        crude_value = as_float(crude["data_value"], "crude prevalence")
        acs_adults = int(acs_row["acs_adult_population"])
        footnote = " ".join(
            value.strip()
            for value in (crude["data_value_footnote_symbol"], crude["data_value_footnote"])
            if value.strip()
        )
        rows.append(
            {
                "county_fips": fips,
                "state_abbr": crude["stateabbr"],
                "state_name": crude["statedesc"],
                "county_name": crude["locationname"],
                "measure_id": crude["measureid"],
                "measure_name": crude["measure"],
                "measure_year": as_int(crude["year"], "year"),
                "release_label": "PLACES 2024 release",
                "places_total_population": as_int(crude["totalpopulation"], "totalpopulation"),
                "places_adult_population": places_adults,
                "crude_prevalence_pct": f"{crude_value:.1f}",
                "crude_low_95_pct": f"{as_float(crude['low_confidence_limit'], 'crude lower limit'):.1f}",
                "crude_high_95_pct": f"{as_float(crude['high_confidence_limit'], 'crude upper limit'):.1f}",
                "age_adjusted_prevalence_pct": f"{as_float(adjusted['data_value'], 'adjusted prevalence'):.1f}",
                "age_adjusted_low_95_pct": f"{as_float(adjusted['low_confidence_limit'], 'adjusted lower limit'):.1f}",
                "age_adjusted_high_95_pct": f"{as_float(adjusted['high_confidence_limit'], 'adjusted upper limit'):.1f}",
                "modeled_adult_count": round(crude_value / 100 * places_adults),
                "count_status": "modeled estimate, not observed cases",
                "acs_adult_population": acs_adults,
                "acs_adult_moe90": acs_row["acs_adult_moe90"],
                "acs_65plus_population": acs_row["acs_65plus_population"],
                "acs_65plus_moe90": acs_row["acs_65plus_moe90"],
                "acs_65plus_share_adult_pct": acs_row["acs_65plus_share_adult_pct"],
                "acs_moe_status": acs_row["acs_moe_status"],
                "adult_population_difference_pct": f"{100 * (acs_adults - places_adults) / places_adults:.1f}",
                "teaching_low_denominator_flag": int(places_adults < 10000),
                "source_footnote": footnote,
            }
        )

    fields = list(rows[0])
    write_csv(output_path, fields, rows)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cdc-input", type=Path)
    parser.add_argument("--acs-input", type=Path)
    parser.add_argument("--tiger-input", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "data")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="oclc-module05-") as temporary:
        temp = Path(temporary)
        sources = {
            "cdc": args.cdc_input or temp / "places.csv",
            "acs": args.acs_input or temp / "b01001.dat",
            "tiger": args.tiger_input or temp / "counties.geojson",
        }
        for label, url in (("cdc", CDC_URL), ("acs", ACS_URL), ("tiger", TIGER_URL)):
            if not sources[label].exists():
                print(f"Downloading {label}: {url}")
                download(url, sources[label])
            validate_raw(label, sources[label])

        output = args.output_dir
        output.mkdir(parents=True, exist_ok=True)
        _, places = build_places(sources["cdc"], output / "places_diabetes_county_2024.csv")
        acs = build_acs(sources["acs"], output / "acs_adult_population_county_2024.csv")
        boundaries = build_boundaries(sources["tiger"], output / "nc_county_boundaries_2024.csv")
        teaching = build_teaching_table(places, acs, boundaries, output / "nc_diabetes_rates_2024.csv")

    print(f"Built {len(teaching):,} North Carolina county rows in {args.output_dir.resolve()}")
    for path in sorted(args.output_dir.glob("*.csv")):
        print(f"{path.name}: {sum(1 for _ in path.open(encoding='utf-8')) - 1:,} rows; sha256={sha256(path)}")


if __name__ == "__main__":
    main()

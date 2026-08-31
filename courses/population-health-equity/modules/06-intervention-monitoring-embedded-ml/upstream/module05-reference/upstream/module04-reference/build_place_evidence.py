"""Build and independently verify APP-5 Module 04 place evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import sqlite3
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


os.environ.setdefault("SOURCE_DATE_EPOCH", "0")
import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["font.family"] = "DejaVu Sans"
matplotlib.rcParams["svg.fonttype"] = "none"
matplotlib.rcParams["svg.hashsalt"] = "oclc-app5-04"
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


ROOT = Path(__file__).resolve().parent
SOURCE_ARCHIVE = "data/raw/tl_2024_25_tract.zip"
SOURCE_MANIFEST = "data/source-manifest.csv"
PLACES_SOURCE = "upstream/checkpoint-reference/candidate/module-02/outputs/public-modeled-prevalence.csv"
LINKAGE_SOURCE = "upstream/checkpoint-reference/candidate/module-02/outputs/tract-linkage-audit.csv"
SQL_FILES = (
    "01-link-geometry-and-measures.sql",
    "02-compare-tract-and-county-aggregation.sql",
    "03-audit-map-release.sql",
)
OUTPUT_TABLES = {
    "geometry-audit.csv": "raw_geometry",
    "geometry-join-audit.csv": "geometry_join_audit",
    "tract-map-table.csv": "tract_map_table",
    "small-area-stability.csv": "small_area_stability",
    "county-aggregation.csv": "county_aggregation",
    "aggregation-comparison.csv": "aggregation_comparison",
    "map-class-summary.csv": "map_class_summary",
    "query-checks.csv": "query_checks",
}
CLASS_ORDER = (
    "less than 5.0%",
    "5.0% to less than 10.0%",
    "10.0% to less than 15.0%",
    "15.0% to less than 20.0%",
    "20.0% or greater",
    "unavailable",
)
CLASS_COLORS = {
    "less than 5.0%": "#f7fbff",
    "5.0% to less than 10.0%": "#c6dbef",
    "10.0% to less than 15.0%": "#6baed6",
    "15.0% to less than 20.0%": "#2171b5",
    "20.0% or greater": "#08306b",
    "unavailable": "#bdbdbd",
}
EXPECTED_SOURCE_SHA256 = "74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4"


class BuildError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BuildError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def format_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.10f}".rstrip("0").rstrip(".")
    return str(value)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def load_csv_table(connection: sqlite3.Connection, table: str, path: Path) -> tuple[int, int]:
    fields, rows = read_csv(path)
    require(fields and len(fields) == len(set(fields)), f"Invalid source fields in {path.name}")
    connection.execute(f'DROP TABLE IF EXISTS "{table}"')
    connection.execute(
        f'CREATE TABLE "{table}" ({", ".join(f"\"{field}\" TEXT" for field in fields)})'
    )
    placeholders = ", ".join("?" for _ in fields)
    connection.executemany(
        f'INSERT INTO "{table}" VALUES ({placeholders})',
        [[row[field] for field in fields] for row in rows],
    )
    return len(rows), len(fields)


def load_dict_table(
    connection: sqlite3.Connection, table: str, fields: list[str], rows: list[dict[str, object]]
) -> tuple[int, int]:
    connection.execute(f'DROP TABLE IF EXISTS "{table}"')
    connection.execute(
        f'CREATE TABLE "{table}" ({", ".join(f"\"{field}\" TEXT" for field in fields)})'
    )
    placeholders = ", ".join("?" for _ in fields)
    connection.executemany(
        f'INSERT INTO "{table}" VALUES ({placeholders})',
        [[format_value(row[field]) for field in fields] for row in rows],
    )
    return len(rows), len(fields)


def load_geometry(root: Path) -> tuple[gpd.GeoDataFrame, list[dict[str, object]], dict[str, object]]:
    archive = root / SOURCE_ARCHIVE
    require(archive.is_file(), "TIGER source archive is missing")
    require(archive.stat().st_size == 4_506_627, "TIGER source byte count changed")
    require(sha256(archive) == EXPECTED_SOURCE_SHA256, "TIGER source SHA-256 changed")
    source_uri = f"zip://{archive.resolve().as_posix()}"
    geometry = gpd.read_file(source_uri).sort_values("GEOID").reset_index(drop=True)
    required_fields = {
        "STATEFP", "COUNTYFP", "TRACTCE", "GEOID", "NAME", "ALAND", "AWATER", "geometry"
    }
    require(required_fields.issubset(geometry.columns), "TIGER geometry fields changed")
    require(len(geometry) == 1620, "TIGER tract row count changed")
    require(geometry["GEOID"].nunique() == 1620, "TIGER tract keys are not unique")
    require(set(geometry["STATEFP"].astype(str)) == {"25"}, "TIGER state identity changed")
    require(geometry["COUNTYFP"].astype(str).nunique() == 14, "TIGER county count changed")
    require(geometry.crs is not None and geometry.crs.to_epsg() == 4269, "TIGER source CRS changed")
    require(int(geometry.geometry.isna().sum()) == 0, "TIGER contains null geometry")
    require(int(geometry.geometry.is_empty.sum()) == 0, "TIGER contains empty geometry")
    require(int(geometry.geometry.is_valid.sum()) == 1620, "TIGER contains invalid geometry")
    type_counts = geometry.geometry.geom_type.value_counts().to_dict()
    require(type_counts == {"Polygon": 1617, "MultiPolygon": 3}, "TIGER geometry types changed")

    projected = geometry.to_crs(epsg=26986)
    projected_area = projected.geometry.area
    source_area = geometry["ALAND"].astype(float) + geometry["AWATER"].astype(float)
    relative_difference = (projected_area - source_area).abs() / source_area
    require(float(relative_difference.max()) < 0.001, "Projected geometry area check failed")

    rows: list[dict[str, object]] = []
    for position, source in geometry.iterrows():
        rows.append(
            {
                "tract_fips": str(source["GEOID"]),
                "state_fips": str(source["STATEFP"]),
                "county_fips": f"{source['STATEFP']}{source['COUNTYFP']}",
                "tract_code": str(source["TRACTCE"]),
                "tract_name": str(source["NAME"]),
                "geometry_type": source.geometry.geom_type,
                "is_valid": int(source.geometry.is_valid),
                "is_empty": int(source.geometry.is_empty),
                "is_null": int(source.geometry is None),
                "aland_sq_m": int(source["ALAND"]),
                "awater_sq_m": int(source["AWATER"]),
                "projected_area_sq_m": float(projected_area.iloc[position]),
                "area_relative_difference": float(relative_difference.iloc[position]),
            }
        )
    facts = {
        "rows": len(geometry),
        "unique_tracts": int(geometry["GEOID"].nunique()),
        "counties": int(geometry["COUNTYFP"].nunique()),
        "source_crs_epsg": 4269,
        "projected_crs_epsg": 26986,
        "polygon_rows": int(type_counts["Polygon"]),
        "multipolygon_rows": int(type_counts["MultiPolygon"]),
        "valid_rows": int(geometry.geometry.is_valid.sum()),
        "empty_rows": int(geometry.geometry.is_empty.sum()),
        "null_rows": int(geometry.geometry.isna().sum()),
        "aland_sq_m": int(geometry["ALAND"].sum()),
        "awater_sq_m": int(geometry["AWATER"].sum()),
        "maximum_area_relative_difference": float(relative_difference.max()),
        "bounds": [float(value) for value in geometry.total_bounds],
    }
    return geometry, rows, facts


def execute_sql(connection: sqlite3.Connection, sql_root: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for filename in SQL_FILES:
        path = sql_root / filename
        require(path.is_file(), f"SQL file is missing: {filename}")
        text = path.read_text(encoding="utf-8")
        require("REPLACE" not in text, f"SQL file is incomplete: {filename}")
        connection.executescript(text)
        hashes[filename] = sha256(path)
    return hashes


def query_csv(connection: sqlite3.Connection, table: str) -> tuple[bytes, int, int]:
    cursor = connection.execute(f'SELECT * FROM "{table}"')
    fields = [description[0] for description in cursor.description or []]
    rows = cursor.fetchall()
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(fields)
    writer.writerows([[format_value(value) for value in row] for row in rows])
    return output.getvalue().encode("utf-8"), len(rows), len(fields)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows([{field: format_value(row[field]) for field in fields} for row in rows])


def source_profile(root: Path, geometry_facts: dict[str, object]) -> tuple[list[str], list[dict[str, object]]]:
    fields = [
        "source_id", "source_url", "archive_bytes", "archive_sha256", "archive_members",
        "tract_rows", "unique_tracts", "state_fips", "county_count", "source_crs_epsg",
        "projected_check_crs_epsg", "valid_geometry_rows", "null_geometry_rows",
        "empty_geometry_rows", "maximum_area_relative_difference", "source_role", "claim_limit",
    ]
    manifest = root / SOURCE_MANIFEST
    require(manifest.is_file(), "Source manifest is missing")
    _, manifest_rows = read_csv(manifest)
    require(len(manifest_rows) == 8, "Source manifest row count changed")
    rows = [
        {
            "source_id": "TIGER2024-MA-TRACT",
            "source_url": "https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_25_tract.zip",
            "archive_bytes": 4_506_627,
            "archive_sha256": EXPECTED_SOURCE_SHA256,
            "archive_members": 7,
            "tract_rows": geometry_facts["rows"],
            "unique_tracts": geometry_facts["unique_tracts"],
            "state_fips": "25",
            "county_count": geometry_facts["counties"],
            "source_crs_epsg": geometry_facts["source_crs_epsg"],
            "projected_check_crs_epsg": geometry_facts["projected_crs_epsg"],
            "valid_geometry_rows": geometry_facts["valid_rows"],
            "null_geometry_rows": geometry_facts["null_rows"],
            "empty_geometry_rows": geometry_facts["empty_rows"],
            "maximum_area_relative_difference": geometry_facts["maximum_area_relative_difference"],
            "source_role": "complete official boundary geometry and tract keys",
            "claim_limit": "boundaries do not define community identity, service access, priority, eligibility, or authority to act",
        }
    ]
    return fields, rows


def make_accessible_map(
    path: Path,
    geometry: gpd.GeoDataFrame,
    map_rows: list[dict[str, str]],
    class_counts: dict[str, int],
    limited_support: int,
) -> None:
    by_tract = {row["tract_fips"]: row for row in map_rows}
    mapped = geometry.copy()
    mapped["map_class"] = [by_tract[str(value)]["map_class"] for value in mapped["GEOID"]]
    mapped["support_state"] = [by_tract[str(value)]["support_state"] for value in mapped["GEOID"]]
    mapped = mapped.to_crs(epsg=26986)
    mapped.geometry = mapped.geometry.simplify(100, preserve_topology=True)

    fig, axis = plt.subplots(figsize=(10.0, 8.2))
    for map_class in CLASS_ORDER:
        subset = mapped[mapped["map_class"] == map_class]
        if not subset.empty:
            subset.plot(
                ax=axis,
                color=CLASS_COLORS[map_class],
                edgecolor="#ffffff",
                linewidth=0.16,
            )
    limited = mapped[mapped["support_state"] == "limited_support_review"]
    if not limited.empty:
        limited.plot(
            ax=axis,
            color="none",
            edgecolor="#202020",
            linewidth=0.22,
            hatch="////",
        )
    counties = mapped.dissolve(by="COUNTYFP")
    counties.boundary.plot(ax=axis, color="#202020", linewidth=0.7)
    axis.set_axis_off()
    axis.set_title(
        "Modeled diabetes prevalence by Massachusetts census tract",
        loc="left",
        fontsize=15,
        fontweight="bold",
        pad=12,
    )
    legend = [
        Patch(facecolor=CLASS_COLORS[map_class], edgecolor="#666666", label=f"{map_class} ({class_counts[map_class]})")
        for map_class in CLASS_ORDER
    ]
    legend.append(
        Patch(facecolor="white", edgecolor="#202020", hatch="////", label=f"Classroom limited-support review ({limited_support})")
    )
    axis.legend(
        handles=legend,
        title="CDC PLACES modeled crude prevalence",
        loc="lower left",
        frameon=True,
        fontsize=8,
        title_fontsize=9,
    )
    fig.text(
        0.02,
        0.025,
        "Measure year 2023, CDC PLACES 2025 tract release. Absolute classes, not ranks. "
        "Gray means unavailable. Hatching marks a classroom review trigger, not a CDC quality label.",
        fontsize=8,
        ha="left",
    )
    fig.text(
        0.02,
        0.006,
        "Public modeled estimates are not observed cases, individual risk, a disparity finding, or an action rule. "
        "See the complete exact table and text alternative.",
        fontsize=8,
        ha="left",
    )
    fig.savefig(
        path,
        format="svg",
        bbox_inches="tight",
        metadata={"Date": None, "Creator": "Open Clinical Learning Commons"},
    )
    plt.close(fig)

    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    tree = ET.parse(path)
    root = tree.getroot()
    root.set("role", "img")
    root.set("aria-labelledby", "map-title map-desc")
    root.set("focusable", "false")
    title = ET.Element(f"{{{namespace}}}title", {"id": "map-title"})
    title.text = "Modeled diabetes prevalence by Massachusetts census tract"
    description = ET.Element(f"{{{namespace}}}desc", {"id": "map-desc"})
    description.text = (
        f"A source-labeled teaching map of all 1,620 Massachusetts census tracts. "
        f"The map displays 1,597 CDC PLACES modeled crude diabetes prevalence estimates in five absolute classes, "
        f"retains 23 tracts as unavailable, and hatches {limited_support} tracts for classroom support review. "
        "The map does not rank, target, or assign eligibility to any tract. A complete exact table and text alternative accompany it."
    )
    root.insert(0, description)
    root.insert(0, title)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def inspect_svg(path: Path) -> dict[str, object]:
    tree = ET.parse(path)
    root = tree.getroot()
    text = path.read_text(encoding="utf-8")
    require(root.attrib.get("role") == "img", "SVG image role is missing")
    require(root.attrib.get("aria-labelledby") == "map-title map-desc", "SVG label relationship is missing")
    require('id="map-title"' in text and 'id="map-desc"' in text, "SVG title or description is missing")
    require("<image" not in text, "SVG contains an embedded raster image")
    require("Absolute classes, not ranks" in text, "SVG source and class note is missing")
    return {
        "role": root.attrib.get("role"),
        "aria_labelledby": root.attrib.get("aria-labelledby"),
        "has_title": 'id="map-title"' in text,
        "has_description": 'id="map-desc"' in text,
        "contains_raster": "<image" in text,
    }


def build(root: Path, output: Path) -> dict[str, object]:
    root = root.resolve()
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {output}")
    output.mkdir(parents=True)

    geometry, geometry_rows, geometry_facts = load_geometry(root)
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")
    geometry_fields = list(geometry_rows[0])
    loaded = {
        "raw_geometry": dict(zip(("rows", "columns"), load_dict_table(connection, "raw_geometry", geometry_fields, geometry_rows))),
    }
    places_path = root / PLACES_SOURCE
    linkage_path = root / LINKAGE_SOURCE
    require(places_path.is_file() and linkage_path.is_file(), "Accepted checkpoint measure evidence is missing")
    loaded["raw_places"] = dict(zip(("rows", "columns"), load_csv_table(connection, "raw_places", places_path)))
    loaded["raw_linkage_audit"] = dict(zip(("rows", "columns"), load_csv_table(connection, "raw_linkage_audit", linkage_path)))
    require(loaded["raw_places"]["rows"] == 1597, "Accepted PLACES row count changed")
    require(loaded["raw_linkage_audit"]["rows"] == 1620, "Accepted linkage audit row count changed")
    sql_root = root / "reference/sql" if (root / "reference/sql").is_dir() else root / "sql"
    sql_hashes = execute_sql(connection, sql_root)

    output_meta: dict[str, dict[str, object]] = {}
    source_fields, source_rows = source_profile(root, geometry_facts)
    source_path = output / "source-profile.csv"
    write_csv(source_path, source_fields, source_rows)
    output_meta[source_path.name] = {
        "rows": 1,
        "columns": len(source_fields),
        "bytes": source_path.stat().st_size,
        "sha256": sha256(source_path),
    }
    for filename, table in OUTPUT_TABLES.items():
        payload, rows, columns = query_csv(connection, table)
        path = output / filename
        path.write_bytes(payload)
        output_meta[filename] = {
            "rows": rows,
            "columns": columns,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }

    _, map_rows = read_csv(output / "tract-map-table.csv")
    _, class_rows = read_csv(output / "map-class-summary.csv")
    class_counts = {row["map_class"]: int(row["tract_count"]) for row in class_rows}
    require(tuple(class_counts) == CLASS_ORDER, "Map class order changed")
    require(sum(class_counts.values()) == 1620, "Map classes do not reconcile to geometry")
    limited_support = sum(row["support_state"] == "limited_support_review" for row in map_rows)
    supported = sum(row["support_state"] == "supported_for_teaching_display" for row in map_rows)
    unavailable = sum(row["support_state"] == "unavailable" for row in map_rows)
    require(limited_support > 0 and supported > 0 and unavailable == 23, "Map support states changed")
    map_path = output / "responsible-diabetes-prevalence-map.svg"
    make_accessible_map(map_path, geometry, map_rows, class_counts, limited_support)
    svg_facts = inspect_svg(map_path)
    output_meta[map_path.name] = {
        "rows": 1,
        "columns": 1,
        "bytes": map_path.stat().st_size,
        "sha256": sha256(map_path),
    }

    _, county_rows = read_csv(output / "county-aggregation.csv")
    _, comparison_rows = read_csv(output / "aggregation-comparison.csv")
    changed_classes = sum(int(row["class_changes_after_aggregation"]) for row in comparison_rows)
    map_facts = {
        "title": "Modeled diabetes prevalence by Massachusetts census tract",
        "source": "CDC PLACES 2025 census-tract release; measure year 2023; TIGER/Line 2024 Massachusetts tracts",
        "measure": "modeled crude diabetes prevalence percent",
        "geometry_tracts": 1620,
        "mapped_estimates": 1597,
        "unavailable_tracts": unavailable,
        "limited_support_review_tracts": limited_support,
        "supported_display_tracts": supported,
        "absolute_class_counts": class_counts,
        "county_teaching_summaries": len(county_rows),
        "tracts_changing_class_after_county_aggregation": changed_classes,
        "reading_order": [
            "Read the source, measure year, and modeled-estimate label.",
            "Use the five absolute legend classes; gray means unavailable.",
            "Treat hatching as a classroom review flag and read the exact interval and population field.",
            "Use the complete tract table for exact values and unavailable states.",
            "Do not infer individual risk, community need, priority, eligibility, or an action rule from the map.",
        ],
        "claim_limit": "teaching display only; no observed cases, individual inference, disparity finding, rank, target, eligibility, allocation, intervention, or deployment",
    }
    facts_path = output / "map-text-facts.json"
    facts_path.write_text(json.dumps(map_facts, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_meta[facts_path.name] = {
        "rows": 1,
        "columns": len(map_facts),
        "bytes": facts_path.stat().st_size,
        "sha256": sha256(facts_path),
    }

    checks = connection.execute("SELECT check_id, status FROM query_checks ORDER BY check_id").fetchall()
    require(len(checks) == 32 and all(status == "pass" for _, status in checks), "One or more SQL checks failed")
    report = {
        "schema_version": "1.0.0",
        "module_id": "oclc-app5-04",
        "module_version": "0.1.0",
        "commons_release": "0.91.0",
        "source_release": "TIGER2024-MA-TRACT",
        "source": {
            "archive_bytes": (root / SOURCE_ARCHIVE).stat().st_size,
            "archive_sha256": sha256(root / SOURCE_ARCHIVE),
            "source_manifest_sha256": sha256(root / SOURCE_MANIFEST),
        },
        "upstream": {
            "checkpoint_id": "oclc-app5-cp01",
            "checkpoint_version": "0.1.0",
            "handoff_manifest_sha256": sha256(root / "upstream/checkpoint-handoff-manifest.csv"),
            "reference_files": 240,
            "candidate_files": 219,
        },
        "loaded": loaded,
        "geometry": geometry_facts,
        "display": {
            "crs_epsg": 26986,
            "topology_preserving_simplification_meters": 100
        },
        "findings": {
            "mapped_estimates": 1597,
            "geometry_only_unavailable": unavailable,
            "retained_places_population": sum(int(row["places_adult_population_field"] or 0) for row in map_rows),
            "minimum_modeled_prevalence_percent": min(float(row["modeled_crude_prevalence_percent"]) for row in map_rows if row["modeled_crude_prevalence_percent"]),
            "maximum_modeled_prevalence_percent": max(float(row["modeled_crude_prevalence_percent"]) for row in map_rows if row["modeled_crude_prevalence_percent"]),
            "limited_support_review_tracts": limited_support,
            "supported_display_tracts": supported,
            "county_teaching_summaries": len(county_rows),
            "tracts_changing_class_after_county_aggregation": changed_classes,
            "map_class_counts": class_counts,
            "query_checks": len(checks),
            "failed_query_checks": 0,
        },
        "accessibility": svg_facts,
        "sql_sha256": sql_hashes,
        "outputs": output_meta,
        "interpretation_status": "responsible public teaching map only; no observed-case, individual-risk, disparity, priority, rank, target, eligibility, outreach, allocation, intervention, implementation, or deployment conclusion",
    }
    report_path = output / "build-report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    connection.close()
    return report


def compare_outputs(left: Path, right: Path) -> None:
    left_files = {path.relative_to(left).as_posix(): sha256(path) for path in left.rglob("*") if path.is_file()}
    right_files = {path.relative_to(right).as_posix(): sha256(path) for path in right.rglob("*") if path.is_file()}
    require(left_files == right_files, "Two place-evidence builds differ")


def verify(root: Path = ROOT) -> dict[str, object]:
    committed = root / "outputs"
    require(committed.is_dir(), "Committed outputs are missing")
    with tempfile.TemporaryDirectory(prefix="app5-module04-verify-") as temporary:
        generated = Path(temporary) / "outputs"
        report = build(root, generated)
        compare_outputs(committed, generated)
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module04-build-") as temporary:
        base = Path(temporary)
        first = base / "first"
        second = base / "second"
        report = build(ROOT, first)
        build(ROOT, second)
        compare_outputs(first, second)
        require(report["findings"]["mapped_estimates"] == 1597, "Mapped estimate count changed")
        require(report["findings"]["geometry_only_unavailable"] == 23, "Unavailable tract count changed")
        require(report["findings"]["query_checks"] == 32, "Query check count changed")
        try:
            build(ROOT, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Place-evidence builder overwrote an existing target")
    committed = verify(ROOT)
    print(
        "APP-5 Module 04 place-evidence self-check passed: "
        f"{committed['geometry']['rows']} geometry tracts, "
        f"{committed['findings']['mapped_estimates']} mapped estimates, and "
        f"{committed['findings']['query_checks']} query checks."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.verify:
            print(json.dumps(verify(ROOT), indent=2, sort_keys=True))
        elif args.write:
            print(json.dumps(build(ROOT, args.output or (ROOT / "outputs")), indent=2, sort_keys=True))
        elif args.output:
            print(json.dumps(build(ROOT, args.output), indent=2, sort_keys=True))
        else:
            parser.error("use --write, --verify, --self-check, or provide --output")
    except (OSError, ValueError, KeyError, sqlite3.Error, ET.ParseError, BuildError) as error:
        parser.exit(1, f"Place-evidence build failed: {error}\n")


if __name__ == "__main__":
    main()

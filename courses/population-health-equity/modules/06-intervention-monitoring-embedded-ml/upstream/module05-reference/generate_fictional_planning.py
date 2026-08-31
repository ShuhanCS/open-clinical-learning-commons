"""Generate and verify the APP-5 Module 05 fictional planning release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "0.1.0"
SOURCE_ID = "fma-dp-01-fictional-planning-v1"
SEED = 73055
EXPECTED_FILES: dict[str, dict[str, object]] = {
    "data-dictionary.csv": {"bytes": 7974, "sha256": "1f60c44182b65ce6a9a1a5d6def9889fbdf72bedf4de8ac4efbf633d30d24a0d"},
    "raw/fictional-planning-layer.csv.gz": {"bytes": 16517, "sha256": "b9ce228fc824ec7c62bbede5fcd8459722b328fc39fa5215036c6e924f562aed"},
    "rule-definitions.csv": {"bytes": 1937, "sha256": "9f5aac5394f07fd7498a342f3dbaec059ff7e671b8ebd05688393f2192cf5849"},
    "sensitivity-variants.csv": {"bytes": 2465, "sha256": "345f9290766b334be792fe8ec567021a2759f8330ff637b3f1e6a4d9879bd90b"},
    "synthetic-source-manifest.csv": {"bytes": 1560, "sha256": "a9a9cd10e67164cd8c47df667f2e559f17f8baa0e2308740ce4c9d9e675c0319"},
}

PLANNING_FIELDS = [
    "scenario_id",
    "synthetic_source_id",
    "tract_fips",
    "county_fips",
    "fictional_capacity_places",
    "fictional_travel_minutes",
    "fictional_staff_readiness",
    "fictional_language_access_ready",
    "fictional_disability_access_ready",
    "fictional_community_review_state",
    "fictional_unresolved_questions",
    "fictional_objection_state",
    "fictional_delivery_burden_score",
    "accountable_owner",
    "generator_version",
    "seed",
    "synthetic_flag",
    "claim_limit",
]
RULE_FIELDS = [
    "rule_id",
    "rule_name",
    "fairness_definition",
    "candidate_filter",
    "selection_order",
    "tie_breaker",
    "award_places",
    "base_awards",
    "resource_places",
    "automatic_action",
    "interpretation_limit",
]
SENSITIVITY_FIELDS = [
    "variant_id",
    "rule_id",
    "variant_type",
    "award_count",
    "parameter",
    "parameter_value",
    "reason",
]
DICTIONARY_FIELDS = [
    "source_id",
    "field_order",
    "field_name",
    "type",
    "nullable",
    "definition",
    "claim_limit",
]
MANIFEST_FIELDS = [
    "source_id",
    "relative_path",
    "format",
    "rows",
    "columns",
    "bytes",
    "sha256",
    "content_bytes",
    "content_sha256",
    "generator_version",
    "seed",
    "synthetic_flag",
    "claim_limit",
]


class SourceError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def csv_bytes(fields: list[str], rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def deterministic_gzip(raw: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
        zipped.write(raw)
    return output.getvalue()


def stable_int(*parts: object) -> int:
    value = "|".join(str(part) for part in (SEED, *parts))
    return int(hashlib.sha256(value.encode("utf-8")).hexdigest()[:16], 16)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def load_accepted_tracts(root: Path) -> list[dict[str, str]]:
    path = root / "upstream/module04-reference/outputs/tract-map-table.csv"
    fields, rows = read_csv(path)
    require(fields[:3] == ["tract_fips", "county_fips", "county_name"], "Accepted tract table schema changed")
    accepted = [row for row in rows if row["modeled_crude_prevalence_percent"]]
    require(len(rows) == 1620 and len(accepted) == 1597, "Accepted tract universe changed")
    require(len({row["tract_fips"] for row in accepted}) == 1597, "Accepted tract keys are not unique")
    require(
        {row["source_release"] for row in accepted} == {"CDC PLACES 2025 census-tract release"},
        "Accepted public source identity changed",
    )
    return sorted(accepted, key=lambda row: row["tract_fips"])


def planning_rows(tracts: list[dict[str, str]]) -> list[dict[str, object]]:
    capacity_values = (0, 10, 20, 30, 40)
    staff_values = ("ready", "ready", "ready", "conditional", "not_ready")
    community_values = (
        "ready_for_planning_review",
        "ready_for_planning_review",
        "ready_for_planning_review",
        "needs_revision",
        "not_reviewed",
    )
    rows: list[dict[str, object]] = []
    for tract in tracts:
        key = tract["tract_fips"]
        rows.append(
            {
                "scenario_id": "FMA-DP-01",
                "synthetic_source_id": SOURCE_ID,
                "tract_fips": key,
                "county_fips": tract["county_fips"],
                "fictional_capacity_places": capacity_values[stable_int(key, "capacity") % len(capacity_values)],
                "fictional_travel_minutes": 10 + stable_int(key, "travel") % 66,
                "fictional_staff_readiness": staff_values[stable_int(key, "staff") % len(staff_values)],
                "fictional_language_access_ready": int(stable_int(key, "language") % 100 < 76),
                "fictional_disability_access_ready": int(stable_int(key, "disability") % 100 < 79),
                "fictional_community_review_state": community_values[stable_int(key, "community") % len(community_values)],
                "fictional_unresolved_questions": stable_int(key, "questions") % 4,
                "fictional_objection_state": "unresolved_objection" if stable_int(key, "objection") % 100 < 8 else "no_recorded_objection",
                "fictional_delivery_burden_score": 1 + stable_int(key, "burden") % 5,
                "accountable_owner": "FMA-DP-01 fictional resource-allocation owner",
                "generator_version": GENERATOR_VERSION,
                "seed": SEED,
                "synthetic_flag": 1,
                "claim_limit": "fictional tract-linked teaching condition; not community fact, consent, need, eligibility, outreach, funding, allocation, service, or authority",
            }
        )
    require(len(rows) == 1597, "Fictional planning row count changed")
    require(all(row["synthetic_flag"] == 1 for row in rows), "Synthetic flag changed")
    return rows


def rule_rows() -> list[dict[str, object]]:
    common_limit = "fictional classroom comparator only; no automatic or real eligibility, outreach, funding, allocation, service, or authority"
    return [
        {
            "rule_id": "equal_geographic",
            "rule_name": "Equal geographic rule",
            "fairness_definition": "equal geographic representation with two teaching awards in each of 14 counties",
            "candidate_filter": "all 1597 accepted measure tracts",
            "selection_order": "source-independent stable teaching tie breaker within county",
            "tie_breaker": "SHA-256 of rule ID, seed, and tract key",
            "award_places": 10,
            "base_awards": 28,
            "resource_places": 280,
            "automatic_action": 0,
            "interpretation_limit": common_limit,
        },
        {
            "rule_id": "need_based",
            "rule_name": "Need-based rule",
            "fairness_definition": "greater fictional attention to higher accepted modeled area-level prevalence",
            "candidate_filter": "all 1597 accepted estimates with limited-support rows retained and labeled",
            "selection_order": "modeled prevalence descending, interval width ascending, stable tie breaker",
            "tie_breaker": "SHA-256 of rule ID, seed, and tract key",
            "award_places": 10,
            "base_awards": 28,
            "resource_places": 280,
            "automatic_action": 0,
            "interpretation_limit": common_limit,
        },
        {
            "rule_id": "capacity_aware",
            "rule_name": "Capacity-aware rule",
            "fairness_definition": "feasible fictional delivery under the fixed resource constraint",
            "candidate_filter": "fictional capacity of at least 10 places",
            "selection_order": "capacity, staff readiness, access readiness, burden, and stable tie breaker",
            "tie_breaker": "SHA-256 of rule ID, seed, and tract key",
            "award_places": 10,
            "base_awards": 28,
            "resource_places": 280,
            "automatic_action": 0,
            "interpretation_limit": common_limit,
        },
        {
            "rule_id": "community_review",
            "rule_name": "Community-review rule",
            "fairness_definition": "procedural readiness with fictional review, access, objection, recourse, and county concentration limits",
            "candidate_filter": "ready review, no unresolved objection, both access plans ready, capacity of at least 10 places",
            "selection_order": "unresolved questions, burden, capacity, modeled context, and stable tie breaker with no more than three awards per county",
            "tie_breaker": "SHA-256 of rule ID, seed, and tract key",
            "award_places": 10,
            "base_awards": 28,
            "resource_places": 280,
            "automatic_action": 0,
            "interpretation_limit": common_limit,
        },
    ]


def sensitivity_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for rule_id in ("equal_geographic", "need_based", "capacity_aware", "community_review"):
        rows.extend(
            [
                {"variant_id": f"{rule_id}-base", "rule_id": rule_id, "variant_type": "base", "award_count": 28, "parameter": "base contract", "parameter_value": "declared", "reason": "reference comparison"},
                {"variant_id": f"{rule_id}-half-resource", "rule_id": rule_id, "variant_type": "resource", "award_count": 14, "parameter": "fictional resource places", "parameter_value": "140", "reason": "test lower resource availability"},
                {"variant_id": f"{rule_id}-expanded-resource", "rule_id": rule_id, "variant_type": "resource", "award_count": 42, "parameter": "fictional resource places", "parameter_value": "420", "reason": "test higher resource availability"},
            ]
        )
    rows.extend(
        [
            {"variant_id": "equal-geographic-reverse-tie", "rule_id": "equal_geographic", "variant_type": "tie_break", "award_count": 28, "parameter": "stable tie direction", "parameter_value": "reverse", "reason": "test arbitrary tie-break dependence"},
            {"variant_id": "equal-geographic-no-county-quota", "rule_id": "equal_geographic", "variant_type": "county_limit", "award_count": 28, "parameter": "county quota", "parameter_value": "none", "reason": "expose geographic concentration without equal representation"},
            {"variant_id": "need-based-lower-bound", "rule_id": "need_based", "variant_type": "uncertainty", "award_count": 28, "parameter": "need criterion", "parameter_value": "modeled lower confidence limit", "reason": "test interval-aware ordering"},
            {"variant_id": "need-based-supported-only", "rule_id": "need_based", "variant_type": "support", "award_count": 28, "parameter": "support state", "parameter_value": "supported_for_teaching_display only", "reason": "test handling of the classroom support flag"},
            {"variant_id": "capacity-access-ready", "rule_id": "capacity_aware", "variant_type": "access", "award_count": 28, "parameter": "access readiness", "parameter_value": "language and disability plans required", "reason": "test access as an entry condition"},
            {"variant_id": "capacity-minimum-20", "rule_id": "capacity_aware", "variant_type": "capacity", "award_count": 28, "parameter": "minimum fictional capacity", "parameter_value": "20", "reason": "test a stricter capacity threshold"},
            {"variant_id": "community-include-revision", "rule_id": "community_review", "variant_type": "community_readiness", "award_count": 28, "parameter": "review state", "parameter_value": "ready or needs_revision", "reason": "test whether revision status changes selection"},
            {"variant_id": "community-max-two-county", "rule_id": "community_review", "variant_type": "county_limit", "award_count": 28, "parameter": "maximum awards per county", "parameter_value": "2", "reason": "test a stricter geographic concentration limit"},
        ]
    )
    return rows


def dictionary_rows() -> list[dict[str, object]]:
    definitions = {
        "fictional-planning-layer": {
            "scenario_id": ("text", "no", "Fictional planning case identifier"),
            "synthetic_source_id": ("text", "no", "Synthetic release identifier"),
            "tract_fips": ("text", "no", "Accepted eleven-character tract linkage key"),
            "county_fips": ("text", "no", "Accepted five-character county linkage key"),
            "fictional_capacity_places": ("integer", "no", "Generated fictional delivery capacity in ten-place units"),
            "fictional_travel_minutes": ("integer", "no", "Generated one-way teaching travel assumption"),
            "fictional_staff_readiness": ("text", "no", "Generated staff readiness state"),
            "fictional_language_access_ready": ("integer", "no", "Generated language-access plan readiness flag"),
            "fictional_disability_access_ready": ("integer", "no", "Generated disability-access plan readiness flag"),
            "fictional_community_review_state": ("text", "no", "Generated fictional review state, not real community opinion"),
            "fictional_unresolved_questions": ("integer", "no", "Generated unresolved planning-question count"),
            "fictional_objection_state": ("text", "no", "Generated fictional objection state"),
            "fictional_delivery_burden_score": ("integer", "no", "Generated ordinal classroom burden assumption from one to five"),
            "accountable_owner": ("text", "no", "Fictional owner responsible for the teaching decision"),
            "generator_version": ("text", "no", "Generator semantic version"),
            "seed": ("integer", "no", "Declared generator seed"),
            "synthetic_flag": ("integer", "no", "One for every fictional row"),
            "claim_limit": ("text", "no", "Explicit prohibition on real community and action claims"),
        },
        "rule-definitions": {field: ("text", "no", f"Declared teaching rule field: {field}") for field in RULE_FIELDS},
        "sensitivity-variants": {field: ("text", "no", f"Predeclared sensitivity field: {field}") for field in SENSITIVITY_FIELDS},
    }
    rows: list[dict[str, object]] = []
    for source_id, fields in definitions.items():
        for order, (field, (kind, nullable, definition)) in enumerate(fields.items(), start=1):
            rows.append(
                {
                    "source_id": source_id,
                    "field_order": order,
                    "field_name": field,
                    "type": kind,
                    "nullable": nullable,
                    "definition": definition,
                    "claim_limit": "Synthetic teaching metadata only; no real need, consent, eligibility, outreach, funding, allocation, service, or authority.",
                }
            )
    return rows


def build(root: Path, target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    target.mkdir(parents=True)
    (target / "raw").mkdir()

    tracts = load_accepted_tracts(root)
    products = [
        ("raw/fictional-planning-layer.csv.gz", PLANNING_FIELDS, planning_rows(tracts), True, SOURCE_ID),
        ("rule-definitions.csv", RULE_FIELDS, rule_rows(), False, "targeting-rule-definitions-v1"),
        ("sensitivity-variants.csv", SENSITIVITY_FIELDS, sensitivity_rows(), False, "targeting-sensitivity-variants-v1"),
        ("data-dictionary.csv", DICTIONARY_FIELDS, dictionary_rows(), False, "targeting-data-dictionary-v1"),
    ]
    manifest: list[dict[str, object]] = []
    for relative, fields, rows, zipped, source_id in products:
        raw = csv_bytes(fields, rows)
        payload = deterministic_gzip(raw) if zipped else raw
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        manifest.append(
            {
                "source_id": source_id,
                "relative_path": relative,
                "format": "csv.gz" if zipped else "csv",
                "rows": len(rows),
                "columns": len(fields),
                "bytes": len(payload),
                "sha256": sha256_bytes(payload),
                "content_bytes": len(raw),
                "content_sha256": sha256_bytes(raw),
                "generator_version": GENERATOR_VERSION,
                "seed": SEED,
                "synthetic_flag": 1,
                "claim_limit": "deterministic fictional teaching release; no real community fact, eligibility, outreach, funding, allocation, service, or authority",
            }
        )
    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "synthetic-source-manifest.csv"
    manifest_path.write_bytes(csv_bytes(MANIFEST_FIELDS, manifest))
    return {
        "planning_rows": len(products[0][2]),
        "rules": len(products[1][2]),
        "sensitivity_variants": len(products[2][2]),
        "dictionary_rows": len(products[3][2]),
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "files": {
            path.relative_to(target).as_posix(): {"bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in sorted(target.rglob("*"))
            if path.is_file()
        },
    }


def compare(left: Path, right: Path) -> None:
    left_files = {path.relative_to(left).as_posix(): sha256(path) for path in left.rglob("*") if path.is_file()}
    right_files = {path.relative_to(right).as_posix(): sha256(path) for path in right.rglob("*") if path.is_file()}
    require(left_files == right_files, "Two fictional planning releases differ")


def verify(root: Path = ROOT) -> dict[str, object]:
    committed = root / "data"
    require(committed.is_dir(), "Committed fictional planning release is missing")
    with tempfile.TemporaryDirectory(prefix="app5-module05-source-verify-") as temporary:
        generated = Path(temporary) / "data"
        report = build(root, generated)
        compare(committed, generated)
    if EXPECTED_FILES:
        actual = report["files"]
        require(actual == EXPECTED_FILES, "Fictional planning file identities changed")
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module05-source-") as temporary:
        base = Path(temporary)
        first = base / "first"
        second = base / "second"
        report = build(ROOT, first)
        build(ROOT, second)
        compare(first, second)
        require(report["planning_rows"] == 1597, "Planning row count changed")
        require(report["rules"] == 4, "Rule count changed")
        require(report["sensitivity_variants"] == 20, "Sensitivity variant count changed")
        try:
            build(ROOT, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Generator overwrote an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 05 fictional-source self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
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
            print(json.dumps(build(ROOT, args.target or (ROOT / "data")), indent=2, sort_keys=True))
        elif args.target:
            print(json.dumps(build(ROOT, args.target), indent=2, sort_keys=True))
        else:
            parser.error("use --write, --verify, --self-check, or provide --target")
    except (OSError, ValueError, KeyError, SourceError) as error:
        parser.exit(1, f"Fictional planning source failed: {error}\n")


if __name__ == "__main__":
    main()

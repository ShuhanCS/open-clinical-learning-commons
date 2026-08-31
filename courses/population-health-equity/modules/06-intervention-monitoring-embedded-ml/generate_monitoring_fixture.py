"""Generate the deterministic APP-5 Module 06 fictional monitoring dry run."""

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
SOURCE_ID = "fma-dp-01-monitoring-dry-run-v1"
SEED = 73056
EXPECTED_MANIFEST_SHA256 = "d6e09f0e57d4890300d44bf48fcf1be34f52698af05a0934c62e25926f6622cd"
EXPECTED_DRY_RUN_SHA256 = "067ac19e07eb8db3a48373d063e77a5b898d63a65b83f7e27504fba8beacdcda"

DRY_RUN_FIELDS = [
    "scenario_id", "synthetic_source_id", "seed", "fictional_test_id", "tract_fips", "county_fips",
    "county_name", "award_position", "fictional_place_position", "planned_week", "staff_readiness",
    "travel_minutes", "travel_concern", "offer_test_state", "response_test_state", "language_access_need_test",
    "language_access_test_state", "disability_access_need_test", "disability_access_test_state",
    "modality_test", "scheduling_test_state", "attendance_test_state", "completion_test_state",
    "fidelity_test_state", "burden_test_score", "feedback_test_state", "objection_test_state",
    "incident_test_state", "escalation_test_route", "pause_test_triggered", "outcome_available",
    "public_prevalence_used_to_generate", "synthetic_flag", "test_role", "interpretation_limit",
]

INTERVENTION_ROWS = [
    ("I01", "candidate", "fictional voluntary diabetes-prevention access and navigation program", "planning only", "population health analytics lead", "any real-world use"),
    ("I02", "starting rule", "community-review comparison carried as least unacceptable fictional planning candidate", "not an allocation decision", "community review council", "rule used automatically"),
    ("I03", "resource", "28 equal teaching awards of 10 fictional places, 280 places total", "fixed fictional constraint", "resource governance owner", "resource amount changed"),
    ("I04", "population", "adults represented only through area-level planning evidence", "no personal eligibility", "population health clinical lead", "individual inference"),
    ("I05", "information", "accessible program information before any voluntary response", "fictional design", "language and disability access owner", "access plan absent"),
    ("I06", "review", "human and community review before any fictional next step", "no automatic action", "community review council", "unresolved objection"),
    ("I07", "choice", "voluntary interest, refusal, correction, and withdrawal routes", "fictional design", "community accountability owner", "choice route absent"),
    ("I08", "delivery", "navigation plus accessible group or remote prevention support", "not service delivery", "program operations owner", "staff not ready"),
    ("I09", "monitoring", "twenty predeclared process, access, burden, feedback, incident, and availability measures", "teaching triggers only", "monitoring owner", "denominator unavailable"),
    ("I10", "feedback", "question, correction, refusal, appeal, disagreement, pause, and stop routes", "fictional exercise", "community accountability owner", "feedback suppressed or ignored"),
    ("I11", "incident", "named escalation for access, privacy, scheduling, burden, and objection tests", "human review required", "safety and privacy owner", "incident unresolved"),
    ("I12", "evaluation", "later prospective evaluation proposal with no effect estimate", "APP-6 owns effect estimation", "evaluation methods owner", "effect claim made"),
    ("I13", "retirement", "stop and retire when access, safety, community, evidence, or stewardship conditions fail", "human authority", "program steward", "stop right removed"),
    ("I14", "deployment", "no production connection or deployment", "prohibited", "program steward", "deployment language added"),
]

MEASURE_ROWS = [
    ("M01", "Selected-area operational readiness", "readiness", "selected tracts not marked staff-not-ready", "all 28 carried tracts", "before start and weekly", "Module 05 planning layer", "program operations owner", "not assessed", "higher", "1.00", "course teaching contract", "hold any not-ready tract for human review"),
    ("M02", "Selected-area travel concern", "access", "selected tracts below 60 fictional travel minutes", "all 28 carried tracts", "before start and monthly", "Module 05 planning layer", "access owner", "not assessed", "higher", "1.00", "course teaching contract", "revise modality and site plan"),
    ("M03", "Offer tests processed", "reach", "dry-run records processed", "all 280 dry-run records", "weekly", "fictional dry-run", "monitoring owner", "fixture absent", "higher", "0.95", "course teaching trigger", "review readiness holds"),
    ("M04", "Response available", "reach", "processed tests with interested, declined, or no-response state", "processed offer tests", "weekly", "fictional dry-run", "monitoring owner", "no processed tests", "higher", "1.00", "course teaching trigger", "repair response capture"),
    ("M05", "Fictional interest", "uptake", "interested test responses", "processed offer tests", "weekly", "fictional dry-run", "monitoring owner", "no processed tests", "descriptive", "none", "no action threshold", "report without performance claim"),
    ("M06", "Fictional refusal", "choice", "declined test responses", "processed offer tests", "weekly", "fictional dry-run", "community accountability owner", "no processed tests", "descriptive", "none", "no action threshold", "preserve refusal without penalty"),
    ("M07", "Language access delivered", "access", "language-access tests provided when needed", "tests with language-access need", "weekly", "fictional dry-run", "language access owner", "no tested need", "higher", "1.00", "course teaching trigger", "pause affected path and correct"),
    ("M08", "Disability access delivered", "access", "disability-access tests provided when needed", "tests with disability-access need", "weekly", "fictional dry-run", "disability access owner", "no tested need", "higher", "1.00", "course teaching trigger", "pause affected path and correct"),
    ("M09", "Scheduling completed", "delivery", "interested tests scheduled", "interested test responses", "weekly", "fictional dry-run", "program operations owner", "no interested tests", "higher", "0.90", "course teaching trigger", "review scheduling and access"),
    ("M10", "Attendance", "delivery", "scheduled tests marked attended", "scheduled tests", "weekly", "fictional dry-run", "program operations owner", "no scheduled tests", "descriptive", "none", "no action threshold", "report without outcome claim"),
    ("M11", "Completion", "delivery", "attended tests marked complete", "attended tests", "monthly", "fictional dry-run", "program operations owner", "no attended tests", "descriptive", "none", "no action threshold", "report without outcome claim"),
    ("M12", "Fidelity", "implementation", "attended tests passing the fictional fidelity check", "attended tests", "weekly", "fictional dry-run", "implementation owner", "no attended tests", "higher", "0.90", "course teaching trigger", "review workflow and training"),
    ("M13", "Low burden", "balancing", "processed tests with burden score at or below 3", "processed offer tests", "weekly", "fictional dry-run", "community accountability owner", "no processed tests", "higher", "0.90", "course teaching trigger", "revise modality and workload"),
    ("M14", "Feedback captured", "feedback", "processed tests with a feedback state", "processed offer tests", "weekly", "fictional dry-run", "community accountability owner", "no processed tests", "higher", "1.00", "course teaching trigger", "repair feedback capture"),
    ("M15", "Objection tests resolved", "recourse", "objection tests routed to hold and review", "tests with objection", "immediate", "fictional dry-run", "community review council", "no objection tests", "higher", "1.00", "course teaching trigger", "hold and review every objection"),
    ("M16", "Incident-free dry run", "safety", "processed tests without an incident", "processed offer tests", "weekly", "fictional dry-run", "safety and privacy owner", "no processed tests", "higher", "0.98", "course teaching trigger", "escalate and investigate incidents"),
    ("M17", "Escalation routed", "governance", "incident tests with a named escalation route", "tests with an incident", "immediate", "fictional dry-run", "program steward", "no incident tests", "higher", "1.00", "course teaching trigger", "stop until routing is complete"),
    ("M18", "Pause trigger honored", "governance", "tests requiring pause marked paused", "tests requiring pause", "immediate", "fictional dry-run", "program steward", "no pause-required tests", "higher", "1.00", "course teaching trigger", "stop until pause is honored"),
    ("M19", "Outcome availability", "evaluation", "records with an outcome", "all 280 dry-run records", "end of exercise", "fictional dry-run", "evaluation methods owner", "fixture absent", "descriptive", "none", "outcomes intentionally unavailable", "make no effect estimate"),
    ("M20", "Real-world action", "authority", "records causing real action", "all 280 dry-run records", "continuous", "release audit", "program steward", "not assessed", "lower", "0.00", "hard authority boundary", "stop release if any real action appears"),
]

FEATURE_ROWS = [
    ("F01", "modeled_crude_prevalence_percent", "public modeled area prevalence", "identity", "standard", "fail", "public", "not need ranking or eligibility"),
    ("F02", "interval_width_percentage_points", "public uncertainty width", "identity", "standard", "fail", "public", "not a confidence or exclusion score"),
    ("F03", "places_adult_population_field", "public adult population field", "log1p", "standard", "fail", "public", "not a resource weight"),
    ("F04", "fictional_capacity_places", "fictional capacity", "identity", "standard", "fail", "synthetic", "not real capacity"),
    ("F05", "fictional_travel_minutes", "fictional travel", "identity", "standard", "fail", "synthetic", "not real travel time"),
    ("F06", "fictional_delivery_burden_score", "fictional burden", "identity", "standard", "fail", "synthetic", "not an individual burden trait"),
    ("F07", "fictional_language_access_ready", "fictional language-access readiness", "yes=1; no=0", "standard", "fail", "synthetic", "not a language identity"),
    ("F08", "fictional_disability_access_ready", "fictional disability-access readiness", "yes=1; no=0", "standard", "fail", "synthetic", "not disability status"),
    ("F09", "fictional_staff_readiness", "fictional staff readiness", "ready=1; otherwise=0", "standard", "fail", "synthetic", "not real staffing"),
]

VARIANT_ROWS = [
    ("base", "base", "standard", 73056, 4, "accepted fixed challenger"),
    ("seed-73057", "seed", "standard", 73057, 4, "alternate seed only"),
    ("seed-73058", "seed", "standard", 73058, 4, "alternate seed only"),
    ("seed-73059", "seed", "standard", 73059, 4, "alternate seed only"),
    ("seed-73060", "seed", "standard", 73060, 4, "alternate seed only"),
    ("robust-scaling", "scaling", "robust", 73056, 4, "median and interquartile range"),
    ("minmax-scaling", "scaling", "minmax", 73056, 4, "zero to one feature range"),
    ("unitnorm-scaling", "scaling", "unitnorm", 73056, 4, "row unit norm after fixed transformations"),
]


class FixtureError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FixtureError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_int(tract_fips: str, position: int, label: str) -> int:
    token = f"{SEED}|{tract_fips}|{position}|{label}".encode("utf-8")
    return int(hashlib.sha256(token).hexdigest()[:16], 16)


def read_csv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_bytes(fields: list[str], rows: list[dict[str, object]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    raw = csv_bytes(fields, rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".gz":
        output = io.BytesIO()
        with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
            zipped.write(raw)
        path.write_bytes(output.getvalue())
    else:
        path.write_bytes(raw)


def tuple_rows(fields: list[str], rows: list[tuple[object, ...]]) -> list[dict[str, object]]:
    return [dict(zip(fields, row)) for row in rows]


def build_dry_run(root: Path) -> list[dict[str, object]]:
    assignments = read_csv(root / "upstream/module05-reference/outputs/rule-assignments.csv.gz")
    selected = sorted(
        (row for row in assignments if row["rule_id"] == "community_review" and row["selected"] == "1"),
        key=lambda row: int(row["selection_order"]),
    )
    require(len(selected) == 28, "Accepted community-review selection changed")
    require(sum(int(row["allocated_places"]) for row in selected) == 280, "Accepted fictional resource changed")
    require(all(row["fictional_objection_state"] == "no_recorded_objection" for row in selected), "Accepted selected objection changed")

    records: list[dict[str, object]] = []
    for area in selected:
        tract = area["tract_fips"]
        staff_ready = area["fictional_staff_readiness"] != "not_ready"
        travel = int(area["fictional_travel_minutes"])
        for position in range(1, 11):
            held = not staff_ready
            offer_state = "held_for_readiness" if held else "processed"
            response_roll = stable_int(tract, position, "response") % 10
            response = "not_tested" if held else ("interested" if response_roll < 6 else "declined" if response_roll < 8 else "no_response")
            language_need = stable_int(tract, position, "language") % 4 == 0
            disability_need = stable_int(tract, position, "disability") % 7 == 0
            language_failure = language_need and stable_int(tract, position, "language-failure") % 19 == 0
            disability_failure = disability_need and stable_int(tract, position, "disability-failure") % 17 == 0
            language_state = "not_needed" if not language_need else "unavailable" if language_failure else "provided"
            disability_state = "not_needed" if not disability_need else "unavailable" if disability_failure else "provided"
            modality = ("remote" if position % 2 else "hybrid") if travel >= 60 else ("in_person" if position % 3 else "hybrid")
            schedulable = response == "interested" and not language_failure and not disability_failure
            scheduled = schedulable and stable_int(tract, position, "schedule") % 10 != 0
            attended = scheduled and stable_int(tract, position, "attendance") % 6 != 0
            completed = attended and stable_int(tract, position, "completion") % 5 != 0
            scheduling_state = "not_applicable" if response != "interested" else "scheduled" if scheduled else "not_scheduled"
            attendance_state = "not_applicable" if not scheduled else "attended" if attended else "not_attended"
            completion_state = "not_started" if not attended else "complete" if completed else "partial"
            fidelity_state = "not_tested" if not attended else "pass" if stable_int(tract, position, "fidelity") % 11 else "fail"
            burden = min(5, max(1, int(area["fictional_delivery_burden_score"]) + (stable_int(tract, position, "burden") % 3 - 1)))
            feedback_roll = stable_int(tract, position, "feedback") % 29
            feedback = "objection" if feedback_roll == 0 else "question" if feedback_roll < 5 else "supportive" if feedback_roll < 11 else "no_feedback"
            objection = "simulated_objection" if feedback == "objection" else "none"
            if language_failure or disability_failure:
                incident = "access_failure"
            elif stable_int(tract, position, "privacy") % 71 == 0:
                incident = "privacy_near_miss"
            elif response == "interested" and not scheduled:
                incident = "scheduling_failure"
            else:
                incident = "none"
            escalation = {
                "access_failure": "access_owner_and_program_steward",
                "privacy_near_miss": "privacy_owner_and_program_steward",
                "scheduling_failure": "operations_owner",
                "none": "none",
            }[incident]
            pause = held or objection != "none" or incident in {"access_failure", "privacy_near_miss"}
            records.append(
                {
                    "scenario_id": "FMA-DP-01",
                    "synthetic_source_id": SOURCE_ID,
                    "seed": SEED,
                    "fictional_test_id": f"FT-{tract}-{position:02d}",
                    "tract_fips": tract,
                    "county_fips": area["county_fips"],
                    "county_name": area["county_name"],
                    "award_position": int(area["selection_order"]),
                    "fictional_place_position": position,
                    "planned_week": 1 + stable_int(tract, position, "week") % 12,
                    "staff_readiness": area["fictional_staff_readiness"],
                    "travel_minutes": travel,
                    "travel_concern": "yes" if travel >= 60 else "no",
                    "offer_test_state": offer_state,
                    "response_test_state": response,
                    "language_access_need_test": "yes" if language_need else "no",
                    "language_access_test_state": language_state,
                    "disability_access_need_test": "yes" if disability_need else "no",
                    "disability_access_test_state": disability_state,
                    "modality_test": modality,
                    "scheduling_test_state": scheduling_state,
                    "attendance_test_state": attendance_state,
                    "completion_test_state": completion_state,
                    "fidelity_test_state": fidelity_state,
                    "burden_test_score": burden,
                    "feedback_test_state": feedback,
                    "objection_test_state": objection,
                    "incident_test_state": incident,
                    "escalation_test_route": escalation,
                    "pause_test_triggered": "yes" if pause else "no",
                    "outcome_available": "no",
                    "public_prevalence_used_to_generate": "no",
                    "synthetic_flag": "yes",
                    "test_role": "software and governance dry run only",
                    "interpretation_limit": "not a person, observed service, clinical outcome, effect estimate, or implementation record",
                }
            )
    require(len(records) == 280 and len({row["fictional_test_id"] for row in records}) == 280, "Dry-run identity changed")
    return records


def generate(target: Path, root: Path = ROOT) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    target.mkdir(parents=True)

    dictionary = [
        {"field": field, "type": "string", "role": "fictional monitoring dry-run field", "missing_rule": "no blank values", "interpretation_limit": "synthetic test only"}
        for field in DRY_RUN_FIELDS
    ]
    write_rows(target / "data-dictionary.csv", ["field", "type", "role", "missing_rule", "interpretation_limit"], dictionary)
    write_rows(target / "intervention-contract.csv", ["item_id", "item", "specification", "authority", "owner", "stop_condition"], tuple_rows(["item_id", "item", "specification", "authority", "owner", "stop_condition"], INTERVENTION_ROWS))
    measure_fields = ["measure_id", "measure_name", "domain", "numerator_definition", "denominator_definition", "cadence", "source", "owner", "unavailable_state", "direction", "teaching_threshold", "threshold_origin", "human_response"]
    measures = tuple_rows(measure_fields, MEASURE_ROWS)
    for row in measures:
        row["automatic_action"] = "no"
        row["interpretation_limit"] = "fictional monitoring design, not a validated operational or clinical measure"
    write_rows(target / "monitoring-measures.csv", measure_fields + ["automatic_action", "interpretation_limit"], measures)
    feature_fields = ["feature_id", "source_field", "role", "transformation", "scaling", "missing_rule", "source_type", "prohibited_use"]
    write_rows(target / "cluster-feature-contract.csv", feature_fields, tuple_rows(feature_fields, FEATURE_ROWS))
    variant_fields = ["variant_id", "variant_type", "scaling", "seed", "clusters", "role"]
    write_rows(target / "challenger-variants.csv", variant_fields, tuple_rows(variant_fields, VARIANT_ROWS))
    dry_run = build_dry_run(root)
    write_rows(target / "raw/fictional-monitoring-dry-run.csv.gz", DRY_RUN_FIELDS, dry_run)

    manifest_fields = ["relative_path", "bytes", "sha256", "rows", "source_type", "role", "interpretation_limit"]
    manifest: list[dict[str, object]] = []
    row_counts = {
        "data-dictionary.csv": len(dictionary),
        "intervention-contract.csv": len(INTERVENTION_ROWS),
        "monitoring-measures.csv": len(MEASURE_ROWS),
        "cluster-feature-contract.csv": len(FEATURE_ROWS),
        "challenger-variants.csv": len(VARIANT_ROWS),
        "raw/fictional-monitoring-dry-run.csv.gz": len(dry_run),
    }
    for relative in sorted(row_counts):
        path = target / relative
        manifest.append(
            {
                "relative_path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "rows": row_counts[relative],
                "source_type": "deterministic synthetic teaching source",
                "role": "Module 06 intervention, monitoring, or clustering contract",
                "interpretation_limit": "not observed care, community input, clinical outcome, effect evidence, or implementation authority",
            }
        )
    write_rows(target / "synthetic-source-manifest.csv", manifest_fields, manifest)
    return {
        "source_id": SOURCE_ID,
        "seed": SEED,
        "dry_run_rows": len(dry_run),
        "manifest_rows": len(manifest),
        "manifest_bytes": (target / "synthetic-source-manifest.csv").stat().st_size,
        "manifest_sha256": sha256(target / "synthetic-source-manifest.csv"),
        "dry_run_sha256": sha256(target / "raw/fictional-monitoring-dry-run.csv.gz"),
        "measures": len(MEASURE_ROWS),
        "features": len(FEATURE_ROWS),
        "variants": len(VARIANT_ROWS),
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    data = root / "data"
    manifest = read_csv(data / "synthetic-source-manifest.csv")
    require(len(manifest) == 6, "Synthetic source manifest row count changed")
    expected = {row["relative_path"] for row in manifest} | {"synthetic-source-manifest.csv"}
    actual = {path.relative_to(data).as_posix() for path in data.rglob("*") if path.is_file()}
    require(actual == expected, "Synthetic source file set changed")
    for row in manifest:
        path = data / row["relative_path"]
        require(path.stat().st_size == int(row["bytes"]), f"Synthetic source byte count changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Synthetic source SHA-256 changed: {row['relative_path']}")
    dry_run = read_csv(data / "raw/fictional-monitoring-dry-run.csv.gz")
    require(len(dry_run) == 280 and len({row["fictional_test_id"] for row in dry_run}) == 280, "Dry-run rows changed")
    require(all(row["synthetic_flag"] == "yes" and row["outcome_available"] == "no" for row in dry_run), "Dry-run identity changed")
    require(all(row["public_prevalence_used_to_generate"] == "no" for row in dry_run), "Dry run depends on public prevalence")
    require(len(read_csv(data / "monitoring-measures.csv")) == 20, "Monitoring measure count changed")
    require(len(read_csv(data / "cluster-feature-contract.csv")) == 9, "Feature contract count changed")
    require(len(read_csv(data / "challenger-variants.csv")) == 8, "Challenger variant count changed")
    if EXPECTED_MANIFEST_SHA256:
        require(sha256(data / "synthetic-source-manifest.csv") == EXPECTED_MANIFEST_SHA256, "Synthetic source manifest identity changed")
    if EXPECTED_DRY_RUN_SHA256:
        require(sha256(data / "raw/fictional-monitoring-dry-run.csv.gz") == EXPECTED_DRY_RUN_SHA256, "Dry-run identity changed")
    return {
        "source_id": SOURCE_ID,
        "seed": SEED,
        "dry_run_rows": len(dry_run),
        "manifest_rows": len(manifest),
        "manifest_bytes": (data / "synthetic-source-manifest.csv").stat().st_size,
        "manifest_sha256": sha256(data / "synthetic-source-manifest.csv"),
        "dry_run_sha256": sha256(data / "raw/fictional-monitoring-dry-run.csv.gz"),
        "measures": 20,
        "features": 9,
        "variants": 8,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module06-source-") as temporary:
        base = Path(temporary)
        first = generate(base / "first")
        second = generate(base / "second")
        require(first == second, "Two monitoring source generations differ")
        first_files = {path.relative_to(base / "first").as_posix(): sha256(path) for path in (base / "first").rglob("*") if path.is_file()}
        second_files = {path.relative_to(base / "second").as_posix(): sha256(path) for path in (base / "second").rglob("*") if path.is_file()}
        require(first_files == second_files, "Two monitoring source file sets differ")
        try:
            generate(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Generator overwrote an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 06 monitoring-source self-check passed: {json.dumps(committed, sort_keys=True)}")


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
            print(json.dumps(generate(args.target or (ROOT / "data")), indent=2, sort_keys=True))
        elif args.target:
            print(json.dumps(generate(args.target), indent=2, sort_keys=True))
        else:
            parser.error("use --write, --verify, --self-check, or provide --target")
    except (OSError, ValueError, KeyError, FixtureError) as error:
        parser.exit(1, f"Monitoring source failed: {error}\n")


if __name__ == "__main__":
    main()

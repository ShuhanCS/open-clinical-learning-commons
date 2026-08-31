"""Validate APP-5 Module 04 learner and reference workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD)\b")
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
UNSUPPORTED_CLAIM = re.compile(
    r"(?im)^(?:Adults who live in darker tracts have diabetes|The map identifies communities that need intervention|"
    r"Tracts in the darkest class should be prioritized|Deploy this map|This map proves a real disparity)\b"
)
PUBLIC_SYNTHETIC_MERGE = re.compile(r"(?i)(public PLACES values are observed synthetic events|PLACES values are synthetic events)")
STIGMATIZING_CLAIM = re.compile(r"(?i)(failing community is deficient|residents are the problem|deficient community)")
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}
EXPECTED_COMPLETE_CHECKS = 930
EXPECTED_LEARNER_CHECKS = 832
EXPECTED_FAILURE_ROUTES = 22


class ValidationError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\.\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, learner: bool = False) -> dict[str, object]:
    import acquire_geometry
    import build_place_evidence
    import build_workspace
    import freeze_upstream

    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    immutable = build_workspace.CONTROL_FILES + build_workspace.DATA_FILES + build_workspace.UPSTREAM_FILES
    if not learner:
        immutable += build_workspace.OUTPUT_FILES
    expected = set(immutable) | set(build_workspace.SQL_FILES) | set(build_workspace.RECORD_FILES) | {
        "release-manifest.csv"
    }
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    expected_count = build_workspace.EXPECTED_LEARNER_FILES if learner else build_workspace.EXPECTED_REFERENCE_FILES
    expected_manifest = (
        build_workspace.EXPECTED_LEARNER_MANIFEST_ROWS
        if learner
        else build_workspace.EXPECTED_REFERENCE_MANIFEST_ROWS
    )
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_count, f"Workspace has exactly {expected_count} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "geography-contract.json").read_text(encoding="utf-8"))
    require(
        contract["module"]
        == {
            "id": "oclc-app5-04",
            "version": "0.1.0",
            "commons_release": "0.91.0",
            "hours": 16.5,
            "course_points": 10,
            "week6_checkpoint_points_after_acceptance": 10,
        },
        "Module identity workload and points match",
    )
    require(
        contract["upstream"]["reference_files"] == 240
        and contract["upstream"]["candidate_files"] == 219
        and contract["upstream"]["candidate_manifest_sha256"]
        == "b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192"
        and contract["upstream"]["handoff_manifest_sha256"]
        == "db70b4e20a17fbddd2b49f7647dd9ce5bcd064e01af5e7a7e23df9122889914e",
        "Frozen Week 3 checkpoint identity matches",
    )
    require(
        contract["source"]["archive_bytes"] == 4_506_627
        and contract["source"]["archive_sha256"]
        == "74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4"
        and contract["source"]["tracts"] == 1620
        and contract["source"]["source_crs_epsg"] == 4269
        and contract["source"]["projected_crs_epsg"] == 26986
        and contract["source"]["display_simplification_meters"] == 100,
        "Public geometry source contract matches",
    )
    require(
        contract["measure"]["matched_tracts"] == 1597
        and contract["measure"]["geometry_only_tracts"] == 23
        and contract["measure"]["limited_support_interval_width"] == 4.0
        and contract["measure"]["limited_support_population"] == 500
        and contract["measure"]["rank_based_classes"] is False,
        "Measure class and support contract matches",
    )
    require(
        contract["assessment"]
        == {
            "criteria": 4,
            "points": 10,
            "pass_score": 8,
            "noncompensable_gates": 22,
            "week6_component_points": 10,
        },
        "Assessment contract matches",
    )
    require(
        contract["workspace"]
        == {
            "learner_files": 275,
            "learner_manifest_rows": 259,
            "reference_files": 287,
            "reference_manifest_rows": 271,
            "editable_records": 12,
            "editable_sql_files": 3,
        },
        "Workspace contract matches",
    )
    require(
        contract["authority"]["responsible_teaching_map"] == "permitted"
        and all(
            value == "prohibited"
            for key, value in contract["authority"].items()
            if key != "responsible_teaching_map"
        ),
        "Authority permits one bounded teaching map and prohibits real-world action",
    )

    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    require(
        release["module_id"] == "oclc-app5-04"
        and release["module_version"] == "0.1.0"
        and release["commons_release"] == "0.91.0"
        and release["status"] == "runnable release candidate",
        "Release identity and status match",
    )
    require(
        release["workspace"]
        == {
            "learner_files": 275,
            "learner_manifest_rows": 259,
            "reference_files": 287,
            "reference_manifest_rows": 271,
            "editable_records": 12,
            "editable_sql_files": 3,
        },
        "Release workspace counts match",
    )
    if EXPECTED_COMPLETE_CHECKS:
        require(
            release["validation"]["complete_checks"] == EXPECTED_COMPLETE_CHECKS
            and release["validation"]["starter_checks"] == EXPECTED_LEARNER_CHECKS
            and release["validation"]["protected_failure_routes"] == EXPECTED_FAILURE_ROUTES,
            "Release validation counts match",
        )

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Release manifest header matches")
    require(
        len(manifest) == expected_manifest
        and [row["relative_path"] for row in manifest] == sorted(immutable),
        f"Release manifest has {expected_manifest} sorted rows",
    )
    for row in manifest:
        relative = Path(row["relative_path"])
        require(
            not relative.is_absolute() and ".." not in relative.parts,
            f"Manifest path is portable: {row['relative_path']}",
        )
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(
            path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"],
            f"Manifest identity matches: {row['relative_path']}",
        )

    source = acquire_geometry.verify(root)
    require(
        source["archive_bytes"] == 4_506_627
        and source["archive_members"] == 7
        and source["manifest_rows"] == 8,
        "Complete official geometry source reproduces",
    )
    handoff = freeze_upstream.verify(root)
    require(
        handoff["payload_files"] == 240
        and handoff["upstream_files"] == 241
        and handoff["candidate_files"] == 219,
        "Complete Week 3 checkpoint handoff reproduces",
    )

    record_text = ""
    for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        record_text += "\n" + text
        if not learner:
            require(not PLACEHOLDER.search(text), f"Submission file is complete: {relative}")

    claim_header, claims = read_csv(root / "ecological-contextual-claims-audit.csv")
    require(
        claim_header == ["claim_id", "proposed_statement", "classification", "decision", "reason", "required_rewrite"],
        "Ecological claims audit header matches",
    )
    require([row["claim_id"] for row in claims] == [f"EC{index:02d}" for index in range(1, 11)], "Claims audit has ten ordered rows")
    score_header, score = read_csv(root / "week6-component-score.csv")
    require(
        score_header == ["criterion_id", "criterion", "points_available", "points_awarded", "status", "evidence"],
        "Score header matches",
    )
    require([row["criterion_id"] for row in score] == ["R1", "R2", "R3", "R4", "TOTAL"], "Score has four criteria and total")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(
        gate_header == ["gate_id", "gate", "status", "evidence", "blocking_if_failed"],
        "Gate header matches",
    )
    require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 23)], "Gate file has 22 ordered rows")

    if learner:
        require(PLACEHOLDER.search(record_text) is not None, "Learner workspace contains explicit prompts")
        require(not any(path.startswith("outputs/") for path in actual), "Learner workspace contains no accepted outputs")
        report = {
            "status": "pass",
            "mode": "learner",
            "checks": len(checks),
            "files": expected_count,
            "manifest_rows": expected_manifest,
            "course_points": 0,
        }
        print(f"APP-5 Module 04 learner validation passed: {len(checks)} checks.")
        return report

    require(not UNSUPPORTED_CLAIM.search(record_text), "Submission makes no unsupported ecological or action claim")
    require(not PUBLIC_SYNTHETIC_MERGE.search(record_text), "Public modeled and fictional synthetic evidence remain separate")
    require(not STIGMATIZING_CLAIM.search(record_text), "Submission makes no stigmatizing place or community claim")
    require(all(row["decision"] in {"accept", "reject"} and row["reason"] and row["required_rewrite"] for row in claims), "Every claim receives a decision reason and rewrite")
    require(sum(row["decision"] == "accept" for row in claims) == 2, "Exactly two bounded statements are accepted")
    require(
        sum(int(row["points_awarded"]) for row in score[:4]) == 10
        and score[-1]["points_awarded"] == "10"
        and all(row["status"] == "pass" for row in score),
        "Reference score is 10 of 10",
    )
    require(
        all(row["status"] == "pass" and row["evidence"] and row["blocking_if_failed"] == "yes" for row in gates),
        "All 22 noncompensable gates pass with evidence",
    )

    source_review = (root / "geometry-source-review.md").read_text(encoding="utf-8")
    require(
        all(
            value in source_review
            for value in (
                "4,506,627",
                "74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4",
                "1,620 rows",
                "1,617 Polygon",
                "3 MultiPolygon",
                "EPSG 4269",
                "0.0001990791",
            )
        ),
        "Geometry source review contains the accepted identity and geometry facts",
    )
    join_review = (root / "geography-join-and-crs-audit.md").read_text(encoding="utf-8")
    require(
        all(value in join_review for value in ("1,597", "23", "0", "unavailable", "100-meter", "32 SQL checks pass")),
        "Join and coordinate-system audit is complete",
    )
    aggregation_review = (root / "aggregation-and-stability-review.md").read_text(encoding="utf-8")
    require(
        all(value in aggregation_review for value in ("1,548", "43", "5", "49", "645", "not official county PLACES estimates", "not a CDC quality designation", "| Less than 5.0% | 82 |")),
        "Aggregation and stability review is complete",
    )
    map_spec = (root / "responsible-map-specification.md").read_text(encoding="utf-8")
    require(
        all(value in map_spec for value in ('role="img"', "map-title map-desc", "fixed absolute classes", "complete exact CSV table", "100 meters")),
        "Responsible map specification is complete",
    )
    text_alternative = (root / "responsible-map-text-alternative.md").read_text(encoding="utf-8")
    require(
        all(value in text_alternative for value in ("Eighty-two", "Eight hundred twenty-six", "Six hundred eight", "Forty-nine", "645", "Twenty-three", "Gray means unavailable")),
        "Structured map text alternative is complete",
    )
    context = (root / "responsible-map-context-memo.md").read_text(encoding="utf-8")
    require(
        all(value in context for value in ("wrong join", "modifiable areal unit problem", "Gray is unavailable, not zero", "No tract is prioritized")),
        "Responsible map context memo is complete",
    )
    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8")
    require(
        all(value in reproduction for value in ("byte-identical outputs", "32 of 32 pass", "1,620", "1,597", "23", "fixed Matplotlib SVG hash salt")),
        "Reproducibility record is complete",
    )
    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    require(
        "Sensitive data supplied to an agent: `none`" in ai_use
        and "Fabricated community input: `none`" in ai_use
        and "Agent-authored real-world recommendation: `none`" in ai_use,
        "AI-use boundary is complete",
    )

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(field(progression, "Progression") in ALLOWED_PROGRESSION, "Progression value is allowed")
    require(field(progression, "Progression") == "continue with conditions", "Progression remains conditioned")
    require(field(progression, "Module 05 permission") == "permitted for curriculum construction", "Module 05 curriculum construction is permitted")
    require(field(progression, "Week 6 checkpoint permission") == "not yet; Modules 05 and 06 must pass first", "Week 6 checkpoint remains gated")
    for label in (
        "Real disparity claim",
        "Individual or household inference",
        "Tract ranking or priority label",
        "Targeting or eligibility",
        "Outreach",
        "Allocation or funding",
        "Model fitting",
        "Intervention-effect estimation",
        "Real community action",
        "Implementation",
        "Production connection",
        "Deployment",
    ):
        require(field(progression, label) == "prohibited", f"{label} remains prohibited")

    source_header, source_rows = read_csv(root / "outputs/source-profile.csv")
    require(len(source_rows) == 1 and source_rows[0]["tract_rows"] == "1620", "Source profile has one accepted source row")
    geometry_header, geometry = read_csv(root / "outputs/geometry-audit.csv")
    require(len(geometry) == 1620 and len({row["tract_fips"] for row in geometry}) == 1620, "Geometry audit has 1,620 unique tracts")
    require(sum(row["is_valid"] == "1" for row in geometry) == 1620 and all(row["is_null"] == "0" and row["is_empty"] == "0" for row in geometry), "All geometry rows are valid and present")
    join_header, joins = read_csv(root / "outputs/geometry-join-audit.csv")
    require(len(joins) == 1620 and sum(row["join_state"] == "matched_measure" for row in joins) == 1597, "Join audit has 1,597 matched tracts")
    require(sum(row["join_state"] == "geometry_only_unavailable" for row in joins) == 23, "Join audit retains 23 unavailable tracts")
    map_header, map_rows = read_csv(root / "outputs/tract-map-table.csv")
    require(len(map_rows) == 1620 and len({row["tract_fips"] for row in map_rows}) == 1620, "Exact map table has every source tract once")
    require(sum(row["map_class"] == "unavailable" and row["modeled_crude_prevalence_percent"] == "" for row in map_rows) == 23, "Unavailable map rows remain blank rather than zero")
    require(sum(row["support_state"] == "limited_support_review" for row in map_rows) == 49, "Exactly 49 tracts carry the classroom support review")
    county_header, counties = read_csv(root / "outputs/county-aggregation.csv")
    require(len(counties) == 14 and all("not an official county PLACES estimate" in row["summary_type"] for row in counties), "Fourteen county teaching summaries retain their label")
    comparison_header, comparisons = read_csv(root / "outputs/aggregation-comparison.csv")
    require(len(comparisons) == 1597 and sum(int(row["class_changes_after_aggregation"]) for row in comparisons) == 645, "Aggregation comparison reproduces 645 class changes")
    class_header, classes = read_csv(root / "outputs/map-class-summary.csv")
    require([int(row["tract_count"]) for row in classes] == [82, 826, 608, 64, 17, 23], "Map class counts match")
    query_header, query_checks = read_csv(root / "outputs/query-checks.csv")
    require(len(query_checks) == 32 and all(row["status"] == "pass" for row in query_checks), "All 32 query checks pass")
    map_facts = json.loads((root / "outputs/map-text-facts.json").read_text(encoding="utf-8"))
    require(
        map_facts["geometry_tracts"] == 1620
        and map_facts["mapped_estimates"] == 1597
        and map_facts["unavailable_tracts"] == 23
        and map_facts["limited_support_review_tracts"] == 49
        and map_facts["tracts_changing_class_after_county_aggregation"] == 645,
        "Structured map facts match",
    )
    map_path = root / "outputs/responsible-diabetes-prevalence-map.svg"
    svg = ET.parse(map_path).getroot()
    svg_text = map_path.read_text(encoding="utf-8")
    require(svg.attrib.get("role") == "img" and svg.attrib.get("aria-labelledby") == "map-title map-desc", "SVG role and accessible label relationship pass")
    require('id="map-title"' in svg_text and 'id="map-desc"' in svg_text and "<image" not in svg_text, "SVG has title description and no raster image")
    require(map_path.stat().st_size == 1_515_932 and sha256(map_path) == "cf5386a255dc37c518e8410ea891f2f73726a95c13b65e22dbadf218ba6c1ae6", "Accepted SVG byte and SHA-256 identity match")

    build_report = json.loads((root / "outputs/build-report.json").read_text(encoding="utf-8"))
    require(
        build_report["geometry"]["rows"] == 1620
        and build_report["findings"]["mapped_estimates"] == 1597
        and build_report["findings"]["geometry_only_unavailable"] == 23
        and build_report["findings"]["query_checks"] == 32
        and build_report["findings"]["failed_query_checks"] == 0,
        "Build report findings match",
    )
    regenerated = build_place_evidence.verify(root)
    require(
        regenerated["findings"]["limited_support_review_tracts"] == 49
        and regenerated["findings"]["tracts_changing_class_after_county_aggregation"] == 645,
        "Independent output regeneration matches",
    )

    report = {
        "status": "pass",
        "mode": "complete",
        "checks": len(checks),
        "files": expected_count,
        "manifest_rows": expected_manifest,
        "course_points": 10,
    }
    print(f"APP-5 Module 04 complete validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, learner: bool = False) -> None:
    try:
        validate(root, learner=learner)
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError, ET.ParseError):
        return
    raise AssertionError(f"Validator accepted an invalid workspace: {root}")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app5-module04-validator-") as temporary:
        base = Path(temporary)
        reference = base / "reference"
        learner = base / "learner"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(learner)
        complete_report = validate(reference)
        learner_report = validate(learner, learner=True)

        names = (
            "upstream-mutation",
            "source-mutation",
            "missing-file",
            "placeholder",
            "changed-sql",
            "bad-score",
            "failed-gate",
            "zero-unavailable",
            "public-synthetic-merge",
            "ranking-authority",
            "targeting-authority",
            "official-county-claim",
            "cdc-quality-label",
            "inaccessible-svg",
            "changed-exact-table",
            "ecological-claim",
            "stigmatizing-label",
            "personal-path",
            "changed-map-hash",
            "changed-map-class",
            "bad-progression",
            "deployment-authority",
        )
        cases: list[tuple[str, Path]] = []
        for name in names:
            target = base / name
            shutil.copytree(reference, target)
            cases.append((name, target))

        upstream_path = cases[0][1] / "upstream/checkpoint-reference/candidate/module-02/outputs/public-modeled-prevalence.csv"
        upstream_path.write_bytes(upstream_path.read_bytes() + b"x")
        source_path = cases[1][1] / "data/raw/tl_2024_25_tract.zip"
        source_path.write_bytes(source_path.read_bytes() + b"x")
        (cases[2][1] / "responsible-map-text-alternative.md").unlink()
        with (cases[3][1] / "responsible-map-context-memo.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        sql_path = cases[4][1] / "sql/03-audit-map-release.sql"
        sql_path.write_text(sql_path.read_text(encoding="utf-8").replace("5663670", "5663671", 1), encoding="utf-8")
        score_path = cases[5][1] / "week6-component-score.csv"
        score_path.write_text(score_path.read_text(encoding="utf-8").replace("R1,Source and geometry integrity,2,2,pass", "R1,Source and geometry integrity,2,1,pass"), encoding="utf-8")
        gate_path = cases[6][1] / "gate-results.csv"
        gate_path.write_text(gate_path.read_text(encoding="utf-8").replace("G22,Progression authority remains bounded,pass", "G22,Progression authority remains bounded,fail"), encoding="utf-8")
        zero_path = cases[7][1] / "responsible-map-text-alternative.md"
        zero_path.write_text(zero_path.read_text(encoding="utf-8").replace("Gray means unavailable", "Gray means zero prevalence"), encoding="utf-8")
        merge_path = cases[8][1] / "responsible-map-context-memo.md"
        merge_path.write_text(merge_path.read_text(encoding="utf-8") + "\nThe public PLACES values are observed synthetic events.\n", encoding="utf-8")
        ranking_path = cases[9][1] / "progression-decision.md"
        ranking_path.write_text(ranking_path.read_text(encoding="utf-8").replace("- Tract ranking or priority label: `prohibited`.", "- Tract ranking or priority label: `permitted`."), encoding="utf-8")
        target_path = cases[10][1] / "progression-decision.md"
        target_path.write_text(target_path.read_text(encoding="utf-8").replace("- Targeting or eligibility: `prohibited`.", "- Targeting or eligibility: `permitted`."), encoding="utf-8")
        county_path = cases[11][1] / "aggregation-and-stability-review.md"
        county_path.write_text(county_path.read_text(encoding="utf-8").replace("They are not official county PLACES estimates.", "They are official county PLACES estimates."), encoding="utf-8")
        support_path = cases[12][1] / "aggregation-and-stability-review.md"
        support_path.write_text(support_path.read_text(encoding="utf-8").replace("The rule is not a CDC quality designation", "The rule is a CDC quality designation"), encoding="utf-8")
        svg_path = cases[13][1] / "outputs/responsible-diabetes-prevalence-map.svg"
        svg_path.write_text(svg_path.read_text(encoding="utf-8").replace('role="img"', 'role="presentation"', 1), encoding="utf-8")
        table_path = cases[14][1] / "outputs/tract-map-table.csv"
        table_path.write_text(table_path.read_text(encoding="utf-8").replace(",unavailable,unavailable,", ",0,unavailable," , 1), encoding="utf-8")
        with (cases[15][1] / "responsible-map-context-memo.md").open("a", encoding="utf-8") as handle:
            handle.write("\nAdults who live in darker tracts have diabetes.\n")
        with (cases[16][1] / "responsible-map-context-memo.md").open("a", encoding="utf-8") as handle:
            handle.write("\nThis failing community is deficient and should be fixed.\n")
        with (cases[17][1] / "ai-use.md").open("a", encoding="utf-8") as handle:
            handle.write("\nC:\\Users\\Example\\private.csv\n")
        release_path = cases[18][1] / "release.json"
        release_path.write_text(release_path.read_text(encoding="utf-8").replace("cf5386a255dc37c518e8410ea891f2f73726a95c13b65e22dbadf218ba6c1ae6", "0" * 64), encoding="utf-8")
        class_path = cases[19][1] / "aggregation-and-stability-review.md"
        class_path.write_text(class_path.read_text(encoding="utf-8").replace("| Less than 5.0% | 82 |", "| Less than 5.0% | 81 |"), encoding="utf-8")
        progression_path = cases[20][1] / "progression-decision.md"
        progression_path.write_text(progression_path.read_text(encoding="utf-8").replace("- Progression: `continue with conditions`.", "- Progression: `approved automatically`."), encoding="utf-8")
        deployment_path = cases[21][1] / "progression-decision.md"
        deployment_path.write_text(deployment_path.read_text(encoding="utf-8").replace("- Deployment: `prohibited`.", "- Deployment: `permitted`."), encoding="utf-8")
        for _, target in cases:
            expect_failure(target)

        copied = base / "copied-learner"
        shutil.copytree(learner, copied)
        for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
            shutil.copy2(reference / relative, copied / relative)
        expect_failure(copied, learner=True)
        expect_failure(learner)

        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        copied_run = subprocess.run(
            [sys.executable, str(reference / "validate_workspace.py"), str(reference)],
            text=True,
            capture_output=True,
            env=environment,
            check=False,
        )
        if copied_run.returncode:
            raise AssertionError(copied_run.stderr.strip() or copied_run.stdout.strip())
        assert complete_report["course_points"] == 10 and learner_report["course_points"] == 0
        assert len(cases) == EXPECTED_FAILURE_ROUTES
    print(
        "APP-5 Module 04 validator self-check passed: reference, learner, copied-validator, "
        f"copied-answer, complete-mode learner, and {EXPECTED_FAILURE_ROUTES} protected failure routes rejected."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            print(json.dumps(validate(args.workspace, learner=args.learner), indent=2, sort_keys=True))
        else:
            parser.error("workspace is required unless --self-check is used")
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError, ET.ParseError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

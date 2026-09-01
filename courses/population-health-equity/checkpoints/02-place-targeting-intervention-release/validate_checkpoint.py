"""Validate the APP-5 cumulative Week 6 checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

import build_checkpoint


CHECKPOINT_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b")
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = build_checkpoint.IMMUTABLE_FILES
WORK_FILES = build_checkpoint.WORK_FILES
MODULES = {
    "module-04": {
        "id": "oclc-app5-04",
        "version": "0.1.0",
        "commons_release": "0.91.0",
        "files": 287,
        "manifest_rows": 271,
        "manifest_bytes": 48575,
        "manifest_sha256": "c0300a2eff3fa9ede53eab4723fe7296cad341cf5f6e4e5e76fde25881652629",
        "points": 10,
        "gates": 22,
    },
    "module-05": {
        "id": "oclc-app5-05",
        "version": "0.1.0",
        "commons_release": "0.92.0",
        "files": 340,
        "manifest_rows": 318,
        "manifest_bytes": 62245,
        "manifest_sha256": "54da8bae1c36ae49397b278fc636f2b8e112f55406acbfc57c94a215087818da",
        "points": 15,
        "gates": 26,
    },
    "module-06": {
        "id": "oclc-app5-06",
        "version": "0.1.0",
        "commons_release": "0.93.0",
        "files": 403,
        "manifest_rows": 377,
        "manifest_bytes": 79357,
        "manifest_sha256": "2e9358d65c889e786db474de97e223982a8d238dba64ec283c6dc950ebb89e82",
        "points": 0,
        "gates": 34,
    },
}
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}
EXPECTED_MANIFEST_ROWS = 1030
EXPECTED_MANIFEST_BYTES = 249511
EXPECTED_MANIFEST_SHA256 = "6d403bfb0e4bb6f177400ae97a3b1d89cf968c35b24482f64cea6b927f397f83"
EXPECTED_NESTED_ROWS = 966
EXPECTED_FILES = 1051
EXPECTED_CHECKPOINT_GATES = 24
EXPECTED_DEFENSE_QUESTIONS = 16
EXPECTED_CONDITIONS = 14
EXPECTED_REVIEWERS = 18
EXPECTED_FAILURE_ROUTES = 14


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


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def markdown_field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\.?\s*$", text)
    return match.group(1).strip() if match else None


def validate_candidate(root: Path, require: Callable[[bool, str], None]) -> None:
    manifest_path = root / "candidate-manifest.csv"
    header, manifest = read_csv(manifest_path)
    require(
        header
        == [
            "relative_path",
            "bytes",
            "sha256",
            "source_module",
            "source_version",
            "role",
        ],
        "Candidate manifest header matches",
    )
    paths = [row["relative_path"] for row in manifest]
    require(
        len(manifest) == EXPECTED_MANIFEST_ROWS and paths == sorted(paths) and len(set(paths)) == len(paths),
        "Candidate manifest has 1,030 sorted unique rows",
    )
    require(
        all(
            path.startswith("candidate/module-0")
            and "\\" not in path
            and not Path(path).is_absolute()
            and ".." not in Path(path).parts
            for path in paths
        ),
        "Candidate paths are portable and traversal free",
    )
    require(
        manifest_path.stat().st_size == EXPECTED_MANIFEST_BYTES
        and sha256(manifest_path) == EXPECTED_MANIFEST_SHA256,
        "Candidate manifest release identity matches",
    )

    module_counts = {name: 0 for name in MODULES}
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        details = MODULES.get(directory)
        require(
            details is not None
            and row["source_module"] == details["id"]
            and row["source_version"] == details["version"]
            and row["role"] == "accepted reference workspace artifact",
            f"Candidate source identity matches: {row['relative_path']}",
        )
        module_counts[directory] += 1
    require(
        module_counts == {"module-04": 287, "module-05": 340, "module-06": 403},
        "Candidate module file counts match",
    )

    nested_total = 0
    for directory, details in MODULES.items():
        module_root = root / f"candidate/{directory}"
        nested_path = module_root / "release-manifest.csv"
        nested_header, nested = read_csv(nested_path)
        require(
            nested_header == ["relative_path", "bytes", "sha256", "role"],
            f"{directory} nested manifest header matches",
        )
        nested_paths = [row["relative_path"] for row in nested]
        require(
            len(nested) == details["manifest_rows"]
            and nested_paths == sorted(nested_paths)
            and len(set(nested_paths)) == len(nested_paths),
            f"{directory} nested manifest row count and order match",
        )
        require(
            nested_path.stat().st_size == details["manifest_bytes"]
            and sha256(nested_path) == details["manifest_sha256"],
            f"{directory} nested manifest release identity matches",
        )
        for row in nested:
            path = module_root / row["relative_path"]
            require(path.is_file(), f"Nested file exists: {directory}/{row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Nested bytes match: {directory}/{row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Nested SHA-256 matches: {directory}/{row['relative_path']}")
        nested_total += len(nested)
    require(nested_total == EXPECTED_NESTED_ROWS, "Three nested manifests protect 966 immutable rows")


def validate(root: Path, mode: str = "complete", verify_candidate: bool = True) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    require(mode in {"complete", "learner"}, "Validation mode is supported")
    require(root.is_dir(), "Checkpoint directory exists")
    required = set(IMMUTABLE_FILES) | set(WORK_FILES) | {"candidate-manifest.csv"}
    _, manifest = read_csv(root / "candidate-manifest.csv")
    expected = required | {row["relative_path"] for row in manifest}
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected and len(actual) == EXPECTED_FILES, "Checkpoint has exactly 1,051 expected files")
    if verify_candidate:
        validate_candidate(root, require)

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = read_json(root / "checkpoint-contract.json")
    release = read_json(root / "release.json")
    require(
        contract["checkpoint_id"] == "oclc-app5-cp02"
        and contract["version"] == "0.1.0"
        and contract["commons_release"] == "0.94.0"
        and release["checkpoint"]["id"] == "oclc-app5-cp02"
        and release["checkpoint"]["commons_release"] == "0.94.0",
        "Checkpoint and release identities match",
    )
    require(
        contract["course_points"] == 25
        and [module["points"] for module in contract["accepted_modules"]] == [10, 15, 0]
        and "adds zero points" in contract["point_source"],
        "Checkpoint point contract is 10 plus 15 plus zero",
    )
    require(
        contract["accepted_component_files"] == EXPECTED_MANIFEST_ROWS
        and contract["accepted_immutable_rows"] == EXPECTED_NESTED_ROWS
        and contract["package"]["candidate_manifest_bytes"] == EXPECTED_MANIFEST_BYTES
        and contract["package"]["candidate_manifest_sha256"] == EXPECTED_MANIFEST_SHA256
        and contract["package"]["assembled_files"] == EXPECTED_FILES,
        "Checkpoint package contract matches",
    )
    require(
        contract["required_gates"]
        == {
            "module04_place": 22,
            "module05_targeting_fairness": 26,
            "module06_intervention_monitoring_ml": 34,
            "checkpoint_integrity": 24,
        },
        "Checkpoint carries 82 inherited and 24 checkpoint gates",
    )
    require(all(value == "prohibited" for value in contract["authority"].values()), "Contract prohibits every real-world authority route")
    require(
        release["accepted_evidence"]["checkpoint_score"] == "25 of 25"
        and release["accepted_evidence"]["component_files"] == EXPECTED_MANIFEST_ROWS
        and release["accepted_evidence"]["immutable_rows"] == EXPECTED_NESTED_ROWS
        and release["accepted_evidence"]["checkpoint_gates"] == "24 of 24 pass"
        and release["accepted_evidence"]["intervention_ready_for_real_use"] is False
        and release["accepted_evidence"]["challenger_accepted"] is False
        and release["package"]["candidate_manifest_sha256"] == EXPECTED_MANIFEST_SHA256
        and release["validation"]["builder_self_check"] == "pass"
        and release["validation"]["validator_self_check"] == "pass"
        and release["validation"]["failure_routes_rejected"] == EXPECTED_FAILURE_ROUTES,
        "Release evidence and package metadata match",
    )

    module04 = root / "candidate/module-04"
    module04_release = read_json(module04 / "release.json")
    _, module04_score = read_csv(module04 / "week6-component-score.csv")
    _, module04_gates = read_csv(module04 / "gate-results.csv")
    require(
        module04_release["module_id"] == "oclc-app5-04"
        and module04_release["commons_release"] == "0.91.0"
        and module04_release["place_release"]["mapped_estimates"] == 1597
        and module04_release["place_release"]["geometry_only_unavailable"] == 23
        and module04_release["place_release"]["limited_support_review_tracts"] == 49
        and module04_release["place_release"]["tracts_changing_class_after_county_aggregation"] == 645
        and module04_release["map_release"]["exact_table_rows"] == 1620,
        "Accepted Module 04 place and map evidence matches",
    )
    require(
        module04_score[-1]["points_awarded"] == "10"
        and len(module04_gates) == 22
        and all(row["status"] == "pass" for row in module04_gates),
        "Accepted Module 04 score and gates pass",
    )

    module05 = root / "candidate/module-05"
    module05_release = read_json(module05 / "release.json")
    _, module05_score = read_csv(module05 / "week6-component-score.csv")
    _, module05_gates = read_csv(module05 / "gate-results.csv")
    require(
        module05_release["module_id"] == "oclc-app5-05"
        and module05_release["commons_release"] == "0.92.0"
        and module05_release["targeting_release"]["rules"] == 4
        and module05_release["targeting_release"]["assignment_rows"] == 6388
        and module05_release["targeting_release"]["awards_per_rule"] == 28
        and module05_release["targeting_release"]["sensitivity_variants"] == 20
        and module05_release["reference_decision"]["planning_candidate"].startswith("community-review rule"),
        "Accepted Module 05 targeting and fairness evidence matches",
    )
    require(
        module05_score[-1]["points_awarded"] == "15"
        and len(module05_gates) == 26
        and all(row["status"] == "pass" for row in module05_gates),
        "Accepted Module 05 score and gates pass",
    )

    module06 = root / "candidate/module-06"
    module06_release = read_json(module06 / "release.json")
    _, module06_gates = read_csv(module06 / "week6-gate-results.csv")
    require(
        module06_release["module_id"] == "oclc-app5-06"
        and module06_release["commons_release"] == "0.93.0"
        and module06_release["intervention_release"]["selected_tracts"] == 28
        and module06_release["intervention_release"]["staff_not_ready"] == 5
        and module06_release["intervention_release"]["high_travel"] == 12
        and module06_release["intervention_release"]["high_burden"] == 1
        and module06_release["intervention_release"]["monitoring_measures"] == 20
        and module06_release["intervention_release"]["monitoring_triggers"] == 6
        and module06_release["intervention_release"]["incident_tests"] == 23,
        "Accepted Module 06 intervention and monitoring evidence matches",
    )
    require(
        module06_release["challenger_release"]["candidate_rows"] == 1597
        and module06_release["challenger_release"]["features"] == 9
        and module06_release["challenger_release"]["clusters"] == 4
        and module06_release["challenger_release"]["alternate_seed_minimum_ari"] == 0.893633
        and module06_release["challenger_release"]["scaling_variant_median_ari"] == 0.11995481449421869
        and module06_release["challenger_release"]["selected_clusters"] == 2
        and module06_release["challenger_release"]["stable_for_bounded_questions"] is False
        and module06_release["reference_decision"]["challenger_accepted"] is False
        and module06_release["reference_decision"]["module06_points_added"] == 0
        and len(module06_gates) == 34
        and all(row["status"] == "pass" for row in module06_gates),
        "Accepted Module 06 challenger decision, zero points, and gates match",
    )

    mutable_text = {name: (root / name).read_text(encoding="utf-8") for name in WORK_FILES}
    require(all(not PERSONAL_PATH.search(text) for text in mutable_text.values()), "Checkpoint records contain no personal absolute path")
    require(all("—" not in text and "–" not in text for text in mutable_text.values()), "Checkpoint records use plain punctuation")
    if mode == "learner":
        require(all(PLACEHOLDER.search(text) for text in mutable_text.values()), "Every learner record contains an explicit placeholder")
    else:
        require(all(not PLACEHOLDER.search(text) for text in mutable_text.values()), "Reference records contain no placeholders")

    index_header, index = read_csv(root / "evidence-index.csv")
    require(
        index_header
        == [
            "module_id", "title", "module_version", "commons_release", "assembled_files",
            "manifest_rows", "manifest_bytes", "manifest_sha256", "checkpoint_points",
            "inherited_gates", "progression", "accepted_decision", "cumulative_role",
        ]
        and len(index) == 3
        and [row["module_id"] for row in index] == ["oclc-app5-04", "oclc-app5-05", "oclc-app5-06"],
        "Evidence index structure matches",
    )

    score_header, score = read_csv(root / "checkpoint-score.csv")
    require(
        score_header == ["source_module", "criterion_id", "criterion", "points_available", "points_awarded", "evidence"]
        and len(score) == 11
        and [row["source_module"] for row in score].count("oclc-app5-04") == 5
        and [row["source_module"] for row in score].count("oclc-app5-05") == 5
        and score[-1]["source_module"] == "checkpoint",
        "Checkpoint score structure matches",
    )
    gates_header, gates = read_csv(root / "checkpoint-gates.csv")
    require(
        gates_header == ["gate_id", "gate", "status", "evidence", "owner"]
        and len(gates) == EXPECTED_CHECKPOINT_GATES
        and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 25)],
        "Checkpoint has 24 ordered integrity gates",
    )
    defense = mutable_text["checkpoint-defense.md"]
    require(
        re.findall(r"(?m)^## Q(\d{2})\.", defense) == [f"{number:02d}" for number in range(1, 17)]
        and len(re.findall(r"(?m)^Answer:", defense)) == EXPECTED_DEFENSE_QUESTIONS
        and len(re.findall(r"(?m)^Evidence:", defense)) == EXPECTED_DEFENSE_QUESTIONS
        and len(re.findall(r"(?m)^Limit:", defense)) == EXPECTED_DEFENSE_QUESTIONS,
        "Checkpoint defense has 16 complete ordered answers",
    )
    _, conditions = read_csv(root / "conditions-register.csv")
    require(
        len(conditions) == EXPECTED_CONDITIONS
        and [row["condition_id"] for row in conditions] == [f"C{number:02d}" for number in range(1, 15)],
        "Conditions register has 14 ordered conditions",
    )
    reviewer = mutable_text["reviewer-record.md"]
    reviewer_status = "REPLACE" if mode == "learner" else "pending before alpha"
    require(
        len(re.findall(rf"(?m)^\| [^|]+ \| [^|]+ \| {re.escape(reviewer_status)} \|$", reviewer)) == EXPECTED_REVIEWERS,
        "Reviewer record has 18 required review roles",
    )

    if mode == "complete":
        require(
            [int(row["assembled_files"]) for row in index] == [287, 340, 403]
            and [int(row["manifest_rows"]) for row in index] == [271, 318, 377]
            and [int(row["checkpoint_points"]) for row in index] == [10, 15, 0]
            and [row["inherited_gates"] for row in index] == ["22 of 22 pass", "26 of 26 pass", "34 of 34 pass"],
            "Evidence index carries accepted files, manifests, points, and gates",
        )
        require(
            len(re.findall(r"(?m)^(?:Answer|Evidence|Limit):\s+\S", defense))
            == EXPECTED_DEFENSE_QUESTIONS * 3,
            "Every defense answer has nonempty answer, evidence, and limit text",
        )
        module04_points = sum(int(row["points_awarded"]) for row in score[:4])
        module05_points = sum(int(row["points_awarded"]) for row in score[5:9])
        require(
            module04_points == 10
            and score[4]["points_awarded"] == "10"
            and module05_points == 15
            and score[9]["points_awarded"] == "15"
            and score[10]["points_awarded"] == "25"
            and "non-additive" in score[10]["evidence"],
            "Module 04 and Module 05 points are counted once and total 25",
        )
        require(all(row["status"] == "pass" and row["evidence"] and row["owner"] for row in gates), "All 24 checkpoint gates pass with evidence and owners")
        require(
            all(row["status"] == "open" and row["owner"] and row["verifier"] and row["blocks"] == "alpha" for row in conditions),
            "All 14 conditions have owners, verifiers, and an alpha block",
        )

        review = mutable_text["place-targeting-intervention-readiness-review.md"]
        review_terms = (
            "1,030 candidate files", "966 immutable rows", "1,597 modeled PLACES", "23 geometry-only rows",
            "Forty-nine tracts", "Six hundred forty-five tracts", "280 places", "four rules",
            "6,388 assignment rows", "56 county consequence rows", "76 suppression-preserving group consequence rows",
            "20 sensitivity variants", "Five selected areas", "Twelve remain high travel", "one remains high burden",
            "20 implementation and monitoring measures", "six triggers", "14 objection tests", "23 incident tests",
            "Outcomes are unavailable", "0.893633", "0.11995481449421869", "only two clusters",
            "challenger is rejected", "25 of 25", "all 24 checkpoint integrity gates pass",
        )
        require(all(term in review for term in review_terms), "Cumulative review contains every accepted result")

        claims = mutable_text["responsible-claims-audit.md"]
        require(
            "not ready for real implementation" in claims
            and "fails its declared scaling-stability" in claims
            and "Unavailable map values" in claims
            and all(
                f"{label}: `prohibited" in claims
                for label in (
                    "Outcome claim", "Causal claim", "Individual inference", "Real need determination",
                    "Consent or eligibility", "Outreach", "Allocation or funding", "Real community action",
                    "Service delivery", "Intervention-effect estimation", "Automatic model action",
                    "Implementation", "Production connection", "Deployment",
                )
            ),
            "Responsible claims audit preserves evidence and authority boundaries",
        )
        require(
            markdown_field(reviewer, "Construction review date") == "2026-08-31"
            and markdown_field(reviewer, "Construction review result") == "complete for runnable release candidate"
            and markdown_field(reviewer, "Pre-alpha named review status") == "pending"
            and markdown_field(reviewer, "Release boundary") == "curriculum construction only",
            "Reviewer record separates construction completion from pending named review",
        )

        reproduction = mutable_text["reproducibility-check.md"]
        require(
            all(
                term in reproduction
                for term in (
                    "Candidate files: `1,030`", "Nested immutable rows: `966`", "Checkpoint files: `1,051`",
                    "Candidate manifest bytes: `249,511`", EXPECTED_MANIFEST_SHA256,
                    "10 + 15 + 0 = 25", "22 + 26 + 34 + 24 = 106",
                    "two builds match byte for byte", "Changed candidate: `rejected`",
                    "Intervention-ready mutation: `rejected`", "Accepted-challenger mutation: `rejected`",
                    "Implementation or deployment mutation: `rejected`", "pending before alpha",
                )
            ),
            "Reproducibility record covers assembly and protected mutations",
        )
        ai = mutable_text["ai-use.md"]
        ai_labels = (
            "Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected",
            "Output used, modified, or rejected", "Material claim", "Independent verification",
            "Correction or retained action", "Human owner", "Accountability statement",
        )
        require(all(markdown_field(ai, label) for label in ai_labels), "AI-use record has every accountable field")

        progression = mutable_text["progression-decision.md"]
        require(
            markdown_field(progression, "Checkpoint score") == "25 of 25"
            and markdown_field(progression, "Module 04 place gates") == "22 of 22 pass"
            and markdown_field(progression, "Module 05 targeting and fairness gates") == "26 of 26 pass"
            and markdown_field(progression, "Module 06 intervention, monitoring, and ML gates") == "34 of 34 pass"
            and markdown_field(progression, "Checkpoint integrity gates") == "24 of 24 pass"
            and markdown_field(progression, "Failed gates") == "none",
            "Progression score and gate totals are exact",
        )
        disposition = markdown_field(progression, "Progression")
        permission = markdown_field(progression, "Module 07 permission")
        require(
            disposition in ALLOWED_PROGRESSION
            and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction")),
            "Module 07 permission matches progression",
        )
        require(
            markdown_field(progression, "Final checkpoint permission") == "prohibited until Module 07 passes"
            and markdown_field(progression, "Intervention ready for real use") == "no"
            and markdown_field(progression, "Clustering challenger accepted") == "no"
            and all(
                markdown_field(progression, label) == "prohibited"
                for label in (
                    "Real need determination", "Consent or eligibility", "Outreach", "Allocation or funding",
                    "Real community action", "Service delivery", "Intervention-effect estimation",
                    "Automatic model action", "Implementation", "Production connection", "Deployment",
                )
            )
            and len(re.findall(r"(?m)^\| C\d{2} \|", progression)) == EXPECTED_CONDITIONS,
            "Progression preserves the final gate, intervention and model decisions, conditions, and authority limits",
        )

    return {
        "status": "pass",
        "mode": mode,
        "checks_passed": len(checks),
        "assembled_files": EXPECTED_FILES,
    }


def replace_bytes(path: Path, old: bytes, new: bytes) -> None:
    original = path.read_bytes()
    if old not in original:
        raise AssertionError(f"Mutation source not found in {path}: {old!r}")
    path.write_bytes(original.replace(old, new, 1))


def mutate_and_reject(
    root: Path,
    relative: str,
    mutate: Callable[[Path], None],
    label: str,
    verify_candidate: bool = False,
) -> None:
    path = root / relative
    original = path.read_bytes()
    try:
        mutate(path)
        try:
            validate(root, "complete", verify_candidate=verify_candidate)
        except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError):
            return
        raise AssertionError(f"Validator accepted protected failure: {label}")
    finally:
        path.write_bytes(original)


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-cp02-validator-") as temporary:
        base = Path(temporary)
        reference = base / "reference"
        learner = base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        build_checkpoint.assemble(learner, reference=False)
        complete = validate(reference, "complete")
        starter = validate(learner, "learner")
        try:
            validate(learner, "complete", verify_candidate=False)
        except ValidationError:
            pass
        else:
            raise AssertionError("Complete validation accepted a learner starter")
        try:
            validate(reference, "learner", verify_candidate=False)
        except ValidationError:
            pass
        else:
            raise AssertionError("Learner validation accepted complete reference records")

        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        copied = subprocess.run(
            [sys.executable, str(reference / "validate_checkpoint.py"), str(reference)],
            text=True,
            capture_output=True,
            env=environment,
            check=False,
        )
        if copied.returncode:
            raise AssertionError(copied.stderr.strip() or copied.stdout.strip())

        mutate_and_reject(reference, "candidate/module-04/VERSION", lambda p: p.write_text("0.1.1\n", encoding="utf-8"), "candidate mutation", True)
        mutate_and_reject(reference, "candidate-manifest.csv", lambda p: p.write_bytes(p.read_bytes() + b"\n"), "outer manifest mutation", True)
        mutate_and_reject(reference, "VERSION", lambda p: p.write_text("0.1.1\n", encoding="utf-8"), "checkpoint version mutation")
        mutate_and_reject(reference, "checkpoint-score.csv", lambda p: replace_bytes(p, b"checkpoint,SUMMARY,Cumulative Week 6 package,25,25", b"checkpoint,SUMMARY,Cumulative Week 6 package,25,30"), "point total mutation")
        mutate_and_reject(reference, "checkpoint-score.csv", lambda p: p.write_bytes(p.read_bytes() + p.read_bytes().splitlines(keepends=True)[1]), "duplicate score row")
        mutate_and_reject(reference, "checkpoint-gates.csv", lambda p: replace_bytes(p, b"G24,Module 07 permission is bounded and every real-world authority route remains prohibited,pass", b"G24,Module 07 permission is bounded and every real-world authority route remains prohibited,fail"), "failed gate")
        mutate_and_reject(reference, "place-targeting-intervention-readiness-review.md", lambda p: replace_bytes(p, b"Five selected areas remain staff-not-ready.", b"All areas are staff-ready."), "hidden capacity condition")
        mutate_and_reject(reference, "progression-decision.md", lambda p: replace_bytes(p, b"Intervention ready for real use: `no`", b"Intervention ready for real use: `yes`"), "intervention-ready mutation")
        mutate_and_reject(reference, "responsible-claims-audit.md", lambda p: replace_bytes(p, b"Outcome claim: `prohibited because outcomes are unavailable`", b"Outcome claim: `effect demonstrated`"), "outcome claim mutation")
        mutate_and_reject(reference, "progression-decision.md", lambda p: replace_bytes(p, b"Clustering challenger accepted: `no`", b"Clustering challenger accepted: `yes`"), "accepted challenger mutation")
        mutate_and_reject(reference, "checkpoint-gates.csv", lambda p: replace_bytes(p, b",clinician-leadership reviewer\n", b",\n"), "missing gate owner")
        mutate_and_reject(reference, "checkpoint-defense.md", lambda p: replace_bytes(p, b"Evidence: `candidate-manifest.csv` and the three nested `release-manifest.csv` files.", b"Evidence:"), "incomplete defense")
        mutate_and_reject(reference, "progression-decision.md", lambda p: replace_bytes(p, b"Module 07 permission: `permitted for curriculum construction`", b"Module 07 permission: `automatic approval`"), "invalid Module 07 permission")
        mutate_and_reject(reference, "progression-decision.md", lambda p: replace_bytes(p, b"Deployment: `prohibited`", b"Deployment: `permitted`"), "deployment authority")
        validate(reference, "complete", verify_candidate=False)

    print(json.dumps({
        "status": "pass",
        "complete_checks": complete["checks_passed"],
        "starter_checks": starter["checks_passed"],
        "protected_failure_routes": EXPECTED_FAILURE_ROUTES,
    }, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, default=CHECKPOINT_ROOT)
    parser.add_argument("--mode", choices=("complete", "learner"), default="complete")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        else:
            print(json.dumps(validate(args.workspace, args.mode), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

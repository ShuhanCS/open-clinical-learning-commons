"""Validate the APP-4 cumulative Week 3 checkpoint."""

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
from decimal import Decimal
from pathlib import Path
from typing import Callable


CHECKPOINT_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "assessment.md", "checkpoint-contract.json",
    "instructor-notes.md", "release.json", "build_checkpoint.py", "validate_checkpoint.py",
)
WORK_FILES = (
    "README.md", "evidence-index.csv", "logic-evidence-readiness-review.md",
    "checkpoint-score.csv", "checkpoint-gates.csv", "checkpoint-defense.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
)
MODULES = {
    "module-01": {
        "id": "oclc-app4-01", "version": "0.1.0", "commons_release": "0.77.0",
        "files": 41, "immutable_rows": 29, "manifest_bytes": 3404,
        "manifest_sha256": "40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45",
    },
    "module-02": {
        "id": "oclc-app4-02", "version": "0.1.0", "commons_release": "0.78.0",
        "files": 86, "immutable_rows": 73, "manifest_bytes": 10564,
        "manifest_sha256": "bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded",
    },
    "module-03": {
        "id": "oclc-app4-03", "version": "0.1.0", "commons_release": "0.79.0",
        "files": 118, "immutable_rows": 102, "manifest_bytes": 16354,
        "manifest_sha256": "e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22",
    },
}
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}


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


def markdown_field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, learner: bool = False) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    required = set(IMMUTABLE_FILES) | set(WORK_FILES) | {"candidate-manifest.csv"}
    require(root.is_dir(), "Checkpoint directory exists")
    header, manifest = read_csv(root / "candidate-manifest.csv")
    require(
        header == [
            "relative_path", "bytes", "sha256", "source_module", "source_version", "role"
        ],
        "Candidate manifest header matches",
    )
    require(
        len(manifest) == 245
        and [row["relative_path"] for row in manifest]
        == sorted(row["relative_path"] for row in manifest),
        "Candidate manifest has 245 sorted rows",
    )
    expected = required | {row["relative_path"] for row in manifest}
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected and len(actual) == 263, "Checkpoint has exactly 263 expected files")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(
            row["source_module"] == MODULES[directory]["id"]
            and row["source_version"] == MODULES[directory]["version"],
            f"Candidate source identity matches: {row['relative_path']}",
        )

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(
        contract["checkpoint_id"] == "oclc-app4-cp01"
        and contract["version"] == "0.1.0"
        and contract["commons_release"] == "0.80.0",
        "Checkpoint identity matches",
    )
    require(
        contract["course_points"] == 40
        and contract["point_source"]
        == "oclc-app4-02 20 points once plus oclc-app4-03 20 points once",
        "Checkpoint point contract matches",
    )
    require(
        contract["accepted_component_files"] == 245
        and contract["accepted_immutable_rows"] == 204
        and len(contract["accepted_modules"]) == 3,
        "Contract accepts 245 files and 204 immutable rows from three modules",
    )
    require(
        [module["points"] for module in contract["accepted_modules"]] == [0, 20, 20]
        and sum(module["points"] for module in contract["accepted_modules"]) == 40,
        "Contract assigns Module 01 zero points and Modules 02 and 03 20 points once",
    )
    require(
        contract["required_gates"] == {
            "module01_decision": 12, "module02_logic": 12,
            "module03_evidence": 12, "checkpoint_integrity": 20,
        },
        "Contract carries 36 inherited and 20 checkpoint gates",
    )
    require(
        contract["thresholds"]["evidence_candidates"] == [0.02, 0.03, 0.04, 0.05, 0.075, 0.10]
        and contract["thresholds"]["accepted"] is None
        and contract["thresholds"]["module02_mock"] == "0.20 rejected mechanics fixture",
        "Contract keeps six evidence candidates unaccepted and rejects the mechanics fixture",
    )

    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [
            path for path in module_root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        ]
        require(len(files) == details["files"], f"{directory} file count matches")
        require(
            (module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"],
            f"{directory} version matches",
        )
        release_path = module_root / "release.json"
        if release_path.is_file():
            release = json.loads(release_path.read_text(encoding="utf-8"))
            identity = (release["module_id"], release["module_version"], release["commons_release"])
        else:
            decision = json.loads((module_root / "decision-contract.json").read_text(encoding="utf-8"))["module"]
            identity = (decision["id"], decision["version"], decision["commons_release"])
        require(
            identity == (details["id"], details["version"], details["commons_release"]),
            f"{directory} release identity matches",
        )
        nested = module_root / "release-manifest.csv"
        require(nested.stat().st_size == details["manifest_bytes"], f"{directory} nested manifest bytes match")
        require(sha256(nested) == details["manifest_sha256"], f"{directory} nested manifest SHA-256 matches")
        nested_header, nested_rows = read_csv(nested)
        require(
            nested_header == ["relative_path", "bytes", "sha256", "role"],
            f"{directory} nested manifest header matches",
        )
        require(len(nested_rows) == details["immutable_rows"], f"{directory} nested immutable row count matches")
        for row in nested_rows:
            path = module_root / row["relative_path"]
            require(
                path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"],
                f"{directory} nested artifact matches: {row['relative_path']}",
            )

    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    manifest_path = root / "candidate-manifest.csv"
    require(
        release["checkpoint"]["id"] == "oclc-app4-cp01"
        and release["checkpoint"]["version"] == "0.1.0"
        and release["checkpoint"]["commons_release"] == "0.80.0",
        "Release identity matches",
    )
    require(
        release["package"]["candidate_manifest_rows"] == 245
        and release["package"]["candidate_manifest_bytes"] == manifest_path.stat().st_size
        and release["package"]["candidate_manifest_sha256"] == sha256(manifest_path)
        and release["package"]["checkpoint_editable_records"] == 9
        and release["package"]["defense_questions"] == 14
        and release["package"]["assembled_files"] == 263,
        "Release package identity matches",
    )

    for name in WORK_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 263}
        print(f"APP-4 Checkpoint 01 learner validation passed: {len(checks)} checks.")
        return report

    index_header, index_rows = read_csv(root / "evidence-index.csv")
    require(
        index_header == [
            "module_id", "title", "version", "commons_release", "assembled_files",
            "manifest_rows", "manifest_bytes", "manifest_sha256", "checkpoint_points",
            "gates", "progression", "accepted_decision", "role",
        ],
        "Evidence index header matches",
    )
    require(
        len(index_rows) == 3
        and [row["module_id"] for row in index_rows]
        == ["oclc-app4-01", "oclc-app4-02", "oclc-app4-03"],
        "Evidence index has three ordered modules",
    )
    require(
        [row["checkpoint_points"] for row in index_rows] == ["0", "20", "20"]
        and sum(Decimal(row["checkpoint_points"]) for row in index_rows) == Decimal("40"),
        "Evidence index assigns Module 01 zero points and Modules 02 and 03 20 points exactly once",
    )
    for row, details in zip(index_rows, MODULES.values(), strict=True):
        require(
            row["version"] == details["version"]
            and row["commons_release"] == details["commons_release"]
            and int(row["assembled_files"]) == details["files"]
            and int(row["manifest_rows"]) == details["immutable_rows"]
            and int(row["manifest_bytes"]) == details["manifest_bytes"]
            and row["manifest_sha256"] == details["manifest_sha256"],
            f"Evidence index identity matches: {row['module_id']}",
        )
    require(
        [row["gates"] for row in index_rows] == ["12 of 12 pass"] * 3,
        "Evidence index carries all inherited passing gates",
    )

    score_header, score = read_csv(root / "checkpoint-score.csv")
    require(
        score_header == [
            "component", "criterion_id", "criterion", "points_possible",
            "points_awarded", "evidence", "gate_status",
        ]
        and len(score) == 20,
        "Checkpoint score has the exact header and 20 rows",
    )
    module02_score = [row for row in score if row["component"] == "oclc-app4-02" and row["criterion_id"].startswith("L")]
    module03_score = [row for row in score if row["component"] == "oclc-app4-03" and row["criterion_id"].startswith("E")]
    require(
        len(module02_score) == 6
        and sum(Decimal(row["points_awarded"]) for row in module02_score) == Decimal("20")
        and all(row["points_awarded"] == row["points_possible"] for row in module02_score),
        "Module 02 component score totals 20 once",
    )
    require(
        len(module03_score) == 11
        and sum(Decimal(row["points_awarded"]) for row in module03_score) == Decimal("20")
        and all(row["points_awarded"] == row["points_possible"] for row in module03_score),
        "Module 03 component score totals 20 once",
    )
    total = next(row for row in score if row["component"] == "checkpoint" and row["criterion_id"] == "TOTAL")
    require(
        total["points_possible"] == "40" and total["points_awarded"] == "40"
        and all(row["gate_status"] in {"pass", "all 12 component gates pass", "all 56 gates pass"} for row in score),
        "Checkpoint score totals 40 with every gate status passing",
    )

    gates_header, gates = read_csv(root / "checkpoint-gates.csv")
    require(gates_header == ["gate_id", "gate", "status", "evidence", "owner"], "Checkpoint gate header matches")
    require(
        len(gates) == 20
        and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 21)]
        and all(row["status"] == "pass" for row in gates),
        "All 20 checkpoint integrity gates pass",
    )

    review = (root / "logic-evidence-readiness-review.md").read_text(encoding="utf-8")
    required_values = (
        "40 of 40", "245 files", "204 immutable rows", "16 complete official NHANES",
        "34,221,200", "3,149,043", "145,563", "442 inventoried fields", "CGH-GIM-01",
        "1,000 Massachusetts adults", "25 FHIR R4 files", "811,803", "100,178,478",
        "11,109", "0d3c4c11e5ab29284f312d76413f8e005fb957226039d324912f80af93dcf3c0",
        "All 16 synthetic mechanics cases", "14,892", "7,544", "328 observed",
        "3,652", "1,806", "2,086", "0.02904272", "0.03015261", "0.02811126",
        "0.12694930", "0.68783144", "-0.03946013", "0.88441129", "0.03274014",
        "0.03041245", "0.03175435", "0.14019059", "0.68422573", "0.07788522",
        "0.81620710", "661.57323641", "17.08750038", "2.99863880", "27.92703988",
        "500-replicate", "7400303", "eight subgroup", "11 suppress", "continue with conditions",
    )
    require(all(value in review for value in required_values), "Cumulative review contains exact accepted logic and evidence")
    review_lower = review.lower()
    require(
        "rejected mechanics fixture, not an evidence candidate" in review_lower
        and "all six evidence candidates remain unselected and unaccepted" in review_lower,
        "Cumulative review reconciles mechanics and evidence without accepting a threshold",
    )
    require(
        "rather than a diagnosis or confirmation of disease" in review_lower,
        "Cumulative review preserves the observed-target meaning",
    )
    require(
        "no retuning" in review_lower and "no pooling" in review_lower,
        "Cumulative review preserves partition and no-retuning limits",
    )
    require(
        "suppressed performance remains blank" in review_lower
        and "no group-specific threshold" in review_lower,
        "Cumulative review preserves subgroup suppression and action limits",
    )
    require(
        not re.search(
            r"(?i)0\.20 is accepted|accepted clinical threshold: 0\.|confirms a diabetes diagnosis|"
            r"score real patients|authorizes deployment",
            review,
        ),
        "Cumulative review contains no accepted-fixture, diagnosis, scoring, or deployment claim",
    )

    module01 = root / "candidate/module-01"
    _, sources = read_csv(module01 / "data/source-inventory.csv")
    require(
        len(sources) == 16
        and sum(int(row["raw_bytes"]) for row in sources) == 34221200
        and sum(int(row["gzip_bytes"]) for row in sources) == 3149043
        and sum(int(row["rows"]) for row in sources) == 145563
        and sum(int(row["seqn_duplicates"]) for row in sources) == 0,
        "Accepted Module 01 source totals match",
    )
    module01_contract = json.loads((module01 / "decision-contract.json").read_text(encoding="utf-8"))
    require(
        module01_contract["service"]["id"] == "CGH-GIM-01"
        and module01_contract["service"]["status"] == "fictional adult general internal medicine and primary care service"
        and module01_contract["assessment"]["course_points_awarded_here"] == 0
        and module01_contract["assessment"]["noncompensable_gates"] == 12,
        "Accepted Module 01 service, zero-point role, and gate total match",
    )

    module02 = root / "candidate/module-02"
    _, synthetic = read_csv(module02 / "data/synthetic-release/source-manifest.csv")
    require(
        len(synthetic) == 25
        and sum(int(row["rows"]) for row in synthetic) == 811803
        and sum(int(row["compressed_bytes"]) for row in synthetic) == 100178478
        and sum(int(row["duplicate_ids"]) for row in synthetic) == 11109
        and sum(int(row["parse_failures"]) for row in synthetic) == 0,
        "Accepted Module 02 synthetic release totals match",
    )
    _, rule_results = read_csv(module02 / "rule-test-results.csv")
    require(
        len(rule_results) == 16 and all(row["status"] == "pass" for row in rule_results),
        "Accepted Module 02 has 16 passing mechanics traces",
    )
    module02_contract = json.loads((module02 / "decision-contract.json").read_text(encoding="utf-8"))
    require(
        module02_contract["assessment"]["points"] == 20
        and module02_contract["assessment"]["noncompensable_gates"] == 12
        and "0.20 arbitrary mechanics-only fixture" in module02_contract["fixtures"]["threshold"]
        and module02_contract["authority"]["clinical_threshold_acceptance"] == "prohibited",
        "Accepted Module 02 point, gate, fixture, and authority contract matches",
    )

    module03 = root / "candidate/module-03"
    evidence_report = json.loads((module03 / "data/evidence/build-report.json").read_text(encoding="utf-8"))
    require(
        evidence_report["source_files"] == 16
        and evidence_report["age_eligible_rows"] == 14892
        and evidence_report["model_rows"] == 7544
        and evidence_report["model_events"] == 328
        and evidence_report["partitions"]["development"] == {"events": 156, "rows": 3652}
        and evidence_report["partitions"]["temporal_holdout"] == {"events": 97, "rows": 1806}
        and evidence_report["partitions"]["transport_stress"] == {"events": 75, "rows": 2086}
        and evidence_report["accepted_threshold"] is None,
        "Accepted Module 03 cohort, partition, and null-threshold evidence matches",
    )
    _, thresholds = read_csv(module03 / "data/evidence/threshold-audit.csv")
    candidates = sorted({
        row["threshold"] for row in thresholds
        if row["threshold_status"] == "evidence candidate, not selected or accepted"
    })
    require(
        candidates == ["0.02000000", "0.03000000", "0.04000000", "0.05000000", "0.07500000", "0.10000000"]
        and len([row for row in thresholds if row["threshold_status"] == "rejected Module 02 mechanics fixture"]) == 3,
        "Accepted Module 03 has six evidence candidates and three rejected fixture rows",
    )
    _, subgroups = read_csv(module03 / "data/evidence/subgroup-support.csv")
    suppressed = [row for row in subgroups if row["support_status"].startswith("suppress")]
    require(
        len(subgroups) == 48
        and len([row for row in subgroups if row["partition"] == "temporal_holdout" and row["support_status"] == "report with boundary"]) == 8
        and len([row for row in subgroups if row["partition"] == "temporal_holdout" and row["support_status"].startswith("suppress")]) == 8
        and len([row for row in subgroups if row["partition"] == "transport_stress" and row["support_status"] == "report with boundary"]) == 5
        and len([row for row in subgroups if row["partition"] == "transport_stress" and row["support_status"].startswith("suppress")]) == 11
        and all(not row["weighted_brier"] and not row["weighted_roc_auc"] for row in suppressed),
        "Accepted Module 03 subgroup support and suppression match",
    )
    _, invariants = read_csv(module03 / "data/evidence/invariants.csv")
    module03_contract = json.loads((module03 / "decision-contract.json").read_text(encoding="utf-8"))
    require(
        len(invariants) == 20 and all(row["status"] == "pass" for row in invariants)
        and module03_contract["assessment"]["points"] == 20
        and module03_contract["assessment"]["noncompensable_gates"] == 12
        and module03_contract["model"]["holdout_or_transport_fit_rows"] == 0
        and module03_contract["thresholds"]["accepted"] is None,
        "Accepted Module 03 invariants, points, gates, and no-retuning contract match",
    )

    defense = (root / "checkpoint-defense.md").read_text(encoding="utf-8")
    require(
        re.findall(r"(?m)^## Q(\d{2})\.", defense) == [f"{number:02d}" for number in range(1, 15)],
        "Checkpoint defense has 14 ordered questions",
    )
    require(
        len(re.findall(r"(?m)^Answer:", defense)) == 14
        and len(re.findall(r"(?m)^Evidence:", defense)) == 14
        and len(re.findall(r"(?m)^Limit:", defense)) == 14,
        "Checkpoint defense answers every question with evidence and a limit",
    )

    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    reproduction_terms = (
        "candidate files: `245`", "nested immutable rows: `204`", "checkpoint files: `263`",
        "module 01 has 0 points", "the sum is 40", "two independent reference builds match byte for byte",
        "- candidate mutation: `rejected`", "- missing-candidate mutation: `rejected`",
        "module 01 point mutation: `rejected`", "duplicate module 02 point mutation: `rejected`",
        "duplicate module 03 point mutation: `rejected`", "wrong-total mutation: `rejected`",
        "failed inherited gate: `rejected`", "failed checkpoint gate: `rejected`",
        "promoted `0.20` fixture: `rejected`", "accepted-threshold mutation: `rejected`",
        "diagnosis mutation: `rejected`", "holdout-retuning mutation: `rejected`",
        "transport-pooling mutation: `rejected`", "unsupported-subgroup mutation: `rejected`",
        "incomplete-defense mutation: `rejected`", "missing-ai-field mutation: `rejected`",
        "invalid-progression mutation: `rejected`", "real-patient scoring mutation: `rejected`",
        "deployment mutation: `rejected`", "pending before alpha",
    )
    require(all(term in reproduction for term in reproduction_terms), "Reproducibility record covers assembly and mutation routes")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(
        markdown_field(progression, "Checkpoint score") == "40 of 40"
        and markdown_field(progression, "Point source")
        == "Module 02 20 points once plus Module 03 20 points once",
        "Checkpoint score and point source are exact",
    )
    require(
        markdown_field(progression, "Module 01 decision gates") == "12 of 12 pass"
        and markdown_field(progression, "Module 02 logic gates") == "12 of 12 pass"
        and markdown_field(progression, "Module 03 evidence gates") == "12 of 12 pass"
        and markdown_field(progression, "Checkpoint integrity gates") == "20 of 20 pass"
        and markdown_field(progression, "Failed gates") == "none",
        "All inherited and checkpoint gate totals pass",
    )
    require(
        markdown_field(progression, "Accepted clinical threshold") == "none"
        and markdown_field(progression, "Module 02 mock threshold") == "0.20 rejected mechanics fixture",
        "Progression preserves null threshold acceptance and rejected fixture status",
    )
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 04 permission")
    require(
        disposition in ALLOWED_PROGRESSION
        and ((disposition in {"continue", "continue with conditions"})
             == (permission == "permitted for curriculum construction")),
        "Module 04 permission matches progression",
    )
    require(
        markdown_field(progression, "Module 05 permission") == "prohibited until Module 04 passes",
        "Module 05 remains gated by Module 04",
    )
    require(
        all(markdown_field(progression, label) == "prohibited" for label in (
            "Diagnosis", "Real-patient scoring", "Clinical alerting", "Clinical action",
            "Implementation", "Production connection", "Deployment",
        )),
        "Clinical, scoring, implementation, production, and deployment authority remain prohibited",
    )
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) == 10, "Progression has ten owned conditions")

    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = (
        "Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared",
        "Files affected", "Output used, modified, or rejected", "Material claim",
        "Independent verification", "Correction or retained action", "Human owner",
        "Accountability statement",
    )
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")

    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 263}
    print(f"APP-4 Checkpoint 01 reference validation passed: {len(checks)} checks.")
    return report


def expect_rejection(
    reference: Path,
    base: Path,
    name: str,
    mutate: Callable[[Path], None],
    message_fragment: str,
) -> None:
    broken = base / name
    # ponytail: hard-linked clones avoid copying the 200 MB candidate for every mutation route.
    shutil.copytree(reference, broken, copy_function=os.link)
    mutate(broken)
    try:
        validate(broken)
    except (OSError, ValidationError) as error:
        if message_fragment not in str(error):
            raise AssertionError(f"{name} failed for the wrong reason: {error}") from error
    else:
        raise AssertionError(f"Validator accepted {name}")


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"Mutation source not found in {path}: {old}")
    path.unlink()
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app4-cp01-validate-") as temporary:
        base = Path(temporary)
        reference, learner = base / "reference", base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run(
            [sys.executable, str(reference / "validate_checkpoint.py"), str(reference)],
            capture_output=True, text=True, check=False,
        )
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_checkpoint.assemble(learner)
        starter = validate(learner, learner=True)

        expect_rejection(
            reference, base, "changed-candidate",
            lambda root: replace(root / "candidate/module-03/data/evidence/invariants.csv", "INV20", "INV99"),
            "Candidate SHA-256 matches",
        )
        expect_rejection(
            reference, base, "missing-candidate",
            lambda root: (root / "candidate/module-03/data/evidence/invariants.csv").unlink(),
            "Checkpoint has exactly 263 expected files",
        )
        expect_rejection(
            reference, base, "changed-module01-points",
            lambda root: replace(root / "evidence-index.csv", ",0,12 of 12 pass", ",1,12 of 12 pass"),
            "points exactly once",
        )
        expect_rejection(
            reference, base, "duplicate-module02-points",
            lambda root: replace(root / "evidence-index.csv", ",20,12 of 12 pass,continue with conditions,Module 03", ",40,12 of 12 pass,continue with conditions,Module 03"),
            "points exactly once",
        )
        expect_rejection(
            reference, base, "duplicate-module03-points",
            lambda root: replace(root / "checkpoint-score.csv", "oclc-app4-03,E01,cohort and target,2,2", "oclc-app4-03,E01,cohort and target,2,22"),
            "Module 03 component score totals 20 once",
        )
        expect_rejection(
            reference, base, "wrong-total",
            lambda root: replace(root / "checkpoint-score.csv", "checkpoint,TOTAL,Week 3 checkpoint total,40,40", "checkpoint,TOTAL,Week 3 checkpoint total,40,39"),
            "Checkpoint score totals 40",
        )
        expect_rejection(
            reference, base, "failed-inherited-gate",
            lambda root: replace(root / "evidence-index.csv", "12 of 12 pass", "11 of 12 pass"),
            "inherited passing gates",
        )
        expect_rejection(
            reference, base, "failed-checkpoint-gate",
            lambda root: replace(root / "checkpoint-gates.csv", ",pass,", ",fail,"),
            "20 checkpoint integrity gates pass",
        )
        expect_rejection(
            reference, base, "promoted-fixture",
            lambda root: replace(root / "logic-evidence-readiness-review.md", "rejected mechanics fixture, not an evidence candidate", "accepted clinical threshold and evidence candidate"),
            "reconciles mechanics and evidence",
        )
        expect_rejection(
            reference, base, "accepted-threshold",
            lambda root: replace(root / "progression-decision.md", "- Accepted clinical threshold: `none`", "- Accepted clinical threshold: `0.05`"),
            "null threshold acceptance",
        )
        expect_rejection(
            reference, base, "diagnosis-claim",
            lambda root: replace(root / "logic-evidence-readiness-review.md", "rather than a diagnosis or confirmation of disease", "and confirms a diabetes diagnosis"),
            "observed-target meaning",
        )
        expect_rejection(
            reference, base, "holdout-retuning",
            lambda root: replace(root / "logic-evidence-readiness-review.md", "and no retuning", "and retuned after review"),
            "partition and no-retuning limits",
        )
        expect_rejection(
            reference, base, "transport-pooling",
            lambda root: replace(root / "logic-evidence-readiness-review.md", "and no pooling", "and pooled with development"),
            "partition and no-retuning limits",
        )
        expect_rejection(
            reference, base, "unsupported-subgroup",
            lambda root: replace(root / "logic-evidence-readiness-review.md", "Suppressed performance remains blank.", "Suppressed performance is reported."),
            "subgroup suppression",
        )
        expect_rejection(
            reference, base, "incomplete-defense",
            lambda root: replace(root / "checkpoint-defense.md", "Answer: APP-4 Modules", "Response: APP-4 Modules"),
            "answers every question",
        )
        expect_rejection(
            reference, base, "missing-ai-field",
            lambda root: replace(root / "ai-use.md", "- Human owner: `Shuhan He and the named APP-4 faculty owner`", "- Human owner: ``"),
            "every accountable field",
        )
        expect_rejection(
            reference, base, "invalid-progression",
            lambda root: replace(root / "progression-decision.md", "- Module 04 permission: `permitted for curriculum construction`", "- Module 04 permission: `not permitted`"),
            "permission matches progression",
        )
        expect_rejection(
            reference, base, "real-patient-scoring",
            lambda root: replace(root / "progression-decision.md", "- Real-patient scoring: `prohibited`", "- Real-patient scoring: `permitted`"),
            "authority remain prohibited",
        )
        expect_rejection(
            reference, base, "deployment-claim",
            lambda root: replace(root / "progression-decision.md", "- Deployment: `prohibited`", "- Deployment: `permitted`"),
            "authority remain prohibited",
        )
        expect_rejection(
            reference, base, "missing-reproduction-route",
            lambda root: replace(root / "reproducibility-check.md", "- Candidate mutation: `rejected`.\n", ""),
            "mutation routes",
        )
        try:
            validate(learner)
        except ValidationError as error:
            assert "Reference record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted learner prompts as complete")

    print(
        f"APP-4 Checkpoint 01 validator self-check passed: {complete['checks_passed']} reference checks "
        f"and {starter['checks_passed']} learner checks; copied validation and 20 failure routes verified."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.checkpoint:
            validate(args.checkpoint, learner=args.learner)
        else:
            parser.error("checkpoint is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

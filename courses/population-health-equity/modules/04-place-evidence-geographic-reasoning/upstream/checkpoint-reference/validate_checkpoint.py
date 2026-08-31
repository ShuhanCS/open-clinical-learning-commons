"""Validate the APP-5 cumulative Week 3 checkpoint."""

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
from pathlib import Path
from typing import Callable


CHECKPOINT_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes",
    "VERSION",
    "assessment.md",
    "checkpoint-contract.json",
    "instructor-notes.md",
    "release.json",
    "build_checkpoint.py",
    "validate_checkpoint.py",
)
WORK_FILES = (
    "README.md",
    "evidence-index.csv",
    "measures-disparities-readiness-review.md",
    "checkpoint-score.csv",
    "checkpoint-gates.csv",
    "responsible-claims-audit.md",
    "checkpoint-defense.md",
    "reviewer-record.md",
    "conditions-register.csv",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-decision.md",
)
MODULES = {
    "module-01": {
        "id": "oclc-app5-01",
        "version": "0.1.0",
        "commons_release": "0.87.0",
        "files": 27,
        "manifest_rows": 16,
        "manifest_bytes": 1907,
        "manifest_sha256": "65ea81f391ed426f63e84593588d57542e827f89f2493aa0b3a2f8b1d9a2b0e9",
        "points": 0,
        "gates": "12 of 12 pass",
    },
    "module-02": {
        "id": "oclc-app5-02",
        "version": "0.1.0",
        "commons_release": "0.88.0",
        "files": 72,
        "manifest_rows": 57,
        "manifest_bytes": 7588,
        "manifest_sha256": "330b4e9ba5071ad4529d46f4af5b15555e8db84ef1718de2a8de42d0aa76a4b0",
        "points": 20,
        "gates": "15 of 15 pass",
    },
    "module-03": {
        "id": "oclc-app5-03",
        "version": "0.1.0",
        "commons_release": "0.89.0",
        "files": 120,
        "manifest_rows": 104,
        "manifest_bytes": 15465,
        "manifest_sha256": "d9591e028ba49d79762d444d769821dc21055a712aceda3f501c0e31bb7d24b8",
        "points": 20,
        "gates": "18 of 18 pass",
    },
}
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}
EXPECTED_MANIFEST_BYTES = 41641
EXPECTED_MANIFEST_SHA256 = "b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192"


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
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\.?\s*$", text)
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
    require(
        len(manifest) == 219
        and [row["relative_path"] for row in manifest]
        == sorted(row["relative_path"] for row in manifest),
        "Candidate manifest has 219 sorted rows",
    )
    expected = required | {row["relative_path"] for row in manifest}
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected and len(actual) == 240, "Checkpoint has exactly 240 expected files")
    require(
        (root / "candidate-manifest.csv").stat().st_size == EXPECTED_MANIFEST_BYTES
        and sha256(root / "candidate-manifest.csv") == EXPECTED_MANIFEST_SHA256,
        "Candidate manifest release identity matches",
    )

    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(
            path.stat().st_size == int(row["bytes"]),
            f"Candidate bytes match: {row['relative_path']}",
        )
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(
            row["source_module"] == MODULES[directory]["id"]
            and row["source_version"] == MODULES[directory]["version"]
            and row["role"] == "accepted reference workspace artifact",
            f"Candidate source identity matches: {row['relative_path']}",
        )

    nested_rows = 0
    for directory, details in MODULES.items():
        module_root = root / f"candidate/{directory}"
        nested_path = module_root / "release-manifest.csv"
        nested_header, nested = read_csv(nested_path)
        require(
            nested_header == ["relative_path", "bytes", "sha256", "role"],
            f"{directory} nested manifest header matches",
        )
        require(
            len(nested) == details["manifest_rows"]
            and [row["relative_path"] for row in nested]
            == sorted(row["relative_path"] for row in nested),
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
            require(
                path.stat().st_size == int(row["bytes"]),
                f"Nested bytes match: {directory}/{row['relative_path']}",
            )
            require(
                sha256(path) == row["sha256"],
                f"Nested SHA-256 matches: {directory}/{row['relative_path']}",
            )
        nested_rows += len(nested)
    require(nested_rows == 177, "Three nested manifests protect 177 immutable rows")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    require(
        contract["checkpoint_id"] == "oclc-app5-cp01"
        and contract["version"] == "0.1.0"
        and contract["commons_release"] == "0.90.0"
        and release["checkpoint"]["id"] == "oclc-app5-cp01"
        and release["checkpoint"]["commons_release"] == "0.90.0",
        "Checkpoint and release identities match",
    )
    require(
        contract["course_points"] == 40
        and contract["point_source"]
        == "oclc-app5-02 20 points once plus oclc-app5-03 20 points once"
        and [module["points"] for module in contract["accepted_modules"]] == [0, 20, 20],
        "Checkpoint point contract is zero plus 20 plus 20",
    )
    require(
        contract["accepted_component_files"] == 219
        and contract["accepted_immutable_rows"] == 177
        and contract["package"]["candidate_manifest_bytes"] == EXPECTED_MANIFEST_BYTES
        and contract["package"]["candidate_manifest_sha256"] == EXPECTED_MANIFEST_SHA256
        and contract["package"]["assembled_files"] == 240,
        "Checkpoint package contract matches",
    )
    require(
        contract["required_gates"]
        == {
            "module01_decision": 12,
            "module02_measures": 15,
            "module03_disparities": 18,
            "checkpoint_integrity": 22,
        },
        "Checkpoint carries 45 inherited and 22 checkpoint gates",
    )
    require(
        all(value == "prohibited" for value in contract["authority"].values()),
        "Contract prohibits every real-world authority route",
    )
    require(
        release["accepted_evidence"]["checkpoint_score"] == "40 of 40"
        and release["accepted_evidence"]["component_files"] == 219
        and release["accepted_evidence"]["immutable_rows"] == 177
        and release["accepted_evidence"]["adult_denominator"] == 5679768
        and release["accepted_evidence"]["synthetic_events"] == 283614
        and release["accepted_evidence"]["suppressed_cells"] == 21230
        and release["package"]["candidate_manifest_sha256"] == EXPECTED_MANIFEST_SHA256
        and release["validation"]["builder_self_check"] == "pass"
        and release["validation"]["validator_self_check"] == "pass"
        and release["validation"]["complete_reference_checks"] == 1460
        and release["validation"]["starter_checks"] == 1446
        and release["validation"]["failure_routes_rejected"] == 27,
        "Release evidence and package metadata match",
    )

    module01 = root / "candidate/module-01"
    module01_contract = json.loads((module01 / "decision-contract.json").read_text(encoding="utf-8"))
    _, sources = read_csv(module01 / "data/source-inventory.csv")
    _, fields = read_csv(module01 / "data/field-inventory.csv")
    _, joins = read_csv(module01 / "data/join-feasibility.csv")
    require(
        module01_contract["module"]["id"] == "oclc-app5-01"
        and module01_contract["case"]["id"] == "FMA-DP-01"
        and module01_contract["assessment"]["course_points_awarded_here"] == 0
        and module01_contract["assessment"]["noncompensable_gates"] == 12,
        "Accepted Module 01 identity, fictional case, points, and gates match",
    )
    require(
        len(sources) == 3
        and len(fields) == 282
        and len(joins) == 3
        and [row["intersection"] for row in joins] == ["1597", "1597", "1613"],
        "Accepted Module 01 source inventory and joins match",
    )

    module02 = root / "candidate/module-02"
    module02_release = json.loads((module02 / "release.json").read_text(encoding="utf-8"))
    module02_contract = json.loads((module02 / "measure-contract.json").read_text(encoding="utf-8"))
    _, module02_queries = read_csv(module02 / "outputs/query-checks.csv")
    _, module02_reconciliation = read_csv(module02 / "outputs/source-reconciliation.csv")
    _, module02_score = read_csv(module02 / "measure-score.csv")
    _, module02_gates = read_csv(module02 / "gate-results.csv")
    require(
        module02_release["module_id"] == "oclc-app5-02"
        and module02_release["source_release"]["rows"] == 7985
        and module02_release["source_release"]["adult_denominator"] == 5679768
        and module02_release["source_release"]["synthetic_events"] == 283614
        and module02_release["measure_release"]["direct_rates_available"] == 1576
        and module02_release["measure_release"]["direct_rates_unavailable"] == 21
        and module02_release["measure_release"]["guided_indirect_required"] == 80,
        "Accepted Module 02 denominator and measure release matches",
    )
    require(
        module02_contract["assessment"]["points"] == 20
        and module02_contract["assessment"]["noncompensable_gates"] == 15
        and len(module02_queries) == 30
        and all(row["status"] == "pass" for row in module02_queries)
        and len(module02_reconciliation) == 8
        and all(row["status"] == "pass" for row in module02_reconciliation)
        and module02_score[-1]["points_awarded"] == "20"
        and len(module02_gates) == 15
        and all(row["status"] == "pass" for row in module02_gates),
        "Accepted Module 02 score, gates, queries, and reconciliation pass",
    )

    module03 = root / "candidate/module-03"
    module03_release = json.loads((module03 / "release.json").read_text(encoding="utf-8"))
    module03_contract = json.loads((module03 / "disparity-contract.json").read_text(encoding="utf-8"))
    _, module03_queries = read_csv(module03 / "outputs/query-checks.csv")
    _, module03_reconciliation = read_csv(module03 / "outputs/equity-margin-reconciliation.csv")
    _, suppression_audit = read_csv(module03 / "outputs/complementary-suppression-audit.csv")
    _, module03_score = read_csv(module03 / "week3-component-score.csv")
    _, module03_gates = read_csv(module03 / "gate-results.csv")
    require(
        module03_release["module_id"] == "oclc-app5-03"
        and module03_release["source_release"]["dimensions"] == 3
        and module03_release["source_release"]["groups"] == 19
        and module03_release["source_release"]["margin_rows"] == 151715
        and module03_release["source_release"]["completeness_rows"] == 7985
        and module03_release["disparity_release"]["group_age_rates"] == 110
        and module03_release["disparity_release"]["standardized_group_rates"] == 22
        and module03_release["disparity_release"]["disparity_comparisons"] == 32
        and module03_release["disparity_release"]["summary_disparities"] == 6,
        "Accepted Module 03 source and disparity release matches",
    )
    require(
        module03_contract["assessment"]["points"] == 20
        and module03_contract["assessment"]["noncompensable_gates"] == 18
        and module03_contract["suppression"]["primary_suppressed_cells"] == 19742
        and module03_contract["suppression"]["complementary_suppressed_cells"] == 1488
        and module03_contract["suppression"]["publishable_cells"] == 9113
        and module03_contract["suppression"]["tract_totals_published"] is False,
        "Accepted Module 03 point and suppression contract matches",
    )
    require(
        len(module03_queries) == 36
        and all(row["status"] == "pass" for row in module03_queries)
        and len(module03_reconciliation) == 12
        and all(row["status"] == "pass" for row in module03_reconciliation)
        and len(suppression_audit) == 4791
        and all(row["status"] == "pass" for row in suppression_audit)
        and module03_score[-1]["points_awarded"] == "20"
        and len(module03_gates) == 18
        and all(row["status"] == "pass" for row in module03_gates),
        "Accepted Module 03 score, gates, queries, reconciliation, and suppression audits pass",
    )

    mutable_text = {
        name: (root / name).read_text(encoding="utf-8") for name in WORK_FILES
    }
    require(
        all(not PERSONAL_PATH.search(text) for text in mutable_text.values()),
        "Checkpoint records contain no personal absolute path",
    )
    if learner:
        require(
            all(PLACEHOLDER.search(text) for text in mutable_text.values()),
            "Every learner record contains an explicit placeholder",
        )
    else:
        require(
            all(not PLACEHOLDER.search(text) for text in mutable_text.values()),
            "Reference records contain no placeholders",
        )

    index_header, index = read_csv(root / "evidence-index.csv")
    require(
        len(index) == 3
        and [row["module_id"] for row in index]
        == ["oclc-app5-01", "oclc-app5-02", "oclc-app5-03"]
        and [int(row["assembled_files"]) for row in index] == [27, 72, 120]
        and [int(row["manifest_rows"]) for row in index] == [16, 57, 104]
        and [int(row["checkpoint_points"]) for row in index] == [0, 20, 20],
        "Evidence index carries three accepted module identities and points exactly once",
    )
    require(
        index_header
        == [
            "module_id",
            "title",
            "module_version",
            "commons_release",
            "assembled_files",
            "manifest_rows",
            "manifest_bytes",
            "manifest_sha256",
            "checkpoint_points",
            "inherited_gates",
            "progression",
            "accepted_decision",
            "cumulative_role",
        ],
        "Evidence index header matches",
    )

    score_header, score = read_csv(root / "checkpoint-score.csv")
    require(
        score_header
        == [
            "source_module",
            "criterion_id",
            "criterion",
            "points_available",
            "points_awarded",
            "evidence",
        ]
        and len(score) == 13
        and [row["source_module"] for row in score].count("oclc-app5-02") == 6
        and [row["source_module"] for row in score].count("oclc-app5-03") == 6,
        "Checkpoint score carries ten criteria, two subtotals, and one total",
    )
    gates_header, gates = read_csv(root / "checkpoint-gates.csv")
    require(
        gates_header == ["gate_id", "gate", "status", "evidence", "owner"]
        and len(gates) == 22
        and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 23)],
        "Checkpoint has 22 ordered integrity gates",
    )

    defense = mutable_text["checkpoint-defense.md"]
    require(
        re.findall(r"(?m)^## Q(\d{2})\.", defense)
        == [f"{number:02d}" for number in range(1, 16)],
        "Checkpoint defense has 15 ordered questions",
    )
    require(
        len(re.findall(r"(?m)^Answer:", defense)) == 15
        and len(re.findall(r"(?m)^Evidence:", defense)) == 15
        and len(re.findall(r"(?m)^Limit:", defense)) == 15,
        "Checkpoint defense answers every question with evidence and a limit",
    )
    _, conditions = read_csv(root / "conditions-register.csv")
    require(
        len(conditions) == 12
        and [row["condition_id"] for row in conditions]
        == [f"C{number:02d}" for number in range(1, 13)],
        "Conditions register has 12 ordered conditions",
    )
    reviewer = mutable_text["reviewer-record.md"]
    require(
        len(re.findall(r"(?m)^\| [^|]+ \| [^|]+ \| (?:pending before alpha|REPLACE) \|$", reviewer))
        == 17,
        "Reviewer record has 17 required review roles",
    )

    if not learner:
        require(
            [row["inherited_gates"] for row in index]
            == ["12 of 12 pass", "15 of 15 pass", "18 of 18 pass"]
            and all(row["progression"] == "continue with conditions" for row in index),
            "Evidence index carries all inherited passing gates and progressions",
        )
        module02_awarded = sum(int(row["points_awarded"]) for row in score[:5])
        module03_awarded = sum(int(row["points_awarded"]) for row in score[6:11])
        require(
            module02_awarded == 20
            and score[5]["points_awarded"] == "20"
            and module03_awarded == 20
            and score[11]["points_awarded"] == "20"
            and score[12]["points_awarded"] == "40",
            "Module 02 and Module 03 contribute 20 points once and total 40",
        )
        require(
            all(row["status"] == "pass" and row["evidence"] and row["owner"] for row in gates),
            "All 22 checkpoint integrity gates pass with evidence and owners",
        )
        require(
            all(
                row["status"] == "open"
                and row["owner"]
                and row["verifier"]
                and row["blocks"] == "alpha"
                for row in conditions
            ),
            "All 12 conditions have owners, verifiers, and an alpha block",
        )

        review = mutable_text["measures-disparities-readiness-review.md"]
        review_terms = (
            "219 files",
            "177 immutable rows",
            "40 of 40",
            "5,679,768",
            "283,614",
            "1,576 available direct standardized rates",
            "21 unavailable direct rates",
            "Eighty tracts",
            "151,715",
            "110 group-age rates",
            "22 standardized group rates",
            "32 reference comparisons",
            "six summary disparity records",
            "6,000 missing",
            "7,578 missing",
            "5,314 missing",
            "8,376 missing",
            "eight-row register",
            "19,742",
            "1,488",
            "21,230",
            "4,791",
        )
        require(all(term in review for term in review_terms), "Cumulative review contains every accepted result")
        require(
            "The accepted adult denominator totals 5,679,768 across five age bands." in review
            and "It reports absolute and relative differences, a summary measure, support, intervals, and both declared and overall references." in review
            and "never combined with the synthetic event numerator" in review
            and "cannot be joined to estimate an intersectional group" in review
            and "Zero conditioned geography missingness does not prove perfect geographic capture" in review
            and "An unavailable rate remains unavailable. It is not zero." in review
            and "Tract totals are not published" in review,
            "Cumulative review preserves evidence, missingness, and suppression limits",
        )

        claims = mutable_text["responsible-claims-audit.md"]
        require(
            "bounded disparity statement is supported only for the fictional synthetic release" in claims
            and "Intersectional claim: `prohibited because the three dimensions are separate margins rather than joint person records`" in claims
            and "blank protected values are unavailable rather than zero" in claims
            and all(
                f"{label}: `prohibited`" in claims
                for label in (
                    "Real disparity claim",
                    "Causal claim",
                    "Mapping in this checkpoint",
                    "Tract ranking",
                    "Targeting, eligibility, or outreach",
                    "Allocation or funding",
                    "Model fitting or intervention-effect estimation",
                    "Real community action",
                )
            ),
            "Responsible claims audit preserves all evidence and authority boundaries",
        )

        require(
            markdown_field(reviewer, "Construction review date") == "2026-08-31"
            and markdown_field(reviewer, "Construction review result")
            == "complete for runnable release candidate"
            and markdown_field(reviewer, "Pre-alpha named review status") == "pending"
            and markdown_field(reviewer, "Release boundary") == "curriculum construction only",
            "Reviewer record separates construction completion from pending named review",
        )

        reproduction = mutable_text["reproducibility-check.md"]
        reproduction_terms = (
            "Candidate files: `219`",
            "Nested immutable rows: `177`",
            "Checkpoint files: `240`",
            "Candidate manifest bytes: `41,641`",
            EXPECTED_MANIFEST_SHA256,
            "the sum is 40",
            "two independent reference builds match byte for byte",
            "Changed candidate: `rejected`",
            "Public-synthetic merge: `rejected`",
            "Intersectional-claim mutation: `rejected`",
            "Suppressed-zero mutation: `rejected`",
            "Reconstructable-total mutation: `rejected`",
            "Real-disparity mutation: `rejected`",
            "Deployment mutation: `rejected`",
            "Missing-reproduction-route mutation: `rejected`",
            "pending before alpha",
        )
        require(all(term in reproduction for term in reproduction_terms), "Reproducibility record covers assembly and mutation routes")

        ai = mutable_text["ai-use.md"]
        ai_labels = (
            "Tool and model",
            "Date",
            "Purpose",
            "Prompt or task",
            "Data classes shared",
            "Files affected",
            "Output used, modified, or rejected",
            "Material claim",
            "Independent verification",
            "Correction or retained action",
            "Human owner",
            "Accountability statement",
        )
        require(all(markdown_field(ai, label) for label in ai_labels), "AI-use record has every accountable field")

        progression = mutable_text["progression-decision.md"]
        require(
            markdown_field(progression, "Checkpoint score") == "40 of 40"
            and markdown_field(progression, "Point source")
            == "Module 02 20 points once plus Module 03 20 points once"
            and markdown_field(progression, "Module 01 decision gates") == "12 of 12 pass"
            and markdown_field(progression, "Module 02 measure gates") == "15 of 15 pass"
            and markdown_field(progression, "Module 03 disparity gates") == "18 of 18 pass"
            and markdown_field(progression, "Checkpoint integrity gates") == "22 of 22 pass"
            and markdown_field(progression, "Failed gates") == "none",
            "Progression score and all gate totals are exact",
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
            markdown_field(progression, "Module 05 permission")
            == "prohibited until Module 04 passes"
            and all(
                markdown_field(progression, label) == "prohibited"
                for label in (
                    "Real disparity claim",
                    "Intersectional claim",
                    "Mapping in this checkpoint",
                    "Tract ranking",
                    "Targeting or eligibility",
                    "Outreach",
                    "Allocation or funding",
                    "Model fitting",
                    "Intervention-effect estimation",
                    "Real community action",
                    "Implementation",
                    "Production connection",
                    "Deployment",
                )
            ),
            "Progression preserves the Module 05 gate and all authority prohibitions",
        )
        require(
            len(re.findall(r"(?m)^\| C\d{2} ", progression)) == 12,
            "Progression record carries all 12 open conditions",
        )

    report = {
        "status": "pass",
        "mode": "learner" if learner else "reference",
        "checks_passed": len(checks),
        "assembled_files": 240,
    }
    print(
        f"APP-5 Checkpoint 01 {report['mode']} validation passed: "
        f"{len(checks)} checks."
    )
    return report


def expect_rejection(
    reference: Path,
    base: Path,
    name: str,
    mutate: Callable[[Path], None],
    message_fragment: str,
) -> None:
    broken = base / name
    # ponytail: hard-linked clones keep 27 mutation routes fast; unlink before rewriting.
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

    with tempfile.TemporaryDirectory(prefix="app5-cp01-validate-") as temporary:
        base = Path(temporary)
        reference = base / "reference"
        learner = base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run(
            [sys.executable, str(reference / "validate_checkpoint.py"), str(reference)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_checkpoint.assemble(learner)
        starter = validate(learner, learner=True)

        routes: tuple[tuple[str, Callable[[Path], None], str], ...] = (
            (
                "changed-candidate",
                lambda root: replace(root / "candidate/module-03/outputs/query-checks.csv", "Q01", "Q99"),
                "Candidate SHA-256 matches",
            ),
            (
                "missing-candidate",
                lambda root: (root / "candidate/module-03/outputs/query-checks.csv").unlink(),
                "Checkpoint has exactly 240 expected files",
            ),
            (
                "changed-module01-points",
                lambda root: replace(root / "evidence-index.csv", ",0,12 of 12 pass", ",1,12 of 12 pass"),
                "points exactly once",
            ),
            (
                "duplicate-module02-points",
                lambda root: replace(root / "checkpoint-score.csv", "oclc-app5-02,SUBTOTAL,Module 02 subtotal,20,20", "oclc-app5-02,SUBTOTAL,Module 02 subtotal,20,40"),
                "contribute 20 points once",
            ),
            (
                "duplicate-module03-points",
                lambda root: replace(root / "checkpoint-score.csv", "oclc-app5-03,SUBTOTAL,Module 03 subtotal,20,20", "oclc-app5-03,SUBTOTAL,Module 03 subtotal,20,40"),
                "contribute 20 points once",
            ),
            (
                "wrong-total",
                lambda root: replace(root / "checkpoint-score.csv", "checkpoint,TOTAL,Week 3 checkpoint total,40,40", "checkpoint,TOTAL,Week 3 checkpoint total,40,39"),
                "contribute 20 points once",
            ),
            (
                "failed-inherited-gate",
                lambda root: replace(root / "evidence-index.csv", "12 of 12 pass", "11 of 12 pass"),
                "inherited passing gates",
            ),
            (
                "failed-checkpoint-gate",
                lambda root: replace(root / "checkpoint-gates.csv", ",pass,", ",fail,"),
                "22 checkpoint integrity gates pass",
            ),
            (
                "public-synthetic-merge",
                lambda root: replace(root / "measures-disparities-readiness-review.md", "is never combined with the synthetic event numerator", "is combined with the synthetic event numerator"),
                "evidence, missingness, and suppression limits",
            ),
            (
                "denominator-mutation",
                lambda root: replace(root / "measures-disparities-readiness-review.md", "5,679,768", "5,679,769"),
                "evidence, missingness, and suppression limits",
            ),
            (
                "reference-mutation",
                lambda root: replace(root / "measures-disparities-readiness-review.md", "32 reference comparisons", "31 reference comparisons"),
                "every accepted result",
            ),
            (
                "missing-interval",
                lambda root: replace(root / "measures-disparities-readiness-review.md", "support, intervals, and both", "support and both"),
                "evidence, missingness, and suppression limits",
            ),
            (
                "hidden-missingness",
                lambda root: replace(root / "measures-disparities-readiness-review.md", "Zero conditioned geography missingness does not prove perfect geographic capture", "Geography capture is complete"),
                "evidence, missingness, and suppression limits",
            ),
            (
                "intersectional-claim",
                lambda root: replace(root / "responsible-claims-audit.md", "Intersectional claim: `prohibited because the three dimensions are separate margins rather than joint person records`", "Intersectional claim: `supported`"),
                "claims audit preserves",
            ),
            (
                "suppressed-zero",
                lambda root: replace(root / "responsible-claims-audit.md", "blank protected values are unavailable rather than zero", "blank protected values are zero"),
                "claims audit preserves",
            ),
            (
                "reconstructable-total",
                lambda root: replace(root / "measures-disparities-readiness-review.md", "Tract totals are not published", "Tract totals are published"),
                "evidence, missingness, and suppression limits",
            ),
            (
                "real-disparity",
                lambda root: replace(root / "progression-decision.md", "- Real disparity claim: `prohibited`", "- Real disparity claim: `supported`"),
                "authority prohibitions",
            ),
            (
                "mapping-ranking",
                lambda root: replace(root / "responsible-claims-audit.md", "- Mapping in this checkpoint: `prohibited`", "- Mapping in this checkpoint: `permitted`"),
                "claims audit preserves",
            ),
            (
                "targeting-allocation",
                lambda root: replace(root / "responsible-claims-audit.md", "- Allocation or funding: `prohibited`", "- Allocation or funding: `permitted`"),
                "claims audit preserves",
            ),
            (
                "incomplete-defense",
                lambda root: replace(root / "checkpoint-defense.md", "Answer: APP-5 Modules", "Response: APP-5 Modules"),
                "answers every question",
            ),
            (
                "missing-reviewer",
                lambda root: replace(root / "reviewer-record.md", "- Construction review date: `2026-08-31`", "- Construction review date: ``"),
                "separates construction completion",
            ),
            (
                "missing-condition",
                lambda root: replace(root / "conditions-register.csv", "C12,Complete clean independent reproduction of all three modules and the checkpoint,independent reproducer,course director,open,alpha\n", ""),
                "12 ordered conditions",
            ),
            (
                "missing-ai-field",
                lambda root: replace(root / "ai-use.md", "- Human owner: `Shuhan He and the named APP-5 faculty owner`", "- Human owner: ``"),
                "every accountable field",
            ),
            (
                "invalid-progression",
                lambda root: replace(root / "progression-decision.md", "- Module 04 permission: `permitted for curriculum construction`", "- Module 04 permission: `not permitted`"),
                "permission matches progression",
            ),
            (
                "implementation",
                lambda root: replace(root / "progression-decision.md", "- Implementation: `prohibited`", "- Implementation: `permitted`"),
                "authority prohibitions",
            ),
            (
                "deployment",
                lambda root: replace(root / "progression-decision.md", "- Deployment: `prohibited`", "- Deployment: `permitted`"),
                "authority prohibitions",
            ),
            (
                "missing-reproduction-route",
                lambda root: replace(root / "reproducibility-check.md", "- Changed candidate: `rejected`.\n", ""),
                "mutation routes",
            ),
        )
        for name, mutation, message in routes:
            expect_rejection(reference, base, name, mutation, message)

        try:
            validate(learner)
        except ValidationError as error:
            assert "Reference records contain no placeholders" in str(error)
        else:
            raise AssertionError("Validator accepted learner prompts as complete")

    print(
        f"APP-5 Checkpoint 01 validator self-check passed: {complete['checks_passed']} reference checks "
        f"and {starter['checks_passed']} learner checks; copied validation and {len(routes)} failure routes verified."
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

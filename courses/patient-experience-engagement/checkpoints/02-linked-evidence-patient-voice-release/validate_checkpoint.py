"""Validate the APP-2 cumulative Week 6 checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path


CHECKPOINT_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes",
    "VERSION",
    "checkpoint-contract.json",
    "assessment.md",
    "instructor-notes.md",
    "build_checkpoint.py",
    "validate_checkpoint.py",
)
WORK_FILES = (
    "README.md",
    "evidence-index.csv",
    "linked-evidence-patient-voice-review.md",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-decision.md",
)
MODULES = {
    "module-04": {
        "id": "oclc-app2-04",
        "version": "0.1.0",
        "files": 65,
        "manifest_rows": 52,
        "manifest_bytes": 6529,
        "manifest_sha256": "bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8",
    },
    "module-05": {
        "id": "oclc-app2-05",
        "version": "0.1.0",
        "files": 49,
        "manifest_rows": 33,
        "manifest_bytes": 4598,
        "manifest_sha256": "6f3d93a1a08458cb39fa8d321a67f10dad1ee45b2a8a2742a969ab969f35c8fa",
    },
    "module-06": {
        "id": "oclc-app2-06",
        "version": "0.1.0",
        "files": 46,
        "manifest_rows": 28,
        "manifest_bytes": 4361,
        "manifest_sha256": "0cb7f2d0ffc6d5ae8cbcd0cf206a61f143dcd603b5b34eb312972d2ecc2f0938",
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
    require(
        all((root / name).is_file() for name in required),
        "All checkpoint controls and records are present",
    )
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    header, manifest = read_csv(root / "candidate-manifest.csv")
    require(
        header == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"],
        "Candidate manifest header matches",
    )
    require(
        len(manifest) == 160
        and [row["relative_path"] for row in manifest]
        == sorted(row["relative_path"] for row in manifest),
        "Candidate manifest has 160 sorted rows",
    )
    expected = required | {row["relative_path"] for row in manifest}
    require(actual == expected and len(actual) == 174, "Checkpoint has exactly 174 expected files")

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
        contract["checkpoint_id"] == "oclc-app2-cp02"
        and contract["commons_release"] == "0.62.0"
        and contract["course_points"] == 45,
        "Checkpoint identity and points match",
    )
    require(
        contract["accepted_week3"]["checkpoint_id"] == "oclc-app2-cp01"
        and contract["accepted_week3"]["candidate_manifest_sha256"]
        == "5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903",
        "Accepted Week 3 identity matches",
    )
    require(
        contract["accepted_component_files"] == 160 and len(contract["accepted_modules"]) == 3,
        "Contract accepts 160 files from three modules",
    )
    require(
        contract["score_map"] == {"oclc-app2-04": 25, "oclc-app2-05": 20, "oclc-app2-06": 0}
        and sum(contract["score_map"].values()) == 45,
        "Contract assigns 45 points exactly once",
    )
    require(
        contract["required_gates"]
        == {
            "module04_linkage": 20,
            "module05_patient_voice_equity": 22,
            "module06_partnership_improvement_ml": 24,
            "checkpoint_integrity": 20,
        },
        "Contract preserves all gate totals",
    )

    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [
            path
            for path in module_root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        ]
        require(len(files) == details["files"], f"{directory} file count matches")
        require(
            (module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"],
            f"{directory} version matches",
        )
        nested = module_root / "release-manifest.csv"
        require(nested.stat().st_size == details["manifest_bytes"], f"{directory} manifest bytes match")
        require(sha256(nested) == details["manifest_sha256"], f"{directory} manifest SHA-256 matches")
        nested_header, nested_rows = read_csv(nested)
        require(
            nested_header == ["relative_path", "bytes", "sha256", "role"]
            and len(nested_rows) == details["manifest_rows"],
            f"{directory} nested manifest shape matches",
        )
        for row in nested_rows:
            path = module_root / row["relative_path"]
            require(
                path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"],
                f"{directory} nested artifact matches: {row['relative_path']}",
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
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 174}
        print(f"APP-2 Checkpoint 2 learner validation passed: {len(checks)} checks.")
        return report

    index_header, index_rows = read_csv(root / "evidence-index.csv")
    require(
        index_header
        == [
            "evidence_id",
            "source_id",
            "source_version",
            "commons_release",
            "candidate_directory",
            "assembled_files",
            "workspace_manifest_sha256",
            "course_points",
            "score_treatment",
            "gate_treatment",
            "progression",
        ]
        and len(index_rows) == 4,
        "Evidence index has four ordered identities",
    )
    require(
        [row["source_id"] for row in index_rows]
        == ["oclc-app2-cp01", "oclc-app2-04", "oclc-app2-05", "oclc-app2-06"],
        "Evidence index order matches",
    )
    require(
        [row["course_points"] for row in index_rows] == ["0", "25", "20", "0"]
        and sum(Decimal(row["course_points"]) for row in index_rows) == Decimal("45"),
        "Evidence index assigns 45 points exactly once",
    )
    require(
        [row["workspace_manifest_sha256"] for row in index_rows]
        == [
            "5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903",
            MODULES["module-04"]["manifest_sha256"],
            MODULES["module-05"]["manifest_sha256"],
            MODULES["module-06"]["manifest_sha256"],
        ],
        "Evidence index preserves every accepted identity",
    )

    module04 = root / "candidate/module-04"
    linkage = read_csv(module04 / "outputs/linkage-reconciliation.csv")[1]
    require(
        [(row["full_source_rows"], row["full_rows_linked_to_h256"], row["difference"]) for row in linkage[:4]]
        == [("1912", "1912", "0"), ("4351", "4351", "0"), ("22150", "22150", "0"), ("145818", "145818", "0")],
        "Module 04 full event linkage remains exact",
    )
    access = {row["measure"]: row for row in read_csv(module04 / "outputs/access-communication-estimates.csv")[1]}
    require(
        access["usual_source"]["weighted_percent"] == "80.78856833"
        and access["after_hours_difficult"]["weighted_percent"] == "52.44065366"
        and access["delayed_for_cost"]["weighted_percent"] == "7.61893012",
        "Module 04 access and communication evidence remains exact",
    )
    require(
        access["provider_language_match"]["eligible_persons"] == "45"
        and access["provider_language_match"]["support_flag"] == "limited_support",
        "Module 04 provider-language limit remains exact",
    )
    digital = {row["evidence_id"]: row for row in read_csv(module04 / "outputs/digital-engagement.csv")[1]}
    require(
        digital["DE03"]["weighted_percent"] == "7.37866394"
        and digital["DE07"]["denominator_n"] == "0"
        and "not available" in digital["DE07"]["interpretation"],
        "Module 04 digital-channel and unavailable portal evidence remains exact",
    )

    module05 = root / "candidate/module-05"
    profile05 = {row["metric"]: row["value"] for row in read_csv(module05 / "outputs/source-profile.csv")[1]}
    require(
        profile05["synthetic_comments_received"] == "420"
        and profile05["double_coded_comments"] == "120"
        and profile05["themes"] == "8",
        "Module 05 synthetic corpus identity remains exact",
    )
    agreement = read_csv(module05 / "outputs/agreement-summary.csv")[1][0]
    require(
        (agreement["records"], agreement["agreements"], agreement["percent_agreement"], agreement["cohens_kappa"])
        == ("120", "96", "80.00000000", "0.77142857"),
        "Module 05 agreement evidence remains exact",
    )
    assisted = read_csv(module05 / "outputs/assisted-classification-audit.csv")[1][0]
    require(
        assisted["accuracy"] == "0.78333333" and "human review is required" in assisted["human_review_rule"],
        "Module 05 assisted-classification boundary remains exact",
    )
    estimates = read_csv(module05 / "outputs/group-estimates.csv")[1]
    contrasts = read_csv(module05 / "outputs/group-contrasts.csv")[1]
    require(
        len(estimates) == 52
        and sum(row["support_status"] == "supported" for row in estimates) == 35
        and len(contrasts) == 36
        and sum(row["support_status"] == "supported" for row in contrasts) == 19,
        "Module 05 support and suppression counts remain exact",
    )
    contrast_map = {(row["dimension"], row["group"], row["measure"]): row for row in contrasts}
    require(
        contrast_map[("income_group", "lower income", "delayed_for_cost")]["difference_pp"] == "4.02137981"
        and contrast_map[("income_group", "lower income", "any_telehealth_event")]["difference_pp"] == "-6.88053616",
        "Module 05 retained equity questions remain exact",
    )

    module06 = root / "candidate/module-06"
    performance = {row["method"]: row for row in read_csv(module06 / "outputs/model-performance.csv")[1]}
    require(
        (performance["transparent_benchmark"]["base_weighted_brier"], performance["transparent_benchmark"]["base_weighted_auc"], performance["transparent_benchmark"]["weighted_teaching_error_cost"])
        == ("0.22962545", "0.54335192", "227"),
        "Module 06 transparent-model evidence remains exact",
    )
    require(
        (performance["bounded_random_forest"]["base_weighted_brier"], performance["bounded_random_forest"]["base_weighted_auc"], performance["bounded_random_forest"]["weighted_teaching_error_cost"])
        == ("0.23135127", "0.53869891", "225"),
        "Module 06 bounded-model evidence remains exact",
    )
    recovery = {(row["measure"], row["estimator"]): row for row in read_csv(module06 / "outputs/estimate-recovery.csv")[1]}
    require(
        recovery[("teaching_composite", "transparent_adjusted")]["absolute_bias_pp"] == "2.48289986"
        and recovery[("teaching_composite", "bounded_ml_adjusted")]["absolute_bias_pp"] == "2.39922466",
        "Module 06 known-truth recovery remains exact",
    )
    weights = {row["method"]: row for row in read_csv(module06 / "outputs/response-weight-diagnostics.csv")[1]}
    require(
        weights["transparent_benchmark"]["stability_status"] == "pass"
        and weights["bounded_random_forest"]["stability_status"] == "pass",
        "Module 06 weight-stability decisions remain passing",
    )
    require(
        all(row["status"] == "pass" for row in read_csv(module06 / "outputs/analysis-checks.csv")[1])
        and all(row["status"] == "pass" for row in read_csv(module06 / "gate-results.csv")[1]),
        "Module 06 analysis and partnership gates remain passing",
    )

    review = (root / "linked-evidence-patient-voice-review.md").read_text(encoding="utf-8").lower()
    exact_review_values = (
        "1,255 people and 28,455 linked events",
        "80.78856833",
        "52.44065366",
        "7.61893012",
        "7.37866394",
        "420 comments",
        "80.00000000",
        "0.77142857",
        "0.78333333",
        "35 estimates and 19 contrasts",
        "4.02137981",
        "-6.88053616",
        "0.22962545",
        "0.23135127",
        "2.48289986",
        "2.39922466",
        "0.08367520",
        "45.00 of 45.00",
    )
    require(all(value in review for value in exact_review_values), "Integrated review contains every exact decision value")
    boundaries = (
        "not patient testimony",
        "do not prove inequity",
        "does not count as engagement",
        "transparent benchmark remains",
        "clinical action: `prohibited`",
        "model deployment: `prohibited`",
    )
    require(all(value in review for value in boundaries), "Integrated review preserves material claim and use boundaries")

    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require(
        all(
            value in reproducibility
            for value in (
                "160 across modules 04 through 06",
                "174",
                "match byte for byte",
                "copied-validator result: `pass`",
                "candidate mutation result: `rejected`",
                "duplicate-score result: `rejected`",
                "failed-gate result: `rejected`",
                "invalid-progression result: `rejected`",
            )
        ),
        "Reproduction record is complete",
    )
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
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

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Week 6 score") == "45.00 of 45.00", "Checkpoint score is exact")
    require(
        markdown_field(progression, "Module 04 gates") == "20 of 20 pass"
        and markdown_field(progression, "Module 05 gates") == "22 of 22 pass"
        and markdown_field(progression, "Module 06 gates") == "24 of 24 pass for curriculum construction",
        "All module gates pass",
    )
    require(
        markdown_field(progression, "Checkpoint integrity gates") == "20 of 20 pass",
        "All checkpoint gates pass",
    )
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 07 permission")
    require(
        disposition in ALLOWED_PROGRESSION
        and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction")),
        "Module 07 permission matches progression",
    )
    require(
        markdown_field(progression, "ML changes response-adjustment decision") == "no"
        and markdown_field(progression, "Teaching adjustment") == "retain transparent benchmark",
        "Model decision and teaching adjustment agree",
    )
    prohibited_labels = (
        "Comment-text machine learning",
        "Patient targeting and group ranking",
        "Official HCAHPS reporting and fielding",
        "Clinical action",
        "Implementation",
        "Model deployment",
    )
    require(
        all(markdown_field(progression, label) == "prohibited" for label in prohibited_labels),
        "All prohibited uses remain prohibited",
    )
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) == 12, "Progression has 12 owned conditions")

    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 174}
    print(f"APP-2 Checkpoint 2 reference validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app2-cp02-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner = base / "reference", base / "learner"
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

        broken = base / "broken-candidate"
        shutil.copytree(reference, broken)
        path = broken / "candidate/module-06/outputs/model-performance.csv"
        path.write_text(
            path.read_text(encoding="utf-8").replace("0.22962545", "0.32962545", 1),
            encoding="utf-8",
            newline="\n",
        )
        try:
            validate(broken)
        except ValidationError as error:
            assert "Candidate SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a candidate mutation")

        duplicate_score = base / "duplicate-score"
        shutil.copytree(reference, duplicate_score)
        path = duplicate_score / "evidence-index.csv"
        path.write_text(
            path.read_text(encoding="utf-8").replace(",0,gate only; no added points", ",1,gate only; no added points", 1),
            encoding="utf-8",
            newline="\n",
        )
        try:
            validate(duplicate_score)
        except ValidationError as error:
            assert "Evidence index assigns 45 points exactly once" in str(error)
        else:
            raise AssertionError("Validator accepted duplicate points")

        failed_gate = base / "failed-gate"
        shutil.copytree(reference, failed_gate)
        path = failed_gate / "progression-decision.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("20 of 20 pass`", "19 of 20 pass`", 1),
            encoding="utf-8",
            newline="\n",
        )
        try:
            validate(failed_gate)
        except ValidationError as error:
            assert "All module gates pass" in str(error)
        else:
            raise AssertionError("Validator accepted a failed gate")

        invalid_progression = base / "invalid-progression"
        shutil.copytree(reference, invalid_progression)
        path = invalid_progression / "progression-decision.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("continue with conditions", "deploy", 1),
            encoding="utf-8",
            newline="\n",
        )
        try:
            validate(invalid_progression)
        except ValidationError as error:
            assert "Module 07 permission matches progression" in str(error)
        else:
            raise AssertionError("Validator accepted an invalid progression")

    print(
        f"APP-2 Checkpoint 2 validator self-check passed: {complete['checks_passed']} reference checks "
        f"and {starter['checks_passed']} learner checks; copied and mutation routes verified."
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

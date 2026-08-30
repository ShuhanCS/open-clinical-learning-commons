"""Validate the APP-1 cumulative Week 6 checkpoint."""

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
IMMUTABLE_FILES = (".gitattributes", "VERSION", "checkpoint-contract.json", "assessment.md", "build_checkpoint.py", "validate_checkpoint.py")
WORK_FILES = ("README.md", "evidence-index.csv", "adjusted-variation-improvement-review.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md")
MODULES = {
    "module-04": {"id": "oclc-app1-04", "version": "0.1.0", "files": 32, "manifest_rows": 10, "manifest_bytes": 1666, "manifest_sha256": "5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb"},
    "module-05": {"id": "oclc-app1-05", "version": "0.1.0", "files": 30, "manifest_rows": 9, "manifest_bytes": 1526, "manifest_sha256": "7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e"},
    "module-06": {"id": "oclc-app1-06", "version": "0.1.0", "files": 38, "manifest_rows": 11, "manifest_bytes": 1833, "manifest_sha256": "b7127dbfac9e7a9549ea682499a1ca5d368a4acbbc20da2e307324be5813b978"},
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
    require(all((root / name).is_file() for name in required), "All checkpoint controls and records are present")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    header, manifest = read_csv(root / "candidate-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"], "Candidate manifest header matches")
    require(len(manifest) == 100 and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Candidate manifest has 100 sorted rows")
    expected = required | {row["relative_path"] for row in manifest}
    require(actual == expected and len(actual) == 113, "Checkpoint has exactly 113 expected files")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(row["source_module"] == MODULES[directory]["id"] and row["source_version"] == MODULES[directory]["version"], f"Candidate source identity matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(contract["checkpoint_id"] == "oclc-app1-cp02" and contract["commons_release"] == "0.54.0" and contract["course_points"] == 45, "Checkpoint identity and points match")
    require(contract["accepted_week3"]["checkpoint_id"] == "oclc-app1-cp01" and contract["accepted_week3"]["candidate_manifest_sha256"] == "ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860", "Accepted Week 3 identity matches")
    require(contract["accepted_component_files"] == 100 and len(contract["accepted_modules"]) == 3, "Contract accepts 100 files from three modules")
    require(contract["score_map"] == {"oclc-app1-04": 25, "oclc-app1-05": 20, "oclc-app1-06": 0} and sum(contract["score_map"].values()) == 45, "Contract assigns 45 points exactly once")
    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [path for path in module_root.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
        require(len(files) == details["files"], f"{directory} file count matches")
        require((module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"], f"{directory} version matches")
        nested = module_root / "workspace-manifest.csv"
        require(nested.stat().st_size == details["manifest_bytes"], f"{directory} manifest bytes match")
        require(sha256(nested) == details["manifest_sha256"], f"{directory} manifest SHA-256 matches")
        nested_header, nested_rows = read_csv(nested)
        require(nested_header == ["relative_path", "bytes", "sha256", "role"] and len(nested_rows) == details["manifest_rows"], f"{directory} nested manifest shape matches")
        for row in nested_rows:
            path = module_root / row["relative_path"]
            require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"{directory} nested artifact matches: {row['relative_path']}")

    text_files = [name for name in WORK_FILES if Path(name).suffix.lower() in {".md", ".csv"}]
    for name in text_files:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 113}
        print(f"APP-1 Checkpoint 2 learner validation passed: {len(checks)} checks.")
        return report

    index_header, index_rows = read_csv(root / "evidence-index.csv")
    require(index_header == ["evidence_id", "source_id", "source_version", "commons_release", "candidate_directory", "assembled_files", "workspace_manifest_sha256", "course_points", "score_treatment", "gate_treatment", "progression"] and len(index_rows) == 4, "Evidence index has four ordered identities")
    require([row["source_id"] for row in index_rows] == ["oclc-app1-cp01", "oclc-app1-04", "oclc-app1-05", "oclc-app1-06"], "Evidence index order matches")
    require(sum(Decimal(row["course_points"]) for row in index_rows) == Decimal("45"), "Evidence index assigns 45 points exactly once")
    require([row["course_points"] for row in index_rows] == ["0", "25", "20", "0"], "Only Modules 04 and 05 receive points")

    module04 = root / "candidate/module-04"
    adjusted = read_csv(module04 / "outputs/adjusted-association.csv")[1][0]
    require((adjusted["adjusted_odds_ratio"], adjusted["lower95"], adjusted["upper95"], adjusted["p_value"]) == ("1.16353250", "0.67665877", "2.00072462", "0.58392672"), "Module 04 adjusted association remains exact")
    performance04 = {row["metric"]: row["value"] for row in read_csv(module04 / "outputs/model-performance.csv")[1]}
    require(performance04["brier_score"] == "0.13490621" and performance04["roc_auc"] == "0.66585409", "Module 04 apparent performance remains exact")
    require(read_csv(module04 / "outputs/expected-outcomes.csv")[1].__len__() == 476, "Module 04 expected outcomes retain 476 people")

    module05 = root / "candidate/module-05"
    site05 = {row["measure_id"]: row for row in read_csv(module05 / "outputs/site-summary.csv")[1]}["M01"]
    require((site05["minimum_proportion"], site05["maximum_proportion"], site05["absolute_range"], site05["global_p_value"]) == ("0.22988506", "0.37804878", "0.14816372", "0.27993975"), "Module 05 site measurement evidence remains exact")
    require("not dispensing possession ingestion adherence" in {row["measure_id"]: row for row in read_csv(module05 / "outputs/measure-summary.csv")[1]}["M04"]["claim_limit"], "Module 05 medication record does not become adherence")

    module06 = root / "candidate/module-06"
    model06 = {row["model"]: row for row in read_csv(module06 / "outputs/model-performance.csv")[1]}
    require((model06["transparent"]["brier"], model06["transparent"]["roc_auc"], model06["transparent"]["fp"], model06["transparent"]["fn"], model06["transparent"]["weighted_error_cost"]) == ("0.09609243", "0.66363212", "17", "9", "44"), "Module 06 transparent evidence remains exact")
    require((model06["bounded_rf"]["brier"], model06["bounded_rf"]["roc_auc"], model06["bounded_rf"]["fp"], model06["bounded_rf"]["fn"], model06["bounded_rf"]["weighted_error_cost"]) == ("0.10745654", "0.62371615", "49", "6", "67"), "Module 06 bounded-ML evidence remains exact")
    equity06 = read_csv(module06 / "outputs/equity-summary.csv")[1]
    require(sum(row["followup_support"].startswith("suppress") for row in equity06) == 2 and sum(row["outcome_support"].startswith("suppress") for row in equity06) == 3, "Module 06 equity suppression remains exact")
    require(all(row["status"] == "pass" for row in read_csv(module06 / "outputs/analysis-checks.csv")[1]), "Module 06 analysis checks remain passing")

    review = (root / "adjusted-variation-improvement-review.md").read_text(encoding="utf-8").lower()
    review_values = ("0.67258471", "1.10542457", "0.00636020", "0.13490621", "1.16353250", "0.14816372", "0.27993975", "0.09609243", "0.10745654", "32 false positives", "45.00 of 45.00")
    require(all(value in review for value in review_values), "Review contains exact survival adjustment variation and ML evidence")
    require(all(value in review for value in ("does not prove equivalence", "measurement question", "never adherence", "question retained", "clinical implementation: `prohibited`", "model deployment: `prohibited`")), "Review preserves every material claim boundary")
    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require(all(value in reproducibility for value in ("100 across modules 04 through 06", "113", "match byte for byte", "candidate mutation result: `rejected`", "score mutation result: `rejected`", "copied-validator result: `pass`")), "Reproduction record is complete")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Week 6 score") == "45.00 of 45.00", "Checkpoint score is exact")
    require(markdown_field(progression, "Module 04 gates") == "18 of 18 pass" and markdown_field(progression, "Module 05 gates") == "18 of 18 pass" and markdown_field(progression, "Module 06 gates") == "24 of 24 pass", "All module gates pass")
    require(markdown_field(progression, "Checkpoint integrity gates") == "18 of 18 pass", "All checkpoint gates pass")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 07 permission")
    require(disposition in ALLOWED_PROGRESSION and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction")), "Module 07 permission matches progression")
    require(markdown_field(progression, "Clinical implementation") == "prohibited" and markdown_field(progression, "Model deployment") == "prohibited", "Implementation and deployment remain prohibited")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) >= 8, "Progression has at least eight owned conditions")
    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 113}
    print(f"APP-1 Checkpoint 2 reference validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app1-cp02-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner = base / "reference", base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_checkpoint.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_checkpoint.assemble(learner)
        starter = validate(learner, learner=True)

        broken = base / "broken-candidate"
        shutil.copytree(reference, broken)
        path = broken / "candidate/module-06/outputs/model-performance.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("0.09609243", "0.19609243", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Candidate SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a candidate mutation")

        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        path = bad_score / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("45.00 of 45.00", "46.00 of 45.00", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_score)
        except ValidationError as error:
            assert "Checkpoint score is exact" in str(error)
        else:
            raise AssertionError("Validator accepted an invalid score")

        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("continue with conditions", "deploy", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_progression)
        except ValidationError as error:
            assert "Module 07 permission matches progression" in str(error)
        else:
            raise AssertionError("Validator accepted an invalid progression")
    print(f"APP-1 Checkpoint 2 validator self-check passed: {complete['checks_passed']} reference checks and {starter['checks_passed']} learner checks; copied and mutation routes verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.checkpoint:
            parser.error("checkpoint is required unless --self-check is used")
        validate(args.checkpoint, learner=args.learner)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

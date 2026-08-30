"""Validate the APP-1 cumulative Week 3 checkpoint."""

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
WORK_FILES = ("README.md", "evidence-index.csv", "survival-readiness-review.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md")
MODULES = {
    "module-01": {"id": "oclc-app1-01", "version": "0.2.0", "files": 19, "manifest_name": "release-manifest.csv", "manifest_bytes": 1063, "manifest_sha256": "4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147"},
    "module-02": {"id": "oclc-app1-02", "version": "0.1.0", "files": 30, "manifest_name": "workspace-manifest.csv", "manifest_bytes": 1217, "manifest_sha256": "9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10"},
    "module-03": {"id": "oclc-app1-03", "version": "0.1.0", "files": 29, "manifest_name": "workspace-manifest.csv", "manifest_bytes": 1385, "manifest_sha256": "067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52"},
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
    require(len(manifest) == 78 and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Candidate manifest has 78 sorted rows")
    expected = required | {row["relative_path"] for row in manifest}
    require(actual == expected and len(actual) == 91, "Checkpoint has exactly 91 expected files")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(row["source_module"] == MODULES[directory]["id"] and row["source_version"] == MODULES[directory]["version"], f"Candidate source identity matches: {row['relative_path']}")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(contract["checkpoint_id"] == "oclc-app1-cp01" and contract["commons_release"] == "0.51.0" and contract["course_points"] == 20, "Checkpoint identity and points match")
    require(contract["accepted_component_files"] == 78 and len(contract["accepted_modules"]) == 3, "Contract accepts 78 files from three modules")
    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [path for path in module_root.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
        require(len(files) == details["files"], f"{directory} file count matches")
        require((module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"], f"{directory} version matches")
        nested = module_root / details["manifest_name"]
        require(nested.stat().st_size == details["manifest_bytes"], f"{directory} manifest bytes match")
        require(sha256(nested) == details["manifest_sha256"], f"{directory} manifest SHA-256 matches")
        nested_header, nested_rows = read_csv(nested)
        require(nested_header == ["relative_path", "bytes", "sha256", "role"], f"{directory} nested manifest header matches")
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
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 91}
        print(f"APP-1 Checkpoint 1 learner validation passed: {len(checks)} checks.")
        return report

    index_header, index_rows = read_csv(root / "evidence-index.csv")
    require(len(index_rows) == 3 and [row["module_id"] for row in index_rows] == ["oclc-app1-01", "oclc-app1-02", "oclc-app1-03"], "Evidence index has three ordered modules")
    require(sum(Decimal("20.00") if row["module_id"] == "oclc-app1-02" else Decimal("0") for row in index_rows) == Decimal("20.00"), "Evidence index assigns 20 points exactly once")
    review = (root / "survival-readiness-review.md").read_text(encoding="utf-8").lower()
    require(all(value in review for value in ("518", "476", "87", "389", "0.67258471", "1.10542457", "0.00636020")), "Review contains exact cohort and survival evidence")
    require("does not prove equivalence" in review and "does not prove independent censoring" in review and "main survival summary" in review, "Review contains quantity and censoring boundaries")
    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require("78" in reproducibility and "two builds match byte for byte" in reproducibility and "candidate mutation" in reproducibility, "Reproduction record is complete")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Checkpoint score") == "20.00 of 20.00", "Checkpoint score is exact")
    require(markdown_field(progression, "Module 03 survival gates") == "16 of 16 pass", "All survival gates pass")
    require(markdown_field(progression, "Checkpoint integrity gates") == "9 of 9 pass", "All checkpoint gates pass")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 04 permission")
    require(disposition in ALLOWED_PROGRESSION, "Progression value is allowed")
    require((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 04 permission matches progression")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) >= 8, "Progression has eight owned conditions")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")
    module02 = root / "candidate/module-02/outputs"
    require(len(read_csv(module02 / "analysis-cohort.csv")[1]) == 476 and len(read_csv(module02 / "event-audit.csv")[1]) == 1018, "Module 02 cohort and event audit counts match")
    module03 = root / "candidate/module-03/outputs"
    require(read_csv(module03 / "ph-check.csv")[1][0]["screen_result"] == "fail", "Module 03 PH failure remains visible")
    require(read_csv(module03 / "cox-model.csv")[1][0]["hazard_ratio"] == "1.10542457", "Module 03 Cox estimate remains exact")
    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 91}
    print(f"APP-1 Checkpoint 1 reference validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app1-cp01-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner = base / "reference", base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_checkpoint.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_checkpoint.assemble(learner)
        starter = validate(learner, learner=True)
        broken = base / "broken"
        shutil.copytree(reference, broken)
        path = broken / "candidate/module-03/outputs/ph-check.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("fail", "pass", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Candidate SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a candidate mutation")
        bad = base / "bad-score"
        shutil.copytree(reference, bad)
        path = bad / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("20.00 of 20.00", "21.00 of 20.00", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad)
        except ValidationError as error:
            assert "Checkpoint score is exact" in str(error)
        else:
            raise AssertionError("Validator accepted an invalid score")
    print(f"APP-1 Checkpoint 1 validator self-check passed: {complete['checks_passed']} reference checks and {starter['checks_passed']} learner checks; copied and mutation routes verified.")


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

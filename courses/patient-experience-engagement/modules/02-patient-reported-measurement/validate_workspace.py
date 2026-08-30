"""Validate an APP-2 Module 02 learner or reference workspace."""

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
from pathlib import Path


sys.dont_write_bytecode = True


PLACEHOLDER = re.compile(r"\b(REPLACE|TODO|TBD)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
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


def field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    import build_measurement
    import build_workspace

    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    immutable = build_workspace.immutable_files()
    expected = set(immutable) | set(build_workspace.RECORD_FILES) | {"release-manifest.csv"}
    require(root.is_dir(), "Workspace directory exists")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    require(actual == expected and len(actual) == 66, "Workspace has exactly 66 expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")
    contract = json.loads((root / "measurement-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app2-02", "version": "0.1.0", "commons_release": "0.57.0", "hours": 16.0, "week": 2}, "Module identity matches")
    require(contract["package"] == {"immutable_manifest_rows": 52, "editable_records": 13, "assembled_files": 66, "external_python_dependencies": 0}, "Package contract matches")
    require(contract["assessment"] == {"points": 20, "pass_points": 16, "noncompensable_gates": 18, "week3_checkpoint_component": True}, "Assessment contract matches")

    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
    require(len(manifest) == 52 and [row["relative_path"] for row in manifest] == sorted(immutable), "Manifest has 52 sorted immutable rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file() and path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Manifest hash matches: {row['relative_path']}")

    with tempfile.TemporaryDirectory(prefix="app2-module02-reproduce-") as temp_dir:
        reproduced = Path(temp_dir) / "reproduced"
        build_measurement.build(reproduced, source_root=root)
        require(build_measurement.generated_fingerprints(reproduced) == build_measurement.generated_fingerprints(root), "Committed measurement evidence reproduces exactly")

    _, sources = read_csv(root / "data/source-inventory.csv")
    require(len(sources) == 28 and sum(int(row["bytes"]) for row in sources) == 25032907, "Source inventory has 28 files and 25,032,907 bytes")
    require(sum(int(row["pages"]) for row in sources) == 1343, "Official PDF suite has 1,343 pages")
    _, modes = read_csv(root / "data/mode-language-inventory.csv")
    counts = {mode: sum(row["mode"] == mode for row in modes) for mode in ("mail", "phone", "web")}
    require(len(modes) == 22 and counts == {"mail": 9, "phone": 4, "web": 9}, "Mode-language inventory is 9 mail, 4 phone, and 9 web")
    _, crosswalk = read_csv(root / "data/version-crosswalk.csv")
    require([(row["legacy_question"], row["updated_question"]) for row in crosswalk] == [("none", "Q20"), ("Q15", "Q21"), ("Q16", "Q22"), ("Q17", "Q23")], "Version crosswalk is exact")
    _, items = read_csv(root / "data/item-map.csv")
    require([row["item_id"] for row in items] == ["Q20", "Q21", "Q22", "Q23", "H_COMP_6_Y_P"], "Item map preserves Q20 through Q23 and the composite")
    _, synthetic = read_csv(root / "data/synthetic/patient-measurement-responses.csv")
    require(len(synthetic) == 240 and all(row["data_class"] == "synthetic_procedural_teaching_only" for row in synthetic), "All 240 response records are visibly synthetic")
    require(sum(row["q22_help_after_discharge"] == "not_applicable" for row in synthetic) == 20, "Q21 skip logic preserves 20 not-applicable records")
    _, scores = read_csv(root / "outputs/synthetic-score-summary.csv")
    values = {row["metric_id"]: row["value"] for row in scores}
    require(values == {"S01": "56.81818182", "S02": "84.09090909", "S03": "78.26086957", "S04": "81.17588933", "S05": "80.00000000"}, "Synthetic scores reproduce")
    _, reliability = read_csv(root / "outputs/reliability-diagnostics.csv")
    reliability_values = {row["diagnostic_id"]: row["value"] for row in reliability}
    require(reliability_values["D01"] == "160" and reliability_values["D03"] == "0.6549707602" and reliability_values["D04"] == "0.6578064258", "Reliability diagnostics reproduce")
    _, concordance = read_csv(root / "outputs/published-concordance.csv")
    require(len(concordance) == 3610 and all(row["use_boundary"] == "source concordance only; no ranking" for row in concordance), "Published concordance has 3,610 non-ranking rows")
    _, invariants = read_csv(root / "outputs/invariant-checks.csv")
    require(len(invariants) == 18 and all(row["status"] == "pass" for row in invariants), "All 18 build invariants pass")

    for relative in build_workspace.RECORD_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")
    if starter:
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "points": 0, "failed_gates": 18}
        print(f"APP-2 Module 02 starter validation passed: {len(checks)} checks.")
        return report

    comparison_header, comparison = read_csv(root / "instrument-comparison.csv")
    require(comparison_header == ["candidate_id", "candidate", "measure_type", "construct_fit", "content_fit", "scoring_status", "language_mode_status", "rights_naming_status", "burden", "decision"] and len(comparison) >= 4, "Instrument comparison covers at least four candidates")
    require(any(row["candidate_id"] == "C01" and row["decision"] == "select with conditions" for row in comparison), "Q22/Q23 selection is explicit")
    _, reproduction = read_csv(root / "scoring-reproduction.csv")
    reproduction_values = {row["metric_id"]: row["value"] for row in reproduction}
    require(reproduction_values["M04"] == "81.17588933" and reproduction_values["M05"] == "80.00000000", "Learner scoring record preserves both formulas")
    access_header, access = read_csv(root / "language-mode-access.csv")
    require(access_header == ["audit_id", "mode", "language", "official_file", "local_route", "access_review", "status"] and len(access) == 22, "Learner access audit covers all 22 instrument files")

    _, score_rows = read_csv(root / "measurement-score.csv")
    require([row["criterion_id"] for row in score_rows] == [f"P{i:02d}" for i in range(1, 6)], "Score has five criteria")
    points = sum(int(row["points_awarded"]) for row in score_rows)
    require(all(0 <= int(row["points_awarded"]) <= int(row["points_possible"]) == 4 for row in score_rows), "Every criterion score is within range")
    require(points >= 16, "Score meets the 16-point threshold")
    _, gates = read_csv(root / "gate-results.csv")
    require([row["gate_id"] for row in gates] == [f"G{i:02d}" for i in range(1, 19)], "Gate record has G01 through G18")
    require(all(row["status"] == "pass" for row in gates), "All noncompensable gates pass")

    validity = (root / "construct-content-validity.md").read_text(encoding="utf-8")
    require(field(validity, "Measure type") == "PREM", "Measure type is PREM")
    reliability_text = (root / "reliability-interpretation.md").read_text(encoding="utf-8").lower()
    require("not evidence" in reliability_text and "hospital-level" in reliability_text, "Reliability claim remains bounded")
    meaning = (root / "meaningful-interpretation.md").read_text(encoding="utf-8")
    require(field(meaning, "Established meaningful-change threshold") == "none established in this module", "No meaningful-change threshold is invented")
    rights = (root / "rights-naming-decision.md").read_text(encoding="utf-8").lower()
    require("public-domain hcahps-derived items; local, unadjusted, unofficial" in rights and "prohibited" in rights, "Rights naming and comparison boundary is exact")
    decision = (root / "measurement-decision.md").read_text(encoding="utf-8")
    require(field(decision, "Clinical action") == "prohibited" and field(decision, "Hospital ranking") == "prohibited", "Clinical action and hospital ranking remain prohibited")
    require("synthetic" not in field(decision, "Selected instrument").lower(), "Synthetic data are not named as the instrument")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    for label in ("Tool and model", "Data classes shared", "Material claim", "Independent verification", "Human owner", "Accountability statement"):
        require(field(ai, label) is not None, f"AI-use field is present: {label}")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    progression_value = field(progression, "Progression")
    require(progression_value in ALLOWED_PROGRESSION, "Progression value is allowed")
    permission = field(progression, "Module 03 permission")
    require((progression_value in {"continue", "continue with conditions"}) == (permission == "permitted for response and representation study"), "Module 03 permission matches progression")
    require(field(progression, "Response weighting") == "reserved for Module 03", "Response weighting remains in Module 03")
    report = {"status": "pass", "mode": "complete", "checks_passed": len(checks), "points": points, "failed_gates": 0}
    print(f"APP-2 Module 02 complete validation passed: {len(checks)} checks and {points}/20 points.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app2-module02-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, starter = base / "reference", base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)
        copied = subprocess.run(
            [sys.executable, str(reference / "validate_workspace.py"), str(reference)],
            cwd=reference, capture_output=True, text=True,
        )
        assert copied.returncode == 0, copied.stderr
        assert not (reference / "__pycache__").exists()
        try:
            validate(starter)
        except ValidationError as error:
            assert "Record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted an incomplete starter")
        cases = []
        for name in ("changed-source", "invalid-score", "failed-gate", "invalid-naming", "invalid-progression", "synthetic-as-real", "missing-record"):
            workspace = base / name
            shutil.copytree(reference, workspace)
            cases.append((name, workspace))
        path = cases[0][1] / "data/raw/instruments/mail/english.pdf"
        with path.open("ab") as handle:
            handle.write(b"changed")
        path = cases[1][1] / "measurement-score.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",4,4,instrument", ",4,5,instrument", 1), encoding="utf-8", newline="\n")
        path = cases[2][1] / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="\n")
        path = cases[3][1] / "rights-naming-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("public-domain HCAHPS-derived items; local, unadjusted, unofficial", "official HCAHPS"), encoding="utf-8", newline="\n")
        path = cases[4][1] / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Progression: `continue with conditions`", "Progression: `deploy`"), encoding="utf-8", newline="\n")
        path = cases[5][1] / "measurement-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("updated HCAHPS Discharge Information pair", "synthetic patient response scale"), encoding="utf-8", newline="\n")
        (cases[6][1] / "measurement-decision.md").unlink()
        expected = {
            "changed-source": "Manifest bytes match", "invalid-score": "Every criterion score is within range",
            "failed-gate": "All noncompensable gates pass", "invalid-naming": "Rights naming and comparison boundary is exact",
            "invalid-progression": "Progression value is allowed", "synthetic-as-real": "Synthetic data are not named as the instrument",
            "missing-record": "Workspace has exactly 66 expected files",
        }
        for name, workspace in cases:
            try:
                validate(workspace)
            except ValidationError as error:
                assert expected[name] in str(error), (name, str(error))
            else:
                raise AssertionError(f"Validator accepted invalid workspace: {name}")
    print(f"APP-2 Module 02 validator self-check passed: {complete_report['checks_passed']} complete and {starter_report['checks_passed']} starter checks; copied validation and seven broken workspaces passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            validate(args.workspace.resolve(), starter=args.starter)
        else:
            parser.error("workspace is required unless --self-check is used")
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

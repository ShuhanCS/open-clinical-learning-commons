"""Validate an APP-3 Module 02 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
ACTION_CLAIM = re.compile(r"(?i)(recommend (?:adding|hiring|increasing) staff|(?<!no )bottleneck is|implement (?:this|now)|caused by staffing)")
URL = re.compile(r"https?://")
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
    import build_measures
    import build_workspace
    import freeze_upstream
    import generate_operational_release

    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    immutable = build_workspace.CONTROL_FILES + build_workspace.DATA_FILES + build_workspace.UPSTREAM_FILES
    if not starter:
        immutable += build_workspace.OUTPUT_FILES
    expected = set(immutable) | set(build_workspace.SQL_FILES) | set(build_workspace.RECORD_FILES) | {"release-manifest.csv"}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    expected_count = 49 if starter else 58
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_count, f"Workspace has exactly {expected_count} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "operational-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app3-02", "version": "0.1.0", "commons_release": "0.67.0", "hours": 16.0, "course_points": 20}, "Module identity and workload match")
    require(contract["source"] == {"release": "cgh-ed-01-operational-v1", "generator_version": "0.1.0", "seed": 73002, "tables": 9, "rows": 318732, "defects": 12}, "Source release contract matches")
    require(contract["measures"] == {"specifications": 17, "sql_files": 4, "outputs": 8, "query_checks": 30}, "Measure contract matches")

    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
    expected_manifest = 34 if starter else 43
    require(len(manifest) == expected_manifest and [row["relative_path"] for row in manifest] == sorted(immutable), f"Manifest has {expected_manifest} sorted rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"Manifest identity matches: {row['relative_path']}")

    source = generate_operational_release.verify(root)
    require(source == {"tables": 9, "total_rows": 318732, "manifest_rows": {"encounters": 43631, "process-events": 250821, "staffing": 4368, "queue-snapshots": 17520, "safety-events": 1274, "calendar-demand": 1092, "scenarios": 4, "known-truth": 10, "defect-register": 12}}, "Nine raw source tables reproduce")
    upstream = freeze_upstream.verify(root)
    require(upstream["files"] == 10, "Ten Module 01 handoff files reproduce")

    record_text = ""
    for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if relative in build_workspace.RECORD_FILES:
            record_text += "\n" + text
        if not starter:
            require(not PLACEHOLDER.search(text), f"Submission file is complete: {relative}")
    if starter:
        require(PLACEHOLDER.search(record_text) is not None, "Starter contains explicit learner placeholders")
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted outputs")
    else:
        require(URL.search(record_text) is None, "Learner records contain no public-to-synthetic source link")
        require(ACTION_CLAIM.search(record_text) is None, "Learner records contain no diagnosis or action claim")

    measure_header, measures = read_csv(root / "measure-specifications.csv")
    require(measure_header == ["measure_id", "name", "family", "type", "unit", "direction", "numerator_or_summary", "denominator_or_population", "exclusions", "event_clock", "attribution", "reporting_window", "refresh_cadence", "owner", "threshold_origin", "unavailable_state", "interpretation_limit"], "Measure specification header matches")
    require([row["measure_id"] for row in measures] == [f"M{index:02d}" for index in range(1, 18)], "Measure specification has 17 ordered rows")
    defect_header, defects = read_csv(root / "defect-repair-log.csv")
    require(defect_header == ["defect_id", "source_table", "defect", "clean_rule", "disposition", "measure_effect", "owner", "status"], "Defect repair header matches")
    require([row["defect_id"] for row in defects] == [f"D{index:03d}" for index in range(1, 13)], "Defect log has 12 ordered rows")
    score_header, score = read_csv(root / "measure-score.csv")
    require(score_header == ["criterion_id", "criterion", "points_available", "points_awarded", "evidence"], "Score header matches")
    require([row["criterion_id"] for row in score] == ["R01", "R02", "R03", "R04", "R05", "TOTAL"], "Score has five criteria and total")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "owner"], "Gate header matches")
    require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 16)], "Gate file has 15 ordered rows")

    if not starter:
        require(all(all(row[column].strip() for column in measure_header) for row in measures), "Every measure field is complete")
        require(all(row["status"] == "closed" for row in defects), "Every seeded defect has a closed clean-layer disposition")
        require(sum(int(row["points_awarded"]) for row in score[:5]) == 20 and score[-1]["points_awarded"] == "20", "Reference score is 20 of 20")
        require(all(row["status"] == "pass" for row in gates), "All 15 noncompensable gates pass")
        progression = (root / "progression-decision.md").read_text(encoding="utf-8")
        value = field(progression, "Progression")
        permission = field(progression, "Module 03 permission")
        require(value in ALLOWED_PROGRESSION, "Progression value is allowed")
        require((value in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 03 permission matches progression")
        for label in ("Operational diagnosis", "Bottleneck claim", "Staffing change", "Clinical action", "Causal claim", "Implementation"):
            require(field(progression, label) == "prohibited", f"{label} remains prohibited")
        require(len([line for line in progression.splitlines() if re.match(r"^\| O\d{2} \|", line)]) == 7, "Seven Module 03 conditions have owners")

        committed = build_measures.verify_committed(root)
        require(committed == {"outputs": 8, "accepted_encounters": 43628, "query_checks": 30}, "Committed measure outputs match")
        with tempfile.TemporaryDirectory(prefix="app3-module02-validate-") as temp_dir:
            regenerated = Path(temp_dir) / "outputs"
            report = build_measures.build(root, root / "sql", regenerated)
            require(report["findings"]["failed_query_checks"] == 0, "All 30 independent query checks pass")
            for relative in build_workspace.OUTPUT_FILES:
                name = Path(relative).name
                require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {
        "status": "pass", "mode": "starter" if starter else "complete",
        "checks_passed": len(checks), "assembled_files": expected_count,
        "manifest_rows": expected_manifest, "course_points": 0 if starter else 20,
    }
    print(f"APP-3 Module 02 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, starter: bool = False) -> None:
    try:
        validate(root, starter=starter)
    except (OSError, ValueError, KeyError, RuntimeError):
        return
    raise AssertionError("Validator accepted an invalid workspace")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app3-module02-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        cases = []
        for name in ("raw-mutation", "missing-table", "bad-sql", "public-link", "staffing-claim", "bad-score", "bad-progression", "missing-file"):
            target = base / name
            shutil.copytree(reference, target)
            cases.append((name, target))
        raw_path = cases[0][1] / "data/raw/encounters.csv.gz"
        raw_path.write_bytes(raw_path.read_bytes() + b"x")
        (cases[1][1] / "data/raw/staffing.csv.gz").unlink()
        sql_path = cases[2][1] / "sql/04-validation-and-defects.sql"
        sql_path.write_text(sql_path.read_text(encoding="utf-8").replace("clean adult encounters', (SELECT COUNT(*) FROM clean_encounters), 43628", "clean adult encounters', (SELECT COUNT(*) FROM clean_encounters), 43627", 1), encoding="utf-8")
        with (cases[3][1] / "operational-interpretation.md").open("a", encoding="utf-8") as handle:
            handle.write("\nhttps://data.cms.gov/ is the local service.\n")
        with (cases[4][1] / "operational-interpretation.md").open("a", encoding="utf-8") as handle:
            handle.write("\nWe recommend adding staff.\n")
        score_path = cases[5][1] / "measure-score.csv"
        score_path.write_text(score_path.read_text(encoding="utf-8").replace("R01,Measure definitions and denominators,4,4,", "R01,Measure definitions and denominators,4,3,"), encoding="utf-8")
        progression_path = cases[6][1] / "progression-decision.md"
        progression_path.write_text(progression_path.read_text(encoding="utf-8").replace("continue with conditions", "advance anyway", 1), encoding="utf-8")
        (cases[7][1] / "measure-specifications.csv").unlink()
        for _, target in cases:
            expect_failure(target)
        expect_failure(starter)
        assert complete_report["course_points"] == 20 and starter_report["course_points"] == 0
    print("APP-3 Module 02 validator self-check passed: reference, starter, and nine failure routes checked.")


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
            print(json.dumps(validate(args.workspace.resolve(), starter=args.starter), indent=2))
        else:
            parser.error("workspace is required")
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

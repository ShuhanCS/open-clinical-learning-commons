"""Validate APP-5 Module 02 learner and reference workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD)\b")
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
OBSERVED_CLAIM = re.compile(r"(?i)(synthetic (?:events?|rates?) (?:are|were) observed|observed diabetes cases|real excess cases)")
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}
SPEC_HEADER = [
    "measure_id", "name", "type", "numerator_or_summary", "denominator_or_standard",
    "age_groups", "multiplier", "interval_or_uncertainty", "availability_rule",
    "source_period", "geography", "interpretation_limit",
]


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


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    import build_measures
    import build_workspace
    import freeze_upstream
    import generate_synthetic_events

    root = root.resolve()
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
    expected_count = 61 if starter else 72
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_count, f"Workspace has exactly {expected_count} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "measure-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app5-02", "version": "0.1.0", "commons_release": "0.88.0", "hours": 16.0, "course_points": 20}, "Module identity and workload match")
    require(contract["upstream"]["handoff_manifest_sha256"] == "beda2254d019c0969c952773b31fb23db30e2be99798aa8af66d5cb1fbd87a2e", "Frozen handoff identity matches")
    require(contract["source"] == {"release": "fma-dp-01-measures-v1", "generator_version": "0.1.0", "seed": 73052, "period": "2024", "tracts": 1597, "age_bands": 5, "rows": 7985, "adult_denominator": 5679768, "synthetic_events": 283614, "zero_denominators": 41, "manifest_sha256": "9915aeb15f62d88a52cfa6304d211a4fd092d33c11e73cd5d63a14d64946823d"}, "Synthetic source contract matches")
    require(contract["measures"] == {"rate_multiplier": 100000, "sql_files": 4, "accepted_output_tables": 10, "query_checks": 30, "tract_union": 1620, "measure_tracts": 1597, "age_band_rows": 7985, "direct_rates_available": 1576, "direct_rates_unavailable": 21, "guided_indirect_required": 80, "public_modeled_rows": 1597}, "Measure release contract matches")
    require(contract["assessment"] == {"criteria": 5, "points": 20, "noncompensable_gates": 15}, "Assessment contract matches")
    require(all(value == "prohibited" for value in contract["authority"].values()), "All analytical and real-world authority remains prohibited")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Release manifest header matches")
    expected_manifest = 46 if starter else 57
    require(len(manifest) == expected_manifest and [row["relative_path"] for row in manifest] == sorted(immutable), f"Release manifest has {expected_manifest} sorted rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"Manifest identity matches: {row['relative_path']}")

    handoff = freeze_upstream.verify(root)
    require(handoff["upstream_files"] == 29 and handoff["reference_files"] == 27 and handoff["nested_manifest_rows"] == 16, "Complete Module 01 handoff reproduces")
    source = generate_synthetic_events.verify(root)
    require(source["event_rows"] == 7985 and source["adult_denominator"] == 5679768 and source["synthetic_events"] == 283614, "Synthetic source reproduces")

    record_text = ""
    for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        record_text += "\n" + text
        if not starter:
            require(not PLACEHOLDER.search(text), f"Submission file is complete: {relative}")

    spec_header, specifications = read_csv(root / "population-measure-specifications.csv")
    require(spec_header == SPEC_HEADER, "Measure specification header matches")
    require([row["measure_id"] for row in specifications] == [f"PM{index:02d}" for index in range(1, 10)], "Measure specification has nine ordered rows")
    score_header, score = read_csv(root / "measure-score.csv")
    require(score_header == ["criterion_id", "criterion", "points_available", "points_awarded", "evidence"], "Score header matches")
    require([row["criterion_id"] for row in score] == ["R01", "R02", "R03", "R04", "R05", "TOTAL"], "Score has five criteria and total")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "owner"], "Gate header matches")
    require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 16)], "Gate file has 15 ordered rows")

    if starter:
        require(PLACEHOLDER.search(record_text) is not None, "Starter contains explicit learner placeholders")
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted outputs")
        report = {"status": "pass", "mode": "starter", "checks": len(checks), "files": expected_count, "manifest_rows": expected_manifest, "course_points": 0}
        print(f"APP-5 Module 02 starter validation passed: {len(checks)} checks.")
        return report

    require(not OBSERVED_CLAIM.search(record_text), "Submission makes an unsupported observed-case claim")
    require(all(all(row[column].strip() for column in spec_header) for row in specifications), "Every measure specification field is complete")
    require(sum(int(row["points_awarded"]) for row in score[:5]) == 20 and score[-1]["points_awarded"] == "20", "Reference score is 20 of 20")
    require(all(row["status"] == "pass" and row["evidence"] and row["owner"] for row in gates), "All 15 noncompensable gates pass with evidence and owners")

    separation = (root / "public-synthetic-separation.md").read_text(encoding="utf-8")
    require("PLACES provides modeled small-area prevalence; the synthetic release provides generated planning-need events. They are never combined into one observed measure." in separation, "Public and synthetic evidence separation is explicit")
    require("PLACES and SVI values do not generate the numerator" in separation, "Synthetic generation inputs remain separate from public values")
    method = (root / "age-band-and-moe-method.md").read_text(encoding="utf-8")
    require("5,679,768" in method and "Forty-one tract-age rows" in method and "does not include covariance" in method, "Age-band and ACS margin method is complete")
    standardization = (root / "standardization-interpretation.md").read_text(encoding="utf-8")
    require("The weights total one" in standardization and "Direct rates are available for 1,576 tracts" in standardization and "Eighty tracts" in standardization, "Standardization interpretation is complete")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    progression_value = field(progression, "Progression")
    permission = field(progression, "Module 03 curriculum construction")
    require(progression_value in ALLOWED_PROGRESSION, "Progression value is allowed")
    require(progression_value == "continue with conditions" and permission == "permitted", "Reference progression permits bounded Module 03 construction")
    for label in ("Disparity claim", "Mapping", "Tract ranking", "Targeting or allocation", "Model fitting", "Intervention-effect estimation", "Real community action", "Implementation", "Deployment"):
        require(field(progression, label) == "prohibited", f"{label} remains prohibited")
    require(len([line for line in progression.splitlines() if re.match(r"^\| O\d{2} \|", line)]) == 8, "Eight Module 03 conditions have owners")
    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    require("Protected or identifiable data shared: `none`" in ai_use and "Agent authority: `none over" in ai_use, "AI-use boundary is complete")

    committed = build_measures.verify_committed(root)
    require(committed == {"outputs": 10, "measure_tracts": 1597, "age_band_rows": 7985, "adult_denominator": 5679768, "synthetic_events": 283614, "query_checks": 30}, "Committed measure outputs match")
    with tempfile.TemporaryDirectory(prefix="app5-module02-validate-") as temp_dir:
        regenerated = Path(temp_dir) / "outputs"
        report = build_measures.build(root, root / "sql", regenerated)
        require(report["findings"]["failed_query_checks"] == 0, "All 30 independent query checks pass")
        for relative in build_workspace.OUTPUT_FILES:
            name = Path(relative).name
            require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {"status": "pass", "mode": "complete", "checks": len(checks), "files": expected_count, "manifest_rows": expected_manifest, "course_points": 20}
    print(f"APP-5 Module 02 complete validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, starter: bool = False) -> None:
    try:
        validate(root, starter=starter)
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError):
        return
    raise AssertionError(f"Validator accepted an invalid workspace: {root}")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app5-module02-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        cases = []
        for name in ("upstream-mutation", "source-mutation", "missing-file", "placeholder", "changed-sql", "bad-score", "bad-progression", "blended-evidence", "observed-claim", "ranking-authority", "targeting-authority", "personal-path"):
            target = base / name
            shutil.copytree(reference, target)
            cases.append((name, target))
        upstream_path = cases[0][1] / "upstream/module01-reference/data/places-diabetes-ma-tract-2025.csv"
        upstream_path.write_bytes(upstream_path.read_bytes() + b"x")
        source_path = cases[1][1] / "data/raw/synthetic-events.csv.gz"
        source_path.write_bytes(source_path.read_bytes() + b"x")
        (cases[2][1] / "population-measure-specifications.csv").unlink()
        with (cases[3][1] / "standardization-interpretation.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        sql_path = cases[4][1] / "sql/04-indirect-standardization-and-validation.sql"
        sql_path.write_text(sql_path.read_text(encoding="utf-8").replace("'283614'", "'283613'", 1), encoding="utf-8")
        score_path = cases[5][1] / "measure-score.csv"
        score_path.write_text(score_path.read_text(encoding="utf-8").replace('R01,"Population, age-band, numerator, denominator, and linkage logic",4,4,', 'R01,"Population, age-band, numerator, denominator, and linkage logic",4,3,'), encoding="utf-8")
        progression_path = cases[6][1] / "progression-decision.md"
        progression_path.write_text(progression_path.read_text(encoding="utf-8").replace("continue with conditions", "advance anyway", 1), encoding="utf-8")
        separation_path = cases[7][1] / "public-synthetic-separation.md"
        separation_path.write_text(separation_path.read_text(encoding="utf-8").replace("They are never combined into one observed measure.", "They are combined into one observed measure."), encoding="utf-8")
        with (cases[8][1] / "public-synthetic-separation.md").open("a", encoding="utf-8") as handle:
            handle.write("\nThe synthetic events are observed diabetes cases.\n")
        ranking_path = cases[9][1] / "progression-decision.md"
        ranking_path.write_text(ranking_path.read_text(encoding="utf-8").replace("- Tract ranking: `prohibited`.", "- Tract ranking: `permitted`."), encoding="utf-8")
        targeting_path = cases[10][1] / "progression-decision.md"
        targeting_path.write_text(targeting_path.read_text(encoding="utf-8").replace("- Targeting or allocation: `prohibited`.", "- Targeting or allocation: `permitted`."), encoding="utf-8")
        with (cases[11][1] / "ai-use.md").open("a", encoding="utf-8") as handle:
            handle.write("\nC:\\Users\\Example\\private.csv\n")
        for _, target in cases:
            expect_failure(target)

        copied = base / "copied-starter"
        shutil.copytree(starter, copied)
        for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
            shutil.copy2(reference / relative, copied / relative)
        expect_failure(copied, starter=True)
        expect_failure(starter)
        assert complete_report["course_points"] == 20 and starter_report["course_points"] == 0
    print("APP-5 Module 02 validator self-check passed: reference, starter, copied-answer, complete-mode starter, and 12 protected failure routes rejected.")


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
            print(json.dumps(validate(args.workspace, starter=args.starter), indent=2))
        else:
            parser.error("workspace is required")
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()

"""Freeze and verify the accepted APP-3 Module 06 handoff."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODULE04 = ROOT.parent / "04-demand-forecasting-capacity"
MODULE05 = ROOT.parent / "05-improvement-scenarios-evaluation"
MODULE04_SOURCES = {
    "module04-version.txt": "VERSION",
    "module04-release.json": "release.json",
    "module04-forecast-contract.json": "forecast-contract.json",
    "shift-metrics.csv": "upstream/shift-metrics.csv",
    "folds.csv": "outputs/folds.csv",
    "transparent-predictions.csv": "outputs/forecast-predictions.csv",
    "error-summary.csv": "outputs/error-summary.csv",
    "error-slices.csv": "outputs/error-slices.csv",
    "week53-forecast.csv": "outputs/week53-forecast.csv",
    "forecast-findings.json": "outputs/forecast-findings.json",
    "module04-model-comparison.md": "reference/model-comparison.md",
    "module04-failure-period-review.md": "reference/failure-period-review.md",
    "module04-capacity-interpretation.md": "reference/capacity-interpretation.md",
    "module04-progression-decision.md": "reference/progression-decision.md",
}
MODULE05_SOURCES = {
    "module05-version.txt": "VERSION",
    "module05-release.json": "release.json",
    "module05-scenario-contract.json": "scenario-contract.json",
    "scenario-findings.json": "outputs/scenario-findings.json",
    "scenario-summary.csv": "outputs/scenario-summary.csv",
    "paired-effects.csv": "outputs/paired-effects.csv",
    "sensitivity-review.csv": "outputs/sensitivity-review.csv",
    "evaluation-measures.csv": "outputs/evaluation-measures.csv",
    "evaluation-threats.csv": "outputs/evaluation-threats.csv",
    "scenario-validation-checks.csv": "outputs/validation-checks.csv",
    "module06-handoff.md": "reference/module06-handoff.md",
    "module05-week6-score.csv": "reference/week6-score.csv",
    "module05-gate-results.csv": "reference/gate-results.csv",
    "module05-progression-decision.md": "reference/progression-decision.md",
    "module05-evaluation-design.md": "reference/evaluation-design.md",
    "module05-access-workforce-safety-review.md": "reference/access-workforce-safety-review.md",
    "module05-evaluation-threat-audit.csv": "reference/evaluation-threat-audit.csv",
    "module05-gaming-unintended-effects.md": "reference/gaming-unintended-effects.md",
    "module05-reproducibility-check.md": "reference/reproducibility-check.md",
}


class HandoffError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def freeze(output: Path) -> list[dict[str, object]]:
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {output}")
    output.mkdir(parents=True)
    rows: list[dict[str, object]] = []
    source_sets = (
        (MODULE04, MODULE04_SOURCES, "oclc-app3-04@0.1.0+commons.0.70.0", "accepted forecast evidence"),
        (MODULE05, MODULE05_SOURCES, "oclc-app3-05@0.1.0+commons.0.71.0", "accepted scenario and evaluation evidence"),
    )
    for source_root, sources, release, role in source_sets:
        for target_name, source_name in sources.items():
            source = source_root / source_name
            if not source.is_file():
                raise HandoffError(f"Missing handoff source: {source}")
            target = output / target_name
            shutil.copy2(source, target)
            rows.append({
                "relative_path": f"upstream/{target_name}",
                "source_path": source_name,
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
                "source_release": release,
                "role": role,
            })
    rows.sort(key=lambda row: str(row["relative_path"]))
    manifest = output / "module06-handoff-manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "source_path", "bytes", "sha256", "source_release", "role"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    if len(rows) != 33 or sum(path.is_file() for path in output.iterdir()) != 34:
        raise HandoffError("Module 06 handoff file contract changed")
    return rows


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root / "upstream"
    manifest = upstream / "module06-handoff-manifest.csv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["relative_path", "source_path", "bytes", "sha256", "source_release", "role"]
        if list(reader.fieldnames or []) != expected_header:
            raise HandoffError("Handoff manifest header mismatch")
        rows = list(reader)
    expected = sorted(f"upstream/{name}" for name in (*MODULE04_SOURCES, *MODULE05_SOURCES))
    if len(rows) != 33 or [row["relative_path"] for row in rows] != expected:
        raise HandoffError("Handoff manifest row contract mismatch")
    for row in rows:
        path = root / row["relative_path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise HandoffError(f"Handoff identity mismatch: {row['relative_path']}")

    release04 = json.loads((upstream / "module04-release.json").read_text(encoding="utf-8"))
    release05 = json.loads((upstream / "module05-release.json").read_text(encoding="utf-8"))
    contract04 = json.loads((upstream / "module04-forecast-contract.json").read_text(encoding="utf-8"))
    findings05 = json.loads((upstream / "scenario-findings.json").read_text(encoding="utf-8"))
    folds = read_csv(upstream / "folds.csv")
    predictions = [row for row in read_csv(upstream / "transparent-predictions.csv") if row["method"] == "seasonal_exponential_smoothing"]
    shifts = read_csv(upstream / "shift-metrics.csv")
    measures = read_csv(upstream / "evaluation-measures.csv")
    score = read_csv(upstream / "module05-week6-score.csv")
    gates = read_csv(upstream / "module05-gate-results.csv")
    handoff = (upstream / "module06-handoff.md").read_text(encoding="utf-8")
    if release04["module_id"] != "oclc-app3-04" or release04["commons_release"] != "0.70.0":
        raise HandoffError("Module 04 release identity mismatch")
    if release05["module_id"] != "oclc-app3-05" or release05["commons_release"] != "0.71.0":
        raise HandoffError("Module 05 release identity mismatch")
    if contract04["forecast"]["rolling_folds"] != 28 or contract04["forecast"]["evaluation_rows_per_method"] != 588:
        raise HandoffError("Forecast comparison contract mismatch")
    if len(folds) != 28 or len(predictions) != 588 or len(shifts) != 1092:
        raise HandoffError("Forecast row identity mismatch")
    if findings05["selection"]["selected_option"] != "none" or findings05["sensitivity"]["null_or_failed_rows"] != 6:
        raise HandoffError("Scenario decision mismatch")
    if len(measures) != 12 or score[-1]["points_awarded"] != "25" or len(gates) != 20 or any(row["status"] != "pass" for row in gates):
        raise HandoffError("Measure, score, or gate handoff mismatch")
    if "Option for feasibility review: `none`" not in handoff or "Implementation authority: `not authorized`" not in handoff:
        raise HandoffError("Module 05 authority handoff mismatch")
    return {
        "files": 33,
        "forecast_rows": 588,
        "shift_rows": 1092,
        "monitoring_measures": 12,
        "module05_points": 25,
        "selected_option": "none",
    }


def self_check() -> None:
    committed = verify(ROOT)
    with tempfile.TemporaryDirectory(prefix="app3-module06-upstream-") as temp_dir:
        base = Path(temp_dir)
        frozen = base / "upstream"
        freeze(frozen)
        if (frozen / "module06-handoff-manifest.csv").read_bytes() != (ROOT / "upstream/module06-handoff-manifest.csv").read_bytes():
            raise AssertionError("Regenerated handoff manifest differs")
        changed = base / "changed"
        shutil.copytree(ROOT / "upstream", changed / "upstream")
        path = changed / "upstream/module05-release.json"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8", newline="\n")
        try:
            verify(changed)
        except HandoffError:
            pass
        else:
            raise AssertionError("Verifier accepted a changed handoff")
    print(f"APP-3 Module 06 upstream self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            rows = freeze((args.output or (ROOT / "upstream")).resolve())
            print(json.dumps({"status": "pass", "files": len(rows)}, indent=2))
        else:
            print(json.dumps(verify(ROOT), indent=2))
    except (OSError, ValueError, KeyError, HandoffError) as error:
        parser.exit(1, f"Upstream handoff failed: {error}\n")


if __name__ == "__main__":
    main()

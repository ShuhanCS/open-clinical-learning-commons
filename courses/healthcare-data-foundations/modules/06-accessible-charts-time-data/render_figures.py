"""Render the FND-1 Module 06 accessible figure release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image


MODULE_ROOT = Path(__file__).resolve().parent
DEFAULT_MISSINGNESS = MODULE_ROOT / "data" / "missingness-profile.csv"
DEFAULT_RATES = MODULE_ROOT / "data" / "rates.csv"
DEFAULT_REGISTRY = MODULE_ROOT / "data" / "denominator-registry.csv"
DEFAULT_SOURCE = MODULE_ROOT / "data" / "resolved-analytic-table.csv"
INPUTS = {
    "missingness": (29, 4_362, "46e9c4dd268db223fac3cd0f01e65e050a3d44f6a28e0babcfb7bd5b552b5ba5"),
    "rates": (6, 1_893, "2398b283e449d6f876a3a3ea123e7905c637ba222f56c6aa03882cfc158942f3"),
    "registry": (27, 10_094, "e13bd0e1cf0716b912476fd81c7e4dd8bc827b2df468421aa2efc33f1f234be6"),
    "source": (374, 121_787, "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"),
}
BLUE = "#0072B2"
ORANGE = "#E69F00"
BLACK = "#000000"


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


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(content.rstrip() + "\n")


def style() -> None:
    matplotlib.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9, "axes.titlesize": 12,
        "axes.labelsize": 9, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 8, "axes.spines.top": False, "axes.spines.right": False,
        "axes.linewidth": 0.8, "grid.color": "#D9DEE7", "grid.linewidth": 0.6,
        "svg.hashsalt": "oclc-fnd1-06-v0.1.0",
    })


def save_figure(fig, target: Path, stem: str, title: str) -> None:
    fig.savefig(target / "figures" / f"{stem}.png", dpi=300, facecolor="white", metadata={"Software": "Open Clinical Learning Commons", "Title": title})
    svg = target / "figures" / f"{stem}.svg"
    fig.savefig(svg, facecolor="white", metadata={"Date": None, "Creator": "Open Clinical Learning Commons", "Title": title})
    svg.write_bytes(b"\n".join(line.rstrip() for line in svg.read_bytes().splitlines()) + b"\n")
    plt.close(fig)


def quality_table(missingness: list[dict[str, str]]) -> list[dict[str, object]]:
    conditions = {
        "death_date": "N01", "gender": "D11", "index_encounter_id": "D02",
        "index_reason_code": "N02", "index_reason_description": "N02",
        "next_30d_encounter_id": "N03|D13|D14", "next_30d_start": "N03|D13|D14",
        "next_30d_days_after_index_stop": "N03|D13|D14",
    }
    rows = []
    for row in missingness:
        if int(row["accepted_missing"]) == 0 and int(row["delta_missing"]) == 0:
            continue
        rows.append({
            "figure_id": "F01", "field_name": row["field_name"],
            "accepted_missing": row["accepted_missing"], "accepted_denominator": row["accepted_rows"],
            "accepted_missing_percent": row["accepted_missing_percent"],
            "defective_missing": row["defective_missing"], "defective_denominator": row["defective_rows"],
            "defective_missing_percent": row["defective_missing_percent"],
            "delta_missing": row["delta_missing"], "structurally_allowed": row["structurally_allowed"],
            "retained_conditions": conditions[row["field_name"]],
            "interpretation_limit": "Accepted optional missingness is not automatically error; defective values are deterministic teaching defects.",
        })
    if len(rows) != 8:
        raise ValueError("F01 table must contain eight registered fields.")
    return rows


def quarterly_table(source: list[dict[str, str]]) -> list[dict[str, object]]:
    counts: Counter[tuple[str, str]] = Counter()
    for row in source:
        start = datetime.fromisoformat(row["index_start"].replace("Z", "+00:00"))
        quarter = (start.month - 1) // 3 + 1
        label = f"{start.year} Q{quarter}"
        counts[(label, row["index_class"])] += 1
    rows = []
    for year in range(2015, 2020):
        for quarter in range(1, 5):
            label = f"{year} Q{quarter}"
            emergency = counts[(label, "emergency")]
            inpatient = counts[(label, "inpatient")]
            rows.append({
                "figure_id": "F03", "quarter_start": f"{year}-{1 + (quarter - 1) * 3:02d}-01",
                "quarter_label": label, "total_index_n": emergency + inpatient,
                "emergency_index_n": emergency, "inpatient_index_n": inpatient,
                "cohort_denominator": 374, "unit": "selected synthetic index encounters",
                "interpretation_limit": "One selected index per person; not hospital volume, a rate, a forecast, or evidence of demand change.",
            })
    if sum(int(row["total_index_n"]) for row in rows) != 374:
        raise ValueError("F03 quarterly counts do not conserve the cohort.")
    return rows


def render_quality(rows: list[dict[str, object]], target: Path) -> None:
    labels = [str(row["field_name"]).replace("_", " ") for row in rows][::-1]
    accepted = [float(row["accepted_missing_percent"]) for row in rows][::-1]
    defective = [float(row["defective_missing_percent"]) for row in rows][::-1]
    y = list(range(len(rows)))
    fig, ax = plt.subplots(figsize=(7, 4))
    height = 0.36
    ax.barh([value - height / 2 for value in y], accepted, height, color=BLUE, edgecolor=BLACK, linewidth=0.7, hatch="///", label="Accepted (n=374)")
    ax.barh([value + height / 2 for value in y], defective, height, color=ORANGE, edgecolor=BLACK, linewidth=0.7, hatch="xx", label="Defective layer (n=379)")
    for index, value in enumerate(accepted):
        ax.text(value + 1, index - height / 2, f"{value:.1f}%", va="center", fontsize=8)
    for index, value in enumerate(defective):
        ax.text(value + 1, index + height / 2, f"{value:.1f}%", va="center", fontsize=8)
    ax.set_yticks(y, labels)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Rows with blank value (%)")
    ax.set_title("Missingness needs field rules, not one blanket fix", loc="left", fontweight="bold")
    ax.grid(axis="x")
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)
    fig.text(0.99, 0.01, "Synthetic teaching layers; exact values in quality-missingness.csv", ha="right", fontsize=8)
    fig.subplots_adjust(left=0.32, right=0.98, top=0.87, bottom=0.29)
    save_figure(fig, target, "quality-missingness", "Missingness needs field rules, not one blanket fix")


def render_rates(rates: list[dict[str, str]], target: Path) -> None:
    labels = [row["measure"] for row in rates][::-1]
    points = [float(row["percent"]) for row in rates][::-1]
    lower = [float(row["wilson_95_lower_percent"]) for row in rates][::-1]
    upper = [float(row["wilson_95_upper_percent"]) for row in rates][::-1]
    y = list(range(len(rates)))
    fig, ax = plt.subplots(figsize=(7, 4))
    for index, (point, low, high) in enumerate(zip(points, lower, upper, strict=True)):
        ax.plot([low, high], [index, index], color=BLUE, linewidth=2)
        ax.plot(point, index, marker="o", markersize=6, color=BLUE, markeredgecolor=BLACK)
        source_row = rates[len(rates) - 1 - index]
        ax.text(high + 0.6, index, f"{source_row['numerator']}/{source_row['denominator']}", va="center", fontsize=8)
    ax.set_yticks(y, labels)
    ax.set_xlim(0, 38)
    ax.set_xlabel("Synthetic cohort (%) with Wilson 95% interval")
    ax.set_title("Recorded events vary by definition and time window", loc="left", fontweight="bold")
    ax.grid(axis="x")
    ax.set_axisbelow(True)
    fig.text(0.99, 0.01, "Exact values: descriptive-rates.csv; RT01 contains RT02-RT04; synthetic intervals only", ha="right", fontsize=8)
    fig.subplots_adjust(left=0.40, right=0.96, top=0.87, bottom=0.15)
    save_figure(fig, target, "descriptive-rates", "Recorded events vary by definition and time window")


def render_quarters(rows: list[dict[str, object]], target: Path) -> None:
    x = list(range(len(rows)))
    labels = [str(row["quarter_label"]) for row in rows]
    total = [int(row["total_index_n"]) for row in rows]
    emergency = [int(row["emergency_index_n"]) for row in rows]
    inpatient = [int(row["inpatient_index_n"]) for row in rows]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x, total, color=BLACK, linestyle="-", marker="o", linewidth=1.8, markersize=4, label="Total")
    ax.plot(x, emergency, color=BLUE, linestyle="--", marker="s", linewidth=1.5, markersize=4, label="Emergency")
    ax.plot(x, inpatient, color=ORANGE, linestyle=":", marker="^", linewidth=1.8, markersize=4, label="Inpatient")
    ax.set_xticks(x, labels, rotation=55, ha="right")
    ax.set_ylim(0, 42)
    ax.set_ylabel("Selected synthetic index encounters (n)")
    ax.set_xlabel("Index-start quarter")
    ax.set_title("Selected index encounters span 20 quarters", loc="left", fontweight="bold")
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.legend(frameon=False, ncol=3, loc="upper right")
    fig.text(0.99, 0.01, "Exact values: quarterly-index-counts.csv; one index/person; not volume or a tested trend", ha="right", fontsize=8)
    fig.subplots_adjust(left=0.11, right=0.98, top=0.87, bottom=0.25)
    save_figure(fig, target, "quarterly-index-counts", "Selected index encounters span 20 quarters")


def alt_text(target: Path) -> None:
    write_text(target / "alt-text/quality-missingness.md", """# F01 text alternative: quality and missingness

Purpose: compare accepted and deliberately defective missingness for eight registered fields.

Structure: grouped horizontal bars begin at zero. Blue diagonal-hatched bars represent 374 accepted rows; orange cross-hatched bars represent the 379-row teaching defect layer. The horizontal axis is percent blank from 0 to 100.

Main values: accepted missingness is highest for death date at 343 of 374, 91.711230 percent. Index reason code and description are each blank for 226 of 374, 60.427807 percent. The three next-encounter companion fields are each blank for 263 of 374, 70.320856 percent. Gender and index encounter ID have no accepted blanks but four and three seeded blanks in the defective layer.

Finding and limit: the defect layer adds missing values that require restoration, but high accepted missingness can be structurally correct. These are synthetic teaching layers, not a real data-quality estimate. Exact values are in tables/quality-missingness.csv.""")
    write_text(target / "alt-text/descriptive-rates.md", """# F02 text alternative: descriptive rates

Purpose: show six registered synthetic-cohort percentages and their Wilson 95-percent intervals.

Structure: a horizontal point-and-interval chart from 0 to 38 percent. Every row uses the same blue line and circle mark plus a direct numerator/denominator label, so meaning does not depend on color.

Main values: any recorded next encounter within 30 days is highest at 111 of 374, 29.679144 percent, interval 25.274719 to 34.496768. Scheduled care is 92 of 374. Any 90-day acute return is 36 of 374. The smallest value is urgent care within 30 days at 4 of 374, 1.069519 percent, interval 0.416679 to 2.717296. Synthetic death within 90 days is 8 of 374.

Finding and limit: definitions and windows differ. RT01 contains the three 30-day next-state categories RT02 through RT04, so rows are not all mutually exclusive. Intervals are descriptive arithmetic for synthetic data, not real-population estimates. Exact values are in tables/descriptive-rates.csv.""")
    write_text(target / "alt-text/quarterly-index-counts.md", """# F03 text alternative: quarterly selected indexes

Purpose: show how 374 selected synthetic index encounters are distributed across 20 quarters from 2015 Q1 through 2019 Q4.

Structure: three lines on a zero-based count axis. Total uses black solid circles, emergency blue dashed squares, and inpatient orange dotted triangles. Exact quarterly values are available in the companion CSV.

Main values: the highest total is 38 in 2015 Q1, comprising 28 emergency and 10 inpatient indexes. The lowest is 3 in 2019 Q3, all emergency. Totals across quarters sum to 374; emergency sums to 314 and inpatient to 60.

Finding and limit: selected index counts are generally lower in later quarters of this pinned cohort, but the figure has one selected index per person and no service-volume denominator or trend model. It is not evidence of hospital demand change, a forecast, or cause. Exact values are in tables/quarterly-index-counts.csv.""")


def validate_input(path: Path, key: str) -> list[dict[str, str]]:
    rows, size, digest = INPUTS[key]
    if path.stat().st_size != size or sha256(path) != digest:
        raise ValueError(f"{key} input fingerprint changed.")
    _, data = read_csv(path)
    if len(data) != rows:
        raise ValueError(f"{key} input row count changed.")
    return data


def render(missingness_path: Path, rates_path: Path, registry_path: Path, source_path: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    missingness = validate_input(missingness_path, "missingness")
    rates = validate_input(rates_path, "rates")
    registry = validate_input(registry_path, "registry")
    source = validate_input(source_path, "source")
    if {row["result_id"] for row in registry if row["result_id"].startswith("RT")} != {f"RT{n:02d}" for n in range(1, 7)}:
        raise ValueError("Rate denominator registry changed.")

    for name in ("tables", "figures", "alt-text"):
        (target / name).mkdir(parents=True)
    quality = quality_table(missingness)
    quarters = quarterly_table(source)
    write_csv(target / "tables/quality-missingness.csv", quality)
    shutil.copy2(rates_path, target / "tables/descriptive-rates.csv")
    write_csv(target / "tables/quarterly-index-counts.csv", quarters)
    style()
    render_quality(quality, target)
    render_rates(rates, target)
    render_quarters(quarters, target)
    alt_text(target)

    specs = (
        ("F01", "quality-missingness", "Which fields have accepted structural missingness or seeded missingness that required restoration?", "Missingness needs field rules, not one blanket fix", "Rows with blank value (%)", "Module 04 missingness profile", "grouped horizontal bars", "Accepted hatch ///; defective hatch xx", "none; no approved estimate", "Synthetic teaching layers; exact values in quality-missingness.csv", "Accepted optional missingness is not automatically error."),
        ("F02", "descriptive-rates", "What selected 30-day and 90-day events are recorded for the synthetic cohort?", "Recorded events vary by definition and time window", "Synthetic cohort (%)", "Module 05 rates and denominator registry", "horizontal point and interval", "direct count labels", "Wilson 95 percent from Module 05", "Exact values: descriptive-rates.csv; RT01 contains RT02-RT04; synthetic intervals only", "Synthetic descriptive intervals; no real-population inference."),
        ("F03", "quarterly-index-counts", "How are the 374 selected index encounters distributed across calendar quarters in the pinned synthetic cohort?", "Selected index encounters span 20 quarters", "Selected synthetic index encounters (n) by index-start quarter", "Module 05 resolved analytic table", "three-series line chart", "solid circle; dashed square; dotted triangle", "none; no approved estimate", "Exact values: quarterly-index-counts.csv; one index/person; not volume or a tested trend", "Selected indexes are not service volume or a tested trend."),
    )
    registry_rows = []
    for figure_id, stem, question, title, units, source_name, chart, cue, uncertainty, caption, limit in specs:
        png = target / f"figures/{stem}.png"
        svg = target / f"figures/{stem}.svg"
        table = target / f"tables/{stem}.csv"
        alternative = target / f"alt-text/{stem}.md"
        with Image.open(png) as image:
            width, height = image.size
            dpi = image.info.get("dpi", (0, 0))[0]
        registry_rows.append({
            "figure_id": figure_id, "question": question, "title": title, "units": units,
            "source": source_name,
            "source_sha256": "|".join(INPUTS[key][2] for key in ("missingness",) if figure_id == "F01") or "|".join(INPUTS[key][2] for key in (("rates", "registry") if figure_id == "F02" else ("source",))),
            "chart": chart, "table_path": f"tables/{stem}.csv", "table_sha256": sha256(table),
            "png_path": f"figures/{stem}.png", "png_sha256": sha256(png),
            "svg_path": f"figures/{stem}.svg", "svg_sha256": sha256(svg),
            "alt_text_path": f"alt-text/{stem}.md", "alt_text_sha256": sha256(alternative),
            "width_pixels": width, "height_pixels": height, "dpi": f"{dpi:.2f}",
            "canvas_inches": "7x4", "palette": f"{BLUE}|{ORANGE}|{BLACK}",
            "redundant_cue": cue, "uncertainty": uncertainty, "zero_baseline": "yes",
            "caption": caption,
            "claim_limit": limit,
        })
    write_csv(target / "figure-registry.csv", registry_rows)
    report = {
        "status": "pass", "version": "0.1.0",
        "inputs": {key: {"rows": INPUTS[key][0], "bytes": INPUTS[key][1], "sha256": INPUTS[key][2]} for key in INPUTS},
        "tables": {path.name: {"rows": len(read_csv(path)[1]), "bytes": path.stat().st_size, "sha256": sha256(path)} for path in sorted((target / "tables").glob("*.csv"))},
        "figures": {path.name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for path in sorted((target / "figures").glob("*"))},
        "registry": {"rows": len(registry_rows), "bytes": (target / "figure-registry.csv").stat().st_size, "sha256": sha256(target / "figure-registry.csv")},
    }
    with (target / "render-report.json").open("w", encoding="utf-8", newline="") as handle:
        handle.write(json.dumps(report, indent=2) + "\n")
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-module06-render-") as temp_dir:
        target = Path(temp_dir) / "release"
        report = render(DEFAULT_MISSINGNESS, DEFAULT_RATES, DEFAULT_REGISTRY, DEFAULT_SOURCE, target)
        assert len(report["figures"]) == 6 and report["tables"]["quarterly-index-counts.csv"]["rows"] == 20
        try:
            render(DEFAULT_MISSINGNESS, DEFAULT_RATES, DEFAULT_REGISTRY, DEFAULT_SOURCE, target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Renderer did not protect an existing target.")
    print("FND-1 Module 06 renderer self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--missingness", type=Path, default=DEFAULT_MISSINGNESS)
    parser.add_argument("--rates", type=Path, default=DEFAULT_RATES)
    parser.add_argument("--denominator-registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.target:
        parser.error("--target is required")
    try:
        report = render(args.missingness.resolve(), args.rates.resolve(), args.denominator_registry.resolve(), args.source.resolve(), args.target.resolve())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Render failed: {exc}\n")
    print(f"FND-1 Module 06 render passed: {len(report['figures'])} figures and {len(report['tables'])} exact tables.")


if __name__ == "__main__":
    main()

# Module 08 assessment

## Decision prompt

You support a hospital operations leader who has received a weekly Massachusetts inpatient occupancy chart. The leader wants to know whether the recent pattern requires immediate investigation, routine monitoring, or no action until the reporting context is clearer.

Build a time-focused evidence package that keeps raw values, dates, reporting coverage, assumptions, and uncertainty visible. The package must distinguish a useful signal from ordinary variation, seasonality, smoothing artifacts, and unsupported process-control claims.

## Source boundary

Use `data/ma_hospital_capacity_time_2024_2026.csv` or rebuild it from the pinned CDC query. You may use the all-jurisdiction release for a declared comparison, but the required decision remains about the Massachusetts series.

Do not:

- introduce patient-level or restricted data;
- convert jurisdiction aggregates into a claim about one hospital;
- drop a week because it weakens the pattern;
- replace missing source values with zero;
- treat reporting coverage as a correction weight;
- hide the raw series behind smoothing;
- call an outside-limit point a special cause without defending the process and baseline assumptions;
- label a source-schema event as a clinical intervention;
- claim that respiratory admissions caused an occupancy change from temporal alignment alone.

## Part 1: time and source audit

In `time-audit.md`, answer:

1. What is the unit of observation?
2. Is the time interval complete and equally spaced?
3. Which values are counts, rates, percentages, or derived summaries?
4. Does the set of reporting hospitals remain fixed?
5. Which source fields or definitions changed during the series?
6. What operational decision can this public aggregate support?
7. What hospital-level decision can it not support?
8. Which baseline, center line, smoothing rule, and limit formula will you use, if any?
9. What would make the process stable enough for a formal control chart?

Record the exact source URL, retrieval date, query period, release checksum, and tool versions.

## Part 2: run the reference lab

Run:

```powershell
Rscript lab.R
```

Inspect all five figures, the weekly table, and the text alternative. Record:

- what the run chart shows that a category chart would hide;
- how the respiratory series differ by pathogen and season;
- which abrupt weekly changes are softened by the four-week trailing mean;
- how the coverage panel changes the reading of the aggregate;
- why the individuals-chart limits are labeled exploratory;
- which facts are available in the CSV and text alternative but not from visual estimation alone.

## Part 3: critique and repair

Run:

```powershell
Rscript critique_charts.R
```

For each flawed display, document the reader task, defect, likely decision error, repair, evidence that the repair worked, and one remaining limit.

### C1: arbitrary dual axes

Explain how a freely chosen scale factor can manufacture visual agreement between occupancy and respiratory admissions. Repair the display using aligned panels, normalization with a defensible reference, or separate charts. Do not imply causation from visual overlap.

### C2: smoothed series without raw values

Identify at least one important weekly change hidden by the four-week trailing mean. Repair the display so the raw values remain primary and the smoothing window is named.

### C3: unsupported control limits

Identify the missing baseline, formula, process definition, seasonality check, and reporting review. Either remove the limits or rebuild an explicitly exploratory chart with a declared baseline and assumptions.

## Part 4: independent run chart

Create `run-chart.png` for the operations leader. It must:

- show all 94 weekly Massachusetts occupancy values in chronological order;
- use an honest y scale and readable date interval;
- label the metric, geography, unit, period, source, and aggregation level;
- include no more than one defensible descriptive reference line;
- directly annotate at least one source-supported time or reporting event;
- avoid inventing an intervention date;
- retain accessible contrast and a non-color reading path;
- point to the exact table and text alternative.

The required annotation may describe the January 2026 source-schema addition of respiratory-season fields. It must be labeled as a reporting or schema event, not a clinical event.

## Part 5: comparison chart

Create `comparison-chart.png` that answers one distinct question about seasonality, reporting, or related measures. Acceptable forms include:

- aligned panels for occupancy and reporting coverage;
- pathogen-specific respiratory admission series with color plus line type;
- indexed seasonal trajectories with a clearly named baseline;
- small multiples across selected jurisdictions with the same scale and inclusion rule.

The chart may not use arbitrary dual axes. If values are indexed, state the reference date and make raw units available in `decision-table.csv`.

## Part 6: process chart

Create `process-chart.png`. Choose one:

1. an exploratory individuals chart with a declared baseline and formula;
2. a run chart with an explicitly justified center line and run-rule analysis;
3. a documented decision not to use control limits because the process assumptions do not hold.

If option 3 is chosen, `process-chart.png` should visualize the evidence that prevents a stable-process claim, such as seasonality and changing coverage. A blank placeholder does not meet the requirement.

Every limit or rule must be reproducible in `analysis.R`. Label exploratory work as exploratory in the title or subtitle.

## Part 7: exact-value table

`decision-table.csv` must contain one row for every Massachusetts week and these columns:

```text
week_end
inpatient_occupancy_pct
occupancy_delta_pct_points
occupancy_rolling_4_week
icu_occupancy_pct
covid_new_admissions
flu_new_admissions
rsv_new_admissions
total_respiratory_new_admissions
hospitals_reporting_occupancy
hospitals_reporting_occupancy_pct
respiratory_season
source_season_status
process_flag
```

`process_flag` may be `not assessed`, `inside exploratory limits`, or `outside exploratory limits`. A stronger label requires a justified formal process-control design.

## Part 8: text alternative

`alt-text.md` contains:

```markdown
# Text alternative

## Short alternative

## Long description

### Purpose and structure

### Main time pattern

### Largest weekly changes

### Seasonal or reporting context

### Process-chart assumptions

### Decision boundary

### Exact-value table
```

The short alternative identifies the display and main finding in one or two sentences. The long description preserves the time span, value range, major changes, reporting context, method, and uncertainty. It points to `decision-table.csv` for all weekly values.

## Part 9: decision note

`decision-note.md` contains:

```markdown
# Decision note

## Decision owner and question

## Finding

## Action now

## Monitoring rule

## Reporting and process limits

## Evidence needed next
```

The action must be operationally specific. Examples include reviewing source reporting for a named week, comparing the public pattern with stable internal hospital measures, or maintaining routine monitoring. Do not prescribe a patient-care intervention from this aggregate alone.

## Exact submission

```text
module-08/
  time-audit.md
  analysis.R
  run-chart.png
  comparison-chart.png
  process-chart.png
  decision-table.csv
  alt-text.md
  decision-note.md
  ai-use.md
```

An approved alternative tool may replace `analysis.R` with an editable source file that regenerates all three figures and the CSV. Manual changes made only to exported PNG files do not meet the requirement.

## Rubric

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Source fidelity and temporal structure | 15% | All weeks, values, source behavior, dates, and aggregation boundaries are preserved and documented. |
| Run-chart judgment | 15% | The chart uses chronological order, a defensible scale and reference, useful annotation, and a decision-focused title. |
| Seasonality and reporting context | 15% | The comparison separates related questions and keeps reporting coverage or seasonal structure visible without deceptive scaling. |
| Process-chart reasoning | 20% | The process, baseline, formula, assumptions, limits, and interpretation are explicit, or non-use is well supported. |
| Smoothing and raw values | 10% | The smoothing window is named, raw values remain available, and hidden short changes are discussed. |
| Accessibility and exact alternatives | 10% | Redundant encodings, readable contrast, text alternatives, and the complete exact-value table support equivalent reading. |
| Reproducibility | 10% | The editable analysis regenerates the three figures and table from the released data. |
| Decision note and AI accountability | 5% | The action fits the evidence, and AI use or non-use is recorded with human verification. |

Passing requires at least 80 percent overall and every pass condition below.

## Noncompensable pass conditions

- All 94 Massachusetts weeks are present in the analysis and exact table.
- Raw values remain visible in at least the run chart and exact table.
- A smoothed line never appears without its named window and the raw series or direct path to it.
- No arbitrary dual axis is used.
- Every center line and limit has a declared data window and reproducible formula.
- Exploratory limits are labeled exploratory.
- Reporting coverage appears in the analysis and is not used as an undocumented correction weight.
- The source-schema event is not described as a clinical intervention.
- The recommendation does not make a hospital-level, causal, or patient-level claim.
- Figures retain the Module 07 accessibility contract.
- The analysis is editable and reproducible.
- No restricted patient or partner data are included.
- `ai-use.md` is complete, including when no AI was used.

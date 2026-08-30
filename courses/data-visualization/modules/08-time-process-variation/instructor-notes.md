# Module 08 instructor notes

## Teaching purpose

This module teaches that a line chart is not automatically a time analysis and that a control chart is not automatically a process claim. Learners must name the decision, unit, interval, baseline, reporting context, and assumptions before interpreting a pattern.

## Preparation

Before class:

1. run `python validate_nhsn_time_series.py`;
2. run `Rscript lab.R`;
3. run `Rscript critique_charts.R`;
4. inspect all eight PNG files at 100 percent zoom;
5. open `weekly_time_decision_table.csv` and confirm 94 weekly rows;
6. compare the raw and smoothed figures at 2024-12-28 and 2025-01-04;
7. review the CDC metadata and current landing page;
8. remind learners that the source is a jurisdiction aggregate across reporting hospitals.

## Reproducible answer facts

| Quantity | Answer |
|---|---:|
| All-jurisdiction rows | 6,208 |
| Jurisdictions | 67 |
| Massachusetts rows | 94 |
| Massachusetts date gaps | 0 |
| Occupancy minimum | 77.96% on 2024-12-28 |
| Occupancy maximum | 87.30% on 2025-03-01 |
| Occupancy mean | 83.87% |
| Occupancy median | 84.12% |
| Respiratory admission maximum | 1,996 on 2025-02-08 |
| Respiratory admission minimum | 13 on 2026-06-27 and 2026-07-18 |
| Reporting coverage minimum | 67.05% on 2025-02-15 |
| Reporting coverage maximum | 96.67% |
| Largest weekly occupancy rise | 6.35 percentage points on 2025-01-04 |
| Largest weekly occupancy decline | 7.79 percentage points on 2024-12-28 |
| Source season field unavailable | 61 weeks |
| Source season field reported | 33 weeks |
| Validation checks | 47 |
| All-jurisdiction SHA-256 | `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1` |
| Massachusetts SHA-256 | `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616` |

## Exploratory individuals-chart key

The reference uses the first 26 observations, 2024-11-09 through 2025-05-03.

| Quantity | Answer |
|---|---:|
| Baseline center | 85.23% |
| Mean moving range | 1.6964 percentage points |
| Lower exploratory limit | 80.72% |
| Upper exploratory limit | 89.75% |

The reference marks five observations below the exploratory lower limit:

- 2024-12-28;
- 2025-12-27;
- 2026-02-28;
- 2026-03-21;
- 2026-05-02.

Do not teach these as confirmed special causes. The chart combines jurisdiction aggregates across a changing set of reporting hospitals. It also spans seasonal respiratory patterns. The correct response is a question for review, not a verdict.

## Concept key

### Run chart

A run chart preserves order. The reference median is descriptive. It is not a goal, a national benchmark, or a control-chart center. Ask learners what decision would change if the median were removed.

### Baseline

A baseline is a declared data window tied to the process and decision. Choosing the first 26 weeks is transparent and reproducible, but it does not make that interval clinically stable. A learner may choose another window if the choice is stated before reviewing the result and is supported by process knowledge.

### Seasonality

The pathogen plot shows strong winter peaks, especially for influenza. It does not establish that respiratory admissions caused the occupancy pattern. Learners should compare shape, timing, reporting, and plausible lag while keeping the causal claim out of the chart title.

### Smoothing

The four-week trailing mean answers a slower trend question. It also delays peaks and softens the sharp decline on 2024-12-28 and rise on 2025-01-04. A smoothing choice must state the window, alignment, and missing edge behavior.

### Reporting coverage

The number and percent of hospitals reporting change. The aligned panel makes that context visible without mapping two unrelated scales onto one panel. Do not divide occupancy by reporting coverage or weight it again unless the source method explicitly supports that calculation.

### Source-schema event

The respiratory-season field is unavailable for 61 Massachusetts rows and reported for 33. Source metadata indicates the field was added in January 2026. This is a reporting event. It is not evidence that respiratory seasonality began in 2026.

## Lab walkthrough

### Figure 1: occupancy run chart

Ask learners to find the largest fall and rise before showing the exact table. Then ask whether the broad decline after early 2026 would be as clear in a category chart.

### Figure 2: respiratory admission seasonality

Ask learners to trace each pathogen using line type alone. Discuss why the three counts may be compared on a shared count axis but should not be collapsed without preserving the components.

### Figure 3: raw and smoothed occupancy

Ask which display an executive would prefer and which an operations analyst needs. Both can be useful, but the trailing mean cannot replace the weekly record.

### Figure 4: reporting coverage context

Ask whether a change in coverage proves a change in occupancy. It does not. The point is to identify a competing explanation and the evidence needed next.

### Figure 5: exploratory process chart

Read the title aloud. Have learners name each missing assumption before interpreting a triangle. The chart is successful when it starts a disciplined review instead of producing an automatic alarm.

## Critique key

### C1: arbitrary dual axes

Expected defects:

- a free scale factor makes unrelated shapes appear aligned;
- separate axes require repeated translation;
- visual proximity suggests association or causation;
- occupancy and admissions have different units and decision meanings;
- the chart omits reporting coverage.

An aligned-panel repair is preferred. A standardized index can pass only when the reference period and loss of raw units are explicit.

### C2: smoothed line only

Expected defects:

- the raw weekly values disappear;
- the four-week window and trailing alignment may be missed;
- sharp changes are delayed and reduced;
- the first three values are unavailable without explanation;
- operational review may begin too late.

### C3: invented limits

Expected defects:

- center and limits are chosen without data or method;
- no baseline period is named;
- the process unit is not defined;
- seasonality is ignored;
- reporting coverage is ignored;
- the chart uses alarm colors without an accessible redundant cue.

Deletion is an acceptable repair when the assumptions cannot be defended.

## Submission review order

Review in this order:

1. source and 94-week continuity;
2. unit of observation and aggregation boundary;
3. raw-series preservation;
4. baseline, smoothing, and limit definitions;
5. reporting and seasonal context;
6. accessibility and exact table;
7. decision language;
8. reproducibility;
9. AI-use record.

Return the work before visual-design scoring if the learner changes source values, drops weeks, or makes an unsupported hospital-level claim.

## Acceptable decision language

An acceptable conclusion is:

> Massachusetts inpatient occupancy declined from the higher levels seen in early 2025 and remained mostly near 81 to 83 percent from spring through summer 2026. Several weeks fall below exploratory limits calculated from the first 26 weeks, but changing reporting coverage, seasonal structure, and the jurisdiction-level aggregation prevent a formal special-cause conclusion. The operations leader should compare these dates with stable internal hospital measures and source reporting before assigning a cause or intervention.

Other conclusions may pass when they preserve the process and causal boundaries.

## Claims that do not pass

- "The control chart proves five special causes."
- "Respiratory admissions caused the occupancy peak."
- "Massachusetts hospitals became more efficient."
- "The 67.05 percent reporting week should be corrected to 100 percent."
- "The four-week average is the true occupancy."
- "Respiratory season began when the source field appeared."
- "A line chart proves an intervention worked."

## Accessibility review

Module 07 requirements remain binding. Check that:

- color is paired with line type, shape, position, or direct labels;
- text and critical marks remain readable in the final export;
- raw and smoothed series can be distinguished without hue;
- process flags use a non-color cue;
- every figure has short and long text support;
- the exact table has all 94 rows and clear headers;
- date labels and captions remain readable in print and a smaller view.

## Handoff to Module 09

Module 09 moves from temporal structure to multivariable comparison. Learners carry forward source fidelity, reporting context, accessible encoding, exact values, and claim discipline. Time should not be flattened into a single summary unless the new decision justifies the loss.

## Human release gates

The module still needs named reviews for:

- hospital operations relevance;
- statistical process-control instruction;
- CDC source fidelity;
- visualization teaching quality;
- accessibility and assistive-technology use;
- independent teachability on a clean system.

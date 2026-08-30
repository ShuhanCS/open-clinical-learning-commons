# DA-730 Module 08: Time and process variation

- Course: DA-730, Clinical data visualization and decision storytelling
- Instructional position: week 4, second applied-portfolio module
- Learner time: 8.5 hours
- Module version: 0.1.0
- Target Commons release: 0.19.0
- Primary environment: R and ggplot2
- Data build and validation: Python 3 standard library
- Clinical source: CDC National Healthcare Safety Network weekly hospital respiratory metrics by jurisdiction
- Public module package: `courses/data-visualization/modules/08-time-process-variation/`

## 1. Module identity and place in the course

Module 08 moves from a static comparison to a process observed through time. Modules 01 through 06 established visual encoding, comparison, distribution, denominators, rates, uncertainty, and missingness. Module 07 made accessible communication a standing requirement. Module 08 now asks what changes when chronological order, intervals, baselines, reporting windows, and process assumptions enter the decision.

The module is not a survey of time-series forecasting. It is a decision-focused introduction to run charts, seasonal comparison, smoothing, reporting context, and cautious process-chart reasoning. A learner must be able to say what a time display supports before adding a trend line or control limit.

The worked case uses weekly public Massachusetts hospital capacity and respiratory admission data. It is valuable because it is current, clinically recognizable, fully public, and imperfect in ways that matter. Reporting coverage changes. The hospital mix may change. A source field appears partway through the period. The all-jurisdiction release also contains unavailable values and published anomalies. Those conditions make the case more realistic than a clean textbook process.

Module 08 extends rather than replaces the Module 07 accessibility contract. Every figure must remain readable without color, include an exact-value path, preserve unavailable values, and carry a short and long text alternative.

## 2. Healthcare decision and audience

### Decision

A hospital operations leader asks whether a recent weekly pattern requires:

- immediate investigation;
- routine monitoring;
- comparison with stable internal data;
- source-quality review before interpretation;
- or no process claim because the assumptions do not hold.

### Decision owner

The primary decision owner is a hospital operations leader who understands capacity and staffing but may not know how a plotted baseline, smoothing window, or control limit was constructed.

Supporting readers include:

- a clinical quality analyst who must reproduce every value;
- an infection-prevention or epidemiology colleague reviewing respiratory context;
- an executive who needs the main pattern quickly;
- an accessibility user who needs the same finding through non-color cues, text, and a table;
- a data steward checking whether a change comes from reporting rather than care delivery.

### Decision questions

The learner must answer:

1. What changed, when, and by how much?
2. Is the series complete and equally spaced?
3. Does the plotted line describe a fixed process or a changing aggregate?
4. What does the raw weekly series show?
5. What does a four-week trailing mean reveal and hide?
6. Is an apparent pattern seasonal, operational, or a reporting artifact?
7. What baseline and formula produced each reference line?
8. Are control-chart assumptions strong enough for a special-cause claim?
9. What should the decision owner do next?
10. What additional internal evidence would change that action?

### Required decision language

The final recommendation uses one of these forms:

- "Investigate [date or interval] because [observed pattern] appears in the raw series, while [reporting and process limits] prevent a causal or formal special-cause conclusion."
- "Continue routine monitoring because [pattern] remains within the declared descriptive or exploratory frame, and review again when [named rule or date] occurs."
- "Compare with stable internal hospital data before acting because this public jurisdiction aggregate changes with [coverage or hospital mix]."
- "Do not use the proposed limits because [baseline, process, seasonality, or reporting assumption] is not defensible."

The learner may not write that a process is controlled, a point is a confirmed special cause, or an intervention worked solely because a line appears outside a calculated boundary.

## 3. Foundation skill revisited or extended

### Foundations I skills revisited

- parse and validate ISO dates;
- sort by time before calculating differences;
- verify uniqueness of the jurisdiction-week key;
- detect missing periods by checking date intervals;
- preserve source blanks instead of converting them to zero;
- calculate new fields from named source columns;
- pin a public query and checksum;
- write deterministic CSV releases;
- separate raw, normalized, derived, and presentation fields;
- record source anomalies rather than silently correcting them.

### Foundations II skills revisited

- distinguish counts, percentages, rates, and denominators;
- calculate and interpret a mean and median;
- compute a first difference and moving range;
- understand how aggregation changes a claim;
- distinguish description, detection, and causal inference;
- recognize confounding by changing measurement and reporting;
- state assumptions before applying a statistical rule;
- separate an exploratory signal from confirmatory evidence.

### Visualization foundations revisited

- use position along a common time axis for change;
- keep chronological order rather than sorting by value;
- select a y scale that supports the reader task without exaggeration;
- label units and periods directly;
- use annotations only for sourced events;
- avoid arbitrary dual axes;
- pair color with line type, shape, direct text, or panel position;
- provide exact values and text alternatives.

### New application

Learners connect time order to an operational decision. They must choose among a run chart, aligned seasonal comparison, smoothed display, or exploratory process chart and defend what each one can and cannot say.

## 4. Assessable learning outcomes

By the end of the module, a learner can:

1. state the unit of observation, time interval, aggregation level, and decision owner for a clinical time series;
2. verify unique dates, chronological order, and interval completeness;
3. distinguish a count, occupancy percentage, reporting percentage, and derived total;
4. create a run chart that retains every weekly observation;
5. choose a descriptive median, target, or no reference line for a stated question;
6. calculate weekly changes and identify the largest increase and decline;
7. calculate a named trailing mean and explain its edge behavior;
8. show raw and smoothed values together when short changes matter;
9. compare pathogen-specific seasonal patterns with shared units and accessible redundant cues;
10. display reporting coverage beside a process measure using aligned panels;
11. explain why reporting coverage is context rather than an automatic correction weight;
12. identify a source-schema event and keep it separate from a clinical intervention;
13. declare a baseline before calculating an exploratory center and limits;
14. reproduce individuals-chart limits using adjacent moving ranges;
15. explain why seasonality, changing coverage, and aggregate mix weaken formal process-control claims;
16. identify how arbitrary dual axes can manufacture visual agreement;
17. decide not to use a control chart when its assumptions cannot be defended;
18. create accessible static figures with exact data and text alternatives;
19. write an operational action that fits the public aggregate evidence;
20. record analysis, AI use, human checks, and remaining uncertainty.

### Mastery threshold

The learner earns at least 80 percent overall and passes every noncompensable condition in Section 15. A polished time chart fails if weeks disappear, the raw series is hidden, a dual axis manufactures agreement, limits have no declared baseline, reporting context is omitted, or the recommendation exceeds the jurisdiction-level evidence.

## 5. Concept ownership and boundaries

### Concepts owned by Module 08

- chronological visual order;
- run charts for operational learning;
- descriptive center lines;
- event annotations tied to evidence;
- trailing moving averages and their visual consequences;
- aligned panels as an alternative to arbitrary dual axes;
- reporting-coverage context for changing aggregates;
- exploratory individuals-chart construction;
- explicit baseline windows;
- moving ranges and the `1.128` constant for adjacent pairs;
- the difference between a signal question and a special-cause verdict;
- source-schema events within a time series;
- time-specific decision notes and monitoring rules.

### Concepts introduced but not mastered here

- formal run-chart rule testing;
- rational subgrouping;
- full statistical process-control design;
- autocorrelation diagnostics;
- interrupted time-series analysis;
- seasonal decomposition;
- forecasting;
- causal impact estimation;
- multilevel hospital time models;
- surveillance threshold construction.

These concepts may be named to set a boundary. They are not required methods for the submission.

### Concepts owned elsewhere

- Module 03 owns basic comparison and chart selection.
- Module 04 owns distributions and outlier judgment.
- Module 05 owns denominators and rate construction.
- Module 06 owns uncertainty, variation, and small-number suppression.
- Module 07 owns the complete accessibility baseline.
- Module 09 owns multivariable comparison and association.
- Foundations II owns the formal statistical ideas behind sampling variability and model interpretation.

### Prohibited shortcuts

- sorting weeks by occupancy;
- dropping inconvenient dates;
- using a category bar chart as the primary time display;
- showing a smooth without the raw series or exact path;
- using two freely scaled y axes to force overlap;
- calling a median a goal or control limit;
- calculating limits from the whole series after selecting interesting points;
- calling every outside-limit point a confirmed special cause;
- labeling January 2026 as a clinical intervention because a source field appeared;
- correcting official anomalies without a documented source correction;
- making a hospital-level claim from a jurisdiction aggregate.

## 6. Lesson sequence and learner time

Total expected learner time is 8.5 hours.

| Segment | Time | Mode | Product |
|---|---:|---|---|
| Decision launch and source framing | 0.5 hour | instructor-led | initial action hypothesis |
| Temporal structure and source audit | 0.75 hour | guided | completed audit notes |
| Run charts, scales, and annotations | 1.0 hour | mini-lesson plus lab | reference run chart |
| Seasonality and aligned comparisons | 0.75 hour | guided lab | pathogen and coverage readings |
| Smoothing and hidden weekly change | 0.75 hour | demonstration plus critique | raw versus smooth comparison |
| Baselines and exploratory individuals charts | 1.25 hours | technical workshop | reproducible center and limits |
| Flawed-chart critique and repair | 1.0 hour | paired critique | three repair plans |
| Independent analysis and figures | 1.5 hours | individual work | three final figures and table |
| Decision note, text alternative, and verification | 0.75 hour | individual work | final submission package |
| Total | 8.5 hours |  |  |

### Before class

Learners complete:

- the Module 07 accessibility submission or equivalent briefing;
- a short source-reading note on NHSN hospital respiratory reporting;
- the data validator;
- a one-paragraph statement of what one Massachusetts row represents.

### Synchronous opening

The instructor shows the raw occupancy series without a title or center line and asks:

1. What would you do after seeing this?
2. Which week attracts your attention?
3. What evidence would distinguish a clinical change from a reporting change?
4. Would the answer differ for a state analyst and one hospital's operations leader?

The goal is to expose that the same shape can support different decisions only after the process and audience are named.

### End-of-module checkpoint

Before submission, the learner performs a cold rerun from the released CSV, opens all figures at normal zoom, confirms the 94-row exact table, reads the short and long alternatives, and checks that the decision note names an action and an evidence boundary.

## 7. Authoritative readings and public clinical sources

### Required clinical source reading

1. CDC, Weekly Hospital Respiratory Data, HRD Metrics by Jurisdiction: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi
2. CDC, Hospital Respiratory Data reporting page: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html
3. CDC, NHSN Hospital Respiratory Data reporting protocol: https://www.cdc.gov/nhsn/pdfs/pscmanual/HRD-Protocol-Final.pdf

The CDC reporting page explains the weekly hospital respiratory reporting system and provides current forms, instructions, and quality-assurance resources. The protocol defines who reports and on what cadence. Learners use those sources to understand that the public table is built from facility reporting rather than a fixed experimental panel.

### Required method reading

1. Institute for Healthcare Improvement, Run Chart Tool: https://www.ihi.org/library/tools/run-chart-tool
2. NIST/SEMATECH, Individuals Control Charts: https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm

IHI establishes the practical role of run charts in improvement work. NIST provides the individuals-chart moving-range formula used in the reference lab. The module does not treat either source as permission to ignore process definition, baseline choice, seasonality, or reporting behavior.

### Standing accessibility sources

1. W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
2. W3C Understanding Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
3. W3C Complex Images: https://www.w3.org/WAI/tutorials/images/complex/

These remain required because line identity, process flags, annotations, exact values, and the overall time pattern must survive without color-only decoding.

### Reading prompts

Learners answer:

- Which facility types report weekly?
- What does one jurisdiction-week aggregate represent?
- Which part of the source documentation addresses reporting coverage or completeness?
- What is the purpose of a run chart?
- How does an individuals chart estimate variation from adjacent observations?
- Which assumptions are not guaranteed by a public jurisdiction aggregate?
- Which information in a multi-line time chart must remain available without hue?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Dataset A: all-jurisdiction normalized release

- File: `data/nhsn_hospital_capacity_jurisdiction_2024_2026.csv`
- Rows: 6,208
- Columns: 14
- Jurisdictions: 67
- Period: 2024-11-09 through 2026-08-22
- Unit: jurisdiction-week
- SHA-256: `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1`
- Public aggregate data: yes
- Synthetic: no

Teaching purpose:

- preserve the complete selected source context;
- show jurisdiction-week keys and missingness patterns;
- allow optional, declared cross-jurisdiction comparisons;
- expose official-source anomalies that require documentation rather than silent cleanup;
- support future modules without redownloading a different release.

### Dataset B: Massachusetts teaching release

- File: `data/ma_hospital_capacity_time_2024_2026.csv`
- Rows: 94
- Columns: 21
- Period: 2024-11-09 through 2026-08-22
- Unit: Massachusetts jurisdiction-week
- SHA-256: `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616`
- Weekly gaps: none
- Public aggregate data: yes
- Synthetic: no

Teaching purpose:

- provide one complete weekly sequence;
- keep occupancy, respiratory admissions, and reporting coverage in one reproducible table;
- show how a source field can become available partway through a series;
- support raw, seasonal, smoothed, aligned-panel, and exploratory process displays;
- make every answer checkable from exact values.

### Provenance chain

```text
CDC NHSN Socrata dataset rhwp-grxi
  -> exact 14-field query for 2024-11-09 through 2026-08-22
  -> raw response checksum d261cbc4...
  -> normalized 6,208-row jurisdiction release
  -> Massachusetts 94-row teaching release
  -> R reference figures and exact weekly decision table
```

### Rights and redistribution

The source is public United States government health-surveillance data. The package records the source, query, retrieval date, and public-data context. Commons documentation uses CC BY 4.0 and code uses MIT. The package does not contain protected health information, patient rows, or restricted partner data.

### Data minimization

The query selects only the fields needed for capacity, occupancy, respiratory admissions, reporting coverage, dates, jurisdiction, and source season status. It does not download unused source columns for the sake of volume.

### Source preservation rule

The all-jurisdiction release preserves:

- 120 jurisdiction-weeks with unavailable core metrics;
- three Guam inpatient rows where occupied counts exceed reported beds;
- three Guam or Northern Mariana Islands ICU rows where occupied counts exceed reported beds;
- one Wisconsin row with 100.68 percent reporting coverage.

Those records are documented and validated. They are not silently removed or capped. The Massachusetts teaching sequence contains no count-above-bed rows and has complete core metrics.

## 9. Data dictionary and expected analytic structure

### Source-preserving fields

| Field | Role | Expected use |
|---|---|---|
| `week_end` | temporal key | x axis, interval checks, annotations |
| `jurisdiction` | geographic key | Massachusetts filter or declared comparison |
| `respiratory_season` | source category | source-reported context only |
| `inpatient_beds` | count | exact context, reconciliation |
| `inpatient_beds_occupied` | count | exact context, reconciliation |
| `inpatient_occupancy_pct` | published percentage | primary run and process measure |
| `icu_beds` | count | optional secondary capacity context |
| `icu_beds_occupied` | count | optional secondary capacity context |
| `icu_occupancy_pct` | published percentage | optional aligned comparison |
| `covid_new_admissions` | count | pathogen-specific seasonal series |
| `flu_new_admissions` | count | pathogen-specific seasonal series |
| `rsv_new_admissions` | count | pathogen-specific seasonal series |
| `hospitals_reporting_occupancy` | count | reporting context and exact table |
| `hospitals_reporting_occupancy_pct` | percentage | aligned reporting-context panel |

### Derived teaching fields

| Field | Formula or rule | Interpretation |
|---|---|---|
| `week_index` | chronological row number | stable plotting and sequence check |
| `calendar_year` | year of `week_end` | calendar grouping |
| `iso_week` | ISO week of `week_end` | optional seasonal alignment |
| `source_season_status` | source label present or unavailable | schema and availability context |
| `days_since_prior` | current date minus prior date | gap detection |
| `total_respiratory_new_admissions` | COVID-19 + influenza + RSV admissions | combined source count when all components exist |
| `reporting_gap_pct` | 100 minus reporting coverage | descriptive missing-reporting context |

### Required learner-derived fields

| Field | Formula or rule | Interpretation |
|---|---|---|
| `occupancy_delta_pct_points` | current occupancy minus prior occupancy | weekly change in percentage points |
| `occupancy_rolling_4_week` | current and prior three weeks' mean | trailing direction, unavailable for first three rows |
| `process_flag` | declared learner rule | no stronger than assumptions support |

### Expected types

- Dates remain ISO dates in CSV and date objects in analysis.
- Counts remain integers when reported.
- Percentages remain numeric percentages on a 0 to 100 scale.
- Blank source fields remain blank or missing, not zero.
- Every derived value is reproducible from named columns.
- Every chart uses the published or documented derived value, not a hand-edited number.

### Unit-of-analysis warning

One row is not one patient, one hospital, or one admission. It is one weekly jurisdiction aggregate across reporting hospitals. A time point may therefore change because the underlying values change, the reporting set changes, or both.

## 10. Worked example and instructor walkthrough

### Step 1: verify the sequence

The validator confirms:

- 94 Massachusetts rows;
- unique dates;
- first date 2024-11-09;
- final date 2026-08-22;
- seven days between every adjacent pair;
- complete core capacity, occupancy, and admission metrics.

The instructor asks why a complete date sequence does not guarantee a stable process. Expected answer: the hospital mix and reporting coverage can still change.

### Step 2: draw the raw occupancy series

Plot every weekly occupancy value against `week_end`. Use points plus a line. Restricting the visible y range to 75 through 90 percent is acceptable because:

- the range is stated through labeled ticks;
- the chart is not a bar chart with a required zero baseline;
- the purpose is weekly variation within a high occupancy range;
- exact values are provided;
- the title does not exaggerate the movement.

The reference adds the series median of 84.12 percent as a dashed descriptive line. It labels the line directly and states that it is not a target or control limit.

### Step 3: identify exact extrema and changes

Measured facts:

- minimum occupancy is 77.96 percent on 2024-12-28;
- maximum occupancy is 87.30 percent on 2025-03-01;
- mean occupancy is 83.87 percent;
- median occupancy is 84.12 percent;
- largest weekly rise is 6.35 percentage points on 2025-01-04;
- largest weekly decline is 7.79 percentage points on 2024-12-28.

The sharp decline and rebound should trigger a source and process question. They do not independently prove a bed, staffing, holiday, or reporting event.

### Step 4: separate pathogen series

Plot COVID-19, influenza, and RSV admission counts on one shared count scale. Use color plus distinct line types. The combined respiratory count reaches 1,996 on 2025-02-08.

The instructor asks:

- Which pathogen contributes most to the largest winter peak?
- Does visual timing establish that admissions caused occupancy?
- What lag or internal data would be needed for a stronger claim?

### Step 5: compare raw and smoothed values

Calculate a four-week trailing mean:

```text
smooth[t] = mean(raw[t-3], raw[t-2], raw[t-1], raw[t])
```

The first three smoothed values are unavailable. Plot the raw values and trailing mean together. The learner must notice that smoothing reduces the visual size of the late-December fall and early-January rebound. Smoothing answers a broader direction question and should not become a substitute for operational detail.

### Step 6: place reporting coverage beside occupancy

Use aligned panels with a common date axis and separate y scales. The minimum reporting coverage is 67.05 percent on 2025-02-15. The maximum is 96.67 percent.

The correct interpretation is not that low coverage caused the occupancy value or that occupancy should be divided by coverage. The correct interpretation is that the aggregate's composition may differ and should be checked before assigning a process cause.

### Step 7: calculate exploratory individuals limits

Declare the first 26 weeks, 2024-11-09 through 2025-05-03, as the teaching baseline.

```text
center = mean(baseline occupancy) = 85.2346
MR[t] = abs(occupancy[t] - occupancy[t-1])
mean MR = 1.6964
sigma estimate = mean MR / 1.128
lower limit = center - 3 * sigma estimate = 80.7229
upper limit = center + 3 * sigma estimate = 89.7463
```

Five dates fall below the exploratory lower limit:

- 2024-12-28;
- 2025-12-27;
- 2026-02-28;
- 2026-03-21;
- 2026-05-02.

No point exceeds the upper exploratory limit.

The reference title begins with `EXPLORATORY`. Shape, not color alone, identifies the outside-limit points. The caption names the formula and the reasons a formal claim is weak.

### Step 8: write the action

The reference recommendation is to compare the marked dates and broad 2026 decline with stable internal hospital measures, staffing and capacity records, and source-reporting status before assigning a cause. The public series supports prioritizing dates for review. It does not prescribe a patient-care or staffing intervention.

## 11. Guided practice

### Exercise A: chart-role sorting

Learners match each question to a chart:

| Question | Best starting display |
|---|---|
| What happened each week? | raw run chart |
| How do three pathogen counts differ over the same period? | accessible multi-line chart |
| Did reporting coverage change near the observed pattern? | aligned panels |
| What broad direction remains after short weekly variation? | raw plus named smooth |
| Does a stable process show unusual variation? | process chart only after assumptions are established |

### Exercise B: annotation audit

Provide five candidate annotations:

1. source respiratory-season field added;
2. assumed holiday staffing shortage;
3. assumed policy change;
4. observed reporting coverage minimum;
5. observed respiratory admission maximum.

Learners may annotate items 1, 4, and 5 with source-supported language. Items 2 and 3 require external evidence before appearing as events.

### Exercise C: smoothing comparison

Learners calculate two-week and four-week trailing means, then compare:

- the date of the apparent low;
- the magnitude of the largest change;
- the number of unavailable edge values;
- the operational question each window answers.

The exercise is not a search for the most attractive curve. The learner chooses a window based on the decision and documents the loss of detail.

### Exercise D: baseline challenge

In small groups, learners propose a baseline and answer:

- Why does this interval represent the process before monitoring?
- Was the interval selected before looking for signals?
- Are reporting coverage and definitions stable?
- Is seasonality present?
- Would a median run chart be more honest?

Groups may conclude that no formal process limits should be used.

### Exercise E: accessible line identity

Learners view the pathogen chart in grayscale and at a smaller size. They must identify each series through line type or direct labels. Any legend-only or color-only distinction is repaired before proceeding.

## 12. Independent exercise

### Scenario

The operations leader has seen a smoothed Massachusetts occupancy line and a second respiratory-admission line on a dual axis. The chart implies that a respiratory surge caused the occupancy pattern and marks several weeks with unexplained red alarm lines.

The learner must replace that display with a reproducible decision package.

### Required analysis

The learner must:

1. load the released Massachusetts CSV;
2. assert 94 unique weekly rows;
3. verify seven-day intervals;
4. calculate weekly occupancy changes;
5. calculate a four-week trailing mean or defend another named window;
6. retain all raw weekly values;
7. compare occupancy with reporting coverage or pathogen-specific admissions;
8. declare a baseline and formula for any process limits;
9. label process results no more strongly than the assumptions support;
10. export the exact decision table;
11. write short and long text alternatives;
12. write a decision note with an action and monitoring rule;
13. document AI use or non-use and human verification.

### Required products

- `run-chart.png` answers what changed over time.
- `comparison-chart.png` answers a distinct seasonal or reporting question.
- `process-chart.png` either presents defensible exploratory process reasoning or visualizes why control limits are not appropriate.
- `decision-table.csv` contains all exact weekly values and derived fields.
- `time-audit.md` documents source, interval, aggregation, baseline, smoothing, and limits.
- `alt-text.md` provides an equivalent reading path.
- `decision-note.md` tells the operations leader what to do next.
- `analysis.R` regenerates the figures and table.
- `ai-use.md` records tool involvement and human checks.

### Independent choice

The learner may add one cross-jurisdiction comparison from the all-jurisdiction release. If used, the learner must declare:

- the jurisdiction inclusion rule;
- missingness and coverage criteria;
- whether the same weeks are compared;
- whether scales are shared;
- why the comparison changes the decision.

This optional comparison may not replace the required Massachusetts analysis.

## 13. Visualization and communication requirements

### Run chart

- Time proceeds left to right.
- All 94 values are present.
- Points remain visible even when a line is used.
- The date axis is readable and not labeled at every week.
- The y axis states percent and uses a defensible range.
- A reference line is directly labeled and correctly named.
- Annotations describe observed or sourced events.
- The title states a finding, not a method alone.
- The source, period, geography, and aggregation appear in the figure or adjacent caption.

### Comparison chart

- Shared units may share an axis.
- Different units use aligned panels or clearly documented normalization.
- Arbitrary dual axes are prohibited.
- A normalized index names its baseline and makes raw units available.
- Multiple lines use a non-color cue.
- Direct labels are preferred when space permits.
- Reporting coverage remains context and is not presented as an adjusted value.

### Process chart

- The process measure is named.
- The baseline start and end dates are named.
- The center-line statistic is named.
- Every limit formula is reproducible.
- Exploratory status is visible in the title or subtitle.
- Outside-limit points use shape or direct text, not color alone.
- The chart states why formal process-control assumptions may fail.
- A learner may choose not to calculate limits.

### Smoothing

- The raw series remains visible or immediately available.
- The window length and alignment are named.
- Edge missingness is visible and explained.
- The title does not imply that the smooth is the true series.
- The decision note identifies at least one short change the smooth reduces or delays.

### Accessibility

- Color is never the only series or flag cue.
- Critical text and marks retain readable contrast.
- The main pattern survives grayscale.
- A smaller-view and print check are documented.
- A short alternative identifies the chart and main finding.
- A structured long description preserves time structure, extrema, context, and limits.
- The exact CSV provides all weekly values.

### Claim discipline

Figure titles and decision notes may state:

- a value rose or fell;
- a period had a higher or lower observed aggregate;
- a seasonal pattern is visible;
- reporting coverage changed;
- a point falls outside explicitly exploratory limits;
- internal data are needed before acting.

They may not state:

- one variable caused another;
- a public aggregate proves one hospital's performance;
- a source-schema change is a clinical intervention;
- a process is stable or controlled without supporting evidence;
- a smoothed value is more real than the weekly observations.

## 14. Exact submission package and filenames

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

### `time-audit.md`

```markdown
# Time and source audit

## Decision and reader

## Source, query, period, and checksum

## Unit, aggregation, and reporting cadence

## Date continuity and missingness

## Metric definitions and derived values

## Reporting coverage and source-schema events

## Smoothing rule and hidden detail

## Baseline and process assumptions

## Claims supported and not supported

## Reproducibility record
```

### `decision-table.csv`

Required columns, in order:

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

The table contains 94 rows sorted by `week_end`. Blank values remain blank.

### `alt-text.md`

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

### `decision-note.md`

```markdown
# Decision note

## Decision owner and question

## Finding

## Action now

## Monitoring rule

## Reporting and process limits

## Evidence needed next
```

### `ai-use.md`

```markdown
# AI-use record

## Tool and model

## Work delegated

## Prompts or instructions

## Outputs retained or rejected

## Source and calculation verification

## Accessibility verification

## Human decisions
```

If no AI tool was used, the file states that directly and records the manual verification process.

### File-quality rules

- PNG files are final exports, not screenshots of code or a desktop.
- `analysis.R` runs from the released data and regenerates all figures and the CSV.
- The Markdown files contain complete analysis, not links to private notes.
- The CSV uses stable headers and ISO dates.
- Every source link is a complete visible URL.
- No temporary outputs, credentials, restricted data, or hidden workbook dependencies are included.

## 15. Rubric and pass conditions

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Source fidelity and temporal structure | 15% | All 94 weeks, exact values, source behavior, aggregation, and dates are preserved and documented. |
| Run-chart judgment | 15% | Chronological order, defensible scale, reference line, annotation, title, and source support the decision. |
| Seasonality and reporting context | 15% | The comparison answers a distinct question and keeps coverage or seasonal structure visible without deceptive scaling. |
| Process-chart reasoning | 20% | The process, baseline, formula, assumptions, limits, and interpretation are explicit, or non-use is well supported. |
| Smoothing and raw values | 10% | The named smooth is reproducible, raw values remain available, and hidden short changes are discussed. |
| Accessibility and exact alternatives | 10% | Redundant encodings, readable contrast, text alternatives, and the complete table provide equivalent access. |
| Reproducibility | 10% | The editable analysis regenerates three figures and the table from the released CSV. |
| Decision note and AI accountability | 5% | The action fits the evidence, and tool use or non-use is recorded with human verification. |

### Score interpretation

- 90 to 100: release-ready after named human review;
- 80 to 89: passes with targeted revisions;
- 70 to 79: substantial resubmission required;
- below 70: the decision package is not usable.

### Noncompensable pass conditions

1. All 94 Massachusetts weeks remain in the analysis and exact table.
2. Raw weekly values remain visible in the run chart and table.
3. Smoothing includes a named window, alignment, and raw-value path.
4. No arbitrary dual axis is used.
5. Every center line and limit has a declared data window and reproducible formula.
6. Exploratory limits are labeled exploratory.
7. Reporting coverage appears and is not used as an undocumented correction weight.
8. A source-schema event is not described as a clinical intervention.
9. The recommendation stays at the jurisdiction-aggregate evidence level.
10. Color is not the only series or process-flag cue.
11. Short text, long text, and the exact table are present.
12. The editable analysis regenerates the submitted products.
13. No protected or restricted data are included.
14. `ai-use.md` is complete.

Failure of any one condition requires revision regardless of the weighted score.

## 16. Common errors, failure modes, and interventions

### Error 1: time is sorted by value

Symptom: the learner creates a ranked line or bar chart.

Intervention: restore chronological order and ask what information disappeared when adjacent weeks were separated.

### Error 2: the y axis manufactures drama

Symptom: a narrow unlabeled range makes a small change look catastrophic.

Intervention: require readable ticks, exact values, a purpose statement, and a comparison with a wider defensible range.

### Error 3: the median becomes a target

Symptom: the chart labels the series median as desired occupancy.

Intervention: rename it descriptive or replace it with a sourced operational goal. Do not infer a target from the data.

### Error 4: an arbitrary dual axis implies agreement

Symptom: occupancy and admissions overlap after a free rescaling.

Intervention: use aligned panels or a declared index. Ask whether another scale factor would reverse the visual story.

### Error 5: smoothing hides the operational event

Symptom: only the trailing mean is shown.

Intervention: restore raw points and line, state the window, and identify the largest change lost by smoothing.

### Error 6: the first baseline that creates signals is selected

Symptom: the learner tries several windows and reports the one with the most alarms.

Intervention: require the baseline rationale and selection timing in the audit. Label post hoc limits exploratory or remove them.

### Error 7: outside limit means confirmed special cause

Symptom: every triangle becomes an operational failure.

Intervention: separate the calculation from the process claim. Require evidence about a stable measure, process, reporting set, and causal event.

### Error 8: reporting coverage becomes a weight

Symptom: occupancy is divided by the percentage of hospitals reporting.

Intervention: restore the published percentage and show coverage in a separate panel. Explain that the source aggregate already follows its own method.

### Error 9: schema availability becomes season onset

Symptom: the learner writes that respiratory season began when the field first appears.

Intervention: label the date as a source-schema event and use observed admission counts for seasonal discussion.

### Error 10: calendar alignment becomes causation

Symptom: respiratory admissions and occupancy peak near each other, so the title says one caused the other.

Intervention: replace causal language with temporal association and name the internal evidence or design needed next.

### Error 11: public aggregate becomes hospital judgment

Symptom: the recommendation tells one hospital to change staffing.

Intervention: narrow the action to source review and comparison with stable internal measures.

### Error 12: accessibility regresses

Symptom: three lines differ only by hue or outside-limit points are red circles among black circles.

Intervention: add line type, shape, direct label, or panel position and rerun grayscale and smaller-view checks.

### Error 13: source anomalies disappear

Symptom: the all-jurisdiction table is filtered until all values look plausible without a record.

Intervention: restore the official rows, document the anomaly, and create a separate sensitivity analysis if exclusion is justified.

### Error 14: exact values and text alternatives are missing

Symptom: only PNG files are submitted.

Intervention: return the package until the 94-row table, short alternative, and structured long description exist.

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

The Module 07 contract is cumulative. Every final figure must:

- avoid color-only line identity;
- use readable text, date labels, and critical marks;
- survive grayscale and print;
- remain interpretable in a smaller viewing context;
- provide exact values in a structured CSV;
- have a short alternative and structured long description;
- expose missing and unavailable values;
- use a predictable chronological reading order.

### Equity

Jurisdiction aggregates can hide differences across community, hospital type, rurality, language, disability, insurance, and access. Learners should not describe the statewide pattern as every Massachusetts patient's experience.

An equity statement belongs in the decision note when it changes the action. A concise acceptable form is:

> The statewide aggregate may hide different capacity and access patterns across hospitals and communities. Compare the flagged dates with stratified internal measures before directing resources.

The module does not require speculative subgroup claims when subgroup data are absent.

### Privacy

The supplied releases contain public aggregate surveillance data. They contain no patient identifiers or protected health information. Learners may not enrich the assignment with patient-level, employee-level, or restricted partner records.

### Responsible claims

The strongest supportable claims are descriptive and operational:

- observed weekly occupancy changed;
- respiratory admissions show seasonal peaks;
- reporting coverage varied;
- a declared exploratory rule marks certain dates;
- internal stable-process evidence is needed next.

Unsupported claims include:

- causal effects of respiratory admissions, staffing, or policy;
- one hospital's process status;
- patient-level risk;
- system efficiency;
- confirmed special cause from the public aggregate alone.

### Source anomaly handling

An implausible published value is not permission to overwrite the source. The learner records the original value, checks metadata, looks for a documented correction, and separates any sensitivity analysis from the released record.

## 18. AI and agent policy

### Permitted uses

Learners may use AI tools to:

- explain unfamiliar code or error messages;
- draft alternative chart approaches;
- suggest plain-language titles or text-alternative structure;
- identify possible data-quality checks;
- generate a first pass of routine plotting code;
- compare a learner-written decision note with the rubric.

### Required human work

The learner remains responsible for:

- opening and reading the source documentation;
- verifying all 94 rows and checksums;
- confirming date order and weekly intervals;
- recalculating extrema, changes, smoothing, center, and limits;
- selecting the baseline and defending it;
- checking that reporting coverage is not misused;
- inspecting every final chart in color, grayscale, print, and smaller view;
- verifying the short and long alternatives against the figure and table;
- approving every claim and action.

### Prohibited uses

AI may not:

- invent a source, intervention, baseline rationale, or result;
- silently replace missing values;
- select a baseline solely to produce desired signals;
- change official source anomalies without a record;
- write a causal conclusion unsupported by the analysis;
- certify accessibility or clinical correctness;
- receive protected, restricted, or confidential records.

### Minimum AI-use record

`ai-use.md` states:

- tool and model;
- work delegated;
- prompts or instructions;
- output retained, revised, or rejected;
- source and calculation checks;
- accessibility checks;
- final human decisions.

The record is required even when the learner used no AI.

## 19. Answer key and instructor notes

### Source and structure answers

- Unit: one jurisdiction-week aggregate across reporting hospitals.
- Geography: Massachusetts for the teaching release.
- Period: 2024-11-09 through 2026-08-22.
- Rows: 94.
- Interval: seven days between every adjacent week.
- Core missingness in Massachusetts: none.
- Source season field: unavailable for 61 weeks and reported for 33.
- Reporting set: not guaranteed to be fixed.

### Run-chart answers

- Minimum: 77.96 percent on 2024-12-28.
- Maximum: 87.30 percent on 2025-03-01.
- Mean: 83.87 percent.
- Median: 84.12 percent.
- Largest rise: 6.35 percentage points on 2025-01-04.
- Largest decline: 7.79 percentage points on 2024-12-28.

### Seasonal and reporting answers

- Combined respiratory admission maximum: 1,996 on 2025-02-08.
- Combined respiratory admission minimum: 13 on 2026-06-27 and 2026-07-18.
- Reporting coverage minimum: 67.05 percent on 2025-02-15.
- Reporting coverage maximum: 96.67 percent.
- Correct boundary: temporal alignment may motivate review but does not establish causation.

### Smoothing answer

The four-week trailing mean uses the current week and prior three weeks. The first three values are unavailable. It makes the broad direction easier to see but reduces and delays abrupt weekly changes. Learners should identify the 2024-12-28 decline and 2025-01-04 rebound as examples.

### Exploratory individuals-chart answer

- Baseline: first 26 weeks, 2024-11-09 through 2025-05-03.
- Center: 85.2346 percent.
- Mean moving range: 1.6964 percentage points.
- Sigma estimate: mean moving range divided by 1.128.
- Lower limit: 80.7229 percent.
- Upper limit: 89.7463 percent.
- Outside lower limit: 2024-12-28, 2025-12-27, 2026-02-28, 2026-03-21, and 2026-05-02.
- Outside upper limit: none.
- Interpretation: exploratory review dates, not confirmed special causes.

### Critique answer

#### C1

The dual-axis scale factor is chosen only to make the lines overlap. The repair uses aligned panels, direct labels, and separate units. It removes the visual suggestion of a shared magnitude or causal relation.

#### C2

The smoothed-only chart removes raw changes, delays the series, and hides three initial missing smooth values. The repair restores the raw line and points, names the trailing window, and explains what the smooth hides.

#### C3

The fixed values 80, 82, and 84 have no data or process basis. The repair either removes them or calculates explicitly exploratory limits from a declared baseline, formula, and process caveat.

### Acceptable final recommendation

> Massachusetts inpatient occupancy was lower through much of 2026 than during the first half of the released series. Five weeks fall below exploratory limits based on the first 26 weeks, but the public series combines reporting hospitals and spans seasonal and coverage changes. Review those dates against stable internal hospital occupancy, capacity, staffing, and reporting records before assigning a cause. Continue weekly monitoring with raw values and coverage shown together.

### Claims that fail

- "Five special causes prove the process improved."
- "The respiratory surge caused the occupancy peak."
- "Hospitals operated below capacity after the intervention."
- "Low reporting can be corrected by dividing the occupancy rate."
- "The smoothed line removes noise and shows the true process."
- "Massachusetts hospitals should change staffing because of this chart."

### Instructor facilitation notes

1. Begin with the decision, not the formula.
2. Ask what one row represents before showing any line.
3. Make learners identify the largest raw changes before introducing smoothing.
4. Show the dual-axis critique long enough for the visual relationship to feel convincing, then reveal the arbitrary scale factor.
5. Require baseline and process definitions before calculating limits.
6. Praise a well-supported decision not to use control limits.
7. End by having learners read the recommendation and delete every word that claims more than the public aggregate supports.

## 20. Runnable acceptance checks

### Data build

From the module directory:

```powershell
python build_nhsn_time_series.py
```

Expected behavior:

- downloads the exact pinned query;
- stops if the raw checksum changed;
- requires the exact 14-field schema;
- requires 6,208 selected rows and 67 jurisdictions;
- requires the pinned date range;
- writes both deterministic CSV releases;
- requires 94 consecutive Massachusetts weeks.

Offline rebuild:

```powershell
python build_nhsn_time_series.py --raw-input nhsn-pinned-query.csv
```

### Data validation

```powershell
python validate_nhsn_time_series.py
```

Expected result:

```text
Module 08 NHSN time data passed 47 checks.
All-jurisdiction rows: 6,208; SHA-256: 8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1
Massachusetts rows: 94; SHA-256: 394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616
```

### Reference lab

```powershell
Rscript lab.R
```

Expected outputs:

```text
output/
  01-occupancy-run-chart.png
  02-respiratory-admission-seasonality.png
  03-raw-and-smoothed-occupancy.png
  04-reporting-coverage-context.png
  05-exploratory-control-chart.png
  weekly_time_decision_table.csv
  alt-text-reference.md
```

### Critique set

```powershell
Rscript critique_charts.R
```

Expected outputs:

```text
critique-output/
  C1-arbitrary-dual-axis.png
  C2-smoothed-line-hides-weekly-change.png
  C3-unsupported-control-limits.png
```

### Visual acceptance

The instructor or reviewer confirms:

- every output opens successfully;
- the run chart has 94 visible weekly observations;
- the median is labeled descriptive;
- pathogen lines remain identifiable without color;
- raw and smoothed occupancy are both visible;
- reporting coverage appears in a separate aligned panel;
- process limits are labeled exploratory with baseline and formula;
- process flags use shape as well as position;
- captions remain readable at normal zoom;
- text alternatives match the exact table.

### Repository checks

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
node --check curriculum-data.js
node --check site.js
git diff --check
```

All checks must pass before the module release is committed.

## 21. Release status, reviewers, version, and known issues

### Release status

- Module version: 0.1.0
- Commons release: 0.19.0
- Status: runnable release candidate
- Technical validation date: 2026-08-29
- Data validator: 47 of 47 checks pass
- Lab execution: five PNGs, one CSV, and one Markdown text alternative pass
- Critique execution: three deliberately flawed PNGs pass
- Tested environment: Windows, Python 3, R 4.6.1, ggplot2 4.0.3

### Required human reviewers

| Review role | Reviewer | Status | Required evidence |
|---|---|---|---|
| Hospital operations relevance | unassigned | pending | decision and action fit an operations leader |
| Statistical process-control instruction | unassigned | pending | baseline, formula, assumptions, and language are sound |
| CDC source fidelity | unassigned | pending | field meanings, reporting behavior, anomalies, and limits are accurate |
| Visualization teaching quality | unassigned | pending | chart sequence and critiques teach the intended judgments |
| Accessibility and assistive technology | unassigned | pending | figures, text, and table provide equivalent access |
| Independent teachability | unassigned | pending | a new instructor can run and teach the package on a clean system |

### Known issues

1. Named human reviews remain pending.
2. The Massachusetts series is a jurisdiction aggregate across a changing set of reporting hospitals, not one stable hospital process.
3. The exploratory individuals-chart baseline is transparent but not independently established as stable.
4. Seasonality, changing coverage, and aggregate mix weaken formal special-cause claims.
5. The source respiratory-season field is unavailable for 61 of 94 teaching rows because it was added later.
6. The all-jurisdiction release contains published anomalies that are preserved and documented rather than corrected.
7. The static accessibility checks do not cover every browser, assistive technology, printer, or viewing condition.
8. Technical execution has been tested on Windows. macOS and Linux clean-run verification remains pending.

### Release decision

Technical release is permitted when all automated checks pass and the repository integration is current. Instructional release still requires named human review. Any revision that changes the source query, checksums, row count, baseline, formula, required outputs, or interpretation boundary requires a new module version and updated release metadata.

### Handoff to Module 09

Module 09 inherits:

- the exact public-source and checksum record;
- the distinction between time and cross-sectional comparison;
- reporting context and aggregation boundaries;
- the accessible line, text, and table contract;
- the rule that a visual association is not a causal conclusion;
- the requirement for a specific decision and next evidence.

If Module 09 summarizes the time series into a single multivariable record, it must state which period and summary were chosen and what temporal information was lost.

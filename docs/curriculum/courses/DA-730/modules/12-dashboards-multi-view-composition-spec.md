# DA-730 Module 12 specification: Dashboards and multi-view composition

Status: runnable release candidate
Module version: 0.1.0
Commons release: 0.23.0
Course owner: Ali Goff
Curriculum sponsor: Shuhan He
Technical package: `courses/data-visualization/modules/12-dashboards-multi-view-composition/`
Module hours: 8.5
Week: 6

## 1. Purpose, scope, and ownership

Module 12 teaches learners to compose the minimum set of views needed for one person to notice an exception, understand its limits, and take the next defensible action.

The central question is not, How many metrics can fit on one screen? It is, What decision should become easier, which evidence is necessary, and what happens next?

The module owns:

- dashboard purpose and audience;
- decision ownership;
- monitoring, review, and reporting distinctions;
- view-purpose audits;
- information hierarchy across coordinated views;
- alert definitions and states;
- measure dictionaries;
- units, direction, denominators, and reporting windows;
- threshold origin and ownership;
- refresh cadence and stale-data behavior;
- overview, comparison, exact-value, and action views;
- multi-view consistency;
- exception-to-action sequences;
- accessible dashboard alternatives;
- removal of decorative or redundant views; and
- reproducible dashboard release contracts.

The module does not own:

- real-time emergency department operations;
- production data pipelines;
- hospital performance rating;
- CMS measure development;
- clinical intervention approval;
- causal analysis;
- risk adjustment;
- statistical process control methods beyond prior course concepts;
- live electronic health record integration;
- production authentication or authorization;
- automated alert delivery;
- final two-audience narrative production; or
- a requirement to use a commercial dashboard product.

Module 11 owns flow, networks, composition, and hierarchy. Module 13 owns the final decision story, audience adaptation, and defense.

### Required intellectual move

Before creating a dashboard, the learner must write one sentence containing the audience, repeated task, decision, supported action, data cadence, and action boundary.

Every retained view must answer a named question that another retained view cannot answer as well.

### Completion standard

The module is complete when the learner can defend a three-through-five-view dashboard, trace every displayed value to a source and definition, explain what happens when data are stale, and connect the alert to a named owner and ordered response.

## 2. Healthcare decision and audience

### Decision owner

The reference decision owner is an emergency department quality director at a low-volume Massachusetts hospital.

### Decision

Decide whether a released public CMS signal is sufficient to open a local definition and current-data review.

### Repeated task

When a new public reporting release becomes available, the director reviews selected emergency department measures, verifies their reporting windows, checks whether a locally governed review trigger is crossed, and assigns the next validation action.

### Supported action

The reference dashboard may support a decision to:

1. validate the CMS-to-local numerator, denominator, exclusions, and extract completeness;
2. pull current local monthly OP-22 and emergency department time data;
3. review arrival, triage, staffing, capacity, communication, and access conditions if the current signal persists; and
4. record the owner, chosen action, and next review date.

### Unsupported actions

The public dashboard does not support:

- calling the displayed value current performance;
- changing staffing from the public value alone;
- changing clinical care from the public value alone;
- attributing the value to patients, clinicians, or one operational cause;
- ranking overall hospital quality;
- treating the Massachusetts median as an official benchmark;
- treating the course trigger as a CMS threshold;
- estimating an intervention effect;
- making an individual patient decision; or
- claiming that the public measure captures all dimensions of emergency care.

### Reference decision

The course scenario selects Anna Jaques Hospital, CMS facility ID `220029`, because:

- CMS reports a low emergency department volume category;
- OP-22 is 23 percent;
- 23 percent is the highest observed value among 53 reporting Massachusetts hospitals;
- the descriptive Massachusetts median is 3 percent;
- the mock quality-improvement review trigger is 10 percent;
- the public reporting period ended 590 days before CMS released the file; and
- the immediate defensible action is validation and current local data review.

The dashboard supports opening the review. It does not support a judgment about current care.

### Audience needs

The emergency department quality director needs:

- one dominant alert;
- direct values and units;
- exact measure definitions;
- visible reporting windows;
- a clear stale-data state;
- a descriptive peer reference;
- a labeled scenario threshold;
- a named threshold owner;
- the selected measure sample or denominator;
- an exact-value table;
- a reproducible source record; and
- an ordered action sequence.

## 3. Competency and learning outcomes

### Competency

Design and defend a small, coordinated, reproducible dashboard that supports one healthcare decision while preserving measure definitions, time, uncertainty boundaries, accessibility, provenance, and action ownership.

### Learning outcomes

By the end of the module, learners can:

1. name one dashboard audience;
2. name the repeated task;
3. state one decision;
4. state one supported action and at least one unsupported action;
5. distinguish a dashboard from a report, scorecard, and analysis page;
6. distinguish public reporting review from operational monitoring;
7. limit a dashboard to three through five necessary views;
8. complete a view-purpose audit;
9. establish one dominant alert hierarchy;
10. define every measure, unit, direction, population, sample, and window;
11. keep incompatible units on separate numeric scales;
12. keep different reporting windows visible;
13. distinguish a descriptive peer median from a benchmark;
14. distinguish a scenario trigger from an official threshold;
15. name the threshold owner and alert action;
16. calculate and display source lag;
17. define refresh cadence and stale-data behavior;
18. preserve unavailable values and source footnotes;
19. provide an exact table outside the graphical dashboard;
20. create a measure dictionary;
21. connect each alert to an ordered response;
22. remove filters without a named task;
23. remove decorative widgets and redundant views;
24. use color as a supporting cue rather than the only status cue;
25. write an equivalent text alternative;
26. reproduce the dashboard from committed data and code;
27. document AI assistance and number verification; and
28. hand a stable evidence package to Checkpoint 2 and Module 13.

### Mastery evidence

Mastery requires a dashboard brief, view-purpose audit, editable analysis, dashboard image, exact decision table, measure dictionary, source record, text alternative, decision note, and AI-use record.

## 4. Prerequisites and conceptual handoff

### Required prerequisites

Learners should have completed Modules 01 through 11.

### Inherited competencies

Module 12 assumes learners can:

- map variables to visual channels;
- evaluate perceptual accuracy;
- choose a chart, table, or no chart;
- show distributions instead of isolated summaries;
- define rates and denominators;
- state uncertainty and small-number limits;
- communicate without color dependence;
- distinguish time sequence from process variation;
- compare groups on aligned scales;
- state what geography adds and conceals; and
- define flows, states, paths, composition, and hierarchy.

### Specific handoff from Module 11

Module 11 ended with several possible structural views and a rule that every view must serve a decision. Module 12 asks which views belong together, which view dominates, which exact values remain available, and which views should be removed.

### Difference from an operational dashboard

The reference source is a public aggregate release with reporting windows that ended hundreds of days before publication. The module therefore teaches a public-reporting review dashboard.

A real operational emergency department dashboard would require:

- current governed local data;
- a defined refresh service level;
- source-completeness monitoring;
- role-based access;
- downtime and stale-state handling;
- clinical and operational governance;
- alert escalation rules;
- production testing; and
- evaluation of unintended effects.

These requirements are discussed but not simulated as completed.

### Misconceptions to diagnose before the lab

- A dashboard must contain many metrics.
- A public reporting value becomes current when placed on a dashboard.
- Every available filter improves usability.
- A state median is a performance target.
- A line at 10 percent is a CMS threshold if it appears beside a CMS measure.
- Percent and minutes can share a scale after normalization.
- A gauge is more actionable than a direct value.
- Red and green are enough to communicate status.
- A dashboard eliminates the need for an exact table.
- A high public value authorizes an intervention.

## 5. Workload and module sequence

The module has 8.5 learner hours within instructional week 6.

| Component | Hours | Evidence |
|---|---:|---|
| Audience, decision, owner, and action boundary | 0.6 | One-sentence dashboard contract. |
| Dashboard forms and view-purpose audit | 0.7 | Retained and rejected view table. |
| Measure dictionary and source-window audit | 0.8 | Three-row dictionary draft. |
| Threshold ownership and stale-data behavior | 0.7 | Alert-state contract. |
| Source trace and reference case | 0.7 | One traced source row per measure. |
| Reference dashboard lab | 0.9 | Five regenerated views and exact table. |
| Critique and repair | 0.8 | Three diagnosed failures. |
| Independent build | 1.8 | Editable source and dashboard. |
| Exact table, text alternative, and decision note | 0.8 | Complete evidence package. |
| Peer audit and Checkpoint 2 handoff | 0.7 | Signed audit and selected checkpoint evidence. |
| Total | 8.5 |  |

### Recommended order

1. Name the audience and repeated task.
2. State the exact decision.
3. Define the supported and unsupported actions.
4. Audit source freshness and reporting windows.
5. Build the measure dictionary.
6. Define trigger origin, owner, and response.
7. List candidate views.
8. Complete the view-purpose audit.
9. Remove redundant views.
10. Build one dominant alert.
11. Add only the evidence needed to interpret it.
12. Add the ordered action path.
13. Produce the exact table and text alternative.
14. Write the decision note.
15. Reproduce and audit the package.

### Stop rules

The build pauses when any of the following is true:

- the audience is named only as leadership or stakeholders;
- the decision is only to monitor performance;
- a measure lacks a unit or reporting window;
- a threshold lacks an owner or origin;
- a view lacks a unique question;
- the stale-data behavior is undefined;
- incompatible units share one numeric scale; or
- the alert has no next action.

## 6. Concept model and vocabulary

### Dashboard

A small set of coordinated views designed for a repeated task and a named decision. A dashboard is defined by use, not by screen shape or software.

### Report

A document or page that communicates findings, often on a scheduled or one-time basis. A report can inform a decision without functioning as a repeated monitoring surface.

### Scorecard

A compact display of performance against declared goals or standards. A scorecard requires legitimate target ownership and should not invent targets from descriptive peer values.

### Analysis page

A workspace for exploring questions, alternatives, or detailed evidence. It may contain more views and controls than a decision dashboard.

### View

One visual, table, text block, or action component that answers a specific question.

### View-purpose audit

A table that records the question, measure, unit, time window, enabled action, and unique role of every retained view.

### Alert

A declared state that requires a named response. An alert needs a measure, condition, threshold origin, owner, action, and review cadence.

### Threshold

A value and operator used to change a state or trigger a response. A threshold may come from regulation, validated evidence, organizational policy, or a fictional course scenario. Its origin must be explicit.

### Benchmark

A formally selected comparison standard. The Massachusetts median in this module is descriptive peer context and is not a benchmark.

### Target

A desired future value adopted by an authorized owner. The module does not define a real hospital target.

### Peer reference

A descriptive value from a comparison group. It provides context without establishing acceptability, statistical difference, or causal meaning.

### Freshness

Whether the data are recent enough for the decision. Freshness depends on the task, reporting window, release date, and refresh expectation.

### Source lag

The number of calendar days between the end of the reporting period and the source release date.

```text
source_lag_days_at_release = cms_release_date - period_end
```

### Stale-data behavior

The visible and operational response when data are older than the declared use allows. In this module, stale public data suppress operational recommendations and redirect the user to current local data.

### Monitoring use

A label stating what kind of decision the data can support. The released rows are labeled `historical_public_reporting_review_only`.

### Exact-value fallback

A table or equivalent that preserves values, units, samples, footnotes, dates, ranks, trigger state, and action outside the graphic.

### Multi-view composition

The arrangement and coordination of several views so their hierarchy, sequence, terminology, and interaction support one task.

### Decorative widget

A display element whose shape, motion, or ornament does not improve the decision. Undefined gauges, rings, and badges are common examples.

## 7. Public sources, rights, and provenance

### Primary CMS dataset

Publisher: Centers for Medicare & Medicaid Services.

Dataset: Timely and Effective Care - Hospital.

Dataset ID: `yv7e-xc69`.

Landing page:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

Complete pinned CSV:

https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv

Hospital data dictionary:

https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf

Measure periods page:

https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods

### Source release fingerprint

| Property | Value |
|---|---|
| CMS release date | 2026-08-13 |
| Complete rows | 138,084 |
| Complete columns | 16 |
| Complete bytes | 34,150,899 |
| SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |

The checksum prevents a silent change in the complete source from changing the teaching case.

### Supporting design guidance

AHRQ dashboard practice page:

https://www.ahrq.gov/evidencenow/tools/dashboard-best-practice.html

AHRQ quality-display guidance:

https://www.ahrq.gov/talkingquality/translate/display/index.html

The module links to and paraphrases these public pages. It does not redistribute the third-party copyrighted PDF linked from the AHRQ dashboard page.

### Rights statement

CMS Provider Data Catalog records are public U.S. government reporting data. The package preserves attribution and does not imply federal endorsement.

Commons documentation is licensed under CC BY 4.0. Commons code is licensed under MIT.

### Data minimization

The complete CMS source includes public street address, ZIP code, and telephone number fields. The teaching release omits them because the dashboard decision does not need them.

Public availability does not remove the responsibility to minimize unnecessary fields.

### Provenance requirements

Every learner package must record:

- publisher;
- dataset title and ID;
- landing-page URL;
- exact file URL;
- release date;
- source checksum;
- selected filters;
- reporting periods;
- transformation code;
- output checksums when required; and
- access or build date.

## 8. Data release and transformation contract

### Source selection

The committed source selection applies:

```text
State == MA
and
Measure ID in {EDV, OP_18b, OP_22}
```

The result contains 186 rows, representing 62 Massachusetts facilities and three required measure rows per facility.

### Released files

| File | Grain | Rows | Columns | SHA-256 |
|---|---|---:|---:|---|
| `cms_ma_ed_dashboard_source_2026.csv` | One hospital-measure-period source row | 186 | 15 | `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b` |
| `ma_ed_public_reporting_dashboard_2026.csv` | One hospital-measure-period teaching row | 186 | 31 | `fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd` |
| `ed_dashboard_measure_dictionary_2026.csv` | One measure definition | 3 | 18 | `2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412` |

### Source fields

The source selection preserves:

- facility ID;
- facility name;
- city;
- state;
- county or parish;
- condition;
- measure ID;
- measure name;
- score;
- sample;
- footnote;
- period start;
- period end;
- CMS release date; and
- source URL.

### Teaching fields

The teaching table adds:

- display label;
- unit;
- direction;
- numeric score;
- value status;
- Massachusetts reported count;
- Massachusetts median;
- Massachusetts minimum;
- Massachusetts maximum;
- unfavorable rank;
- selected-hospital flag;
- scenario threshold;
- threshold operator;
- trigger result;
- trigger origin;
- source lag;
- monitoring-use label;
- action; and
- interpretation boundary.

### Value status

The builder assigns:

- `reported` when a numeric measure score parses successfully;
- `reported_category` when EDV is low, medium, high, or very high; and
- `not_available` when the source value is neither numeric nor a released EDV category.

Unavailable values and footnotes remain in both the source and teaching releases. No unavailable value is imputed.

### Peer calculations

For each numeric measure:

```text
ma_reported_n = count of Massachusetts hospitals with numeric scores
ma_median = ordinary median of numeric hospital scores
ma_min = minimum numeric score
ma_max = maximum numeric score
ma_rank_unfavorable = 1 + count of numeric scores greater than the hospital score
```

Both numeric measures are lower-is-better in the teaching dictionary. Ties receive the same competition rank.

The peer calculations are descriptive. They are not uncertainty-adjusted comparisons, official CMS classifications, or statistical tests.

### Scenario triggers

The mock course charter declares:

```text
OP_18b alert when score >= 240 minutes
OP_22 alert when score >= 10 percent
```

The trigger origin is always labeled `mock QI charter assumption, not a CMS threshold` or an equivalent explicit phrase.

EDV has no performance trigger.

### Source lag classification

The builder calculates source lag for each row.

Rows with source lag greater than 180 days receive the course label `historical_public_reporting_review_only`.

The 180-day rule is a teaching use classification. It is not a CMS timeliness standard.

### Deterministic build

The Python builder uses only the standard library. It sorts output deterministically and writes stable line endings and field order so exact release checksums can be verified.

The default build starts from the committed 186-row selection. The optional `--source-csv` path validates and selects from the complete pinned CMS CSV.

## 9. Worked public-reporting dashboard case

### Selected facility

Facility: Anna Jaques Hospital.

CMS facility ID: `220029`.

Location: Newburyport, Massachusetts.

CMS emergency department volume category: low.

The facility is selected for a clear curriculum case, not for public criticism.

### Measure EDV

Display label: Emergency department volume category.

Role: context only.

Selected value: low.

Reporting period: 2024-01-01 through 2024-12-31.

Source lag at release: 590 days.

Massachusetts categories reported: 53.

Unavailable: 9.

EDV has no performance trigger in the course scenario.

### Measure OP_18b

Display label: Median ED time before departure.

Unit: minutes.

Direction: lower is better.

Source measure name excludes transferred patients and psychiatric or mental-health patients.

Selected value: 188 minutes.

Selected sample: 422.

Reporting period: 2024-10-01 through 2025-09-30.

Source lag at release: 317 days.

Massachusetts numeric values: 54.

Unavailable: 8.

Massachusetts median: 211.5 minutes.

Massachusetts range: 113 to 336 minutes.

Selected unfavorable rank: 45.

Mock trigger: at or above 240 minutes.

Trigger result: not crossed.

### Measure OP_22

Display label: Patients leaving before being seen.

Unit: percent.

Direction: lower is better.

Selected value: 23 percent.

Selected denominator or source sample: 19,211.

Reporting period: 2024-01-01 through 2024-12-31.

Source lag at release: 590 days.

Massachusetts numeric values: 53.

Unavailable: 9.

Massachusetts median: 3 percent.

Massachusetts range: 0 to 23 percent.

Selected unfavorable rank: 1.

Mock trigger: at or above 10 percent.

Trigger result: crossed.

### Interpretation

The public OP-22 value is an exception under the fictional course rule and an observed extreme among reporting Massachusetts hospitals.

The public value is also historical. It cannot establish current operating conditions, cause, or intervention need.

### Supported decision path

1. Open a local definition and data review.
2. Confirm CMS-to-local numerator, denominator, exclusions, and extract completeness.
3. Pull current local monthly OP-22 and emergency department time data.
4. If the signal persists, review system conditions with clinical and operational owners.
5. Record the action, owner, evidence, and next review date.

### Reference answer boundary

The correct answer is not that the facility currently performs poorly.

The correct answer is that the historical public signal is sufficient to begin validation and obtain current local evidence under the mock course charter.

## 10. Dashboard and multi-view selection framework

### Dashboard brief

Before selecting views, learners complete:

| Field | Required statement |
|---|---|
| Decision owner | One named role. |
| Repeated task | What the person does and when. |
| Exact decision | One choice or determination. |
| Supported action | What the evidence may authorize. |
| Unsupported action | What the evidence may not authorize. |
| Refresh cadence | When new data are expected. |
| Stale behavior | What changes when data are too old. |
| Threshold origin | Regulation, evidence, policy, or scenario. |
| Threshold owner | Who can adopt or revise it. |
| Review date | When the decision is revisited. |

### Candidate-view questions

A view is a candidate only if it answers one of these questions:

- What needs attention?
- Is the evidence fresh enough for this action?
- Where is the value among relevant peers?
- Does a related measure show the same pattern?
- What happens next?
- Which exact definition or value must be inspected?

### Released five-view contract

#### View 1: OP-22 alert

Question: What needs attention, and what should happen immediately?

Contents:

- selected OP-22 value;
- percent unit;
- Massachusetts descriptive median;
- mock 10-percent trigger;
- explicit non-CMS label;
- trigger result; and
- immediate validation action.

#### View 2: freshness

Question: Can the public value support a current operational action?

Contents:

- reporting periods;
- CMS release date;
- source lag;
- historical-public-reporting label; and
- current-local-data requirement.

#### View 3: OP-22 peer distribution

Question: Where is the selected public value within numeric values reported by Massachusetts hospitals?

Contents:

- all 53 reported numeric values;
- selected facility;
- 3-percent state median;
- mock 10-percent trigger;
- direct labels; and
- descriptive-comparison warning.

#### View 4: OP-18b peer distribution

Question: Does the second public emergency department measure show the same trigger pattern?

Contents:

- all 54 reported numeric values;
- selected 188-minute value;
- 211.5-minute state median;
- mock 240-minute trigger;
- direct labels; and
- separate minutes scale.

#### View 5: ordered action path

Question: Who does what next?

Contents:

- one named decision owner;
- definition validation;
- current local data pull;
- conditional systems review; and
- documentation and next review.

### Why the units remain separate

OP-22 is a percent. OP_18b is a median number of minutes. They also use different reporting windows.

The views may share typography, annotation style, and spatial rhythm. They must not share one numeric axis or invented common score.

### Why a map is removed

The decision concerns one selected facility and statewide descriptive context. A map would add position without improving the validation decision.

### Why a trend is removed

The released table contains one public reporting value per selected measure, not a monthly time series. Connecting unrelated releases or fabricating intermediate periods would imply unsupported change.

### Why a gauge is removed

A gauge consumes space, often hides the denominator and threshold owner, and makes exact peer context harder to see. A direct value and labeled reference line are more precise.

### Why unrestricted filters are removed

The reference task is fixed to one decision owner, one facility, and three measures. Filters are added only when a named task requires narrowing or comparing the display.

### View cap

Learners use three through five views. Additional analysis belongs in a linked detail report or exact table.

## 11. Teaching sequence and facilitation

### Opening prompt

Ask: What decision becomes easier after looking at this dashboard?

If the answer is only to see the data, the dashboard brief is incomplete.

### Activity 1: classify the product

Show a report, scorecard, exploratory page, and monitoring dashboard. Learners identify the audience, cadence, decision, threshold ownership, and action in each.

### Activity 2: source-window audit

Learners trace EDV, OP_18b, and OP_22 from the source selection into the teaching table. They record units, periods, selected values, sample fields, and lag.

### Activity 3: threshold ownership

Give the mock 10-percent and 240-minute conditions without an origin label. Learners must ask who set them, for what action, with what review cadence, and whether they are CMS rules.

### Activity 4: view-purpose audit

Learners receive ten candidate views. They retain at most five and document why each surviving view is unique.

### Activity 5: reference build

Learners run the lab, inspect the five-view dashboard, and compare the visual values with the exact table.

### Activity 6: critique and repair

Learners repair a KPI wall, a mixed-unit dashboard, and a decorative-widget dashboard.

### Activity 7: independent build

Learners choose Run, Modify, or Author. The competency and grading contract remain identical.

### Activity 8: accessibility audit

Peers inspect reading order, direct labels, status words, non-color cues, exact-value fallback, and text-alternative completeness.

### Activity 9: decision defense

Each learner answers:

- Why is this the dominant alert?
- Why is the evidence historical?
- Why is the trigger not a CMS benchmark?
- What current local data are needed?
- Which view was removed?
- What action is supported now?

### Facilitation principle

Start with the decision contract, then remove views. Do not begin by teaching dashboard software controls.

## 12. Reproducible lab contract

### Inputs

- `data/cms_ma_ed_dashboard_source_2026.csv`.
- `data/ma_ed_public_reporting_dashboard_2026.csv`.
- `data/ed_dashboard_measure_dictionary_2026.csv`.

### Required outputs

- `01-minimum-ed-public-reporting-dashboard.png`.
- `dashboard-decision-table.csv`.
- `alt-text-reference.md`.

### Dashboard output requirements

- Exactly five views.
- One visually dominant OP-22 alert.
- OP-22 shown as 23 percent.
- OP-18b shown as 188 minutes.
- Units shown wherever values appear.
- Mock triggers labeled as non-CMS.
- Massachusetts medians labeled as descriptive.
- Reporting periods and source lag visible.
- OP-22 and OP_18b use separate numeric scales.
- Reported hospital counts visible.
- One named owner.
- Four ordered actions.
- Historical-public-reporting boundary visible.
- No public value labeled current.
- Finding-led title.
- Legible caption and source line.

### Exact table requirements

The table contains exactly three selected-facility rows and includes:

- measure ID;
- display label;
- raw value;
- numeric value where applicable;
- unit;
- sample;
- status;
- footnote;
- start date;
- end date;
- CMS release date;
- source lag;
- peer reported count;
- peer median;
- unfavorable rank;
- scenario threshold;
- trigger result;
- trigger origin;
- monitoring-use label; and
- action.

### Text alternative requirements

The alternative follows the dashboard reading order and preserves all five purposes, selected values, peer references, thresholds, reporting periods, lag, actions, and interpretation boundary.

### Dependencies

- Python 3 standard library for build and validation.
- R 4.6.1 tested.
- ggplot2 4.0.3 tested.
- Base R grid for dashboard composition.
- No dashboard-specific package.

### Build and validate commands

```powershell
python courses/data-visualization/modules/12-dashboards-multi-view-composition/build_ed_dashboard_case.py
python courses/data-visualization/modules/12-dashboards-multi-view-composition/validate_ed_dashboard_case.py
```

Expected validation result:

```text
Module 12 ED dashboard data passed 179 checks.
```

### Reference lab command

```powershell
Rscript courses/data-visualization/modules/12-dashboards-multi-view-composition/lab.R --output "$env:TEMP\oclc-da730-m12-lab"
```

### Critique lab command

```powershell
Rscript courses/data-visualization/modules/12-dashboards-multi-view-composition/critique_charts.R --output "$env:TEMP\oclc-da730-m12-critiques"
```

### Complete-source refresh command

```powershell
Invoke-WebRequest -Uri "https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv" -OutFile "$env:TEMP\Timely_and_Effective_Care-Hospital.csv" -UseBasicParsing
python courses/data-visualization/modules/12-dashboards-multi-view-composition/build_ed_dashboard_case.py --source-csv "$env:TEMP\Timely_and_Effective_Care-Hospital.csv"
```

The builder rejects a complete source whose pinned fingerprint does not match.

## 13. Critique and repair set

### C1: wall of KPIs

The flawed display presents 18 equally weighted values without a dominant exception, decision owner, threshold origin, or next action.

Learners must:

- name the audience and repeated task;
- identify one alert;
- retain no more than four supporting views;
- state threshold ownership;
- connect the alert to an action;
- move secondary values to a detail table; and
- explain every deleted view.

### C2: hidden windows and units

The flawed display converts percent, minutes, and another percent into an invented common index. It calls the values current and hides the different reporting windows.

Learners must:

- restore the original units;
- restore reporting periods;
- remove the common numeric scale;
- show source lag;
- state the monitoring-use boundary;
- decide whether the measures belong together; and
- avoid interpreting the normalized values as comparable performance.

### C3: decorative widgets

The flawed display uses radial shapes and undefined composite percentages. It omits denominators, threshold owners, reporting windows, and actions.

Learners must:

- replace composites with source measures or remove them;
- use direct values;
- name the denominator or sample meaning;
- state threshold origin;
- add the owner and action path;
- provide an exact table; and
- justify any remaining decoration by task value.

### Critique pass standard

A repair must correct the decision and measure contract. Changing colors, fonts, or chart software without repairing the contract does not pass.

### Critique outputs

- `C1-wall-of-kpis.png`.
- `C2-hidden-windows-and-units.png`.
- `C3-decorative-widgets.png`.

## 14. Assessment and checkpoint contribution

### Submission package

```text
module-12/
  dashboard-brief.md
  analysis.R
  dashboard.png
  dashboard-decision-table.csv
  measure-dictionary.csv
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

### Dashboard brief requirements

The brief defines:

- decision owner;
- audience task;
- exact decision;
- supported action;
- unsupported actions;
- refresh cadence;
- stale-data behavior;
- measures considered;
- views retained;
- views rejected;
- threshold owner;
- alert action; and
- review date.

### View-purpose audit requirements

For each retained view, learners record:

| View | Question answered | Measure | Unit | Window | Action enabled | Unique role |
|---|---|---|---|---|---|---|

Use three through five views. Delete any view without a unique task.

### Decision note

The 300-to-450-word decision note answers:

1. What is the one alert?
2. What evidence supports opening a review?
3. Why is the evidence not current operational performance?
4. Which definition and source checks come first?
5. What current local data are needed?
6. What action follows if the current local signal persists?
7. Which dashboard view was removed and why?

### Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Audience, decision, and owner | 10 | One person, one task, one decision, and one action boundary. |
| View-purpose discipline | 15 | Three through five necessary views and documented rejections. |
| Measure definitions | 15 | Units, populations, samples, windows, directions, and limits. |
| Threshold and action contract | 15 | Origin, owner, result, response, and no CMS-threshold claim. |
| Time and freshness | 10 | Different periods and lag visible; stale behavior defined. |
| Visual hierarchy and comparison | 10 | One dominant alert and legible separate-unit peer views. |
| Reproducibility and exact table | 10 | Editable source regenerates the dashboard and exact output. |
| Accessibility | 10 | Direct labels, non-color cues, exact table, and complete text alternative. |
| Provenance and AI record | 5 | Complete source and AI-use records. |
| Total | 100 |  |

### Pass conditions

All conditions are required:

- at least 80 of 100 points;
- three through five views;
- one named owner;
- exact measure dictionary;
- visible reporting windows;
- no mixed-unit scale;
- mock triggers labeled as non-CMS;
- stale-data behavior;
- current-local-data requirement;
- reproducible source;
- exact table; and
- accessible alternative.

### Automatic return conditions

Return the package without grading when:

- the public score is labeled current;
- a scenario trigger is called a CMS benchmark;
- OP_18b minutes and OP_22 percent share one numeric scale;
- unavailable values are silently imputed;
- a view has no decision purpose;
- no owner or action is named;
- the dashboard recommends an operational intervention from the public data alone;
- a source URL, period, or checksum is missing;
- the dashboard cannot be regenerated; or
- the accessible alternative omits the alert or action.

### Week-6 checkpoint contribution

Module 12 closes the applied visualization sequence and contributes the decision dashboard, exact table, measure dictionary, source record, view-purpose audit, accessible alternative, and decision brief to Checkpoint 2.

Checkpoint 2 should assess a coherent evidence package from Modules 07 through 12 rather than six disconnected assignments.

## 15. Accessibility and equivalent communication

### Visual hierarchy

One alert is visually and verbally dominant. Supporting views use lower emphasis but remain readable.

### Status communication

Status appears in words such as `trigger crossed`, `trigger not crossed`, and `historical public reporting`.

Color may reinforce status. Color cannot carry status alone.

### Direct labels

Selected values, medians, mock triggers, units, and reported counts are labeled directly. Essential information does not require hover.

### Reading order

The dashboard reading order is:

1. alert;
2. freshness;
3. OP-22 peer context;
4. OP-18b peer context; and
5. action sequence.

The text alternative uses the same order.

### Contrast and non-color cues

- Text meets course contrast standards.
- Selected values use shape, position, text, or line weight in addition to color.
- Reference lines use different line patterns and direct labels.
- Alert words remain visible in grayscale.
- Small text is not used for essential definitions.

### Exact-value fallback

Every dashboard submission includes a three-row exact decision table and three-row measure dictionary.

### Text alternative requirements

The alternative states:

- audience and decision;
- all view purposes;
- selected values and units;
- peer medians and reported counts;
- mock trigger values and results;
- reporting periods and lag;
- ordered actions;
- threshold ownership boundary; and
- public-reporting interpretation limit.

### Cognitive accessibility

Use stable names for the same concepts. Do not alternate among target, benchmark, threshold, goal, and average as if they are interchangeable.

Use short action verbs and visible sequence numbers.

### Motion and interaction

The reference dashboard is static. A learner-built interactive version must preserve keyboard access, visible focus, non-hover access to essential values, predictable controls, and an equivalent static export.

## 16. Ethics, equity, privacy, and language

### Public data still require careful interpretation

The data identify public facilities but contain no patient-level records. Public aggregate status does not authorize blame, causal attribution, or a current performance judgment.

### Non-stigmatizing language

Prefer:

- patients leaving before being seen;
- historical public reporting value;
- selected for definition and current-data review;
- observed peer position;
- current local signal; and
- system conditions requiring review.

Avoid:

- bad hospital;
- failing hospital;
- noncompliant patients;
- poor patients;
- current crisis;
- proven staffing problem; and
- CMS failure threshold.

### System-focused review

If a current local signal persists, a real review should consider:

- arrival patterns;
- triage processes;
- wait communication;
- language access;
- disability access;
- staffing;
- physical and inpatient capacity;
- registration and discharge processes;
- outside events; and
- data capture completeness.

The public value alone cannot identify which condition matters.

### Equity boundary

The released public facility-level rows do not support patient subgroup analysis. Learners must not imply that the aggregate value applies equally to every racial, ethnic, language, disability, age, payer, or clinical group.

### Threshold governance

A real threshold requires authorized ownership, review cadence, evidence, exception handling, action capacity, and monitoring for unintended effects.

The fictional course trigger cannot be transferred into real practice without that governance.

### Data minimization

Street address, ZIP code, and telephone number are omitted from the teaching data because they do not support the decision.

### Real-data transfer

A production dashboard would require governance, role-based access, privacy and security review, validated definitions, source monitoring, current local data, clinical and operational approval, and a documented escalation process.

## 17. AI-use contract

### Permitted uses

Learners may use AI to:

- explain dashboard code;
- suggest a simpler layout;
- identify possible redundant views;
- help debug a join or date calculation;
- draft alt text for learner verification;
- draft a measure-dictionary template;
- improve prose clarity; and
- identify possible mixed-unit or threshold-language errors.

### Prohibited substitution

AI output cannot replace:

- source verification;
- checksum verification;
- measure-definition review;
- sample or denominator interpretation;
- reporting-window audit;
- source-lag calculation;
- threshold ownership;
- exact-value verification;
- clinical or operational interpretation;
- accessibility review; or
- learner defense.

### Required record

The learner records:

- tool and model when known;
- date;
- prompt or task;
- generated code or prose;
- output accepted;
- material revisions;
- values checked;
- definitions checked; and
- final responsibility statement.

### Required verification

Every number in AI-assisted prose or code must be compared with the exact decision table.

Every measure statement must be compared with the measure dictionary and source record.

### Verification questions

- Did the AI call a public value current?
- Did it invent a denominator definition?
- Did it call a peer median a benchmark?
- Did it call the mock trigger a CMS rule?
- Did it combine minutes and percent?
- Did it drop unavailable hospitals?
- Did it recommend an intervention before current local data?
- Did it add decorative views without a task?
- Did it remove the text alternative or exact table?
- Did it fabricate a real-time refresh claim?

## 18. Instructor implementation and answers

### Instructor preparation

1. Run the Python builder.
2. Run the 179-check validator.
3. Run the reference lab.
4. Run the critique lab.
5. Inspect the dashboard and all three critique figures.
6. Confirm the three-row decision table.
7. Confirm the three-row measure dictionary.
8. Trace one row per measure to the committed source selection.
9. Review the source record and interpretation boundary.
10. Prepare one example of a legitimate local threshold and owner.

### Eight-and-a-half-hour teaching plan

| Time | Activity |
|---|---|
| 0:00-0:35 | Audience, decision, owner, and action boundary. |
| 0:35-1:15 | Dashboard, report, scorecard, and analysis page. |
| 1:15-2:00 | Measure dictionary and source-window audit. |
| 2:00-2:40 | Threshold ownership, alert states, and stale-data behavior. |
| 2:40-3:25 | Trace CMS source, teaching table, and selected facility. |
| 3:25-4:20 | Run and inspect the five-view reference dashboard. |
| 4:20-5:10 | Critique C1 through C3. |
| 5:10-7:05 | Independent or scaffolded build. |
| 7:05-7:50 | Exact table, text alternative, and decision note. |
| 7:50-8:30 | Peer view-purpose audit and Checkpoint 2 handoff. |

### Measured answer key

| Question | Answer |
|---|---:|
| Complete CMS rows | 138,084 |
| Massachusetts selected rows | 186 |
| Massachusetts facilities | 62 |
| Measures per facility | 3 |
| EDV reported categories | 53 |
| EDV unavailable | 9 |
| OP_18b reported hospitals | 54 |
| OP_18b unavailable | 8 |
| OP_18b Massachusetts median | 211.5 minutes |
| OP_18b Massachusetts range | 113 to 336 minutes |
| Selected OP_18b | 188 minutes |
| Selected OP_18b sample | 422 |
| Selected OP_18b unfavorable rank | 45 |
| OP_18b mock trigger | 240 minutes, not crossed |
| OP_22 reported hospitals | 53 |
| OP_22 unavailable | 9 |
| OP_22 Massachusetts median | 3 percent |
| OP_22 Massachusetts range | 0 to 23 percent |
| Selected OP_22 | 23 percent |
| Selected OP_22 source sample | 19,211 |
| Selected OP_22 unfavorable rank | 1 |
| OP_22 mock trigger | 10 percent, crossed |
| OP_18b lag at release | 317 days |
| OP_22 lag at release | 590 days |

### Core answer

The reference dashboard supports opening a local definition and current-data review for OP-22.

The 23-percent public value crosses the mock 10-percent trigger and is the highest observed value among reporting Massachusetts hospitals. The reporting period ended 590 days before release, so the dashboard does not support a current operational judgment.

### Why OP_18b remains visible

OP_18b provides related emergency department context without showing the same alert pattern. The selected 188-minute value is below the descriptive state median and below the mock trigger.

It remains separate because its unit and reporting window differ from OP-22.

### Common recovery moves

If the dashboard has too many views, return to the view-purpose audit. If units are mixed, restore one scale per unit. If a trigger appears official, restore the origin and owner. If the public value is labeled current, add the period and lag, then narrow the supported action. If the action jumps to intervention, insert definition validation and current local data first.

### Independent instructor test

An instructor unfamiliar with the build should be able to regenerate all outputs from a clean checkout, trace every reference number, explain the alert boundary, and teach the module without undocumented conversation context.

## 19. Technical validation and acceptance tests

### Data checks

The validator passes 179 checks covering:

- required files;
- exact row counts;
- exact column counts;
- exact SHA-256 values;
- facility and measure keys;
- 62-facility coverage;
- three selected rows per facility;
- allowed measure IDs;
- source field preservation;
- address-field omission;
- value-status rules;
- unavailable-value preservation;
- footnote preservation;
- reporting periods;
- release date;
- source URL;
- numeric parsing;
- reported counts;
- medians;
- ranges;
- unfavorable ranks;
- selected-facility facts;
- threshold values;
- threshold operators;
- trigger results;
- trigger origins;
- source-lag calculations;
- monitoring-use labels;
- actions;
- interpretation boundaries;
- measure-dictionary definitions;
- owner and cadence fields; and
- release metadata.

### Lab checks

- One PNG dashboard exists and is nonempty.
- The dashboard contains exactly five views.
- One CSV decision table exists and has exactly three rows.
- One Markdown text alternative exists and is nonempty.
- R exits successfully using ggplot2 and base grid.
- No dashboard package is required.

### Critique checks

- Three PNG critique files exist and are nonempty.
- Each flaw is deliberate and documented.
- Each critique supports a contract-level repair.

### Visual inspection

Review:

- alert dominance;
- five-view reading order;
- selected values;
- unit labels;
- reporting periods;
- source lag;
- mock-trigger labels;
- peer-median labels;
- separate numeric scales;
- reported counts;
- action sequence;
- line and label clipping;
- contrast;
- footnote legibility;
- source line; and
- critique readability.

### Repository checks

- Release JSON parses.
- JavaScript syntax passes.
- Curriculum checker passes.
- `git diff --check` passes.
- No local absolute path appears in public documentation.
- No Unicode em dash or en dash appears in the module contract.
- No drafting marker remains.
- No temporary output or bytecode directory is committed.

### Acceptance facts

- Facilities: 62.
- Measures: 3.
- Selected rows: 186.
- OP-22 selected value: 23 percent.
- OP-18b selected value: 188 minutes.
- Longest source lag: 590 days.
- Dashboard views: 5.
- Validator result: 179 of 179 checks pass.

## 20. Release, review, and change control

### Release status

Version 0.1.0 is a runnable release candidate in Commons 0.23.0.

### Completed review

Technical build, validator execution, lab execution, critique execution, and visual inspection are complete.

### Required human roles

- emergency department quality relevance;
- CMS measure and source fidelity;
- dashboard and information design;
- equity and action language;
- accessibility; and
- independent teachability.

### Alpha gate

The module cannot become alpha until named reviewers record decisions and material findings are resolved.

### Version policy

- Patch: wording, typo, or noncontractual correction.
- Minor: source refresh, assessment change, output change, or competency-compatible expansion.
- Major: incompatible decision, source, learning outcome, measure set, or submission contract.

### Source refresh

A source refresh requires:

- a new complete-source fingerprint;
- new selected-file checksums;
- row and column counts;
- measure periods;
- selected-facility facts;
- missingness counts;
- peer summaries;
- trigger results;
- source-lag calculations;
- validator expectations;
- regenerated dashboard and critiques;
- visual inspection;
- module version;
- Commons version;
- source-register update; and
- human review of material changes.

### Known limits

- Historical public aggregate data only.
- Different measure windows.
- No real-time operational feed.
- No risk adjustment.
- No uncertainty-adjusted facility comparison.
- Descriptive peer medians only.
- Fictional course triggers.
- No subgroup analysis.
- No causal conclusion.
- No intervention-effect conclusion.
- Human review remains pending.
- Clean-run testing is currently Windows only.

## 21. Checkpoint 2 and Module 13 handoff

### Checkpoint 2 purpose

Checkpoint 2 occurs at the end of week 6. It demonstrates that the learner can turn sourced clinical data into a coordinated, accessible, decision-limited visual evidence package.

### Evidence selected from Modules 07 through 12

The checkpoint package includes:

- one accessible figure using color and non-color cues;
- one temporal or process-variation figure;
- one aligned multi-group comparison;
- one place, flow, composition, or structural view;
- the Module 12 decision dashboard;
- exact tables;
- measure or structure definitions;
- source records and checksums;
- a view-purpose audit;
- one critique repair;
- accessible text alternatives;
- a decision brief; and
- an AI-use record.

### Integration requirements

The package must use consistent:

- audience language;
- measure names;
- units;
- denominators;
- time windows;
- source citations;
- threshold labels;
- accessibility conventions;
- interpretation boundaries; and
- action language.

Checkpoint 2 is not a folder dump. The learner selects and connects evidence to one decision.

### Module 13 handoff

Module 12 hands Module 13:

- one named decision owner;
- one stable decision;
- one dominant finding;
- a reproducible evidence package;
- exact values and definitions;
- source and rights records;
- declared uncertainty and freshness limits;
- accessible figures and text alternatives;
- an ordered action path; and
- a documented AI-use record.

Module 13 reshapes one analysis for two audiences. The measure definitions, data values, source, uncertainty, and action boundary must remain stable even when title, annotation, sequence, explanatory depth, and format change.

### Module 13 questions

- What does the decision owner need first?
- What does a second audience need explained?
- Which evidence remains in both versions?
- Which detail moves to notes or appendix?
- Which title states the finding without overclaiming?
- Which annotation changes the decision?
- What action is requested?
- What should the audience not conclude?

### Final boundary

Module 12 ends when the dashboard is minimal, reproducible, accessible, definition-complete, freshness-aware, and tied to a defensible action. Module 13 begins when the stable evidence must become a concise decision story for different audiences.

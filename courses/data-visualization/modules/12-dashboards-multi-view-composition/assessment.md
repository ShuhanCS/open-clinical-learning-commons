# Module 12 assessment

## Decision task

You are the emergency department quality director for the course scenario. Build the minimum public-reporting review dashboard needed to decide whether a released CMS value should trigger a local definition and current-data review.

Your dashboard must not present the public data as current operations. It must distinguish different units and reporting windows, preserve exact definitions and samples, and connect every alert to an owner and action.

## Required package

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

## Required work

### 1. Dashboard brief

Define:

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

### 2. View-purpose audit

For every retained view, complete:

| View | Question answered | Measure | Unit | Window | Action enabled | Why another view cannot answer it |
|---|---|---|---|---|---|---|

Use three through five views. Delete any view without a named task or action.

### 3. Dashboard

The dashboard must include:

- one alert hierarchy;
- one freshness or reporting-window view;
- one OP-22 peer view;
- one OP-18b peer view or a justified alternative;
- one ordered action view;
- direct values and units;
- reported hospital counts;
- mock-trigger labels;
- a statement that triggers are not CMS benchmarks;
- a statement that public aggregate reporting is historical; and
- a finding-led title.

Do not combine percent and minutes on one numeric scale.

### 4. Exact decision table

Include all three selected hospital rows with:

- measure ID and label;
- raw value;
- unit;
- sample;
- status and footnote;
- start and end date;
- CMS release date;
- lag at release;
- peer reported count and median;
- unfavorable rank;
- scenario trigger;
- trigger result;
- trigger origin;
- monitoring-use label; and
- action.

### 5. Measure dictionary

For EDV, OP_18b, and OP_22, define:

- source name;
- display name;
- unit;
- direction;
- grain;
- numerator or summary;
- denominator or included population;
- sample meaning;
- reporting period;
- release date;
- scenario trigger;
- trigger owner;
- action;
- refresh cadence;
- decision owner;
- interpretation limit; and
- source URL.

### 6. Decision note

Write 300 to 450 words that answers:

1. What is the one alert?
2. What evidence supports opening a review?
3. Why is the evidence not current operational performance?
4. Which definition and source checks come first?
5. What current local data are needed?
6. What action follows if the current local signal persists?
7. Which dashboard view was removed and why?

### 7. Accessible alternative

The text alternative must state:

- audience and decision;
- all five view purposes;
- selected values and units;
- peer medians and reported counts;
- mock trigger values and results;
- reporting windows and lag;
- ordered actions;
- threshold boundary; and
- interpretation limit.

### 8. AI-use record

Document prompts, generated code or prose, accepted output, changes, and checks. State how you verified every number against the exact table and every definition against the measure dictionary.

## Scaffold options

### Run

Run the reference lab, verify the five-view audit, and rewrite the decision note for the named audience.

### Modify

Run the reference lab, remove or replace one view, and show that the remaining dashboard still answers the decision. You may replace a peer plot with an exact table or bullet display.

### Author

Build the dashboard from the released teaching table using R, Python, Tableau, Power BI, or another approved editable tool.

The competency and grading standard remain the same.

## Critique repairs

### C1: wall of KPIs

Reduce 18 equally weighted values to one named alert and no more than four supporting views. State the owner and action.

### C2: hidden windows and units

Restore each original unit and reporting window. Remove the invented common scale. Decide whether the measures belong on one dashboard.

### C3: decorative widgets

Replace the undefined radial widgets with direct values, denominators, threshold ownership, and an action sequence, or remove them.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Audience, decision, and owner | 10 | One person, one task, one decision, one action boundary. |
| View-purpose discipline | 15 | Three through five necessary views; rejected views documented. |
| Measure definitions | 15 | Complete units, populations, samples, windows, directions, and limits. |
| Threshold and action contract | 15 | Scenario origin, owner, trigger result, ordered response, and no CMS-threshold claim. |
| Time and freshness | 10 | Different periods and lags visible; stale-state behavior defined. |
| Visual hierarchy and comparison | 10 | One alert dominates; peer references and separate units are legible. |
| Reproducibility and exact table | 10 | Editable source rebuilds the dashboard and exact output. |
| Accessibility | 10 | Direct labels, non-color cues, readable hierarchy, exact table, and text alternative. |
| Provenance and AI record | 5 | Complete source and AI-use records. |
| Total | 100 |  |

## Pass conditions

All are required:

- score at least 80;
- three through five views;
- one named owner;
- exact measure dictionary;
- reporting windows visible;
- no mixed-unit scale;
- mock triggers labeled as non-CMS;
- stale-data behavior;
- current-local-data requirement;
- reproducible source;
- exact table; and
- accessible alternative.

## Automatic return conditions

Return without grading if:

- the public score is labeled current;
- a scenario trigger is called a CMS benchmark;
- OP_18b minutes and OP_22 percent share one scale;
- unavailable values are silently imputed;
- a view has no decision purpose;
- no owner or action is named;
- the dashboard recommends an operational intervention from public aggregate data alone;
- a source URL, period, or checksum is missing;
- the dashboard cannot be regenerated; or
- the accessible alternative omits the alert or action.

## Reference answer boundary

The supported decision is to open a local definition and current-data review for OP-22. The public 23-percent value crosses the mock 10-percent trigger, but the period ended 590 days before release. The first action is validation and current local data, not a staffing or clinical judgment.

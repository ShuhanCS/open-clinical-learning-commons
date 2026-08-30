# Module 03 instructor notes and answer key

## Teaching purpose

This module turns Module 01's mappings and Module 02's perception evidence into a decision process. The goal is not memorizing a chart taxonomy. The goal is a defensible chain from decision to reader task to evidence structure to display and failure test.

Reward a correct table or no-display decision as strongly as a well-built chart.

## Verified setup

```powershell
Rscript build_selection_cases.R
Rscript validate_selection_cases.R
Rscript lab.R
Rscript critique_charts.R
```

Reference environment:

- R 4.6.1
- ggplot2 4.0.3
- Windows

Expected results:

- 13 of 13 checks pass;
- 10 selection cases are recreated;
- two HCAHPS figures render;
- one exact-value table and two matrices are written; and
- one flawed four-panel dashboard renders.

## Eight-hour teaching sequence

| Segment | Time | Instructor action | Learner evidence |
|---|---:|---|---|
| Executive decision opening | 30 min | Present one HCAHPS table and ask three different reader questions. | Three different task statements |
| DECIDE concept core | 45 min | Walk through decision, evidence, comparison, information, display, and evaluation. | Completed worked matrix row |
| Cases C01 to C03 | 75 min | Compare the chart, relationship view, and table using one source. | Three matrix decisions |
| Cases C04 to C10 | 90 min | Run rapid question-to-display rounds, including the no-display case. | Ten-case draft matrix |
| Runnable lab | 60 min | Build the two charts and exact table. | Verified outputs |
| Dashboard critique | 45 min | Diagnose one form forced onto four questions. | Repair plan |
| Independent assessment | 105 min | Coach task and failure reasoning, not aesthetic preference. | Six-part package |
| Peer run and revision | 30 min | Test code, table, alternatives, and no-display gate. | Corrected package |
| **Total** | **480 min** | | **8 hours** |

## Reference choices

| Case | Choice | Why | Required companion |
|---|---|---|---|
| C01 | Aligned dot plot | Supports order and close comparison. | Table with response rate and survey count. |
| C02 | Table | Exact lookup is the task. | Definition and missing-value note. |
| C03 | Scatterplot | Two quantitative positions reveal paired combinations. | Plotted-value table and survey count. |
| C04 | Distribution view with subgroup comparison | The decision depends on tails and hidden processes. | n, median, upper quantile, and subgroup counts. |
| C05 | Line or run chart with process context | Ordered periods are central. | Measure-definition and period note. |
| C06 | Ordered composition view | Parts contribute to one total. | Counts, denominator, and suppressed values. |
| C07 | Flow view | Defined transitions are the question. | Transition table and cohort definition. |
| C08 | Map plus aligned comparison | Place informs action, while the table preserves precise comparison. | Estimate, denominator, uncertainty, and workforce table. |
| C09 | Coordinated comparison and table | Overview and exact lookup are both necessary. | Accessible exact-value table and source status. |
| C10 | No display | The evidence cannot support the requested claim. | Written evidence-gap and data-request note. |

Alternative choices can earn full credit when they fit the same task, evidence, precision, context, and failure gate.

## Worked HCAHPS answers

### C01 comparison

The aligned dot plot is primary because the executive task is to order results and see close gaps. Direct values assist lookup. Response rate and completed surveys stay in the companion table because forcing all three measures into marks would add a second comparison task.

### C02 lookup

The CSV table is the display. A bar chart adds estimation and scanning without helping retrieve three exact fields for named hospitals. Plain-language measure, release, period, and unavailable-value notes remain necessary.

### C03 relationship

The scatterplot maps response rate and recommendation percentage to paired position. Completed surveys may use area as secondary context because the primary relationship remains on position. The committee may identify unusual combinations for follow-up. It cannot infer that response rate causes recommendation results.

## Dashboard critique answer key

The flawed dashboard:

- repeats horizontal bars regardless of reader task;
- normalizes incompatible percentages and counts onto one unlabeled conceptual scale;
- replaces exact lookup with visual estimation;
- encodes a relationship as the average of recommendation percent and response rate, a fabricated measure with no decision meaning;
- hides the actual survey-count unit; and
- uses multiple panels without preserving source definitions or exact values.

Smallest repair:

1. keep the comparison dot plot;
2. use a table for exact response-rate lookup;
3. use a scatterplot for the relationship;
4. show survey count in the companion table or as clearly labeled secondary area; and
5. remove any panel without a named action.

## Common errors and interventions

| Error | What it reveals | Intervention |
|---|---|---|
| Learner begins with a favorite chart | Tool vocabulary precedes the decision. | Hide chart names and ask for owner, choice, and task first. |
| One numeric field becomes a bar chart automatically | Data type is mistaken for sufficient design logic. | Change the task from compare to lookup and revisit. |
| Every case has two views | Multiple views are treated as sophistication. | Require each view to answer a different necessary question. |
| Table is called a fallback | Exact lookup is undervalued. | Time one exact retrieval from a chart and from the table. |
| No-display case receives a disclaimer and chart anyway | Disclosure is mistaken for evidence. | Ask what value the mark would truthfully represent. |
| Map selected because geography exists | Location field is mistaken for a place-based decision. | Name the geographic action and denominator first. |
| Relationship plot receives a causal title | Association and cause are conflated. | Rewrite the title as a paired descriptive question. |
| Dashboard repeats one template | Consistency is confused with task fit. | List the reader task above every panel. |
| AI fills a missing context field | Plausibility replaces provenance. | Trace context to source or mark it unresolved. |

## Strong decision-note pattern

> The executive team must order current recommendation results and identify two hospitals for deeper review. I recommend an aligned dot plot with direct percentages, paired with an exact table containing response rate and completed surveys. Position supports the comparison task, while the table preserves lookup and context. I rejected a multi-metric bubble chart because it would make survey volume visually prominent without answering the primary question. Publication stops if the hospital set, measurement period, or measure definition is inconsistent. The display describes the CMS release; it does not establish fair ranking, statistical difference, cause, or overall hospital quality.

## Grading guidance

For the 25 matrix points:

- 5 points: decision owners and choices;
- 5 points: reader tasks and data shape;
- 5 points: precision and context;
- 5 points: candidates, companions, and rejected alternatives; and
- 5 points: no-display triggers and final choices.

For the 20 display-fit points:

- 8 points: comparison display;
- 6 points: relationship display;
- 6 points: exact lookup table.

## Accessibility check

- Figures remain readable in grayscale and at ordinary document size.
- Direct labels or CSV preserve exact values.
- The scatterplot's size encoding has a text legend and is not essential to the primary relationship.
- Alt text is separate for both figures.
- The table has meaningful column headers and no merged visual cells.
- The no-display result is a readable evidence-gap note.

## If time is short

Keep C01, C02, C03, C04, C08, C09, and C10. Assign the other three cases as post-class matrix work. Keep both builds, the table defense, and no-display gate.

## Human review still required

Before alpha release, record visualization-faculty, hospital-executive or clinical, accessibility, and independent-instructor reviews.

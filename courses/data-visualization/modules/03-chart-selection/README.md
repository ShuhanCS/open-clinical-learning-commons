# Module 03: Chart selection in practice

- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module ID: `oclc-da730-03`
- Learner time: 8 hours
- Prerequisites: Modules 01 and 02
- Release status: runnable release candidate
- Module version: 0.1.0

## The decision

A hospital executive team wants to review patient experience, response rate, and survey volume. One display cannot answer every question equally well.

Your job is to choose the smallest useful display for each decision. A defensible answer may be a chart, a table, two coordinated views, or no display until better evidence exists.

## Competency

Select and justify a chart, table, coordinated pair of views, or decision not to visualize based on the question, data structure, audience, and required precision.

By the end of the module, you can:

1. start with the decision and reader task rather than a chart menu;
2. connect comparison, lookup, distribution, time, relationship, composition, flow, geography, and monitoring tasks to data requirements;
3. identify context that must travel with the display;
4. compare plausible candidates and reject one for a concrete reason;
5. state a no-display trigger before seeing a polished chart; and
6. build a reproducible primary view with the necessary companion table or note.

## The DECIDE selection method

### D: Decision and owner

Name who will act and what choice the evidence informs. “Explore the data” is an analytic activity, not yet a decision.

### E: Evidence grain and shape

State what one row represents and what structure the data actually contain:

- one value across groups;
- repeated values over time;
- individual-level distribution;
- two quantitative variables;
- parts within one total;
- transitions among states;
- values tied to geography; or
- exact fields for lookup.

A chart cannot recover a distribution from one aggregate mean or a trend from one reporting period.

### C: Comparison and reader task

Name what the reader must do:

- detect;
- identify;
- order;
- estimate;
- compare;
- look up;
- follow a path; or
- locate a place.

Use Module 02's perception evidence to judge the candidate encoding.

### I: Information precision and context

Ask how exact the answer must be and what must travel with it. Healthcare displays often need denominators, sample size, uncertainty, missingness, period, measure definition, adjustment status, and source release.

### D: Display candidates and companions

Propose at least two candidates. Choose the smallest form that carries the answer. Name any required companion:

- a table for exact lookup;
- a source and definition note;
- a denominator or uncertainty column;
- a second view that answers a genuinely different question; or
- a text explanation when a chart would imply more evidence than exists.

### E: Evaluate failure and the no-display gate

Before finalizing, ask:

- What plausible claim could this display invite that the data do not support?
- Which patient group, tail, denominator, period, or missing value could it hide?
- Does a simpler table answer the task better?
- Do incompatible definitions or missing evidence require a pause?

Choosing no display is correct when the available evidence cannot answer the question.

## Display families are candidates, not answers

| Reader question | Useful starting candidates | Evidence required | Common failure |
|---|---|---|---|
| How do named groups compare? | Dot plot, common-baseline bar, table | Comparable measure and period | Treating visible rank as fair or statistically distinct |
| What is the exact value? | Table, direct label | Exact value and definition | Making the reader estimate from a decorative chart |
| What does the distribution look like? | Histogram, density, box plot, empirical cumulative distribution | Individual or suitable grouped values | Plotting only an average |
| How does it change over time? | Line, run, or control chart | Repeated consistent periods | Connecting incomparable releases |
| Are two measures related? | Scatterplot | Paired values at the same grain | Implying causation or hiding missing pairs |
| How do parts form a total? | Ordered bars, stacked bars, composition table | One defensible denominator and nonoverlapping parts | Using categories that do not share a total |
| Where do people or events move? | Flow view plus transition table | Defined cohort, states, and transitions | Double-counting repeated events |
| Where is the pattern? | Map plus ranked comparison | Stable geography, denominator, and estimate | Mapping raw counts as if they were rates |
| What must we monitor? | Minimum coordinated views plus exact table | Stable refresh, targets or references, and action rules | Filling a dashboard with unrelated chart types or one repeated template |

The final selection still depends on audience, precision, access, and decision consequences.

## The 10 cases

The case release covers:

1. hospital comparison;
2. exact lookup;
3. a relationship question;
4. a distribution question;
5. a time question;
6. composition;
7. flow;
8. geography;
9. monitoring with coordinated views; and
10. a no-display evidence gap.

Each case names the decision owner, decision, reader task, data shape, precision need, required context, source, reference choice, companion, and no-display trigger.

## Run the package

From this module directory:

```powershell
Rscript build_selection_cases.R
Rscript validate_selection_cases.R
Rscript lab.R
Rscript critique_charts.R
```

The lab creates:

- `outputs/lab/01-comparison-dot-plot.png`
- `outputs/lab/02-response-relationship.png`
- `outputs/lab/03-exact-lookup-table.csv`
- `outputs/lab/selection-matrix-reference.csv`
- `outputs/lab/selection-matrix-template.csv`

The critique script creates:

- `outputs/critique/01-one-form-for-every-question.png`

## Three scaffold tiers

### Tier 1: Apply the matrix

Complete all 10 cases using the learner template. For each case, choose a candidate, required companion, rejected alternative, failure test, final choice, and justification.

### Tier 2: Modify the question

Change one element of three cases:

- reader task;
- number of groups;
- precision need;
- data grain;
- available context; or
- audience.

Record whether the display choice changes and why.

### Tier 3: Build and defend

Build the HCAHPS comparison and relationship cases, then justify why the exact lookup case should remain a table. Submit the exact package in `assessment.md`.

## Required decision rules

- A chart family is never justified by data type alone.
- A table is a complete answer when exact lookup is the task.
- Multiple views are justified only when they answer different necessary questions.
- A dashboard is not a reason to repeat the same chart form.
- A map is justified by a place-based decision, not by the presence of a ZIP code.
- A no-display decision must name the missing evidence and the next data request.

## Accessibility

The selected display must remain interpretable without color, use readable labels, show source and period, and include a text alternative. A companion table should be accessible as text or CSV, not only as a screenshot. No-display decisions need a plain-language evidence-gap note.

## AI use

AI may propose candidates or critique a selection matrix. You must verify the data grain, source, measure, reader task, and failure test. Record the tool, purpose, adopted change, and verification in `decision-note.md`. AI cannot invent context or turn a missing-evidence case into a confident chart.

## Sources

Primary HCAHPS source:

https://data.cms.gov/provider-data/dataset/dgck-syfz

AHRQ guidance on displaying healthcare quality information:

https://www.ahrq.gov/talkingquality/translate/display/index.html

AHRQ dashboard best-practice guide:

https://www.ahrq.gov/evidencenow/tools/dashboard-best-practice.html

The case table includes complete public URLs for CMS, CDC, Synthea, and CDC WONDER sources used in the exercises.

## Handoff

Module 03 selects a form that is plausible for the question and available structure. Module 04 shows why even a plausible chart and correct summary can hide a consequential tail, subgroup, or second process.

# Module 11 assessment

## Decision task

You are preparing a simulated transitions-of-care definition review. Choose one index-to-follow-up path for the mock quality team to audit before anyone proposes a real measure or intervention.

Your recommendation must use the released Synthea case. It must remain explicit that the records are simulated and that absence from the extract is not proof that care did not occur.

## Required package

```text
module-11/
  structure-definition.md
  analysis.R
  cohort-flow.png
  transition-matrix.png
  composition.png
  path-table.csv
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

## Required work

### 1. Structure definition

Before making a figure, define:

- decision owner;
- decision and action boundary;
- unit that travels;
- cohort start and end;
- index event;
- thirty-day state;
- ninety-day endpoint;
- node vocabulary;
- edge meaning and direction;
- denominator for every percentage;
- dropped and retained records;
- death precedence;
- meaning of no encounter recorded;
- synthetic-data boundary; and
- one alternative structure you rejected.

### 2. Conserved flow

Build a three-stage flow with:

- 374 people at every stage;
- counts encoded as ribbon width;
- one person counted once;
- visible state labels and counts;
- a title that states the supported finding;
- a caption naming the cohort and synthetic-data limit; and
- no rate encoded as if it were a count.

### 3. Matrix

Cross index class with thirty-day state. Every cell must show:

- count;
- percentage;
- denominator direction; and
- an empty or zero state where applicable.

### 4. Composition

Compare ninety-day endpoint composition within each index class. State that the denominator resets within each bar. Show count and percentage when space permits and preserve exact values in the table.

### 5. Exact path table

Include all seven observed transition paths and these fields:

- path;
- count;
- denominator;
- ninety-day acute-return count;
- ninety-day acute-return percentage;
- cohort acute-return percentage; and
- reference screen result.

### 6. Decision note

Write 250 to 400 words that answers:

1. Which pathway should the simulated team audit first?
2. Why does it pass the declared screen?
3. What does the flow reveal?
4. What does the matrix or composition reveal more clearly?
5. What records or definitions should be checked next?
6. What cannot be concluded?

The note must not call the screen a quality threshold, call no encounter recorded a care failure, or generalize the synthetic percentage to a real population.

### 7. Accessible alternative

The text alternative must name:

- all stage totals;
- all node totals;
- the reference path;
- the overall and reference percentages;
- the unit and denominator; and
- the synthetic-data interpretation boundary.

### 8. AI-use record

List any prompt, completion, code suggestion, debugging help, or prose revision used. State what you personally checked against the released data and source record.

## Scaffold options

### Run

Run the complete reference script. Audit the cohort contract, trace one patient and one path, and revise the decision note in your own words.

### Modify

Run the reference script, then change the flow ordering or replace the composition view with a dot plot. Explain which task becomes easier and which becomes harder.

### Author

Build all outputs from the released cohort and edge tables. You may use R, Python, Tableau, Power BI, or another approved editable tool.

The competency and grading standard do not change by scaffold.

## Critique repairs

Repair all three supplied failure modes.

### C1: changing denominator flow

Identify each denominator, recalculate all displayed percentages from one declared base or label the changing bases, and decide whether a funnel is still appropriate.

### C2: hairball network

Define node and edge meaning. Replace the node-link display with an adjacency matrix, filtered ego network, ranked edge table, or other structure that supports one named task.

### C3: treemap area and rate conflict

Separate volume from rate. Use a bar, dot, matrix, or coordinated pair of views so the audience does not read area as the rate.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Decision and action boundary | 10 | Names one owner, one definition-audit decision, and what happens next. |
| Cohort and unit | 15 | Defines eligibility, one index event per person, windows, and exclusions. |
| Nodes, edges, and conservation | 15 | Defines all structures and proves 374 people remain at each stage. |
| Denominators and rates | 15 | Makes cohort, node, and path denominators explicit and computes rates correctly. |
| Visual selection | 10 | Uses the flow, matrix, and composition for distinct questions and rejects an unsuitable structure. |
| Exactness and reproducibility | 10 | Script rebuilds the figures and seven-row table from committed data. |
| Accessibility | 10 | Uses readable labels, non-color cues, exact table, and equivalent text. |
| Interpretation and ethics | 10 | Uses precise absence language and preserves the synthetic-data boundary. |
| Source and AI records | 5 | Complete provenance and AI-use records. |
| Total | 100 |  |

## Pass conditions

All of these are required:

- total score at least 80;
- no double counting;
- stage totals equal 374;
- correct path denominator;
- exact source record;
- reproducible editable source;
- accessible alternative;
- synthetic-data statement; and
- no unsupported real-world quality claim.

## Automatic return conditions

Return the package without grading if:

- a ribbon encodes a rate as count;
- the denominator changes silently;
- one patient appears more than once in the index cohort;
- no encounter recorded is described as no care;
- the screen is described as validated;
- the result is presented as a real clinical estimate;
- a source URL or checksum is missing;
- the figure cannot be regenerated; or
- the text alternative omits the decision-relevant finding.

## Reference answer boundary

The released screen identifies `Inpatient -> No encounter recorded`: 38 synthetic patients, 6 with a ninety-day acute return, 15.8%, compared with 9.6% in the full cohort. The supported action is to audit definitions and sample records in the simulated workflow. It is not to rate care or allocate resources.

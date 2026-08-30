# DA-730 Module 03 specification: Chart selection in practice

- Specification version: 0.1.0
- Commons release: 0.14.0
- Status: runnable release candidate
- Last updated: 2026-08-29
- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module package: `courses/data-visualization/modules/03-chart-selection/`
- Prerequisite packages: `courses/data-visualization/modules/01-encoding-grammar/` and `courses/data-visualization/modules/02-perception-accuracy/`

## 1. Module identity and place in the course

| Field | Contract |
|---|---|
| Module ID | `oclc-da730-03` |
| Title | Chart selection in practice |
| Course position | Third of 13 modules |
| Learner time | 8 hours |
| Prerequisites | Modules 01 and 02 |
| Primary concept | A display is selected from the decision, reader task, evidence structure, precision need, and failure gate |
| Primary software path | R and ggplot2 |
| Primary case | Hospital patient experience, response rate, and survey volume |
| Decision owner | Hospital executive team |
| Next module | Module 04, Distributions versus summaries |

Module 01 established the grammar of a display. Module 02 established that different channels create different perceptual judgments. Module 03 joins those ideas into a repeatable selection process. The answer is not always a chart. It may be a table, coordinated pair, or a decision to request better evidence.

This module closes the first chart-selection sequence. Later modules deepen one structure at a time. Module 03 gives learners a disciplined starting choice without pretending that one taxonomy resolves every design question.

## 2. Healthcare decision and audience

### Primary decision

A hospital executive team is reviewing publicly reported patient-experience results. It wants to decide which hospitals or measures deserve deeper review. The briefing must support three different questions:

1. How do current recommendation results compare across a declared hospital set?
2. What are the exact recommendation result, response rate, and completed-survey count for a named hospital?
3. Which combinations of recommendation result and response rate warrant follow-up?

These questions use overlapping fields but require different reader actions. The learner selects the smallest useful form for each and explains why one repeated chart template would fail.

### Decision boundary

The exercise may identify records for deeper review. It may not:

- declare a fair quality ranking;
- infer a statistically meaningful difference without uncertainty evidence;
- infer that response rate causes the recommendation result;
- treat one HCAHPS measure as total hospital quality; or
- convert missing or suppressed results into estimated marks.

### Audience characteristics

The executive team includes clinical, operational, patient-experience, and analytic readers. Some need a rapid pattern, some need an exact value, and some need the source context behind a question. The deliverable must work in a meeting, in a saved briefing, and through an accessible alternative.

The design must account for:

- limited meeting time;
- different levels of statistical and visualization training;
- screen, print, grayscale, zoom, and assistive-technology use;
- pressure to rank even when comparability is incomplete; and
- the need to return from a visible pattern to an exact sourced record.

### Secondary cases

The 10-case matrix transfers the same reasoning to:

- an exact lookup;
- a quantitative relationship;
- a patient-level distribution;
- an ordered time series;
- part-to-whole composition;
- a care-pathway flow;
- a geographic pattern;
- a multi-measure monitoring question; and
- a question that the available evidence cannot support.

## 3. Foundation skill revisited or extended

The module assumes learners can:

- inspect a CSV and state what one row represents;
- classify variables by analytical role;
- identify marks, channels, scales, guides, and layers;
- distinguish detection, identification, ordering, estimation, comparison, and lookup;
- describe why aligned position generally supports close comparison better than angle or area; and
- run a supplied R script and inspect its outputs.

It extends these skills through the DECIDE method:

1. **Decision and owner:** Who acts, and what choice does the evidence inform?
2. **Evidence grain and shape:** What does one row represent, and is the available structure appropriate?
3. **Comparison and reader task:** What must the reader do?
4. **Information precision and context:** Are exact values, denominators, uncertainty, periods, definitions, or missingness required?
5. **Display candidates and companions:** What is the smallest useful form, and does another necessary view or note belong beside it?
6. **Evaluate failure and no-display conditions:** What evidence gap would stop publication?

The method is a reasoning scaffold, not a rigid chart taxonomy. A different selection can earn full credit when the learner preserves the decision, data, task, precision, context, and failure logic.

## 4. Assessable learning outcomes

### Competency statement

Select and justify a chart, table, coordinated pair of views, or decision not to visualize based on the question, data structure, audience, and required precision.

### Outcomes

| ID | Outcome | Direct evidence |
|---|---|---|
| M03.1 | State a named decision owner and actionable choice before selecting a form. | Ten-case selection matrix |
| M03.2 | Distinguish comparison, lookup, relationship, distribution, time, composition, flow, geography, monitoring, and evidence-verification tasks. | Matrix reader-task fields and assessment items |
| M03.3 | Match each task to the minimum defensible data grain and shape. | Data-shape and no-display fields |
| M03.4 | Identify required context, including denominators, periods, uncertainty, missingness, definitions, and source status. | Matrix, source record, and companion choices |
| M03.5 | Compare at least two plausible forms and reject one for a decision-specific reason. | Rejected-alternative field and decision note |
| M03.6 | Defend a table as the primary display for exact lookup. | Exact-lookup CSV and assessment response |
| M03.7 | Build reproducible comparison and relationship views from a pinned public clinical release. | `analysis.R` and two PNGs |
| M03.8 | Apply a predeclared no-display trigger when evidence is missing, mismatched, or unsupported. | C10 and transfer response |
| M03.9 | Communicate a bounded executive recommendation with an accessible companion. | Decision note and alt text |

## 5. Concept ownership and boundaries

### This module owns

- decision-first chart selection;
- reader task as a selection input;
- data grain and shape as selection constraints;
- precision and context requirements;
- choosing a table as a positive design decision;
- selecting coordinated views only when they answer distinct necessary questions;
- comparing a candidate with a rejected alternative;
- declaring a no-display trigger before polishing a result;
- the DECIDE selection matrix; and
- diagnosing a dashboard that forces one form onto unrelated questions.

### This module introduces but does not own

- distributions and subgroup structure;
- ordered time and process views;
- part-to-whole, flow, geography, and monitoring displays;
- denominators and adjustment;
- uncertainty and small-number stability;
- accessible color and redundant encodings;
- multi-view coordination; and
- executive annotation and narrative.

The matrix introduces these structures so learners can make an initial choice. Their statistical, ethical, and design details belong to later modules.

### Explicitly out of scope

- a universal chart chooser;
- memorizing chart names as a competency;
- full distribution analysis, owned by Module 04;
- rate and denominator analysis, owned by Module 05;
- uncertainty estimation, owned by Module 06;
- complete color and accessibility design, owned by Module 07;
- time-series and process inference, owned by Module 08;
- full small-multiple, map, flow, dashboard, or narrative construction, owned by Modules 09 through 13;
- causal inference from a visual relationship;
- fair hospital ranking; and
- importing every future module dataset into this package.

## 6. Lesson sequence and learner time

The module totals 8 hours, or 480 minutes.

| Sequence | Time | Activity | Required evidence |
|---|---:|---|---|
| Executive decision opening | 30 min | Ask three different questions of one HCAHPS source. | Three reader-task statements |
| DECIDE concept core | 45 min | Work from decision through failure gate. | One completed matrix row |
| HCAHPS cases C01 to C03 | 75 min | Compare an aligned plot, exact table, and relationship view. | Three defended selections |
| Transfer cases C04 to C10 | 90 min | Select forms for distribution, time, composition, flow, geography, monitoring, and unsupported evidence. | Ten-case draft matrix |
| Runnable lab | 60 min | Build two charts, one lookup table, and matrix files. | Verified outputs |
| Dashboard critique | 45 min | Diagnose one bar form forced onto four questions. | Repair plan |
| Independent assessment | 105 min | Complete the six-part submission. | Assessment package |
| Peer run and revision | 30 min | Check code, source, alternatives, access, and no-display gate. | Verification note and corrections |
| **Total** | **480 min** | | **8 hours** |

### Sequence rule

Do not open with a gallery of chart names. Begin with the executive choice and ask learners to name the reader task. Chart vocabulary enters after decision, evidence, and precision are explicit.

### Short-time path

If synchronous time is limited, keep C01, C02, C03, C04, C08, C09, and C10 in class. Assign C05, C06, and C07 as matrix work. Keep the two builds, table defense, dashboard critique, and no-display gate.

## 7. Authoritative readings and public clinical sources

### Required design guidance

1. Agency for Healthcare Research and Quality, Displaying Your Data.
   https://www.ahrq.gov/talkingquality/translate/display/index.html
2. Agency for Healthcare Research and Quality, Best Practices in Dashboard Design.
   https://www.ahrq.gov/evidencenow/tools/dashboard-best-practice.html

Learners extract the decision purpose, comparison or lookup need, amount of information, ordering, labeling, and audience burden from these readings. The readings inform judgment. They do not replace the DECIDE analysis of the actual case.

### Required clinical sources

CMS, Hospitals topic:

https://data.cms.gov/provider-data/topics/hospitals

CMS, Patient survey (HCAHPS) - Hospital:

https://data.cms.gov/provider-data/dataset/dgck-syfz

### Transfer-source directory

- CMS, Timely and Effective Care - Hospital: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- CDC WONDER datasets: https://wonder.cdc.gov/datasets.html
- CDC PLACES county data: https://data.cdc.gov/d/fu4u-a9bh
- Synthea: https://synthetichealth.github.io/synthea/

These transfer URLs identify appropriate public-source families. Cases C04 through C09 define future data requirements but do not claim that those datasets were downloaded or transformed in this module.

### Required prerequisite materials

- Module 01 encoding map and HCAHPS source record;
- Module 02 perception evidence note and decision note;
- `courses/data-visualization/modules/03-chart-selection/README.md`;
- `courses/data-visualization/modules/03-chart-selection/data-spec.md`; and
- the 10-row canonical case table.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Canonical selection-case release

| Field | Value |
|---|---|
| Path | `data/selection_cases_2026.csv` |
| Rows | 10 |
| Columns | 13 |
| Grain | One question-to-display decision case |
| Builder | `build_selection_cases.R` |
| Validator | `validate_selection_cases.R` |
| Checksum | `0f295bd9bf94e9f5800e4fdaebea303d8cc0b28ccd3afcb01603d8e1c0a2eff8` |
| Rights | Original instructional metadata released under the repository documentation license |

The case table is not an imported clinical dataset. It is a deterministic instructional index that names the decision, reader task, required evidence shape, source family, reference choice, companion, and failure gate.

### Upstream HCAHPS release

| Field | Value |
|---|---|
| Publisher | Centers for Medicare & Medicaid Services |
| Dataset | Patient survey (HCAHPS) - Hospital |
| Dataset ID | `dgck-syfz` |
| CMS release | 2026-08-13 |
| Coverage | 2024-10-01 through 2025-09-30 |
| Shared extract | `../01-encoding-grammar/data/hcahps_ma_recommend_2026.csv` |
| Shared extract rows | 65 Massachusetts recommendation-result rows |
| Status counts | 56 reported and 9 unavailable |
| Shared extract checksum | `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74` |
| Original CMS file checksum | `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc` |
| Rights | U.S. government public-reporting data in the public domain; attribution requested; no implied endorsement |

### Worked-analysis subsets

The relationship view uses the 56 reported rows with finite recommendation result, response rate, and completed surveys. The comparison and lookup views select the 15 such hospitals with the largest completed-survey counts, breaking ties by facility ID. This deterministic rule supports a readable teaching view. It does not define a clinical peer group.

### Teaching purpose

Using one source for C01 through C03 isolates the selection problem. The question changes while the underlying source remains stable. Learners can therefore see why overlapping fields do not justify one repeated display.

### Rights and reuse rule

Keep publisher, dataset title, complete URL, release, coverage, transformations, checksums, and limits with any reused extract. Do not imply that CMS endorses the course, analysis, or recommendation.

## 9. Data dictionary and expected analytic structure

### Selection-case dictionary

| Field | Type | Meaning |
|---|---|---|
| `case_id` | string | Stable key `C01` through `C10` |
| `case_title` | string | Short question label |
| `decision_owner` | string | Person or group that acts |
| `decision` | string | Choice the evidence informs |
| `reader_task` | string | Primary operation the reader performs |
| `data_shape` | string | Minimum grain and structure needed |
| `precision_need` | string | Pattern, exact value, relationship, shape, or other exactness requirement |
| `context_required` | string | Definitions, denominator, uncertainty, period, missingness, or other attached context |
| `source_url` | URL | Full public-source or source-family URL |
| `reference_choice` | string | Defensible starting selection |
| `required_companion` | string | Necessary table, note, or second view |
| `no_display_trigger` | string | Evidence failure that stops a quantitative display |
| `build_mode` | category | `build`, `table`, or `decision-only` |

### Reader-task vocabulary

| Task | Reader action | Typical evidence requirement |
|---|---|---|
| Compare | Order units and judge gaps | Comparable quantitative measure across units |
| Lookup | Retrieve exact named values | Stable identifiers, definitions, and exact fields |
| Relationship | Examine paired quantitative combinations | Two comparable measures at the same grain |
| Distribution | Inspect shape, tails, and subgroups | Unit-level or sufficiently granular observations |
| Time | Follow ordered periods | Stable measure definition and ordered time field |
| Composition | Judge contributions to one total | Mutually interpretable parts and defensible total |
| Flow | Follow movement among states | Defined cohort, states, transitions, and counts |
| Geography | Locate spatial pattern | Aligned geography, denominator, period, and estimate |
| Monitor | Combine overview with retrieval | Refreshable measures, status rules, and exact values |
| Verify evidence | Decide whether a claim can be shown | Adequate denominator, definition, population, and period |

### HCAHPS analytic structure

The lab requires:

- `facility_id` and `facility_name`;
- `recommend_percent`;
- `response_rate_percent`;
- `completed_surveys`;
- `value_status`;
- `period_start` and `period_end`; and
- `cms_release_date`.

One row represents one Massachusetts hospital's `H_RECMND_DY` result in the pinned release. Unavailable values remain in the source extract and are excluded only through an explicit reported-value filter.

### Derived outputs

| Output | Grain | Selection logic |
|---|---|---|
| Comparison PNG | One mark per selected hospital | 15 largest completed-survey counts among complete reported rows |
| Relationship PNG | One mark per complete reported hospital | All finite reported rows |
| Lookup CSV | One row per selected hospital | Same deterministic 15-hospital comparison subset |
| Reference matrix CSV | One row per case | Canonical 10-case table |
| Learner matrix CSV | One row per case | Canonical fields plus blank decision fields |

## 10. Worked example and instructor walkthrough

### Worked question

The executive team asks, "Which recommendation results should we review more closely?"

### DECIDE walkthrough

1. **Decision and owner:** The hospital executive team selects results for deeper review. It is not publishing a definitive hospital ranking.
2. **Evidence grain and shape:** One reported recommendation percentage is available for each hospital. Response rate and completed surveys provide necessary context.
3. **Comparison and reader task:** The primary task is to order hospitals and inspect close gaps.
4. **Information precision and context:** The pattern is primary, but exact percentages, response rate, survey count, release, and measurement period must remain retrievable.
5. **Display candidates and companions:** Compare an aligned dot plot, common-baseline bar chart, multi-metric bubble chart, and exact table. Select the aligned dot plot with a companion table.
6. **Evaluate failure:** Stop if hospital definitions, measure definitions, or periods are inconsistent.

### Why the dot plot is selected

Aligned position supports ordering and close comparison. Direct labels assist retrieval. The table preserves response rate and completed surveys without forcing three different quantities into one mark.

### Rejected alternative

A multi-metric bubble chart is rejected because area would make survey volume visually prominent while weakening the primary percentage comparison. It also encourages the reader to combine measures that answer different questions.

### Bound the result

The view describes a declared CMS release and subset. It does not establish statistical difference, cause, fair peer comparison, or total hospital quality.

### Counterexample: exact lookup

When the executive asks for three exact fields for a named hospital, the table becomes the primary display. A chart would replace retrieval with estimation. The source and measure notes still accompany the table.

## 11. Guided practice

### Tier 1: Run and interpret

Learners:

1. rebuild and validate the case table;
2. run the lab against the Module 01 HCAHPS extract;
3. inspect the comparison plot, relationship plot, lookup table, and matrices;
4. complete DECIDE fields for C01 through C03; and
5. explain why the three cases do not share one primary form.

### Tier 2: Complete and critique

Learners complete C04 through C10. For each case they must:

- name the decision and reader task;
- confirm whether the required data shape exists;
- state the precision and context needs;
- choose one candidate and companion;
- reject one plausible alternative;
- apply the no-display trigger; and
- state the final choice.

The instructor then renders the intentionally flawed dashboard. Learners diagnose each panel before seeing the repair key.

### Tier 3: Modify and defend

Each learner changes one element of the HCAHPS decision:

- the decision owner;
- the primary reader task;
- the size of the hospital set;
- the need for exact values;
- the available context; or
- the evidence failure condition.

The learner predicts whether the primary form, companion, or no-display gate changes, implements the resulting view, and explains the change. A cosmetic change alone does not meet Tier 3.

## 12. Independent exercise

### Prompt

Complete all 10 question-to-display decisions. Build the two HCAHPS chart cases. Defend why the exact lookup case is a table. Prepare one executive recommendation that includes its required companion and a no-display gate.

### Required chain for each matrix row

1. Who acts?
2. What choice is informed?
3. What must the reader do?
4. What does one row represent?
5. What evidence shape is available?
6. How precise must the reading be?
7. What context must travel with it?
8. What form is plausible?
9. What companion is necessary?
10. What plausible alternative fails, and why?
11. What evidence failure stops publication?
12. What is the final choice?

### Build requirement

The learner writes `analysis.R` that:

- reads the Module 01 extract through a relative path;
- checks required fields;
- uses deterministic reported and 15-hospital subsets;
- creates the comparison and relationship figures;
- exports the exact lookup table;
- includes source release and period in output context; and
- writes the exact filenames under `figures/`.

### Transfer prompts

1. A leader requests a county map of raw admissions. Name the decision, missing denominator, required companion, and no-display trigger.
2. A distribution question arrives with only a mean. State why no chart repair can recover the hidden patient-level structure.
3. A dashboard team asks that every panel use bars for consistency. State which consistency requirements matter and which reader-task differences override the template.

## 13. Visualization and communication requirements

### Comparison figure

`figures/comparison.png` must:

- use aligned position or common-baseline length;
- support ordering and close-gap comparison;
- display readable hospital labels;
- show percentage units;
- include exact values directly or through the companion table;
- state CMS release and period;
- avoid implying statistical separation or a quality league table; and
- remain interpretable without color.

### Relationship figure

`figures/relationship.png` must:

- map recommendation percent and response rate to paired quantitative position;
- identify both units;
- use completed surveys only as labeled secondary context when included;
- provide a plotted-value table;
- state the CMS release;
- identify missing-value filtering; and
- say that association does not establish cause.

### Exact lookup table

`figures/exact-lookup.csv` is the primary display for C02. It includes facility ID, hospital name, recommendation percentage, response-rate percentage, and completed surveys for the declared subset. Column names and units must be understandable outside the R session.

### Coordinated-view rule

Every view in a pair must answer a distinct necessary question. Repeating the same information in another style does not justify a second view. Each pair must share identifiers, definitions, period, and source status.

### No-display rule

A disclaimer cannot rescue a mark that lacks a defensible value. When the no-display trigger is met, submit a readable evidence-gap note naming what is missing, why the proposed claim cannot be shown, and what evidence is needed next.

## 14. Exact submission package and filenames

```text
module-03/
  selection-matrix.md
  analysis.R
  figures/
    comparison.png
    relationship.png
    exact-lookup.csv
  source-record.yml
  alt-text.md
  decision-note.md
```

### `selection-matrix.md`

Include all 10 cases with decision and owner, reader task, data grain and shape, precision and context, candidate display, required companion, rejected alternative, no-display trigger, final choice, and two to four sentences of justification.

### `source-record.yml`

Retain the module source record and add:

- analysis date;
- exact subset rule;
- source and output row counts;
- transformations;
- output paths;
- input and output checksums; and
- unresolved source limitations.

### `alt-text.md`

Write a separate 80 to 150 word alternative for each PNG. Introduce the CSV in two sentences that name its columns and deterministic selection rule.

### `decision-note.md`

Use these headings:

```markdown
# Decision note

## Executive team and decision
## Reader task
## Selected primary display
## Required companion
## Rejected alternative
## Failure and no-display test
## What the evidence cannot establish
## Reproducibility check
## AI assistance disclosure
```

### Reproducibility rule

Relative paths, source checks, deterministic filters, and exact output filenames are required. A screenshot, proprietary published link, or manually edited CSV without runnable source is incomplete.

## 15. Rubric and pass conditions

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Ten-case selection matrix | 25 | Complete decision, task, grain, precision, context, candidate, companion, rejection, failure gate, and choice |
| Reproducible analysis | 20 | Relative paths, field checks, deterministic subsets, two PNGs, and exact CSV export |
| Display-task fit | 20 | Comparison, relationship, and lookup forms each fit their distinct task |
| Decision note | 15 | Executive recommendation, companion, rejected alternative, failure test, and bounded claim |
| Source and provenance | 10 | Exact sources, release, period, transformations, outputs, rights, and checksums |
| Accessibility and alternatives | 10 | Readable non-color-dependent figures, complete alternatives, and accessible lookup file |
| **Total** | **100** | |

The pass mark is 75. All five conditions are mandatory:

1. all 10 cases have a final choice and no-display trigger;
2. `analysis.R` creates the two figures and exact CSV;
3. C02 remains a table unless the reader task is explicitly changed;
4. C10 remains no display until its named evidence gap is resolved; and
5. source, release, period, subset, transformations, and limits are accurate.

### Week-3 checkpoint contribution

The selection matrix, built views, table defense, source record, and decision note enter the week-3 visualization judgment dossier. At the checkpoint, the learner must show how Modules 01 through 03 connect variable roles, perceptual judgment, and display choice.

## 16. Common errors, failure modes, and interventions

| Failure | Likely misconception | Intervention |
|---|---|---|
| Learner begins with a favorite chart | Tool vocabulary precedes the decision. | Hide chart names and ask for owner, choice, and task first. |
| One numeric field automatically becomes a bar | Data type is treated as sufficient selection logic. | Change the task from comparison to lookup and select again. |
| Every case receives two views | More views are treated as more sophisticated. | Require a distinct necessary question for every view. |
| The table is called a fallback | Exact lookup is undervalued. | Time one retrieval from a chart and the table. |
| C10 receives a chart plus disclaimer | Disclosure is confused with evidence. | Ask what defensible value each mark would represent. |
| A map is chosen because a place field exists | Geography is mistaken for a geographic decision. | Name the place-based action and aligned denominator. |
| A relationship title claims cause | Paired position is confused with causal identification. | Rewrite the title as a descriptive relationship question. |
| Composition parts do not share a total | Part-to-whole syntax is used without a whole. | Rebuild the denominator and hierarchy before drawing. |
| Flow counts mix people and encounters | Grain changes across transitions. | Define cohort, state, unit, and repeat handling. |
| A time view joins incompatible periods | Ordering is treated as comparability. | Audit measure definition and reporting window before plotting. |
| The dashboard repeats one template | Visual consistency is confused with task fit. | Put the reader task above every panel and redesign separately. |
| AI supplies missing context | Plausibility replaces provenance. | Trace the field to the source or mark it unresolved. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Required meaning cannot depend on color alone.
- Hospital labels and exact values must be available as text.
- The relationship view's point size, if used, has a text legend and remains secondary.
- Both figures require complete text alternatives.
- The lookup table uses meaningful headers and no merged visual cells.
- No-display output is a readable evidence-gap note, not an empty placeholder.
- Figures must remain legible at ordinary document size and when zoomed.

### Equity

HCAHPS response patterns, missingness, language access, survey mode, who is reached, and who responds may affect interpretation. The teaching extract does not include patient subgroup fields. A hospital-level comparison cannot establish equitable experience across race, ethnicity, language, disability, payer, gender, or other populations.

A geographic or workforce case must not turn a model-based area estimate into a claim about every resident. A map can identify a place for deeper review, but resource allocation requires denominator, uncertainty, local context, and stakeholder input.

### Privacy

The HCAHPS input is aggregate public data. No patient-level record enters this module. If a learner substitutes patient-level or restricted data, the substitution requires separate authorization, minimization, secure handling, disclosure review, and an instructor-approved release plan. It must not be committed to the public repository.

### Responsible claims

Allowed:

- describe patterns in the declared CMS release and subset;
- retrieve exact published values;
- identify unusual combinations for follow-up;
- state a task-specific display recommendation;
- explain what context or evidence is missing; and
- choose not to visualize.

Not allowed:

- call the 15-hospital subset a clinical peer group;
- infer statistical difference without uncertainty evidence;
- infer cause from recommendation and response-rate association;
- rank total hospital quality from one measure;
- estimate unavailable values without an approved method; or
- present a map, flow, composition, or time view when its required structure is absent.

## 18. AI and agent policy

AI may assist with:

- proposing candidate forms;
- identifying a likely reader task;
- debugging the build or analysis code;
- checking whether output fields match the stated selection;
- suggesting an alternative or failure test;
- editing the source record, decision note, or alt text; and
- checking consistency across the package.

AI may not:

- invent missing data, denominators, dates, definitions, or source terms;
- convert unavailable values into plausible numbers;
- choose a final display without the learner's evidence check;
- claim to have visually inspected an output it did not inspect;
- make a causal or quality-ranking claim from the HCAHPS views;
- bypass the no-display trigger; or
- replace the learner's reproducibility run.

The decision note records the tool, purpose, adopted change, and learner verification. `No AI assistance used.` is complete when true.

## 19. Answer key and instructor notes

The instructor key is:

`courses/data-visualization/modules/03-chart-selection/instructor-notes.md`

It contains:

- the verified environment and outputs;
- the complete eight-hour sequence;
- reference choices for all 10 cases;
- accepted alternative logic;
- worked HCAHPS answers;
- the flawed-dashboard diagnosis and smallest repair;
- common-error interventions;
- a strong executive decision-note pattern;
- point-level grading guidance;
- accessibility checks;
- the short-time path; and
- human review requirements.

### Reference decisions

| Case | Reference selection | Required companion |
|---|---|---|
| C01 | Aligned dot plot | Response-rate and survey-count table |
| C02 | Table | Definition and missing-value note |
| C03 | Scatterplot | Plotted-value and survey-count table |
| C04 | Distribution view with subgroup comparison | n, median, upper quantile, and subgroup counts |
| C05 | Line or run chart with process context | Definition and reporting-period note |
| C06 | Ordered composition view | Counts, denominator, and suppression table |
| C07 | Flow view | Transition table and cohort definition |
| C08 | Map plus aligned comparison | Estimate, denominator, uncertainty, and workforce table |
| C09 | Coordinated comparison and exact table | Accessible table and source status |
| C10 | No display | Evidence-gap and data-request note |

These are reference answers, not a fixed menu. An alternative receives full credit when it supports the same decision and task, uses adequate evidence, preserves required context, and passes a defensible failure test.

## 20. Runnable acceptance checks

Run from `courses/data-visualization/modules/03-chart-selection/`.

### Rebuild the case table

```powershell
Rscript build_selection_cases.R
```

Pass: `data/selection_cases_2026.csv` contains the same 10 deterministic cases and checksum.

### Validate the cases and upstream data

```powershell
Rscript validate_selection_cases.R
```

Pass: 13 of 13 checks succeed, including task coverage, build modes, no-display case, HCAHPS release, reported row count, and relationship fields.

### Generate learner lab outputs

```powershell
Rscript lab.R
```

Pass: the script creates:

- `01-comparison-dot-plot.png`;
- `02-response-relationship.png`;
- `03-exact-lookup-table.csv`;
- `selection-matrix-reference.csv`; and
- `selection-matrix-template.csv`.

### Generate the critique dashboard

```powershell
Rscript critique_charts.R
```

Pass: `01-one-form-for-every-question.png` is created.

### Visual inspection

Confirm:

- comparison labels and direct values are readable;
- comparison source release and period are visible;
- the relationship view maps two percentages to position;
- completed surveys are clearly secondary;
- the noncausal caption is visible;
- the lookup CSV contains the five contracted fields;
- the critique visibly forces bars onto distinct tasks; and
- the critique's combined relationship value is clearly presented as an intentional flaw.

### Source and link check

Confirm browser resolution for all full source URLs in the case table and for both required AHRQ readings. Record redirects or access barriers without substituting an unofficial copy.

### Repository checks

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
node --check curriculum-data.js
git diff --check
```

### Clean-run gate

Before alpha, an independent instructor follows only the learner README from a clean checkout, rebuilds and validates the cases, generates every output, completes the matrix, and records hidden assumptions or broken links.

## 21. Release status, reviewers, version, and known issues

### Release identity

| Item | Value |
|---|---|
| Module version | 0.1.0 |
| Commons release | 0.14.0 |
| Status | Runnable release candidate |
| Release date | 2026-08-29 |
| Technical validation | Complete |
| Visual inspection | Complete for three generated PNGs |
| Human review | Pending |

### Maturity gate

The module is a runnable release candidate because the case table is deterministic, all 13 data checks pass, the shared HCAHPS source remains pinned, two charts and one exact table render, the flawed dashboard renders, the assessment package is exact, and the instructor key covers every case.

Alpha requires sign-off from:

1. visualization faculty for task and selection logic;
2. a hospital executive, clinician, or patient-experience leader for decision realism;
3. accessibility review for figures, tables, alternatives, and no-display communication; and
4. independent teachability from a clean checkout.

Beta requires a taught pilot and revision. Stable requires successful reuse by a second instructor or program.

### Known issues

- Human reviews are pending.
- Reference choices are task-specific starting points and can become harmful if taught as a rigid taxonomy.
- Cases C04 through C09 define required structures without importing their future module extracts.
- The 15-hospital subset supports readability, not clinical comparability.
- HCAHPS worked views are descriptive and do not establish cause, statistical distinction, fair ranking, or total hospital quality.
- The relationship view uses completed surveys as area, which is secondary context and not the primary comparison channel.
- AHRQ pages returned a request-blocked title in the automated headless Chromium check, but both exact URLs resolved with full official content through an independent web fetch on 2026-08-29.
- Automated source links can redirect or change after release.
- macOS and Linux clean-run verification is pending.

## Handoff to Module 04

Module 03 ends with a defensible first selection. Module 04 then challenges a common assumption behind that choice: even a plausible form and correct summary can hide a long tail, a second mode, an unequal subgroup, or a distinct operational process.

The learner carries forward:

- decision owner and action;
- reader task;
- data grain and shape;
- required context and failure gate;
- selected primary and companion forms;
- source record; and
- a bounded claim.

The next build unit is Module 04, Distributions versus summaries. Its existing runnable candidate must be reconciled with this source-first 21-section contract before release.

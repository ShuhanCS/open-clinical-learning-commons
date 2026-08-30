# DA-730 Module 11 specification: Flow, networks, composition, and hierarchy

Status: runnable release candidate
Module version: 0.1.0
Commons release: 0.22.0
Course owner: Ali Goff
Curriculum sponsor: Shuhan He
Technical package: `courses/data-visualization/modules/11-flow-networks-composition-hierarchy/`
Module hours: 8.0
Week: 6

## 1. Purpose, scope, and ownership

Module 11 teaches learners to represent structure when ordinary comparison, distribution, time, and geography no longer express the decision well.

The central question is not, Which exotic chart should I use? It is, What exactly is moving, connected, nested, or divided, and what decision depends on that structure?

The module owns:

- cohort flows;
- state transitions;
- funnels when stages are genuinely nested;
- alluvial and Sankey reasoning;
- nodes, edges, direction, and weights;
- adjacency and transition matrices;
- network-display failure modes;
- composition and part-to-whole displays;
- trees, hierarchies, and treemaps;
- conservation and attrition;
- edge and path denominators;
- double counting; and
- the decision to use an ordinary table or comparison instead.

The module does not own:

- survival analysis;
- Markov modeling;
- causal pathway analysis;
- formal graph theory;
- network centrality inference;
- referral optimization;
- risk adjustment;
- real readmission-measure construction;
- implementation science;
- dashboard composition; or
- narrative capstone production.

Module 12 owns dashboards and coordinated monitoring. Module 13 owns final audience, annotation, narrative, and defense.

### Required intellectual move

Before selecting a display, the learner must write a structure definition containing the unit, cohort, stages, nodes, edges, direction, time window, denominator, exclusions, and interpretation boundary.

### Completion standard

The module is complete when the learner can prove that the same unit is conserved through the reference flow, explain why the matrix and composition views answer different questions, and refuse a network or hierarchy display that lacks a decision purpose.

## 2. Healthcare decision and audience

### Decision owner

A simulated transitions-of-care director is preparing a definition review before a real quality measure is proposed.

### Decision

Choose one index-to-follow-up pathway for a mock audit of cohort logic, encounter grouping, observation windows, and missing-record meaning.

### Supported action

The team may select records from the simulated pathway, trace the source fields, test alternate definitions, and document what a production data owner would need to confirm.

### Unsupported actions

The module does not support:

- rating a hospital;
- labeling a care pathway as poor;
- identifying a preventable return;
- contacting a patient;
- allocating clinical resources;
- setting a payment measure;
- estimating a real readmission rate; or
- claiming that no encounter recorded means no care occurred.

### Reference decision

The declared teaching screen selects `Inpatient -> No encounter recorded` because:

- its denominator is 38 synthetic patients;
- 6 have an acute return within 90 days;
- its acute-return percentage is 15.8%;
- the full cohort percentage is 9.6%; and
- the path has at least 20 people and exceeds the full cohort percentage.

The action is to audit the definition. The screen is not validated, risk-adjusted, official, or inferential.

### Audience needs

The transitions-of-care director needs:

- a conserved cohort;
- visible state counts;
- explicit denominators;
- exact path values;
- a way to distinguish first follow-up from any later acute event;
- clear absence language;
- a reproducible source record; and
- a statement of what must be checked before real use.

## 3. Competency and learning outcomes

### Competency

Select and define a flow, matrix, network, composition, or hierarchical display when links, states, or part-to-whole structure are central to a healthcare decision.

### Learning outcomes

By the end of the module, learners can:

1. name the decision before naming the chart;
2. define the unit that travels through a flow;
3. create a one-row-per-person index cohort;
4. distinguish an event, state, node, edge, path, branch, and hierarchy;
5. declare edge direction and weight;
6. preserve a missing or absent state instead of dropping it;
7. prove conservation at every stage;
8. distinguish cohort, node, path, and group denominators;
9. distinguish a count-width flow from a rate display;
10. choose an alluvial display for a small conserved sequence;
11. choose a matrix for origin-destination lookup and exact comparison;
12. choose a stacked composition view for within-group shares;
13. choose a tree or indented table for nesting;
14. use a treemap only when area supports the task;
15. reject a node-link hairball without a topology task;
16. audit double counting and changing denominators;
17. preserve exact values outside the figure;
18. write an equivalent text alternative;
19. describe extract absence without claiming real-world absence;
20. keep synthetic output separate from empirical evidence; and
21. hand a stable definition dictionary to a dashboard builder.

### Mastery evidence

Mastery requires a complete structure definition, three reproducible views, an exact table, a source record, an accessible alternative, a decision note, and an AI-use record.

## 4. Prerequisites and conceptual handoff

### Required prerequisites

Learners should have completed Modules 01 through 10.

### Inherited competencies

Module 11 assumes learners can:

- identify variable types and visual channels;
- evaluate perceptual accuracy;
- choose a chart, table, or no chart;
- distinguish distributions from summaries;
- define numerator and denominator;
- state uncertainty and small-number limits;
- use accessible color and non-color cues;
- distinguish chronological order from process variation;
- compare groups on common scales; and
- state what geography adds and conceals.

### Specific handoff from Module 10

Module 10 ended with the rule that a structure must serve a decision and must name what it hides. Module 11 changes the central relation from place to transition, connection, hierarchy, or composition.

### Misconceptions to diagnose before the lab

- Every relationship belongs in a network.
- Every sequence belongs in a Sankey.
- Ribbon width can represent either counts or rates without consequence.
- A funnel automatically proves attrition.
- Missing rows can be dropped.
- A treemap's largest area means highest rate.
- Synthetic patient-level data behave like de-identified clinical records.

## 5. Workload and module sequence

The module has 8.0 learner hours within instructional week 6.

| Component | Hours | Evidence |
|---|---:|---|
| Decision and synthetic-data boundary | 0.5 | Written decision and action boundary. |
| Cohort and unit definition | 0.75 | Structure definition draft. |
| Flow, network, composition, and hierarchy core | 0.75 | Selection notes. |
| Source and cohort trace | 0.75 | One audited patient path. |
| Reference lab | 1.0 | Three regenerated outputs. |
| Critique and repair | 0.75 | Three diagnosed failures. |
| Independent build | 1.75 | Editable source and figures. |
| Exact table, accessibility, and decision note | 1.0 | Submission package. |
| Peer conservation audit and handoff | 0.75 | Signed checklist. |
| Total | 8.0 |  |

### Recommended order

1. Name the decision and audience.
2. Define the unit.
3. Define one index event per unit.
4. Define mutually exclusive states.
5. Define edge direction and weight.
6. Prove conservation in a table.
7. Select a visual structure.
8. Build the flow.
9. Build an exact alternative.
10. Write the decision note.

### Stop rule

If the learner cannot state what one ribbon unit represents, the visual build pauses. The cohort table must be repaired first.

## 6. Concept model and vocabulary

### Cohort

A declared set of units eligible for the analysis. In this case the unit is one adult synthetic patient with one first qualifying acute encounter.

### Event

A time-stamped record such as an emergency, inpatient, outpatient, urgent-care, wellness, or ambulatory encounter.

### State

A mutually exclusive category assigned at a declared point or interval. A state is not automatically identical to a raw event class.

### Node

A defined state, entity, or category in a structural display. Every node needs a type, membership rule, and denominator.

### Edge

A defined relationship from one node to another. Every edge needs meaning, direction, time, and weight.

### Path

The ordered sequence of states followed by one unit. A path count is not a path rate until a denominator and outcome are declared.

### Conservation

The rule that the same 374 cohort members remain accounted for at every stage. A no-record state is necessary to preserve conservation.

### Attrition

A reduction in units across genuinely nested stages. Attrition must not be simulated by silently changing the denominator.

### Composition

Parts of a defined whole. A 100% stacked bar resets the denominator within each bar and must say so.

### Hierarchy

A parent-child nesting relation. A sequence, association, or referral does not become a hierarchy merely because it can be drawn as a tree.

### Network

Entities connected by defined edges. A node-link display is only one representation of a network and is often inferior to a matrix or edge list for comparison.

### Flow versus rate

The reference ribbons carry counts. The acute-return percentage belongs in the path table or a rate display. A 15.8% rate cannot be given a ribbon width unless its denominator and count relationship remain explicit.

## 7. Public sources, rights, and provenance

### Core source

Synthea is an open-source synthetic patient generator.

- Project: https://synthetichealth.github.io/synthea/
- Downloads: https://synthea.mitre.org/downloads
- Archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- Repository: https://github.com/synthetichealth/synthea
- Data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- License: https://github.com/synthetichealth/synthea/blob/master/LICENSE

### Archive identity

- Label: April 2020 CSV sample.
- Retrieved: 2026-08-30.
- Bytes: 8,982,431.
- SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.

### Rights decision

The project uses Apache 2.0, and the official site describes the generated records as synthetic and free from cost, privacy, and security restrictions. Redistribution with attribution is allowed.

### Data minimization decision

The source contains synthetic names, addresses, SSNs, driver identifiers, and passports. They are not real identifiers, but the lesson does not need them. The Commons removes them to model purpose limitation and prevent irrelevant identifier-like data from distracting learners.

The release also omits provider, organization, payer, and cost fields because the case does not use them.

### Alternate source

ClinicalTrials.gov may support a sponsor-condition-site network extension:

https://clinicaltrials.gov/data-api/about-api

The alternate case is not required, downloaded, or redistributed in version 0.1.0.

### Provenance requirement

Every learner submission copies the source URL, retrieval date, archive checksum, released-table checksums, selection logic, and synthetic-data statement.

## 8. Data release and transformation contract

### Released tables

| Table | Rows | Columns | Grain |
|---|---:|---:|---|
| Patient source selection | 1,171 | 6 | One synthetic patient. |
| Encounter source selection | 53,346 | 9 | One synthetic encounter. |
| Teaching cohort | 374 | 25 | One adult synthetic patient and one index event. |
| Edge audit | 15 | 9 | One aggregate directed edge. |

### Patient release checksum

`a208fe4ff6fc9dc5cee4a201043a2f059943b8c058fdb191e19b0f9ffbb821bf`

### Encounter release checksum

`00298bf68f89dee9734cf133c516ad6b7efe95c8cd15a9458e7fb09c1dca56ce`

### Cohort release checksum

`b3f1cf69a54fd2f38dfe6debfd009ebb1c7d2b1ef7b42d7b35c989a9f068f3ca`

### Edge release checksum

`13ee29b6fb6e16235cb3b9509d72f95a6b478024a7322d011bb04a4e8064fa8d`

### Cohort algorithm

1. Sort encounters by patient, start timestamp, and encounter ID.
2. Find emergency and inpatient encounters from 2015-01-01 through 2019-12-31.
3. Calculate completed age at encounter start.
4. Keep candidates for patients age 18 or older.
5. Select the first qualifying encounter per patient.
6. Search encounters starting after index stop.
7. Assign the first qualifying encounter within 30 days to a teaching state.
8. If none exists, assign `No encounter recorded`.
9. Search 90 days for any emergency or inpatient return.
10. Check the synthetic death date.
11. Assign one mutually exclusive endpoint with death precedence.
12. Compute path counts and rates.
13. Apply the declared teaching screen.
14. Aggregate adjacent-stage edges.
15. Verify conservation.

### Date boundary

The first next encounter must start after index stop. This avoids counting the index event or a concurrent row as follow-up.

### Class grouping

- Ambulatory, outpatient, wellness: Scheduled care.
- Urgent care: Urgent care.
- Emergency, inpatient: Acute return.
- No qualifying row: No encounter recorded.

### Endpoint precedence

Death within 90 days is the terminal endpoint even if an acute return also occurred. The separate acute-return flag preserves that audit information.

### Screen formula

```text
path_count >= 20
and
path_acute_return_pct > cohort_acute_return_pct
```

No statistical significance or clinical importance is implied.

## 9. Worked synthetic transition case

### Cohort facts

- 374 adult synthetic patients.
- 314 emergency index encounters.
- 60 inpatient index encounters.
- One index event per person.

### Thirty-day state facts

- 263 no encounter recorded.
- 92 scheduled care.
- 15 acute return.
- 4 urgent care.

### Ninety-day endpoint facts

- 330 no acute return within 90 days.
- 36 acute return within 90 days.
- 8 death within 90 days.

### Why 15 and 36 differ

Fifteen is the count whose first next encounter within 30 days is acute. Thirty-six is the count with any acute encounter within 90 days. These are different definitions and cannot share a label.

### Seven observed paths

- Emergency -> No encounter recorded: 225.
- Emergency -> Scheduled care: 73.
- Inpatient -> No encounter recorded: 38.
- Inpatient -> Scheduled care: 19.
- Emergency -> Acute return: 12.
- Emergency -> Urgent care: 4.
- Inpatient -> Acute return: 3.

### Reference screen result

The inpatient-to-no-encounter-recorded path has 38 people, 6 acute returns within 90 days, and a 15.8% path percentage. The full cohort percentage is 9.6%.

### Interpretation

The path is worth auditing because it meets the declared screen and because its absence state needs careful definition. The data do not show that follow-up failed.

### Questions for a production owner

- Does the real source capture outside-network care?
- Are encounter classes consistent across facilities?
- Is discharge time reliable?
- What counts as planned follow-up?
- How are transfers represented?
- What is the observation completeness window?
- How are deaths linked?
- Should index events be episodes rather than single encounters?
- What exclusions and risk adjustment apply?

## 10. Visual selection framework

### Alluvial flow

Use when:

- the unit is conserved;
- there are few ordered stages;
- states are mutually exclusive at each stage;
- path shape matters; and
- approximate volume is sufficient in the figure.

Do not use when:

- units can appear in several states simultaneously;
- denominators change without a nested cohort;
- there are too many paths;
- exact comparison is primary; or
- a table is clearer.

### Funnel

Use only when stages are ordered and nested, such as eligible, contacted, enrolled, completed. A funnel is misleading when each percentage uses a different eligible population.

### Transition or adjacency matrix

Use when origin-destination cells, sparse combinations, and exact within-origin percentages matter. The matrix is often better than a node-link diagram.

### Node-link diagram

Use when topology, paths, neighborhoods, bridges, or connected components are the decision task. Define every node and edge first. Filter or aggregate when the result becomes a hairball.

### Stacked composition

Use when the question is part-to-whole within a small number of groups. State the whole and denominator of each bar.

### Tree or hierarchy

Use for real parent-child nesting. An indented table may outperform a tree when exact labels and values matter.

### Treemap

Use when approximate area comparison supports the task and categories are genuinely nested. Do not let area encode volume while a prominent label invites the audience to read area as a rate.

### Ordinary table

Use when the audience needs exact lookup, when there are few paths, or when multiple definitions must remain visible. Special chart types are not a default achievement.

## 11. Teaching sequence and facilitation

### Opening

Show an unlabeled Sankey and ask what one ribbon unit means. Reveal that the source mixed visits, patients, and percentages. Use the failure to establish the structure-definition requirement.

### Concept core

Teach in this order:

1. unit;
2. cohort;
3. stage;
4. state;
5. node;
6. edge;
7. path;
8. denominator;
9. conservation;
10. display choice.

### Source trace

Trace one patient from the patient table through sorted encounters into the cohort row and aggregate edges.

### Reference comparison

Place the flow, matrix, and composition view side by side. Ask what each makes easy and what it hides.

### Critique

Learners repair changing denominators, a network hairball, and a treemap with conflicting encodings.

### Build

Learners create the complete package at Run, Modify, or Author scaffold level.

### Close

Peers verify conservation and read the text alternative without seeing the figures.

## 12. Reproducible lab contract

### Inputs

- `synthea_acute_transition_cohort_2020.csv`.
- `synthea_transition_edges_2020.csv` for audit.

### Required outputs

- `01-defined-cohort-flow.png`.
- `02-transition-matrix.png`.
- `03-endpoint-composition.png`.
- `transition-path-decision-table.csv`.
- `alt-text-reference.md`.

### Flow requirements

- Three stages.
- Same 374 people at each stage.
- Ribbon width encodes count.
- Index class has color and text labels.
- Every node shows count.
- Title states a supported finding.
- Caption states cohort and simulation boundary.

### Matrix requirements

- Rows are index class.
- Columns are thirty-day state.
- Cells show count and percentage within index class.
- Empty combinations remain visible.
- Denominator direction is stated.

### Composition requirements

- Bars are index class.
- Segments are mutually exclusive endpoints.
- Each bar sums to 100%.
- Count and percentage labels appear when space permits.
- Death precedence is stated.

### Exact table requirements

All seven paths and both path and cohort percentages are present.

### Dependencies

- Python 3 standard library for build and validation.
- R 4.6.1 tested.
- ggplot2 4.0.3 tested.
- No new flow, network, or geospatial package.

### Rebuild commands

```powershell
python courses/data-visualization/modules/11-flow-networks-composition-hierarchy/build_transition_case.py
python courses/data-visualization/modules/11-flow-networks-composition-hierarchy/validate_transition_case.py
Rscript courses/data-visualization/modules/11-flow-networks-composition-hierarchy/lab.R --output "$env:TEMP\oclc-da730-m11-lab"
```

## 13. Critique and repair set

### C1: changing denominator flow

The flawed display labels 500 eligible as 100%, 420 reached as 84%, 290 completed as 69%, and 86 positive as 30%. The 30% uses completed as its base while the earlier percentages use eligible.

Learners must:

- write every numerator and denominator;
- decide whether stages are nested;
- recalculate from a stable cohort or label each base;
- choose a table or ordinary bars if a funnel implies false conservation; and
- state the supported action.

### C2: node-link hairball

The flawed display has 22 nodes and many unlabeled edges.

Learners must define:

- node type;
- edge type;
- direction;
- weight;
- time interval;
- duplicates;
- task; and
- whether a matrix or edge list is superior.

### C3: treemap area-rate conflict

The flawed treemap uses area for service volume and color plus labels for a rate. The largest service has the lowest rate.

Learners must separate the questions and propose:

- an ordered rate dot plot with volume labels;
- coordinated count and rate bars;
- a table; or
- another structure with unambiguous encodings.

### Critique pass standard

A repair must correct the data definition, not only change the color or title.

## 14. Assessment and checkpoint contribution

### Submission package

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

### Rubric dimensions

- decision and action boundary;
- cohort and unit;
- node, edge, and conservation definitions;
- denominator and rate accuracy;
- visual selection;
- reproducibility;
- accessibility;
- interpretation and ethics;
- provenance; and
- AI-use documentation.

### Required threshold

The learner must score at least 80 of 100 and meet all noncompensable pass conditions.

### Noncompensable conditions

- One patient per index cohort row.
- Stage totals equal 374.
- Exact denominator for 15.8%.
- No real-world quality claim.
- No claim that absent row means absent care.
- Reproducible source.
- Source record and accessible alternative.

### Week-6 checkpoint contribution

Module 11 contributes evidence that the learner can define and audit a complex structure. Module 12 adds coordinated monitoring. Checkpoint 2 packages the applied visualization work at the end of week 6.

## 15. Accessibility and equivalent communication

### Visual requirements

- Labels do not depend on color.
- Node counts are printed.
- Reading order is left to right.
- Small ribbons do not carry essential labels.
- Contrast meets course standards.
- Matrix cells carry exact count and percentage.
- Composition values remain available in a table.

### Text alternative requirements

The alternative must state:

- 374-person cohort;
- 314 emergency and 60 inpatient index events;
- all four thirty-day state totals;
- all three ninety-day endpoint totals;
- reference path denominator and percentage;
- full cohort percentage;
- meaning of ribbon width;
- meaning of no encounter recorded; and
- synthetic-data boundary.

### Cognitive accessibility

Use stable state names across figures and prose. Do not alternate among follow-up absent, lost, failed, missing, and no care. The released phrase is `No encounter recorded`.

### Exact-value fallback

Every visual submission includes the seven-row path table.

## 16. Ethics, equity, privacy, and language

### Synthetic does not mean consequence-free

The records are simulated, but the language habits will transfer to real clinical work. Learners must practice purpose limitation, clear absence definitions, and non-stigmatizing interpretation.

### Required language

Prefer:

- no encounter recorded in this extract;
- simulated pathway;
- selected for definition audit;
- requires confirmation in a real data system; and
- cannot estimate real care quality.

Avoid:

- lost patient;
- failed follow-up;
- noncompliant patient;
- poor-performing pathway;
- preventable return; and
- real readmission rate.

### Subgroup fields

Race, ethnicity, and sex remain in the source selection for provenance and optional missingness audit. They are not used to rank pathways. Small synthetic subgroup cells do not support equity conclusions.

### Privacy habit

The Commons omits unused synthetic names, addresses, and identifier-like fields. Learners document the minimization choice even though no real person is represented.

### Real-data transfer

A production version would require governance, privacy review, cohort validation, data-completeness assessment, small-cell rules, clinical review, and appropriate legal authority.

## 17. AI-use contract

### Permitted uses

- explain code;
- suggest a chart alternative;
- help debug a join or date calculation;
- draft alt text for learner verification;
- identify possible denominator ambiguity; and
- improve prose clarity.

### Prohibited substitution

AI output cannot replace:

- source verification;
- cohort uniqueness check;
- conservation proof;
- denominator calculation;
- source-rights review;
- clinical interpretation; or
- learner defense.

### Required record

The learner records:

- tool and model when known;
- date;
- prompt or task;
- output used;
- material revisions;
- values checked; and
- final responsibility statement.

### Verification questions

- Did the AI treat encounters as people?
- Did it invent a Synthea field?
- Did it call the synthetic result a readmission rate?
- Did it drop no-record states?
- Did it suggest a Sankey without conservation?
- Did it change a denominator silently?

## 18. Instructor implementation and answers

### Instructor preparation

1. Run the validator.
2. Run the lab and critiques.
3. Inspect all six figures.
4. Confirm the seven-row table.
5. Trace one patient.
6. Review the source record.
7. Prepare one local example of changing denominators.

### Reference outputs

The lab produces:

- one proportional alluvial flow;
- one two-by-four transition matrix;
- one two-bar endpoint composition;
- one exact path table; and
- one text alternative.

### Core answer

The reference screen selects inpatient to no encounter recorded for a definition audit. The decision note should recommend checking observation completeness, transfer handling, follow-up class definitions, and whether real systems capture outside-network care.

### Answer boundary

The learner must not recommend a quality intervention from the synthetic percentage alone.

### Common recovery moves

If the flow does not conserve, return to the cohort table. If the matrix rates do not sum to 100% within a row, inspect the row denominator. If the composition omits death, inspect endpoint precedence. If the figure is crowded, use the table.

### Independent instructor test

An instructor unfamiliar with the build should be able to regenerate all outputs from a clean checkout using the README commands and teach the module without relying on undocumented conversation context.

## 19. Technical validation and acceptance tests

### Data checks

The validator must pass 64 checks covering:

- file existence;
- exact row counts;
- exact column counts;
- exact SHA-256 values;
- patient uniqueness;
- encounter uniqueness;
- patient joins;
- removed direct identifier-like fields;
- known encounter classes;
- UTC timestamps;
- nonnegative duration;
- adult eligibility;
- index window;
- one index per patient;
- state vocabulary;
- endpoint vocabulary;
- death precedence;
- next-event interval;
- path labels;
- measured counts;
- path denominators;
- percentage values;
- reference screen;
- edge uniqueness;
- stage conservation; and
- node conservation.

### Lab checks

- Three PNG files exist and are nonempty.
- Decision table has seven rows.
- Text alternative exists and is nonempty.
- R exits successfully without a new package.

### Critique checks

- Three PNG files exist and are nonempty.
- Each flaw is deliberate and described in instructor notes.

### Visual inspection

Review title, labels, stage order, ribbon conservation, empty matrix cell, stacked-bar total, captions, contrast, clipping, and critique legibility.

### Repository checks

- JSON parses.
- JavaScript syntax passes.
- Curriculum checker passes.
- `git diff --check` passes.
- No local absolute path appears in public documentation.
- No Unicode em dash or en dash appears in the module contract.
- No temporary outputs or bytecode directories are committed.

## 20. Release, review, and change control

### Release status

Version 0.1.0 is a runnable release candidate in Commons 0.22.0.

### Completed review

Technical build, validator execution, lab execution, critique execution, and visual inspection are complete.

### Required human roles

- transitions-of-care relevance;
- Synthea source fidelity;
- flow and network visualization;
- equity and synthetic-data language;
- accessibility; and
- independent teachability.

### Alpha gate

The module cannot become alpha until named reviewers record decisions and material findings are resolved.

### Version policy

- Patch: wording, typo, or noncontractual correction.
- Minor: cohort, source, assessment, output, or competency-compatible change.
- Major: incompatible decision, unit, source, learning outcome, or submission contract.

### Source refresh

A refresh requires new checksums, measured facts, validator expectations, visual outputs, version, review record, and data-source register entry.

### Known limits

- Simulated data only.
- Older reproducible sample.
- No empirical quality estimate.
- No risk adjustment.
- No outside-network capture concept.
- Reference screen is a teaching rule.
- Human review remains pending.
- Clean-run testing is currently Windows only.

## 21. Handoff to Module 12

Module 11 hands Module 12:

- a named decision owner;
- one-row-per-person cohort;
- explicit index and observation windows;
- stable state vocabulary;
- exact counts and denominators;
- a source record and checksums;
- a flow, matrix, composition view, and table;
- accessibility and text-alternative requirements;
- a precise absence definition;
- a synthetic-data boundary; and
- a definition-audit action.

Module 12 must decide which of these views belongs in a monitoring display. It must not place every available chart on a dashboard.

### Module 12 questions

- Who monitors the process?
- What exception requires action?
- Which one to four views are necessary?
- What refresh cadence matches the decision?
- Which thresholds are descriptive, operational, or validated?
- How does the user move from overview to exact records?
- What does the dashboard say when data are stale or incomplete?

### Final boundary

Module 11 ends when the structure is defined, conserved, reproducible, accessible, and tied to a modest decision. Module 12 begins when several stable views must be coordinated for ongoing monitoring.

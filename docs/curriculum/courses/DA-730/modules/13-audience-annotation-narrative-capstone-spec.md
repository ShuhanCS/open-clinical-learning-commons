# DA-730 Module 13 specification: Audience, annotation, narrative, and capstone

Status: runnable release candidate
Module version: 0.1.0
Commons release: 0.25.0
Course owner: Ali Goff
Curriculum sponsor: Shuhan He
Technical package: `courses/data-visualization/modules/13-audience-annotation-narrative-capstone/`
Module hours: 16.5
Week: 7

## 1. Purpose, scope, and ownership

Module 13 teaches learners to turn one stable evidence chain into a decision story for two audiences without changing the source values, definitions, uncertainty, freshness, or action boundary.

The central question is not, How can I make this chart more persuasive? It is, What does this audience need first, what evidence must remain visible, and which parts of the analytic truth cannot change?

The module owns:

- audience definition;
- audience authority and task;
- finding-led titles;
- evidence hierarchy;
- annotation purpose;
- primary and supporting views;
- visual sequence;
- executive and technical adaptation;
- decision briefs;
- explicit requests and action ownership;
- narrative integrity;
- stable analytic invariants;
- accessible decision stories;
- transformation records;
- reproducibility checks;
- critique responses;
- capstone packaging;
- oral defense; and
- final course handoff.

The module does not own:

- changing source values to strengthen a story;
- hiding uncertainty or missingness;
- replacing a decision with advocacy alone;
- causal inference not supported by the design;
- real-time operations from historical public data;
- production clinical implementation;
- approval to use restricted patient records;
- live data-system integration;
- institutional communications approval;
- a requirement to use one presentation product; or
- a requirement to create more than one supporting figure.

### Required intellectual move

Before adapting a figure, the learner writes two lists:

1. what may change for the audience; and
2. what must remain invariant.

The learner then proves that every changed title, annotation, sequence, and explanation preserves the evidence chain.

### Completion standard

The module is complete when the learner can produce and defend two audience-specific figures from one reproducible analysis, preserve exact values and definitions, provide an accessible table and alternative, state one material limitation, request one defensible action, and answer questions without expanding the claim.

## 2. Healthcare decision and two audiences

### Stable decision

Authorize a local definition and current-data review for a historical public CMS emergency department signal.

### Primary audience

Emergency department quality director.

The quality director needs:

- exact measure identities;
- units and directions;
- selected values;
- source samples;
- reporting windows;
- source lag;
- descriptive peer context;
- mock-trigger origin;
- trigger results;
- ordered validation actions; and
- a boundary on operational use.

### Secondary audience

Hospital quality committee.

The committee needs:

- one supported finding;
- why it matters now;
- why the evidence is not current performance;
- the first action requested;
- who owns the action;
- what evidence comes back for review; and
- what the committee should not conclude.

### Stable supported action

1. Validate the CMS-to-local numerator, denominator, exclusions, and source completeness.
2. Pull current local monthly OP-22 and emergency department time data.
3. If the current signal persists, review arrival, triage, staffing, capacity, communication, and access conditions.
4. Record the owner, action, evidence, and next review date.

### Stable unsupported actions

Neither audience version supports:

- calling the public value current performance;
- changing staffing from the public value alone;
- changing clinical care from the public value alone;
- identifying a cause;
- rating overall hospital quality;
- treating the Massachusetts median as a benchmark;
- treating a course trigger as a CMS threshold;
- claiming intervention effectiveness; or
- blaming patients or clinicians.

### Audience adaptation question

What can become shorter, more direct, or more detailed without changing the evidence or the decision boundary?

## 3. Competency and learning outcomes

### Competency

Produce and defend a sourced, reproducible, accessible visualization package that communicates one stable finding and recommendation to two named healthcare audiences.

### Learning outcomes

By the end of the module, learners can:

1. name an audience as a person or authorized group;
2. state what the audience controls;
3. state the decision before writing the title;
4. distinguish a finding from an interpretation;
5. distinguish an interpretation from a recommendation;
6. distinguish a recommendation from an authorized action;
7. write a finding-led title;
8. select one primary figure;
9. add one supporting figure only for a different question;
10. remove evidence that does not serve the decision;
11. retain evidence that prevents a misleading conclusion;
12. use annotation to explain rather than exaggerate;
13. preserve units, denominators, windows, samples, and uncertainty;
14. preserve missingness and footnotes;
15. preserve threshold origin and ownership;
16. preserve source and rights records;
17. adapt technical depth without changing values;
18. write a concise decision brief;
19. state one material limitation once and clearly;
20. create an exact accessible table;
21. write an equivalent text alternative;
22. document every material transformation;
23. rerun the package from a clean checkout;
24. document AI assistance and verification;
25. critique causal, freshness, and annotation failures;
26. respond to critique without expanding the claim;
27. prepare a short oral defense;
28. answer questions with source evidence; and
29. package the final half-term checkpoint.

### Mastery evidence

Mastery requires a primary figure, one justified supporting figure, exact table, text alternative, editable analysis, source record, transformation record, audience-adaptation record, decision brief, reproducibility check, critique response, AI-use record, slides, and written question responses.

## 4. Prerequisites and checkpoint handoff

### Required prerequisites

Learners must complete Modules 01 through 12 and Checkpoints 1 and 2.

### Inherited competencies

Module 13 assumes learners can:

- map data to visual channels;
- evaluate perceptual accuracy;
- select a chart, table, multiple views, or no display;
- expose distributions hidden by summaries;
- distinguish counts, rates, denominators, and adjustment;
- communicate uncertainty and small-number status;
- use color with redundant cues;
- distinguish time pattern from process inference;
- compare many groups on stable scales;
- decide when geography adds value;
- define and conserve flows and hierarchies; and
- compose a minimum decision dashboard.

### Checkpoint 2 input contract

The approved capstone proposal supplies:

- decision owner;
- secondary audience;
- decision question;
- source and rights;
- population and unit;
- time window;
- measures and definitions;
- planned analysis;
- primary and supporting display plan;
- accessible-table plan;
- text-alternative plan;
- reproducibility plan;
- ethics and equity boundary;
- expected limitation;
- deliverables;
- review date; and
- review conditions.

### Reference-case handoff

The runnable reference uses the released Module 12 CMS public-reporting data. It does not create a new clinical data source or silently refresh the upstream release.

### Misconceptions to diagnose

- A stronger title is a more causal title.
- Executive audiences do not need limitations.
- Technical audiences need every chart.
- Annotation may direct attention away from contradictory evidence.
- A supporting figure can answer the same question as the primary figure.
- Simplification permits changing denominators.
- A story must end in intervention.
- An oral defense rewards confidence more than accuracy.
- A board-ready chart should hide data age.
- A public value becomes current when repeated in a slide.

## 5. Workload and module sequence

The module has 16.5 learner hours within instructional week 7.

| Component | Hours | Evidence |
|---|---:|---|
| Checkpoint 2 feedback and capstone lock | 1.0 | Approved evidence-chain contract. |
| Audience authority and task analysis | 1.0 | Two audience briefs. |
| Finding, interpretation, recommendation, and action | 1.0 | Claim ladder. |
| Title and annotation workshop | 1.0 | Three title and annotation alternatives. |
| Primary and supporting figure selection | 1.0 | View-purpose defense. |
| Reference two-audience lab | 1.5 | Two regenerated figures and exact table. |
| Critique and repair | 1.0 | Three diagnosed story failures. |
| Independent capstone analysis and build | 4.0 | Editable analysis and evidence outputs. |
| Accessibility and exact-value package | 1.0 | Table and equivalent alternative. |
| Decision brief and adaptation record | 1.0 | Audience-specific narrative package. |
| Reproducibility and release check | 1.0 | Clean-run record. |
| Oral defense preparation and rehearsal | 1.0 | Slides and question responses. |
| Final revision and submission | 1.0 | Complete final checkpoint. |
| Total | 16.5 |  |

### Recommended order

1. Resolve Checkpoint 2 conditions.
2. Freeze the source release.
3. Freeze the population, unit, and measures.
4. Freeze the decision and action boundary.
5. Name both audiences and their authority.
6. Write the stable finding.
7. Select the primary figure.
8. Decide whether a supporting figure answers a different question.
9. Write the invariant list.
10. Draft audience-specific titles and annotations.
11. Build both versions from one analysis.
12. Compare every number with the exact table.
13. Write the accessible alternative.
14. Complete the transformation and adaptation records.
15. Run the clean reproduction check.
16. Rehearse the oral defense.
17. Submit on the official last day of the half-term.

### Stop rules

The build pauses when:

- the audience controls nothing relevant to the request;
- the decision is only to raise awareness;
- the finding lacks a source row;
- a title implies cause without a causal design;
- a changed version uses different data;
- a material limit disappears from one audience version;
- the supporting figure repeats the primary question;
- the requested action exceeds the evidence; or
- the clean-run path fails.

## 6. Concept model and vocabulary

### Audience

A named person or authorized group with a task, information need, decision right, and action boundary.

### Reader task

What the audience must notice, compare, verify, decide, explain, or do.

### Finding

A source-supported statement about the observed or modeled evidence.

### Interpretation

An explanation of what the finding may mean within the source and design limits.

### Recommendation

A proposed next step based on the finding and interpretation.

### Authorized action

What the named decision owner may legitimately approve or assign.

### Claim ladder

```text
source value -> finding -> interpretation -> recommendation -> authorized action
```

Each rung requires support. The learner may stop before the next rung when the evidence does not support it.

### Finding-led title

A title that states the strongest supported result and its relevant boundary.

Reference example:

`A historical public OP-22 signal warrants a current local review`

Non-passing example:

`Emergency department performance failure caused by staffing`

### Annotation

Text or graphic guidance that directs attention to evidence, definition, change, threshold, uncertainty, or action.

Annotation must not manufacture importance or hide contradictory evidence.

### Primary figure

The one visual that carries the main decision story.

### Supporting figure

An optional visual that answers a different necessary question. It is not a second attempt to show the same result.

### Invariant

An element that cannot change across audience versions without changing the evidence or claim.

### Adaptable element

An element that may change to fit audience task, knowledge, time, or delivery context while preserving the invariants.

### Decision brief

A concise record of audience, finding, evidence, requested decision, action owner, limitation, and review plan.

### Material limitation

A limit that changes what the reader should conclude or do.

### Transformation record

A complete account of source selection, calculation, recoding, filtering, ordering, annotation, and export.

### Reproducibility check

Evidence that a new user can regenerate the submitted outputs from committed source and code.

### Oral defense

A structured explanation and question response in which the learner connects claims to source evidence and refuses unsupported expansion.

## 7. Public sources, rights, and provenance

### Reused primary source

Publisher: Centers for Medicare & Medicaid Services.

Dataset: Timely and Effective Care - Hospital.

Dataset ID: `yv7e-xc69`.

Landing page:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

Complete pinned CSV:

https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv

Hospital data dictionary:

https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf

Measure-period page:

https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods

### Upstream teaching release

Main teaching table:

`courses/data-visualization/modules/12-dashboards-multi-view-composition/data/ma_ed_public_reporting_dashboard_2026.csv`

Rows: 186.

Columns: 31.

SHA-256: `fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd`.

Measure dictionary:

`courses/data-visualization/modules/12-dashboards-multi-view-composition/data/ed_dashboard_measure_dictionary_2026.csv`

Rows: 3.

Columns: 18.

SHA-256: `2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412`.

Source selection:

`courses/data-visualization/modules/12-dashboards-multi-view-composition/data/cms_ma_ed_dashboard_source_2026.csv`

Rows: 186.

Columns: 15.

SHA-256: `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b`.

### Source release fingerprint

| Property | Value |
|---|---|
| CMS release date | 2026-08-13 |
| Complete rows | 138,084 |
| Complete columns | 16 |
| Complete bytes | 34,150,899 |
| SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |

### Rights

CMS Provider Data Catalog records are public U.S. government reporting data. Attribution is preserved and reuse does not imply federal endorsement.

Commons documentation uses CC BY 4.0. Commons code uses MIT.

### Provenance rule

Audience adaptation cannot alter the source fingerprint. If the learner refreshes or replaces the source, the work becomes a new release and requires a new source record, measured facts, validation, interpretation, and review.

### Data minimization

The reference analysis uses public facility name, city, state, county, measure identity, score, sample, footnote, period, release date, and derived teaching fields. Street address, ZIP code, and telephone number remain omitted because the decision does not need them.

## 8. Evidence chain and invariant contract

### Stable selected facility

Facility: Anna Jaques Hospital.

CMS facility ID: `220029`.

### Stable exact values

| Measure | Value | Unit | Sample | Reporting period | Lag at release |
|---|---:|---|---:|---|---:|
| EDV | Low | CMS category | Not applicable | 2024-01-01 through 2024-12-31 | 590 days |
| OP_18b | 188 | minutes | 422 | 2024-10-01 through 2025-09-30 | 317 days |
| OP_22 | 23 | percent | 19,211 | 2024-01-01 through 2024-12-31 | 590 days |

### Stable peer context

- OP_18b reported hospitals: 54.
- OP_18b Massachusetts median: 211.5 minutes.
- OP_18b selected unfavorable rank: 45.
- OP_22 reported hospitals: 53.
- OP_22 Massachusetts median: 3 percent.
- OP_22 selected unfavorable rank: 1.

### Stable scenario triggers

- OP_18b mock review trigger: at or above 240 minutes, not crossed.
- OP_22 mock review trigger: at or above 10 percent, crossed.

The triggers remain labeled as mock quality-improvement charter assumptions, not CMS thresholds.

### Stable finding

The historical public OP-22 signal is sufficient under the course scenario to open a local definition and current-data review.

### Stable material limitation

The OP-22 reporting period ended 590 days before the CMS release. The public value cannot establish current operational performance.

### Stable action boundary

The first action is validation and current local data. The public value alone does not authorize intervention.

### Elements that may change

- title length;
- subtitle detail;
- annotation density;
- evidence order;
- label vocabulary;
- peer-detail depth;
- footnote placement;
- figure aspect ratio;
- supporting prose length; and
- presentation sequence.

### Elements that may not change

- source release;
- selected facility;
- measure values;
- units;
- samples;
- reporting windows;
- release date;
- lag;
- peer medians;
- reported counts;
- threshold values;
- threshold origin;
- trigger results;
- finding;
- material limitation;
- supported action; and
- unsupported actions.

## 9. Worked two-audience decision story

### Technical version

Audience: emergency department quality director.

Primary question: Which public signal requires validation, and what exact evidence should the local team check first?

The technical figure shows:

- all reported Massachusetts OP-22 values;
- selected 23-percent value;
- 3-percent descriptive median;
- mock 10-percent review trigger;
- 53 reported hospitals;
- reporting period;
- 590-day source lag;
- non-CMS trigger label; and
- ordered validation action.

The supporting evidence keeps OP_18b and EDV in the exact table rather than adding another peer panel to the primary story.

### Executive version

Audience: hospital quality committee.

Primary question: What action should the committee authorize, and why is the action review rather than intervention?

The executive figure shows:

- one finding-led title;
- 23-percent public OP-22 value;
- 590-day lag;
- one sentence on peer context;
- one explicit non-CMS threshold boundary;
- one action request; and
- one next-review requirement.

### What changes

The technical version provides peer distribution, reported count, exact reference lines, and definition-first action detail.

The executive version provides the stable finding, evidence age, requested authorization, owner, and return evidence with less analytic density.

### What stays stable

Both versions state:

- 23 percent;
- OP-22 unit and meaning;
- historical public reporting;
- 2024 reporting window;
- 2026-08-13 release;
- 590-day lag;
- descriptive peer context;
- mock-trigger status;
- definition and current-data review; and
- no current performance or intervention claim.

### Reference recommendation

Authorize the emergency department quality director to validate the measure definition and return with current local monthly OP-22 and emergency department time evidence before any operational change is considered.

## 10. Audience, title, annotation, and sequence framework

### Audience brief

For each audience, complete:

| Field | Required statement |
|---|---|
| Audience | One person or authorized group. |
| Authority | What the audience may approve or assign. |
| Task | What the audience must notice, compare, verify, or decide. |
| Prior knowledge | Definitions or context that may be assumed. |
| Time available | Realistic reading or presentation time. |
| Required evidence | What cannot be omitted. |
| Avoided detail | What belongs in a table, note, or appendix. |
| Requested action | One bounded next step. |

### Claim ladder worksheet

| Rung | Reference statement |
|---|---|
| Source value | CMS reports OP-22 at 23 percent for the selected period. |
| Finding | The value is the highest observed among 53 reporting Massachusetts hospitals and crosses the mock course trigger. |
| Interpretation | The historical signal warrants validation but does not establish current performance. |
| Recommendation | Open a local definition and current-data review. |
| Authorized action | Assign the quality director to return with current local evidence. |

### Title test

A title passes when it:

- states a supported finding;
- includes the key boundary when omission would mislead;
- uses audience vocabulary;
- does not imply cause;
- does not convert a scenario trigger into policy; and
- aligns with the requested action.

### Annotation test

Every annotation must answer one question:

- What is the key value?
- What is the comparison?
- What is the definition?
- What is the time boundary?
- What is the threshold origin?
- What happens next?

Delete annotations that only repeat the title, add drama, or direct attention away from a material limit.

### Primary-figure test

The primary figure must carry the finding and decision by itself when accompanied by its title, source line, and accessible alternative.

### Supporting-figure test

A supporting figure is allowed only when it answers a different question needed for the decision.

Reference technical question: Where is the selected value among reporting peers?

Reference executive question: Why is the immediate action validation rather than intervention?

The executive version is an audience adaptation, not an additional analytic claim.

### Sequence test

Use this order:

1. finding;
2. evidence;
3. boundary;
4. requested decision;
5. owner and next review.

Do not lead with methods unless the audience task is method approval.

## 11. Teaching sequence and facilitation

### Opening prompt

Ask: Which sentence must remain true in both audience versions?

If learners name a style preference rather than an evidence statement, return to the invariant contract.

### Activity 1: audience authority

Learners compare an emergency department quality director with a hospital quality committee. They state what each can approve, what each needs to verify, and what neither can conclude.

### Activity 2: claim ladder

Learners separate the source value, finding, interpretation, recommendation, and authorized action. They identify where a causal or current-performance claim would exceed the source.

### Activity 3: title ladder

Learners write:

- an axis-label title;
- a descriptive title;
- a finding-led title;
- an overclaimed title; and
- a corrected finding-led title.

### Activity 4: annotation audit

Learners label each annotation as value, comparison, definition, time, threshold, or action. Unclassified annotation is removed or justified.

### Activity 5: reference lab

Learners regenerate both audience figures, exact table, accessible alternative, audience-adaptation record, and decision brief.

### Activity 6: invariant comparison

Learners compare every displayed number and claim across both outputs. Any unexplained difference fails the exercise.

### Activity 7: critique and repair

Learners repair causal title, hidden-freshness, and annotation-misdirection examples.

### Activity 8: independent capstone build

Learners apply the framework to the approved Checkpoint 2 proposal.

### Activity 9: peer redelivery

One learner presents the technical version in four minutes. A peer presents the executive version in two minutes. The source and action boundary must remain identical.

### Activity 10: defense rehearsal

Peers ask about source, denominator, missingness, uncertainty, alternative displays, accessibility, causality, equity, action, and refresh.

### Facilitation principle

Treat audience adaptation as evidence-preserving translation, not persuasion detached from the source.

## 12. Reproducible lab contract

### Inputs

- Module 12 `ma_ed_public_reporting_dashboard_2026.csv`.
- Module 12 `ed_dashboard_measure_dictionary_2026.csv`.

### Required outputs

- `01-technical-decision-story.png`.
- `02-executive-decision-story.png`.
- `decision-story-table.csv`.
- `alt-text-reference.md`.
- `audience-adaptation-reference.md`.
- `decision-brief-reference.md`.

### Technical figure requirements

- Emergency department quality director named.
- OP-22 peer distribution retained.
- Selected 23-percent value directly labeled.
- 3-percent Massachusetts median directly labeled as descriptive.
- Mock 10-percent trigger labeled as non-CMS.
- 53 reported hospitals stated.
- Reporting window stated.
- 590-day lag stated.
- Validation action stated.
- No current performance claim.

### Executive figure requirements

- Hospital quality committee named.
- Finding-led title.
- 23-percent value.
- 590-day lag.
- Historical public-reporting label.
- One bounded authorization request.
- Quality director as owner.
- Current local data as return evidence.
- No intervention claim.

### Exact table requirements

The table contains exactly three selected-facility rows and preserves:

- measure ID;
- display label;
- raw value;
- numeric value;
- unit;
- sample;
- value status;
- footnote;
- period start;
- period end;
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

### Adaptation record requirements

The reference record compares:

- audience;
- authority;
- reader task;
- title;
- evidence retained;
- evidence moved to table or note;
- annotation density;
- requested action;
- material limitation; and
- invariants checked.

### Decision brief requirements

The reference brief names both audiences, stable finding, evidence, requested decision, action owner, return evidence, material limitation, and unsupported conclusion.

### Dependencies

- Python 3 standard library for validation.
- R 4.6.1 tested.
- ggplot2 4.0.3 tested.
- Base R grid for composition.
- No presentation or dashboard package.

### Validation command

```powershell
python courses/data-visualization/modules/13-audience-annotation-narrative-capstone/validate_decision_story_case.py
```

### Lab command

```powershell
Rscript courses/data-visualization/modules/13-audience-annotation-narrative-capstone/lab.R --output "$env:TEMP\oclc-da730-m13-lab"
```

### Critique command

```powershell
Rscript courses/data-visualization/modules/13-audience-annotation-narrative-capstone/critique_charts.R --output "$env:TEMP\oclc-da730-m13-critiques"
```

## 13. Critique and repair set

### C1: overstated causality

The flawed title states that staffing caused patients to leave before being seen. The public aggregate source contains no staffing exposure, causal design, or current local series.

Learners must:

- identify the unsupported causal rung;
- restore the public source value and period;
- rewrite the title as a supported finding;
- narrow the action to validation and current data;
- state which evidence would be needed for a staffing claim; and
- preserve non-blaming language.

### C2: hidden freshness

The flawed executive card labels 23 percent as current and removes the 2024 reporting window, 2026 release date, and 590-day lag.

Learners must:

- restore the source window;
- restore release date and lag;
- change the use label to historical public reporting;
- suppress operational recommendations;
- request current local evidence; and
- explain why a timestamp alone is not enough.

### C3: annotation misdirection

The flawed figure uses a large arrow and alarm language to amplify the selected value while placing the non-CMS trigger and freshness limit in unreadable text.

Learners must:

- classify every annotation;
- restore hierarchy to the decision-relevant evidence;
- directly label the threshold origin;
- make the freshness boundary readable;
- remove dramatic but unsupported language;
- retain exact peer context; and
- state the supported action.

### Critique pass standard

A repair must correct the claim and evidence contract. A new color, font, or layout without a corrected claim does not pass.

### Critique outputs

- `C1-overstated-causality.png`.
- `C2-hidden-freshness.png`.
- `C3-annotation-misdirection.png`.

## 14. Assessment and final checkpoint contribution

### Submission package

```text
module-13/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis.R
  source-record.yml
  transformation-record.md
  audience-adaptation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  defense/
    slides.pdf
    questions-and-responses.md
```

### Primary figure

The primary figure carries the main finding and requested decision.

### Supporting figure

The supporting figure answers a different necessary question. The learner may omit it with an approved `not needed` record when the primary figure and exact table fully support the decision.

### Decision brief

The brief contains 600 to 900 words and includes:

- audience;
- finding;
- evidence;
- requested decision;
- action owner;
- next review;
- uncertainty or freshness;
- material limitation; and
- unsupported conclusion.

### Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Audience, authority, and decision | 10 | Two named audiences, one stable decision, and realistic authority. |
| Finding and claim integrity | 15 | Finding, interpretation, recommendation, and action remain supported and separate. |
| Primary and supporting views | 15 | Primary figure carries the decision; supporting figure answers a different question. |
| Audience adaptation | 10 | Adaptable elements change while all invariants remain stable. |
| Annotation and narrative sequence | 10 | Title and annotations guide attention to value, boundary, and action without distortion. |
| Reproducibility and provenance | 10 | Editable analysis, source record, transformation record, and clean-run evidence are complete. |
| Accessibility | 10 | Exact table, equivalent alternative, redundant cues, hierarchy, and delivery checks. |
| Clinical, ethical, and equity boundary | 10 | No causal, current, stigmatizing, or unauthorized action claim. |
| Critique response and AI record | 5 | Repair and AI verification are specific and evidence-backed. |
| Oral defense | 5 | Learner answers source, method, limit, alternative, action, and access questions without expanding the claim. |
| Total | 100 |  |

### Pass conditions

All are required:

- at least 80 of 100 points;
- two named audiences;
- one stable decision;
- one primary figure;
- no redundant supporting figure;
- exact accessible table;
- equivalent text alternative;
- full source record;
- full transformation record;
- clean reproduction;
- material limitation;
- bounded action;
- complete AI record; and
- completed defense.

### Automatic return conditions

Return without grading when:

- a source value changes across versions;
- the title claims cause without a causal design;
- the public value is called current;
- the mock trigger is called a CMS threshold;
- a peer median is called a benchmark;
- the reporting window or lag is hidden;
- the action jumps to intervention;
- the exact table or alternative is missing;
- the analysis cannot regenerate the figures;
- the supporting figure repeats the primary question;
- the source record is incomplete;
- AI-generated values are not verified; or
- restricted patient data appear in the submission.

## 15. Accessibility and equivalent communication

### Primary-figure requirements

- Finding-led title is readable.
- Essential values are directly labeled.
- Units appear with values.
- Status does not depend on color.
- Selected and reference marks use redundant cues.
- Source and period remain visible.
- Footnotes are readable at the delivery size.
- Meaning survives grayscale.

### Executive-version requirements

- Reading order is obvious.
- One action request is visually clear.
- Evidence age is not buried.
- Large type does not remove the unit or boundary.
- The owner and return evidence are stated.
- No essential information depends on animation.

### Exact table

Every capstone includes an accessible table containing the values that affect the decision. The table preserves units, samples, status, footnotes, periods, and source.

### Text alternative

The alternative states:

- audience;
- decision;
- figure structure;
- source population;
- strongest finding;
- exact key values;
- comparison reference;
- time or freshness boundary;
- threshold origin when used;
- requested action;
- action owner; and
- unsupported conclusion.

### Two-audience equivalence

Both alternatives preserve the same values, source, finding, material limit, and action boundary.

### Slides

Defense slides require:

- readable title and body type;
- logical reading order;
- one idea per slide;
- direct figure labels;
- speaker explanation of visual content;
- accessible exported PDF when PDF is required; and
- an accessible alternative supplied outside the slides.

### Interaction and motion

An interactive capstone must provide keyboard access, visible focus, non-hover access to essential values, a stable static export, exact table, and text alternative.

## 16. Ethics, equity, privacy, and language

### Narrative power requires restraint

Titles and annotations shape action. A visually accurate figure can still mislead when the story exaggerates cause, hides age, erases missingness, or assigns blame.

### Required language

Prefer:

- historical public reporting signal;
- observed peer position;
- mock review trigger;
- definition and current-data review;
- system conditions requiring review;
- current local evidence; and
- action contingent on validation.

Avoid:

- failing hospital;
- staffing caused the result;
- patients chose not to wait;
- current emergency;
- CMS failure threshold;
- proven intervention need; and
- quality crisis.

### Equity boundary

The facility-level public file contains no subgroup evidence. Neither audience version may imply that the aggregate value describes all racial, ethnic, language, disability, age, payer, clinical, or access groups equally.

The recommended current local review should plan subgroup and access checks when governance and cell sizes permit.

### Patient and clinician respect

Do not blame patients for leaving before being seen or clinicians for a public aggregate value. A real review examines system conditions, data capture, arrival patterns, triage, wait communication, language access, disability access, staffing, and capacity.

### Privacy

The reference uses public aggregate facility data and no patient records.

A learner-selected capstone that introduces patient-level data must stop unless the source is approved synthetic data or an authorized environment outside the public Commons.

### Rights

Every reused image, table, excerpt, and source retains attribution and reuse terms. Public access does not authorize copying third-party copyrighted material.

### Implementation boundary

Final course approval is an educational assessment decision. It is not institutional approval to publish, intervene, deploy, or change care.

## 17. AI-use contract

### Permitted uses

AI may support:

- title alternatives;
- annotation alternatives;
- code explanation;
- debugging;
- layout suggestions;
- draft text alternatives;
- audience-language translation;
- critique prompts;
- defense question generation; and
- prose editing.

### Prohibited substitution

AI cannot replace:

- source verification;
- rights review;
- checksum verification;
- measure definition;
- denominator verification;
- time-window verification;
- threshold origin;
- clinical interpretation;
- audience authority;
- accessibility testing;
- human review; or
- oral defense.

### Required record

The learner records:

- tool and model when known;
- date;
- prompt or instruction;
- generated artifact;
- output used;
- material revisions;
- values checked;
- definitions checked;
- source URLs checked;
- figure inspection;
- accessibility checks;
- human decisions; and
- final responsibility statement.

### Cross-audience AI check

Learners compare AI-assisted versions for:

- changed numbers;
- missing units;
- missing dates;
- stronger causal language;
- invented benchmarks;
- invented thresholds;
- missing limitations;
- different action boundaries;
- stigmatizing language; and
- inaccessible output.

### Defense rule

The learner must be able to explain and defend every submitted AI-assisted sentence and line of code. Unexplained output is not evidence of competence.

## 18. Instructor implementation and answers

### Instructor preparation

1. Run the Module 13 validator.
2. Run the reference lab.
3. Run the critique lab.
4. Inspect all five figures.
5. Compare the two audience figures with the three-row exact table.
6. Compare both text alternatives with the figures.
7. Review the adaptation and decision-brief references.
8. Prepare one learner-specific defense question per rubric dimension.
9. Confirm official final due date.
10. Confirm accessible defense arrangements.

### Reference answer

The historical public OP-22 value is sufficient to authorize a local definition and current-data review. It is not sufficient to judge current performance or authorize intervention.

### Technical-audience answer

The quality director should trace the CMS-to-local numerator, denominator, exclusions, source completeness, and current monthly series. OP_22, OP_18b, and EDV remain available in the exact table.

### Executive-audience answer

The quality committee should authorize the review, assign the quality director, and require current local evidence at the next review before considering an operational change.

### Invariant answer key

Both versions must preserve:

- 23-percent OP-22;
- 19,211 source sample;
- 3-percent Massachusetts median;
- 53 reported hospitals;
- 10-percent mock trigger;
- 2024 reporting period;
- 2026-08-13 release;
- 590-day lag;
- non-CMS trigger origin;
- historical-use label;
- definition and current-data action; and
- no intervention conclusion.

### Common recovery moves

If the title overclaims, return to the claim ladder. If the executive figure hides age, restore the period and lag. If the technical figure is crowded, move exact secondary evidence to the table. If the supporting figure repeats the primary question, remove it. If versions disagree, compare both against the exact table and invariant record. If the action expands during defense, return to the authorized-action rung.

### Defense question bank

1. What is the exact decision?
2. Who can authorize it?
3. Which source row supports the finding?
4. Why is the peer median not a benchmark?
5. Who owns the threshold?
6. Why is the public value not current?
7. What current local data are needed?
8. What changed between audiences?
9. What could not change?
10. Why is the supporting figure necessary?
11. What would make it unnecessary?
12. Which annotation prevents the most serious error?
13. Which subgroup question remains unanswered?
14. Which causal claim is unsupported?
15. How did you verify AI-assisted work?
16. How does a nonvisual reader receive the same finding?
17. What would trigger a source refresh?
18. What action is not authorized?

### Independent instructor test

An instructor unfamiliar with the build can regenerate the outputs, trace every value, teach the audience-adaptation exercise, apply the rubric, and conduct the defense without undocumented conversation context.

## 19. Technical validation and acceptance tests

### Validator checks

The Module 13 validator checks:

- required upstream files;
- exact row counts;
- exact column counts;
- exact SHA-256 values;
- selected-facility row count;
- selected measure IDs;
- selected values;
- samples;
- status;
- reporting periods;
- release date;
- source lag;
- peer reported counts;
- peer medians;
- unfavorable ranks;
- threshold values;
- trigger results;
- trigger origins;
- monitoring-use label;
- action text;
- dictionary units;
- dictionary directions;
- decision owner;
- refresh cadence;
- interpretation limits; and
- cross-audience invariant facts.

### Lab checks

- Two PNG files exist and are nonempty.
- Technical figure is at least 600 by 400 pixels.
- Executive figure is at least 600 by 400 pixels.
- Exact table has three rows.
- Text alternative exists and covers both audiences.
- Adaptation record exists and names changed and invariant elements.
- Decision brief exists and states the stable action and limit.
- R exits successfully without a new package.

### Critique checks

- Three PNG files exist and are nonempty.
- Each failure is deliberate and documented.
- Each repair changes the claim or evidence contract.

### Visual inspection

Review:

- title claim;
- audience label;
- direct values;
- unit;
- peer reference;
- reported count;
- threshold origin;
- reporting window;
- source lag;
- action request;
- owner;
- source line;
- clipping;
- contrast;
- reading order; and
- cross-version invariants.

### Repository checks

- Release JSON parses.
- JavaScript syntax passes.
- Curriculum checker passes.
- `git diff --check` passes.
- No local absolute path appears in public documentation.
- No Unicode em dash or en dash appears in the module contract.
- No unfinished drafting marker remains.
- No temporary output or bytecode directory is committed.

### Acceptance facts

- Upstream teaching rows: 186.
- Selected decision-story rows: 3.
- Audience versions: 2.
- Selected OP-22: 23 percent.
- Selected OP_18b: 188 minutes.
- Maximum source lag: 590 days.
- Mock triggers labeled non-CMS: 2.
- Stable supported action: definition and current-data review.

## 20. Release, review, and change control

### Release status

Version 0.1.0 is a runnable release candidate in Commons 0.25.0.

### Completed review

Technical validation, lab execution, critique execution, output comparison, and visual inspection are complete.

### Required human roles

- DA-730 faculty;
- emergency department quality relevance;
- CMS source fidelity;
- executive communication;
- visualization and information design;
- accessibility;
- equity and action language; and
- independent teachability.

### Alpha gate

The module cannot become alpha until named reviewers record decisions and material findings are resolved.

### Version policy

- Patch: wording, typo, or noncontractual correction.
- Minor: compatible source, lab, assessment, output, critique, or audience expansion.
- Major: incompatible decision, source, learning outcome, audience, submission, or defense contract.

### Upstream change

A change to Module 12 source data requires:

- new source fingerprints;
- new selected facts;
- new validator expectations;
- regenerated figures and table;
- updated adaptations and brief;
- cross-audience invariant audit;
- visual inspection;
- version changes; and
- human review.

### Known limits

- Historical public aggregate data only.
- One reference facility.
- Two professional audiences in the runnable example.
- No real-time operations.
- No subgroup evidence.
- No causal design.
- Mock course triggers.
- Descriptive peer context.
- Human review remains pending.
- Clean-run testing is currently Windows only.

## 21. Final checkpoint and curriculum handoff

### Final checkpoint purpose

The final checkpoint occurs on the official last day of the half-term. It demonstrates the complete DA-730 outcome with one decision-ready release and oral defense.

### Final package

```text
final-capstone/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis/
  data/
  source-record.yml
  transformation-record.md
  audience-adaptation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  defense/
    slides.pdf
    questions-and-responses.md
```

### Final release gate

The final checkpoint must:

- pass the folder validator;
- regenerate from a clean checkout;
- preserve approved source and rights;
- preserve exact values and definitions;
- pass accessibility review;
- preserve the action boundary;
- resolve Checkpoint 2 conditions;
- include instructor and domain review;
- include a complete AI-use record; and
- pass oral defense.

### Handoff to later courses

The final DA-730 release becomes reusable evidence for:

- FND-1 source, table, and provenance work;
- FND-2 inference and reproducibility work;
- APP-1 through APP-7 domain-specific decisions;
- CAP-0 proposal and feasibility review; and
- CAP-1 final learning-health-system analytics.

The visualization may be reused. Its source, definitions, limitations, accessibility, and action boundary travel with it.

### Final boundary

Module 13 ends when one evidence chain is source-faithful, audience-specific, reproducible, accessible, action-bounded, and defended. The next curriculum builds apply these habits inside the two foundation courses, seven distinct applied courses, and separate capstones.

# APP-1 Module 05: Clinical variation and patterns of care

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app1-05`.
- Course: APP-1, Data for Clinical Care.
- Instructional week: 5.
- Hours: 16.0.
- Module version target: 0.1.0.
- Commons release target: 0.53.0.
- Submission: clinical variation memo.
- Course points: 20, awarded once at the Week 6 checkpoint.
- Prerequisites: accepted APP-1 Module 04 at Commons 0.52.0 and the unchanged full pinned Synthea database.

This module turns cohort, survival, and risk-adjustment evidence into a patterns-of-care analysis. Learners define process, treatment-record, procedure, utilization, and outcome measures; preserve each denominator; compare variation across pathway exposure, synthetic teaching site, a clinical subgroup, and time; and decide whether one bounded finding is useful enough to enter improvement design.

## 2. Decision, readers, and intended use

The continuing decision is whether a hospital medicine care-improvement council should design and prospectively evaluate a pathway that increases scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge.

Module 05 asks:

> Which recorded patterns of care vary enough to shape a prospective improvement option, and which apparent differences must stop at description because clinical need, timing, measurement, or synthetic provenance could explain them?

Primary readers are the hospital medicine council, clinical care analytics lead, APP-1 faculty owner, methods reviewer, and learner. The intended use is curriculum progression and prospective-test design. It is not real-facility reporting, quality grading, causal evaluation, payment, or deployment.

## 3. Accepted upstream identity and immutable handoff

The module accepts only:

- Module 04 ID `oclc-app1-04`, version `0.1.0`, and Commons release `0.52.0`;
- Module 04 immutable manifest SHA-256 `5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb`;
- Module 02 analysis-cohort SHA-256 `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`;
- Module 04 expected-outcomes SHA-256 `e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e`;
- the 476-person risk set, 129 recorded scheduled-follow-up exposures, 87 later acute returns, and six fixed teaching sites; and
- the full pinned Synthea SQLite database SHA-256 `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`.

The module may derive post-discharge care records from the accepted database and join the frozen expected probability. It may not change cohort membership, index time, exposure, outcome, event order, censoring, expected probability, or teaching-site assignment.

## 4. Public source, rights, and source-row rule

The sole patient-level source remains the April 2020 Synthea sample archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip

Synthea describes its records as synthetic and available for unrestricted secondary use: https://synthetichealth.github.io/synthea/

Module 05 reads the accepted SQLite database in read-only mode. It uses source rows from `encounters`, `medications`, `procedures`, and `careplans`, linked to the accepted cohort through the synthetic patient identifier. No new patient, event, treatment, procedure, outcome, site, or subgroup value is generated. The six teaching-site labels remain the deterministic Module 02 extension and carry a known direct site effect of zero.

## 5. Learning outcomes

By the end of the module, a learner can:

- translate a care-pathway question into numerator, denominator, time, source, and claim contracts;
- distinguish an encounter, order, procedure, and care-plan record from care received or benefit;
- explain why a medication order is treatment-record exposure and not medication adherence;
- calculate proportions, absolute percentage-point differences, and encounter rates with exact denominators;
- compare process and outcome patterns without changing the accepted outcome model;
- separate clinical or operational importance from statistical compatibility;
- use confidence intervals and a global test without turning a p-value into the decision;
- inspect pathway composition before calling procedure-count differences quality variation;
- apply support and suppression rules before presenting site or subgroup results;
- interpret time-window rates with the correct person-day denominator;
- identify confounding by indication, clinical need, measurement, and timing;
- audit association-versus-causation language;
- write one bounded variation finding with a valid improvement handoff; and
- reproduce and validate the complete module package.

## 6. Foundation skill revisited and ownership boundary

FND-1 owns clean relational tables, joins, denominators, and descriptive summaries. FND-2 owns uncertainty, comparisons, regression recognition, and validity threats. Module 05 revisits those skills through one care-transition pathway.

Module 05 owns:

- care-process and care-record measure definitions;
- recorded treatment exposure and the explicit non-adherence boundary;
- procedure, utilization, outcome, site, clinical-subgroup, and time variation;
- clinical or operational thresholds used alongside uncertainty;
- record-mix and residual-confounding review;
- association-versus-causation claim audit;
- the 20-point clinical variation memo; and
- the bounded handoff to Module 06.

Module 06 owns formal demographic subgroup and equity analysis, improvement design, driver diagrams, implementation measures, and the simple-versus-machine-learning comparison. Module 07 owns the final clinical recommendation and defense.

## 7. Explicitly out of scope

- medication adherence, persistence, possession ratio, or days covered;
- proof that an appointment was offered, attended, useful, accessible, or high quality;
- proof that medication reconciliation met a real operational specification;
- causal effect of scheduled follow-up, treatment, procedure, site, or time;
- treatment effectiveness or comparative effectiveness;
- changing or refitting the Module 04 expected-outcome model;
- propensity scores, inverse weighting, target-trial emulation, or instrumental variables;
- demographic disparity, fairness, or inequity conclusions;
- machine learning, feature selection, or model deployment;
- real clinician, facility, payer, or community ranking; and
- real-population prevalence, utilization, quality, safety, or implementation claims.

## 8. Lesson sequence and learner time

| Block | Hours | Work |
|---|---:|---|
| Handoff and source-row verification | 1.0 | Verify three upstream fingerprints and the read-only database |
| Measure and denominator contracts | 2.5 | Define process, treatment-record, procedure, utilization, and outcome measures |
| Person-level care-pattern table | 2.5 | Join source rows to the frozen cohort and expected probability |
| Exposure and clinical-subgroup variation | 2.0 | Compare absolute differences, intervals, thresholds, and clinical need |
| Teaching-site variation and suppression | 2.0 | Preserve fixed site order, support, global evidence, and zero-effect provenance |
| Time and utilization patterns | 1.5 | Calculate fixed-window counts and person-day rates |
| Record mix and residual confounding | 1.0 | Inspect common procedure and treatment records before interpreting counts |
| Memo, claim audit, and Module 06 handoff | 2.5 | Select one bounded finding and reject unsupported claims |
| Reproduction and release | 1.0 | Rebuild, validate, and record accountable agent use |
| Total | 16.0 |  |

## 9. Required readings and methods sources

- AHRQ Care Coordination Measures Atlas: https://www.ahrq.gov/ncepcr/care/coordination/atlas.html
- AHRQ Safe Transitions medication-reconciliation measure profile: https://www.ahrq.gov/sites/default/files/wysiwyg/professionals/prevention-chronic-care/improve/coordination/atlas2014/appendix4a.pdf
- CDC Field Epidemiology Manual, Analyzing and Interpreting Data: https://www.cdc.gov/field-epi-manual/php/chapters/analyze-interpret-data.html
- Synthea project and data description: https://synthetichealth.github.io/synthea/
- Synthea CSV exporter table documentation: https://synthetichealth.github.io/synthea/build/javadoc/org/mitre/synthea/export/CSVExporter.html

The AHRQ material supplies a real care-coordination measurement frame. It does not convert a Synthea procedure row into validated real-world medication reconciliation. The CDC reading supports count-first description, measures of association, confidence intervals, and interpretation beyond a p-value.

## 10. Time, denominator, and record contract

Day 0 remains the accepted index encounter stop. The scheduled-follow-up exposure remains one or more `ambulatory`, `outpatient`, or `wellness` encounters during days greater than 0 through 30. The frozen landmark occurs at day 30.

Post-landmark process records use days greater than 30 through 365. The three utilization windows are:

- early post-landmark: days greater than 30 through 90, 60 days;
- middle: days greater than 90 through 180, 90 days; and
- late: days greater than 180 through 365, 185 days.

All 476 people have the same 335 post-landmark days available for the record-pattern analysis. A later acute return ends the time-to-first-event outcome in Modules 03 and 04, but it does not erase later source records from this descriptive utilization analysis. Every rate therefore states whether its denominator is people, eligible encounters, or person-days.

## 11. Measure contract

The immutable `measure-contract.csv` gives each measure an ID, role, source rows, numerator, denominator, time, threshold, and claim limit.

Required measures are:

- recorded scheduled follow-up within day 30;
- continued scheduled-care record during days 31 through 90;
- any scheduled-care record during days 31 through 365;
- any medication-order record during days 31 through 365;
- medication-reconciliation procedure record during days 31 through 365;
- any procedure record during days 31 through 365;
- total, scheduled, and acute encounter counts during days 31 through 365;
- later acute return by day 365; and
- the unchanged Module 04 expected probability.

The reference uses an absolute 0.10 difference as an educational operational-importance threshold for process-record proportions and 0.05 for the later acute-return proportion. These are curriculum decision thresholds, not clinical guidelines or minimum important differences validated in patients.

## 12. Treatment exposure and adherence boundary

A Synthea `medications` row is a prescription or administration record generated by the simulation. In this module it supports only `medication_record_31_365_flag` and `medication_record_count_31_365`.

It does not establish dispensing at a known date, possession, administration, ingestion, persistence, correct dose, benefit, or patient preference. The module therefore reports recorded treatment exposure. A learner who calls the measure adherence, compliance, medication possession ratio, or days covered fails the measure-definition gate.

## 13. Procedure and record-mix review

Procedure rows are summarized first as a binary person-level flag and then as a record mix. Raw procedure counts are not treated as quality because the broad adult acute cohort contains different clinical pathways and needs. The reference record mix must keep common pregnancy, screening, medication-reconciliation, examination, chemotherapy, and other procedure descriptions visible when present.

Medication reconciliation receives a separate process-record flag because it is relevant to care transitions. The flag states only that the exact procedure description appears in the source window. It does not prove the full reconciliation process described by AHRQ.

## 14. Exposure and clinical-subgroup comparisons

Exposure comparisons use recorded day-30 scheduled follow-up versus no recorded day-30 scheduled follow-up. The clinical subgroup comparison uses index encounter class: inpatient versus emergency. Race, ethnicity, gender, and other equity-relevant fields are carried only for Module 06 and are not analyzed here.

For each binary measure, the module reports group denominators, numerators, proportions, absolute difference, an unpooled large-sample 95% interval for the difference, two-sided Fisher exact p-value, the curriculum threshold, and whether the interval excludes zero. Learners must interpret the estimate, interval, threshold, timing, and clinical need together.

## 15. Teaching-site variation and suppression

Teaching sites remain in fixed alphabetical order. They are labels assigned by the deterministic Module 02 extension, not source facilities. Their known direct effect on the outcome is zero.

Site-level process proportions may be displayed when a site has at least 50 eligible people and at least 10 numerator and 10 complement observations. Otherwise the result is suppressed. Medication-reconciliation rates among the day-30 exposed group are expected to be too sparse for site comparison and remain suppressed.

The module reports the maximum-minus-minimum range and one six-site Pearson chi-square test for scheduled follow-up. It does not report pairwise site tests, league tables, best/worst labels, or rank order. A large range can be operationally interesting while the global evidence remains compatible with chance and the known synthetic zero-effect design.

## 16. Time and utilization comparisons

For each fixed time window and exposure group, the module reports:

- people and person-days;
- people with a scheduled-care record;
- scheduled-care records and rate per 1,000 person-days;
- all encounter records and rate per 1,000 person-days; and
- acute encounter records and rate per 1,000 person-days.

Unequal window length makes raw count comparison invalid. Rates are descriptive source-record rates, not real utilization rates. An encounter count can reflect need, pregnancy or chronic-care pathways, simulation logic, or repeated records; it is not automatically overuse or underuse.

## 17. Clinical significance, statistical evidence, and causal language

Every primary comparison receives two separate labels:

1. whether the absolute difference reaches the frozen curriculum threshold; and
2. whether its 95% interval excludes zero.

Neither label settles clinical value. A p-value does not measure effect size, importance, bias, measurement validity, or causality. A threshold does not repair confounding or poor measurement. The memo must state at least one credible noncausal explanation for every selected difference.

Allowed verbs include `recorded`, `observed`, `differed`, `was associated`, `was compatible`, and `suggests a prospective measurement question`. Prohibited verbs include `caused`, `prevented`, `improved`, `failed`, `underperformed`, `was effective`, and `was safer` unless the sentence explicitly rejects that interpretation.

## 18. Exact learner deliverables and 20-point assessment

The learner package contains:

- `variation-memo.md`;
- `measure-interpretation.md`;
- `support-suppression-review.md`;
- `claim-audit.csv`;
- `handoff-to-module06.md`;
- `reproducibility-check.md`;
- `ai-use.md`;
- the immutable contracts, source record, environment, builder, validator, and workspace manifest; and
- all reference-shaped outputs produced by the learner's build.

The 20 points are awarded once at the Week 6 checkpoint:

| Criterion | Points |
|---|---:|
| Measure, timing, source, and denominator fidelity | 4.00 |
| Exposure, clinical-subgroup, site, and time variation | 5.00 |
| Clinical significance, uncertainty, and support decisions | 4.00 |
| Clinical reasoning, confounding, and claim discipline | 4.00 |
| Reproducibility, accessibility, handoff, and accountable agent use | 3.00 |
| Total | 20.00 |

## 19. Noncompensable gates and common failures

All 18 gates are noncompensable:

1. Exact Module 02 cohort, Module 04 expected outcomes, and SQLite fingerprints.
2. Unchanged 476 people, 129 exposures, 87 outcomes, and six sites.
3. Read-only use of the full pinned source.
4. Exact day-0, day-30, and day-365 timing.
5. Every numerator has its correct denominator.
6. Medication records are not labeled adherence.
7. Procedure records are not labeled care quality.
8. Outcome and expected probability remain unchanged.
9. Exposure and index-class comparisons include counts, absolute differences, and intervals.
10. Time comparisons use person-days rather than raw counts alone.
11. Site order is fixed and unsupported results are suppressed.
12. The six sites remain synthetic with known direct effect zero.
13. Operational thresholds and statistical evidence remain separate.
14. Record mix and at least two residual-confounding explanations are reviewed.
15. No causal, efficacy, fairness, real-site ranking, or deployment claim is made.
16. Every display has an exact table and structured text alternative.
17. The Module 06 handoff contains exactly one bounded finding, equity question, improvement lever, and simpler benchmark.
18. Reproduction, source identity, and material agent use are independently verified.

Common failures include counting records without people, changing the denominator between groups, treating no record as no care, interpreting a medication order as ingestion, comparing time-window counts without exposure time, choosing a finding by p-value alone, ranking synthetic sites, ignoring pathway composition, and using synthetic evidence to authorize implementation.

## 20. Reproducibility, validation, and mutation rejection

The builder:

- opens the SQLite database in read-only mode;
- verifies the database, cohort, and expected-outcome SHA-256 values;
- rejects an existing output target;
- writes every person and aggregate output deterministically;
- uses no random process;
- fixes the site order and measure order;
- records package, software, source-row, and expected finding details; and
- produces the same bytes on two complete builds.

The validator checks immutable workspace fingerprints, exact output shapes and hashes, source and outcome conservation, measure definitions, support decisions, fixed findings, accessible display text, memo claims, handoff structure, and assessment totals. It rejects changed upstream inputs, changed contracts, incomplete starter work, altered outputs, invalid scores, unsupported progression, placeholders, personal paths, and causal or ranking language.

The released package contains eleven deterministic outputs totaling 180,851 bytes. Its nine-row immutable learner-workspace manifest is 1,526 bytes with SHA-256 `7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e`. Module-root validation passes 129 checks, complete reference validation passes 159 checks, and learner-starter validation passes 82 checks.

## 21. Progression, reference finding, reviewers, version, and known issues

The reference finding is bounded deliberately: scheduled-follow-up recording varies across the six synthetic teaching sites by `0.14816372`, enough to cross the curriculum's operational threshold, while the global Pearson chi-square p-value is `0.27993975`. The global comparison does not establish site performance and the extension's known direct site effect remains zero. The finding supports a prospective measurement and workflow question, not a site intervention or grade.

The Module 06 handoff must contain exactly:

- one bounded variation finding;
- one equity question that Module 05 has not answered;
- one feasible improvement lever to test prospectively; and
- one transparent analytic benchmark for the embedded machine-learning comparison.

Allowed progression decisions are `continue`, `continue with conditions`, `revise`, and `refer`. Reference progression is `continue with conditions`.

Required review coverage before alpha includes clinical care, care transitions, medication safety, health-services methods, statistics, informatics, equity, accessibility, privacy, responsible AI, and an independent instructor. Named reviews remain pending.

Module version: 0.1.0. Commons release: 0.53.0.

Known limits are the synthetic source; broad, heterogeneous acute-care cohort; source records that do not establish care quality, need, access, completion, adherence, or benefit; arbitrary teaching-site labels; simple large-sample difference intervals; no multiplicity correction because pairwise selection is prohibited; and pending named review. None of these limits changes the module's teaching purpose: define variation carefully, preserve denominators, and stop claims at the evidence boundary.

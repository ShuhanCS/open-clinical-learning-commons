# APP-1: Data for Clinical Care

APP-1 is the first domain-specific applied course. Learners use a continuing synthetic clinical pathway to build a longitudinal cohort, analyze time-to-event outcomes, compare care fairly, inspect variation and equity, test a bounded machine-learning extension, and defend a feasible improvement recommendation.

- Credits: 3
- Delivery: online half-term
- Learner work: 112.5 hours
- Prerequisites: accepted FND-1 and FND-2 technical releases
- Core tools: SQL and Python
- Final deliverable: clinical care improvement brief with reproducible evidence and a defense
- Course package version: 0.1.0
- Commons release: 0.54.0
- Current package status: Modules 01 through 06 and the Week 3 and Week 6 checkpoints are runnable release candidates

## Seven applied modules

1. Framing a care-pathway decision - 15.5 hours.
2. Longitudinal cohorts and follow-up - 16.0 hours.
3. Survival and time-to-event outcomes - 16.5 hours.
4. Risk adjustment and fair comparison - 16.5 hours.
5. Clinical variation and patterns of care - 16.0 hours.
6. Equity, feasible improvement, and embedded machine learning - 16.0 hours.
7. Clinician leadership, recommendation, and defense - 16.0 hours.

Module 06 contains eight hours of cumulative application and equity work plus an eight-hour bounded machine-learning extension. Module 07 is the clinician-led leadership block. Joe Joseph, MD, is the designated clinician, subject to direct identity and publishable-biography confirmation before learner-facing release.

## Runnable module

- [Module 01: Framing a care-pathway decision](modules/01-care-pathway-decision/README.md)
- [Module 01 durable specification](../../docs/curriculum/courses/APP-1/modules/01-care-pathway-decision-spec.md)
- [Module 02: Longitudinal cohorts and follow-up](modules/02-longitudinal-cohorts-followup/README.md)
- [Module 02 durable specification](../../docs/curriculum/courses/APP-1/modules/02-longitudinal-cohorts-followup-spec.md)
- [Module 03: Survival and time-to-event outcomes](modules/03-survival-time-to-event/README.md)
- [Module 03 durable specification](../../docs/curriculum/courses/APP-1/modules/03-survival-time-to-event-spec.md)
- [Week 3 checkpoint](checkpoints/01-longitudinal-survival-readiness/README.md)
- [Week 3 checkpoint durable specification](../../docs/curriculum/courses/APP-1/checkpoints/01-longitudinal-survival-readiness-spec.md)
- [Module 04: Risk adjustment and fair comparison](modules/04-risk-adjustment-fair-comparison/README.md)
- [Module 04 durable specification](../../docs/curriculum/courses/APP-1/modules/04-risk-adjustment-fair-comparison-spec.md)
- [Module 05: Clinical variation and patterns of care](modules/05-clinical-variation-patterns-of-care/README.md)
- [Module 05 durable specification](../../docs/curriculum/courses/APP-1/modules/05-clinical-variation-patterns-of-care-spec.md)
- [Module 06: Equity, feasible improvement, and embedded machine learning](modules/06-equity-improvement-embedded-ml/README.md)
- [Module 06 durable specification](../../docs/curriculum/courses/APP-1/modules/06-equity-improvement-embedded-ml-spec.md)
- [Week 6 checkpoint](checkpoints/02-adjusted-variation-improvement-release/README.md)
- [Week 6 checkpoint durable specification](../../docs/curriculum/courses/APP-1/checkpoints/02-adjusted-variation-improvement-release-spec.md)

Module 01 profiles the complete pinned 16-table, 471,836-row Synthea source. Its reference pathway begins with 518 synthetic adults, preserves 9 index deaths, 8 early post-discharge deaths, and 25 early acute returns, and defines a 476-person day-30 landmark risk set. Among eligible people, 129 have scheduled follow-up and 87 have a later acute return. Sixty-four sparse source organizations make raw site ranking `not ready`.

The 19-file learner workspace contains nine frozen source and contract records, nine editable decision records, and one deterministic release manifest. The standard-library profiler, builder, and validator reproduce exact evidence and reject changed source facts, missing pathway states, invalid scoring, unsupported progression, and incomplete records.

Module 02 preserves all 518 initial people and makes 9 index deaths, 8 early post-discharge deaths, and 25 early acute returns explicit before defining the corrected 476-person landmark risk set. Its 1,018-row event audit supports a 476-row survival-ready analysis cohort with 129 exposed people, 87 later events, and 389 administrative censors. A deterministic six-site extension adds overlapping case mix without changing source exposure or outcomes.

Module 03 releases 84 event-time rows, 12 fixed-time risk rows, and exact log-rank, Cox, proportional-hazards, death-audit, and accessible-curve evidence. The log-rank p-value is 0.67258471 and the unadjusted hazard ratio is 1.10542457, but the PH screen fails at p = 0.00636020. Fixed-time evidence remains the main summary.

The Week 3 checkpoint assembles 78 accepted module files into a 91-file package. It carries the 20.00-point Module 02 score once, requires all 16 survival gates, and continues to Module 04 with the failed PH screen as an open methods condition.

Module 04 uses a fixed day-335 outcome because every no-event person reaches the same administrative boundary and no competing death occurs first. Its prespecified four-predictor expected model has apparent Brier score 0.13490621 and apparent ROC AUC 0.66585409. The secondary adjusted scheduled-follow-up odds ratio is 1.16353250 with a 95 percent interval from 0.67665877 to 2.00072462. All six synthetic sites meet the reporting minimums, remain in fixed order, and are reported with caution rather than ranked.

Module 05 reads 1,694 post-landmark encounter rows, 742 medication rows, 1,832 procedure rows, and 92 care-plan rows from the full pinned Synthea database. Recorded scheduled follow-up spans 22.99 percent to 37.80 percent across the fixed synthetic teaching sites, but the global p-value is 0.27993975 and the known direct site effect is zero. The module treats that 14.82-point spread as a prospective measurement question, not site performance, and explicitly prevents medication orders from becoming an adherence measure.

Module 06 preserves 12 fixed equity groups, reports counts and uncertainty, and suppresses unsupported process or outcome summaries without combining small groups. Its pathway separates the observed 476 to 129/347 record split from offer, preference, scheduling, completion, barriers, and burden that require prospective collection. On 143 held-out people and 17 events, the transparent model has Brier score 0.09609243 and AUC 0.66363212; the bounded random forest has 0.10745654 and 0.62371615. The forest catches three more events but adds 32 false positives and 35 flags, so it does not change the capacity-aware scheduling proposal.

The Week 6 checkpoint assembles 32 Module 04 files, 30 Module 05 files, and 38 Module 06 files into a 113-file package. It scores 45.00 points exactly once and continues to Module 07 with clinical implementation and model deployment prohibited.

## Three cumulative checkpoints

- Week 3: decision charter, longitudinal cohort, and survival-readiness release - 20 course points.
- Week 6: survival and risk-adjusted comparison, variation, equity, improvement, and simple-versus-machine-learning release - 45 course points.
- Official half-term end date: clinician-led improvement brief, implementation and monitoring plan, and defense - 35 course points.

The 7.5-week phrase is a planning model. Published dates use the official MGH Institute half-term calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Data and claim boundary

The course reuses the full pinned Synthea April 2020 CSV release:

https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip

No real patient records are used. Synthetic frequencies do not estimate real prevalence, quality, access, equity, outcomes, treatment effects, or facility performance. The package supports technical education and prospective-test design only.

## Durable records

- [Course specification](../../docs/curriculum/courses/APP-1/course-spec.md)
- [Source record](../../docs/source/app-1-clinical-care-source-record.md)
- [Master curriculum architecture](../../docs/specs/2026-08-29-curriculum-master-architecture-spec.md)
- [Build ledger](../../docs/curriculum/BUILD-LEDGER.md)

## Build order

Modules 01 through 06 and the Week 3 and Week 6 checkpoints are complete. Module 07 next owns clinician leadership, recommendation, stakeholder action, monitoring, and defense.

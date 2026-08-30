# FND-2: Modeling, Inference, and Reproducible Analytics

FND-2 teaches learners to turn checked healthcare data into analytic evidence and defend the method, assumptions, performance, limits, and monitoring plan. It is a separate straight-through technical foundations course, not a three-week block inside each applied course.

- Credits: 3
- Delivery: online half-term
- Learner work: 112.5 hours
- Prerequisite: accepted FND-1 technical toolkit
- Core tools: SQL, Python, pandas, notebooks, statistical and machine-learning packages, Git, and semantic versioning
- R role: read, run, and interpret, without grading from-scratch R programming
- Continuing prediction case: the accepted 374-person FND-1 synthetic acute-care cohort
- Continuing forecast case: the pinned 6,208-row CDC NHSN jurisdiction-week public release
- Final deliverable: a reproducible model or agent-assisted analytics package with a model card
- Course specification status: complete candidate
- Module package status: Modules 01 through 04 and Checkpoint 1 are runnable release candidates
- Course package version: 0.1.0
- Commons release: 0.43.0

## Seven technical modules

1. Analytic aims and a reproducible modeling workspace.
2. Regression models and interpretation.
3. Prediction workflows and evaluation.
4. Adjustment, missing data, and longitudinal structure.
5. Forecasting and temporal validation.
6. Agent-assisted modeling and testing.
7. Model cards, governance, and defense.

## Runnable modules

- [Module 01: Analytic aims and a reproducible modeling workspace](modules/01-aims-reproducible-workspace/README.md)
- [Module 01 durable specification](../../docs/curriculum/courses/FND-2/modules/01-aims-reproducible-workspace-spec.md)
- [Module 02: Regression models and interpretation](modules/02-regression-interpretation/README.md)
- [Module 02 durable specification](../../docs/curriculum/courses/FND-2/modules/02-regression-interpretation-spec.md)
- [Module 03: Prediction workflows and evaluation](modules/03-prediction-evaluation/README.md)
- [Module 03 durable specification](../../docs/curriculum/courses/FND-2/modules/03-prediction-evaluation-spec.md)
- [Module 04: Validity, adjustment, and longitudinal structure](modules/04-validity-adjustment-longitudinal/README.md)
- [Module 04 durable specification](../../docs/curriculum/courses/FND-2/modules/04-validity-adjustment-longitudinal-spec.md)

Module 01 preserves the accepted 374-row FND-1 table, assigns all 29 source fields and five derived fields a role, freezes the 224/75/75 temporal split with 25/7/4 positive outcomes, and registers the training-prevalence baseline before model fitting. Its standard-library builder and validator create a protected learner workspace and reject incomplete submissions.

Module 02 fits a conditional linear case on 69 training rows within the 111-row recorded-next-encounter subset and bounded logistic cases on 224 training rows with 25 outcomes. It reports exact formulas, model matrices, classical and HC3 uncertainty, diagnostics, nonlinear and interaction exercises, sparse-cell checks, paired R reading, and a quantity-correct Module 03 handoff.

Module 03 fits all preprocessing inside training, compares the constant baseline, `LOG01`, one bounded random forest, and a deliberately leaked critique model, and applies a frozen validation rule. It selects `ML01`, locks threshold 0.08513264 before test, and reports the untouched 75-row test evidence: 48 true negatives, 23 false positives, 2 false negatives, and 2 true positives. Four test outcomes, subgroup suppression, accessible exact tables, and the teaching-only boundary remain binding.

Module 04 separates prediction from causal adjustment and makes selection, missingness, within-person dependence, and censoring visible. It preserves the 374-row public-safe Synthea case, adds a 600-person treatment fixture with a known -6-point effect and 91 missing severity values, compares seven adjustment routes, models 2,400 repeated observations from 600 people, and reads a 600-person survival case with 449 events and 151 censored records. All results remain synthetic teaching evidence.

## Runnable checkpoint

- [Checkpoint 1: Modeling-readiness and prediction-evaluation release](checkpoints/01-modeling-readiness-release/README.md)
- [Checkpoint 1 durable specification](../../docs/curriculum/courses/FND-2/checkpoints/01-modeling-readiness-release-spec.md)

Checkpoint 1 assembles rather than recomputes Modules 01 through 03. It freezes 72 module artifacts and six controls in a 78-row manifest, preserves the corrected 40-point 15/10/15 map, enforces 23 gates and a 12-question defense, and carries the four-outcome test evidence and teaching-only boundary into Module 04.

## Three cumulative checkpoints

- Week 3: aim, reproducible model setup, regression, and prediction evaluation.
- Week 6: validity, longitudinal, forecasting, tests, trace log, and human sign-off.
- Official half-term end date: final analytics package, model card, monitoring and stop rules, reproducibility audit, and technical defense.

The 7.5-week phrase is a planning model. Published due dates use the official MGH Institute half-term calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Course decision

The final decision owner is a clinical analytics model-risk lead. The review separates two decisions:

1. Is the analytics package technically correct, reproducible, accessible, and honestly documented?
2. What use, if any, may the fitted model support?

A package may pass while the model-use recommendation remains `do not deploy`. That is the expected reference outcome for a small synthetic cohort with only four acute-return outcomes in its held-out test period.

## Data plan

The main modeling table is a versioned derivation of the accepted FND-1 374-row, 29-field analytic table. Prediction occurs at index-encounter stop. Only pre-index and index-time fields may become predictors. The 90-day acute-return label has 36 positive and 338 negative rows.

The declared temporal 60/20/20 split has:

- 224 training rows with 25 positive outcomes;
- 75 validation rows with 7 positive outcomes; and
- 75 test rows with 4 positive outcomes.

Post-index next-encounter, outcome, endpoint, and follow-up fields are excluded from predictors. They remain available only for labels, evaluation, and leakage tests.

The forecasting release reuses all 6,208 public CDC NHSN jurisdiction-week rows across 67 jurisdictions and the exact 94-week Massachusetts teaching series already registered in the Commons. FND-2 adds temporal validation and forecasting evidence without changing the source observations.

CDC source:

https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi

## Durable records

- [Course specification](../../docs/curriculum/courses/FND-2/course-spec.md)
- [Source record](../../docs/source/fnd-2-modeling-inference-reproducible-analytics-source-record.md)
- [FND-1 handoff course](../healthcare-data-foundations/README.md)
- [Master curriculum architecture](../../docs/specs/2026-08-29-curriculum-master-architecture-spec.md)
- [Build ledger](../../docs/curriculum/BUILD-LEDGER.md)

## Build order

Build Modules 01 through 07 one at a time. Each unit receives a durable specification, versioned data or accepted upstream input, runnable work, learner assessment, instructor notes, validator, review fields, semantic-version decision, commit, and push before the next unit begins.

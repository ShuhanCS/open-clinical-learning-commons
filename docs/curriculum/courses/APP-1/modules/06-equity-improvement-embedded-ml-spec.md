# APP-1 Module 06: Equity, feasible improvement, and embedded machine learning

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app1-06`.
- Course: APP-1, Data for Clinical Care.
- Course position: instructional Week 6 through Week 6.5.
- Total learner time: 16.0 hours.
- Application and improvement work: 8.0 hours.
- Embedded machine-learning extension: 8.0 hours.
- Submission: cumulative Week 6 adjusted-variation-and-improvement release.
- Prerequisites: accepted APP-1 Modules 01 through 05 and accepted Week 3 checkpoint identity.
- Module version at first runnable release: `0.1.0`.
- Commons release at first runnable release: `0.54.0`.

This module completes the six-week technical case. It does not add course points. It supplies required equity, improvement, and machine-learning gates to the Week 6 package, which scores the existing 25-point Module 04 analysis and 20-point Module 05 memo exactly once.

## 2. Decision, readers, and intended use

The learner answers two linked questions:

1. Is a feasible prospective pathway-improvement test justified by the accepted evidence?
2. Does one bounded machine-learning model materially change that decision compared with the transparent risk-adjusted benchmark?

The primary readers are a clinical care analytics lead, a clinical improvement reviewer, an equity reviewer, and a methods reviewer. The package is a curriculum artifact built from synthetic data. It may support Module 07 leadership review. It may not authorize care, rank real sites or groups, certify fairness, or deploy a model.

## 3. Accepted upstream identity and immutable handoff

The build accepts only these versioned inputs:

- APP-1 Module 05, version `0.1.0`, Commons `0.53.0`.
- Module 05 workspace manifest SHA-256 `7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e`.
- `care-patterns.csv`: 476 rows, 26 fields, 99,475 bytes, SHA-256 `c5d372e777ff3b190859e7c418b87c4f165776b84fb86346db700fa39f516a6e`.
- Module 02 `analysis-cohort.csv`: 476 rows, 49 fields, 200,699 bytes, SHA-256 `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`.
- Module 04 `expected-outcomes.csv`: 476 rows, 12 fields, 54,320 bytes, SHA-256 `e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e`.

The accepted Module 05 handoff is fixed:

- Bounded finding: recorded scheduled follow-up ranges from `0.22988506` to `0.37804878` across six fixed synthetic sites, a `0.14816372` spread; global p = `0.27993975` and the known direct site effect is zero.
- Equity question: in a prospective workflow, do offer, scheduling, completion, and burden differ across prespecified groups after support, missingness, and privacy review?
- Improvement lever: capacity-aware scheduling before discharge with documented offer, preference, appointment status, and a safe escalation route.
- Transparent benchmark: the recorded-follow-up proportion with an exact numerator, denominator, Wilson interval, fixed timing, and no site ranking, plus the Module 04 risk-adjustment feature formula.

The builder must reject a changed file, changed row identity, duplicate patient, missing patient, changed contract, or extra evaluation row.

## 4. Public source, rights, and source-row rule

The accepted cohort comes from the Synthea synthetic health record source already frozen by Modules 02 through 05. No real patient data are used. The module reads the three accepted CSV extracts and does not query or modify the source SQLite database.

The person is the analysis unit. The accepted 476 `patient_id` values must match one-to-one across all three inputs. Demographic fields come from the accepted cohort and retain their source labels. They are audit fields, not verified identities or model predictors.

## 5. Learning outcomes

By the end of the module, learners can:

1. Prespecify an equity review before looking at subgroup results.
2. Preserve subgroup denominators, missingness, uncertainty, and suppression.
3. Distinguish a synthetic source-record difference from evidence of inequity or unfairness.
4. Show the observed pathway and the data that a prospective improvement test would still need to collect.
5. Convert a bounded analytic finding into a driver diagram and a usable measure set.
6. Compare a transparent model with one bounded machine-learning model under the same prediction time, features, split, rows, and threshold.
7. Evaluate discrimination, calibration, error counts, error costs, subgroup support, and failure cases together.
8. State whether machine learning changes the decision and why.
9. Release a reproducible cumulative Week 6 package without double-counting grades.

## 6. Foundation skill revisited and ownership boundary

This course revisits foundations through a clinical improvement decision. Learners again use denominators, missingness, descriptive comparisons, uncertainty, accessible displays, validation, and reproducibility, but the task is now to decide whether a care-pathway test is justified.

Ownership is strict:

- Module 04 owns survival carry-forward, the transparent risk-adjustment formula, expected outcomes, and the 25-point adjusted analysis.
- Module 05 owns care-pattern variation and the 20-point variation memo.
- Module 06 owns the equity gate, pathway display, improvement design, and simple-versus-ML decision.
- Module 07 owns clinical leadership, stakeholder action, implementation authorization, monitoring, and defense.

Module 06 may narrow, defer, or stop an improvement proposal. It may not repair weak upstream evidence with a more complex model.

## 7. Explicitly out of scope

The module does not:

- infer gender identity from the source `gender` field;
- treat synthetic race or ethnicity labels as proof of lived identity, access, discrimination, fairness, or inequity;
- combine small groups merely to make them reportable;
- rank groups or sites;
- use pairwise subgroup hypothesis tests as a fairness scorecard;
- add site, exposure, expected probability, demographics, or post-exposure fields to the predictive feature set;
- tune on held-out evaluation rows;
- search multiple model families, thresholds, or subgroup definitions;
- claim that a lower false-negative count alone justifies a model;
- recommend real clinical use, automated prioritization, or model deployment; or
- award extra course points for equity, improvement, or machine learning.

## 8. Lesson sequence and learner time

| Lesson | Hours | Work product |
|---|---:|---|
| Prespecify the equity question and support rules | 1.5 | `equity-review.md` plan |
| Audit subgroup counts, missingness, process, and outcome summaries | 2.0 | completed equity review |
| Map the observed and prospective pathway | 1.5 | pathway figure and accessible alternative |
| Design the feasible change and driver diagram | 2.0 | driver diagram and improvement brief |
| Define implementation, process, outcome, access, safety, and balancing measures | 1.0 | measure registry |
| Freeze prediction time, features, split, model, threshold, and error costs | 1.5 | model contract review |
| Fit and compare the transparent and bounded models | 3.0 | model comparison evidence |
| Audit calibration, subgroups, and failure cases | 2.0 | failure-case review |
| Decide whether ML changes the recommendation | 0.5 | progression decision |
| Assemble and reproduce the Week 6 release | 1.0 | cumulative checkpoint package |
| Total | 16.0 | |

## 9. Required methods and evidence sources

Learners use the course-wide source and methods record plus the accepted Module 04 and Module 05 contracts. The module requires methods support for:

- Wilson intervals for a recorded proportion;
- prespecified subgroup analysis and minimum-support suppression;
- pathway and driver-diagram construction;
- implementation, process, outcome, access, safety, and balancing measures;
- logistic risk prediction and random forests;
- Brier score, ROC AUC, log loss, calibration intercept and slope;
- paired stratified bootstrap comparison; and
- confusion counts and explicit error-cost scenarios.

Methods sources explain the calculation. They do not convert synthetic findings into clinical evidence.

## 10. Equity question and field contract

The primary equity question is whether recorded scheduled follow-up by day 30 differs across prespecified source-recorded groups, while recognizing that a record does not establish offer, access, preference, attendance, completion, burden, quality, need, or benefit.

The dimensions are fixed before analysis:

| Dimension | Fixed groups | Field meaning |
|---|---|---|
| Age at index | 18-44, 45-64, 65+ | calculated age band at the index encounter |
| Source-recorded gender | F, M | source value; not established gender identity |
| Source-recorded race | asian, black, native, other, white | synthetic source category; not a fairness conclusion |
| Source-recorded ethnicity | hispanic, nonhispanic | synthetic source category; not lived access or identity |

For every group, the analysis reports total rows, missing field rows, recorded-follow-up numerator and denominator, Wilson interval when reportable, outcome events, expected events, and observed-to-expected ratio when reportable. Fixed category order replaces result-based sorting.

## 11. Support, missingness, privacy, and suppression contract

The process measure is reportable only when all conditions hold:

- at least 30 people;
- at least 5 recorded-follow-up rows; and
- at least 5 rows without recorded follow-up.

The outcome and observed-to-expected summary are reportable only when all conditions hold:

- at least 30 people;
- at least 5 observed events;
- at least 5 non-events; and
- at least 5 expected events.

Unsupported cells retain the group label, denominator, missingness count, and suppression reason but omit the protected estimate. The reference equity summary suppresses the native and other race process estimates, and suppresses the Asian, native, and other race outcome summaries. No groups are merged to evade the rule.

Zero field-level missingness must be reported as a source result, not interpreted as complete or accurate identity capture. The review conclusion is one of `question retained`, `question narrowed`, or `question not supported`; it is never `fair`, `unfair`, or `equity proven`.

## 12. Observed and prospective pathway contract

The observed pathway uses only accepted records:

- 476 landmark-eligible people;
- 129 with recorded scheduled follow-up by day 30;
- 347 without a qualifying record;
- 25 later acute returns among the 129 with a qualifying record;
- 104 without a later return among the 129;
- 62 later acute returns among the 347 without a qualifying record; and
- 285 without a later return among the 347.

The pathway display must state that the source does not observe whether follow-up was offered, preferred, accepted, scheduled before discharge, completed, inaccessible, unwanted, burdensome, or clinically appropriate.

The prospective pathway adds those missing data states as proposed collection points, visually distinct from observed nodes. It must have an SVG, an exact node table, an exact edge table, and a structured text alternative. Color cannot be the only carrier of meaning.

## 13. Feasible improvement and measure contract

The bounded improvement option is a capacity-aware scheduling workflow before discharge. The workflow records eligibility, offer, preference, acceptance or decline, appointment status, capacity barrier, safe escalation, completion, and burden. It does not force scheduling and does not assume that every person wants or needs the same pathway.

The driver diagram must connect the aim to primary drivers, secondary drivers, and candidate changes. At minimum it addresses reliable identification, patient preference, scheduling capacity, handoff reliability, and safe escalation.

The measure registry must include:

- implementation: proportion of eligible discharges screened;
- process: proportion with offer and preference documented;
- process: proportion accepting an offer who are scheduled before discharge;
- outcome: proportion with completed scheduled care by day 30;
- access/equity: offer and completion by the fixed prespecified groups;
- balancing: discharge delay, staff workload, unwanted appointments, cancellations, and reported burden; and
- safety: early acute return, explicitly not attributed to the workflow without a prospective design.

Each measure needs an operational definition, numerator, denominator, timing, owner, source, stratification rule, interpretation, and failure response. The retrospective synthetic source cannot populate the unobserved prospective fields.

## 14. Prediction time, feature, split, and model contract

The prediction question is the risk of later acute return after the day-30 landmark. Both models use the same accepted people and information available by the prediction time.

Eligible features are exactly the Module 04 baseline formula:

- `age_decade_from_40`;
- `any_prior_acute`;
- `prior_365d_condition_count`; and
- `index_inpatient`.

Prohibited features include landmark exposure, recorded follow-up, teaching site, expected probability, outcome fields, post-landmark fields, synthetic assignment fields, gender, race, and ethnicity. Demographic fields remain audit-only.

Rows are ordered by `index_start`, then `patient_id`. The first 333 rows are training rows and the final 143 are held-out evaluation rows. The evaluation set contains 17 events. The split is fixed and may not be randomized, tuned, or reopened.

The transparent benchmark is a training-only binomial generalized linear model with a logit link and the four fixed features. The bounded ML model is `RandomForestClassifier` with 200 trees, `max_depth=3`, `min_samples_leaf=15`, `max_features=None`, random seed `20260830`, and `n_jobs=1`. No third model is fitted.

## 15. Evaluation, calibration, threshold, and error-cost contract

Both models are evaluated on the same 143 held-out rows with:

- Brier score;
- ROC AUC;
- log loss;
- calibration intercept;
- calibration slope;
- five fixed calibration groups ordered by probability then patient ID;
- confusion counts at a threshold fixed at `0.20`; and
- a paired stratified bootstrap with 1,000 replicates and seed `20260830` for the ML-minus-transparent Brier and AUC differences.

The threshold is a teaching threshold, fixed before evaluation. It is not an intervention threshold. The explicit teaching error-cost scenario assigns cost 3 to a false negative and cost 1 to a false positive. It is a sensitivity exercise, not a clinical value judgment.

The reference comparison is expected to show that the random forest catches three additional events but produces 32 additional false positives and 35 additional flags. Its weighted teaching cost is 67 versus 44 for the transparent model. The random forest also has worse point estimates for Brier score and AUC. These findings support retaining the transparent benchmark; uncertainty remains visible in the paired bootstrap intervals.

The exact held-out Brier scores are `0.09609243` for the transparent model and `0.10745654` for the bounded random forest. The exact AUC values are `0.66363212` and `0.62371615`, respectively.

## 16. Subgroup model audit and failure-case contract

The held-out subgroup audit uses the fixed source-recorded gender, race, and ethnicity categories. It reports a model metric only when the group has at least 30 evaluation rows, 5 events, and 5 non-events. Unsupported rows retain counts and a suppression reason.

The audit is descriptive and cannot certify model fairness. Small groups are not merged. Results are not ranked. A supported subgroup difference cannot authorize group-specific thresholds or different treatment.

Failure-case review includes every false negative from each model and an aggregate review of false positives. Learners inspect baseline features, prediction, outcome, and model disagreement without exposing personal paths or inventing clinical stories. At least these failure modes must be addressed:

- leakage or post-prediction information;
- evaluation-set tuning or test contamination;
- unsupported subgroup comparison;
- reliance on discrimination without calibration or error counts;
- performance-only recommendation;
- use of the model to replace universal workflow measurement; and
- deployment from synthetic retrospective evidence.

## 17. Exact learner deliverables

The learner workspace contains immutable controls and editable records.

Immutable controls:

- `.gitattributes`;
- `VERSION`;
- `source-record.yml`;
- `equity-contract.csv`;
- `model-contract.json`;
- `feature-contract.csv`;
- `environment.yml`;
- `assessment.md`;
- `build_equity_improvement.py`;
- `build_workspace.py`; and
- `validate_equity_improvement.py`.

Editable records:

- `README.md`;
- `equity-review.md`;
- `pathway-display.md`;
- `improvement-brief.md`;
- `driver-diagram.csv`;
- `improvement-measures.csv`;
- `ml-comparison.md`;
- `failure-case-review.md`;
- `reproducibility-check.md`;
- `ai-use.md`; and
- `progression-decision.md`.

Generated reference outputs:

- `analysis-checks.csv`;
- `equity-summary.csv`;
- `pathway-nodes.csv`;
- `pathway-edges.csv`;
- `pathway-figure.svg`;
- `split-registry.csv`;
- `model-predictions.csv`;
- `model-performance.csv`;
- `bootstrap-comparison.csv`;
- `calibration-bins.csv`;
- `threshold-errors.csv`;
- `subgroup-model-audit.csv`;
- `feature-importance.csv`;
- `failure-cases.csv`; and
- `build-report.json`.

The package includes a sorted SHA-256 manifest of immutable controls. Learner work files contain explicit prompts. Reference work files contain complete answers and exact evidence citations.

At first release, the 11-row immutable manifest is 1,833 bytes with SHA-256 `b7127dbfac9e7a9549ea682499a1ca5d368a4acbbc20da2e307324be5813b978`.

## 18. Week 6 cumulative checkpoint and assessment

The checkpoint path is `courses/clinical-care/checkpoints/02-adjusted-variation-improvement-release/`.

The checkpoint freezes accepted APP-1 Modules 04 through 06 while retaining the accepted Week 3 identity. It scores 45 course points exactly once:

| Scored source | Points |
|---|---:|
| Module 04 survival and risk-adjusted outcome analysis | 25 |
| Module 05 clinical variation memo | 20 |
| Total | 45 |

Module 06 earns no additional points. Its equity, pathway, improvement, accessibility, ML, failure, reproducibility, and progression requirements are noncompensable gates. The checkpoint cannot pass if any required gate fails, even when the scored Module 04 and Module 05 components total 45.

## 19. Noncompensable gates and common failures

The module must fail when any of these occur:

1. An accepted input identity or SHA-256 changes.
2. Patient IDs do not match one-to-one across inputs.
3. A subgroup definition is selected after reviewing results.
4. Counts, missingness, support, or suppression are absent.
5. A source-record difference is called proof of inequity, unfairness, or access.
6. Small groups are merged to evade suppression.
7. The pathway display hides unobserved offer, preference, completion, or burden states.
8. The improvement option lacks process, outcome, access, safety, or balancing measures.
9. A prohibited or post-prediction feature enters either model.
10. The two models use different prediction times, features, splits, rows, or thresholds.
11. More than one ML model is searched.
12. Evaluation rows affect fitting, tuning, or threshold selection.
13. Calibration, error counts, error costs, subgroup support, or failure cases are missing.
14. The recommendation relies only on a performance metric.
15. Machine learning replaces the transparent benchmark or universal prospective measurement.
16. The package authorizes real clinical implementation or deployment.
17. The learner package cannot be reproduced.
18. AI use, human verification, or accountable ownership is missing.
19. The Week 6 checkpoint assigns more or fewer than 45 points or scores a component twice.
20. The progression decision is missing, internally inconsistent, or outside the allowed values.

## 20. Reproducibility, validation, and mutation rejection

The reference build must be deterministic under the frozen environment, seed, inputs, contracts, and split. Validation must cover the module root, complete reference workspace, learner starter, copied validator, and cumulative checkpoint.

The smallest complete check set includes:

- two independent output builds match byte for byte;
- two independently assembled reference workspaces match;
- the learner workspace contains prompts but no reference outputs;
- an existing target is never overwritten;
- changed cohort, care-pattern, expected-outcome, contract, or generated output is rejected;
- leaked feature, changed split, changed threshold, changed support rule, invalid score, and invalid progression mutations are rejected;
- all exact row counts, field counts, byte counts, and SHA-256 values in the release record are verified; and
- the pathway SVG has an accessible title and description plus exact table alternatives.

The validator uses only package dependencies already required for the analysis. It does not add a new test framework.

At first release, module-root validation passes 153 checks, complete-reference validation passes 189 checks, and learner-starter validation passes 100 starter checks.

## 21. Progression, reference finding, reviewers, version, and known issues

Allowed module dispositions are `continue`, `continue with conditions`, `revise`, or `refer`. Module 07 construction is permitted only for `continue` or `continue with conditions`. Clinical implementation and model deployment remain prohibited.

The expected reference conclusion is:

- the site spread remains a measurement question, not evidence of site performance;
- the retrospective source cannot answer whether offer, access, completion, preference, or burden differs across groups;
- a capacity-aware prospective scheduling test is feasible enough for leadership review if those states are collected and safety and balancing measures are retained;
- the random forest does not materially improve the held-out evidence and does not change the improvement decision; and
- the transparent model and universal prospective workflow measurement remain the preferred benchmark.

Required reviewers before alpha are a hospital medicine clinician, clinical improvement reviewer, health-services methods reviewer, equity reviewer, clinical informatician, accessibility reviewer, privacy reviewer, responsible-AI reviewer, and independent instructor. Module 07 clinical leadership remains assigned to Joe Joseph, MD, subject to identity and publishable-biography confirmation.

Known limits are material but bounded: the source is synthetic; demographic fields are simplified source categories; the retrospective records do not observe key access states; the held-out set has 17 events; subgroup evaluation is sparse; the error costs are educational; and neither model is suitable for clinical deployment.

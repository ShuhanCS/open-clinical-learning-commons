# APP-4 Module 06 specification: Safety case, monitoring, governance, and embedded machine learning

## 1. Module identity, purpose, timing, and workload

- Course: `APP-4: Data for Clinical Decision Support`.
- Module ID: `oclc-app4-06`.
- Module title: `Safety case, monitoring, governance, and embedded machine learning`.
- Module version: `0.1.0`.
- Commons release: `0.83.0`.
- Workload: `16.0 hours`.
- Safety, monitoring, and governance: `8.0 hours`.
- Embedded machine learning: `8.0 hours`.
- Course points added here: `0`.
- Assessment role: required noncompensable gate for the cumulative Week 6 release.
- Package: `courses/clinical-decision-support/modules/06-safety-monitoring-governance-embedded-ml/`.

The course uses a 7.5-week planning model. Week 6 is the cumulative workflow, sandbox, safety, monitoring, governance, and ML checkpoint. The official section calendar controls the actual due date.

This module turns the Module 05 sandbox evidence into a safety and monitoring case. Learners must preserve the successes, visible failures, silent failure, blocked accessibility defect, and unresolved authority limits. The embedded ML exercise then asks whether one fixed gradient-boosted challenger earns replacement of the accepted transparent model under rules declared before the evaluation sets are inspected.

The lesson is not that a complex model is good or bad. The lesson is that a model decision depends on evidence, workflow, burden, missed cases, subgroup support, drift, reproducibility, interpretation, and governance together.

## 2. Place in the course and the Week 6 checkpoint

Modules 01 through 03 form the technical evidence block. Module 04 owns the 25-point workflow, alert-burden, human-factors, access, equity, and privacy review. Module 05 owns the local nonproduction sandbox and failure-mode gate. Module 06 owns the safety case, monitoring, governance, incident life cycle, and fixed ML comparison.

The Week 6 score is fixed as follows:

| Component | Course points | Checkpoint treatment |
|---|---:|---|
| Module 04 workflow, burden, and equity review | 25 | counted once |
| Module 05 sandbox and failure modes | 0 | required gate |
| Module 06 safety, monitoring, governance, and ML | 0 | required gate |
| Week 6 total | 25 | no duplicate points |

A learner cannot compensate for a failed safety, monitoring, leakage, subgroup, reproduction, or authority gate with the Module 04 point total.

The passing Module 06 disposition is `continue with conditions`. That disposition permits Checkpoint 02 curriculum assembly only. It does not permit silent-mode evaluation, real-patient scoring, clinical alerting, implementation, a production connection, or deployment.

## 3. Decision question, accountable owner, and authority boundary

### Decision question

Is the safety and monitoring case ready for clinician leadership review, and does the fixed ML challenger change the recommendation?

### Accountable owner

The teaching decision belongs to the fictional `CGH-GIM-01 clinical decision support governance council`. Individual records name clinical, patient-safety, data, terminology, service, model, equity, accessibility, evaluation, workflow, and governance owners.

### Allowed decisions

Learners may recommend one of four curriculum dispositions:

- `continue with conditions`;
- `revise`;
- `refer`; or
- `stop`.

They may retain or reject the fixed challenger as a replacement under the predeclared all-rules contract. They may also identify evidence that would be needed before a stopped or referred question could return.

### Prohibited decisions and actions

This module cannot:

- change the intended use;
- change `panel-t003` from a passive mechanics fixture;
- select or accept a clinical threshold;
- interpret `0.03000000` as an approved cutoff;
- rewrite or remove a Module 05 failure;
- automate an alert, order, referral, diagnosis, or other clinical action;
- score a real patient;
- begin silent-mode evaluation;
- implement or connect a production service;
- deploy either model; or
- claim local validity, utility, safety, fairness, FHIR conformance, or CDS Hooks conformance.

## 4. Protected Module 05 handoff and nested evidence chain

Every learner and reference workspace embeds the complete accepted Module 05 reference workspace under `upstream/module05/`.

The exact upstream identity is:

| Property | Required value |
|---|---|
| Module | `oclc-app4-05@0.1.0` |
| Commons release | `0.82.0` |
| Reference files | 341 |
| Immutable manifest rows | 324 |
| Manifest bytes | 75,019 |
| Manifest SHA-256 | `6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf` |
| Sandbox cases | 31 |
| Prefetch resources | 184 |
| Trace events | 61 |
| Detected silent failures | 1 |
| Blocked accessibility defects | 1 |
| Module 05 gates | 20 of 20 pass |
| Carried Module 04 score | 25.00 of 25.00, exactly once |
| Design | `panel-t003` |
| Threshold fixture | `0.03000000`, unaccepted |
| Accepted clinical threshold | none |

The nested Module 05 workspace also preserves all 302 Module 04 files and the 204-row immutable Week 3 chain. Module 06 may add safety and model-comparison evidence around this release. It may not recompute, clean, simplify, or reinterpret the upstream release.

## 5. Assessable learning outcomes

By the end of the module, a learner can:

1. translate a complete prototype failure register into a structured hazard register;
2. distinguish a seeded teaching failure from an observed clinical incident or incident rate;
3. map each hazard to cause, consequence, detection, control, owner, escalation, fallback, stop, restart, and retirement;
4. define a monitoring measure with a source, cadence, owner, threshold origin, unavailable state, and human action;
5. detect a silent failure through independent request, response, terminal-trace, and human-notice ledgers;
6. explain why a service log alone cannot detect the seeded silent failure;
7. distinguish a teaching trigger from a validated local control limit;
8. assign decision rights across clinical, safety, data, model, equity, accessibility, service, and governance owners;
9. preserve temporal separation between development, holdout, and later-cycle stress evidence;
10. fit one fixed gradient-boosted classifier without search or holdout-guided tuning;
11. compare transparent and challenger models on common rows using calibration, Brier score, log loss, ROC AUC, burden, missed cases, subgroup support, and transport behavior;
12. apply all predeclared replacement rules even when some metrics favor the challenger;
13. retain a simpler model when the complex challenger fails any required rule;
14. carry a scored component forward exactly once while preserving zero-point gates; and
15. hand a bounded Week 6 package to clinician leadership without expanding course authority.

## 6. Concept ownership and boundaries

### Module 06 owns

- hazard and safety-case structure;
- monitoring definitions and unavailable states;
- silent-failure surveillance;
- incident, escalation, fallback, stop, restart, and retirement rules;
- governance ownership and decision rights;
- the fixed challenger contract;
- leakage checks;
- transparent-versus-challenger comparison;
- the all-rules replacement decision; and
- the protected Checkpoint 02 handoff.

### Module 06 reuses without changing

- Module 01 intended use and clinical question;
- Module 02 logic, inputs, suppression, and missing-input rules;
- Module 03 cohort, target, predictors, weights, splits, threshold candidates, transparent predictions, and subgroup support;
- Module 04 workflow, burden, alert budget, equity review, score, `panel-t003`, and threshold role; and
- Module 05 runtime, case matrix, responses, traces, failure findings, and authority limits.

### Module 07 owns later

- clinician-led interpretation and challenge;
- the product and safety brief;
- disagreement and accountability records;
- the bounded silent-mode evaluation proposal, if recommended;
- communication to clinical and operational readers; and
- the final defense.

Module 07 cannot use leadership discussion to change the frozen cohort, model results, threshold role, prototype result, failure register, score, or Week 6 gate result.

## 7. Source authority, provenance, and teaching claim limits

### Historical public model evidence

The model comparison reuses 7,544 historical public NHANES teaching rows from Module 03. The target is an observed HbA1c result at or above 6.5 percent. It is not a diagnosis. The source cannot establish local clinical validity, workflow utility, or patient benefit.

| Artifact | Rows | SHA-256 | Role |
|---|---:|---|---|
| `model-cohort.csv.gz` | 7,544 | `5ee21d19ecaca1e95e57910b2ca12b27960473eb16be4edac0b62b96de731304` | frozen target, predictors, groups, weights, and partitions |
| `predictions.csv.gz` | 7,544 | `2bd6064b557c34936e7c8ef606dc0ac5ffa7751095d7100d3312e69c411f122f` | accepted transparent probabilities |
| `subgroup-support.csv` | 48 | `064882d3dafcb8d652a86c6baabc083d8f9c0387604af67c4753af0345deafc6` | frozen support states and group definitions |

### Synthetic safety evidence

The Module 05 failures and Module 06 monitoring scenarios are seeded teaching fixtures. They show whether the analysis and governance process can detect known conditions. They do not estimate how often those conditions occur in clinical practice.

### Reproducibility boundary

Source hashes and deterministic outputs establish computational identity. They do not replace clinical, patient-safety, model-risk, workflow, equity, accessibility, privacy, security, or patient review.

## 8. Safety-case and hazard-register contract

The generated hazard register contains 22 rows:

- 17 hazards carried directly from the Module 05 failure register; and
- five prospective Module 06 hazards for outcome availability, calibration drift, subgroup support erosion, override capture failure, and governance delay.

Every row must contain:

| Field | Required meaning |
|---|---|
| Hazard ID | stable `H01` through `H22` identifier |
| Origin | Module 05 failure identity or Module 06 prospective source |
| Hazard | the unsafe or misleading state |
| Cause | the declared mechanism that can create the state |
| Consequence | the human, workflow, evidence, or governance effect |
| Detection | the evidence that makes the state visible |
| Control | the action that bounds the state |
| Owner | the accountable role |
| Escalation | who receives the unresolved condition |
| Fallback | the bounded state used while the issue is unresolved |
| Stop rule | when the affected evaluation or release must stop |
| Restart rule | evidence required before work resumes |
| Retirement trigger | evidence that the concept or control should be retired |
| Evidence status | seeded or prospective teaching evidence, not observed incidence |

A blank owner, unavailable detection source, hidden failure, automatic action, or absent stop and restart route blocks the release.

The learner's `hazard-review.csv` records control adequacy, residual risk, owner confirmation, disposition, and status for each `H01` through `H22`.

## 9. Monitoring measure contract

The generated register contains 20 measures. Each measure has a definition, source, cadence, owner, threshold origin, trigger, unavailable state, human action, and `automatic_action = none`.

| ID | Measure | Main question |
|---|---|---|
| M01 | eligible opportunities | is the denominator stable and interpretable? |
| M02 | input availability | are all required inputs present? |
| M03 | firing | how often does the candidate response appear? |
| M04 | suppression | are declared suppression reasons stable and visible? |
| M05 | burden | how many candidate flags occur per 1,000 eligible opportunities? |
| M06 | human response | can acknowledgement, dismissal, deferral, and unavailable response be observed? |
| M07 | latency | does the service remain within the teaching budget? |
| M08 | errors | are visible failures classified and explained? |
| M09 | silent failure | do four independent ledgers reconcile? |
| M10 | outcome availability | can calibration and outcome review be performed? |
| M11 | calibration | do mean probability and observed outcome remain aligned? |
| M12 | discrimination | does weighted ROC AUC remain within the declared reference? |
| M13 | drift | how do later-cycle performance and burden differ from holdout? |
| M14 | subgroup support | are denominators, events, follow-up, and support sufficient? |
| M15 | version | do requests and responses use accepted teaching versions? |
| M16 | incidents | are severe or repeated related hazards accumulating? |
| M17 | overrides | are human disagreement and hidden work observable? |
| M18 | accessibility | do released cards pass the declared structure checks? |
| M19 | duplicate suppression | are repeat hook instances suppressed with a trace reason? |
| M20 | semantic rejects | are terminology and unit mismatches rejected visibly? |

### Unavailable-state rule

A missing numerator, denominator, outcome, response ledger, support count, or version record cannot be converted to zero, normal, safe, or unchanged. The learner must state that the measure is unavailable, name the missing source, stop the affected interpretation, and assign a human next action.

### Threshold-origin rule

Every trigger must name its origin. Origins include an accepted historical baseline, a seeded failure, a prior module budget, a predeclared replacement rule, or a prospective governance rule. A teaching trigger is not a validated clinical control limit.

## 10. Silent-failure, monitoring-scenario, and incident contract

### Silent-failure definition

A silent failure is `a received request with no response, no terminal trace, and no human notice`.

The four independent ledgers are:

1. request received;
2. response present;
3. terminal trace present; and
4. human notice present.

The request ledger supplies the denominator. A request present in the first ledger and absent from all three remaining ledgers counts once. The Module 05 service log cannot replace this test because the seeded case disappears after receipt.

### Eight seeded monitoring scenarios

| ID | Seeded truth | Expected response |
|---|---|---|
| S01 | all ledgers reconcile and no trigger fires | continue human review |
| S02 | required input availability falls to 96 percent | show unavailable and investigate |
| S03 | suppression reason mix shifts by 25 percent | verify logic, case mix, and traces |
| S04 | one received request becomes silent | stop affected evaluation and escalate |
| S05 | absolute calibration error exceeds 0.010 | pause claims and investigate |
| S06 | one group loses declared event support | suppress group result and refer |
| S07 | one request uses an unreviewed model version | reject visibly and stop affected release |
| S08 | one card loses the required summary | block release and return to accessibility review |

These are exercises with known truth, not clinical event rates.

### Incident review

The incident record must preserve the original evidence, affected hazard, detection time, owner, action, escalation, closure evidence, restart decision, and retirement consideration. A resolved incident cannot be deleted from the teaching record.

## 11. Governance, escalation, fallback, stop, restart, and retirement

The package contains 12 escalation routes. Every route is human owned and has `automatic_action = none`.

Required governance roles are:

- clinical owner;
- patient-safety owner;
- data steward;
- model steward;
- equity steward;
- accessibility owner;
- service owner; and
- governance council.

Each role must name what it is accountable for, its decision right, the evidence required, and the next escalation point.

### Stop

Stop the affected evaluation or release when a control cannot bound the hazard, required evidence is unavailable, a severe incident occurs, a silent failure is detected, an unreviewed version appears, or a required gate fails.

### Restart

Restart requires correction evidence, a passing repeat fixture, reconciliation where relevant, named-owner confirmation, and a recorded governance decision. A passing code test alone is not sufficient when the stop condition concerns clinical meaning, safety, support, or authority.

### Retirement

Retirement must be considered when a control cannot be restored, the intended use is no longer supportable, repeated incidents remain unresolved, outcome observation cannot support evaluation, or required governance ownership is unavailable.

## 12. Fixed machine-learning population, features, and fit contract

### Common population

Both models use the same 7,544 rows:

| Partition | Cycles | Rows | Events | Role |
|---|---|---:|---:|---|
| Development | 2013-2014 and 2015-2016 | 3,652 | 156 | fitting only |
| Temporal holdout | 2017-2018 | 1,806 | 97 | untouched primary evaluation |
| Transport stress | 2021-2023 | 2,086 | 75 | untouched later-cycle stress evaluation |

### Target

`LBXGH at or above 6.5 percent; observed laboratory result, not diagnosis`.

### Predictors

1. age centered at 50 and divided by ten;
2. BMI centered at 30 kg/m2 and divided by five; and
3. source-recorded female indicator.

No new feature, interaction, target proxy, outcome-derived value, post-index value, missing-value imputation, group-specific feature, or external source may be added.

### Fixed challenger

| Setting | Value |
|---|---|
| Class | `sklearn.ensemble.GradientBoostingClassifier` |
| Estimators | 80 |
| Learning rate | 0.05 |
| Maximum depth | 2 |
| Minimum leaf size | 50 |
| Subsample | 1.0 |
| Random state | 7400600 |
| Search | none |
| Holdout-guided tuning | prohibited |

Survey weights are normalized within the development set for fitting. Their relative values remain unchanged. Holdout and stress weights are used only in evaluation metrics.

The model is fit once. A rerun must reproduce the same prediction file and every derived comparison byte for byte.

## 13. Evaluation, threshold, subgroup, and drift contract

### Model-level measures

Both models are compared on:

- weighted prevalence;
- weighted mean probability;
- absolute calibration error;
- weighted Brier score;
- weighted log loss; and
- weighted ROC AUC.

### Candidate thresholds

The same six values are evaluated for both models and all three partitions:

`0.02000000`, `0.03000000`, `0.04000000`, `0.05000000`, `0.07500000`, and `0.10000000`.

Every row must state `evidence candidate, not selected or accepted`. The `0.03000000` value also remains the unaccepted Module 05 sandbox fixture. Comparing burden or missed cases at a candidate value does not accept it.

Threshold measures are:

- weighted flag rate;
- weighted sensitivity;
- weighted specificity;
- weighted missed cases per 1,000; and
- weighted flags per 1,000.

### Subgroup support

The comparison preserves the Module 03 group definitions and support states for recorded sex, age band, BMI band, and race and Hispanic-origin categories. Unsupported AUC values remain blank. Results are descriptive support checks and cannot rank groups, certify fairness, or create group-specific clinical action.

### Drift

The later 2021-2023 cycle is a transport stress comparison. Differences may be described. The data do not identify why a difference occurred and do not establish local temporal performance.

## 14. Predeclared replacement rules and exact reference result

The challenger replaces the transparent model only if every rule passes.

| Rule | Required result | Reference status | Reference finding |
|---|---|---|---|
| R01 | same evidence, target, predictors, cutoffs, weights, and rows | pass | 12 source and split checks reviewed |
| R02 | one fixed fit with no holdout-guided tuning | pass | fixed classifier fit once |
| R03 | temporal-holdout ROC AUC is not lower | fail | difference `-0.00743486` |
| R04 | transport ROC AUC is no more than 0.010 lower | fail | difference `-0.01928938` |
| R05 | Brier score is not worse on either evaluation set | pass | holdout `-0.00021620`; stress `-0.00033886` |
| R06 | calibration error is at most 0.005 on holdout and 0.010 on stress | pass | holdout `0.00075165`; stress `0.00304604` |
| R07 | burden differs by at most 0.100 and missed cases rise by at most 2 per 1,000 | pass | max flag difference `0.09474026`; max missed increase `1.93231763` |
| R08 | supported subgroup ROC AUC degradation is at most 0.050 | fail | maximum degradation `0.10385240` |
| R09 | all leakage and reproducibility checks pass | pass | 12 of 12 pass |
| R10 | global importance is complete and normalized | pass | three predictors sum to 1.00000000 |
| R11 | intended use, threshold role, workflow, and authority stay fixed | pass | no threshold or clinical authority added |

The challenger passes 8 of 11 rules. The transparent model remains accepted for the teaching comparison.

The challenger improves weighted Brier score and has smaller absolute calibration error on the holdout. Those findings do not erase the discrimination losses or the supported subgroup failure. Better development performance also cannot substitute for untouched evaluation evidence.

Global impurity importance is available for all three predictors. It does not provide direction, causality, a patient-level explanation, local reliability, or clinical meaning.

## 15. Worked example

### Part A: silent failure

Start with Module 05 case `M05-F15`.

1. Confirm that the request ledger contains the request.
2. Search the response ledger and confirm the response is absent.
3. Search the terminal-trace ledger and confirm the terminal trace is absent.
4. Search the human-notice ledger and confirm the notice is absent.
5. Count the case once as a silent failure.
6. Record the owner as the patient-safety owner.
7. Apply the M09 trigger of one or more events.
8. Stop the affected evaluation, preserve all four ledger states, and escalate to the governance council.
9. Do not estimate a clinical failure rate from the one seeded case.

The wrong approach is to inspect only the service log and declare success because no error appears. The absence of a service-log error is part of the seeded failure.

### Part B: model replacement

The challenger has a lower temporal-holdout Brier score than the transparent model:

- transparent: `0.02811126`;
- challenger: `0.02789506`; and
- challenger minus transparent: `-0.00021620`.

It also has lower temporal-holdout ROC AUC:

- transparent: `0.68783144`;
- challenger: `0.68039658`; and
- challenger minus transparent: `-0.00743486`.

R05 passes, but R03 fails. The learner continues through every remaining rule and finds R04 and R08 also fail. The correct decision is `retain transparent model`. Selecting the metric that favors the challenger would violate the predeclared contract.

## 16. Guided practice

### Exercise 1: complete the inherited hazard chain

Assign learners one or more of H01 through H17. For each hazard, require them to locate the exact Module 05 case, failure, cause, detection evidence, control, owner, and visible or silent state. They then add consequence, escalation, fallback, stop, restart, and retirement.

The group must answer:

- What can a person misunderstand?
- Which evidence makes the state visible?
- What happens if that evidence is unavailable?
- Who can stop the affected evaluation?
- What evidence is needed to restart?
- When should the control or concept be retired?

### Exercise 2: reconcile the monitoring plan

Give each group five measures. Require the group to identify numerator, denominator, source ledger, cadence, owner, trigger origin, unavailable state, and human action. Recombine the groups and reject duplicate measures with conflicting definitions.

### Exercise 3: scenario tabletop

Run S02, S04, S06, and S08. Learners must identify the first triggered measure, named owner, fallback, stop condition, and prohibited automatic action.

### Exercise 4: freeze the ML contract

Before results are shown, learners sign off on:

- target;
- three predictors;
- weights;
- development cycles;
- temporal holdout;
- transport stress set;
- six candidate thresholds;
- missing-input rule;
- fixed model settings;
- 11 replacement rules; and
- all prohibited actions.

The instructor then runs the builder once.

## 17. Independent exercise and 16-hour sequence

| Block | Hours | Learner work |
|---|---:|---|
| Upstream release and authority review | 1.0 | verify Module 05 identity, score, gates, failures, design, and threshold role |
| Hazard construction | 2.0 | review H01 through H22 and residual conditions |
| Monitoring definitions | 2.0 | complete M01 through M20 with unavailable states |
| Incident and life-cycle governance | 2.0 | complete escalation, fallback, stop, restart, retirement, and accountability |
| Safety-case synthesis | 1.0 | make the bounded safety disposition |
| Fixed ML contract and leakage audit | 1.5 | freeze the model and verify L01 through L12 |
| Model fit and model-level evaluation | 2.0 | reproduce predictions and compare calibration, Brier, log loss, and AUC |
| Threshold burden and missed cases | 1.5 | review all six candidates without selecting one |
| Subgroup support and transport | 1.0 | apply support boundaries and drift language |
| Replacement decision | 1.0 | apply R01 through R11 and retain or replace |
| Release, defense, and handoff | 1.0 | validate, defend, and freeze Checkpoint 02 input |
| Total | 16.0 | complete Module 06 package |

The independent submission must answer two questions in one coherent decision:

1. Is the safety and monitoring case ready for clinician leadership review?
2. Does the fixed challenger replace the transparent model?

The learner must support both answers from exact files and rows. Unsupported confidence, an invented local claim, or a decision based on one favorable metric fails the relevant gate.

## 18. Exact submission, scoring, gates, and progression

### Learner records

The learner submits these 17 assessed files:

1. `safety-case.md`;
2. `hazard-review.csv`;
3. `monitoring-plan.csv`;
4. `silent-failure-monitoring.md`;
5. `incident-escalation-review.csv`;
6. `fallback-stop-restart-retirement.csv`;
7. `governance-accountability.csv`;
8. `ml-contract-review.md`;
9. `model-comparison.md`;
10. `threshold-burden-review.csv`;
11. `subgroup-drift-review.csv`;
12. `leakage-interpretability-review.md`;
13. `checkpoint-score-carryforward.csv`;
14. `gate-results.csv`;
15. `reproducibility-check.md`;
16. `ai-use.md`; and
17. `progression-checkpoint02-handoff.md`.

### Immutable evidence

The workspace also contains 369 immutable manifest rows:

- 15 Module 06 controls;
- 13 Module 06 generated outputs; and
- all 341 Module 05 reference files.

The assembled workspace contains 387 files.

### Gates

| Gate | Required evidence |
|---|---|
| G01 | exact Module 05 release identity |
| G02 | exact nested Module 04 and Week 3 chain |
| G03 | all 17 Module 05 failures preserved |
| G04 | four-ledger silent-failure finding preserved |
| G05 | blocked accessibility defect preserved |
| G06 | all 22 hazards reviewed |
| G07 | fallback, stop, restart, and retirement complete |
| G08 | all 20 monitoring measures complete |
| G09 | cadence, owner, origin, unavailable state, and human action complete |
| G10 | human escalation only, with no automatic action |
| G11 | incident fallback and stop route complete |
| G12 | governance roles and decision rights complete |
| G13 | fixed ML contract preserved |
| G14 | common evidence, target, predictors, weights, and rows preserved |
| G15 | temporal separation and no tuning verified |
| G16 | calibration and discrimination reviewed |
| G17 | all candidate thresholds reviewed without acceptance |
| G18 | subgroup support and drift limits preserved |
| G19 | all-rules replacement decision applied |
| G20 | reproduction and AI accountability complete |
| G21 | 25 Module 04 points carried once; Module 06 adds zero |
| G22 | progression and authority remain bounded |

Every gate is noncompensable. The passing reference has 22 of 22 gates and a Week 6 score of 25.00 of 25.00 counted once.

## 19. Accessibility, equity, privacy, security, responsible claims, and AI policy

### Accessibility

The Module 05 malformed card remains blocked. Safety and monitoring records must not use color alone, unexplained abbreviations, unlabeled status, or blank unavailable values. Structured tables require clear headers and plain-language interpretation.

### Equity and support

Group comparisons preserve declared denominators, events, support states, and blank unsupported AUC values. Learners may describe a supported historical difference. They may not rank groups, certify fairness, assign a group cause, create a group-specific threshold, or infer local clinical behavior.

### Privacy and security

The package uses historical public or synthetic teaching evidence. Learners may not add real patient data, identifiers, credentials, tokens, local personal paths, live endpoints, or production configuration. Network access is not needed for the release checks.

### Responsible claims

The words `safe`, `effective`, `validated`, `fair`, `compliant`, and `ready for deployment` require evidence this module does not provide. The strongest supported statement is that the curriculum package has a complete, reproducible safety and monitoring design ready for bounded Week 6 and clinician-leadership review.

### AI and agent policy

Agents may help draft records, run deterministic code, compare files, and identify inconsistencies. Humans retain hazard acceptability, clinical meaning, trigger approval, model replacement, threshold acceptance, progression, stop, restart, retirement, and every clinical or production decision.

An agent may not:

- change intended use;
- accept a threshold;
- hide a failure;
- tune after holdout inspection;
- invent an unavailable value or patient outcome;
- score a real patient;
- begin silent mode;
- implement, connect production, or deploy; or
- present its own output as independent human review.

## 20. Runnable acceptance checks and deliberate failure routes

### Supported environment

- Python 3.12;
- NumPy 2.0.2; and
- scikit-learn 1.9.0.

### Commands

From the module directory:

```powershell
python build_evidence.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

The evidence self-check builds the fixed challenger twice and confirms byte-identical outputs. The workspace self-check assembles learner and reference workspaces, protects existing destinations, and confirms their common immutable manifest. The validator checks the complete reference, learner starter, a copied reference, and deliberate failures.

The release validator performs 1,230 reference checks and 1,152 learner checks. It rejects 22 deliberate failure routes:

1. missing assessed record;
2. changed Module 06 immutable evidence;
3. changed Module 05 manifest;
4. removed nested Module 04 file;
5. changed hazard identity;
6. hidden inherited failure;
7. failed hazard review;
8. single-ledger silent-failure substitution;
9. changed monitoring identity;
10. missing monitoring owner;
11. automatic action added;
12. unsafe fallback added;
13. governance role changed;
14. holdout-guided tuning added;
15. model performance rewritten;
16. threshold accepted;
17. challenger accepted despite failed rules;
18. subgroup degradation hidden;
19. score inflated;
20. gate failed;
21. agent authority expanded; and
22. progression expanded to production deployment.

## 21. Release status, reviewers, known issues, and protected handoff

### Release status

- Module version: `0.1.0`.
- Commons release: `0.83.0`.
- Status: runnable release candidate.
- Evidence: 22 hazards, 20 measures, eight monitoring scenarios, 12 escalation rules, 7,544 prediction rows, 11 replacement rules, and 22 invariants.
- ML result: 8 of 11 replacement rules pass; transparent model retained.
- Workspace: 369 immutable rows, 17 assessed records, 387 files.
- Workspace manifest: 88,971 bytes with SHA-256 `e6553079256fdd2a37ab042a87c2ec69812cad7074abefa7d7907e6ee7b56f7d`.
- Validation: 1,230 reference checks, 1,152 learner checks, copied validation pass, and 22 rejected failure routes.
- Score: 25.00 Module 04 points carried once; Module 06 adds 0.00.
- Progression: `continue with conditions`.

### Required named review before alpha

The runnable teaching release does not claim completed named review. Before alpha, the course owner must record human review from:

- clinical decision support and clinician leadership;
- patient safety;
- workflow and human factors;
- FHIR and CDS Hooks interoperability;
- model risk, statistics, and independent reproduction;
- patient and caregiver perspective;
- equity and language access;
- disability access and accessibility;
- privacy and security; and
- curriculum and assessment leadership.

### Known issues

- The official APP-4 section and half-term dates remain to be assigned from the published academic calendar.
- Monitoring triggers are teaching rules, not validated local clinical control limits.
- The public-survey model comparison does not establish local validity, utility, safety, or fairness.
- The FHIR and CDS Hooks-shaped sandbox remains a teaching shape rather than a conformance artifact.

### Protected Checkpoint 02 handoff

Checkpoint 02 must freeze this complete 387-file release and its release manifest. It must preserve:

- the full 341-file Module 05 workspace;
- all 302 nested Module 04 files and the complete Week 3 chain;
- all 31 sandbox cases and every response and trace;
- all 17 inherited failure modes;
- the detected silent failure and blocked accessibility defect;
- all 22 hazards, 20 monitoring measures, eight scenarios, and 12 escalation rules;
- all 7,544 common model rows and predictions;
- the six unaccepted threshold candidates;
- the 11 replacement rules and failed R03, R04, and R08 results;
- the retained transparent model;
- `panel-t003` and the unaccepted `0.03000000` fixture;
- all 22 Module 06 gates; and
- the 25-point score exactly once.

Checkpoint 02 may assemble, validate, and defend the cumulative Week 6 curriculum release. It may not recompute accepted evidence, rewrite a failure, tune the model, select a threshold, expand intended use, score a real patient, begin silent mode, alert or act clinically, implement, connect production, or deploy.

After Checkpoint 02 is accepted, Module 07 may add clinician leadership, communication, accountability, disagreement, evaluation-proposal, and defense records without changing the frozen Week 3 or Week 6 evidence.

# APP-2 Module 06: Partnered improvement and embedded machine learning

## 1. Module identity, duration, and place in the course

- Module ID: `oclc-app2-06`.
- Course: APP-2, Data for Patient Experience and Engagement.
- Course position: instructional Week 6.
- Total learner time: 16.0 hours.
- Patient partnership and improvement work: 8.0 hours.
- Embedded machine-learning extension: 8.0 hours.
- Submission: cumulative Week 6 linked-evidence and patient-voice release.
- Prerequisites: accepted APP-2 Modules 01 through 05 and the accepted Week 3 checkpoint identity.
- Module version at first runnable release: `0.1.0`.
- Commons release at first runnable release: `0.61.0`.

Module 06 finishes the six-week technical case. It adds no course points. It supplies the required partnership, improvement, and machine-learning gates for the Week 6 checkpoint, which carries the Module 04 score of 25 points and the Module 05 score of 20 points exactly once.

## 2. Decision, readers, and intended use

Learners answer two linked questions:

1. Does the accepted evidence support a feasible, accessible, patient-partnered improvement proposal?
2. Does one bounded machine-learning response model materially change the response-adjustment decision compared with the transparent cell-weight benchmark?

The primary readers are a patient or caregiver partner, a patient-experience lead, an improvement reviewer, a survey-methods reviewer, and a model reviewer. The package may enter Module 07 clinician and patient leadership review. It may not authorize fielding, clinical action, patient targeting, group ranking, official HCAHPS reporting, or model deployment.

## 3. Accepted upstream identity and immutable handoff

The build accepts only the following versioned evidence:

- APP-2 Module 03, version `0.1.0`, Commons `0.58.0`.
- Module 03 `adult-inpatient-frame.csv`: 1,255 rows, 19 fields, 294,946 bytes, SHA-256 `96e7b493aabf51bdb6c6072e2175ebe560a8ab211287983c6b38e851244e8d4a`.
- Module 03 `response-study.csv`: 1,255 rows, 16 fields, 271,547 bytes, SHA-256 `eb593a7883c10ff8b83456a4b66b7c8132a3a787d1151d1baf4093d21f10a0af`.
- Module 03 `response-contract.json`: 3,224 bytes, SHA-256 `399e60c91895b6ce797b20c9229a21056be7bddb860b469aedc2ab2b8a39b133`.
- Module 03 `release.json`: 6,161 bytes, SHA-256 `58e15614fa749d21cccaccc8cd952d114c23ab7cb4b3d87c73b22c5bbad62352`.
- APP-2 Module 04 `release.json`: 5,063 bytes, SHA-256 `de31b805351946d644dccc5125deffdffdb993470fbdd74670278c2ca6e7e1d0`.
- APP-2 Module 05, version `0.1.0`, Commons `0.60.0`.
- Module 05 `release.json`: 5,261 bytes, SHA-256 `a73f007335ac7ce4a3c8b79eeb164b141288b70a6f5d55bf4414b231b6ee22a8`.
- Module 05 `voice-equity-contract.json`: 1,205 bytes, SHA-256 `43317518d8c65dc3a498083129b2227ff6f877f114185eeb8775a3e550cd42e3`.
- Module 05 group-support, estimate, contrast, channel-exclusion, equity-memo, and progression files with their recorded SHA-256 identities.

The accepted handoff is fixed:

- The target is 1,255 public-derived MEPS adult inpatient frame records with positive person weights.
- The response generator has 782 synthetic respondents and 473 synthetic nonrespondents.
- Q22, Q23, mode, response, item missingness, and comment fields remain synthetic procedural teaching data.
- Module 04 owns linked access, communication, engagement, service-use, denominator, and uncertainty evidence.
- Module 05 owns the 420-comment synthetic corpus, human coding benchmark, assisted classification audit, group support, 20-point score, and equity claim limits.
- The supported lower-income teaching contrasts remain descriptive signals. They do not prove inequity or cause.
- Comment text is prohibited from model training.

The builder must reject a changed input file, changed row identity, duplicate record, missing record, altered response status, changed Q22 or Q23 truth, changed group-support rule, or unexpected extra row.

## 4. Source, data classes, rights, and row rule

The public-derived frame comes from the accepted AHRQ MEPS HC-256 source package frozen in Module 03. Module 06 reads the released teaching extracts and does not re-download or modify the source files.

The row is one accepted frame record. `frame_record_id` must match one-to-one between the public-derived frame and synthetic response overlay. Public-derived fields, synthetic procedural fields, and reference teaching records remain visibly separated.

No real comment text or actual patient-partner statement is included in the reference solution. The construction reference may demonstrate a simulated facilitation record only when every simulated interpretation is labelled as such. Before alpha use, a named patient or caregiver partner must review the evidence, record their own interpretations and disagreements, and approve the terms of participation.

## 5. Learning outcomes

By the end of the module, learners can:

1. Prepare a patient-partner session with decision rights, compensation, access, privacy, and disagreement rules.
2. Separate a simulated reference interpretation from an actual patient or caregiver contribution.
3. Turn bounded public and synthetic evidence into questions rather than claims about lived experience.
4. Record where patient-partner interpretation changes, narrows, or stops a proposal.
5. Build a driver diagram, workflow, and measure registry for an accessible discharge-information and feedback test.
6. Define implementation, process, outcome, response, access, safety, and balancing measures with exact denominators.
7. Fit a transparent response-adjustment benchmark and one bounded machine-learning model under the same fields and split.
8. compare calibration, response errors, weight stability, known-truth recovery, subgroup support, and failure cases.
9. Decide whether machine learning changes the response-adjustment decision without replacing patient partnership or transparent methods.
10. Release a reproducible 45-point Week 6 handoff without double counting.

## 6. Foundation skill revisited and ownership boundary

This course revisits foundations through a patient-experience decision. Learners again use row identity, categories, denominators, weights, missingness, uncertainty, accessible displays, validation, and reproducibility. Here those skills determine whether patient-experience evidence can support a partnered improvement proposal.

Ownership remains strict:

- Module 03 owns the target frame, response generator, item rules, transparent response cells, and known truth.
- Module 04 owns linkage, denominators, survey uncertainty, and the 25-point linked-evidence analysis.
- Module 05 owns qualitative coding, synthetic-comment boundaries, group support, equity interpretation, and the 20-point memo.
- Module 06 owns patient-partner interpretation, disagreement records, improvement design, and transparent-versus-ML response adjustment.
- Checkpoint 02 owns the cumulative Week 6 acceptance and 45-point handoff.
- Module 07 owns clinician and patient leadership, action, monitoring, accountability, and defense.

A more complex response model cannot repair invalid measurement, unsupported groups, synthetic patient voice, or missing patient partnership.

## 7. Explicitly out of scope

The module does not:

- claim that the reference facilitation record is actual patient engagement;
- infer patient need, preference, trust, discrimination, burden, or access from a group difference;
- treat synthetic comments as testimony, prevalence evidence, or saturation evidence;
- train any model on comment text, codes, themes, group labels, Q22, Q23, response probability truth, or post-response fields;
- use race, insurance, sex, or other audit-only fields as model predictors;
- merge small groups to make them reportable;
- search several model families, feature sets, splits, thresholds, or factor bounds;
- tune on evaluation rows;
- optimize only ROC AUC or another single score;
- let machine learning replace the transparent benchmark, patient-partner interpretation, human comment review, or fixed support rules;
- use a response model to target patients or choose contact intensity;
- change the official HCAHPS items or claim an official HCAHPS score;
- authorize a real improvement test, patient contact, clinical action, or model deployment; or
- award extra points for Module 06.

## 8. Lesson sequence and learner time

| Lesson | Hours | Work product |
|---|---:|---|
| Prepare partnership terms, evidence, and questions | 1.0 | engagement status and session plan |
| Review evidence with patient or caregiver partners | 2.0 | interpretation and disagreement record |
| Choose or stop a feasible improvement aim | 1.0 | bounded improvement brief |
| Map drivers and the proposed workflow | 1.5 | driver diagram and workflow |
| Define measures, burden, access alternatives, and feedback | 2.0 | measure registry and accountability record |
| Revise the proposal and record decision rights | 0.5 | revision rule |
| Freeze predictors, split, models, bounds, and decision rule | 1.5 | model contract review |
| Fit the transparent benchmark and bounded model | 2.0 | model performance and weights |
| Test Q22, Q23, and composite recovery | 1.5 | known-truth recovery table |
| Audit calibration, errors, subgroups, and failure cases | 2.0 | model and failure review |
| Decide whether ML changes the adjustment decision | 0.5 | ML comparison |
| Assemble and reproduce the Week 6 handoff | 0.5 | cumulative release candidate |
| Total | 16.0 | |

## 9. Patient-partner participation contract

Before an actual partner session, the team records:

- the named patient or caregiver partner and role;
- compensation and payment timing;
- preparation time and materials;
- decision rights over interpretation, proposed change, patient-facing language, and return of results;
- language, disability, format, technology, scheduling, and support needs;
- privacy and recording choices;
- permission for attribution or anonymity;
- a route to disagree without pressure to reach consensus; and
- a method for reviewing the final record.

The partner is not asked to represent all patients. The team must distinguish a partner's interpretation from a population estimate. A partner may add a question, narrow the proposal, require an access alternative, reject wording, request more evidence, or stop progression.

The reference package uses a clearly labelled simulated curriculum record because no named APP-2 patient or caregiver partner has been confirmed. This supports construction testing but remains a condition before alpha.

## 10. Evidence packet and interpretation protocol

The patient-partner evidence packet includes only bounded findings:

- the target, response, and item-missingness flow;
- the public-linked access and communication estimates;
- the Module 05 group-support table with unsupported estimates left blank;
- the lower-income delayed-cost and telehealth contrasts with confidence intervals and claim limits;
- the synthetic comment themes, channel audit, human-coding agreement, and synthetic boundary;
- the exact list of unmeasured constructs; and
- the current prohibitions on targeting, ranking, causal claims, and implementation.

For each item, partners record:

- what the result may mean;
- what it does not establish;
- what is missing from the evidence;
- whether the team's interpretation differs;
- what changed because of the discussion;
- who owns the follow-up; and
- whether the item is open, resolved, deferred, or stopping.

The record preserves disagreement. Consensus is not a passing condition.

## 11. Improvement question and bounded proposal

The reference improvement question is:

`Could a multilingual, accessible discharge-information and feedback workflow help patients understand warning signs and sources of help without adding cost, channel, disability-access, proxy, privacy, or after-hours burden?`

The reference proposal is a universal offer, not group targeting. Before discharge, the workflow records preferred language, contact channel, accessible format, proxy involvement, and whether the person wants follow-up. Staff use unchanged discharge content to check understanding of warning signs and where to get help. The workflow offers phone, mail, web, interpreter-supported, proxy-supported, and no-contact choices. A later feedback step asks about clarity and burden, returns aggregate findings to the patient advisory group, and records what changed.

The public and synthetic evidence does not establish that this workflow will help. Module 06 designs a feasible prospective test for leadership review. It does not implement the test.

## 12. Driver diagram and workflow contract

The driver diagram must connect one measurable aim to primary drivers, secondary drivers, and candidate changes. At minimum it addresses:

- patient choice and decision rights;
- understandable discharge information;
- language and communication access;
- non-digital and accessible format alternatives;
- after-hours and cost questions;
- reliable workflow ownership;
- response and missing-voice monitoring;
- return of results to patients; and
- a stop or revision route.

The workflow records eligibility, universal offer, preference, consent to contact, language, channel, format, proxy choice, teach-back status, follow-up attempt, response, burden, escalation, feedback return, and revision. Every step has an owner, timing, required input, output, failure mode, access alternative, and stop rule.

No blank prospective field is filled from a retrospective proxy.

## 13. Measure registry contract

The measure registry includes at least:

- implementation: eligible discharges where the workflow is available;
- process: universal offer recorded;
- process: language, channel, format, proxy, and contact preference recorded;
- process: discharge-information check completed or declined;
- response: follow-up opportunities, returns, total nonresponse, and item missingness;
- outcome: unchanged Q22 and Q23 item results, reported separately before any teaching composite;
- patient-reported outcome: clarity or burden measure defined for the prospective test without claiming validation;
- access: offer, completion, response, and burden by prespecified groups when support permits;
- balancing: discharge delay, staff time, unwanted contact, duplicate contact, interpreter delay, and digital burden;
- safety: failed escalation or incorrect routing, defined prospectively; and
- accountability: time from evidence review to patient-facing feedback and recorded revision.

Each measure has an operational definition, numerator, denominator, exclusions, timing, owner, source, stratification rule, missingness rule, interpretation, and failure response. Official HCAHPS results remain separate from local teaching calculations.

## 14. Response-model question and eligible-field contract

The model estimates the probability that an invited synthetic frame record is a respondent. It is a teaching response-adjustment model, not a patient-level intervention model.

Both methods use exactly the three Module 03 response-cell fields:

- `age_band`;
- `other_language_at_home`; and
- `income_group`.

The scikit-learn pipeline applies `OneHotEncoder(handle_unknown="ignore", sparse_output=False)` inside a `ColumnTransformer`. Preprocessing is fitted only on training rows.

Prohibited predictors include assigned mode, health status, proxy status, insurance, sex, race and ethnicity, region, panel, public SAQ status, response probability truth, Q21, Q22, Q23, item missingness, observed response fields, comment fields, theme fields, group estimates, linked outcomes, post-response fields, and source row order. Some of these fields help generate the synthetic response mechanism. They remain excluded so the model uses the same information as the transparent benchmark.

## 15. Split, transparent benchmark, and bounded ML contract

The split is fixed before model fitting:

- use `train_test_split` with `test_size=0.30`;
- stratify on response status;
- set `random_state=20260830`;
- preserve the returned row identities in `split-registry.csv`; and
- never reopen the evaluation rows for fitting, threshold selection, feature changes, or model selection.

The transparent benchmark computes the Module 03 response cell factor on training rows only:

`sum of base person weights in the training frame cell / sum of base person weights among training respondents in that cell`

The factor is bounded from 1.0 through 3.0 and applied to evaluation respondents in the same cell.

The bounded ML model is one `RandomForestClassifier` in the preprocessing pipeline:

- `n_estimators=200`;
- `max_depth=3`;
- `min_samples_leaf=25`;
- `max_features=None`;
- `random_state=20260830`; and
- `n_jobs=1`.

Training uses the accepted base person weight as `sample_weight`. The response factor is `1 / predicted response probability`, bounded from 1.0 through 3.0. No second ML model, hyperparameter search, cross-validation search, probability recalibration, or result-based threshold change is allowed.

## 16. Evaluation, calibration, errors, and weight stability

Both methods are evaluated on the same held-out rows. Required model evidence includes:

- base-weighted Brier score;
- base-weighted ROC AUC;
- base-weighted log loss;
- five fixed calibration groups ordered by predicted probability and frame ID;
- confusion counts at the fixed response threshold of `0.60`;
- an explicit teaching error-cost scenario with cost 2 for a false positive and cost 1 for a false negative;
- minimum, median, 95th percentile, and maximum bounded response factor;
- factor-cap hits;
- Kish effective sample size before and after response adjustment; and
- largest adjusted-weight share.

The error-cost scenario asks what happens when a model treats a likely missing voice as likely covered. It is not a contact policy, utility estimate, or permission to target patients.

Weight stability passes only when every factor is between 1.0 and 3.0, no value is missing or infinite, adjusted-weight Kish effective sample size is at least 85 percent of the base-weight effective sample size among evaluation respondents, and the largest adjusted weight is below 3 percent of total adjusted weight.

## 17. Known-truth recovery and ML decision rule

Known truth is evaluated only in the held-out set. For Q22, Q23, and the teaching composite, the package reports:

- full-frame truth with base person weights;
- respondent base-weighted estimate;
- respondent transparent-adjusted estimate; and
- respondent ML-adjusted estimate.

Item-specific answered denominators remain explicit. A response factor does not repair Q22 or Q23 item nonresponse. The teaching composite is the mean of the two question-level proportions and is not an official HCAHPS score.

ML changes the response-adjustment decision only if all of the following hold:

1. The ML-adjusted teaching-composite absolute bias is at least 0.50 percentage points lower than the transparent-adjusted absolute bias.
2. ML does not worsen either Q22 or Q23 absolute bias by more than 0.25 percentage points.
3. ML base-weighted Brier score is no more than 0.005 worse than the transparent benchmark.
4. Both methods pass the weight-stability rules.
5. Required calibration, error, subgroup, and failure evidence is complete.
6. No source, split, feature, synthetic-boundary, partnership, claim, or progression gate fails.

If the criteria do not all pass, the transparent benchmark remains the teaching adjustment. A passing ML comparison still would not authorize deployment or patient targeting.

## 18. Subgroup model audit and failure-case contract

The held-out audit retains the 13 Module 05 groups across other language at home, income, insurance coverage, and race and ethnicity. A model metric is reportable only when a group has at least 30 evaluation rows, 10 respondents, and 10 nonrespondents. Unsupported rows retain the group, counts, and suppression reason while protected metrics remain blank.

The audit reports Brier score, mean predicted response, observed response, transparent mean factor, ML mean factor, and support status for both methods. Audit-only insurance and race fields never enter model training. Small groups remain separate. Results are not ranked and cannot certify fairness.

Failure-case review covers:

- every evaluation row where the two methods disagree at the fixed threshold;
- aggregate false positives and false negatives for both methods;
- rows where either factor reaches 3.0;
- large transparent-versus-ML factor differences;
- unsupported subgroup results;
- omitted generator fields and residual bias;
- item nonresponse that response adjustment does not solve;
- test contamination and preprocessing leakage;
- performance-only recommendations;
- comment-text leakage;
- targeting or differential contact by predicted response; and
- deployment from synthetic teaching evidence.

## 19. Exact learner deliverables and generated outputs

The learner workspace contains immutable controls and editable records.

Immutable controls:

- `.gitattributes`;
- `VERSION`;
- `source-record.yml`;
- `module06-contract.json`;
- `feature-contract.csv`;
- `partner-contract.csv`;
- `environment.yml`;
- `assessment.md`;
- `build_partnered_improvement_ml.py`;
- `build_workspace.py`; and
- `validate_workspace.py`.

Editable records:

- `README.md`;
- `engagement-status.md`;
- `patient-partner-session.md`;
- `interpretation-disagreement.csv`;
- `improvement-brief.md`;
- `driver-diagram.csv`;
- `workflow.csv`;
- `measure-registry.csv`;
- `burden-access-review.md`;
- `feedback-accountability.md`;
- `ml-comparison.md`;
- `failure-case-review.md`;
- `responsible-claims.md`;
- `reproducibility-check.md`;
- `ai-use.md`;
- `gate-results.csv`; and
- `progression-decision.md`.

Generated reference evidence:

- `upstream-inventory.csv`;
- `analysis-checks.csv`;
- `improvement-evidence.csv`;
- `partner-question-register.csv`;
- `transparent-weight-cells.csv`;
- `split-registry.csv`;
- `model-predictions.csv`;
- `model-performance.csv`;
- `calibration-bins.csv`;
- `threshold-errors.csv`;
- `response-weight-diagnostics.csv`;
- `estimate-recovery.csv`;
- `subgroup-model-audit.csv`;
- `feature-importance.csv`;
- `failure-cases.csv`;
- `invariant-checks.csv`; and
- `build-report.json`.

The package includes a sorted SHA-256 manifest of immutable controls. Learner work files contain direct prompts. Reference work files contain complete simulated teaching answers, exact evidence citations, and an explicit condition for actual patient-partner review.

At first release, the 17 generated evidence files total 283,224 bytes. Reference and learner assemblies each contain 46 files. Their 28-row immutable manifest is 4,361 bytes with SHA-256 `b1ccdbf8fa528f8d486680629f1e6a224f94c658d19eba8d632e325a39b97ab2`.

## 20. Week 6 checkpoint and noncompensable gates

Checkpoint 02 uses `courses/patient-experience-engagement/checkpoints/02-linked-evidence-patient-voice-release/`.

It carries 45 course points exactly once:

| Scored source | Points |
|---|---:|
| Module 04 linked patient evidence | 25 |
| Module 05 patient voice and equity | 20 |
| Module 06 | 0 |
| Total | 45 |

Module 06 gates are noncompensable. The module fails when any of these occur:

1. An accepted upstream file or SHA-256 identity changes.
2. Frame identities do not match one-to-one.
3. A public-derived, synthetic, simulated-partner, or actual-partner field is mislabeled.
4. The reference simulation is presented as actual patient engagement.
5. Partnership terms omit compensation, access, privacy, decision rights, or disagreement.
6. Patient-partner interpretation and disagreement are absent.
7. A supported descriptive signal is called proof of inequity or cause.
8. Unsupported group estimates are populated or groups are merged to evade support rules.
9. Synthetic comments are treated as testimony, prevalence, or saturation.
10. The proposal lacks a driver diagram, workflow, measure registry, burden review, access alternatives, feedback route, or revision rule.
11. A prospective field is inferred from a retrospective proxy.
12. Comment text or another prohibited field enters model training.
13. The two methods use different eligible fields, training rows, evaluation rows, or factor bounds.
14. Preprocessing or model fitting uses evaluation rows.
15. More than one ML model or parameter search is used.
16. Calibration, error counts, error costs, weight stability, known-truth recovery, subgroup support, or failure cases are missing.
17. The ML recommendation ignores the prespecified decision rule.
18. Machine learning replaces the transparent benchmark, patient partnership, or human comment review.
19. The package targets patients or groups by predicted response.
20. The package authorizes official reporting, real fielding, clinical action, implementation, or deployment.
21. The learner workspace cannot be reproduced or immutable files change.
22. The 25-point and 20-point components are not carried exactly once.
23. Any required Module 06 gate fails even when the score is 45 of 45.
24. Progression is inconsistent with the evidence, conditions, or prohibited uses.

Construction may continue with a clearly recorded condition for named patient or caregiver, survey-methods, qualitative, equity, accessibility, language-access, privacy, responsible-AI, clinical, faculty, and independent reproduction review before alpha.

## 21. Validation, release, and handoff

Validation must prove:

- exact input sizes, hashes, shapes, and row identities;
- deterministic split and deterministic model outputs;
- preprocessing fitted only on training rows;
- the same three eligible fields and same held-out rows for both methods;
- response factors bounded from 1.0 through 3.0;
- protected blanks for unsupported subgroup metrics;
- no comment text or prohibited field in the model pipeline;
- correct Q22, Q23, and teaching-composite recovery calculations;
- all 24 gates present and internally consistent;
- Module 04 and Module 05 points carried exactly once;
- deterministic learner and reference workspace assembly;
- mutation rejection for a changed source, changed response, failed gate, and invalid progression; and
- no overwrite of an existing assembly target.

Release `0.1.0` is a runnable curriculum-construction candidate at Commons `0.61.0`. It may permit Checkpoint 02 assembly with conditions. It does not remove the need for actual patient partnership or named review before alpha.

At first release, source reference validation passes 155 checks, assembled reference validation passes 242 checks, and learner validation passes 220 checks. Evidence and workspace two-build equality, copied validation, changed-response rejection, changed-output rejection, failed-gate rejection, invalid-progression rejection, and existing-target rejection all pass.

## 22. Known issues before alpha

- The named APP-2 patient or caregiver partner, compensation, access needs, participation terms, and review record are pending.
- The reference partnership record is a labelled simulation and cannot count as actual engagement.
- The response mechanism, Q21, Q22, Q23, item missingness, comments, coding records, and partner reference record are synthetic or simulated.
- The response model intentionally omits several fields used by the known generator because it must match the transparent benchmark's eligible fields.
- Response adjustment cannot correct item nonresponse or unmeasured selection.
- Public MEPS teaching evidence cannot establish local workflow feasibility, patient preference, discrimination, trust, burden, causal effect, or improvement benefit.
- Official HCAHPS scoring, administration, adjustment, and reporting remain outside this teaching package.
- Named faculty, patient, caregiver, survey-methods, qualitative, health-services data, equity, accessibility, language-access, privacy, responsible-AI, clinical, governance, and independent reproduction reviews remain pending.
- The official course section and half-term dates must be assigned before publishing due dates.

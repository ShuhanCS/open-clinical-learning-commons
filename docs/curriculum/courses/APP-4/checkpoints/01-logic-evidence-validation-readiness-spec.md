# APP-4 Checkpoint 01: Logic, evidence, calibration, and validation readiness

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-app4-cp01`.
- Course: APP-4, Data for Clinical Decision Support.
- Due point: end of instructional Week 3.
- Checkpoint version: `0.1.0`.
- Commons release: `0.80.0`.
- Accepted modules: APP-4 Modules 01, 02, and 03.
- Course points: 40.
- Point source: Module 02 contributes 20 points once and Module 03 contributes 20 points once.
- Required zero-point gate: Module 01.
- Decision: whether the accepted use case, logic, historical evidence, calibration, threshold comparisons, and claim limits may enter Module 04 curriculum work.
- Package: `courses/clinical-decision-support/checkpoints/01-logic-evidence-validation-readiness/`.

This is the first cumulative APP-4 release gate. It joins the use-case boundary, nonproduction logic, public historical evidence, calibration, threshold consequences, and authority limits into one decision. It is not a new analytic assignment and does not rescore the accepted module work.

The checkpoint freezes three complete reference workspaces. A learner cannot repair a source, alter a rule trace, refit the model, change a threshold table, or strengthen an authority claim inside the checkpoint. A material correction returns to its owning module, receives a reviewed new version, reproduces, and enters a rebuilt checkpoint.

The published academic calendar controls the actual due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The Week 3 label is an instructional checkpoint. It does not replace the official dates assigned to the APP-4 section.

## 2. Decision, readers, and required answer

The checkpoint asks:

> May the accepted `CGH-GIM-01` intended use, nonproduction logic, public historical evidence, calibration, threshold comparisons, and claim limits enter Module 04 alert-burden, human-factors, equity, and candidate-design work?

Primary readers are the `CGH-GIM-01` clinical decision support governance council, the APP-4 faculty owner, a primary-care or endocrinology reviewer, a clinical-informatics reviewer, an interoperability and terminology reviewer, an NHANES survey-methods reviewer, a biostatistics and calibration reviewer, a workflow and human-factors reviewer, a patient and access reviewer, an equity reviewer, an accessibility reviewer, a responsible-AI reviewer, and the future Module 04 analyst.

The allowed disposition is `continue`, `continue with conditions`, `revise`, or `refer`. A continuing answer must name:

- all three accepted module identities;
- all 245 candidate files and 204 nested immutable rows;
- the 40-point source and no-double-counting rule;
- all 36 inherited and 20 checkpoint gates;
- the fictional service, clinician user, workflow moment, intended action, nonaction, and prohibited actions;
- all 16 public XPT source identities and their evidence limits;
- the complete synthetic release, its defects, and its nonproduction role;
- all 16 mechanics cases and their trace result;
- the historical cohort, target meaning, predictors, partitions, survey design, and missingness rule;
- temporal-holdout and transport performance and calibration;
- all six evidence candidates and the rejected `0.20` mechanics fixture;
- threshold burden, missed-case, and decision-curve limits;
- subgroup support, suppression, and uncertainty limits;
- the 40-point score and all failed gates, if any;
- every unresolved condition;
- the exact Module 04 permission and scope; and
- every clinical-use, implementation, and deployment prohibition.

A continuing answer opens curriculum construction only. It does not select a clinical threshold, grant approval for silent-mode scoring, authorize a prototype, or permit real-patient use.

## 3. Accepted Module 01 use-case and source package

The checkpoint accepts Module 01 only as:

- module ID `oclc-app4-01`;
- version `0.1.0`;
- Commons release `0.77.0`;
- 41 assembled reference files;
- 29 immutable manifest rows;
- manifest size 3,404 bytes;
- manifest SHA-256 `40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45`;
- 12 of 12 decision gates passing;
- progression `continue with conditions`; and
- zero checkpoint points.

The accepted service is the explicitly fictional `CGH-GIM-01` adult general internal medicine and primary care service. The primary user is the clinician responsible for the current adult encounter. The workflow moment is after required intake information is available and before encounter close.

The intended support remains a nonbinding candidate advisory asking whether confirmatory HbA1c testing may be appropriate. The concept cannot diagnose diabetes, confirm disease, place an order, change treatment, message a patient, deny a service, target a person for nonclinical action, or act without clinician review.

The public release contains 16 complete official NHANES XPT files:

- DEMO, BMX, DIQ, and GHB for 2013-2014;
- DEMO, BMX, DIQ, and GHB for 2015-2016;
- DEMO, BMX, DIQ, and GHB for 2017-2018; and
- DEMO, BMX, DIQ, and GHB for August 2021-August 2023.

The source release has:

- 34,221,200 raw bytes;
- 3,149,043 deterministic gzip bytes;
- 145,563 component rows;
- 442 inventoried fields;
- zero duplicate `SEQN` rows in every component; and
- all-four-component intersections of 6,979, 6,744, 6,401, and 7,199 across the four releases.

The source inventory SHA-256 is `10861ec8526a8cdb9c5e47b45d3b226ea2d545fdecb324b0fda755b274a37e54`. The field inventory SHA-256 is `2b124ea7954bc0eb2225ba4e15abc637eb575a0e9037832aeb0df7a12149b848`.

NHANES supports historical population evidence, not local workflow evidence or prospective clinical utility. Module 01 remains a required gate because every later result depends on its purpose, user, source role, ownership, stop rights, and claim boundary. It adds no points.

## 4. Accepted Module 02 logic, trigger, and synthetic package

The checkpoint accepts Module 02 only as:

- module ID `oclc-app4-02`;
- version `0.1.0`;
- Commons release `0.78.0`;
- 86 assembled reference files;
- 73 immutable manifest rows;
- manifest size 10,564 bytes;
- manifest SHA-256 `bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded`;
- score 20 of 20;
- 12 of 12 logic gates passing; and
- progression `continue with conditions`.

The accepted synthetic source is `CGH-GIM-01-SYNTHETIC-2026-08-31-v1`. Synthea 4.0.0 ran with the pinned Java runtime, seeds, dates, population, state, and thread count. Its source manifest SHA-256 is `0d3c4c11e5ab29284f312d76413f8e005fb957226039d324912f80af93dcf3c0`.

The frozen release contains:

- 1,000 synthetic Massachusetts adults;
- 25 FHIR R4 resource files;
- 811,803 resource rows;
- 1,549,494,665 canonical UTF-8 bytes;
- 100,178,478 gzip bytes;
- zero parse failures; and
- 11,109 repeated resource IDs in four provider or organization files.

The repeated IDs remain measured source defects. They are not silently removed and cannot enter an analytic join without an explicit entity-resolution decision.

The fixed teaching hook is `patient-view` version `1.0`. The ordered mechanics checks service, context, idempotency, input readiness, terminology and units, suppressions, score availability, a mock branch value, and delivery. Stable reason codes make every terminal state traceable.

Sixteen Commons cases cover:

1. below-fixture branch;
2. candidate response at the branch boundary;
3. candidate response above the branch boundary;
4. missing input;
5. stale input;
6. inconsistent input;
7. duplicate request;
8. delayed input;
9. terminology mismatch;
10. hook-version mismatch;
11. recent-HbA1c suppression;
12. known-diabetes suppression;
13. unit mismatch;
14. unsupported service;
15. silent delivery failure; and
16. missing score fixture.

All 16 reference results and ordered traces pass. A passing mechanics trace does not establish clinical correctness.

The Module 02 scores are branch-test fixtures, not predictions. The `0.20` value is arbitrary mechanics only. It was not estimated, recommended, selected, or accepted. The Module 02 score contributes 20 checkpoint points exactly once.

## 5. Accepted Module 03 evidence, calibration, and validation package

The checkpoint accepts Module 03 only as:

- module ID `oclc-app4-03`;
- version `0.1.0`;
- Commons release `0.79.0`;
- 118 assembled reference files;
- 102 immutable manifest rows;
- manifest size 16,354 bytes;
- manifest SHA-256 `e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22`;
- score 20 of 20;
- 12 of 12 evidence gates passing; and
- progression `continue with conditions`.

The evidence release ID is `APP4-M03-NHANES-EVIDENCE-2026-08-31-v1`. It has 17 fingerprinted evidence files and evidence-manifest SHA-256 `b226b33cc0ba2cec0efe2a5046357b10431941e0c9e286f9be889de05321c9a3`.

The fixed cohort includes nonpregnant adults ages 35 through 70 with BMI at least 25 kg/m2, `DIQ010 = 2` for no self-reported diabetes, observed HbA1c, and complete survey-design fields. Pregnant and unknown pregnancy states are excluded when the field applies. No imputation is used.

The target is `LBXGH >= 6.5%`. It means the observed survey laboratory value is at or above the declared cut point. It is not a diagnosis, confirmed disease, treatment indication, or patient-level recommendation.

The release contains:

| Partition | Cycles | Rows | Outcomes | Weight | Model role |
|---|---|---:|---:|---|---|
| Development | 2013-2014 and 2015-2016 | 3,652 | 156 | `WTMEC2YR / 2` | fit the fixed model |
| Temporal holdout | 2017-2018 | 1,806 | 97 | `WTMEC2YR` | evaluate without retuning |
| Transport stress | 2021-2023 | 2,086 | 75 | `WTPH2YR` | separate evaluation without pooling |
| Total model cohort |  | 7,544 | 328 | partition specific | historical teaching evidence |

The full age-eligible audit frame has 14,892 rows. `SDMVSTRA` and `SDMVPSU` remain attached to analytic rows.

The fixed transparent model is one survey-weighted binomial GLM with a logit link. The predictors are age centered at 50 per 10 years, BMI centered at 30 per 5 kg/m2, and a female indicator. Race and Hispanic origin remain audit dimensions and are not model predictors. No temporal-holdout or transport row affects fitting or tuning.

The 20 passing evidence invariants protect source totals, cohort counts, partition separation, target meaning, model identity, threshold status, and authority boundaries.

The Module 03 score contributes 20 checkpoint points exactly once.

## 6. Point architecture and no-double-counting rule

The source course has two 20-point Week 3 components:

| Source component | Owning module | Points | Checkpoint treatment |
|---|---|---:|---|
| Use-case and logic specification | Module 02 | 20 | counted once |
| Evidence, calibration, and threshold audit | Module 03 | 20 | counted once |
| Source-feasibility and use-case gate | Module 01 | 0 | required, not scored |
| Checkpoint review | Checkpoint 01 | 0 | cumulative gate, no new course points |
| Total |  | 40 | exact Week 3 total |

`checkpoint-score.csv` carries the six accepted Module 02 criteria:

| Criterion | Points |
|---|---:|
| Use-case and logic release | 3 |
| Ordered logic, trigger, suppression, and reasons | 5 |
| Event-time input, terminology, unit, and failure contract | 4 |
| Synthetic provenance, defects, limits, and reproducibility | 3 |
| Sixteen expected results and ordered traces | 3 |
| Change control, consequences, claims, AI, and progression | 2 |
| Module 02 subtotal | 20 |

It also carries the 11 accepted Module 03 criteria:

| Criterion | Points |
|---|---:|
| Cohort and target | 2.0 |
| Survey design | 2.0 |
| Model specification | 2.0 |
| Performance | 2.0 |
| Calibration | 2.0 |
| Threshold consequences | 2.0 |
| Decision curve | 1.5 |
| Transport stress | 1.5 |
| Subgroup support | 1.5 |
| Week 3 component release | 1.5 |
| Reproducibility, claims, and AI | 2.0 |
| Module 03 subtotal | 20.0 |

The reference total is 40 of 40. A passing threshold is 28 of 40, but all gates remain noncompensable. The checkpoint cannot add a new criterion, award points for its defense, average a failed gate into a passing score, or count a component twice.

## 7. Cumulative evidence index and chain of custody

`evidence-index.csv` has one ordered row for each accepted module. Every row records:

- module ID and title;
- module and Commons versions;
- complete assembled file count;
- nested immutable manifest rows, bytes, and SHA-256;
- checkpoint points;
- inherited gate result;
- accepted progression;
- accepted decision; and
- cumulative role.

The checkpoint builder calls each owning module's `build_workspace.py` and requests its complete reference workspace. It verifies the expected file count, immutable-row count, and nested manifest SHA-256 before copying any candidate file.

The cumulative candidate contains:

| Candidate directory | Complete files | Nested immutable rows | Role |
|---|---:|---:|---|
| `candidate/module-01/` | 41 | 29 | source and intended-use gate |
| `candidate/module-02/` | 86 | 73 | logic, input, synthetic, and 20-point component |
| `candidate/module-03/` | 118 | 102 | evidence, calibration, threshold, and 20-point component |
| Total | 245 | 204 | frozen Week 3 candidate |

`candidate-manifest.csv` fingerprints every candidate file with its relative path, bytes, SHA-256, source module, source version, and role. Candidate rows are sorted. The learner and reference packages receive the same candidate manifest.

The outer manifest protects complete module workspaces, including each module's reference answers and nested manifest. The nested manifests independently protect 204 immutable source, evidence, fixture, and control files.

A changed candidate invalidates the checkpoint. The correction belongs in the owning module.

## 8. Integrated logic and evidence readiness review

`logic-evidence-readiness-review.md` is the main cumulative narrative. It must answer one question rather than paste three module summaries together.

The review must reconcile these accepted layers:

| Layer | Accepted evidence | Limit that must remain visible |
|---|---|---|
| Intended use | one fictional service, clinician user, encounter moment, nonbinding support, nonaction, owners, and stop rights | no clinical permission |
| Public source | complete NHANES releases and exact source identities | no local workflow or prospective utility evidence |
| Synthetic source | complete FHIR-shaped release and measured defects | not real patients or conformance evidence |
| Logic mechanics | 16 deterministic cases and ordered traces | fixture score and branch value are not evidence |
| Historical model | fixed cohort, target, survey design, transparent model, and partitions | observed cut-point indicator is not diagnosis |
| Temporal holdout | untouched 2017-2018 evidence | no retuning or local validation claim |
| Transport stress | separate 2021-2023 evidence with `WTPH2YR` | no pooling or unsupported causal explanation |
| Thresholds | six historical classification tradeoffs | no selected or accepted threshold |
| Decision curve | net-benefit quantities under declared threshold odds | no patient-benefit proof |
| Subgroups | denominators, outcomes, effective support, suppression, and uncertainty | no trait, certification, or group action |

The Module 02 mechanics branch and Module 03 evidence are not interchangeable. The checkpoint keeps the logic trace because Module 04 needs its failure and reason structure. It rejects the fixture score and `0.20` value because Module 04 must use the six evidence candidates for comparative curriculum work.

The review must not rewrite an unavailable result as zero, report a suppressed metric, infer a cause for transport differences, or treat historical flags per 1,000 as local cards per 1,000 encounters.

## 9. Performance and calibration readiness

The checkpoint freezes exact performance and calibration point estimates.

### Temporal holdout

| Measure | Accepted value |
|---|---:|
| Rows | 1,806 |
| Outcomes | 97 |
| Weighted prevalence | 0.02904272 |
| Weighted mean probability | 0.03015261 |
| Weighted Brier score | 0.02811126 |
| Weighted log loss | 0.12694930 |
| Weighted ROC AUC | 0.68783144 |
| Calibration-in-the-large | -0.03946013 |
| Calibration slope | 0.88441129 |

### Transport stress

| Measure | Accepted value |
|---|---:|
| Rows | 2,086 |
| Outcomes | 75 |
| Weighted prevalence | 0.03274014 |
| Weighted mean probability | 0.03041245 |
| Weighted Brier score | 0.03175435 |
| Weighted log loss | 0.14019059 |
| Weighted ROC AUC | 0.68422573 |
| Calibration-in-the-large | 0.07788522 |
| Calibration slope | 0.81620710 |

The point estimates support bounded historical comparison. They do not show local validity, clinical utility, patient benefit, or safety. The model has moderate historical discrimination, and the transport calibration result strengthens the need for a conditional rather than unqualified progression.

The 500-replicate stratified-PSU sensitivity bootstrap uses fixed predictions and seed `7400303`. It is a deterministic teaching method pending formal complex-survey review.

## 10. Threshold, decision-curve, transport, and subgroup readiness

All six evidence candidates remain unselected and unaccepted:

| Candidate | Holdout flags per 1,000 | Sensitivity | Specificity | Positive predictive value | Missed per 1,000 |
|---:|---:|---:|---:|---:|---:|
| 0.020 | 661.57323641 | 0.89675075 | 0.34546126 | 0.03936689 | 2.99863880 |
| 0.030 | 325.40301123 | 0.60091129 | 0.68283783 | 0.05363225 | 11.59062056 |
| 0.040 | 172.19709642 | 0.36288643 | 0.83350669 | 0.06120433 | 18.50350918 |
| 0.050 | 105.90526558 | 0.22855075 | 0.89776324 | 0.06267615 | 22.40498219 |
| 0.075 | 36.68485865 | 0.06348936 | 0.96411690 | 0.05026334 | 27.19881351 |
| 0.100 | 17.08750038 | 0.03841504 | 0.98355044 | 0.06529200 | 27.92703988 |

The Module 02 `0.20` value appears in three rejected comparison rows, one for each analytic partition. It remains a mechanics fixture. It is not a seventh evidence candidate.

The 63-row net-benefit table compares the model, treat-all, and treat-none strategies under the declared threshold odds. Its role is to teach consequence-weighted comparison. It does not estimate patient benefit or choose the correct action.

The transport comparison has 13 rows. It names data, weight, support, prevalence, performance, calibration, and burden differences without claiming why they occurred.

The subgroup-support table has 48 rows:

- development has 14 reportable and two suppressed rows;
- temporal holdout has eight reportable and eight suppressed rows; and
- transport stress has five reportable and 11 suppressed rows.

Suppressed Brier and ROC AUC values remain blank. Threshold metrics remain unavailable for every subgroup because no threshold is accepted. No group-specific threshold, action, ranking, fairness certification, or trait claim is allowed.

Module 04 receives all six candidates, not one silently favored candidate. It must compare a less interruptive alternative and no alert. It owns the workflow, burden, access, equity, and human-governance work needed before a candidate-design recommendation can be considered.

## 11. Noncompensable inherited and checkpoint gates

The inherited gate totals are:

- Module 01: 12 of 12;
- Module 02: 12 of 12; and
- Module 03: 12 of 12.

Checkpoint 01 adds 20 integrity gates:

1. all three accepted module identities and complete reference workspaces are exact;
2. the 245-row candidate manifest is sorted and complete;
3. all 204 nested immutable rows match their accepted manifests;
4. Module 01 source identities, completeness, intended use, and authority limits remain exact;
5. the service remains fictional and the support concept remains nonbinding;
6. the complete synthetic source identity, duplicate count, and limitations remain visible;
7. all 16 mechanics cases and ordered traces pass;
8. the Module 02 score and `0.20` value remain rejected mechanics fixtures;
9. the historical target remains an observed cut-point indicator, not diagnosis;
10. development, temporal holdout, and transport remain separate with zero retuning;
11. weights, strata, PSUs, and the transport phlebotomy weight remain explicit;
12. model performance, calibration, and evidence identities reproduce;
13. all six evidence candidates remain unselected and unaccepted;
14. burden, missed-case, and decision-curve evidence remains descriptive;
15. 2021-2023 remains a separate transport stress test;
16. unsupported subgroup performance remains suppressed and no group action is authorized;
17. Module 01 has zero points and Modules 02 and 03 have 20 points once each;
18. all 36 inherited and 20 checkpoint gates pass;
19. defense, reproduction, AI, claims, ownership, and conditions are complete; and
20. only bounded Module 04 curriculum construction is permitted.

All 56 gates must pass. A failed gate forces `revise` or `refer` regardless of the 40-point score.

## 12. Learner records and defense contract

The learner and reference packages each contain nine checkpoint records:

| Record | Required content |
|---|---|
| `README.md` | decision, point source, use instructions, threshold status, and authority boundary |
| `evidence-index.csv` | all three module identities, nested manifests, points, gates, progression, and roles |
| `logic-evidence-readiness-review.md` | integrated logic and evidence decision with exact values and limits |
| `checkpoint-score.csv` | six Module 02 criteria, 11 Module 03 criteria, subtotals, and 40-point total |
| `checkpoint-gates.csv` | 20 ordered gates, status, evidence, and owner |
| `checkpoint-defense.md` | 14 ordered answers, each with exact evidence and a limit |
| `reproducibility-check.md` | candidate identity, nested identity, two-build result, upstream checks, mutations, and open review |
| `ai-use.md` | complete accountable agent-use record |
| `progression-decision.md` | score, gates, threshold status, Module 04 permission, later gates, conditions, and prohibitions |

Every learner record contains `REPLACE` and remains incomplete by design. Every reference record is complete and contains no placeholder.

The defense questions ask the learner to explain:

1. which releases are frozen;
2. how the 40 points are counted;
3. what clinical purpose remains in scope;
4. what public and synthetic sources support;
5. whether the logic tests pass;
6. how `0.20` is handled;
7. what the historical target means;
8. how development, holdout, and transport remain separate;
9. what performance and calibration support;
10. what threshold comparisons show;
11. how decision-curve and subgroup results are bounded;
12. what mechanics-and-evidence conflict was resolved;
13. what Module 04 may do; and
14. what remains prohibited and unresolved.

Each answer requires an `Answer:`, `Evidence:`, and `Limit:` line. A polished answer without traceable evidence or a decision boundary is incomplete.

## 13. Deterministic assembly contract

`build_checkpoint.py` uses only the Python standard library and the accepted module builders.

Assembly order:

1. refuse an existing target;
2. verify all checkpoint controls and the chosen learner or reference record set;
3. copy the eight immutable checkpoint controls;
4. copy the nine learner or reference records;
5. build the complete Module 01 reference workspace;
6. require 41 files, 29 immutable rows, and the accepted manifest SHA-256;
7. build the complete Module 02 reference workspace;
8. require 86 files, 73 immutable rows, and the accepted manifest SHA-256;
9. build the complete Module 03 reference workspace;
10. require 118 files, 102 immutable rows, and the accepted manifest SHA-256;
11. copy all 245 candidate files under their module directory;
12. write the sorted outer candidate manifest; and
13. require exactly 263 assembled files.

The assembled workspace has:

- eight immutable checkpoint controls;
- nine editable checkpoint records;
- 245 frozen candidate files; and
- one candidate manifest.

Total: 263 files.

Two reference builds must return the same report and byte-identical candidate manifest. A learner build must have the same candidate manifest. Candidate-file hashes must match between independent builds. An existing target must be rejected.

The accepted candidate manifest is 45,897 bytes with SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`.

## 14. Validation, copied execution, and mutation rejection

`validate_checkpoint.py` validates the checkpoint without external Python packages.

Complete reference validation performs 1,284 checks. Learner validation performs 1,245 checks. Validation covers:

- exact file inventory;
- all 245 outer candidate fingerprints and source identities;
- all three nested manifests and 204 nested immutable fingerprints;
- checkpoint contract, release, version, points, gates, thresholds, and authority;
- exact Module 01 source totals and service boundary;
- exact Module 02 synthetic totals, defects, 16 trace results, points, and fixture status;
- exact Module 03 cohort, partition, invariant, threshold, support, and no-retuning contracts;
- evidence index and no-double-counting rule;
- 20-row checkpoint score;
- 20 ordered checkpoint gates;
- required cumulative evidence and prohibited claims;
- 14 defense answers with evidence and limits;
- reproduction routes;
- AI accountability;
- progression, conditions, and Module 04 permission; and
- every clinical-use and deployment prohibition.

The validator copied inside the assembled workspace must validate that workspace successfully. This prevents a package from depending on an unshipped local validator.

The self-check rejects 20 deliberate failure routes:

1. changed candidate;
2. missing candidate;
3. changed Module 01 points;
4. duplicated Module 02 points;
5. duplicated Module 03 points;
6. wrong checkpoint total;
7. failed inherited gate;
8. failed checkpoint gate;
9. promoted `0.20` fixture;
10. accepted-threshold mutation;
11. diagnosis claim;
12. holdout retuning;
13. transport pooling;
14. unsupported subgroup performance;
15. incomplete defense;
16. missing AI accountability field;
17. invalid progression permission;
18. real-patient scoring permission;
19. deployment permission; and
20. missing reproduction route.

Submitting learner prompts as a complete reference package is also rejected.

## 15. Common failure modes and instructor response

| Failure | Required response |
|---|---|
| A module directory is missing or changed | rebuild from the accepted owning module |
| A nested manifest changes | return to the owning module and review a new version |
| Module 01 receives points | restore its zero-point gate role |
| Module 02 or Module 03 points appear twice | restore one 20-point component for each |
| The checkpoint adds points | remove the added score and preserve the source plan |
| A passing score hides a failed gate | stop progression and revise or refer |
| The service or intended use becomes real | restore the fictional boundary or refer |
| Public and synthetic source roles are mixed | restore separate identities and claims |
| The 11,109 duplicate IDs disappear | return to Module 02 and restore the measured defect |
| A mechanics trace is called clinical validation | restore the mechanics-only claim |
| The `0.20` fixture becomes evidence | reject it and restore all six evidence candidates |
| One HbA1c result is called diagnosis | restore the observed cut-point meaning |
| Holdout or transport affects fitting | return to Module 03 and release a reviewed new version |
| `WTPH2YR` is replaced or ignored | return to Module 03 and repair the transport design |
| A threshold is selected by code or an agent | restore null acceptance and refer to human governance |
| Historical flags become local card burden | restore the historical classification limit |
| Decision curve is called patient benefit | restore the threshold-odds and non-benefit limit |
| Transport difference receives an unsupported cause | remove the causal explanation |
| Suppressed subgroup performance is filled | restore blank metrics and support language |
| A group-specific action appears | remove it and refer to methods, equity, and clinical owners |
| Module 04 permission includes a live score or alert | restore curriculum-only permission |
| Prototype work begins early | complete Module 04 and its progression gate first |
| A candidate is edited inside the checkpoint | correct the owning module and reassemble |
| A defense answer lacks evidence or a limit | return the defense as incomplete |
| AI use lacks a human owner or independent check | return the record as incomplete |

Instructors stop review at the first broken fingerprint, duplicated point, failed gate, selected threshold, diagnosis claim, unsupported subgroup result, or clinical-use permission.

## 16. Progression contract and Module 04 handoff

The reference disposition is:

- checkpoint score `40 of 40`;
- Module 01 decision gates `12 of 12 pass`;
- Module 02 logic gates `12 of 12 pass`;
- Module 03 evidence gates `12 of 12 pass`;
- checkpoint integrity gates `20 of 20 pass`;
- failed gates `none`;
- accepted clinical threshold `none`;
- Module 02 mock threshold `0.20 rejected mechanics fixture`;
- progression `continue with conditions`;
- Module 04 permission `permitted for curriculum construction`;
- Module 05 permission `prohibited until Module 04 passes`; and
- diagnosis, real-patient scoring, clinical alerting, clinical action, implementation, production connection, and deployment `prohibited`.

Module 04 receives:

- the exact fictional service and intended-use boundary;
- the ordered logic, reason, suppression, input, terminology, unit, time, and failure contracts;
- all 16 mechanics cases;
- the fixed historical cohort, target, predictors, partitions, and survey design;
- temporal-holdout and transport performance and calibration;
- all six unaccepted evidence candidates;
- threshold flags, missed cases, sensitivity, specificity, predictive value, and decision-curve quantities;
- subgroup support and suppression;
- the 40-point Week 3 score;
- all open conditions; and
- every authority prohibition.

Module 04 may:

- compare historical candidate burden in relation to synthetic workflow assumptions;
- perform task and human-factors analysis;
- examine access, language, disability, privacy, equity, override, dismissal, deferment, and hidden work;
- compare all six evidence candidates;
- compare a less interruptive alternative;
- compare no alert; and
- develop a human-governed candidate-design recommendation for later sandbox construction.

Module 04 may not:

- inherit or promote `0.20`;
- change the cohort, model, predictions, partitions, or evidence tables;
- accept a threshold for real clinical use;
- score a real patient;
- display a clinical alert;
- claim local validity or patient benefit;
- build the Module 05 prototype early; or
- implement, connect, or deploy.

Ten open conditions assign the clinical purpose, survey design, independent model reproduction, interoperability teaching shapes, patient and access review, synthetic workflow proxies, threshold comparison, subgroup suppression, responsible agent use, official dates, and clean reproduction to named human owners.

## 17. Release, review, and exit criteria

Checkpoint version `0.1.0` exits as a runnable release candidate at Commons `0.80.0` only when:

- two independent reference assemblies match;
- learner and reference candidates are identical;
- existing-target refusal passes;
- all 245 outer fingerprints match;
- all three nested manifests and 204 immutable artifacts match;
- the copied validator passes;
- reference validation passes 1,284 checks;
- learner validation passes 1,245 checks;
- all 20 failure routes are rejected;
- learner prompts are rejected as a complete package;
- the score is 40 with no duplication;
- all 56 inherited and checkpoint gates pass;
- all six evidence candidates remain unaccepted;
- `0.20` remains a rejected mechanics fixture;
- the defense has 14 complete answers;
- the progression record matches the bounded Module 04 permission;
- every clinical-use and deployment route remains prohibited; and
- the complete curriculum regression passes.

The accepted candidate manifest is 45,897 bytes with SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`.

Named APP-4 faculty, primary-care or endocrinology, survey-methods, biostatistics, calibration, clinical-informatics, interoperability, terminology, workflow, human-factors, patient, access, equity, privacy, accessibility, responsible-AI, and independent-reproduction reviews remain required before alpha.

The official APP-4 section must map the Week 3 checkpoint to the published academic calendar before assigning a due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The release is a curriculum construction candidate. It is not permission to diagnose, score a real patient, display an alert, order, treat, implement, connect to a production system, or deploy.

# APP-4 Module 03 specification: Evidence, calibration, and validation

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app4-03`.
- Module version: `0.1.0`.
- Commons release: `0.79.0`.
- Course: APP-4, Data for Clinical Decision Support.
- Course week: 3 of the seven-module, 7.5-week course.
- Learner time: 16.5 hours.
- Course points: 20 of the 40-point Week 3 checkpoint.
- Status: runnable release candidate.
- Continuing case: fictional adult general internal medicine and primary care service `CGH-GIM-01`.
- Continuing decision: whether a nonbinding advisory concept may continue from historical evidence review into cumulative logic and evidence review, then later workflow evaluation.

Module 03 replaces the arbitrary score and `0.20` branch value used for mechanics in Module 02 with a fixed, reproducible historical evidence analysis. It builds one transparent classification model from public NHANES development evidence, evaluates an untouched temporal holdout, keeps the later 2021-2023 release separate as a transport stress test, and audits calibration, candidate thresholds, burden, missed cases, decision-curve quantities, and subgroup support.

The module does not diagnose diabetes or accept a threshold. It does not score a real patient, create a clinical alert, order a test, establish local validity, authorize implementation, connect to a clinical system, or deploy.

### Prerequisites

Learners must have:

1. passed APP-4 Modules 01 and 02;
2. accepted the 73-file Module 02 immutable handoff;
3. retained all 16 complete NHANES public XPT identities;
4. retained the Module 02 logic, input, terminology, timing, suppression, trace, and authority boundaries;
5. completed FND-1 and FND-2 work on joins, missingness, survey design, regression, prediction, calibration, thresholds, uncertainty, and reproducibility; and
6. no unresolved logic or input issue that would invalidate historical analysis.

### Course handoff

Module 02 permits historical evidence construction but forbids fitting inside Module 02 or treating its mock score and threshold as evidence. Module 03 owns the historical cohort, target, predictors, model, temporal validation, later transport stress test, calibration, threshold tradeoff, decision-curve, and subgroup-support analysis.

A passing Module 03 package permits APP-4 Checkpoint 01 assembly. It does not by itself permit Module 04. The cumulative checkpoint must freeze and reconcile the accepted Module 02 and Module 03 releases before workflow scoring begins.

## 2. Healthcare decision and named audience

### Healthcare decision

The module decision is:

> Does the historical evidence justify assembling the Week 3 release and continuing toward workflow evaluation under stated limits?

This is a curriculum progression decision about evidence readiness. It is not a diagnosis, clinical recommendation, threshold approval, implementation decision, or deployment decision.

### Named audiences

| Audience | Decision supported |
| --- | --- |
| APP-4 learner team | whether its cohort, model, calibration, threshold, transport, and support evidence is complete and internally consistent |
| APP-4 faculty | whether the 20-point Module 03 component can enter the 40-point Week 3 checkpoint |
| Primary-care or endocrinology reviewer | whether the teaching cohort, outcome wording, confirmatory boundary, and consequence questions are clinically coherent |
| Biostatistics and calibration reviewer | whether model, evaluation, calibration, threshold, and uncertainty methods are supportable |
| NHANES survey-methods reviewer | whether cycle, weight, stratum, PSU, pooling, and later phlebotomy-weight treatment are correct |
| Clinical informatics reviewer | whether historical predictors remain distinct from event-time local availability |
| Equity and patient reviewers | whether exclusions, support, suppression, access, and consequence claims remain bounded |
| Checkpoint 01 council | whether the combined logic and evidence release may progress with conditions |

## 3. Foundation skill being revisited or extended

### FND-1 extension

Module 03 revisits technical foundations in a clinical evidence chain:

- joins become four cycle-specific one-to-one joins across DEMO, BMX, DIQ, and GHB;
- data types become code, unit, missing-state, and weight checks;
- row counts become a sequential cohort flow with every exclusion visible;
- missingness remains unavailable rather than being silently imputed;
- source identity becomes a 16-file byte and SHA-256 gate before parsing;
- output identity becomes a 17-file evidence manifest plus deterministic gzip; and
- reproducibility means two clean builds produce byte-identical releases.

### FND-2 extension

Module 03 applies modeling foundations to a decision support question:

- development, evaluation, and transport partitions are assigned once and never exchanged;
- one fixed transparent binomial GLM is compared with a constant prevalence baseline;
- a target, predictor, score, threshold, classification, and action remain different objects;
- discrimination, Brier score, log loss, calibration-in-the-large, calibration slope, and score-range calibration answer different questions;
- candidate thresholds are evaluated through flags, missed cases, sensitivity, specificity, predictive value, and hypothetical net benefit;
- subgroup evidence starts with rows, outcomes, non-outcomes, effective support, uncertainty, and suppression; and
- a similar AUC cannot substitute for calibration, transport, clinical utility, or safety.

### DA-730 use

Learners use concept-first visualization to communicate cohort loss, observed versus predicted evidence, threshold tradeoffs, later-cycle change, and subgroup support. Every visual has an exact CSV alternative. Color cannot carry status alone, unsupported subgroup estimates stay blank, and a chart title cannot turn a historical model into a clinical recommendation.

## 4. Learning outcomes that can be assessed

By the end of Module 03, a learner can:

1. verify every inherited public and synthetic source identity before analysis;
2. translate a clinical screening concept into explicit historical inclusion, exclusion, missingness, and information-cutoff rules;
3. state why `LBXGH >= 6.5%` is an observed laboratory cut-point indicator rather than diagnosis or confirmed disease;
4. construct and audit a four-cycle one-to-one NHANES evidence frame;
5. apply `WTMEC2YR / 2` to the pooled 2013-2016 development evidence;
6. preserve cycle-specific `WTMEC2YR` for the 2017-2018 holdout;
7. use `WTPH2YR` for the 2021-2023 blood-analyte transport stress test;
8. retain `SDMVSTRA` and `SDMVPSU` through every analytic output;
9. explain why 2021-2023 is not pooled with the earlier releases;
10. fit the fixed weighted binomial GLM only on development rows;
11. reproduce the constant baseline and transparent-model results;
12. distinguish discrimination, overall accuracy, calibration, threshold classification, and decision-curve quantities;
13. interpret calibration-in-the-large and calibration slope without treating either as a full calibration guarantee;
14. compare all six evidence candidate thresholds in exact operational units;
15. reject `0.20` as a Module 02 mechanics fixture rather than a historical evidence candidate;
16. keep every threshold unselected and unaccepted pending human consequence and governance review;
17. describe holdout-to-transport changes without assigning an unsupported cause;
18. apply subgroup support and suppression rules before reporting performance;
19. explain what the 500-replicate teaching interval does and does not support;
20. produce accessible exact tables for every display concept; and
21. make a bounded `continue`, `continue with conditions`, `revise`, or `refer` progression decision.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 03 owns

- historical eligibility, exclusions, target, information cutoff, and missingness;
- one fixed development, temporal-holdout, and transport partition;
- cycle-specific survey weights, strata, and PSUs;
- the 2021-2023 phlebotomy-weight exception;
- the development-only transparent model;
- the constant baseline;
- fixed participant-level historical probabilities;
- performance, calibration, threshold, decision-curve, transport, and subgroup evidence;
- deterministic teaching uncertainty;
- the six evidence candidate thresholds;
- rejection of the Module 02 mock threshold as evidence;
- evidence limitations and claim boundaries; and
- the protected Checkpoint 01 component handoff.

### Checkpoint 01 owns next

- exact assembly of the accepted Module 02 and Module 03 components;
- one 40-point Week 3 score without duplicate points;
- reconciliation of logic, input, model, threshold, and claim boundaries;
- validation of both immutable manifests;
- one cumulative progression decision; and
- permission or refusal for Module 04 construction.

### Module 04 owns later

- task and workflow analysis;
- candidate-card burden in the synthetic service;
- timing, interruption, dismissal, deferment, and competing alerts;
- less interruptive alternatives and no-alert comparison;
- patient communication, access, human factors, and equity review; and
- selection of one candidate design for sandbox construction, subject to governance.

### Modules 05 through 07 own later

- local nonproduction prototype behavior and failure testing;
- safety case, monitoring, governance, and fixed embedded-ML challenger;
- clinician leadership, product brief, cumulative defense, and final recommendation; and
- final package acceptance without clinical-use authority.

### Explicitly out of scope

This module does not:

- establish symptoms, clinical diagnosis, treatment need, or confirmed disease;
- infer that NHANES fields are available in a local EHR at the decision moment;
- use race or Hispanic-origin category as a predictor;
- impute missing values;
- tune, refit, recalibrate, or select a model on holdout or transport rows;
- add nonlinear terms, interactions, or a machine-learning challenger;
- select or accept a clinical threshold;
- estimate local alert burden, fatigue, clinician behavior, patient preference, access, or capacity;
- prove patient benefit, clinical utility, safety, fairness, or local transport;
- score a real patient or send a clinical message;
- connect to a clinical system; or
- authorize implementation or deployment.

## 6. Lesson sequence with estimated learner time

| Lesson | Focus | Learner work | Hours |
| --- | --- | --- | ---: |
| 1 | Decision, target, and authority | Reopen the Module 02 handoff; separate result, diagnosis, score, threshold, action, and authority | 1.5 |
| 2 | Cohort and survey design | Rebuild eligibility, exclusions, missingness, cycle roles, weights, strata, PSUs, and phlebotomy exception | 2.0 |
| 3 | Evidence frame and reproducibility | Verify all 16 XPT files, inspect 14,892 audit rows, reproduce the 7,544-row model cohort, and check the manifest | 2.5 |
| 4 | Transparent model and baseline | Fit the fixed weighted GLM on 3,652 development rows, reproduce coefficients, and compare the constant baseline | 2.5 |
| 5 | Performance and calibration | Evaluate the 1,806-row untouched holdout and read Brier, log loss, AUC, calibration-in-the-large, slope, and score ranges | 2.5 |
| 6 | Thresholds and decision curves | Audit all six evidence candidates, reject `0.20`, translate tradeoffs per 1,000, and interpret threshold odds | 2.5 |
| 7 | Transport and subgroup support | Compare 2,086 later rows without causal attribution; apply support, suppression, and uncertainty rules | 1.5 |
| 8 | Week 3 component release | Defend claims, limitations, AI use, invalidation, and bounded checkpoint progression | 1.5 |
| Total |  |  | 16.5 |

## 7. Authoritative readings and public clinical sources

### Required public and clinical readings

1. CDC/NCHS, NHANES Weighting Module: https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx
2. CDC/NCHS, Brief Overview of Sample Design, Nonresponse Bias Assessment, and Analytic Guidelines for NHANES August 2021-August 2023: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/OverviewBrief.aspx?Cycle=2021-2023
3. CDC/NCHS, Guidelines for High Quality Analyses of NHANES Data: https://wwwn.cdc.gov/Nchs/Nhanes/QualityAnalysesGuidelines.aspx
4. CDC/NCHS, NHANES 2013-2014 DEMO documentation: https://wwwn.cdc.gov/Nchs/data/nhanes/Public/2013/DataFiles/DEMO_H.htm
5. CDC/NCHS, NHANES 2021-2023 GHB documentation: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/GHB_L.htm
6. USPSTF, Prediabetes and Type 2 Diabetes Screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes
7. NIDDK, Diabetes and Prediabetes Tests: https://www.niddk.nih.gov/health-information/professionals/clinical-tools-patient-management/diabetes/diabetes-prediabetes
8. Collins et al., TRIPOD+AI reporting statement: https://www.bmj.com/content/385/bmj-2023-078378
9. Riley et al., external validation guidance: https://www.bmj.com/content/384/bmj-2023-074820
10. Van Calster et al., Calibration: the Achilles heel of predictive analytics: https://link.springer.com/article/10.1186/s12916-019-1466-7
11. Vickers and Elkin, Decision Curve Analysis: https://journals.sagepub.com/doi/pdf/10.1177/0272989X06295361

### Reading purpose

- The CDC weighting tutorial explains why the MEC weight is divided across pooled two-year cycles.
- The 2021-2023 overview establishes the new phlebotomy weight for blood analytes and the need to read that cycle's changed design carefully.
- USPSTF supplies a public clinical screening frame, while NIDDK supplies the laboratory cut point and confirmation boundary.
- TRIPOD+AI and external-validation guidance keep development and evaluation data separate and require calibration, discrimination, and clinical-usefulness evidence.
- The calibration readings prevent AUC-only interpretation.
- Decision-curve analysis supplies the threshold-odds framework but does not create patient values or threshold authority.

All linked readings are context, not permission to claim that the reference teaching cohort is a complete current clinical policy or that the model is clinically usable.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Inherited public source release

Module 01 pins all four components for four cycles:

| Cycle | Role | Components | Weight role |
| --- | --- | --- | --- |
| 2013-2014 | Development | DEMO_H, BMX_H, DIQ_H, GHB_H | `WTMEC2YR / 2` |
| 2015-2016 | Development | DEMO_I, BMX_I, DIQ_I, GHB_I | `WTMEC2YR / 2` |
| 2017-2018 | Untouched temporal holdout | DEMO_J, BMX_J, DIQ_J, GHB_J | `WTMEC2YR` |
| August 2021-August 2023 | Separate transport stress | DEMO_L, BMX_L, DIQ_L, GHB_L | `WTPH2YR` from GHB_L |

The 16 compressed sources contain 145,563 component rows and 3,149,043 gzip bytes. `inherited/module02/inherited/module01/data/source-inventory.csv` records the source URLs, codebooks, retrieval date, raw and compressed byte counts, hashes, rows, fields, and roles.

### Derived evidence release

The accepted evidence release is `APP4-M03-NHANES-EVIDENCE-2026-08-31-v1`. Its manifest SHA-256 is `b226b33cc0ba2cec0efe2a5046357b10431941e0c9e286f9be889de05321c9a3`.

| File | Rows | Purpose |
| --- | ---: | --- |
| `cohort-audit.csv.gz` | 14,892 | Full age-eligible joined audit frame with exclusions and unavailable states |
| `model-cohort.csv.gz` | 7,544 | Fixed complete-case model rows and design fields |
| `predictions.csv.gz` | 7,544 | Baseline and fixed model probabilities |
| `cohort-flow.csv` | 36 | Nine sequential stages for four cycles |
| `missingness.csv` | 32 | Eight required field families for four cycles |
| `survey-design.csv` | 3 | Partition-specific weight, strata, PSU, support, and pooling rules |
| `model-coefficients.csv` | 4 | Intercept and three fixed terms |
| `performance.csv` | 6 | Baseline and model results in three partitions |
| `calibration.csv` | 3 | Overall calibration evidence |
| `calibration-groups.csv` | 15 | Five weighted score ranges per partition |
| `threshold-audit.csv` | 21 | Six candidates plus rejected mock value in three partitions |
| `net-benefit.csv` | 63 | Model, test-all, and test-none across seven values and three partitions |
| `subgroup-support.csv` | 48 | Four dimensions with support and suppression across three partitions |
| `bootstrap-intervals.csv` | 48 | Holdout and transport teaching intervals |
| `transport-comparison.csv` | 13 | Holdout-to-transport changes |
| `invariants.csv` | 20 | Release acceptance checks |
| `build-report.json` | 1 | Machine-readable release summary and authority boundary |

`evidence-manifest.csv` records bytes, hashes, row counts, and roles for all 17 files.

### Rights and teaching purpose

NHANES files are U.S. federal public-use data. Learners retain attribution, codebooks, cycle identity, and analytic limitations. The derived release contains public respondent identifiers only. It contains no local patient, clinician, employee, credential, or protected data.

The purpose is to teach reproducible historical evidence review. The data do not describe the fictional service or prove local prevalence, availability, utility, workflow fit, safety, fairness, benefit, implementation readiness, or deployment readiness.

## 9. Data dictionary and expected analytic structure

### Source variables

| Variable | Source | Role | Rule |
| --- | --- | --- | --- |
| `SEQN` | All components | Public respondent join key | One row per component within cycle; never join across cycles |
| `RIDAGEYR` | DEMO | Eligibility and predictor | Ages 35 through 70; centered at 50 and divided by 10 |
| `RIAGENDR` | DEMO | Predictor and audit dimension | Source values 1 and 2; female indicator equals 1 for value 2 |
| `RIDRETH3` | DEMO | Audit-only dimension | Never enters the model or a group-specific action |
| `RIDEXPRG` | DEMO | Pregnancy eligibility | When applicable, value 2 passes; pregnant and unknown states do not |
| `WTMEC2YR` | DEMO | Development and holdout weight | Divide by two only for the pooled development cycles |
| `SDMVSTRA` | DEMO | Masked variance stratum | Retain through every model row |
| `SDMVPSU` | DEMO | Masked variance PSU | Retain within stratum |
| `BMXBMI` | BMX | Eligibility and predictor | Observed, at least 25 kg/m2, centered at 30 and divided by 5 |
| `DIQ010` | DIQ | Self-reported diabetes history | Only value 2 passes; not a local problem list |
| `LBXGH` | GHB | Historical target source | Observed value at or above 6.5%; not diagnosis |
| `WTPH2YR` | GHB_L | 2021-2023 blood-analyte weight | Required for the transport stress test |

### Derived variables

| Variable | Grain | Meaning |
| --- | --- | --- |
| `participant_id` | Participant-cycle | Stable public teaching identifier containing cycle and `SEQN` |
| `partition` | Participant-cycle | `development`, `temporal_holdout`, or `transport_stress` |
| `model_eligible` | Age-eligible participant-cycle | Passes every fixed cohort and design gate |
| `outcome_hba1c_ge_6_5` | Participant-cycle | Observed cut-point indicator; blank if HbA1c is unavailable |
| `analytic_weight` | Participant-cycle | Partition-specific weight after the declared development division |
| `model_probability` | Model row | Fixed transparent-model score |
| `development_prevalence_baseline` | Model row | Weighted development prevalence repeated as the constant baseline |

### Expected grains

- Cohort audit: one age-eligible public respondent per cycle.
- Model cohort: one complete eligible public respondent per cycle.
- Prediction: one fixed probability per model row.
- Performance: one model-partition combination.
- Calibration summary: one partition.
- Calibration range: one partition and weighted score group.
- Threshold audit: one partition and threshold value.
- Net benefit: one partition, threshold, and strategy.
- Subgroup support: one partition, dimension, and group.
- Bootstrap interval: one evaluation partition and metric.

No synthetic FHIR row is joined to a public NHANES respondent. Public historical evidence and synthetic workflow truth stay separate.

## 10. Worked example and instructor walkthrough

### Starting prompt

The fictional council asks: "The model has an AUC near 0.69. Which threshold should we deploy?"

The correct first response is that the question skips several gates. The evidence must first establish the cohort, target, partition, survey design, baseline, calibration, threshold consequences, support, and authority boundary. This course never authorizes deployment.

### Walkthrough

1. Verify all 16 inherited XPT gzip identities before parsing.
2. Inspect `cohort-flow.csv`: 14,892 people are age eligible and 7,544 reach the final model cohort.
3. Confirm 3,652 development rows and 156 outcomes, 1,806 temporal-holdout rows and 97 outcomes, and 2,086 transport rows and 75 outcomes.
4. Verify that only development rows fit the weighted GLM.
5. Reproduce the four coefficients: intercept `-3.60085649`, age `0.10287215`, BMI `0.41904828`, and female indicator `-0.42667556`.
6. Compare the holdout constant baseline with the transparent model.
7. Read holdout AUC `0.68783144` together with Brier `0.02811126`, calibration-in-the-large `-0.03946013`, and calibration slope `0.88441129`.
8. At threshold `0.02`, observe weighted sensitivity `0.89675075` and about 662 flags per 1,000.
9. At threshold `0.10`, observe weighted sensitivity `0.03841504` and about 17 flags per 1,000.
10. At rejected `0.20`, observe only four flagged holdout rows and zero weighted outcomes captured in transport.
11. Read decision-curve rows only under their threshold-odds assumptions.
12. Compare transport AUC `0.68422573`, Brier `0.03175435`, calibration-in-the-large `0.07788522`, and slope `0.81620710` without assigning a cause.
13. Check support before reading any subgroup AUC or Brier score.

### Correct reference decision

`continue with conditions`

The evidence is complete enough to enter Checkpoint 01 assembly. It is not enough to choose a threshold, begin workflow work before the checkpoint passes, or support any live use.

## 11. Guided practice

### Practice A: reconstruct the target

Classify each phrase as observed result, target, diagnosis, confirmed disease, score, threshold, or action. Correct the phrase "undiagnosed diabetes" to the bounded historical target actually present in the release.

### Practice B: rebuild the cohort flow

Starting from each cycle's interviewed rows, calculate every sequential removal. Identify which losses arise from age, self-reported history, pregnancy status, BMI missingness, BMI eligibility, HbA1c missingness, or design fields.

### Practice C: repair a survey-weight error

Diagnose three broken analyses: unmodified `WTMEC2YR` across both development cycles, `WTMEC2YR` instead of `WTPH2YR` in 2021-2023, and pooling the later stress test into development.

### Practice D: protect the holdout

Review a proposed workflow that changes the BMI term after seeing holdout AUC. Mark the changed model as a new development candidate that requires a new untouched evaluation route.

### Practice E: read calibration

Explain how holdout mean prediction can be close to weighted prevalence while the calibration slope differs from one. Use overall and score-range tables together.

### Practice F: translate thresholds

For `0.02`, `0.04`, `0.075`, and `0.10`, state flags per 1,000, sensitivity, specificity, positive predictive value, missed cases per 1,000, and the unresolved human consequence question.

### Practice G: stop an unsupported subgroup claim

Compare a supported sex row with a suppressed age or race and Hispanic-origin row. Explain why showing a denominator and outcome count is different from reporting a performance estimate or authorizing group action.

### Practice H: separate change from cause

Rewrite "the pandemic caused calibration drift" as a supported transport statement using only the exact release evidence.

## 12. Independent exercise

### Assignment

Complete all 15 assessed records and defend one bounded progression decision. Every numeric statement must trace to an immutable evidence table. Every clinical or operational statement must identify its owner and evidence gap.

### Required decisions

The learner must decide:

1. whether the cohort and target are coherent enough for a teaching analysis;
2. whether the weight and partition rules were correctly applied;
3. whether the model adds historical discrimination or overall-accuracy evidence beyond the baseline;
4. whether calibration is adequately described rather than declared good or bad from one number;
5. which threshold candidates remain worth carrying forward, without selecting one clinically;
6. whether decision-curve assumptions are explicit enough to interpret;
7. whether transport changes are described without unsupported causes;
8. which subgroup performance cells must remain suppressed;
9. whether the evidence can enter Checkpoint 01; and
10. which conditions block Module 04 and every clinical-use route.

### Independent defense questions

1. Why is one HbA1c result not a diagnosis?
2. Why is the 2021-2023 weight different?
3. Which rows fit the model, and which rows never may?
4. What does AUC answer that calibration does not?
5. How can calibration-in-the-large look close while slope remains uncertain?
6. What human values are hidden inside a threshold?
7. Why does a positive net-benefit value not prove benefit?
8. Which subgroup result is suppressed, and what evidence would change that?
9. What exact change invalidates Module 03 but not Module 02?
10. Why must Checkpoint 01 pass before Module 04 begins?

## 13. Visualization and communication requirements

### Required cohort-flow display

Show all nine stages for all four cycles. Label row counts and removals. Do not merge "not eligible" with "unknown" or "missing." Use `cohort-flow.csv` as the exact alternative.

### Required calibration display

Compare weighted mean prediction and weighted observed outcome across the five score ranges for holdout and transport. Include the identity line, overall calibration-in-the-large and slope, teaching intervals, and a note that grouped points do not replace a flexible external calibration curve. Use `calibration.csv`, `calibration-groups.csv`, and `bootstrap-intervals.csv` as exact alternatives.

### Required threshold display

Show all six evidence candidates on the same scale. Include flags and missed eligible cases per 1,000 plus sensitivity and specificity. Mark `0.20` as a rejected mechanics comparison, not an evidence candidate. Do not highlight one candidate as recommended or accepted. Use `threshold-audit.csv` as the exact alternative.

### Required transport display

Show holdout and transport values side by side for prevalence, mean probability, Brier score, log loss, AUC, calibration-in-the-large, slope, and every candidate flag rate. Title the display as a transport stress comparison, not a drift diagnosis or causal explanation. Use `transport-comparison.csv` as the exact alternative.

### Required subgroup display

Lead with rows, outcomes, non-outcomes, effective sample size, and support status. Unsupported performance stays blank. Do not rank protected groups, encode a group as good or bad, or imply a group-specific threshold. Use `subgroup-support.csv` as the exact alternative.

### Communication rules

- State the public source, cycles, weights, population, target, partition, and release.
- Keep observed, predicted, classified, and acted-on quantities separate.
- Write probabilities and rates with named denominators.
- Do not rely on color alone.
- Provide readable labels, keyboard-accessible tables, plain-language summaries, and structured text alternatives.
- Keep unavailable and suppressed values blank with reasons.
- Put the strongest claim limit next to the result it constrains.

## 14. Exact submission package and filenames

### Immutable files

The builder creates a 102-row immutable manifest:

- 73 accepted Module 02 inherited files under `inherited/module02/`;
- 11 Module 03 control files; and
- 18 evidence files, including `evidence-manifest.csv` and the 17 fingerprinted derived outputs.

Learners may read but not modify these files.

### Editable assessed records

The learner submits exactly:

1. `evidence-release.md`
2. `cohort-target-contract.csv`
3. `survey-design-audit.csv`
4. `model-specification.csv`
5. `performance-interpretation.md`
6. `calibration-audit.csv`
7. `threshold-consequence-audit.csv`
8. `decision-curve-interpretation.md`
9. `transport-stress-audit.csv`
10. `subgroup-support-audit.csv`
11. `evidence-limitations.md`
12. `week3-component-release.md`
13. `claim-boundary.csv`
14. `ai-use.md`
15. `progression-decision.md`

The assembled workspace also contains `release-manifest.csv`, for 118 total files.

### File rules

- Filenames and table headers are fixed.
- Complete work contains no `REPLACE` marker.
- Starter work retains a visible `REPLACE` marker in every assessed record.
- Assessed records contain no personal local path.
- Numeric claims trace to immutable evidence.
- Exact tables are CSV; narrative interpretation is Markdown.
- A learner may not replace unavailable evidence with zero, normal, below threshold, or no alert.

## 15. Rubric and pass conditions

| Criterion | Points |
| --- | ---: |
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
| Total | 20.0 |

The complete rubric and 12 noncompensable gates are in `assessment.md`.

### Passing threshold

A learner needs at least 14 of 20 points and must pass all 12 gates. A threshold number, model metric, polished display, or strong narrative cannot compensate for a wrong target, weight, partition, authority claim, unsupported subgroup estimate, or hidden failure.

### Excellence indicators

Excellent work:

- explains why each cycle and weight has its role;
- connects model evidence to exact decision consequences without overclaiming;
- reads calibration across overall and score-range evidence;
- translates all candidates into comparable units;
- surfaces who is excluded and which subgroup estimates are unsupported;
- identifies what evidence would actually change the progression decision; and
- leaves a reviewer able to reproduce every finding without guessing.

## 16. Common errors, failure modes, and instructor interventions

| Error or failure | Why it matters | Instructor intervention |
| --- | --- | --- |
| Calling the target diabetes or undiagnosed diabetes | One HbA1c result is not confirmed disease | Return to the target contract and NIDDK confirmation boundary |
| Treating self-report as a local problem list | Source meaning and local availability differ | Require separate public and synthetic field roles |
| Pooling all four cycles | Destroys the declared temporal and transport design | Rebuild partitions before reading any model output |
| Using the wrong 2021-2023 weight | Ignores blood-draw nonresponse guidance | Trace `WTPH2YR` from GHB_L documentation |
| Tuning after seeing holdout results | Converts evaluation evidence into development evidence | Freeze the result or create a new future evaluation route |
| Reporting AUC alone | Hides probability accuracy and consequence tradeoffs | Require Brier, log loss, calibration, and threshold evidence |
| Declaring calibration good from mean agreement | Ignores slope and score-range behavior | Read all calibration levels together |
| Selecting a threshold from code | Assigns clinical value without human authority | Restore all six candidates and null accepted threshold |
| Promoting `0.20` | Confuses a branch fixture with evidence | Keep the three rejected comparison rows |
| Claiming net benefit proves benefit | Treats assumed threshold odds as observed patient values | State the assumption and missing prospective evidence |
| Reporting a suppressed subgroup AUC | Hides inadequate outcome support | Blank the metric and show denominator and reason |
| Assigning a cause to transport change | Cross-cycle difference does not identify mechanism | Rewrite as a descriptive stress finding |
| Starting Module 04 immediately | Bypasses cumulative Week 3 review | Assemble and pass Checkpoint 01 first |
| Claiming clinical readiness | Historical survey evidence cannot authorize use | Return to the authority contract and stop the package |

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

- Every display has an exact CSV alternative and structured text summary.
- Tables identify headers, units, denominators, status, and missing reasons.
- Status is expressed through text and structure, not color alone.
- Threshold and calibration displays remain interpretable under zoom and grayscale.
- Screen-reader order follows question, source, result, limitation, and action.
- Suppressed and unavailable cells remain labeled rather than disappearing.

### Equity

- The cohort audit shows who is removed by age, history, pregnancy, BMI, missing BMI, missing HbA1c, and design requirements.
- The reference teaching frame does not cover every earlier-age or lower-BMI consideration in the public recommendation.
- Race and Hispanic-origin category is audit only and never a predictor.
- Every subgroup row begins with denominator, outcomes, non-outcomes, effective support, and status.
- The support rule requires at least 100 rows, 20 outcomes, 20 non-outcomes, and effective sample size 50.
- Unsupported Brier and AUC values remain blank.
- No observed difference becomes a trait, fairness certificate, rank, exclusion, or group-specific threshold.
- Module 04 must examine access, language, disability, patient preference, and workflow consequences not observed here.

### Privacy

- Only public-use NHANES respondent identifiers and explicitly synthetic Module 02 data appear.
- No real local patient, clinician, employee, credential, workplace, or restricted data enter the module.
- Public respondent rows cannot be reidentified, linked to outside personal data, or sent to an external agent as a reidentification task.
- The fictional service remains visibly synthetic.

### Responsible claims

Allowed claims describe the exact public release, cohort, model, weighted metrics, candidate tradeoffs, support, reproduction, and curriculum progression.

Prohibited claims include diagnosis, confirmed disease, local prevalence, local event-time availability, causal effect, clinical utility, patient benefit, fairness certification, safe threshold, real-patient score, clinical alert, implementation readiness, or deployment readiness.

## 18. AI and agent policy, required disclosure, and verification

### Permitted assistance

An agent may help:

- draft deterministic parsing, modeling, validation, or visualization code;
- explain a metric using only the accepted evidence;
- propose alternative table wording or accessible text;
- identify a mismatch between records and immutable outputs;
- generate test mutations; and
- organize the release and review checklist.

### Human-only decisions

An agent may not choose or accept:

- intended clinical use;
- final eligibility or exclusion policy;
- diagnostic meaning;
- predictor acceptability;
- clinical threshold or consequence value;
- subgroup action;
- patient communication;
- workflow design;
- safety control;
- checkpoint progression;
- implementation; or
- deployment.

### Required disclosure

`ai-use.md` records:

1. tool and task;
2. data boundary;
3. output used;
4. human decisions preserved;
5. deterministic check;
6. detected error or limitation;
7. revision; and
8. accountable human owners.

### Verification rule

Every agent-assisted analytic result must reproduce from the 16 accepted sources through `build_evidence.py`. Every narrative number must match an immutable table. Source hash change, output mismatch, hidden failure, invented clinical fact, threshold choice, unsupported subgroup result, or prohibited authority claim fails the package.

## 19. Answer key and instructor notes

### Reference cohort and source findings

- The age-eligible audit frame contains 14,892 rows.
- The model cohort contains 7,544 rows and 328 outcomes.
- Development contains 3,652 rows and 156 outcomes.
- Temporal holdout contains 1,806 rows and 97 outcomes.
- Transport stress contains 2,086 rows and 75 outcomes.
- The evidence manifest contains 17 output rows and has SHA-256 `b226b33cc0ba2cec0efe2a5046357b10431941e0c9e286f9be889de05321c9a3`.

### Reference model

| Term | Coefficient | Odds ratio | Interpretation boundary |
| --- | ---: | ---: | --- |
| Intercept | -3.60085649 | 0.02730033 | At centered reference values; not baseline clinical risk |
| Age per 10 years from 50 | 0.10287215 | 1.10834970 | Prediction association, not causal |
| BMI per 5 kg/m2 from 30 | 0.41904828 | 1.52051377 | Prediction association, not causal |
| Female indicator | -0.42667556 | 0.65267527 | Source coding, not gender identity or treatment rule |

### Reference evaluation

| Measure | Temporal holdout | Transport stress |
| --- | ---: | ---: |
| Weighted prevalence | 0.02904272 | 0.03274014 |
| Weighted mean probability | 0.03015261 | 0.03041245 |
| Weighted Brier score | 0.02811126 | 0.03175435 |
| Weighted log loss | 0.12694930 | 0.14019059 |
| Weighted ROC AUC | 0.68783144 | 0.68422573 |
| Calibration-in-the-large | -0.03946013 | 0.07788522 |
| Calibration slope | 0.88441129 | 0.81620710 |

The point results support historical discrimination above a constant baseline but do not select a threshold or establish local utility.

### Reference threshold findings

- `0.02` has high historical sensitivity and very high candidate-card burden.
- `0.03` through `0.05` progressively reduce flags while increasing missed eligible outcomes.
- `0.075` and `0.10` produce low flag rates with very low sensitivity.
- `0.20` is rejected; in the transport stress test it captures zero weighted outcomes.
- All six evidence candidates remain open and unaccepted.

### Reference subgroup findings

The holdout has eight supported and eight suppressed subgroup-performance rows. The transport stress test has five supported and 11 suppressed rows. Suppression is part of the result, not missing work. No group-specific threshold or action is allowed.

### Reference progression

`continue with conditions`

Checkpoint 01 assembly may begin. Module 04 remains prohibited until the cumulative checkpoint passes. The accepted-threshold value remains null.

### Instructor stop points

Stop the exercise if a learner:

- changes a cohort rule without versioning and rebuilding;
- calls the outcome diagnosis;
- retunes on holdout or transport data;
- uses the wrong later-cycle weight;
- chooses a threshold;
- fills a suppressed subgroup metric;
- invents a cause for transport change;
- claims patient benefit or local validity; or
- bypasses Checkpoint 01.

## 20. Runnable acceptance checks for data, code, links, and expected findings

### Source release checks

`build_evidence.py` must:

- verify all 16 inherited gzip byte counts and SHA-256 identities before parsing;
- reject duplicate `SEQN` within any component-cycle file;
- keep cycle joins one-to-one;
- preserve all 145,563 component rows in the source inventory;
- construct exactly 14,892 age-eligible audit rows;
- construct exactly 7,544 model rows and 328 outcomes;
- assign exactly 3,652 development, 1,806 holdout, and 2,086 transport rows;
- use `WTPH2YR` in transport;
- fit zero holdout or transport rows;
- produce 17 fingerprinted evidence files;
- pass 20 invariants;
- refuse overwrite;
- produce two byte-identical clean builds; and
- reject a changed inherited source.

Commands:

```powershell
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/build_evidence.py --self-check
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/build_evidence.py --verify
```

### Evidence contract checks

The validator must confirm:

- evidence manifest SHA-256 `b226b33cc0ba2cec0efe2a5046357b10431941e0c9e286f9be889de05321c9a3`;
- six performance rows, three calibration rows, 15 score-range rows, 21 threshold rows, 63 net-benefit rows, 48 subgroup rows, 48 bootstrap rows, and 13 transport rows;
- holdout AUC `0.68783144` and Brier `0.02811126`;
- transport AUC `0.68422573` and Brier `0.03175435`;
- six evidence candidates;
- three rejected `0.20` partition rows;
- null accepted threshold;
- blank unsupported subgroup performance;
- 500 valid replicates for every bootstrap metric; and
- no threshold metric in a subgroup row.

### Workspace checks

`build_workspace.py` and `validate_workspace.py` must:

- freeze exactly 73 Module 02 inherited files;
- create a 102-row immutable manifest;
- create 15 editable assessed records;
- create exactly 118 files;
- produce byte-identical reference manifests;
- validate complete and starter packages;
- reject changed immutable evidence;
- reject copied reference work in starter mode;
- reject missing assessed records;
- reject placeholders in complete mode;
- reject accepted-threshold language;
- reject diagnosis language;
- reject holdout retuning; and
- reject deployment authority.

Commands:

```powershell
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/build_workspace.py --self-check
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/validate_workspace.py --self-check
```

### Manual checks

1. Read the outcome wording aloud and confirm that it does not claim diagnosis.
2. Trace every reference number to an immutable table.
3. Confirm that `0.20` is visually and textually rejected.
4. Confirm that no candidate is highlighted as selected or accepted.
5. Inspect suppressed subgroup outputs for blank performance fields.
6. Confirm that every display has an exact table and readable text alternative.
7. Confirm that transport statements describe changes without causes.
8. Confirm that Module 04 remains gated by Checkpoint 01.
9. Confirm that no personal local path appears.
10. Have a qualified human reproduce the release before alpha.

### Full curriculum regression

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

All previously accepted course, module, checkpoint, data, workspace, and claim contracts must continue to pass.

## 21. Release status, reviewers, version, and known issues

### Release

- Module version: `0.1.0`.
- Commons release: `0.79.0`.
- Status: runnable release candidate.
- Reference progression: `continue with conditions`.
- Next permitted unit: APP-4 Checkpoint 01 assembly.
- Module 04 status: prohibited until Checkpoint 01 passes.
- Accepted threshold: none.
- Clinical use, real-patient scoring, alerting, implementation, and deployment: prohibited.

### Required reviewers before alpha

- APP-4 faculty owner;
- Joe Joseph, MD, SFHM, as clinician of record for the later leadership block;
- primary-care or endocrinology clinical-content reviewer;
- biostatistics and calibration reviewer;
- NHANES complex-survey methods reviewer;
- clinical informatics reviewer;
- patient and caregiver reviewer;
- equity, access, language, and disability reviewer coverage;
- privacy and data-governance reviewer;
- responsible-AI and model reviewer;
- accessibility and communication reviewer; and
- independent reproduction reviewer.

### Known issues and open decisions

- The official APP-4 section and half-term dates still require program assignment.
- The USPSTF-aligned reference frame does not encode every earlier-age, lower-BMI, symptom, or risk-based screening route.
- Clinical reviewers must confirm the final target wording, exclusions, predictor acceptability, and confirmatory-action language.
- A named survey-methods reviewer must confirm the coefficient and prediction-performance variance approach.
- The deterministic PSU bootstrap is a teaching sensitivity method, not a publication-grade endorsement.
- No smooth calibration curve is released; weighted score groups supplement but do not replace one.
- Complete-case selection may affect the historical evidence population.
- Later-cycle differences have no assigned cause.
- Many subgroup performance cells are suppressed.
- All six threshold candidates still require patient, clinical, workflow, capacity, safety, equity, and governance review.
- The `0.20` value remains a rejected mechanics fixture.
- Named human review and clean independent reproduction remain pending before alpha.

Construction acceptance:

- [x] The 73-file Module 02 handoff is frozen.
- [x] All 16 public sources are verified before parsing.
- [x] The cohort, target, partitions, weights, and model are executable.
- [x] The 17-file evidence release reproduces byte for byte.
- [x] Holdout and transport evidence remain untuned and separate.
- [x] Calibration, threshold, decision-curve, subgroup, transport, and uncertainty tables are complete.
- [x] No clinical threshold is selected or accepted.
- [x] The workspace and validator cover the required failure routes.
- [x] The 20-point component and Checkpoint 01 handoff are explicit.
- [x] Every clinical-use and deployment route remains prohibited.

APP-4 Module 03 is complete for curriculum construction. Resume with APP-4 Checkpoint 01 by freezing the exact accepted Module 02 and Module 03 packages, preserving all 40 source points once, reconciling their conditions, and making one cumulative progression decision before Module 04 begins.

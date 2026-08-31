# APP-4 Data for Clinical Decision Support source record

- Source course ID: APP-4.
- Source title: Data for Clinical Decision Support.
- Source filename: `08-APP-4-Clinical-Decision-Support.docx`.
- Source bytes: 21,676.
- Source SHA-256: `20d651c3a777c878fa2d1219738366b99da76ba985e6082c73168cf8df63ded2`.
- Verified: 2026-08-30.
- Commons course specification: `docs/curriculum/courses/APP-4/course-spec.md`.

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`; and
- `OneDrive_2026-08-29 (1).zip`.

The APP-4 DOCX files are byte-for-byte identical. Both are 21,676 bytes and have the SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Primary graded tools: SQL and Python with pandas and notebooks.
- R role: read, run, and interpret calibration and decision-curve work; writing R from scratch is not graded.
- Interoperability environment: nonproduction FHIR R4 and CDS Hooks sandbox.
- Versioning and accountability: Git, release records, and an AI-use log.

The Commons treats the source's seven weeks as seven instructional weeks inside an official half-term. Week 3 and Week 6 are instructional checkpoints. The final checkpoint is due on the official last day of the assigned half-term.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Source purpose and ownership

APP-4 teaches learners to decide whether a clinical decision support concept is useful and safe enough to move beyond offline analysis. Learners define the user, workflow moment, intended action, safety boundary, logic, trigger, threshold, input availability, evidence, calibration, validation, subgroup performance, alert burden, failure modes, monitoring, escalation, retirement, and human owner.

APP-4 does not repeat generic data retrieval, cleaning, SQL, regression, classification, visualization, or reproducible repository instruction. It revisits those foundation skills through one sociotechnical decision support problem. The course owns the gap between a technically evaluated prediction and a support tool that may affect a clinician, patient, and workflow.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Framing a decision support use case | 15.5 | CDS use-case charter |
| 2 | Decision support logic, triggers, and data | 16.0 | Logic and data-input specification |
| 3 | Evidence, calibration, and validation | 16.5 | CDS evidence and calibration audit |
| 4 | Alert burden, human factors, and equity | 16.5 | Workflow and alert-burden review |
| 5 | Sandbox prototype and failure modes | 16.0 | Sandbox prototype checkpoint |
| 6 | Safety case, monitoring, and governance | 16.0 | Draft CDS safety and monitoring plan |
| 7 | Product brief and defense | 16.0 | Final CDS package |
| Total |  | 112.5 |  |

## Source learning objectives

The source defines six course objectives:

1. frame a decision support use case around a user, workflow moment, intended action, and safety boundary;
2. specify transparent logic, triggers, thresholds, and data requirements;
3. evaluate evidence, calibration, thresholds, net benefit, subgroup performance, and prospective validity;
4. assess alert burden, usability, automation bias, equity, privacy, and failure-related harm;
5. build a nonproduction sandbox prototype and safety case that separates demonstration from deployment and makes silent failure visible; and
6. defend an implementation, monitoring, escalation, and retirement plan under human clinical ownership.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Use-case and logic specification | End of Week 2 | 20% |
| Evidence, calibration, and threshold audit | End of Week 3 | 20% |
| Workflow, alert-burden, and equity review | End of Week 4 | 25% |
| Final CDS product brief, prototype, evaluation, and safety case | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The Commons preserves every source point exactly once:

- Week 3: the 20-point use-case and logic specification and 20-point evidence, calibration, and threshold audit form one cumulative 40-point technical release. Module 01 evidence is required but adds no points.
- Week 6: the 25-point workflow, alert-burden, and equity review remains the scored component. Modules 05 and 06 add required sandbox, failure-mode, safety, monitoring, governance, and embedded-ML gates without adding points.
- Official half-term end date: the final CDS package remains 35 points.

Weeks 2 and 4 remain feedback milestones. They do not create extra course points. The course total is `40 + 25 + 35 = 100`.

## Materials the source says must be developed

The source requires:

- a synthetic clinical scenario with a risk-prediction cohort, temporal holdout, predictions, and a simulated post-deployment stream;
- seeded calibration drift, stale or missing inputs, alert-burden problems, and at least one silent-failure route;
- a CDS charter, logic and input specification, evidence and calibration audit, workflow review, prototype, safety case, monitoring plan, and product brief;
- nonproduction FHIR and CDS Hooks examples, test and edge cases, a threshold and alert-budget worksheet, governance prompts, and an AI-use log; and
- answer keys and rubrics for logic, calibration, workflow, failure modes, safety, monitoring, and defense.

These are build requirements. The source DOCX does not contain runnable data or code.

## Commons continuing decision

The course uses an explicitly fictional adult general internal medicine and primary care service, `CGH-GIM-01`, at Commons General Hospital. Learners decide whether an advisory card that asks a clinician to consider confirmatory HbA1c testing may advance from offline sandbox review to a proposal for a locally governed, time-limited silent-mode evaluation.

The advisory is considered only after required encounter data are available and before the encounter closes. It must remain reviewable, dismissible, attributable, and nonbinding. It cannot diagnose diabetes, place an order, block care, deny a service, target a person for nonclinical action, or change treatment automatically.

The course package may recommend seeking local approval for a silent-mode evaluation. It cannot grant that approval, connect to a live clinical system, process real patient data, start prospective scoring, display an alert to a clinician, or authorize deployment.

## Full public evidence architecture

### NHANES role

The National Health and Nutrition Examination Survey supplies full public releases for historical risk evidence, temporal validation, calibration, decision-threshold analysis, and subgroup support. It does not represent the fictional service, local prevalence, local workflow, current input availability, local alert burden, or prospective clinical utility.

Official NHANES portal:

https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/

Official analytic guidance:

https://wwwn.cdc.gov/Nchs/data/nhanes/analyticguidelines/11-16-analytic-guidelines.pdf

The initial full-release candidate contains four complete source files from each of four survey cycles. All 16 resource URLs returned HTTP 200 during source-contract verification on 2026-08-30.

| Cycle | Role | Complete XPT resources |
|---|---|---|
| 2013-2014 | earlier development evidence | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/DEMO_H.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/BMX_H.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/DIQ_H.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/GHB_H.xpt |
| 2015-2016 | later development evidence | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DEMO_I.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/BMX_I.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DIQ_I.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/GHB_I.xpt |
| 2017-2018 | temporal holdout | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/BMX_J.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DIQ_J.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/GHB_J.xpt |
| 2021-2023 | later-cycle transport stress test | https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DIQ_L.xpt ; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/GHB_L.xpt |

`DEMO` supplies demographic and survey-design fields, `BMX` supplies body measures, `DIQ` supplies diabetes questionnaire fields, and `GHB` supplies glycohemoglobin laboratory fields. Files join within a cycle on `SEQN` only after uniqueness, eligibility, missingness, codebook, and survey-design checks pass.

Module 01 must download and inspect every complete XPT file before a derived teaching table is created. It must record the final URL, retrieval date, bytes, SHA-256, rows, fields, `SEQN` uniqueness, duplicate state, missingness, codebook link, cycle, survey-design variables, weight choice, and release limitation. The source contract does not predeclare hashes or row counts that have not yet been reproduced.

The course must preserve cycle boundaries, survey design, unavailable values, and later-cycle comparability limits. A pooled or weighted estimate requires a documented weight decision. The 2021-2023 cycle is a transport and drift stress test, not a claim that the survey changed because of one known cause.

### Interoperability and sandbox standards

CDS Hooks published specification, version 2.0.1:

https://cds-hooks.hl7.org/

FHIR R4 Observation resource:

https://hl7.org/fhir/R4/observation.html

FHIR R4 Condition resource:

https://hl7.org/fhir/R4/condition.html

These specifications define the teaching message and resource shapes. They do not certify conformance, implementation readiness, security, terminology coverage, or interoperability with a real electronic health record.

### Synthetic clinical record generator

Synthea supplies an open-source route for generating synthetic patient records:

https://github.com/synthetichealth/synthea

The construction candidate pins Synthea version 4.0.0:

https://github.com/synthetichealth/synthea/releases/tag/v4.0.0

The module build must record the exact release, executable identity, configuration, seed, population, exporter, generated-resource counts, bytes, hashes, and generation log. If the accepted release changes, the module needs a new source record and semantic-version decision.

Synthea data are synthetic. They do not establish real prevalence, model performance, workflow fit, safety, burden, fairness, or deployment readiness.

### Safety and implementation guidance

ONC SAFER Guides landing page:

https://www.healthit.gov/topic/safety/safer-guides

ONC SAFER Computerized Provider Order Entry with Decision Support guide:

https://www.healthit.gov/wp-content/uploads/2025/06/SAFER-Guide-3.-CPOE-Final.pdf

The guidance supports review questions about governance, workflow, monitoring, unintended consequences, and safe use. It does not replace local policy, security review, clinical approval, validation, or implementation testing.

## Synthetic workflow and monitoring layer

Public NHANES data do not contain a linked local workflow, event-time input state, CDS request and response log, clinician interaction, alert burden, interface failure, or known silent-failure truth. The Commons therefore builds a separate synthetic release for `CGH-GIM-01`.

The release must contain at least these linked tables or FHIR-derived equivalents:

| Table or resource set | Required grain and role |
|---|---|
| patients | one synthetic person with eligibility and explicit synthetic identity |
| encounters | one synthetic encounter with service, start, decision moment, and close time |
| observations | one synthetic observation with code, value, unit, status, effective time, and availability time |
| conditions | one synthetic condition record with clinical status, verification status, and recorded time |
| predictions | one offline prediction with model version, information cutoff, score, calibration version, and eligibility |
| cds-requests | one synthetic hook invocation with hook, context, prefetch identity, and request time |
| cds-responses | one synthetic card or no-card result with reason, threshold, rule trace, and response time |
| interactions | one synthetic view, dismissal, acknowledgment, deferment, or unavailable state |
| monitoring-stream | one synthetic interval with eligibility, firing, display, interaction, outcome availability, drift, latency, and silent-failure fields |
| known-truth | one seeded logic, data, workflow, calibration, burden, or silent-failure condition |

Every generated layer requires a generator version, seed, field dictionary, row and resource counts, bytes, checksums, referential tests, FHIR-shape checks, known-truth contract, defect register, explicit synthetic flag, and a statement that no record may enter a live clinical system.

## Source-to-module routing

| Module | Source role | Protected handoff |
|---:|---|---|
| 01 | Inspect all 16 NHANES files, standards, safety guidance, and synthetic-generation route; define the fictional service, intended use, user, workflow moment, action, and boundary. | Source feasibility, use-case charter, data-role map, ownership map, and claim boundary. |
| 02 | Build transparent rule, trigger, input-availability, terminology, threshold, alert-budget, and traceability specifications. | Accepted 20-point use-case and logic component. |
| 03 | Build the historical evidence cohort and audit discrimination, calibration, thresholds, net benefit, temporal validity, later-cycle transport, and subgroup support. | Accepted 40-point Week 3 technical release. |
| 04 | Test workflow fit, alert burden, usability, automation bias, privacy, access, subgroup consequences, and human override. | Accepted 25-point workflow and equity component. |
| 05 | Build and test a nonproduction FHIR R4 and CDS Hooks sandbox with normal, edge, stale, missing, inconsistent, delayed, and silent-failure cases. | Accepted sandbox and failure-mode evidence. |
| 06 | Add the safety case, monitoring, drift, escalation, stop, retirement, governance, and bounded ML comparison without changing accepted evidence silently. | Accepted 25-point Week 6 application release and Module 07 permission. |
| 07 | Freeze both checkpoints and add clinician leadership, product brief, communication, accountability, evaluation proposal, stewardship, and defense. | Accepted or conditioned final course package. |

## Embedded machine-learning decision

Module 06 contains eight hours of safety, monitoring, and governance work plus an eight-hour ML extension. The extension compares the accepted transparent logistic model with one fixed gradient-boosted classification challenger using the same target, eligible predictors, information cutoff, development cycles, temporal holdout, later-cycle stress test, missing-input rules, threshold candidates, alert budget, and evaluation rows.

The comparison must report calibration, sensitivity, specificity, predictive values, alert count, alerts per encounter, missed eligible cases, subgroup support, later-cycle drift, missing-input behavior, failure cases, reproducibility, and leakage tests. The accepted decision rule must consider calibration, burden, safety, and interpretability, not only discrimination.

ML may challenge the transparent model or fail to improve it. It cannot change the intended use, invent unavailable inputs, set a clinical threshold autonomously, replace the workflow review, conceal calibration failure, automate a clinical action, or replace human governance.

## Stable source decisions

- APP-4 remains a distinct applied course.
- The course totals 112.5 hours.
- SQL and Python are graded working tools; R remains read-run-interpret.
- APP-4 owns workflow logic, triggers, input availability, thresholds in use, calibration in use, alert burden, human factors, sandbox prototyping, failure modes, safety cases, monitoring, governance, and retirement.
- NHANES provides full public historical evidence. It does not provide local workflow evidence or deployment validity.
- `CGH-GIM-01` is fictional and the FHIR/CDS Hooks layer is synthetic and nonproduction.
- Module 06 contains eight hours of safety, monitoring, and governance plus an eight-hour embedded ML extension.
- Module 07 is clinician led.
- Checkpoints preserve the source weights as 40 points at Week 3, 25 points at Week 6, and 35 points on the official half-term end date.
- Full public releases must be acquired, inspected, and fingerprinted before derived teaching evidence is created.
- No protected, identifiable, workplace, restricted patient, or live clinical-system data enter the Commons or an external agent.

## Interpretation rule

The source document controls curriculum intent, workload, and assessment weight. The Commons specification adds exact public-source routes, synthetic boundaries, interoperability contracts, filenames, checkpoints, validation, accessibility, reviewer, leadership, and release controls needed to make the course runnable.

# APP-4: Data for Clinical Decision Support

## 1. Course identity and catalog role

- Course ID: APP-4.
- Title: Data for Clinical Decision Support.
- Credits: 3.
- Delivery: online half-term.
- Planning rhythm: seven instructional weeks plus the official half-term end date.
- Total learner work: 112.5 hours.
- Prerequisites: accepted FND-1 and FND-2 technical releases.
- Primary graded tools: SQL and Python.
- R role: read, run, and interpret calibration and decision-curve code; writing R from scratch is not graded.
- Interoperability role: build and inspect nonproduction FHIR R4 and CDS Hooks examples.
- Final deliverable: clinical decision support package with a nonproduction prototype, safety case, monitoring plan, and defense.
- Course version target: 0.1.0.
- Current Commons release: 0.85.0 through Module 07.
- Specification status: construction candidate.

APP-4 is where learners take a prediction or rule into a specific clinical workflow and decide whether it is useful and safe enough to deserve further evaluation. The work starts with the person receiving support, the moment they receive it, the action they may consider, and the harm the tool could cause. Learners then specify logic and inputs, audit calibration and thresholds, count burden, test failure modes in a sandbox, and build a human-owned safety and monitoring case.

The academic calendar controls each due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase is a planning model. Week 3 and Week 6 are instructional checkpoints. The final package is due on the published last day of the assigned half-term.

| Half-term | Published dates | Inclusive calendar days | Approximate weeks |
|---|---|---:|---:|
| Fall 2026 half-term 1 | September 8 through October 27 | 50 | 7.14 |
| Fall 2026 half-term 2 | October 28 through December 18 | 52 | 7.43 |
| Spring 2027 half-term 1 | January 11 through March 2 | 51 | 7.29 |
| Spring 2027 half-term 2 | March 3 through April 24 | 53 | 7.57 |
| Summer 2027 half-term 1 | May 10 through June 29 | 51 | 7.29 |
| Summer 2027 half-term 2 | June 30 through August 20 | 52 | 7.43 |

## 2. Source authority and normalization

The source course is `08-APP-4-Clinical-Decision-Support.docx`, 21,676 bytes, SHA-256 `20d651c3a777c878fa2d1219738366b99da76ba985e6082c73168cf8df63ded2`. Byte-identical copies appear in both supplied curriculum archives.

The source record is `docs/source/app-4-clinical-decision-support-source-record.md`.

The source defines seven modules totaling 112.5 hours and assessments weighted 20, 20, 25, and 35 percent. The Commons preserves every point once:

- Week 3: 40 points;
- Week 6: 25 points; and
- official half-term end date: 35 points.

The Week 3 release combines the use-case and logic specification with the evidence, calibration, and threshold audit. The Week 6 release carries the accepted workflow, alert-burden, and equity score and adds required sandbox, failure-mode, safety, monitoring, governance, and embedded-ML gates. The final package adds clinician leadership, communication, stewardship, accountability, and defense without rescoring earlier work.

APP-4 does not inherit another applied course's checkpoint weights. Its source assessment plan is authoritative, so APP-4 uses `40 / 25 / 35`.

## 3. Place in the program and prerequisite handoffs

### FND-1 handoff

Learners arrive able to maintain a reproducible repository, retrieve and join complete public releases, define cohorts and denominators, clean and profile data, record provenance, preserve raw data, publish exact tables, and verify agent-assisted work.

APP-4 does not reteach generic project setup, SQL, data cleaning, missing-value handling, or public-data acquisition. It applies those skills to event-time input availability, clinical terminology, trigger traces, workflow logs, versioned predictions, sandbox messages, and silent-failure surveillance.

### FND-2 handoff

Learners arrive able to define an analytic aim, target, outcome window, and information cutoff; fit transparent regression and classification models; preserve temporal order; evaluate discrimination and calibration; compare thresholds; audit subgroup support; and document model limits.

APP-4 does not prove that a model can predict. It asks whether a model or rule can support one person at one workflow moment without creating unacceptable burden or harm. Thresholds, missing inputs, alert budgets, override, drift, failure detection, escalation, retirement, and clinical ownership become part of the decision.

### DA-730 handoff

Learners use accessible tables, calibration displays, threshold summaries, monitoring charts, interface mockups, and audience adaptation from DA-730. APP-4 grades these artifacts for decision support meaning, not chart mechanics.

### Applied-course handoffs

- APP-1 supplies careful clinical outcome and care-pathway reasoning. APP-4 does not reuse an APP-1 model as deployment evidence unless its identity and intended use are accepted explicitly.
- APP-2 supplies patient burden, trust, access, and representation questions. APP-4 owns how those concerns affect the alert and workflow.
- APP-3 supplies operational measures, process reliability, monitoring, and escalation reasoning. APP-4 owns the CDS trigger, response, failure, and governance contract.

### Downstream handoff

- APP-5 may reuse subgroup-support and fairness questions but owns population denominators, geography, targeting, and community accountability.
- APP-6 may reuse the monitoring and evaluation proposal but owns causal estimands and study design.
- CAP-1 may use the frozen safety case and governance record only after it preserves the exact accepted release and its limits.

## 4. Course decision and named audiences

The continuing teaching decision is:

> Should the explicitly fictional `CGH-GIM-01` adult general internal medicine and primary care service propose a locally governed, time-limited silent-mode evaluation of an advisory card that asks a clinician to consider confirmatory HbA1c testing, or should the concept be revised, referred, or stopped?

The card may be evaluated only after required encounter data are available and before the encounter closes. It cannot diagnose diabetes, place an order, block care, deny a service, change treatment, or act without clinician review.

### Primary decision owner

The primary owner is a fictional clinical decision support governance council led jointly by a clinical informatics physician, primary care clinical lead, nursing or workflow lead, patient-safety lead, and data steward. The council may accept, condition, revise, refer, or stop a proposal to seek local approval. A curriculum package does not authorize silent-mode scoring, implementation, or deployment.

### Required audiences

| Audience | What they need |
|---|---|
| Clinicians receiving the card | intended use, trigger, timing, evidence, uncertainty, action, override, and burden |
| Patients and patient representatives | purpose, privacy, access, subgroup consequences, recourse, and limits |
| Clinical informatics and EHR teams | hook, context, input availability, terminology, trace, latency, version, and failure state |
| Primary care and relevant specialty reviewers | clinical meaning, confirmatory action, exclusions, contraindications, safety, and unsupported claims |
| Quality and patient-safety teams | failure modes, incident routes, monitoring, escalation, stop, fallback, and retirement |
| Workflow, nursing, and operations leads | alert count, timing, interruption, role fit, workload, handoffs, and competing work |
| Analytics and data stewards | cohort, target, cutoff, model version, calibration, thresholds, drift, lineage, and reproduction |
| Governance and privacy reviewers | intended use, prohibited use, data minimization, access, approval, audit, and accountability |

## 5. Course learning outcomes

By the end of APP-4, learners can:

| ID | Assessable course outcome | Program connection |
|---|---|---|
| CLO-1 | Frame a CDS use case with a named user, workflow moment, intended action, benefit, safety boundary, accountable owner, and stop condition. | Applied framing and leadership |
| CLO-2 | Specify testable logic, triggers, inputs, terminology, timing, thresholds, alert modality, traceability, and unavailable states. | FND-1 data work applied to CDS |
| CLO-3 | Audit discrimination, calibration, thresholds, net benefit, temporal validity, transport, subgroup support, and alert workload for the intended use. | FND-2 modeling applied to CDS |
| CLO-4 | Evaluate workflow fit, alert burden, usability, automation bias, access, equity, privacy, override, and human consequences. | Human factors and sociotechnical application |
| CLO-5 | Build and validate a nonproduction FHIR R4 and CDS Hooks prototype with normal, edge, stale, missing, inconsistent, delayed, and silent-failure cases. | Interoperability and reproducibility |
| CLO-6 | Assemble a safety case with monitoring, calibration-drift detection, incident routes, escalation, stop, fallback, restart, governance, and retirement rules. | Safety and governance |
| CLO-7 | Defend a bounded recommendation that separates curriculum acceptance, technical evidence, local approval, silent-mode evaluation, clinical use, and deployment. | Clinician leadership and accountability |

## 6. Concept ownership and boundaries

### APP-4 owns

- intended use, named user, workflow moment, intended action, and prohibited action;
- clinical decision support rights, sociotechnical fit, and human ownership;
- rule logic, model use, hook, context, trigger, firing, suppression, and response trace;
- data availability at the decision, observation timing, terminology, units, missingness, staleness, and inconsistency;
- threshold choice in relation to calibration, alert budget, missed cases, workload, and harm;
- temporal validity, later-cycle transport, subgroup support, and decision-curve interpretation;
- alert burden, interruption, usability, automation bias, override, access, privacy, and equity in use;
- nonproduction FHIR R4 and CDS Hooks prototyping;
- failure-mode analysis, silent-failure detection, latency, logging, versioning, and rollback evidence;
- safety cases, monitoring, drift, escalation, stop, fallback, restart, governance, and retirement; and
- a clinician-led CDS product brief and defense.

### APP-4 extends rather than repeats

- FND-1 owns generic data engineering, source acquisition, cleaning, SQL, provenance, and reproducible release work.
- FND-2 owns generic regression, classification, prediction evaluation, calibration, validation, model cards, and model monitoring.
- DA-730 owns visualization concepts, perception, accessibility, uncertainty displays, dashboards, and communication design.
- APP-1 owns longitudinal clinical-care analysis, treatment comparison, survival, risk adjustment, care-pathway variation, and clinical improvement recommendations.
- APP-2 owns patient-reported measures, response, missingness, representation, patient voice, and partnered engagement.
- APP-3 owns operational measures, statistical process control, demand, capacity, queues, scenarios, balancing measures, and clinical performance improvement.

APP-4 revisits these methods only when they change a decision support use case. A calibrated model is necessary evidence, not a sufficient reason to create an alert.

### Out of scope

- real patient, clinician, employee, protected, workplace, or restricted data;
- connection to a live EHR, identity provider, message bus, terminology service, or clinical network;
- clinical diagnosis, treatment recommendation, order placement, denial, triage, or patient targeting;
- real silent-mode scoring, alert display, implementation, staged rollout, or deployment;
- autonomous threshold, alert, safety, monitoring, escalation, or retirement decisions;
- claims of regulatory compliance, medical-device status, security certification, FHIR conformance, or vendor readiness;
- a complete diabetes-screening guideline or substitute for clinical judgment; and
- causal claims that the advisory improves outcomes.

## 7. Continuing source and analytic thread

### Full public evidence

The course uses 16 complete NHANES XPT files from the 2013-2014, 2015-2016, 2017-2018, and 2021-2023 cycles. Each cycle contributes demographics, body measures, diabetes questionnaire, and glycohemoglobin files.

The development period uses the earlier cycles. The 2017-2018 cycle is a temporal holdout. The 2021-2023 cycle is a later-cycle transport and drift stress test. Module 01 must download, fingerprint, profile, and inspect all 16 files before any derived teaching table is accepted.

NHANES provides population-survey evidence. It does not validate the fictional service, prove local utility, represent local workflow, or supply alert-interaction data. Survey design, weights, cycle differences, missingness, and outcome ascertainment remain visible throughout the course.

### Transparent model and decision rule

The initial model family is a predeclared transparent logistic regression using a small set of information that the synthetic workflow can make available at the decision time. The final predictor list, outcome definition, exclusions, units, and threshold candidates require qualified clinical and methods review before alpha.

The accepted model must preserve a fixed information cutoff and report calibration as well as discrimination. Threshold selection must state the implied number of cards, missed eligible cases, burden, and unsupported actions. No threshold may be chosen by an agent or average performance score alone.

### Synthetic workflow release

The synthetic `CGH-GIM-01` release uses FHIR R4-shaped patients, encounters, observations, and conditions plus CDS Hooks-shaped requests and responses. It adds predictions, interactions, a monitoring stream, and known truth for logic defects, input staleness, missingness, burden, calibration drift, delayed response, and silent failure.

Synthea 4.0.0 is the candidate upstream generator. A deterministic Commons layer creates the fictional service workflow and seeded failures. The exact generator, configuration, seed, population, resource counts, checksums, and defects become fixed in Module 01 and Module 02 releases.

### Safety guidance

CDS Hooks 2.0.1 and FHIR R4 define the teaching shapes. ONC SAFER guidance supplies review prompts for safe use. None of these sources certifies the prototype, validates local practice, or grants implementation authority.

## 8. Workload and module sequence

| Module | Title | Hours | Assessment role |
|---:|---|---:|---|
| 01 | Framing a decision support use case | 15.5 | Required Week 3 gate |
| 02 | Decision support logic, triggers, and data | 16.0 | 20-point Week 3 component |
| 03 | Evidence, calibration, and validation | 16.5 | 20-point Week 3 component |
| 04 | Alert burden, human factors, and equity | 16.5 | 25-point Week 6 component |
| 05 | Sandbox prototype and failure modes | 16.0 | Required Week 6 gate |
| 06 | Safety case, monitoring, governance, and embedded machine learning | 16.0 | Required Week 6 gate |
| 07 | Clinician leadership, product brief, and defense | 16.0 | 35-point final component |
| Total |  | 112.5 | 100 points |

Modules 01 through 03 form the applied technical block. Modules 04 through 06 form the workflow, prototype, and safety block. Module 06 contains eight hours of safety, monitoring, and governance and eight hours of embedded ML. Module 07 is clinician led.

## 9. Module 01 brief: Framing a decision support use case

- Module ID: `oclc-app4-01`.
- Hours: 15.5.
- Package path: `courses/clinical-decision-support/modules/01-cds-use-case-decision/`.
- Specification: `docs/curriculum/courses/APP-4/modules/01-cds-use-case-decision-spec.md`.
- Decision: may the fictional advisory concept proceed to logic and input specification?
- Submission: CDS use-case charter and source-feasibility release.
- Point role: required zero-point gate for Checkpoint 01.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.77.0`; Module 02 construction is permitted with conditions.

Learners identify the receiving clinician, patient consequence, encounter boundary, decision moment, intended action, alternative action, nonaction, possible benefit, possible harm, accountable owner, and people who can pause the concept. They draw the workflow before adding an alert.

The module acquires and inspects all 16 complete NHANES files, the interoperability specifications, safety guidance, and the synthetic-generation route. It records what each source can and cannot support. It defines the fictional service and prohibits linkage to a real facility or patient.

Progression requires an accepted intended-use statement, user and workflow map, source feasibility record, public-versus-synthetic data-role map, preliminary input-availability inventory, clinical and patient consequence map, ownership and decision-rights record, claim boundary, and decision to begin logic construction.

No prediction, threshold choice, alert firing, clinical recommendation, or implementation claim is allowed in Module 01.

The accepted release contains all 16 complete NHANES XPT files as deterministic gzip artifacts. The official raw files total 34,221,200 bytes and 145,563 component rows; the repository copies total 3,149,043 gzip bytes. The 442-row field inventory and four-row join profile reproduce, every file has unique `SEQN`, and the all-four intersections are 6,979, 6,744, 6,401, and 7,199 across the four cycles. The learner and reference workspaces each contain 41 files with a 29-row immutable manifest. Complete validation passes 177 checks, starter validation passes 121 checks, and six protected failure routes pass.

## 10. Module 02 brief: Decision support logic, triggers, and data

- Module ID: `oclc-app4-02`.
- Hours: 16.0.
- Package path: `courses/clinical-decision-support/modules/02-logic-triggers-data/`.
- Specification: `docs/curriculum/courses/APP-4/modules/02-logic-triggers-data-spec.md`.
- Decision: is the rule and input contract testable, traceable, and bounded enough to enter evidence review?
- Submission: 20-point use-case, logic, and data-input specification.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.78.0`; Module 03 construction is permitted with conditions.

Learners define eligibility, exclusions, suppressions, hook, context, trigger, input codes, units, value sets, availability time, staleness limits, missing and inconsistent states, threshold candidates, card content, nonaction, override, audit trace, and prohibited behavior.

SQL owns cohort and event-time input logic. Python independently checks the logic table, truth table, unit handling, time ordering, unavailable states, and trace completeness. The module includes normal, boundary, stale, missing, inconsistent, delayed, duplicate, and suppressed cases before any model performance is considered.

The 20-point component cannot pass with a clinically incoherent intended use, an unavailable input, a hidden default, an untraceable rule, a threshold chosen by the agent, or an automatic action.

The accepted package preserves the 29 immutable Module 01 files, adds a complete 1,000-adult Synthea FHIR R4 release with 25 files and 811,803 resource rows, and measures 11,109 repeated provider and organization IDs without silently removing them. Sixteen linked Commons cases cover normal, boundary, missing, stale, inconsistent, duplicate, delayed, terminology, version, suppression, unit, context, silent-failure, and missing-score conditions. The learner and reference workspaces each contain 86 files with a 73-row immutable manifest and 12 assessed records. All reference traces pass, while model fitting inside Module 02 and clinical-threshold acceptance remain prohibited.

## 11. Module 03 brief: Evidence, calibration, and validation

- Module ID: `oclc-app4-03`.
- Hours: 16.5.
- Package path: `courses/clinical-decision-support/modules/03-evidence-calibration-validation/`.
- Specification: `docs/curriculum/courses/APP-4/modules/03-evidence-calibration-validation-spec.md`.
- Decision: does the historical evidence justify continuing to workflow and sandbox evaluation under stated limits?
- Submission: 20-point evidence, calibration, and threshold audit and the 40-point Week 3 release.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.79.0`; Checkpoint 01 assembly is permitted with conditions.

Learners build the NHANES evidence cohort with a fixed information cutoff, preserve survey-cycle identity, fit the transparent model on the declared development evidence, and evaluate the temporal holdout without tuning it. They report the target definition, prevalence, missingness, support, discrimination, calibration-in-the-large, calibration slope, calibration by score range, confusion measures at every candidate threshold, alert count, and missed eligible cases.

The later-cycle release is a transport stress test. Learners state what changed in data availability, support, prevalence, calibration, and burden without assigning an unsupported cause. Subgroup review begins with denominators, outcome counts, missingness, support, and uncertainty.

Decision-curve or net-benefit output is interpreted only for the declared threshold range and consequence assumptions. It does not prove patient benefit. Checkpoint 01 freezes Modules 01 through 03 before workflow scoring begins.

The accepted package verifies all 16 inherited NHANES sources before parsing and releases 14,892 age-eligible audit rows, 7,544 model rows, and 328 observed HbA1c outcomes. One fixed survey-weighted binomial GLM is fit on 3,652 development rows, then evaluated without tuning on a 1,806-row temporal holdout and a separate 2,086-row 2021-2023 transport stress test using `WTPH2YR`. The 17-file evidence release includes weighted performance, calibration, six candidate-threshold audits, decision-curve quantities, subgroup support and suppression, transport comparison, 500-replicate teaching intervals, and 20 passing invariants. No threshold is selected or accepted, and the Module 02 `0.20` value is rejected as evidence.

## 12. Module 04 brief: Alert burden, human factors, and equity

- Module ID: `oclc-app4-04`.
- Hours: 16.5.
- Package path: `courses/clinical-decision-support/modules/04-alert-burden-human-factors-equity/`.
- Specification: `docs/curriculum/courses/APP-4/modules/04-alert-burden-human-factors-equity-spec.md`.
- Decision: is one candidate design supportable enough to prototype without unacceptable burden or exclusion?
- Submission: 25-point workflow, alert-burden, human-factors, and equity review.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.81.0`; Module 05 sandbox construction is permitted with conditions.

Learners test the card against a task analysis, workflow map, timing window, role and handoff map, alert budget, interruption level, competing alerts, expected action, dismissal and deferment, patient communication, access needs, privacy, and override. They compare at least one less interruptive alternative and no alert.

Burden is reported as eligible encounters, cards, cards per clinician session, repeated cards, unavailable inputs, response time, views, dismissals, deferments, and unresolved cases. A dismissal is not automatically misuse, fatigue, or poor care.

The equity review asks who is excluded by missing measurements, coded diagnoses, language, disability, access, and workflow design. It separates unsupported subgroup estimates from observed differences and keeps patients out of automated targeting.

The accepted release freezes the complete 263-file Week 3 reference checkpoint and verifies all 204 nested immutable rows. Its deterministic workflow layer contains 1,000 synthetic people, 1,200 encounter opportunities, 200 repeats, 120 sessions, 12 fictional clinicians, 288 candidate-frame encounters, 39 unavailable inputs, 7,200 candidate-event rows, and 108 access and equity slices. The six evidence candidates produce 116, 12, 3, 3, 0, and 0 synthetic cards.

The release compares six interruptive banners, six passive contextual panels, and no alert. Its 302-file learner or reference workspace contains 285 immutable rows and 16 assessed records. The 25-point reference passes all 20 gates, 2,400 reference checks, 2,284 learner checks, copied validation, and 20 deliberate failure routes. The human reference advances `panel-t003` for Module 05 mechanics only. The `0.03` value remains unaccepted, and every clinical-use, implementation, and deployment route remains prohibited.

## 13. Module 05 brief: Sandbox prototype and failure modes

- Module ID: `oclc-app4-05`.
- Hours: 16.0.
- Package path: `courses/clinical-decision-support/modules/05-sandbox-prototype-failure-modes/`.
- Specification: `docs/curriculum/courses/APP-4/modules/05-sandbox-prototype-failure-modes-spec.md`.
- Decision: does the nonproduction prototype behave as specified and fail visibly enough to enter a safety case?
- Submission: sandbox prototype and failure-mode checkpoint.
- Point role: required zero-point gate for Checkpoint 02.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.82.0`; Module 06 curriculum construction is permitted with conditions.

Learners implement the accepted logic in a local, nonnetworked FHIR R4 and CDS Hooks teaching sandbox. Every request, prefetch item, rule branch, prediction version, threshold, suppression, response, and no-response state is traceable.

The test matrix includes normal, boundary, missing, stale, inconsistent, duplicate, delayed, unavailable-service, terminology mismatch, version mismatch, and silent-failure cases. Learners distinguish a visible failure from a request that disappeared without a response, log, or human notice.

The prototype cannot connect to a real EHR, process real patient data, send a clinical message, or claim conformance. Passing sandbox tests is evidence about the teaching implementation only.

The accepted release freezes all 302 files in the Module 04 reference workspace, including its 285-row immutable manifest and 204 nested Week 3 rows. The local standard-library sandbox contains 31 cases, 184 FHIR R4-shaped prefetch resources, 31 response envelopes, and 61 trace events. It reproduces all 12 Module 04 positive fixtures, including one repeat, and adds declared normal-negative, exact-boundary, visible-failure, silent-failure, and accessibility-defect tests.

All 31 declared tests pass and all 20 release invariants pass. The four-ledger visibility audit detects one seeded silent failure, and the accessibility audit blocks one malformed card. The 341-file learner or reference workspace contains 324 immutable rows and 16 assessed records. The reference passes 2,649 checks, the learner starter passes 2,558 checks, copied validation passes, and 20 deliberate failure routes are rejected. Module 05 adds no points, carries the accepted 25 Module 04 points once, and permits Module 06 curriculum construction without permitting silent-mode evaluation, implementation, production connection, or deployment.

## 14. Module 06 brief: Safety case, monitoring, governance, and embedded machine learning

- Module ID: `oclc-app4-06`.
- Hours: 16.0.
- Safety, monitoring, and governance block: 8.0 hours.
- Embedded ML extension: 8.0 hours.
- Package path: `courses/clinical-decision-support/modules/06-safety-monitoring-governance-embedded-ml/`.
- Specification: `docs/curriculum/courses/APP-4/modules/06-safety-monitoring-governance-embedded-ml-spec.md`.
- Decision: is the safety and monitoring case ready for clinician leadership review, and does a fixed ML challenger change the recommendation?
- Submission: cumulative Week 6 release.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.83.0`; Checkpoint 02 curriculum assembly is permitted with conditions.

The safety block maps hazards to causes, controls, detection, owners, escalation, fallback, stop, restart, and retirement. Monitoring covers eligibility, input availability, firing, suppression, burden, response, latency, errors, silent failure, outcome availability, calibration, drift, subgroup support, version, incidents, and overrides. Every measure has a cadence, owner, threshold origin, unavailable state, and human action.

The ML extension compares the accepted transparent logistic model with one fixed gradient-boosted classification challenger. Both models use the same predictors, target, cutoffs, development cycles, temporal holdout, later-cycle stress test, missing-input rules, threshold candidates, alert budget, and evaluation rows. There is no tuning after holdout inspection.

The challenger replaces the transparent model only if every predeclared calibration, discrimination, burden, missed-case, subgroup-support, drift, reproducibility, leakage, and interpretability rule passes. Better average discrimination is insufficient. ML cannot change intended use, set the threshold, excuse a workflow defect, or automate action.

The Week 6 package carries the 25 Module 04 course points once. Modules 05 and 06 add required gates but no points.

The runnable release freezes the complete 341-file Module 05 workspace inside a 387-file learner or reference workspace with 369 immutable rows and 17 assessed records. Its final manifest is 88,971 bytes with SHA-256 `e6553079256fdd2a37ab042a87c2ec69812cad7074abefa7d7907e6ee7b56f7d`. It preserves all 31 sandbox cases, 17 inherited failures, the seeded silent failure, the blocked accessibility defect, `panel-t003`, the unaccepted `0.03000000` fixture, the 25-point score carryforward, and all 20 Module 05 gates.

The safety evidence contains 22 hazards, 20 monitoring measures, eight seeded monitoring scenarios, and 12 human escalation routes. Every measure has a cadence, owner, threshold origin, unavailable state, and human action. Every hazard has detection, control, escalation, fallback, stop, restart, and retirement. No automatic action is permitted.

The fixed gradient-boosted challenger uses the same 7,544 rows, target, three predictors, analytic weights, development cycles, temporal holdout, transport stress set, missing-input rule, and six unaccepted thresholds as the transparent model. It passes 8 of 11 replacement rules. It fails temporal-holdout discrimination by `-0.00743486`, transport discrimination by `-0.01928938`, and the supported subgroup rule with maximum degradation `0.10385240`. The transparent model remains accepted for the teaching comparison.

All 22 Module 06 gates pass. Reference validation passes 1,230 checks, learner validation passes 1,152 checks, copied validation passes, and 22 deliberate failure routes are rejected. Progression is `continue with conditions` to cumulative Week 6 curriculum assembly. No threshold, silent-mode, clinical, implementation, production, or deployment authority is added.

## 15. Module 07 brief: Clinician leadership, product brief, and defense

- Module ID: `oclc-app4-07`.
- Hours: 16.0.
- Clinician of record: Joe Joseph, MD, SFHM. Dated public identity is confirmed; participation and final wording require direct confirmation before alpha.
- Package path: `courses/clinical-decision-support/modules/07-clinician-leadership-product-defense/`.
- Specification: `docs/curriculum/courses/APP-4/modules/07-clinician-leadership-product-defense-spec.md`.
- Decision: whether to recommend seeking local approval for a bounded silent-mode evaluation, revise the concept or evidence, refer the question, or stop.
- Submission: final CDS product brief, prototype, evaluation proposal, safety case, and defense.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.85.0`; final-checkpoint curriculum assembly is permitted with conditions.

Module 07 freezes the accepted Week 3 and Week 6 evidence before adding leadership records. Learners cannot change the cohort, model, threshold, alert budget, workflow score, prototype result, failed test, or ML decision inside the leadership package.

The final package includes an intended-use brief, workflow and patient-consequence brief, evidence synthesis, logic and input specification, prototype disclosure, safety case, monitoring plan, silent-failure plan, evaluation proposal, model and rule stewardship, governance and retirement record, accountable owners, disagreement record, accessible communication, reproducibility audit, responsible-claims audit, AI-use record, and defense.

Leadership must address uncertainty, alert burden, patient access, staff voice, clinical override, hidden work, failure detection, who can stop the concept, what evidence would permit reconsideration, and what remains outside course authority.

## 16. Three cumulative checkpoint contracts

### Checkpoint 1: Logic, evidence, calibration, and validation readiness

- Timing: end of instructional Week 3.
- Course points: 40.
- Package path: `courses/clinical-decision-support/checkpoints/01-logic-evidence-validation-readiness/`.
- Specification: `docs/curriculum/courses/APP-4/checkpoints/01-logic-evidence-validation-readiness-spec.md`.
- Decision: may the accepted use case, logic, public evidence, calibration, threshold, and claim limits enter workflow and prototype work?
- Build status: runnable release candidate at Checkpoint version `0.1.0` and Commons release `0.80.0`; bounded Module 04 curriculum construction is permitted with conditions.

Required evidence includes the Module 01 charter and source audit; exact identities for all 16 NHANES files; source limitations; fictional-service declaration; intended use; user and workflow moment; action and prohibited action; logic, trigger, suppression, input, unit, time, terminology, and unavailable-state contracts; truth table and edge cases; cohort and information cutoff; survey-design decision; transparent model; temporal holdout; later-cycle stress test; calibration; threshold table; alert budget; net-benefit interpretation; subgroup support; 40-point score; gates; AI record; defense; and progression decision.

The checkpoint counts the 20-point Module 02 and 20-point Module 03 components once. Module 01 adds no points but is a required gate.

The accepted checkpoint freezes 245 files from the complete Module 01 through Module 03 reference workspaces, including 204 nested immutable rows. Its candidate manifest is 45,897 bytes with SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`. The 263-file learner or reference workspace preserves a 40-point total, 36 inherited gates, 20 checkpoint gates, nine assessed records, and a 14-question defense. Reference validation passes 1,284 checks, learner validation passes 1,245 checks, and all 20 failure routes are rejected. No threshold is accepted. Module 04 may compare all six evidence candidates, a less interruptive alternative, and no alert for curriculum construction only.

### Checkpoint 2: Workflow, sandbox, safety, and monitoring release

- Timing: end of instructional Week 6.
- Course points: 25.
- Package path: `courses/clinical-decision-support/checkpoints/02-workflow-sandbox-safety-release/`.
- Specification: `docs/curriculum/courses/APP-4/checkpoints/02-workflow-sandbox-safety-release-spec.md`.
- Decision: is the complete nonproduction case strong enough for clinician leadership review?
- Build status: runnable release candidate at Checkpoint version `0.1.0` and Commons release `0.84.0`; Module 07 clinician leadership review is permitted with conditions.

Required evidence includes the accepted Week 3 identity; workflow and task analysis; role and handoff map; alert burden; alternatives; usability review; automation-bias controls; access, equity, privacy, and patient consequences; FHIR and CDS Hooks message shapes; traceable prototype; normal and edge tests; visible and silent failures; latency and version tests; hazard log; safety controls; monitoring measures; drift and subgroup checks; incident route; escalation, stop, fallback, restart, and retirement rules; governance; transparent-versus-ML comparison; leakage tests; 25-point score; gates; AI record; defense; and progression decision.

The checkpoint counts the 25-point Module 04 component once. Modules 05 and 06 supply required prototype, failure, safety, monitoring, governance, and ML gates without adding points.

The accepted checkpoint freezes 1,030 files from the complete Module 04 through Module 06 reference workspaces. Its candidate manifest is 236,732 bytes with SHA-256 `14ac12dd890045dce21cdc44a9b614770b8b2428bd71a1d4f5eb9cc9de63d642`. The 1,047-file learner or reference package preserves a 25-point total, 62 inherited gates, 20 checkpoint gates, nine assessed records, and a 14-question defense. Reference validation passes 8,353 checks, learner validation passes 8,308 checks, and all 24 failure routes are rejected. `panel-t003` and `0.03000000` remain mechanics fixtures, no threshold is accepted, the sandbox failures and accessibility blocker remain visible, and the transparent model remains retained.

### Final checkpoint: Clinical decision support package

- Timing: official last day of the assigned half-term.
- Course points: 35.
- Package path: `courses/clinical-decision-support/checkpoints/03-clinical-decision-support-package/`.
- Specification: `docs/curriculum/courses/APP-4/checkpoints/03-clinical-decision-support-package-spec.md`.
- Decision: should the fictional governance council recommend seeking local approval for a bounded silent-mode evaluation, revise, refer, or stop?
- Build status: specified; runnable package pending.

Required evidence includes both accepted checkpoints; immutable candidate manifest; final reproducible repository; intended-use and product brief; evidence synthesis; logic and input contract; threshold and alert budget; workflow and patient-consequence brief; prototype disclosure; safety case; monitoring and silent-failure plan; evaluation proposal; model, rule, terminology, data, and interface stewardship; escalation, stop, fallback, restart, and retirement rules; accountability and disagreement records; accessible exact evidence; technical appendix; AI and claims audit; 35-point score; gates; defense; reviewer record; reproduction; conditions; and separate package and evaluation recommendations.

The final checkpoint adds 35 points once, giving a course total of `40 + 25 + 35 = 100` with no duplication.

## 17. Assessment map and grading rules

| Source assessment | Feedback milestone | Cumulative checkpoint | Course points |
|---|---|---|---:|
| Use-case and logic specification | End of Week 2 | Week 3 | 20 |
| Evidence, calibration, and threshold audit | End of Week 3 | Week 3 | 20 |
| Workflow, alert-burden, and equity review | End of Week 4 | Week 6 | 25 |
| Final CDS product brief, prototype, evaluation, and safety case | End of Week 7 | Official half-term end date | 35 |
| Total |  |  | 100 |

Every component uses five recurring criteria: correct, reproducible, sound clinical decision support reasoning, clear and usable, and responsible agent use.

A numeric threshold cannot compensate for a wrong source, patient or encounter definition, information cutoff, input time, unit, terminology, survey weight, calibration calculation, target, threshold consequence, workflow moment, alert count, hidden failure, inaccessible output, unsupported claim, or missing human owner.

## 18. Software, reproducibility, and data policy

SQL owns cohort, event-time eligibility, input availability, trigger, suppression, and monitoring-denominator logic. Python owns source checks, joins, models, calibration, threshold tables, decision analysis, subgroup support, synthetic workflow generation, prototype logic, ML, accessible exports, and validation. R output is read and interpreted when a supported runtime is available. Git records reviewed versions and immutable handoffs.

Every public source is pinned by landing page, resource URL, cycle or release, retrieval date, bytes, hash, rows, fields, codebook, rights, grain, reporting period, and completeness. A build must inspect the complete accepted release before deriving teaching evidence. Binary XPT and generated FHIR files may stay outside Git when needed, but their identities, acquisition commands, profiles, deterministic selections, and hashes must remain in the release.

Synthetic data require an upstream generator, Commons generator, versions, configuration, seed, known-truth contract, relationship and shape tests, explicit flags, counts, bytes, hashes, and defect registry. The raw synthetic layer remains immutable. Repairs occur in a derived layer through tested code.

Every module must provide a complete reference, incomplete learner template, instructor material, assessment, rubric, source and data specification, release record, semantic version, deterministic builder, validator, failure self-check, and protected handoff.

## 19. Accessibility, equity, privacy, and responsible claims

Every calibration, threshold, burden, drift, subgroup, and monitoring display has an exact table and structured text alternative. Interface state does not rely on color alone. Card purpose, intended action, uncertainty, source, time, owner, and unavailable state remain available to assistive technology.

Every subgroup review begins with eligibility, denominator, outcome count, missingness, support, uncertainty, survey design, and suppression. Learners may identify a supported concern. They may not treat a modeled or synthetic difference as a trait of a real group, lower a safety standard for one group, or target patients for nonclinical action.

No protected or identifiable patient, clinician, employee, workplace, or restricted data enter the repository or an external agent. Synthetic workflow data are not real clinical or workforce surveillance. The prototype collects no credentials and connects to no clinical system.

NHANES does not prove local validity. Calibration in a historical survey does not prove clinical utility. A threshold does not define the right action by itself. A dismissal does not prove alert fatigue. A passing sandbox test does not prove interoperability or safety. A silent-mode proposal is not permission to score real patients. Package acceptance does not authorize deployment.

## 20. Agent policy and accountability

Agents may help draft code, test cases, documentation, message examples, accessibility text, and alternative interpretations. Learners must disclose the tool, task, prompt or instruction, output used, verification, revision, and accountable human.

An agent may not choose the intended use, clinical action, eligibility, exclusion, threshold, alert budget, suppression, safety control, monitoring trigger, subgroup claim, escalation, stop rule, restart rule, retirement decision, or final recommendation. It may not receive protected data, fabricate a FHIR or CDS Hooks claim, hide a failed test, or rewrite an unavailable result as zero.

Every agent-produced analytic artifact requires an independent deterministic check against the accepted source or known truth. The learner owns the submission. Faculty, clinical reviewers, and the fictional governance council own review decisions. No agent receives clinical or deployment authority.

## 21. Instruction, feedback, and clinician leadership

The course uses short demonstrations, guided public-data and sandbox laboratories, case conferences, critique, structured peer review, threshold and burden conferences, failure drills, and defense rehearsals. Feedback milestones at Weeks 2 and 4 prepare the cumulative checkpoints without adding points.

Joe Joseph, MD, SFHM, is the designated clinician for Module 07 under the dated public identity boundary already recorded in the Commons. The course makes no current-employer or current-title claim. Participation, schedule, format, recording permission, and final biography wording require direct confirmation.

The clinician-led block focuses on decision ownership, workflow consequences, patient and staff trust, uncertainty, competing priorities, failure response, communication, disagreement, stop authority, and the difference between an analytic package and permission to use a tool clinically.

If the named clinician cannot participate live, an approved recorded case conference plus a qualified clinician-led synchronous defense must preserve the same learning outcomes. The substitution and qualifications require program approval before alpha.

## 22. Reviewer roles and release gates

### Required reviewer coverage before alpha

- APP-4 faculty owner;
- Joe Joseph, MD, SFHM, as clinician of record;
- primary care or endocrinology clinical-content reviewer;
- clinical informatics reviewer;
- FHIR and CDS Hooks interoperability reviewer;
- biostatistics and calibration reviewer;
- NHANES and complex-survey methods reviewer;
- human-factors and usability reviewer;
- patient-safety reviewer;
- nursing or clinical-workflow reviewer;
- patient, access, language, disability, and equity reviewer coverage;
- privacy, data-governance, and security reviewer;
- responsible-AI and model reviewer;
- accessibility and communication reviewer; and
- independent reproducer.

One person may cover more than one role only when the record states the qualifications and conflicts. Missing clinical, safety, patient, survey-methods, interoperability, privacy, accessibility, or independent-reproduction coverage blocks alpha.

### Course release gates

1. The exact source DOCX identity and source normalization remain unchanged.
2. Seven modules total 112.5 hours and three checkpoints total 100 points.
3. All 16 complete NHANES files are acquired, fingerprinted, profiled, and joined only through tested cycle-specific logic.
4. Survey design, weights, codebooks, cycle differences, missingness, and support are explicit.
5. The fictional service and every synthetic resource are unmistakably synthetic.
6. Intended use, user, workflow moment, action, nonaction, prohibited action, and owner are explicit.
7. Logic, input, unit, terminology, availability, staleness, suppression, and trace contracts pass.
8. Calibration, thresholds, burden, missed cases, temporal validation, transport, and subgroup support are reproducible.
9. Workflow, patient consequence, usability, access, equity, privacy, override, and alert burden are reviewed.
10. The sandbox is local and nonproduction and passes normal, edge, stale, missing, inconsistent, delayed, version, and silent-failure tests.
11. Safety controls, monitoring, incident routes, escalation, stop, fallback, restart, governance, and retirement have named human owners.
12. The fixed ML challenger uses the same eligible evidence and cannot replace the transparent model unless every predeclared rule passes.
13. Every display has an exact accessible alternative and every unavailable state remains unavailable.
14. Reference and learner packages differ in assessed work, not in immutable evidence.
15. Deterministic builders, validators, mutation checks, and independent reproduction pass.
16. No artifact authorizes patient-level action, live scoring, clinical use, implementation, production connection, or deployment.

## 23. Durable paths and build order

Course artifacts:

- source record: `docs/source/app-4-clinical-decision-support-source-record.md`;
- course specification: `docs/curriculum/courses/APP-4/course-spec.md`;
- course package: `courses/clinical-decision-support/`;
- course package index: `courses/clinical-decision-support/README.md`.

Module specification paths:

1. `docs/curriculum/courses/APP-4/modules/01-cds-use-case-decision-spec.md`
2. `docs/curriculum/courses/APP-4/modules/02-logic-triggers-data-spec.md`
3. `docs/curriculum/courses/APP-4/modules/03-evidence-calibration-validation-spec.md`
4. `docs/curriculum/courses/APP-4/modules/04-alert-burden-human-factors-equity-spec.md`
5. `docs/curriculum/courses/APP-4/modules/05-sandbox-prototype-failure-modes-spec.md`
6. `docs/curriculum/courses/APP-4/modules/06-safety-monitoring-governance-embedded-ml-spec.md`
7. `docs/curriculum/courses/APP-4/modules/07-clinician-leadership-product-defense-spec.md`

Checkpoint specification paths:

1. `docs/curriculum/courses/APP-4/checkpoints/01-logic-evidence-validation-readiness-spec.md`
2. `docs/curriculum/courses/APP-4/checkpoints/02-workflow-sandbox-safety-release-spec.md`
3. `docs/curriculum/courses/APP-4/checkpoints/03-clinical-decision-support-package-spec.md`

Each unit is built, validated, versioned, committed, pushed, and remote-verified before the next unit begins. Module 01 pins all public and synthetic source identities. Modules 02 and 03 build Checkpoint 01. Modules 04 through 06 build Checkpoint 02. Module 07 freezes both checkpoints before the final package.

## 24. Known issues and construction acceptance

Human decisions and evidence still required before alpha:

- assign the official APP-4 section and half-term dates before publishing due dates;
- acquire, fingerprint, profile, and independently review all 16 complete NHANES XPT files;
- confirm the final clinical target, predictor list, exclusions, units, threshold candidates, and confirmatory-action wording with qualified clinical reviewers;
- confirm the complex-survey design and weight treatment for development, temporal holdout, later-cycle stress, and any pooled estimates;
- build and review the Synthea and Commons synthetic release, known truth, subgroup support, drift, burden, and silent-failure design;
- review the FHIR R4 and CDS Hooks teaching shapes, terminology, value sets, version behavior, and conformance disclaimers;
- independently review the transparent model, calibration, decision analysis, fixed ML contract, and no-retuning rule;
- confirm Joe Joseph's participation, schedule, format, recording permission, and final biography wording;
- name the faculty, clinical, informatics, interoperability, survey-methods, calibration, human-factors, safety, workflow, patient, equity, access, privacy, security, accessibility, responsible-AI, and independent-reproduction reviewers; and
- complete clean human reproduction and final release authorization.

Construction acceptance for this course-level unit:

- [x] The exact DOCX source is fingerprinted in both archives.
- [x] Seven distinct modules total 112.5 hours.
- [x] The source assessment weights are preserved as 40, 25, and 35 checkpoint points.
- [x] Modules 01 through 03 form the applied technical block.
- [x] Modules 04 through 06 form the workflow, prototype, and safety block.
- [x] Module 06 contains an eight-hour embedded ML extension.
- [x] Module 07 is clinician led.
- [x] The continuing decision uses an explicitly fictional service and nonproduction advisory.
- [x] Sixteen complete public NHANES source routes have declared roles and boundaries.
- [x] Synthetic FHIR R4 and CDS Hooks data have a required resource, truth, provenance, and validation contract.
- [x] Every checkpoint has a decision, points, evidence, and protected handoff.
- [x] APP-4 remains distinct from FND-1, FND-2, DA-730, and APP-1 through APP-3.
- [x] Clinical use, live scoring, automatic action, implementation, and deployment remain outside course authority.
- [x] Module 01 pins all 16 complete public XPT files, profiles 145,563 component rows and 442 fields, releases a validated 41-file decision-framing workspace, and permits Module 02 construction with conditions without fitting a model or selecting a threshold.
- [x] Module 02 releases a complete 811,803-row synthetic FHIR source, 16 deterministic rule cases, and an 86-file workspace while keeping its mock score and threshold mechanics only.
- [x] Module 03 releases a reproducible 7,544-row historical model cohort, untouched temporal-holdout and transport evidence, six unaccepted candidate thresholds, and a validated 118-file workspace.
- [x] Checkpoint 01 freezes all 245 accepted Module 01 through Module 03 files, counts 20 plus 20 points once, preserves all six thresholds as unaccepted, and releases a validated 263-file cumulative workspace.
- [x] Module 04 freezes the complete Week 3 release, compares all six unaccepted candidates with interruptive, passive, and no-alert designs, scores the 25-point workflow component once, and releases a validated 302-file workspace with a protected Module 05 sandbox handoff.
- [x] Module 05 freezes all 302 Module 04 files, releases 31 local FHIR R4 and CDS Hooks-shaped normal and failure cases in a validated 341-file workspace, detects seeded silent failure from independent ledgers, blocks a malformed card, and protects the zero-point Module 06 handoff.
- [x] Module 06 freezes all 341 Module 05 files, builds a complete safety and monitoring case, evaluates one fixed challenger on the same 7,544 rows, retains the transparent model after three replacement-rule failures, and protects the zero-point Week 6 handoff.
- [x] Checkpoint 02 freezes all 1,030 Module 04 through Module 06 files, counts the 25-point Module 04 score once, preserves all 82 inherited and checkpoint gates, and releases a validated 1,047-file cumulative workspace.
- [x] Module 07 freezes both accepted checkpoints in a validated 1,347-file leadership candidate, adds the 35-point final component, passes 26 gates, and separates curriculum acceptance from the recommendation to revise before seeking local silent-mode approval.

APP-4 Modules 01 through 07 and Checkpoints 01 and 02 are complete for curriculum construction. Resume with the final checkpoint by freezing the exact 1,347-file Module 07 release, counting its 35-point component once, preserving all 26 gates and 16 open conditions, and retaining the separate `accept with conditions` package status and `revise before seeking local silent-mode approval` CDS recommendation.

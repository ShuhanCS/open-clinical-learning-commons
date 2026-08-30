# APP-2: Data for Patient Experience and Engagement

## 1. Course identity and catalog role

- Course ID: APP-2.
- Title: Data for Patient Experience and Engagement.
- Credits: 3.
- Delivery: online half-term.
- Planning rhythm: seven instructional weeks plus the official half-term end date.
- Total learner work: 112.5 hours.
- Prerequisites: accepted FND-1 and FND-2 technical releases.
- Primary graded tools: SQL and Python.
- R role: read, run, and interpret survey, weighting, reliability, and psychometric code; writing R from scratch is not graded.
- Final deliverable: patient-experience and engagement package with reproducible evidence and a defense.
- Course version target: 0.1.0.
- Current Commons release: 0.59.0 through runnable Module 04 and Checkpoint 01.
- Specification status: construction candidate.

APP-2 teaches learners to treat patient experience, engagement, and patient-reported outcomes as measured evidence. Learners must ask what a measure captures, who had a chance to respond, who is missing, how collection mode affects the result, and what action the evidence can support.

The academic calendar controls each due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase is a planning model. Week 3 and Week 6 are instructional checkpoints. The final package is due on the published last day of the assigned half-term.

The published calendar confirms that this is a close planning shorthand rather than one exact duration:

| Half-term | Published dates | Inclusive calendar days | Approximate weeks |
|---|---|---:|---:|
| Fall 2026 half-term 1 | September 8 through October 27 | 50 | 7.14 |
| Fall 2026 half-term 2 | October 28 through December 18 | 52 | 7.43 |
| Spring 2027 half-term 1 | January 11 through March 2 | 51 | 7.29 |
| Spring 2027 half-term 2 | March 3 through April 24 | 53 | 7.57 |
| Summer 2027 half-term 1 | May 10 through June 29 | 51 | 7.29 |
| Summer 2027 half-term 2 | June 30 through August 20 | 52 | 7.43 |

## 2. Source authority and normalization

The source course is `06-APP-2-Patient-Experience-and-Engagement.docx`, 25,906 bytes, SHA-256 `3feff30f5128587a482a3f4ca42979a46059bbe98e3febc98f4556c4cfafc009`. Byte-identical copies appear in both supplied curriculum archives.

The source record is `docs/source/app-2-patient-experience-engagement-source-record.md`.

The source defines seven modules totaling 112.5 hours and assessments weighted 20, 25, 20, and 35 percent. The Commons preserves every point once:

- Week 3: 20 points;
- Week 6: 45 points; and
- official half-term end date: 35 points.

The Week 3 package contains the decision charter, patient-measurement lab, and representation evidence. The Week 6 package adds the response and linked-evidence analysis, patient-voice memo, partnered-improvement work, and embedded ML gates. The final package adds leadership, patient-facing reporting, monitoring, accountability, and defense without rescoring earlier evidence.

## 3. Place in the program and prerequisite handoffs

### FND-1 handoff

Learners arrive able to maintain a reproducible repository, retrieve and join public data, define denominators, profile missingness, produce descriptive evidence, create accessible displays, record provenance, and verify agent-assisted work.

APP-2 does not reteach generic SQL, data cleaning, project setup, or chart construction. It applies those skills to survey instruments, response frames, patient-reported evidence, comments, access, and engagement.

### FND-2 handoff

Learners arrive able to define an analytic aim, choose a transparent model, distinguish prediction from association and causation, assess assumptions and subgroup support, evaluate a fixed test set, and document model use and limits.

APP-2 extends those skills through scale scoring, meaningful-change reasoning, survey weighting, response propensity, mode effects, missingness, and bounded qualitative synthesis.

### Downstream handoff

- APP-3 may rely on a patient-centered outcome or balancing measure.
- APP-4 may rely on burden, trust, usability, and patient-consequence evidence.
- APP-5 may rely on evidence about channel exclusion, representation, language, and access.
- CAP-1 may rely on patient partnership, measured patient voice, and an accountable feedback plan.

## 4. Course decision and named audiences

The continuing teaching decision is:

> Should an adult inpatient service and its patient/caregiver advisory group design and prospectively evaluate a multilingual discharge-communication feedback process that helps patients understand the help and warning signs needed for recovery at home?

The public CMS source establishes how hospital-level patient experience is measured and reported. It does not provide local patient-level responses, local subgroup experience, causal effects, or evidence that one workflow change will help. The course therefore builds from measure definition to a bounded prospective evaluation proposal.

### Primary decision owner

The primary owner is an adult inpatient patient-experience council that shares interpretation and design authority with a patient/caregiver advisory group.

### Required audiences

| Audience | What they need |
|---|---|
| Patient and caregiver partners | construct relevance, burden, language access, interpretation, disagreements, feedback, and decision rights |
| Clinical decision owner | target population, patient-reported evidence, feasibility, safety, and a bounded next action |
| Care team | communication steps, workflow, access, burden, measures, and escalation |
| Survey and analytics team | instrument, scoring, frame, response, missingness, weights, linkage, uncertainty, and reproduction |
| Access and digital team | channel availability, portal assumptions, navigation, exclusion risk, and alternatives |
| Governance reviewer | permitted use, privacy, comments, agent use, claims, conditions, and stop rules |

## 5. Course learning outcomes

By the end of APP-2, learners can:

| ID | Assessable course outcome | Program connection |
|---|---|---|
| CLO-1 | Define a patient-experience or engagement decision with a target population, patient partners, evidence needs, accountable owner, and feasible action. | PLO-1, PLO-5 |
| CLO-2 | Select, score, and interpret patient-reported outcome and experience measures, including reliability, validity, direction, burden, accessibility, and meaningful change. | PLO-1, PLO-2 |
| CLO-3 | Assess sampling, coverage, response rates, item missingness, nonresponse, mode effects, weighting, and representation before comparing results. | PLO-2, PLO-3 |
| CLO-4 | Link patient-reported, access, communication, engagement, and service-use evidence with aligned denominators and complete provenance. | PLO-1, PLO-4 |
| CLO-5 | Compare groups and channels, analyze comments within qualitative limits, and report equity concerns without blaming patients or overstating frequencies. | PLO-3, PLO-6 |
| CLO-6 | Compare a transparent response-adjustment approach with a bounded ML extension and state whether the extension changes the decision. | PLO-2, PLO-3, PLO-6 |
| CLO-7 | Produce and defend a patient-informed improvement package with implementation measures, feedback, accountability, monitoring, and stop rules. | PLO-4, PLO-5, PLO-6 |

## 6. Concept ownership and boundaries

### APP-2 owns

- patient experience, engagement, partnership, PREM, and PROM distinctions;
- construct definition and fit-for-purpose instrument selection;
- scale direction, scoring, reliability, validity, meaningful change, burden, language, and accessibility;
- target population, sampling frame, coverage, response rate, item missingness, nonresponse, mode effects, and weighting;
- patient-level and event-level linkage with denominator alignment;
- access, communication, navigation, portal, engagement, and service-use evidence;
- transparent comment coding and bounded assisted classification;
- subgroup interpretation, uncertainty, representation, equity, and non-stigmatizing reporting;
- patient-partner interpretation, disagreement, co-design, feedback, and accountability;
- a transparent response-adjustment benchmark versus a bounded ML extension; and
- clinician leadership, patient-facing reporting, monitoring, and defense.

### APP-2 extends rather than repeats

- FND-1 data work gains survey frames, scoring rules, response states, linkage governance, and patient-partner records.
- FND-2 modeling gains response propensity, weight diagnostics, mode effects, known-selection simulation, and decision-level ML comparison.
- DA-730 skills are used for accessible patient-facing evidence. General chart theory is not repeated.

### Out of scope

- protected, identifiable, workplace, or restricted patient data;
- using public HCAHPS data to rank hospitals, clinicians, demographic groups, or communities;
- treating a PREM as a clinical outcome, satisfaction score, or individual diagnosis;
- treating comments as a prevalence estimate;
- modifying a validated instrument without permission and validation;
- claiming that weighting removes all nonresponse bias;
- using ML to replace patient partnership, transparent weighting, or human comment review;
- clinical implementation, automated patient targeting, or efficacy claims; and
- synthetic comments presented as real patient testimony.

## 7. Continuing source and analytic thread

### CMS HCAHPS public source

APP-2 begins with the complete CMS Patient survey (HCAHPS) - Hospital file:

https://data.cms.gov/provider-data/dataset/dgck-syfz

| Item | Accepted fact |
|---|---|
| Publisher | Centers for Medicare & Medicaid Services |
| Accepted raw bytes | 105,461,119 |
| Raw SHA-256 | `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc` |
| Deterministic gzip bytes | 2,195,547 |
| Gzip SHA-256 | `56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c` |
| Rows | 325,720 |
| Facilities | 4,790 |
| Measure IDs | 68 |
| State or territory codes | 56 |
| Reporting period | 2024-10-01 through 2025-09-30 |
| Patient-level records | no |

The full file is retained as a compressed immutable source. A small profile and measure inventory are derived from the entire file. No convenience sample replaces it.

### AHRQ MEPS public-use layer

Later modules use MEPS HC-256 and selected 2024 event files:

https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256

The full-year file supplies public person-level survey weights, patient satisfaction, health status, access, quality, utilization, and expenditure fields. HC-254D through HC-254G supply inpatient, emergency, outpatient, and office-based events and link through `DUPERSID`. Each module must pin exact archives, terms, codebooks, rows, fields, and hashes before use.

### Documented synthetic layers

The course may add:

1. a synthetic comment corpus with no real patient text; and
2. a known response-selection mechanism applied to a public-use analytic population.

Both require a generator, seed, data dictionary, source-field map, known truth, validation, and explicit synthetic flags. They may teach method behavior but cannot estimate real patient sentiment, response bias, prevalence, or intervention effect.

## 8. Workload and module sequence

| Module | Title | Instructional week | Hours | Main submission |
|---:|---|---:|---:|---|
| 01 | Framing a patient-experience and engagement decision | 1 | 15.5 | Patient-experience decision charter |
| 02 | Patient-reported measurement and scale construction | 2 | 16.0 | Patient-measurement lab |
| 03 | Response, representation, and survey bias | 3 | 16.5 | Response and representation audit with Week 3 release |
| 04 | Linked patient evidence | 4 | 16.5 | Response and linked-evidence analysis |
| 05 | Patient voice, group differences, and equity | 5 | 16.0 | Equity and patient-voice memo |
| 06 | Partnered improvement and embedded machine learning | 6 | 16.0 | Week 6 release with transparent-versus-ML comparison |
| 07 | Clinician and patient leadership, accountability, and defense | 7 | 16.0 | Final patient-experience and engagement package |
| Total |  |  | 112.5 |  |

Module 06 contains eight hours of patient partnership and improvement work plus an eight-hour ML extension. The extension tests response-adjustment behavior against a known selection mechanism. It cannot replace the transparent benchmark or patient-partner interpretation.

## 9. Module 01 brief: Framing a patient-experience and engagement decision

- Module ID: `oclc-app2-01`.
- Hours: 15.5.
- Package path: `courses/patient-experience-engagement/modules/01-patient-experience-decision/`.
- Specification: `docs/curriculum/courses/APP-2/modules/01-patient-experience-decision-spec.md`.
- Decision: whether the recovery-at-home patient-reported construct is defined well enough to enter instrument selection.
- Submission: patient-experience decision charter.

Learners distinguish experience, satisfaction, PROMs, PREMs, engagement, partnership, and clinical outcomes; map the patient journey; name patient-partner decision rights; reproduce the complete HCAHPS profile; and identify evidence the public hospital-level source cannot provide.

Progression requires an exact source identity, one accountable decision, one target population, a patient-partner role, a construct map, a claim boundary, and permission to begin instrument selection. Improvement implementation remains prohibited.

## 10. Module 02 brief: Patient-reported measurement and scale construction

- Module ID: `oclc-app2-02`.
- Hours: 16.0.
- Package path: `courses/patient-experience-engagement/modules/02-patient-reported-measurement/`.
- Specification: `docs/curriculum/courses/APP-2/modules/02-patient-reported-measurement-spec.md`.
- Status: runnable release candidate at Commons 0.57.0.
- Decision: which patient-reported instrument and scoring rule fit the recovery-at-home question.
- Submission: 20-point patient-measurement lab component.

Learners compare candidate instruments, distinguish construct and content validity from reliability, implement scoring and direction rules, inspect item behavior, interpret meaningful change, and audit language, format, proxy, and burden requirements. No instrument may be altered or combined without an explicit rights and validation decision.

The released teaching selection is the updated HCAHPS Q22/Q23 Discharge Information pair. The package retains all 22 current mode-language instruments and five guidance PDFs, keeps Q20 separate, applies Q21 skip logic, and distinguishes the unadjusted teaching calculation from the official adjusted CMS composite.

## 11. Module 03 brief: Response, representation, and survey bias

- Module ID: `oclc-app2-03`.
- Hours: 16.5.
- Package path: `courses/patient-experience-engagement/modules/03-response-representation-bias/`.
- Specification: `docs/curriculum/courses/APP-2/modules/03-response-representation-bias-spec.md`.
- Status: runnable release candidate at Commons 0.58.0.
- Decision: who the evidence represents and whether it may enter linked analysis.
- Submission: response and representation audit with cumulative Week 3 release.

Learners define the target population and sampling frame, compute overall and subgroup response, separate item missingness from total nonresponse, compare responders with the eligible frame, inspect coverage and mode effects, apply one bounded weighting method, and document privacy and consent limits.

The Week 3 package scores the Module 02 measurement lab at 20 points. Module 03 response evidence is a noncompensable gate for the later 25-point response and linked-evidence component.

The released case retains the full five-file MEPS HC-256 suite and builds a 1,255-person public-derived frame with a deterministic synthetic response layer. The 13-cell teaching adjustment improves Q22, Q23, and the composite relative to base weighting but leaves known residual bias. No synthetic rate is a real patient, hospital, HCAHPS, access, equity, prevalence, or clinical result.

## 12. Module 04 brief: Linked patient evidence

- Module ID: `oclc-app2-04`.
- Hours: 16.5.
- Package path: `courses/patient-experience-engagement/modules/04-linked-patient-evidence/`.
- Specification: `docs/curriculum/courses/APP-2/modules/04-linked-patient-evidence-spec.md`.
- Status: runnable release candidate at Commons 0.59.0.
- Decision: whether experience, access, communication, engagement, and service-use evidence can be linked and interpreted with aligned denominators.
- Submission: 25-point response and linked-evidence analysis component.

Learners pin MEPS person and event files, build the governed linkage, reconcile eligible populations and periods, define access and communication measures, interpret digital engagement without equating access with preference, and compare service-use patterns without causal claims.

The released case retains all 25 official files for HC-256 and HC-254D through HC-254G. Every one of the 174,231 source event rows links to the person file with no event-person weight mismatch. The accepted 1,255-person target contains 28,455 linked events, including 12 inpatient stays that began in 2023 and continued into the 2024 event file. Released teaching tables omit direct MEPS identifiers and preserve the exact Week 3 response handoff.

The evidence package separates 14 denominator decisions, 10 access and communication estimates, eight service-use estimates, and seven digital-channel results. The 45-record provider-language estimate is limited support, and the absent portal-preference field is recorded as unavailable rather than inferred from telehealth use. Synthetic linked patterns are procedural teaching associations, never real patient-experience, causal, clinical, prevalence, targeting, or ranking evidence.

## 13. Module 05 brief: Patient voice, group differences, and equity

- Module ID: `oclc-app2-05`.
- Hours: 16.0.
- Decision: which patient-voice and subgroup findings are supportable enough to inform co-design.
- Submission: 20-point equity and patient-voice memo component.

Learners apply a transparent codebook to synthetic comments, check agreement, use bounded assisted classification only after human coding, preserve example context, state why comment frequency is not prevalence, compare prespecified groups with uncertainty, audit channel exclusion, and revise stigmatizing language.

## 14. Module 06 brief: Partnered improvement and embedded machine learning

- Module ID: `oclc-app2-06`.
- Hours: 16.0.
- Application block: 8.0 hours.
- Embedded ML extension: 8.0 hours.
- Decision: whether the evidence supports a feasible improvement proposal and whether ML changes the response-adjustment decision.
- Submission: cumulative Week 6 release.

Patient partners record interpretations and disagreements before the team drafts a driver diagram, workflow, measures, burden review, feedback loop, and revision rule.

The ML extension compares a transparent response-propensity or weighting benchmark with one bounded model under the same eligible fields, train/test separation, simulated selection mechanism, and recovery targets. Weight stability, bias recovery, subgroup support, calibration, error costs, and failure cases matter more than one discrimination score.

The Week 6 package scores Module 04 at 25 points and Module 05 at 20 points. Module 06 gates are required but add no points.

## 15. Module 07 brief: Clinician and patient leadership, accountability, and defense

- Module ID: `oclc-app2-07`.
- Hours: 16.0.
- Clinician of record: Joe Joseph, MD, SFHM. Dated public identity is confirmed; participation and final wording require direct confirmation before alpha.
- Patient-partner co-lead: role required; named participant and participation terms pending.
- Decision: what the service and patient advisory group should do next, who owns it, how results return to patients, and when the proposal must stop or change.
- Submission: final patient-experience and engagement package and defense.

Leadership cannot repair an invalid measure or unrepresentative evidence. The panel may narrow, revise, refer, or stop the proposal. Patient-facing reporting, feedback, compensation, access, ownership, monitoring, and disagreement records are required.

## 16. Three cumulative checkpoint contracts

### Checkpoint 1: Measurement and representation readiness

- Timing: end of instructional Week 3.
- Course points: 20.
- Package path: `courses/patient-experience-engagement/checkpoints/01-measurement-representation-readiness/`.
- Specification: `docs/curriculum/courses/APP-2/checkpoints/01-measurement-representation-readiness-spec.md`.
- Status: runnable release candidate at Commons 0.58.0.
- Decision: may the selected measure and response evidence enter linked analysis?

Required evidence includes the Module 01 charter, instrument and rights record, scoring checks, validity and reliability interpretation, meaningful-change and burden decisions, target population, sampling frame, response and item-missingness profile, mode and coverage review, bounded weighting evidence, source and AI records, 20-point measurement score, gates, and progression decision.

### Checkpoint 2: Linked evidence and patient voice

- Timing: end of instructional Week 6.
- Course points: 45.
- Future path: `courses/patient-experience-engagement/checkpoints/02-linked-evidence-patient-voice-release/`.
- Decision: is the case strong enough for clinician and patient leadership review?

Required evidence includes accepted Week 3 identity, MEPS source and linkage records, aligned denominators, access, communication, engagement, service-use, response, missingness, weighting, group and uncertainty evidence, synthetic-comment provenance, human codebook and agreement, qualitative limits, equity and exclusion review, patient-partner interpretations, improvement design, transparent-versus-ML comparison, 45-point score, gates, and Module 07 progression.

### Final checkpoint: Patient-experience and engagement package

- Timing: official last day of the assigned half-term.
- Course points: 35.
- Future path: `courses/patient-experience-engagement/checkpoints/03-patient-experience-engagement-package/`.
- Decision: should the organization run a bounded prospective measurement and improvement test, revise, refer, or stop?

Required evidence includes both accepted checkpoints, the final reproducible repository, evidence synthesis, patient-facing report, patient-partner interpretation and disagreement record, action brief, workflow and feasibility, access and burden review, implementation, process, outcome, balancing, response, and data-quality measures, feedback and accountability plan, transparent-versus-ML conclusion, monitoring and stop rules, technical appendix, AI record, defense, 35-point score, gates, and disposition.

## 17. Assessment map and grading rules

| Source assessment | Feedback milestone | Cumulative checkpoint | Course points |
|---|---|---|---:|
| Patient-measurement lab | End of Week 2 | Week 3 | 20 |
| Response and linked-evidence analysis | End of Week 4 | Week 6 | 25 |
| Equity and patient-voice memo | End of Week 5 | Week 6 | 20 |
| Patient-experience and engagement package | End of Week 7 | Official half-term end date | 35 |
| Total |  |  | 100 |

Every component uses five recurring criteria: correct, reproducible, sound patient-measurement reasoning, clear and patient-centered, and responsible agent use.

A numeric threshold cannot compensate for a wrong instrument, invalid score, undefined sampling frame, hidden nonresponse, misaligned denominator, restricted data, inaccessible output, fabricated comment, unsupported causal claim, or missing patient-partner record.

## 18. Software, reproducibility, and data policy

SQL owns linkage and denominator logic. Python owns source checks, scoring, response analysis, group comparison, bounded comment analysis, ML, and validation. Git records exact reviewed versions. R output is read and interpreted when a supported runtime is available.

Every source is pinned by URL, bytes, hash, date, terms, grain, and field inventory. The full accepted public source stays available in compressed form when repository limits permit. Derived teaching extracts record their owning script and remain reproducible from the full source.

Synthetic data require a generator, seed, known-truth contract, source-field map, explicit flag, and tests. No synthetic result may be described as observed patient testimony, real response bias, prevalence, equity, access, or intervention effect.

## 19. Accessibility, equity, privacy, and responsible claims

Every display has an exact table and structured text alternative. Patient-facing reports use plain language, readable structure, and equivalent formats. Survey instruments require language, proxy, disability access, and burden review.

Every group comparison begins with the eligible denominator, invited count when available, response count, item missingness, weight support, and uncertainty. Small or unsupported results are suppressed. Channel access and response do not equal patient preference.

No protected, identifiable, or restricted patient data enter the repository or an external agent. Public facility data remain public but are not used for unsupported ranking. Synthetic comments remain visibly synthetic.

Patient-reported experience is not satisfaction, clinical outcome, causation, or proof of quality. Weighting does not recover people absent from the frame. Comments provide context but not a population frequency. Package acceptance does not authorize implementation.

## 20. Agent policy and accountability

Agents may explain code, propose tests, diagnose scoring and linkage errors, draft documentation, and assist with bounded comment classification. The learner records the tool, purpose, prompt, data classes, affected files, output used or rejected, material claims, independent check, corrections, retained limits, and human owner.

Prohibited use includes patient or restricted data, hidden assistance, unverified scoring or clinical claims, fabricated patient voice, and treating repeated agent output as independent confirmation.

## 21. Instruction, feedback, and clinician leadership

Learners receive a weekly case walkthrough, measurement or data lab, structured critique with patient-partner input, targeted feedback after Weeks 2, 4, 5, and 6, a question clinic, and a monitored help channel.

Joe Joseph, MD, SFHM, is the designated clinician for Module 07 under the same dated identity boundary recorded for APP-1. The course makes no current-employer or current-title claim. Participation, schedule, format, recording permission, and final biography wording require confirmation.

A patient/caregiver partner co-lead is also required. The program must confirm the person, compensation, preparation, access needs, authority, recording consent, and review rights before alpha.

## 22. Reviewer roles and release gates

| Role | Main responsibility |
|---|---|
| APP-2 faculty owner | outcomes, workload, scoring, checkpoints, and progression |
| Patient/caregiver partner | construct relevance, burden, interpretation, language, feedback, and accountability |
| Patient-experience measurement reviewer | instrument fit, scoring, validity, reliability, and meaningful change |
| Survey methods reviewer | frame, response, missingness, mode, weighting, and representation |
| Health-services data reviewer | MEPS sources, linkage, denominators, access, engagement, and service-use meaning |
| Qualitative methods reviewer | codebook, agreement, examples, comment limits, and assisted classification |
| Equity and accessibility reviewer | exclusion, language, disability access, respectful reporting, and alternatives |
| Model evaluation reviewer | transparent benchmark, ML extension, recovery targets, calibration, support, and failures |
| Privacy and governance reviewer | source terms, permitted use, comments, prompts, and excluded data |
| Responsible-AI reviewer | trace, independent checks, corrections, and human ownership |
| Independent reproducer | clean build, exact outputs, hidden dependencies, and release identity |
| Clinical decision owner | recommendation, feasibility, conditions, monitoring, and stop rules |

Curriculum-construction references may proceed with named conditions. Alpha requires program and human review. No release authorizes a real workflow change.

## 23. Durable paths and build order

- Course specification: `docs/curriculum/courses/APP-2/course-spec.md`.
- Source record: `docs/source/app-2-patient-experience-engagement-source-record.md`.
- Course package: `courses/patient-experience-engagement/`.
- Build ledger: `docs/curriculum/BUILD-LEDGER.md`.

Module specification paths:

1. `docs/curriculum/courses/APP-2/modules/01-patient-experience-decision-spec.md`.
2. `docs/curriculum/courses/APP-2/modules/02-patient-reported-measurement-spec.md`.
3. `docs/curriculum/courses/APP-2/modules/03-response-representation-bias-spec.md`.
4. `docs/curriculum/courses/APP-2/modules/04-linked-patient-evidence-spec.md`.
5. `docs/curriculum/courses/APP-2/modules/05-patient-voice-equity-spec.md`.
6. `docs/curriculum/courses/APP-2/modules/06-partnered-improvement-embedded-ml-spec.md`.
7. `docs/curriculum/courses/APP-2/modules/07-clinician-patient-leadership-defense-spec.md`.

Checkpoint paths:

1. `docs/curriculum/courses/APP-2/checkpoints/01-measurement-representation-readiness-spec.md`.
2. `docs/curriculum/courses/APP-2/checkpoints/02-linked-evidence-patient-voice-release-spec.md`.
3. `docs/curriculum/courses/APP-2/checkpoints/03-patient-experience-engagement-package-spec.md`.

Build Modules 01 through 07 in order. Build each checkpoint after its upstream modules. Every unit receives a durable specification, learner package, complete reference, instructor materials, exact data or accepted handoff, checks, release record, semantic-version decision, commit, push, and ledger handoff before the next unit.

## 24. Known issues and decisions still requiring confirmation

- Confirm Joe Joseph's participation, schedule, format, recording permission, and final biography wording.
- Name and confirm the patient/caregiver partner co-lead, compensation, authority, access, preparation, and review terms.
- Complete named human review of the Module 02 HCAHPS version, scoring, access, naming, and comparison decisions before alpha.
- Complete named review of the accepted 25-file MEPS HC-256 and HC-254D through HC-254G release, linkage rules, denominator decisions, and Module 05 handoff before alpha.
- Build and review the synthetic comment corpus before Module 05; no real comments may be copied into it.
- Define and test the known response-selection generator before Module 06.
- Confirm R survey and psychometric execution in one supported teaching environment.
- Assign the official course section and half-term dates before publishing due dates.
- Named measurement, survey, patient, qualitative, accessibility, equity, governance, model, clinical, and reproduction reviews remain pending before alpha.

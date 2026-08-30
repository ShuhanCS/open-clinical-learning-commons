# APP-1: Data for Clinical Care

## 1. Course identity and catalog role

- Course ID: APP-1.
- Title: Data for Clinical Care.
- Credits: 3.
- Delivery: online half-term.
- Planning rhythm: seven instructional weeks plus the official half-term end date.
- Total learner work: 112.5 hours.
- Prerequisites: accepted FND-1 and FND-2 technical releases.
- Primary graded tools: SQL and Python.
- R role: read, run, and interpret published survival and risk-adjustment code; writing R from scratch is not graded.
- Final deliverable: clinical care improvement brief with complete reproducible evidence and a defense.
- Course version target: 0.1.0.
- Current Commons release: 0.54.0 through runnable Module 06 and the Week 6 checkpoint.
- Specification status: construction candidate.

APP-1 is the first applied course. Learners follow a clinical cohort over time, compare care and outcomes while accounting for baseline differences, and recommend a feasible care-pathway improvement. The course takes longitudinal cohorts, censoring, survival analysis, risk adjustment, and clinical variation from foundation recognition to working skill.

The official academic calendar controls each checkpoint date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase is a planning model. Week 3 and Week 6 are instructional checkpoints. The final package is due on the published last day of the assigned half-term.

## 2. Source authority and normalization

The source course is `05-APP-1-Clinical-Care.docx`, 25,134 bytes, SHA-256 `00e1ecf99fe3ad365b21e934fca64c225b1a63a00067afcf451a06050a372d57`. Byte-identical copies appear in both supplied curriculum archives.

The source record is:

`docs/source/app-1-clinical-care-source-record.md`

The source defines seven modules totaling 112.5 hours and four assessments weighted 20, 25, 20, and 35 percent. The Commons preserves every point exactly once while normalizing delivery to three cumulative checkpoints:

- Week 3: 20 points;
- Week 6: 45 points; and
- official half-term end date: 35 points.

The Week 3 package includes the Week 1 decision charter, Week 2 phenotype and cohort, and Week 3 survival-readiness evidence. The Week 6 package adds the scored survival/risk-adjusted and clinical-variation work plus required Module 06 equity, improvement, and embedded machine-learning gates. The final package adds leadership, implementation, monitoring, and defense without rescoring earlier evidence.

## 3. Place in the program and prerequisite handoffs

### FND-1 handoff

Learners arrive able to:

- maintain a versioned and reproducible workspace;
- retrieve and join relational healthcare data;
- define a cohort, index, denominator, and analytic table;
- profile missingness and quality conditions;
- produce descriptive evidence and accessible displays;
- record provenance and transformations; and
- disclose and verify agent-assisted work.

APP-1 does not reteach generic SQL joins, environments, data cleaning, or chart construction. It applies them to a longitudinal care pathway with follow-up, censoring, exposure, outcomes, and clinical decision ownership.

### FND-2 handoff

Learners arrive able to:

- translate a decision into an analytic aim, target, and prediction time;
- fit and interpret regression models;
- distinguish prediction, association, and causal questions;
- evaluate models with fixed splits and uncertainty;
- recognize confounding, missing-data mechanisms, longitudinal dependence, and survival structure;
- test pipelines and reject leakage or contamination;
- document model use, monitoring, stop rules, and governance; and
- defend a reproducible analytic package.

APP-1 moves survival analysis and risk adjustment to working level. It requires the learner to run the methods, connect them to a care pathway, explain clinical meaning, and make a bounded improvement recommendation.

### Downstream handoff

- APP-3 and APP-5 may rely on the ability to compare outcomes across sites and subgroups.
- APP-6 may rely on time-to-event and follow-up reasoning.
- CAP-1 may rely on a complete longitudinal cohort, survival analysis, risk adjustment, improvement recommendation, and defense.

## 4. Course decision and named audiences

The continuing teaching decision is:

> Should a hospital medicine care-improvement council design and prospectively evaluate a pathway that increases scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge?

The reference analysis examines adults in the pinned Synthea longitudinal release. It uses a day-30 landmark and follows eligible people for the first acute return from day 31 through day 365. This is a synthetic teaching question. It does not establish that scheduled follow-up causes fewer acute returns.

### Primary decision owner

The primary decision owner is a hospital medicine medical director or clinical care-improvement council with authority to sponsor a prospective improvement test.

### Required audiences

| Audience | What they need |
|---|---|
| Clinical decision owner | target population, patient-important outcomes, strength of evidence, feasibility, safety, and a specific next step |
| Care team | pathway steps, workflow implications, inclusion and exclusion rules, measures, and escalation |
| Data and analytics team | phenotype, index, exposure, follow-up, censoring, case mix, methods, checks, and reproduction |
| Quality and operations partner | implementation owner, process measures, balancing measures, workload, and review cadence |
| Patient or community partner | why the outcome matters, burden, access and equity concerns, and how feedback changes the plan |
| Governance reviewer | source rights, privacy, agent use, claim boundary, monitoring, stop rules, and condition ownership |

The final brief must be understandable to clinical and operational readers while preserving an exact technical appendix.

## 5. Course learning outcomes

By the end of APP-1, learners can:

| ID | Assessable course outcome | Program connection |
|---|---|---|
| CLO-1 | Define a care-pathway decision, target population, treatment or exposure, comparator, outcome set, evidence standard, audience, and feasible next action. | PLO-1, PLO-5 |
| CLO-2 | Construct a longitudinal clinical cohort with validated phenotype, index date, lookback, follow-up, outcome, censoring, and time-at-risk definitions. | PLO-1, PLO-4 |
| CLO-3 | Run and interpret Kaplan-Meier, log-rank, Cox, and risk-adjustment analyses and state what each result can and cannot claim. | PLO-2, PLO-3 |
| CLO-4 | Compare care, utilization, and outcomes across exposure, site, subgroup, and time while accounting for case mix and measurement limits. | PLO-2, PLO-3 |
| CLO-5 | Evaluate clinical variation and equity without converting sparse, adjusted, or observational evidence into unsupported causal or fairness claims. | PLO-3, PLO-6 |
| CLO-6 | Compare a simpler analytic approach with a bounded machine-learning extension and explain whether the extension changes the decision. | PLO-2, PLO-3, PLO-6 |
| CLO-7 | Produce and defend a clinical care improvement brief with implementation, monitoring, unintended-consequence measures, stakeholder ownership, and a reassessment rule. | PLO-4, PLO-5, PLO-6 |

## 6. Concept ownership and boundaries

### APP-1 owns

- care-pathway decision framing;
- target patient population and patient-important outcome set;
- longitudinal phenotype and index logic at working level;
- follow-up, time at risk, censoring, and competing-event recognition;
- Kaplan-Meier estimation and interpretation;
- log-rank comparison;
- Cox model execution, interpretation, and proportional-hazards checks;
- baseline case mix and transparent risk adjustment;
- observed-to-expected and standardized outcome comparisons;
- treatment, procedure, adherence, utilization, and site variation;
- clinical versus statistical significance;
- residual-confounding and observational-claim discipline;
- prespecified subgroup and equity review for the care pathway;
- pathway improvement design, process and balancing measures;
- a bounded machine-learning extension to challenge or improve the simpler case;
- clinical leadership, stakeholder planning, implementation, monitoring, and defense.

### APP-1 extends rather than repeats

- FND-1 cohort and reproducibility skills are extended with time at risk, censoring, and clinical phenotype adjudication.
- FND-2 regression and validity skills are extended with survival and risk-adjusted care comparison.
- DA-730 visualization skills are used to show pathways, survival, adjusted variation, and uncertainty; chart concepts are not retaught as a separate sequence.

### Out of scope

- randomized-trial emulation or a defensible causal treatment-effect estimate;
- full competing-risks estimation beyond guided recognition unless later approved;
- machine learning as a replacement for the simpler analysis;
- real patient, workplace, restricted, or identifiable data;
- deployment or a claim of clinical efficacy;
- ranking real clinicians, facilities, demographic groups, or communities;
- fairness certification;
- a claim that synthetic frequencies represent real prevalence, quality, access, utilization, outcomes, or treatment effect;
- generic SQL, Python, Git, regression, or visualization instruction already owned by prerequisites.

## 7. Continuing source and analytic thread

### Primary source

APP-1 reuses the complete pinned Synthea April 2020 CSV release accepted in FND-1:

https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip

| Item | Accepted fact |
|---|---|
| Publisher | The MITRE Corporation / Synthea |
| Archive bytes | 8,982,431 |
| Archive SHA-256 | `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a` |
| Source tables | 16 |
| Source rows | 471,836 |
| Uncompressed source bytes | 82,293,440 |
| Synthetic people | 1,171 |
| Encounter rows | 53,346 |
| Organizations | 1,119, of which 1,103 appear on encounters |
| Contains real patient records | no |

The official Synthea site describes a synthetic complete medical history with encounters, medications, allergies, and social determinants that may be used without patient privacy restrictions:

https://synthetichealth.github.io/synthea/

The generator source is Apache-2.0 licensed:

https://github.com/synthetichealth/synthea

### Reference pathway feasibility

The initial feasibility rule uses:

- first emergency or inpatient encounter for an adult from 2010-01-01 through 2019-03-31;
- discharge stop as the initial pathway origin;
- scheduled ambulatory, outpatient, or wellness follow-up within 30 elapsed days;
- exclusion from the landmark analysis after a recorded index death, early post-discharge death, or acute return in the first 30 days;
- day 30 after discharge as landmark time zero; and
- first emergency or inpatient return from day 31 through day 365 as the primary time-to-event outcome.

The complete source produces:

| Feasibility item | Count |
|---|---:|
| initial adult index cohort | 518 |
| recorded death on or before index discharge | 9 |
| early post-discharge death through day 30 | 8 |
| acute return before or at day 30 | 25 |
| day-30 landmark eligible | 476 |
| scheduled follow-up within 30 days | 129 |
| acute return from day 31 through day 365 | 87 |
| outcomes among follow-up exposed | 25 |
| outcomes among unexposed | 62 |
| distinct index organizations among landmark-eligible people | 64 |

These counts support a working longitudinal and survival case. They do not support stable 64-organization comparison. Module 02 therefore owns a deterministic six-site teaching extension with documented generation, known case-mix structure, preserved source rows, and an explicit synthetic-extension flag. No site pattern may be presented as observed real performance.

### Source layers

1. Immutable raw Synthea archive when redistribution and local capacity permit.
2. Complete relational SQLite build created by the accepted FND-1 builder.
3. Versioned APP-1 longitudinal cohort and event-level teaching extracts.
4. Deterministic six-site and care-process extension for stable method instruction.
5. Cumulative checkpoint and final decision packages.

## 8. Workload and module sequence

| Module | Title | Instructional week | Hours | Main submission |
|---:|---|---:|---:|---|
| 01 | Framing a care-pathway decision | 1 | 15.5 | Care-pathway decision charter |
| 02 | Longitudinal cohorts and follow-up | 2 | 16.0 | Validated phenotype and cohort with follow-up |
| 03 | Survival and time-to-event outcomes | 3 | 16.5 | Survival analysis notebook and Week 3 release |
| 04 | Risk adjustment and fair comparison | 4 | 16.5 | Risk-adjusted comparison and interpretation memo |
| 05 | Clinical variation and patterns of care | 5 | 16.0 | Clinical variation memo |
| 06 | Equity, feasible improvement, and embedded machine learning | 6 | 16.0 | Equity and improvement release with simple-versus-ML comparison |
| 07 | Clinician leadership, recommendation, and defense | 7 | 16.0 | Final clinical care improvement brief and defense |
| Total |  |  | 112.5 |  |

Module 06 contains eight hours of equity, improvement, and cumulative application work plus an eight-hour machine-learning extension. The extension may improve, challenge, or fail to improve the case. It cannot replace the simpler survival and risk-adjusted analyses.

## 9. Module 01 brief: Framing a care-pathway decision

- Module ID: `oclc-app1-01`.
- Hours: 15.5.
- Package path: `courses/clinical-care/modules/01-care-pathway-decision/`.
- Specification: `docs/curriculum/courses/APP-1/modules/01-care-pathway-decision-spec.md`.
- Foundation extension: decision framing, cohort feasibility, target population, and evidence boundary.
- Decision: whether the proposed 30-day follow-up pathway is measurable and worth carrying into longitudinal analysis.
- Submission: care-pathway decision charter.

The learner maps entry, discharge, follow-up, landmark, outcome, and reassessment; defines population, exposure, comparator, outcomes, audiences, evidence standard, feasibility limits, and improvement options; and interprets the exact source-feasibility counts. The learner must recognize immortal-time risk, sparse sites, synthetic-source limits, and why the analysis supports a prospective improvement design rather than a causal effectiveness claim.

Progression requires one complete decision contract, exact source identity, a defensible outcome set, explicit stop/referral rules, and permission to build the Module 02 cohort.

## 10. Module 02 brief: Longitudinal cohorts and follow-up

- Module ID: `oclc-app1-02`.
- Hours: 16.0.
- Foundation extension: FND-1 cohort work gains phenotype adjudication, landmark eligibility, time at risk, censoring, and event logic.
- Decision: whether the cohort is valid enough for survival analysis.
- Submission: validated phenotype and cohort with follow-up.

The module downloads or verifies the full pinned source, builds the relational database, creates the first qualifying adult acute index, audits early events, fixes the day-30 landmark, constructs time-to-acute-return and censoring fields, validates event and procedure evidence, and produces a cohort flow. It also builds the deterministic six-site teaching extension and records exactly which fields are original, derived, or synthetic extension.

Required outputs include source and extension records, phenotype logic, SQL, cohort flow, person-level cohort, event-level audit table, censoring table, dictionary, transformation record, and tests.

## 11. Module 03 brief: Survival and time-to-event outcomes

- Module ID: `oclc-app1-03`.
- Hours: 16.5.
- Foundation extension: FND-2 survival recognition becomes working analysis.
- Decision: what the time-to-event evidence says and whether the cohort may enter adjusted comparison.
- Submission: survival analysis notebook and cumulative Week 3 release.

Learners summarize follow-up and censoring, fit Kaplan-Meier curves, calculate risk at prespecified times, conduct a log-rank comparison, fit a guided Cox model, check proportional hazards, read paired R survival output, identify competing-event concerns, and write a clinical interpretation.

The Week 3 package freezes Modules 01 through 03. It scores the source 20-point phenotype-and-cohort component once. Survival evidence is a noncompensable progression gate into Module 04 and is scored later in the 25-point survival/risk-adjusted source component.

## 12. Module 04 brief: Risk adjustment and fair comparison

- Module ID: `oclc-app1-04`.
- Hours: 16.5.
- Foundation extension: FND-2 regression and validity become a care-specific risk-adjustment workflow.
- Decision: whether adjusted outcome differences are sufficiently credible to compare care groups and teaching sites.
- Submission: risk-adjusted comparison and interpretation memo.

Learners define baseline case mix, distinguish prognostic from post-exposure fields, fit and validate a transparent expected-outcome model, calculate observed-to-expected ratios and standardized rates, assess calibration and support, compare unadjusted and adjusted evidence, and state residual-confounding limits.

No adjusted comparison becomes a causal effect, clinician grade, or real-site ranking. Sparse, unsupported, or unstable estimates are suppressed or pooled with an explicit rule.

## 13. Module 05 brief: Clinical variation and patterns of care

- Module ID: `oclc-app1-05`.
- Hours: 16.0.
- Foundation extension: descriptive and model evidence become pathway variation and clinical-significance reasoning.
- Decision: which variation is meaningful enough to shape an improvement option.
- Submission: clinical variation memo.

Learners compare follow-up, treatment, procedures, utilization, and outcomes across exposure, teaching site, subgroup, and time. They define adherence or exposure, preserve denominators, distinguish clinical from statistical significance, inspect residual confounding, and audit every statement for association-versus-causation errors.

The module hands Module 06 one bounded variation finding, one equity question, one improvement lever, and one simpler analytic benchmark.

## 14. Module 06 brief: Equity, feasible improvement, and embedded machine learning

- Module ID: `oclc-app1-06`.
- Hours: 16.0.
- Application block: 8.0 hours.
- Embedded machine-learning extension: 8.0 hours.
- Decision: whether a feasible pathway improvement is justified and whether machine learning changes the decision.
- Submission: cumulative Week 6 application release.

### Application work

Learners prespecify subgroup comparisons, review counts and missingness, examine pathway access and outcomes, distinguish an equity concern from proof of unfairness, create an accessible pathway display, draft a driver diagram, and define implementation, process, outcome, and balancing measures.

### Machine-learning extension

Learners compare the transparent risk-adjusted benchmark with one bounded machine-learning model fit under the same prediction time, eligible features, split, and evaluation rows. The extension must report calibration, subgroup support, error costs, failure cases, and whether it changes the improvement decision. Test contamination, feature leakage, unsupported subgroup ranking, and performance-only recommendations fail the module.

### Week 6 package

The package freezes Modules 04 through 06 and scores 45 points exactly once:

- survival and risk-adjusted outcome analysis: 25 points; and
- clinical variation memo: 20 points.

Equity, improvement, and simple-versus-ML comparison are required gates and draft-final evidence, not extra points.

## 15. Module 07 brief: Clinician leadership, recommendation, and defense

- Module ID: `oclc-app1-07`.
- Hours: 16.0.
- Leadership clinician: Joe Joseph, MD, subject to identity and publishable-biography confirmation.
- Decision: what the care-improvement council should do next, who owns it, how it should be tested, and when it must stop or change.
- Submission: final clinical care improvement brief and defense.

The learner reads the analysis as a clinical decision owner, identifies people affected, weighs evidence, feasibility, equity, safety, workload, and operational constraints, makes a specific bounded recommendation, defines implementation and stakeholder roles, chooses process/outcome/balancing measures, sets monitoring and reassessment triggers, and defends the decision under questioning.

The leadership block cannot repair weak technical evidence by rhetoric. It may narrow, defer, refer, or stop the recommendation.

## 16. Three cumulative checkpoint contracts

### Checkpoint 1: Longitudinal and survival readiness

- Timing: end of instructional Week 3.
- Course points: 20.
- Future path: `courses/clinical-care/checkpoints/01-longitudinal-survival-readiness/`.
- Decision owner: APP-1 faculty owner with clinical phenotype reviewer.
- Decision: may the cohort and survival evidence enter adjusted comparison?

Required package:

- accepted Module 01 charter and source-feasibility evidence;
- complete Module 02 source, phenotype, SQL, cohort, censoring, dictionary, transformation, and validation records;
- Module 03 survival notebook, exact tables, accessible curve alternative, assumption checks, and interpretation;
- repository, commit, environment, semantic version, source fingerprints, AI-use record, and reproduction result;
- 20-point phenotype-and-cohort score;
- noncompensable survival-readiness gates; and
- progression decision.

Reference score map:

| Criterion | Points |
|---|---:|
| Decision, target population, phenotype, and index | 4 |
| Source, SQL, longitudinal cohort, follow-up, and censoring | 8 |
| Cohort validation, event audit, and reproducibility | 5 |
| Interpretation, access, and accountable agent use | 3 |
| Total | 20 |

### Checkpoint 2: Adjusted variation and feasible improvement

- Timing: end of instructional Week 6.
- Course points: 45.
- Future path: `courses/clinical-care/checkpoints/02-adjusted-variation-improvement-release/`.
- Decision owner: clinical care analytics lead with methods and improvement reviewers.
- Decision: is the analytic case strong enough to support a draft improvement recommendation and leadership review?

Required package:

- accepted Week 3 identity;
- survival and Cox evidence with assumption limits;
- baseline case mix and risk-adjustment contract;
- expected outcomes, observed-to-expected ratios, standardized comparisons, calibration, and support checks;
- treatment, utilization, time, site, subgroup, clinical-significance, and residual-confounding evidence;
- equity review with counts, missingness, uncertainty, suppression, and unsupported comparisons;
- accessible pathway and variation displays with exact tables and alternatives;
- driver diagram, improvement measures, feasibility, and unintended consequences;
- transparent benchmark versus bounded machine-learning comparison;
- complete source, transformation, AI, tests, failure, reproduction, and reviewer records;
- 45-point score and gates; and
- Module 07 progression decision.

Score map:

| Source component | Points |
|---|---:|
| Survival and risk-adjusted outcome analysis | 25 |
| Clinical variation memo | 20 |
| Total | 45 |

### Final checkpoint: Clinical care improvement package

- Timing: official last day of the assigned half-term.
- Course points: 35.
- Future path: `courses/clinical-care/checkpoints/03-clinical-care-improvement-package/`.
- Decision owner: hospital medicine medical director or clinical care-improvement council role.
- Decision: should the organization run a bounded prospective improvement test, revise the proposal, refer it, or stop?

Required package:

- accepted Week 3 and Week 6 packages;
- complete versioned data and analytic repository;
- final evidence synthesis and clinical care improvement brief;
- patient population, pathway, exposure, comparator, outcome, and claim boundary;
- simple-versus-machine-learning comparison;
- feasibility, workflow, stakeholder, equity, safety, and unintended-consequence plan;
- process, outcome, balancing, access, and implementation measures;
- monitoring, reassessment, rollback, stop, and escalation rules;
- leadership reflection and stakeholder plan;
- accessible technical appendix and exact evidence index;
- final AI-use and accountability statement;
- live, recorded, or equivalent defense;
- 35-point score, gates, conditions, and disposition.

Allowed dispositions are `run bounded prospective improvement test`, `revise before testing`, `refer`, or `stop`. The reference package cannot authorize clinical implementation from synthetic retrospective evidence.

## 17. Assessment map and grading rules

| Source assessment | Feedback milestone | Cumulative checkpoint | Course points |
|---|---|---|---:|
| Phenotype and cohort lab | End of Week 2 | Week 3 | 20 |
| Survival and risk-adjusted outcome analysis | End of Week 4 | Week 6 | 25 |
| Clinical variation memo | End of Week 5 | Week 6 | 20 |
| Clinical care improvement brief | End of Week 7 | Official half-term end date | 35 |
| Total |  |  | 100 |

Every component uses five recurring criteria with course-specific weights:

1. correct;
2. reproducible;
3. sound clinical reasoning;
4. clear and action-guiding; and
5. responsible agent use.

Passing a checkpoint requires the numeric threshold, every noncompensable gate, complete source and transformation evidence, adequate technical interpretation, and an allowed progression or final disposition. Strong writing cannot compensate for an invalid cohort, wrong time zero, mishandled censoring, leakage, changed evidence, restricted data, inaccessible outputs, or an unsupported causal claim.

## 18. Software, reproducibility, and data policy

### Required tools

- SQL for phenotype, index, follow-up, event, and analytic-table logic.
- Python for data checking, survival analysis, risk adjustment, variation, machine learning, and release validation.
- Git for version history and exact reviewed commits.
- Semantic versioning for every module and checkpoint release.
- R survival output for read-run-interpret work when an instructor runtime is available.

### Reproducibility rules

- Every source is fingerprinted before use.
- Every derived table has one owning script or query.
- Time zero, follow-up, censoring, exposure, and outcome rules are machine-readable.
- Randomness has a declared seed.
- Preprocessing is fit only on allowed data.
- Exact evidence tables accompany displays.
- Every package has a learner template, complete reference, validator, and release record.
- Existing targets are never silently overwritten.
- Personal absolute paths, secrets, credentials, and hidden dependencies fail release.

### Data policy

- Public and documented synthetic data are allowed.
- Real patient, workplace, restricted, and identifiable data are prohibited from the public course.
- The full Synthea source remains available through its official URL and is verified by checksum.
- Derived teaching extracts remain small enough to version when practical.
- A deterministic extension must preserve original source fields, mark every extension field, publish its generator, record its seed, and state which result is known by construction.
- No synthetic estimate may be described as real clinical prevalence, quality, access, utilization, equity, site performance, or treatment effect.

## 19. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Every display has an exact table and structured text alternative.
- Survival curves include risk tables or exact time-point tables.
- Pathway diagrams have node, edge, and narrative equivalents.
- Tables have headers and logical reading order.
- Color is not the only carrier of meaning.
- Equivalent written or recorded defense routes preserve the same technical standard.

### Equity

- Subgroups are prespecified from clinical or access relevance.
- Every subgroup result begins with denominator, event count, follow-up, and missingness.
- Small or unsupported comparisons are suppressed.
- Differences are described as concerns or signals unless stronger evidence supports more.
- The plan identifies who may benefit, who may carry burden, and who may be missed.
- A synthetic subgroup result cannot certify fairness or inequity in a real population.

### Privacy

- No real patient or identifiable data enter the repository or an external agent.
- Synthetic identifiers are minimized in learner-facing outputs.
- Exact source rights and terms accompany each data layer.
- Credentials, API keys, and personal paths are prohibited.

### Responsible claims

- Association is not causation.
- A hazard ratio is not a risk difference or probability.
- Risk adjustment does not remove unmeasured confounding.
- An observed-to-expected ratio is conditional on its model and population.
- A machine-learning metric does not establish clinical value.
- Package acceptance does not authorize implementation.

## 20. Agent policy and accountability

Agents may explain code, propose tests, diagnose errors, draft documentation, and help structure survival, risk-adjustment, variation, and improvement work. The learner remains accountable.

Every graded package records:

- tool and model used when known;
- date and purpose;
- prompt or task request;
- files or data classes shared;
- output used or rejected;
- material claims produced;
- independent verification method;
- corrections made;
- retained limitations; and
- named human owner.

Prohibited use includes patient or restricted data, hidden assistance, unverified analytic or clinical claims, bypassing required learning, and treating repeated model output as independent confirmation.

A material agent-assisted step needs a different verification route: exact recalculation, source comparison, test, independent code path, or qualified human review. Agent output is not evidence by itself.

## 21. Instruction, feedback, and clinician leadership

Learners receive:

- a weekly clinical case walkthrough;
- a live or recorded data lab;
- a structured interpretation critique;
- targeted phenotype and cohort feedback in Week 2;
- survival and risk-adjustment feedback in Week 4;
- variation feedback in Week 5;
- draft improvement feedback in Week 6;
- a weekly question clinic and monitored help channel; and
- clinician-led leadership and defense work in Module 07.

Joe Joseph, MD, is the designated clinician for the leadership block, subject to direct identity and publishable-biography confirmation. The architecture does not depend on a current employer or title.

The leadership work uses the learner's own project. It focuses on decision ownership, people affected, evidence, feasibility, equity, safety, workflow, implementation, monitoring, escalation, reassessment, and defense under questioning.

## 22. Reviewer roles and release gates

Required course-review coverage includes:

| Role | Main responsibility |
|---|---|
| APP-1 faculty owner | objectives, workload, checkpoints, grading, and progression |
| Clinical phenotype reviewer | population, phenotype, index, event, follow-up, and clinical meaning |
| Biostatistical methods reviewer | censoring, survival, adjustment, uncertainty, and claim boundary |
| Clinical informatics reviewer | source grain, longitudinal logic, workflow meaning, and data limits |
| Model evaluation reviewer | benchmark, machine-learning extension, calibration, subgroup support, and failures |
| Improvement science reviewer | driver logic, process/outcome/balancing measures, feasibility, and reassessment |
| Accessibility reviewer | tables, alternatives, pathway diagrams, survival displays, and defense access |
| Privacy and data-governance reviewer | source rights, excluded data, prompts, and allowed use |
| Responsible-AI reviewer | trace, material independent checks, and human ownership |
| Independent reproducer | clean environment, ordered commands, exact output comparison, and hidden dependencies |
| Clinical decision owner | recommendation, implementation scope, conditions, and stop rules |

Each module may proceed as a curriculum-construction reference with explicit conditions. Alpha requires named program review. Live learner assessment requires actual learner and reviewer acknowledgment. No package authorizes real clinical implementation.

## 23. Durable paths and build order

### Course records

- Course specification: `docs/curriculum/courses/APP-1/course-spec.md`.
- Source record: `docs/source/app-1-clinical-care-source-record.md`.
- Build ledger: `docs/curriculum/BUILD-LEDGER.md`.
- Course package: `courses/clinical-care/`.

### Module specifications

1. `docs/curriculum/courses/APP-1/modules/01-care-pathway-decision-spec.md`.
2. `docs/curriculum/courses/APP-1/modules/02-longitudinal-cohorts-followup-spec.md`.
3. `docs/curriculum/courses/APP-1/modules/03-survival-time-to-event-spec.md`.
4. `docs/curriculum/courses/APP-1/modules/04-risk-adjustment-fair-comparison-spec.md`.
5. `docs/curriculum/courses/APP-1/modules/05-clinical-variation-patterns-of-care-spec.md`.
6. `docs/curriculum/courses/APP-1/modules/06-equity-improvement-embedded-ml-spec.md`.
7. `docs/curriculum/courses/APP-1/modules/07-clinician-leadership-defense-spec.md`.

### Checkpoint specifications

1. `docs/curriculum/courses/APP-1/checkpoints/01-longitudinal-survival-readiness-spec.md`.
2. `docs/curriculum/courses/APP-1/checkpoints/02-adjusted-variation-improvement-release-spec.md`.
3. `docs/curriculum/courses/APP-1/checkpoints/03-clinical-care-improvement-package-spec.md`.

### Build sequence

Build Modules 01 through 07 one at a time. After Modules 01 through 03, build Checkpoint 1. After Modules 04 through 06, build Checkpoint 2. After Module 07, build the final checkpoint. Every unit receives a durable specification, learner package, complete reference, instructor materials, exact data or accepted handoff, runnable checks, release record, semantic-version decision, commit, push, and ledger handoff before the next unit begins.

## 24. Known issues and decisions still requiring confirmation

- Confirm the intended Joe Joseph, MD, and approved public biography before learner-facing publication.
- The pinned 2020 Synthea source is intentionally stable but old and synthetic.
- The raw landmark cohort spans 64 sparse organizations; stable site-comparison instruction requires the documented six-site extension in Module 02.
- The exact extension generator, case-mix coefficients, site effects, and known-truth contract are owned by Module 02 and must not be invented in later modules.
- Confirm R survival-package execution on at least one supported teaching environment before alpha.
- Confirm the official course section's half-term dates before assigning calendar due dates.
- Named clinical, methods, improvement, accessibility, governance, responsible-AI, and reproduction reviewers remain pending before alpha.
- No reference package may be described as evidence that scheduled follow-up improves outcomes in real patients.

# APP-1 Module 01: Framing a care-pathway decision

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app1-01`.
- Title: Framing a care-pathway decision.
- Version: 0.2.0.
- Commons release target: 0.49.1.
- Course: APP-1, Data for Clinical Care.
- Instructional week: 1.
- Learner work: 15.5 hours.
- Prerequisites: accepted FND-1 and FND-2 final technical packages.
- Package path: `courses/clinical-care/modules/01-care-pathway-decision/`.
- Primary deliverable: care-pathway decision charter.
- Decision owner: hospital medicine care-improvement council role.
- Status: runnable release candidate after validation and release checks pass.

This module fixes the clinical decision before learners build a new cohort or fit a model. It converts a broad idea - improving follow-up after acute care - into a target population, pathway, exposure, comparator, outcome set, evidence standard, audience, feasibility boundary, and next analytic action.

The module does not award separate course points. Its accepted evidence enters the cumulative 20-point Week 3 technical checkpoint.

## 2. Healthcare decision and named audience

The reference decision is:

> Should a hospital medicine care-improvement council design and prospectively evaluate a pathway that increases scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge?

The retrospective synthetic analysis is used to decide whether the question is measurable and whether a bounded prospective improvement test is worth designing. It cannot establish that follow-up causes fewer acute returns.

### Primary decision owner

The primary owner is a hospital medicine medical director or care-improvement council with authority to sponsor a prospective improvement test.

### Required audiences

| Audience | Required information |
|---|---|
| Clinical decision owner | patient population, outcomes, evidence threshold, feasibility, safety, and next action |
| Care team | pathway steps, eligibility, workflow change, measures, and escalation |
| Analytics team | source, phenotype, index, landmark, exposure, comparator, outcomes, and checks |
| Quality or operations partner | process measure, capacity, workload, balancing measure, and review cadence |
| Patient or community partner | outcome relevance, burden, access, equity, and feedback role |
| Governance reviewer | rights, privacy, agent use, claim boundary, stop and referral rules |

The learner must write for these readers. Internal product, interface, or implementation jargon does not belong in the charter.

## 3. Foundation skill being revisited or extended

### FND-1 extension

The learner reuses source provenance, relational grain, cohort denominators, index logic, transformation records, checks, and reproducibility. APP-1 adds a longitudinal landmark, time at risk, patient-important outcomes, clinical phenotype review, and a decision owner.

### FND-2 extension

The learner reuses analytic aims, estimands, prediction-time discipline, validity threats, uncertainty, model-use limits, and governance. APP-1 applies them to a clinical pathway and distinguishes:

- a pathway-improvement decision;
- an observational association question;
- a future prospective evaluation; and
- an unsupported causal-effect claim.

### DA-730 use

The learner uses accessible pathway mapping and decision communication but does not repeat general visualization theory.

## 4. Learning outcomes that can be assessed

By completing Module 01, the learner can:

1. name one decision owner and one feasible next action;
2. define the target population, entry event, discharge origin, and day-30 landmark;
3. distinguish the initial index cohort from landmark eligibility;
4. define scheduled follow-up exposure and the no-follow-up comparator;
5. define a primary time-to-event outcome and supporting process, safety, access, and patient-important outcomes;
6. explain why early death and early acute return affect landmark eligibility;
7. explain why classifying follow-up at discharge time would create immortal-time bias;
8. state the evidence needed before prospective testing and before wider implementation;
9. map clinical, patient, analytic, operational, and governance stakeholders;
10. interpret all fixed source-feasibility counts;
11. identify the 64-organization sparsity problem and require the Module 02 teaching extension;
12. distinguish source fields, derived fields, and future synthetic-extension fields;
13. state what the synthetic source supports and prohibits;
14. define stop and referral triggers;
15. disclose any agent use and independently verify material claims; and
16. defend a `continue`, `continue with conditions`, `revise`, or `refer` progression decision.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 01 owns

- the exact care-pathway decision;
- target population and pathway entry;
- treatment or exposure concept and comparator;
- primary and supporting outcome set;
- patient-important and operational measure gaps;
- decision owner and stakeholder map;
- evidence standards for analysis, prospective testing, and implementation;
- source-feasibility interpretation;
- known landmark and site-sparsity conditions;
- bounded improvement options;
- claim, stop, and referral rules;
- Module 02 progression decision.

### Later modules own

- Module 02: phenotype code, SQL, final index cohort, landmark dataset, censoring, extension generator, six teaching sites, and validation;
- Module 03: Kaplan-Meier, log-rank, Cox, proportional-hazards, competing-event, and survival interpretation;
- Module 04: baseline case mix, risk adjustment, expected outcomes, standardized comparison, and calibration;
- Module 05: care, utilization, site, time, and clinical variation;
- Module 06: equity, improvement design, pathway display, driver diagram, measures, and embedded machine learning;
- Module 07: clinician leadership, implementation, stakeholder plan, recommendation, monitoring, and defense.

### Out of scope

- downloading or rebuilding the full database as a graded Module 01 task;
- final phenotype SQL;
- fitting a survival, regression, risk-adjustment, or machine-learning model;
- estimating a treatment effect;
- ranking the 64 source organizations;
- inventing the six-site extension before Module 02 defines and tests its generator;
- clinical implementation;
- real-patient, workplace, identifiable, credential, or restricted data;
- claims of efficacy, causation, fairness, real prevalence, or real site performance.

## 6. Lesson sequence with estimated learner time

| Sequence | Activity | Hours | Evidence produced |
|---:|---|---:|---|
| 1 | Course case, source, decision owner, and claim-boundary orientation | 1.0 | annotated case notes |
| 2 | Map entry, discharge, follow-up, landmark, outcome, and reassessment | 2.0 | pathway map |
| 3 | Define population, exposure, comparator, and timing | 2.5 | decision-charter draft |
| 4 | Build the outcome set and evidence standards | 2.0 | outcome and evidence tables |
| 5 | Read and challenge the complete-source feasibility profile | 2.0 | feasibility interpretation |
| 6 | Map audiences, affected people, owners, and referrals | 1.5 | stakeholder map |
| 7 | Compare feasible improvement options and unintended consequences | 1.5 | improvement-options table |
| 8 | Reproducibility, source rights, agent disclosure, and claim audit | 1.0 | AI-use and source checks |
| 9 | Independent charter completion, peer critique, revision, and defense | 2.0 | complete submission and progression decision |
| Total |  | 15.5 |  |

The instructor may change synchronous and asynchronous placement but must preserve 15.5 hours and every assessable outcome.

## 7. Authoritative readings and public clinical sources

### Required readings

1. Synthea official description and downloadable synthetic records:
   https://synthetichealth.github.io/synthea/
2. Synthea source and Apache-2.0 license:
   https://github.com/synthetichealth/synthea
3. CMS Measures Management System Blueprint Measure Lifecycle overview, especially conceptualization, specification, testing, and continued evaluation:
   https://mmshub.cms.gov/blueprint-measure-lifecycle-overview
4. PCORI Methodology Standards, especially stakeholder engagement, patient-centered outcomes, target population, comparator, clinical context, and follow-up:
   https://www.pcori.org/research-related-projects/about-our-research/research-methodology/pcori-methodology-standards
5. FDA Patient-Focused Drug Development guidance on selecting fit-for-purpose clinical outcome assessments:
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/patient-focused-drug-development-selecting-developing-or-modifying-fit-purpose-clinical-outcome

### Reading purpose

- Synthea establishes the source's synthetic status, available clinical record types, and privacy boundary.
- CMS supplies a measure lifecycle from concept through specification, testing, implementation, and continued evaluation.
- PCORI supplies patient-centered question, stakeholder, comparator, target population, and follow-up discipline.
- FDA reinforces that outcomes should reflect how patients feel, function, or survive and must fit the context of use.

The module does not imply that its synthetic improvement question is an FDA-regulated clinical trial or a CMS-endorsed quality measure.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Source course document

| Item | Value |
|---|---|
| file | `05-APP-1-Clinical-Care.docx` |
| bytes | 25,134 |
| SHA-256 | `00e1ecf99fe3ad365b21e934fca64c225b1a63a00067afcf451a06050a372d57` |
| verified copies | both supplied curriculum archives |
| teaching purpose | authoritative APP-1 outcomes, schedule, workload, assessments, tools, and material requirements |

### Full Synthea source

| Item | Value |
|---|---|
| publisher | The MITRE Corporation / Synthea |
| archive | `synthea_sample_data_csv_apr2020.zip` |
| URL | https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip |
| bytes | 8,982,431 |
| SHA-256 | `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a` |
| tables | 16 |
| rows | 471,836 |
| uncompressed bytes | 82,293,440 |
| people | 1,171 |
| synthetic | yes |
| real patient records | no |
| teaching purpose | source feasibility, phenotype, longitudinal timing, exposure, outcome, and clinical-record logic |

The module release carries the complete 16-row source-table inventory and a twelve-row feasibility profile. The full source remains downloadable and fingerprinted rather than duplicated in every learner package.

### Rights

The Synthea generator is Apache-2.0 licensed. Generated data are synthetic and described by the publisher as available without patient privacy restrictions. Terminologies and export formats may carry separate terms; the module uses the accepted CSV source and does not claim ownership of external terminologies.

### Interpretation limits

The source can support reproducible technical instruction. It cannot estimate real clinical prevalence, quality, access, utilization, equity, site performance, treatment effect, or benefit.

## 9. Data dictionary and expected analytic structure

### Immutable source inventory

`data/source-table-inventory.csv` has one row per accepted source table:

| Field | Meaning |
|---|---|
| `table_name` | relational table name |
| `archive_path` | exact source CSV path |
| `source_bytes` | uncompressed file bytes |
| `source_rows` | rows excluding header |
| `source_columns` | source columns |
| `source_sha256` | exact source CSV fingerprint |

### Immutable feasibility profile

`data/source-feasibility.csv` has one row per registered fact:

| Field | Meaning |
|---|---|
| `metric_id` | ordered feasibility identifier |
| `metric` | fact being measured |
| `value` | exact numeric or controlled value |
| `unit` | row, person, event, organization, or status |
| `rule` | source and timing definition |
| `decision_use` | how the fact affects the charter |

### Pathway map

`pathway-map.csv` has one row per ordered pathway state:

- state ID;
- sequence;
- state;
- entry rule;
- exit rule;
- time relation;
- source evidence;
- owner;
- failure or ambiguity;
- downstream use.

### Outcome set

`outcome-set.csv` has one row per primary, process, balancing, safety, access, or patient-important outcome concept. Every row records exact timing, numerator or event, denominator or risk set, source availability, decision relevance, and claim limit.

Module 01 defines concepts. Module 02 owns final code and field-level analytic data.

## 10. Worked example and instructor walkthrough

The instructor walks through one intentionally flawed question:

> Did outpatient follow-up reduce readmissions?

Learners identify six defects:

1. no decision owner;
2. no target population or qualifying acute event;
3. no discharge origin or follow-up window;
4. follow-up is post-discharge and cannot be assigned at discharge;
5. readmission lacks event, time, competing-event, and risk-set definitions; and
6. `reduce` is an unsupported causal verb for the planned retrospective synthetic analysis.

The class repairs it to:

> Among synthetic adults with no recorded index death, early post-discharge death, or acute return through day 30 after their first qualifying acute-care discharge, how do time to the first acute return from day 31 through day 365 and supporting pathway measures differ between those with and without scheduled follow-up in the first 30 days, and is the evidence sufficient to design a bounded prospective improvement test?

### Walkthrough calculations

The instructor reads the registered facts in order:

1. 518 adults enter the initial index cohort.
2. Nine have a recorded death date on or before the index discharge date.
3. Eight die after discharge and through day 30.
4. Twenty-five have an acute return before or at day 30.
5. The conditions are nonoverlapping in this release, leaving 476 landmark-eligible people.
6. Of those, 129 have scheduled follow-up within 30 days.
7. Eighty-seven have an acute return from day 31 through day 365.
8. Twenty-five later outcomes occur in the follow-up group and 62 in the comparator.
9. The 476 people span 64 index organizations.

The walkthrough stops before calculating a crude effect. The point is to decide whether the question, timing, outcomes, and later method plan are coherent.

### Correct reference interpretation

The pathway is feasible for longitudinal and survival instruction. It is not ready for raw organization ranking. Follow-up exposure is observed after discharge, so the day-30 landmark prevents classifying later follow-up as if known at discharge. Index deaths, early post-discharge deaths, and returns describe clinically important groups but are outside the landmark comparison and remain visible in the cohort flow. Later Modules must address confounding, support, censoring, and synthetic-source limits.

## 11. Guided practice

Learners complete a structured repair of three candidate questions:

1. a discharge follow-up pathway;
2. a medication-monitoring pathway; and
3. a procedure-to-recovery pathway.

For each, they identify:

- decision owner;
- target population;
- entry and exit;
- treatment, exposure, or care process;
- comparator;
- time zero and follow-up;
- primary and supporting outcomes;
- evidence standard;
- affected people and audiences;
- feasibility conditions;
- unsupported claim;
- next analytic action.

The class selects the reference discharge follow-up pathway because it is measurable in the accepted full source, yields sufficient landmark and outcome counts for a working teaching case, and creates clear longitudinal, survival, adjustment, variation, equity, machine-learning, and leadership work for Modules 02 through 07.

## 12. Independent exercise

The learner completes the reference pathway charter without copying the answer key.

Required independent decisions:

1. write the decision in one sentence;
2. name the decision owner and proposed next action;
3. define initial cohort and day-30 landmark eligibility;
4. define exposure and comparator;
5. define one primary and at least four supporting outcome concepts;
6. map at least six pathway states;
7. set distinct evidence standards for continuing analysis, prospective testing, and implementation;
8. name at least six stakeholder roles and one affected-person role;
9. interpret all twelve feasibility rows;
10. record at least three feasible improvement options;
11. state at least six prohibited claims or uses;
12. record stop and referral triggers;
13. disclose and verify agent use; and
14. recommend `continue`, `continue with conditions`, `revise`, or `refer` for Module 02.

The learner must justify timing and outcome choices from the evidence, not from the answer key's wording.

## 13. Visualization and communication requirements

Module 01 requires a pathway map as a structured table. A visual diagram is optional.

If a visual is submitted, it must have:

- the same ordered states as `pathway-map.csv`;
- visible distinction between discharge origin, exposure window, day-30 landmark, and outcome window;
- early death and early acute return shown as visible branches rather than deleted people;
- no implication that exposure is known at discharge;
- text labels rather than color-only meaning;
- a structured alternative with every node, edge, and timing rule;
- a title naming the synthetic teaching context; and
- a caption stating that the analysis supports method instruction and prospective-test design, not a causal or clinical-effect claim.

The decision charter begins with the practical decision and why it matters. Methods support the decision rather than becoming the story.

## 14. Exact submission package and filenames

The builder creates exactly 19 files:

```text
app1-module01-workspace/
  VERSION
  decision-contract.json
  source-record.yml
  data-spec.md
  assessment.md
  profile_source.py
  validate_workspace.py
  release-manifest.csv
  data/
    source-table-inventory.csv
    source-feasibility.csv
  care-pathway-decision-charter.md
  pathway-map.csv
  outcome-set.csv
  evidence-standard.csv
  stakeholder-map.csv
  improvement-options.csv
  source-feasibility-interpretation.md
  ai-use.md
  progression-decision.md
```

The release manifest freezes nine immutable controls and source records. Nine learner-authored records remain editable until assessment.

No full source archive or SQLite database is submitted in Module 01. The official archive URL, bytes, fingerprint, table inventory, and feasibility outputs provide the source contract. Module 02 owns full database assembly.

## 15. Rubric and pass conditions

Module 01 uses a 20-point readiness rubric for feedback. These are not additional course points; the Week 3 checkpoint converts accepted Module 01 evidence into its cumulative 20-point course assessment.

| ID | Readiness criterion | Points |
|---|---|---:|
| D01 | Decision owner, target population, action, and pathway logic | 4 |
| T01 | Exposure, comparator, timing, landmark, outcomes, and claim boundary | 4 |
| F01 | Exact source-feasibility interpretation and site-sparsity condition | 4 |
| S01 | Patient, clinical, analytic, operational, and governance stakeholder reasoning | 4 |
| R01 | Complete reproducible package, access, agent accountability, and progression decision | 4 |
| Total |  | 20 |

Passing requires:

- at least 16 of 20 readiness points;
- every noncompensable gate;
- no placeholder in complete mode;
- all exact source facts preserved;
- a defensible day-30 landmark;
- explicit synthetic and noncausal boundaries;
- `continue` or `continue with conditions`; and
- Module 02 permission recorded.

Noncompensable gates include exact source fingerprints, complete outcome timing, visible early events, no raw organization ranking, no claim that follow-up causes outcomes, no restricted data, complete source and agent disclosure, accessible structured pathway evidence, and complete condition ownership.

## 16. Common errors, failure modes, and instructor interventions

| Error or failure | Why it matters | Instructor response |
|---|---|---|
| “Improve readmissions” without a decision owner | no one can act or accept conditions | require one owner and one bounded action |
| Exposure classified at discharge | follow-up occurs after discharge and creates immortal-time bias | require the day-30 landmark and visible early-event branch |
| Early death or return deleted from the cohort story | hides clinically important pathway outcomes | restore initial cohort and landmark flow separately |
| Outcome defined only as a database field | no patient, clinical, or decision meaning | require primary and supporting outcome concepts |
| Raw 64-organization ranking | cells are too sparse and synthetic | prohibit ranking and carry the six-site extension requirement |
| “Follow-up reduced returns” | observational synthetic association cannot establish cause | rewrite as difference and prospective-test rationale |
| Feasibility counts copied without interpretation | numbers do not explain the decision | require one decision consequence per metric |
| Patient stakeholder omitted | outcome relevance and burden are unexamined | add patient/community role and feedback route |
| Agent output treated as a source | generated text is not evidence | require source comparison or independent check |
| Large database submitted | unnecessary duplication and portability burden | retain URL, fingerprints, inventory, and small registered outputs |

Repeated confusion about landmark design triggers methods referral before Module 02.

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

- Every table has a header and logical reading order.
- The pathway map is complete without a visual.
- Optional visuals use non-color cues and structured alternatives.
- Decision, evidence, limits, and next action appear in clear headings.
- Equivalent written, oral, or recorded defense routes use the same standard.

### Equity

- Stakeholder mapping includes people affected by access barriers.
- Outcome selection includes patient-important burden and access, not only acute return.
- Subgroups are not ranked in Module 01.
- The charter identifies which people may be missed by a follow-up intervention.
- Synthetic demographic patterns cannot establish real inequity or fairness.

### Privacy

- Only public synthetic source structure and aggregate counts are used.
- Synthetic identifiers are not needed in the module package.
- No patient, workplace, restricted, credential, secret, or personal-path data may enter the package or an external agent.

### Responsible claims

The package must explicitly prohibit clinical efficacy, causal effect, real prevalence, real site performance, fairness certification, and implementation authorization claims.

## 18. AI and agent policy, required disclosure, and verification

Agents may help explain terminology, critique a decision statement, suggest missing stakeholders, test file structure, and edit documentation. They may not decide the clinical recommendation or replace source review.

`ai-use.md` records:

- tool and model when known;
- date;
- purpose;
- prompts or tasks;
- data classes shared;
- files affected;
- output used, modified, or rejected;
- material claim;
- independent verification;
- correction or retained action;
- human owner; and
- accountability statement.

At least one material agent-assisted claim, or an explicit no-material-use statement, is required. A material claim must be checked against the accepted source record, feasibility table, authoritative reading, calculation, or qualified human review. Repeating the prompt to the same agent is not independent verification.

## 19. Answer key and instructor notes

### Reference answer summary

- Decision owner: hospital medicine care-improvement council role.
- Next action: decide whether to build the cohort and design a bounded prospective improvement test.
- Initial population: 518 synthetic adults at their first qualifying emergency or inpatient encounter from 2010-01-01 through 2019-03-31.
- Origin: qualifying encounter discharge stop.
- Early branches: 9 index deaths, 8 early post-discharge deaths, and 25 acute returns before or at day 30.
- Landmark population: 476 people with no index death, early post-discharge death, or acute return through day 30.
- Exposure: at least one ambulatory, outpatient, or wellness encounter after discharge and through day 30.
- Comparator: no such scheduled encounter in that window.
- Primary outcome: first emergency or inpatient return after day 30 and through day 365.
- Landmark exposure count: 129.
- Later outcomes: 87 total, 25 exposed and 62 unexposed.
- Source organizations: 64 among landmark-eligible people; raw ranking prohibited.
- Correct recommendation: `continue with conditions` to Module 02.

### Required conditions

1. Module 02 must reproduce full-source counts.
2. Module 02 must create and register the six-site teaching extension.
3. Index death, early post-discharge death, and acute return remain visible in the cohort flow.
4. Follow-up exposure is assigned only at the day-30 landmark.
5. Later models adjust only baseline or otherwise valid fields.
6. Patient-important, access, and balancing measures remain explicit gaps until source or synthetic-extension support is defined.
7. No causal or real-clinical claim is permitted.

### Instructor judgment

Automation can verify completeness, exact facts, paths, and controlled values. The instructor decides whether the charter is clinically coherent, the outcomes matter, the feasibility reasoning is credible, and the learner understands landmark bias and claim limits.

## 20. Runnable acceptance checks for data, code, links, and expected findings

The release must provide:

- deterministic reference and learner assembly;
- existing-target refusal;
- 19 exact workspace files;
- nine-row immutable manifest with bytes and SHA-256;
- exact source archive, course document, table, row, and byte identities;
- 16 ordered source-table rows totaling 471,836 rows and 82,293,440 bytes;
- exact encounter, patient, organization, medication, procedure, and observation table facts;
- twelve ordered source-feasibility rows;
- exact 518/9/8/25/476/129/87/25/62/64 pathway facts;
- a controlled `not ready` raw-site comparison result;
- a portable standard-library source profiler;
- a profiler self-check using a synthetic miniature SQLite fixture;
- complete record schemas;
- 20-point readiness rubric arithmetic;
- required pathway states and outcome roles;
- controlled progression decision and condition ownership;
- placeholder rejection in complete mode;
- no Unicode em dash or en dash in learner-facing records;
- no personal absolute path, credential, secret, or prohibited data class;
- changed source evidence, invalid score, missing pathway state, unsupported progression, and incomplete-record rejection;
- full visible URLs for source and readings; and
- whole-curriculum regression checks.

The frozen reference release has:

- 132 complete-reference checks;
- 95 learner-starter checks;
- 1,063 manifest bytes; and
- manifest SHA-256 `4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147`.

Two independently assembled reference packages produce the same manifest. The profiler, builder, validator, existing-target refusal, changed-source rejection, missing-pathway-state rejection, invalid-score rejection, and invalid-progression rejection all pass.

## 21. Release status, reviewers, version, and known issues

### Release decision

- Module version: 0.2.0.
- Commons release target: 0.49.1.
- Reference progression: `continue with conditions`.
- Module 02 permission: `permitted for curriculum construction`.
- Clinical use: prohibited.

### Required review coverage

- APP-1 faculty owner;
- hospital medicine or clinical-care pathway reviewer;
- clinical informatics or phenotype reviewer;
- biostatistical methods reviewer with landmark and survival expertise;
- patient or community perspective reviewer;
- accessibility reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer; and
- independent reproducer.

### Known issues

- Named program and patient/community review remain pending before alpha.
- Joe Joseph, MD, identity and publishable biography remain pending for Module 07, not Module 01 release logic.
- The source is synthetic and cannot support real clinical estimates.
- The pinned source is intentionally stable but dates to April 2020.
- Sixty-four source organizations are too sparse for raw ranking.
- The six-site extension is not created in Module 01; Module 02 owns its exact generator and known-truth contract.
- Patient-reported burden, follow-up completion quality, and real access barriers are not fully observed in the source and must remain evidence gaps.
- An actual course section must map the module to the official half-term calendar before assigning a due date.

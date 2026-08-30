# APP-1 Module 02: Longitudinal cohorts and follow-up

## 1. Identity, release, and durable paths

- Module ID: `oclc-app1-02`.
- Title: Longitudinal cohorts and follow-up.
- Course: APP-1, Data for Clinical Care.
- Week: 2.
- Hours: 16.0.
- Module version target: 0.1.0.
- Commons release target: 0.50.0.
- Submission: validated phenotype and cohort with follow-up.
- Decision: whether the cohort is valid enough for survival analysis.
- Primary decision owner: APP-1 faculty owner with clinical phenotype and biostatistical-methods reviewers.

Durable paths:

- module package: `courses/clinical-care/modules/02-longitudinal-cohorts-followup/`;
- module specification: `docs/curriculum/courses/APP-1/modules/02-longitudinal-cohorts-followup-spec.md`;
- course specification: `docs/curriculum/courses/APP-1/course-spec.md`;
- course source record: `docs/source/app-1-clinical-care-source-record.md`; and
- build ledger: `docs/curriculum/BUILD-LEDGER.md`.

## 2. Course role and foundation extension

FND-1 taught general cohort construction, index selection, analytic-table grain, and reproducible SQL. Module 02 applies those skills to a clinical pathway where time has direct analytic meaning. Learners must distinguish index encounter, discharge origin, exposure window, landmark, risk-set entry, event time, death branch, censoring, and administrative end.

The module does not repeat generic SQL or data-cleaning instruction. It extends foundation work through:

- phenotype adjudication for an adult acute-care pathway;
- date-versus-timestamp interpretation;
- index-death and early-event branches;
- a post-discharge exposure that is known only at day 30;
- landmark eligibility;
- person-time and time-to-event fields;
- explicit event and censoring audits; and
- a documented teaching extension that remains separate from source observations.

## 3. Prerequisite handoff and corrected upstream identity

The accepted upstream is APP-1 Module 01 version 0.2.0 at Commons 0.49.1. Its immutable manifest is 1,063 bytes with SHA-256 `4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147`.

Module 02 must preserve:

- source archive SHA-256 `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`;
- 16 source tables, 471,836 rows, and 82,293,440 uncompressed bytes;
- 1,171 synthetic people and 53,346 encounter rows;
- 518 initial adult index records;
- 9 index deaths;
- 8 early post-discharge deaths;
- 25 early acute returns;
- 476 day-30 landmark-eligible people;
- 129 people with scheduled follow-up;
- 87 later acute returns, divided into 25 exposed and 62 unexposed outcomes; and
- 64 source index organizations with raw site comparison status `not ready`.

The 476-person denominator replaces the superseded 485-person preliminary denominator. Synthea death is date-granular while encounter discharge is timestamped. A recorded death date on or before the index discharge date is an index-death branch and cannot enter the day-30 risk set.

## 4. Decision and exact analytic question

The continuing course decision is:

> Should a hospital medicine care-improvement council design and prospectively evaluate a pathway that increases scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge?

Module 02 asks:

> Does the complete longitudinal phenotype preserve every initial person and branch, assign follow-up only after its observation window closes, and produce a defensible day-30 risk set with event and censoring fields that may enter survival analysis?

An accepting decision authorizes Module 03 curriculum construction only. It does not authorize a treatment-effect estimate, facility ranking, prospective test, or clinical implementation.

## 5. Learning objectives

By the end of the module, learners can:

1. translate a pathway decision into exact inclusion, index, exclusion, exposure, landmark, event, and censoring rules;
2. explain why date-granular death and timestamped encounters require a declared reconciliation rule;
3. write read-only SQL that selects one deterministic adult index encounter per person;
4. preserve index death, early death, and early acute return as visible branches rather than silent exclusions;
5. construct one row per initial person and one row per landmark-eligible person with correct time-at-risk fields;
6. distinguish source fields, transparent derivations, and synthetic-extension fields;
7. audit all relevant index, follow-up, acute-return, and death events;
8. explain censoring, competing-event recognition, and administrative follow-up without treating censoring as no event;
9. reproduce the deterministic six-site assignment and its known-truth contract; and
10. release a checked cohort that another analyst can reproduce and use in Module 03.

## 6. Workload contract

| Activity | Hours | Evidence |
|---|---:|---|
| Module 01 handoff, pathway review, and decision contract | 1.0 | handoff audit |
| Phenotype, date-time rules, index selection, and cohort math | 3.0 | phenotype specification and first SQL |
| Longitudinal joins, follow-up exposure, and event audit | 4.0 | event-level audit and longitudinal cohort |
| Landmark, time at risk, death, censoring, and administrative end | 3.0 | censoring table and checks |
| Deterministic six-site extension and provenance | 2.5 | extension record, assignments, and support table |
| Guided and independent interpretation exercises | 1.5 | validation notes and handoff explanation |
| Assessment, reproduction, and progression decision | 1.0 | complete release package |
| Total | 16.0 |  |

## 7. Source, rights, and full-data rule

Primary source:

https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip

Official source information:

https://synthetichealth.github.io/synthea/

Generator source and Apache-2.0 license:

https://github.com/synthetichealth/synthea

The module uses the complete pinned source through the accepted FND-1 relational database builder. The generated database is approximately 141 MB and is rebuilt locally rather than stored in Git. Module 02 commits complete derived teaching extracts, exact SQL, fingerprints, and checks.

Synthea records are synthetic rather than real. Source counts support technical teaching only. They do not estimate real prevalence, access, utilization, quality, equity, outcome risk, treatment effect, or site performance.

Supporting measurement and methods readings:

- CMS Measures Management System Blueprint: https://mmshub.cms.gov/blueprint-measure-lifecycle-overview
- PCORI Methodology Standards: https://www.pcori.org/research-related-projects/about-our-research/research-methodology/pcori-methodology-standards
- FDA patient-focused outcome guidance: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/patient-focused-drug-development-selecting-developing-or-modifying-fit-purpose-clinical-outcome

## 8. Exact phenotype and timing contract

### Initial population

For each synthetic person, select the first encounter that:

- has class `emergency` or `inpatient`;
- starts on or after `2010-01-01T00:00:00Z`;
- starts before `2019-04-01T00:00:00Z`; and
- occurs at age 18 or older.

Break a same-start tie by encounter ID. The selected encounter stop is discharge origin and day 0.

### Death branches

- Index death: recorded death date is on or before the index discharge date.
- Early post-discharge death: recorded death date is after the discharge date and on or before the discharge date plus 30 days.
- Later death: recorded death date is after day 30 and on or before day 365.

Death is date-granular. The module must not manufacture a death time within that date. Index and early deaths remain in the 518-person cohort and do not enter the landmark risk set.

### Early acute-return branch

The first `emergency` or `inpatient` encounter starting after discharge and no later than 30 elapsed days after discharge is the early acute return. All qualifying events remain in the event audit; only the first defines the branch.

### Scheduled follow-up exposure

Scheduled follow-up is at least one `ambulatory`, `outpatient`, or `wellness` encounter starting after discharge and no later than 30 elapsed days after discharge. All qualifying records remain auditable. Exposure is assigned only when the window closes at the day-30 landmark.

### Landmark and outcome

Landmark eligibility requires no index death, early post-discharge death, or early acute return. The primary event is the first `emergency` or `inpatient` encounter starting after day 30 and no later than day 365 after discharge.

## 9. Time at risk, censoring, and competing-event contract

For each landmark-eligible person:

- risk-set origin is discharge plus 30 elapsed days;
- event time is the first later acute-return start;
- administrative end is discharge plus 365 elapsed days;
- observed time is event time minus landmark when the event occurs first;
- otherwise observed time ends at the earliest recognized later death or administrative end; and
- the event indicator is 1 only for the first later acute return.

A later recorded death is a competing-event concern and a censoring boundary for the primary cause-specific teaching analysis when it precedes the acute return. Death after the acute return remains in the event audit but does not change first-event time. Module 03 must explain that cause-specific censoring does not make death noninformative and does not replace competing-risks analysis.

The release must prove:

- every landmark row has positive observed time;
- no event starts on or before the landmark;
- no event or censoring time exceeds 335 days after the landmark;
- event and censoring dispositions are mutually exclusive;
- event plus non-event counts equal 476; and
- source-derived times can be traced to an event-audit row or declared administrative end.

## 10. Required source-derived tables

The reference builder writes the following outputs from read-only SQL and standard-library Python:

| File | Grain | Required content |
|---|---|---|
| `outputs/index-cohort.csv` | one row per initial person | source person and index IDs, baseline demographics, index timing and class, source organization, and pre-index counts |
| `outputs/event-audit.csv` | one row per relevant source event | index, scheduled follow-up, early acute return, later acute return, and death records with timing, role, and first-event selection |
| `outputs/longitudinal-cohort.csv` | one row per initial person | all branches, first-event fields, exposure, landmark eligibility, event indicator, observed time, and censor reason |
| `outputs/query-checks.csv` | one row per invariant | observed values for source, phenotype, branch, exposure, outcome, time, and conservation checks |
| `outputs/cohort-flow.csv` | one row per ordered flow step | starting, branch or exclusion, remaining, and conserved counts |
| `outputs/censoring-summary.csv` | one row per disposition and exposure group | people, events or censoring reason, and observed-time summary |

Synthetic identifiers are retained only where necessary for reproducible joins. Names, addresses, SSNs, driver identifiers, passports, providers, payers, costs, and other unnecessary fields are not released.

## 11. Six-site teaching extension and known truth

Raw source organization comparison remains prohibited. The source has 476 landmark-eligible people across 64 sparse index organizations. Module 02 creates six teaching sites labeled `SITE-A` through `SITE-F`.

The extension contract is:

1. Keep all source rows, exposure values, outcomes, dates, and source organization IDs unchanged.
2. Derive a baseline risk score only from age at index, prior 365-day acute encounters, prior 365-day condition count, and index encounter class.
3. Rank the 476 eligible people by baseline score with a deterministic SHA-256 tie-break and assign low, medium, or high baseline-risk tier.
4. Draw one teaching site from fixed tier-specific probabilities using SHA-256 of seed string `app1-six-site-v1` plus synthetic patient ID.
5. Give every person exactly one site and retain all three baseline-risk tiers at every site.
6. Inject no site effect into source exposure or outcome. The known direct site effect is zero because site assignment is an instructional label, not a data-generating cause of the already observed source event.
7. Mark every new field as `synthetic_extension` and keep it separate from source and derived fields.

Fixed site probabilities by tier:

| Tier | SITE-A | SITE-B | SITE-C | SITE-D | SITE-E | SITE-F |
|---|---:|---:|---:|---:|---:|---:|
| low | 0.25 | 0.20 | 0.18 | 0.15 | 0.12 | 0.10 |
| medium | 0.12 | 0.15 | 0.18 | 0.20 | 0.18 | 0.17 |
| high | 0.08 | 0.10 | 0.14 | 0.18 | 0.22 | 0.28 |

The probabilities sum to 1.00 within each tier. The extension is intended to create overlapping but different case-mix distributions for risk-adjustment instruction. It is not a simulation of real facilities.

## 12. Extension outputs and provenance

Required extension outputs:

| File | Grain | Required content |
|---|---|---|
| `outputs/site-assignment.csv` | one row per landmark-eligible person | patient ID, risk score, risk tier, hash-derived uniform value, teaching site, seed, and extension version |
| `outputs/analysis-cohort.csv` | one row per landmark-eligible person | longitudinal source and derived fields plus teaching-site extension fields |
| `outputs/site-support.csv` | one row per teaching site | people, exposure groups, outcomes, risk-tier counts, age and prior-acute summaries, and raw descriptive rates |
| `extension-contract.json` | one module-level contract | algorithm, seed, probabilities, field classes, preserved source facts, known direct effect, and prohibited claims |

The builder also writes `outputs/build-report.json` with output rows, fields, bytes, SHA-256, environment, and validation summary.

## 13. Data dictionary and field classes

`data-dictionary.csv` must contain one row for every released field with:

- file;
- field;
- data type;
- grain;
- field class: `source`, `derived`, or `synthetic_extension`;
- source table or derivation;
- timing availability;
- missing-value meaning;
- allowed use; and
- prohibited interpretation.

Minimum required field groups:

- synthetic patient and encounter identifiers;
- index start, stop, class, and source organization;
- age, gender, race, and ethnicity from the synthetic source;
- prior encounter, acute, and condition counts measured before index;
- index-death, early-death, and early-acute flags and dates;
- first scheduled-follow-up flag, ID, date, and elapsed days;
- landmark eligibility and landmark date-time;
- first later acute-return flag, ID, date-time, and elapsed days;
- later-death recognition;
- observed time, event indicator, and censor reason;
- risk score and risk tier; and
- teaching-site assignment, seed, and extension version.

Demographic fields support case-mix and measurement review. They do not define biology, identity quality, fairness, or real population patterns.

## 14. SQL, builder, and reproducibility contract

The release contains four complete read-only SQL files:

1. `sql/01-index-cohort.sql`;
2. `sql/02-event-audit.sql`;
3. `sql/03-longitudinal-cohort.sql`; and
4. `sql/04-validation.sql`.

The Python builder:

- uses only the standard library;
- opens the accepted SQLite database read-only;
- refuses an existing target;
- rejects write or database-control SQL;
- executes queries in fixed order;
- writes LF-terminated UTF-8 CSV;
- assigns sites with SHA-256 and fixed probabilities;
- writes a sorted build report;
- preserves partial output for diagnosis if a build fails; and
- includes a miniature-database self-check for index death, early death, early acute return, landmark, exposure, outcome, censoring, and deterministic site assignment.

Two builds from the same source, SQL, and extension contract must be byte-identical.

## 15. Learner route and guided practice

### Guided practice

Learners trace five synthetic patient timelines:

1. index death;
2. early post-discharge death;
3. early acute return;
4. scheduled follow-up followed by later acute return; and
5. no scheduled follow-up with administrative censoring.

For each timeline they identify source rows, branch, landmark eligibility, exposure availability, risk-set entry, event indicator, observed time, and claim limit.

### Independent practice

Learners must:

1. complete the phenotype specification;
2. complete or repair all four SQL files;
3. reproduce the 518-person and 476-person tables;
4. reconcile cohort flow and event audit;
5. explain all censoring dispositions;
6. reproduce the six-site extension;
7. reconcile every released field to the dictionary;
8. complete transformation, validation, reproduction, and AI-use records; and
9. issue an allowed progression decision.

Changing the seed, site probabilities, source outcomes, source exposures, or upstream timing rules is not an acceptable learner shortcut.

## 16. Exact submission package

The learner submits:

- `README.md`;
- `VERSION`;
- `source-record.yml`;
- `extension-contract.json`;
- `data-dictionary.csv`;
- four SQL files;
- `phenotype-spec.md`;
- `transformation-record.md`;
- `validation-notes.md`;
- `reproducibility-check.md`;
- `ai-use.md`;
- `progression-decision.md`;
- `outputs/index-cohort.csv`;
- `outputs/event-audit.csv`;
- `outputs/longitudinal-cohort.csv`;
- `outputs/query-checks.csv`;
- `outputs/cohort-flow.csv`;
- `outputs/censoring-summary.csv`;
- `outputs/site-assignment.csv`;
- `outputs/analysis-cohort.csv`;
- `outputs/site-support.csv`; and
- `outputs/build-report.json`.

No personal absolute path, credential, secret, real patient data, restricted data, or undeclared external file may appear.

## 17. Assessment and noncompensable gates

This module carries the 20-point phenotype-and-cohort source component that enters the cumulative Week 3 checkpoint.

| Criterion | Points |
|---|---:|
| Phenotype, index, date-time rule, and branch logic | 5 |
| Longitudinal exposure, landmark, event, and time-at-risk construction | 5 |
| Event audit, censoring, conservation, and validation | 4 |
| Six-site extension, field classes, provenance, and support | 3 |
| Reproducibility, interpretation, accessibility, and accountable agent use | 3 |
| Total | 20 |

Passing requires at least 16 points and every noncompensable gate:

1. accepted source and Module 01 fingerprints;
2. exactly one deterministic index row per person;
3. 518-person initial cohort conservation;
4. exact 9/8/25 death and early-return branches;
5. exact 476-person landmark denominator;
6. exposure assigned only at day 30;
7. 129 exposed people and 87 later events with 25/62 outcome split;
8. positive, bounded, auditable time at risk;
9. no event after censoring or before risk-set entry;
10. complete event audit and censoring disposition;
11. source, derived, and extension fields separated;
12. deterministic six-site assignment with no changed source outcome or exposure;
13. all six sites contain both exposure groups, later events, and all three risk tiers;
14. complete exact dictionary, source, transformation, and reproduction records;
15. no causal, efficacy, real-site, fairness, or implementation claim; and
16. complete agent disclosure and an allowed progression decision.

## 18. Accessibility, equity, privacy, and responsible claims

Every summary is count first. Exact tables must remain available alongside any future figure. Color cannot be the only carrier of branch, exposure, event, or censoring status. Site labels use neutral letters and cannot imply rank.

Equity review begins with measurement questions:

- Is scheduled encounter occurrence an adequate measure of access?
- What patient burden or preference is missing?
- Are synthetic demographic fields complete and meaningful enough for the proposed comparison?
- Does a missing source encounter mean no care, care outside the generated system, or absent documentation?
- Does the extension create support differences that later adjustment must expose?

The module cannot certify fairness. It cannot rank demographic groups or real facilities. No protected or identifiable patient data enter the release.

## 19. AI and agent policy

Agents may help draft SQL, tests, data dictionaries, and interpretation. They may receive only public synthetic source structure, generated teaching extracts, source fingerprints, and curriculum text.

The AI-use record must include:

- tool and model;
- date;
- task and prompt summary;
- data classes shared;
- files affected;
- output used, modified, or rejected;
- at least one material claim;
- independent verification;
- correction or retained action;
- human owner; and
- accountability statement.

Material timing, count, field-class, extension, or censoring claims must be checked against the accepted database, released SQL, exact output, independent calculation, or qualified human review. Repeating a prompt to the same agent is not independent verification.

## 20. Runnable acceptance checks and fixed findings

The release validator must check:

- exact required files and schemas;
- read-only SQL and forbidden-token rejection;
- source and upstream fingerprints;
- output rows, fields, bytes, and SHA-256;
- 518 initial and 476 landmark rows;
- 9 index deaths, 8 early post-discharge deaths, and 25 early acute returns;
- 129 exposed people and 87 later events divided 25/62;
- one index per person and one analysis row per eligible person;
- all relevant source events represented in the event audit;
- event, death, and administrative-end ordering;
- positive observed time and maximum 335-day landmark follow-up;
- deterministic six-site assignment with fixed seed and probabilities;
- one site per person, six sites, all three tiers per site, exposure support, and event support;
- unchanged source exposure and outcome fields after extension;
- complete data dictionary and field classes;
- assessment arithmetic and gate values;
- placeholder, personal-path, credential, secret, and prohibited-data rejection;
- mutation rejection for changed source evidence, wrong landmark, outcome leakage into assignment, changed seed, invalid score, and unsupported progression; and
- whole-curriculum regression checks.

The frozen release has:

- ten output files totaling 749,342 bytes;
- 518 index rows, 1,018 event-audit rows, 518 longitudinal rows, and 476 analysis rows;
- 87 events, 389 administrative censors, and no competing-death censor before event;
- six site-support rows with 68 to 88 people and 10 to 21 later events per site;
- an eight-row immutable workspace manifest of 1,217 bytes with SHA-256 `9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10`;
- 1,140 complete reference checks;
- 82 learner-starter checks; and
- 1,150 checks when the complete source database is reproduced.

Two complete output builds and two reference workspace builds match byte for byte. The validator copied into a learner workspace enforces the same manifest checks while ignoring Python's generated cache directory. Existing targets, incomplete starters, changed output bytes, invalid scores, and unsupported progression values are rejected.

## 21. Progression, reviewers, and known issues

Allowed dispositions are:

- `continue`;
- `continue with conditions`;
- `revise`; and
- `refer`.

The reference target is `continue with conditions`. Module 03 permission is `permitted for curriculum construction` only when all gates pass.

Required review roles:

- APP-1 faculty owner;
- hospital medicine or care-pathway reviewer;
- clinical informatics and phenotype reviewer;
- biostatistical reviewer with landmark, survival, and censoring expertise;
- synthetic-data and extension reviewer;
- patient or community perspective reviewer;
- accessibility reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer; and
- independent reproducer.

Known issues before alpha:

- named human reviews remain pending;
- the source is synthetic and dated April 2020;
- death is date-granular and not clinically adjudicated;
- scheduled encounter occurrence does not prove completion, access, need, quality, or benefit;
- source outcomes are sparse and cannot support clinical efficacy or real-population claims;
- the six teaching sites are synthetic labels with no injected direct effect and are not real facilities;
- the primary teaching analysis recognizes later death as a competing concern but does not replace a full competing-risks analysis; and
- an actual course section must map the module to the official half-term calendar before assigning a due date.

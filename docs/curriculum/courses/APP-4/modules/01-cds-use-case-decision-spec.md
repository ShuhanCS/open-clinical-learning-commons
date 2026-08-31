# APP-4 Module 01: Framing a decision support use case

## 1. Module identity, duration, prerequisites, and place in the course

- Course: APP-4, Data for Clinical Decision Support.
- Module ID: `oclc-app4-01`.
- Title: Framing a decision support use case.
- Course week: 1.
- Learner time: 15.5 hours.
- Module version: `0.1.0`.
- Commons release: `0.77.0`.
- Package path: `courses/clinical-decision-support/modules/01-cds-use-case-decision/`.
- Primary deliverable: CDS use-case charter and source-feasibility release.
- Course points awarded here: 0.
- Week 3 handoff: Module 02 owns the 20-point use-case and logic component; Module 03 owns the 20-point evidence, calibration, and threshold component.

This module fixes the decision support purpose before learners build logic, fit a model, choose a threshold, or create a card. It converts a broad idea about diabetes-related testing into one fictional service, one user, one workflow moment, one nonbinding support action, explicit nonaction, patient and clinician consequences, public and synthetic data roles, accountable owners, prohibited claims, and one permitted next curriculum action.

The module also creates the complete public-data base for later technical work. Learners inspect all 16 official NHANES XPT files named by the course contract. They do not begin with a convenience sample or a prepared analytic table.

### Prerequisites

Learners must be able to:

- work in a versioned reproducible repository;
- acquire and fingerprint a complete public release;
- identify a table grain and primary key;
- inspect fields, missingness, uniqueness, and join coverage;
- distinguish source, derived, public, and synthetic data;
- explain a target, information cutoff, and validation period without fitting a model;
- read an exact table and structured text alternative;
- document AI or agent assistance; and
- state what evidence cannot support.

FND-1 and FND-2 establish those skills. APP-4 applies them to a clinical decision support use case.

## 2. Healthcare decision and named audience

The reference decision is:

> Are the intended use, user, workflow moment, action boundary, source evidence roles, synthetic-data plan, and accountable owners defined well enough to begin logic and input specification?

The decision owner is the fictional `CGH-GIM-01` clinical decision support governance council. The permitted next action is to construct and test the nonproduction logic and input contract in Module 02.

The continuing concept is a nonbinding advisory asking the clinician responsible for the current adult encounter to consider whether confirmatory HbA1c testing is appropriate. The decision moment occurs after required encounter information is available and before the encounter closes.

This is not a diagnosis, order, treatment recommendation, denial, or patient-level action. It is not permission to fit the model early. It is a readiness decision about whether the use case and evidence plan are bounded enough for logic construction.

### Primary audience

| Audience | What that audience must be able to decide |
|---|---|
| CDS governance council | whether the use case may enter Module 02 construction and what conditions remain |
| Clinician receiving the future card | whether the purpose, timing, action, nonaction, uncertainty, and override preserve clinical ownership |
| Primary care or endocrinology reviewer | whether the clinical purpose and confirmatory-action wording are coherent enough for further specification |
| Clinical informatics reviewer | whether the user, workflow moment, input routes, trigger boundary, and audit needs are testable |
| Nursing and workflow reviewer | whether timing, handoffs, interruption, documentation, and hidden work are represented |
| Patient and access representative | whether testing burden, communication, privacy, access, exclusion, and recourse are visible |
| NHANES survey-methods reviewer | whether source roles, cycle differences, design variables, weight decisions, and claim limits are correct |
| Patient-safety reviewer | whether prohibited actions, future failure conditions, stop rights, and unavailable states are explicit |
| Data steward and independent reproducer | whether all source identities, fields, joins, code, manifests, and conditions reproduce exactly |

Each audience has a decision right. The accountability record states who can require revision, who can stop work, and what evidence each person owns.

## 3. Foundation skill being revisited or extended

### FND-1 extension

Learners reuse source acquisition, immutable raw layers, hashes, table grain, primary keys, joins, field inventories, missingness, data dictionaries, structured records, and deterministic builds. APP-4 changes the trust boundary: a field is not usable merely because it exists in a file. It must be available, valid, current, interpretable, and appropriate at the exact workflow moment.

The extension requires learners to ask:

- when was a value observed;
- when did it become available;
- what unit, code, status, and source version apply;
- what happens when it is missing, stale, duplicated, delayed, or inconsistent;
- whether a field is historical evidence, a candidate input, a suppression, or only context;
- which source role requires public data and which requires synthetic workflow truth; and
- who owns the correction when data and clinical meaning disagree.

### FND-2 extension

Learners reuse target definition, information cutoff, classification framing, temporal validation, calibration, thresholds, subgroup support, model cards, monitoring, and governance. Module 01 does not execute those analyses. It fixes the intended-use and source contract that later modeling must honor.

The extension is from technical model evaluation to a sociotechnical decision:

- a target becomes one input to a support action rather than the action itself;
- a threshold becomes a burden and harm decision rather than a score cutoff alone;
- a prediction timestamp becomes an input-availability contract;
- validation becomes evidence for one user and one workflow moment;
- missingness becomes a possible failure or exclusion route;
- calibration drift becomes an owned monitoring problem; and
- model acceptance remains separate from clinical-use permission.

### DA-730 use

Learners use accessible tables, workflow maps, exact labels, plain-language summaries, and decision-first writing. Module 01 does not reteach chart selection. Later calibration, burden, and monitoring displays will be judged for clinical decision support meaning and accessibility.

## 4. Learning outcomes that can be assessed

By the end of Module 01, a learner can:

1. state one bounded CDS readiness decision in one sentence;
2. identify `CGH-GIM-01` as a fictional service with no public facility linkage;
3. name the clinician responsible for the current encounter as the primary user;
4. define the future decision moment relative to information availability and encounter close;
5. distinguish intended support, intended human action, nonaction, and prohibited action;
6. explain why a card may be dismissed or lead to no action without automatically indicating error;
7. identify possible patient and clinician burdens before building the card;
8. assign decision, revision, stop, and evidence ownership;
9. acquire and verify all 16 complete official NHANES XPT files;
10. explain the four cycle roles and preserve cycle identity;
11. distinguish DEMO, BMX, DIQ, and GHB source roles;
12. verify unique `SEQN` values within every file;
13. interpret cycle-specific join support without declaring a final cohort;
14. identify required survey-design fields without selecting an unsupported analysis weight;
15. explain why a public survey cannot establish local workflow or deployment validity;
16. separate public historical evidence from future synthetic workflow evidence;
17. define the minimum synthetic generator, resource, provenance, and known-truth requirements;
18. classify a claim as allowed, conditional, or prohibited;
19. disclose and verify AI or agent assistance;
20. assemble a portable 41-file workspace with a 29-row immutable manifest; and
21. defend a `continue`, `continue with conditions`, `revise`, or `refer` progression decision without granting live-use authority.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 01 owns

- the exact readiness decision;
- the fictional service declaration;
- the primary user;
- the workflow moment;
- intended support, human action, nonaction, and prohibited action;
- preliminary patient and clinician consequences;
- all 16 accepted public source identities;
- cycle and component roles;
- source field and join feasibility;
- public-versus-synthetic data roles;
- the future synthetic-generation contract;
- candidate input routes without predictor acceptance;
- stakeholder decision, revision, and stop rights;
- responsible claim boundaries;
- AI and agent disclosure; and
- the Module 02 progression decision.

### Module 02 owns later

- final logic, trigger, hook, context, and suppression definitions;
- event-time input availability;
- code, value-set, unit, status, timing, and staleness contracts;
- normal, boundary, missing, stale, inconsistent, and duplicate truth cases;
- final clinical eligibility and exclusion proposals for review;
- traceable no-card and unavailable states;
- the first versioned synthetic clinical and workflow release; and
- the 20-point Week 3 use-case and logic component.

### Module 03 owns later

- final historical target and predictor contracts;
- analytic cohort construction;
- survey-design and weight decisions;
- transparent model fitting;
- temporal holdout use;
- later-cycle transport analysis;
- discrimination, calibration, and threshold tables;
- alert budget and missed-case consequences;
- decision-curve interpretation;
- subgroup support; and
- the 20-point Week 3 evidence and calibration component.

### Later modules own

- Module 04: workflow fit, alert burden, human factors, access, privacy, and equity;
- Module 05: nonproduction FHIR R4 and CDS Hooks prototype and failure modes;
- Module 06: safety case, monitoring, governance, drift, silent-failure surveillance, and embedded ML; and
- Module 07: clinician leadership, product brief, evaluation proposal, recommendation, and defense.

### Explicitly out of scope

Module 01 cannot:

- define a final clinical diagnosis or screening rule;
- declare a final target, predictor, eligibility, exclusion, recency, or threshold;
- fit, tune, select, compare, or score a model;
- calculate local `CGH-GIM-01` prevalence or performance;
- treat a four-file join as the final analytic cohort;
- call NHANES a local validation cohort;
- combine survey cycles without a later reviewed design and weight decision;
- copy a public participant identifier, row, or value into synthetic data;
- generate a live or production clinical record;
- fire a card or simulate a clinical action;
- diagnose, order, deny, target, or change treatment;
- claim FHIR conformance, EHR readiness, clinical utility, or deployment safety;
- authorize silent-mode scoring, implementation, or deployment; or
- award course points.

## 6. Lesson sequence with estimated learner time

| Lesson | Topic | Hours | Learner evidence |
|---:|---|---:|---|
| 1 | Course case, fictional service, and decision owner | 1.0 | annotated decision statement |
| 2 | User, workflow moment, intended support, action, and nonaction | 1.5 | workflow-action map draft |
| 3 | Intended-use boundary, patient consequence, and prohibited action | 1.5 | intended-use boundary draft |
| 4 | Complete 16-file NHANES acquisition and identity audit | 2.5 | source-inventory verification |
| 5 | Field inventory, cycle joins, survey design, and missingness | 2.0 | source-feasibility notes |
| 6 | CDS Hooks, FHIR R4, Synthea, SAFER, and synthetic data roles | 1.5 | standards and generator review |
| 7 | Accountability, patient and clinician burden, privacy, and stop rights | 1.5 | stakeholder and claim records |
| 8 | Guided public-versus-synthetic and input-availability mapping | 1.5 | two completed evidence maps |
| 9 | Peer challenge and decision revision | 1.0 | challenged charter |
| 10 | Independent assembly, validation, and defense | 1.5 | complete 41-file submission |
| Total |  | 15.5 |  |

The sequence is straight through. Learners cannot replace the source audit with modeling or skip the workflow decision because the public files are available.

## 7. Authoritative readings and public clinical sources

### Required public sources

NHANES continuous survey portal:

https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/

NHANES analytic guidance:

https://wwwn.cdc.gov/Nchs/data/nhanes/analyticguidelines/11-16-analytic-guidelines.pdf

CDS Hooks published specification:

https://cds-hooks.hl7.org/

FHIR R4 Observation:

https://hl7.org/fhir/R4/observation.html

FHIR R4 Condition:

https://hl7.org/fhir/R4/condition.html

Synthea 4.0.0 release:

https://github.com/synthetichealth/synthea/releases/tag/v4.0.0

ONC SAFER Guides:

https://www.healthit.gov/topic/safety/safer-guides

ONC SAFER Guide 3, Computerized Provider Order Entry with Decision Support:

https://www.healthit.gov/wp-content/uploads/2025/06/SAFER-Guide-3.-CPOE-Final.pdf

### Reading purpose

Learners use NHANES documentation to understand file roles, codebooks, survey design, cycle boundaries, and interpretation limits. They use CDS Hooks and FHIR R4 to identify future teaching message and resource shapes. They use Synthea to evaluate a synthetic-generation route. They use SAFER as a source of safety and governance questions.

No reading certifies the course prototype or decides the clinical target, threshold, or implementation plan. Formal clinical guidance and local policy review remain required before alpha and outside course authorization.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Complete source identities

| File | Cycle role | Rows | Columns | Raw bytes | Raw SHA-256 |
|---|---|---:|---:|---:|---|
| `DEMO_H.xpt` | 2013-2014 development | 10,175 | 47 | 3,833,200 | `f8f0cbb3085a323d4cde22349b164878fea1e64dbc404e65b5815c7816b547d7` |
| `BMX_H.xpt` | 2013-2014 development | 9,813 | 26 | 2,045,520 | `fd5e9fc6e6aab0a4aee6e699f51497bbc9b62101f7f43aee924c473e38fd9442` |
| `DIQ_H.xpt` | 2013-2014 development | 9,770 | 54 | 4,228,960 | `c74c7ccef65e6997dfac1db1e73bc3f63dec67c70b2e322ffc14f14ce27429a9` |
| `GHB_H.xpt` | 2013-2014 development | 6,979 | 2 | 112,720 | `0695894ad55ac96f315a8415401977b0856c402d16762115b534bcd5dfeae89e` |
| `DEMO_I.xpt` | 2015-2016 development | 9,971 | 47 | 3,756,480 | `c9297c6c37ae8f78f29be9568fa2a03cf3b112616a39afee04030fc775a66a0d` |
| `BMX_I.xpt` | 2015-2016 development | 9,544 | 26 | 1,989,600 | `d31da84e14212b4e58e8340598a5b8e2144fac83333563e966eb1b332e4141d6` |
| `DIQ_I.xpt` | 2015-2016 development | 9,575 | 54 | 4,144,720 | `e87587479b29f175b63eee5dd40d582837e3e3fe2665503012085eefdb978e0d` |
| `GHB_I.xpt` | 2015-2016 development | 6,744 | 2 | 108,960 | `e4bc626cd12f6057c7806aef4f85874c9bf1407a7480d6621a4af142260addd2` |
| `DEMO_J.xpt` | 2017-2018 temporal holdout | 9,254 | 46 | 3,412,720 | `c0b46e0345ea19404928656277c8b0d10b0cca348a9b2fe4fc3c67e8b7ee73ec` |
| `BMX_J.xpt` | 2017-2018 temporal holdout | 8,704 | 21 | 1,466,000 | `8d675e42d8826ac98714b2c3dd4c5138a5e353fb4424f7eff5e6db4a01ce838a` |
| `DIQ_J.xpt` | 2017-2018 temporal holdout | 8,897 | 54 | 3,851,840 | `1ecbf5360dfc331d1efbf32198553dc30e9a1f4cff0a907ed30ca72bac797f89` |
| `GHB_J.xpt` | 2017-2018 temporal holdout | 6,401 | 2 | 103,520 | `35f07094573a0061a03ed609a5a363b34eb1b1c7065d1623b43d72e132a8a654` |
| `DEMO_L.xpt` | 2021-2023 transport stress | 11,933 | 27 | 2,582,160 | `ca4374a158b493b8b0163e1388da21d57a18d1b9cecff2aa4e2fa2bec494fe23` |
| `BMX_L.xpt` | 2021-2023 transport stress | 8,860 | 22 | 1,563,200 | `44440c416d9ad709e8b1708a5975378ab4d5b18edc39eb5015c2ae7186500170` |
| `DIQ_L.xpt` | 2021-2023 transport stress | 11,744 | 9 | 847,600 | `9535a023673ae869afae19d842d8679e06f6a464606ac15900686b41ef05090f` |
| `GHB_L.xpt` | 2021-2023 transport stress | 7,199 | 3 | 174,000 | `67aee0353160e2392dc0a33bece99b90764a630c76d82415ac4639105ad9dd03` |
| Total |  | 145,563 component rows | 442 field records | 34,221,200 | 16 separately pinned hashes |

### Provenance contract

`profile_sources.py --acquire` retrieves every exact URL with a declared user agent, writes the raw response to a temporary file, parses the full XPT, profiles every field, and writes a deterministic gzip copy with an empty embedded filename and zero modification time. The committed release records both official decompressed identity and repository gzip identity.

`profile_sources.py` without `--acquire` performs no network request. It decompresses and checks all 16 committed files against hard-coded raw and gzip identities, reparses them, rebuilds the 16-row source inventory, 442-row field inventory, four-row join profile, and five-row standards inventory, and fails on any mismatch.

### Rights and data classes

NHANES files are public federal survey data. The module keeps exact source routes and documentation. Learners must still preserve source attribution and follow the publisher's guidance.

The files are public participant-level survey data, not local patient records. They do not contain `CGH-GIM-01` patients. No public identity or row may be copied into synthetic data. No protected, workplace, or restricted data enter the module.

## 9. Data dictionary and expected analytic structure

### Immutable source inventory

`data/source-inventory.csv` contains these fields:

| Field | Meaning |
|---|---|
| source_id | stable Commons identity for cycle, component, and suffix |
| cycle | official survey cycle label used in the course |
| component | DEMO, BMX, DIQ, or GHB |
| suffix | H, I, J, or L |
| cycle_role | development, temporal holdout, or transport stress role |
| component_role | demographics and design, body measures, questionnaire, or laboratory |
| url | exact complete XPT route |
| codebook_url | exact official documentation route |
| retrieved | acquisition date |
| raw_filename | official XPT filename |
| raw_bytes and raw_sha256 | official decompressed file identity |
| gzip_filename | repository raw-layer path |
| gzip_bytes and gzip_sha256 | deterministic repository artifact identity |
| rows and columns | complete parsed source dimensions |
| seqn_unique and seqn_duplicates | within-file key evidence |
| teaching_role | permitted course use |
| claim_limit | unsupported use |

### Immutable field inventory

`data/field-inventory.csv` records all 442 source fields. A row contains source ID, cycle, component, source order, field name, pandas data type, rows, nonmissing, missing, distinct nonmissing, and source role.

The inventory verifies field presence. It does not harmonize codebooks or approve a predictor. For example, `BMXBMI` appears in every BMX file, but its presence alone does not make it an accepted model input.

### Immutable cycle join profile

`data/cycle-join-profile.csv` reports source rows, pairwise DEMO joins, all-four intersections, required-field presence, and survey-design-field presence. Joins use `SEQN` within the same cycle only.

The all-four intersections are:

- 6,979 in 2013-2014;
- 6,744 in 2015-2016;
- 6,401 in 2017-2018; and
- 7,199 in 2021-2023.

These counts do not apply age, clinical, questionnaire, missingness, or outcome eligibility. They are not model cohorts.

### Immutable standards inventory

`data/standards-inventory.csv` contains five rows for CDS Hooks 2.0.1, FHIR R4 Observation, FHIR R4 Condition, Synthea 4.0.0, and the 2025 ONC SAFER CDS guide. Each row records version, URL, teaching role, and claim limit.

### Editable record structure

The 11 learner records use Markdown or CSV. CSV headers and row counts are fixed so peer and validator review can compare like with like. Learners may revise cell content within the claim boundary.

## 10. Worked example and instructor walkthrough

### Starting prompt

> Build a model from NHANES that finds people who might have diabetes, then alert clinicians to order an HbA1c.

This prompt is not ready. It has no named user, workflow moment, information cutoff, nonaction, burden estimate, local evidence, threshold rule, or safety boundary. It also collapses prediction, diagnosis, ordering, and implementation.

### Walkthrough

1. Name the fictional service before naming a model: `CGH-GIM-01`.
2. Name the user: the clinician responsible for the current adult encounter.
3. Name the workflow moment: after required information is available and before encounter close.
4. Narrow the support: ask the clinician to consider whether confirmatory HbA1c testing is appropriate.
5. Preserve nonaction: the clinician may dismiss, defer, or take no action.
6. Prohibit diagnosis, automatic ordering, blocked workflow, treatment change, denial, and nonclinical targeting.
7. Ask what public evidence can support. NHANES can support later historical model evidence after survey-methods gates pass.
8. Ask what public evidence cannot support. NHANES cannot represent local event-time availability, burden, interaction, or silent failure.
9. Declare a separate future synthetic layer for workflow truth.
10. Assign owners for clinical purpose, survey methods, interoperability, safety, patient consequences, privacy, accessibility, AI, and reproduction.
11. Permit only Module 02 curriculum construction.

### Correct reference decision

The correct construction decision is `continue with conditions`. Source feasibility and the intended-use boundary are adequate for logic construction, but material clinical, survey, terminology, workflow, generator, interoperability, patient, safety, privacy, accessibility, AI, and reproduction conditions remain open.

### Source arithmetic learners must explain

The 145,563 value is the sum of rows across 16 component files. It is not a participant count. The all-four intersection within each cycle is smaller and still not a final analytic cohort.

The 442 value is the count of field records across all files. Field-name presence does not establish common coding, clinical suitability, or predictor acceptance.

## 11. Guided practice

### Practice A: repair the decision

Learners mark every unsupported word in the starting prompt. They rewrite it until it contains a user, workflow moment, intended support, human action, nonaction, patient consequence, clinician burden, owner, and prohibited action.

### Practice B: audit four source roles

For one cycle, learners inspect DEMO, BMX, DIQ, and GHB documentation and explain the grain, key, missingness, role, and limit of each component. They identify which fields require codebook interpretation.

### Practice C: reconcile row counts

Learners reproduce the component row counts and all-four intersection for one cycle. They explain why the smaller intersection is not yet a cohort and why a join failure may reflect component eligibility rather than bad data.

### Practice D: inspect cycle change

Learners compare field inventories between an earlier cycle and 2021-2023. They describe the observed schema difference and propose what later harmonization evidence is needed. They do not assign an unsupported cause.

### Practice E: separate public and synthetic evidence

Learners classify 12 questions. Historical field support and survey design belong to NHANES. Event-time availability, card burden, interaction, latency, drift, and silent failure belong to the future synthetic release. Clinical benefit remains unavailable in both.

### Practice F: challenge stop rights

Peers review the stakeholder map and ask who can stop the concept for clinical incoherence, survey error, workflow burden, patient access, privacy, safety, inaccessible communication, irresponsible AI, or failed reproduction.

## 12. Independent exercise

The learner completes all 11 records without changing immutable evidence.

### Required decisions

The submission must:

1. state the exact module readiness decision;
2. identify the fictional service and decision owner;
3. name the primary user and workflow moment;
4. distinguish intended support, action, nonaction, and prohibited action;
5. name at least one patient consequence and one clinician burden;
6. interpret all 16 source identities and four cycle roles;
7. explain the component-row and participant-count difference;
8. identify every future data role as public, synthetic, both with different purposes, or unavailable;
9. list preliminary input routes without accepting predictors;
10. define synthetic provenance, separation, known truth, and failure requirements;
11. assign decision, revision, stop, and evidence ownership;
12. classify allowed, conditional, and prohibited claims;
13. disclose material AI use and independent checks; and
14. issue one permitted progression decision with conditions and authority limits.

### Independent defense questions

1. What decision does Module 01 make?
2. Why is `CGH-GIM-01` fictional?
3. Who receives the proposed support and when?
4. What can the clinician do or decline to do?
5. Why is confirmatory testing language not a diagnosis or order?
6. What do the 145,563 rows count?
7. Why is the all-four intersection not a final cohort?
8. What survey-design evidence is present, and what decision remains open?
9. What changed in the later-cycle source schema?
10. Which questions require synthetic workflow truth?
11. Which questions remain unavailable even with synthetic data?
12. Who can stop the concept?
13. What may Module 02 build?
14. What remains prohibited after progression?

## 13. Visualization and communication requirements

Module 01 uses exact tables and one workflow map. It does not need a performance chart.

### Required displays

- one user-workflow-action table;
- one intended-use boundary table;
- one public-versus-synthetic data-role table;
- one input-availability table;
- one stakeholder accountability table;
- one claim-boundary table; and
- one plain-language source-feasibility interpretation.

### Display rules

- Every table has a title or filename that states its decision role.
- CSV headers use plain ASCII and retain the fixed schema.
- Status does not rely on color.
- IDs are stable and unique.
- Public and synthetic roles appear in separate columns.
- `open`, `conditional`, `prohibited`, and `unavailable` remain explicit words.
- The source interpretation states the 16-file, 34,221,200-byte, 145,563-row, and 442-field scale accurately.
- A component-row total is never labeled as people.
- A join count is never labeled as an accepted cohort.
- Clinical and deployment authority limits appear in the same package as the recommendation.

## 14. Exact submission package and filenames

The workspace contains exactly 41 files.

### Immutable controls and source evidence, 29 manifest rows

- `.gitattributes`
- `VERSION`
- `requirements.txt`
- `assessment.md`
- `data-spec.md`
- `decision-contract.json`
- `profile_sources.py`
- `source-record.yml`
- `validate_workspace.py`
- `data/source-inventory.csv`
- `data/field-inventory.csv`
- `data/cycle-join-profile.csv`
- `data/standards-inventory.csv`
- `data/raw/DEMO_H.xpt.gz`
- `data/raw/BMX_H.xpt.gz`
- `data/raw/DIQ_H.xpt.gz`
- `data/raw/GHB_H.xpt.gz`
- `data/raw/DEMO_I.xpt.gz`
- `data/raw/BMX_I.xpt.gz`
- `data/raw/DIQ_I.xpt.gz`
- `data/raw/GHB_I.xpt.gz`
- `data/raw/DEMO_J.xpt.gz`
- `data/raw/BMX_J.xpt.gz`
- `data/raw/DIQ_J.xpt.gz`
- `data/raw/GHB_J.xpt.gz`
- `data/raw/DEMO_L.xpt.gz`
- `data/raw/BMX_L.xpt.gz`
- `data/raw/DIQ_L.xpt.gz`
- `data/raw/GHB_L.xpt.gz`

### Editable learner records, 11 files

- `cds-use-case-charter.md`
- `user-workflow-action-map.csv`
- `intended-use-boundary.csv`
- `source-feasibility-interpretation.md`
- `public-synthetic-data-role-map.csv`
- `input-availability-inventory.csv`
- `synthetic-generation-contract.md`
- `stakeholder-accountability-map.csv`
- `claim-boundary.csv`
- `ai-use.md`
- `progression-decision.md`

### Generated workspace control

- `release-manifest.csv`

### Build commands

```powershell
python .\profile_sources.py
python .\build_workspace.py --target .\learner-workspace
python .\validate_workspace.py .\learner-workspace --starter
```

### Reference commands

```powershell
python .\build_workspace.py --target .\reference-workspace --reference
python .\validate_workspace.py .\reference-workspace
```

The builder refuses to overwrite an existing target. Reference and learner workspaces contain the same immutable evidence. They differ only in the 11 assessed records.

## 15. Rubric and pass conditions

Module 01 has no numeric course score. Review uses five evidence areas and 12 noncompensable gates.

| Evidence area | Complete when |
|---|---|
| Decision and intended use | user, workflow moment, support, action, nonaction, consequences, owner, and prohibited actions are coherent |
| Full public-source audit | all 16 files, 442 fields, cycle joins, missingness, survey-design routes, and codebooks are interpreted correctly |
| Public and synthetic separation | every evidence question has the correct source role and no identity or validity leakage |
| Accountability and responsible claims | revision, stop, evidence ownership, AI use, and unsupported claims are explicit |
| Reproducible handoff | exact 41-file package, 29-row manifest, complete records, validation, defense, and progression all pass |

### Noncompensable gates

1. All 16 complete public files have exact accepted raw and gzip identities.
2. All 16 files parse and have unique `SEQN` values.
3. Four cycles each contain exactly DEMO, BMX, DIQ, and GHB with the correct suffix.
4. The 442-row field inventory and four-row join profile reproduce.
5. NHANES remains historical survey evidence and is not called local validation.
6. `CGH-GIM-01` and future workflow data remain explicitly fictional and synthetic.
7. User, workflow moment, intended action, nonaction, and prohibited action are explicit.
8. Patient and clinician consequences, burden, stop rights, and evidence owners are explicit.
9. Public and synthetic data roles remain separate.
10. The submission contains no model, final target, threshold, alert result, or clinical recommendation.
11. AI use is disclosed and independently checked.
12. Progression permits Module 02 construction only while live use and deployment remain prohibited.

A complete-looking charter cannot compensate for changed source bytes, local-validation language, a selected threshold, missing ownership, or live-use permission.

## 16. Common errors, failure modes, and instructor interventions

| Error | Why it fails | Instructor response |
|---|---|---|
| Starting with a model | bypasses the user, action, and harm decision | return to the charter and workflow moment |
| Calling the card a diabetes alert | implies a diagnosis and vague action | require exact nonbinding confirmatory-testing language |
| Treating 145,563 rows as participants | sums component rows and double-counts people | reproduce within-cycle keys and intersections |
| Calling the intersection a cohort | ignores eligibility, missingness, target, and survey decisions | relabel it source support and assign cohort work to Module 03 |
| Pooling cycles immediately | hides survey and schema differences | preserve cycles and defer the weight decision |
| Treating `BMXBMI` presence as predictor acceptance | confuses availability with intended-use fitness | record it as a candidate route only |
| Treating `LBXGH` as a diagnosis | exceeds the source and clinical contract | require clinical target review later |
| Using NHANES as local validation | invents local workflow and calibration evidence | separate historical and local evidence roles |
| Copying public rows into synthetic data | collapses provenance and identities | rebuild a separate generator contract |
| Assuming FHIR-shaped data are conformant | confuses a teaching shape with implementation readiness | add the explicit conformance limit |
| Omitting nonaction | turns the card into a command | require dismiss, defer, no-card, and no-action states |
| Calling every dismissal fatigue | treats an interaction as a motive | require later burden and workflow evidence |
| Selecting a threshold in Week 1 | bypasses calibration, alert budget, harm, and governance | remove it and assign it to Module 03 |
| Permitting silent-mode scoring | turns curriculum progression into prospective use | restore every authority prohibition |
| Hiding agent assistance | breaks accountability | complete the AI-use and verification record |

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

- CSV records have stable headers and logical row order.
- Markdown uses descriptive headings and short direct sentences.
- Status is conveyed with words, not color.
- URLs remain complete and usable.
- The workflow can be read as an exact table without a diagram.
- Acronyms are defined in course instruction before assessment.
- The advisory purpose, action, uncertainty, and nonaction must be expressible in plain language.

### Equity and access

Learners identify who may be excluded by missing body measures, incomplete history, documentation differences, access to confirmatory testing, language, disability, transportation, cost, or follow-up burden. Module 01 does not calculate subgroup performance. It defines the questions and owners that later work must answer.

A candidate input cannot become an automatic exclusion merely because it is missing. A synthetic subgroup difference cannot become a claim about a real group. No public survey category becomes a patient-targeting rule.

### Privacy

The module uses public NHANES files and an explicitly fictional service. It contains no local patient, clinician, employee, workplace, or restricted data. No credentials, network endpoints, or live-system identifiers enter the workspace.

Public participant identifiers remain inside the public source layer. They are never used as synthetic identifiers or linked to a real person.

### Responsible claims

- Source feasibility does not establish clinical usefulness.
- A field in every cycle is not automatically a valid predictor.
- A survey-weight field does not choose the correct analysis by itself.
- A four-component intersection is not an accepted cohort.
- A historical holdout is not local prospective validation.
- A later-cycle difference does not establish its cause.
- A FHIR-shaped record is not a conformant clinical implementation.
- A sandbox plan is not permission to build a live tool.
- Module progression is not clinical approval.

## 18. AI and agent policy, required disclosure, and verification

Agents may help draft acquisition code, profile fields, compare schemas, create record templates, propose test cases, and improve plain-language documentation. Learners must record the task, data shared, output used, independent check, revision, and accountable owner.

Agents may not:

- choose the clinical purpose or intended user;
- define the final target, eligibility, exclusions, predictors, terminology, units, or recency rules;
- choose a survey weight or combine cycles;
- select a threshold or alert budget;
- decide the card wording or interruption level;
- infer patient preferences or subgroup traits;
- approve the synthetic generator or known truth;
- waive a failed source or accessibility check;
- issue progression approval;
- authorize patient scoring, clinical action, implementation, or deployment; or
- receive protected or identifiable data.

Required verification includes pinned raw and gzip hashes, full XPT parsing, `SEQN` uniqueness, field counts, cycle joins, source-role review, two-build manifest equality, complete and starter validation, failure-route tests, and named human review before alpha.

The learner owns the submission. Human reviewers own curriculum, clinical, survey-methods, interoperability, safety, patient, privacy, accessibility, and governance decisions.

## 19. Answer key and instructor notes

### Reference answer summary

- Service: explicitly fictional `CGH-GIM-01`.
- User: clinician responsible for the current adult encounter.
- Moment: after required information is available and before encounter close.
- Support: consider whether confirmatory HbA1c testing is appropriate.
- Human choices: consider, defer, dismiss, or take no action.
- Prohibited behavior: diagnosis, automatic order, blocked workflow, treatment change, denial, nonclinical targeting, or action without clinician review.
- Public source: 16 complete NHANES files, 34,221,200 raw bytes, 145,563 component rows, 442 field records, zero duplicate `SEQN` rows.
- Cycle support: 6,979, 6,744, 6,401, and 7,199 all-four intersections.
- Public role: historical evidence only.
- Synthetic role: future event-time workflow, interaction, burden, drift, and failure truth.
- Unavailable role: clinical benefit and local deployment validity.
- Progression: `continue with conditions` for Module 02 curriculum construction.
- Course points: 0.
- Live-use authority: none.

### Required open conditions

- named clinical review of purpose and wording;
- exact eligibility, exclusions, target, predictors, units, terminology, and recency rules;
- NHANES survey-design, weight, harmonization, and subgroup review;
- Synthea and Commons generator identity, configuration, seed, and known truth;
- FHIR R4 and CDS Hooks teaching-shape review;
- patient, access, language, disability, workflow, burden, and privacy review;
- safety, responsible-AI, and accessibility review;
- official course dates;
- Joe Joseph participation details for Module 07; and
- clean independent human reproduction.

### Instructor judgment

`continue with conditions` is correct because the source release and decision boundary are adequate for Module 02 construction, while important human decisions remain honestly open. `continue` would overstate readiness. `revise` is appropriate if a learner selects a threshold, implies diagnosis or automatic ordering, calls NHANES local validation, collapses public and synthetic identities, or cannot name stop authority. `refer` is appropriate if the clinical purpose or governance question needs a different owner.

## 20. Runnable acceptance checks for data, code, links, and expected findings

### Source checks

- exactly 16 deterministic gzip XPT files exist;
- decompressed bytes and SHA-256 match every pinned official identity;
- gzip bytes and SHA-256 match every committed package identity;
- every file parses with pandas XPORT support;
- every file contains `SEQN`;
- every file has zero duplicate `SEQN` rows;
- the source inventory contains 16 rows;
- the field inventory contains 442 rows;
- the cycle join profile contains four rows;
- the standards inventory contains five rows;
- raw bytes total 34,221,200;
- gzip bytes total 3,149,043;
- component rows total 145,563;
- four-component intersections equal 6,979, 6,744, 6,401, and 7,199;
- required candidate and survey-design field routes are present; and
- a one-byte source mutation changes the pinned identity.

### Builder checks

- learner and reference builds each contain 41 files;
- each manifest contains 29 sorted immutable rows;
- two reference builds have byte-identical manifests;
- learner and reference immutable evidence is identical;
- learner records retain assessed placeholders;
- reference records contain no placeholders;
- existing targets are never overwritten; and
- no build depends on a personal local path.

### Validator checks

- complete reference validation passes 177 checks;
- starter validation passes 121 checks;
- all 12 gates remain required;
- missing records fail;
- changed raw files fail;
- placeholders in a complete package fail;
- copied reference answers in starter mode fail;
- personal local paths fail;
- invalid progression fails;
- deployment permission fails; and
- the exact 41-file set is enforced.

### Link checks

All 16 XPT URLs returned HTTP 200 during source-contract verification on 2026-08-30 and were downloaded successfully for this release. The module retains the full raw bytes, so ordinary validation does not depend on a live network request.

### Expected findings

- each file has unique `SEQN` values;
- component row counts differ within every cycle;
- the GHB file defines the all-four intersection in each accepted cycle;
- DEMO includes the required survey-design routes in every cycle;
- `RIDAGEYR`, `BMXBMI`, `DIQ010`, and `LBXGH` are present in every cycle through their assigned component;
- the 2021-2023 DIQ file has 9 fields while the earlier DIQ files each have 54;
- public evidence cannot answer local workflow or alert burden questions; and
- progression does not authorize modeling or live use.

## 21. Release status, reviewers, version, and known issues

### Release decision

- Module version: `0.1.0`.
- Commons release: `0.77.0`.
- Status: runnable release candidate.
- Reference progression: `continue with conditions`.
- Module 02 construction: permitted with conditions.
- Course points: 0.
- Model, target, predictor, threshold, alert, patient scoring, clinical action, implementation, and deployment authority: prohibited.

The release contains all 16 complete public files, deterministic profiles, complete learner and reference record sets, a protected builder, a validator, failure checks, assessment, instructor notes, and exact handoff boundaries.

### Required review coverage before alpha

- APP-4 faculty owner;
- primary care or endocrinology clinical reviewer;
- clinical informatics physician;
- nursing or workflow lead;
- patient and access representative;
- NHANES and complex-survey methods reviewer;
- FHIR and CDS Hooks interoperability reviewer;
- patient-safety reviewer;
- privacy and data-governance reviewer;
- accessibility and communication reviewer;
- responsible-AI reviewer; and
- independent reproducer.

Joe Joseph, MD, SFHM, is the named clinician for Module 07 under the accepted dated identity boundary. This Module 01 release does not claim his review, participation, or endorsement.

### Known issues

- The official APP-4 section and half-term dates are not assigned.
- Clinical purpose, eligibility, exclusions, target, predictors, units, terminology, recency, threshold candidates, and final wording require named review.
- Survey weight, combined-cycle, harmonization, variance, missingness, and subgroup methods remain open.
- The Synthea executable identity, configuration, seed, population, FHIR output, Commons workflow layer, and known truth are not yet built.
- FHIR R4 and CDS Hooks records are planned teaching shapes, not reviewed conformance artifacts.
- No patient, workflow, burden, silent-failure, prospective-utility, or deployment evidence exists yet.
- Named human and independent reproduction reviews remain pending before alpha.

Module 01 is complete for curriculum construction. Module 02 must freeze this 29-file immutable handoff, preserve the 16 source identities and every authority limit, build the first versioned synthetic source layer, and specify logic and input availability without fitting the Module 03 model early.

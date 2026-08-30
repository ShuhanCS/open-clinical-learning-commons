# APP-3 Module 01: Framing a clinical performance and improvement decision

## 1. Module identity, duration, prerequisites, and place in the course

- Course: APP-3, Data for Clinical Performance and Improvement.
- Module ID: `oclc-app3-01`.
- Title: Framing a clinical performance and improvement decision.
- Course week: 1.
- Learner time: 15.5 hours.
- Module version: `0.1.0`.
- Commons release: `0.66.0`.
- Package path: `courses/clinical-performance-improvement/modules/01-clinical-performance-decision/`.
- Primary deliverable: clinical performance and improvement decision charter.
- Course points awarded here: 0.
- Week 3 handoff: Module 02 owns the 20-point measure build and Module 03 owns the 20-point performance diagnostic.

This module fixes the service decision before learners calculate a local rate, construct a dashboard, diagnose a bottleneck, forecast demand, or propose a change. It converts a broad wish to improve emergency-service performance into a fictional service, one unit moving through that service, a process boundary, a set of measure families, accepted evidence roles, accountable people, prohibited claims, and one feasible next analytic action.

### Prerequisites

Learners must be able to:

- identify a table grain and primary key;
- distinguish source fields from derived fields;
- inspect missing and unavailable values;
- explain a numerator and denominator in plain language;
- preserve a source fingerprint and transformation record;
- use a versioned workspace; and
- communicate a decision with an accessible exact table or simple process map.

APP-3 assumes those foundation skills and applies them to clinical performance, operational flow, safety, demand, capacity, and accountable improvement work.

## 2. Healthcare decision and named audience

The reference decision is:

> Are the service problem, unit of flow, source evidence, measure families, and accountable action defined well enough to build the local measurement system?

The decision owner is the fictional `CGH-ED-01` clinical performance and improvement council. The permitted next action is to build and validate local measure definitions from the fictional service event model in Module 02.

This is not a decision to change care, staffing, or workflow. It is a readiness decision about whether measure construction may begin.

### Primary audience

| Audience | What that audience must be able to decide |
|---|---|
| Clinical performance and improvement council | whether the decision is bounded enough to permit Module 02 measure construction |
| Emergency clinician reviewer | whether the unit, event states, safety language, and exclusions are clinically coherent |
| Nursing and frontline workflow reviewer | whether the process states are observable and whether future measurement could create burden |
| Patient and access representative | whether the measure families cover access, burden, and supported differences that matter to people receiving care |
| Data and measure steward | whether source identity, grain, unavailable values, lineage, and future field ownership are explicit |
| Safety and quality reviewer | whether error, near miss, adverse event, and harm can remain distinct in later modules |
| Workforce representative | whether staff workload and overtime are represented as balancing evidence rather than presumed solutions |
| Equity and privacy reviewer | whether subgroup use, support, and patient inference stay within governance boundaries |

Each audience has a decision right, not just a request for feedback. The stakeholder record must say who can require revision, who can stop unsafe or unsupported work, and who owns the next evidence.

## 3. Foundation skill being revisited or extended

### FND-1 extension

Learners reuse reproducible workspace setup, source fingerprints, relational grain, event identifiers, joins, missingness, quality checks, and transformation records. APP-3 changes the object of study: the central record is one synthetic adult emergency encounter moving through time and process states.

The extension requires learners to ask:

- what exactly enters the service;
- which event starts the clock;
- which states should occur and in what order;
- which event stops the clock;
- what happens when a state is absent, duplicated, or out of order;
- what denominator each future measure belongs to; and
- which failures are data-quality problems versus possible performance signals.

### FND-2 extension

Learners reuse estimands, temporal order, train and evaluation separation, uncertainty, model-purpose statements, and reproducibility. Module 01 does not fit a model. It prepares the decision contract that later forecasting and scenario work must honor.

The extension is from a technical prediction task to a service decision:

- prediction target becomes demand relevant to a named operating action;
- forecast horizon becomes the lead time available to the service;
- error costs become the consequences of over- and under-forecasting;
- model performance becomes one part of operational usefulness; and
- monitoring becomes a clinical and organizational responsibility.

### DA-730 use

Learners use accessible tables, exact labels, process maps, and decision-first writing. APP-3 does not reteach chart selection or general visualization theory. A future run chart, control chart, forecast display, or dashboard will be judged here for clinical performance meaning and decision use.

## 4. Learning outcomes that can be assessed

By the end of Module 01, a learner can:

1. state one bounded clinical performance decision in one sentence;
2. name one owner with authority to accept, revise, continue, or refer the work;
3. identify `CGH-ED-01` as fictional with no public hospital linkage;
4. define one synthetic adult emergency encounter as the unit of flow;
5. specify valid entry, intermediate, disposition, and exit states;
6. define the encounter clock and identify invalid temporal states;
7. separate service scope from pediatric, inpatient, public-ranking, staffing, and clinical-action scope;
8. distinguish outcome, process, balancing, safety, demand, capacity, workload, access, and equity measure families;
9. explain how numerator, denominator, unit, time window, and missingness affect a performance measure;
10. distinguish error, near miss, adverse event, and harm without collapsing them into one count;
11. explain why a public facility-measure aggregate cannot establish current local operations;
12. explain why a historical facility-week capacity field cannot establish a current staffing need;
13. audit all rows of each accepted public release rather than a convenience sample;
14. preserve blank, `Not Available`, footnoted, and `-999999` values as source evidence;
15. identify who bears measurement and improvement burden;
16. assign one owner and one next module to every unresolved evidence need;
17. mark claims as allowed, conditional, or prohibited;
18. disclose and verify any AI or agent assistance;
19. assemble a portable deterministic workspace;
20. defend a `continue`, `continue with conditions`, `revise`, or `refer` progression decision; and
21. explain why readiness points in this module are not course points.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 01 owns

- the exact readiness decision;
- the fictional service declaration;
- the unit moving through the service;
- the entry and exit states;
- the initial process boundary;
- the future operational table declaration;
- the accepted public source identities;
- public-source grain and feasibility interpretation;
- measure-family roles;
- stakeholder decision rights;
- responsible claim boundaries;
- AI and agent disclosure; and
- the Module 02 progression decision.

### Module 02 owns later

- synthetic encounter and process-event construction;
- field-level source and derived status;
- exact numerator and denominator logic;
- measure versioning;
- exclusions and missing-state rules;
- encounter conservation checks;
- valid local summary calculation; and
- the 20-point Week 3 measure component.

### Module 03 owns later

- process variation;
- control-chart eligibility and limits;
- safety signals;
- bottleneck diagnosis;
- alternative explanations;
- operational diagnostic evidence; and
- the 20-point Week 3 performance-diagnostic component.

### Later modules own

- Module 04: demand forecasting and capacity decisions;
- Module 05: improvement scenarios, counterfactual assumptions, and evaluation design;
- Module 06: feasibility, monitoring, and the embedded machine-learning extension; and
- Module 07: clinician-led recommendation, leadership, defense, and final disposition.

### Explicitly out of scope

Module 01 cannot:

- calculate a local `CGH-ED-01` performance rate;
- identify a current bottleneck;
- state that a public hospital performs well or poorly;
- copy a public facility identifier into synthetic data;
- infer a patient-level experience from a hospital aggregate;
- treat unavailable or sentinel values as zero;
- recommend staffing, scheduling, or workflow change;
- claim that a pattern caused harm;
- authorize clinical action or implementation;
- fit or deploy a model; or
- award course points.

## 6. Lesson sequence with estimated learner time

| Lesson | Topic | Hours | Learner evidence |
|---:|---|---:|---|
| 1 | Course case, decision owner, and fictional-service boundary | 1.0 | annotated decision statement |
| 2 | Unit of flow, event states, and encounter clock | 2.0 | unit-of-flow draft |
| 3 | Process boundary, scope, and failure branches | 1.5 | process-boundary draft |
| 4 | Performance measure families and accountable action | 2.0 | measure-family draft |
| 5 | Complete CMS timely-care source audit | 1.5 | source notes and unavailable-value audit |
| 6 | Complete CMS complications source audit | 1.5 | safety-source notes and claim limits |
| 7 | Complete HHS capacity snapshot and state extract audit | 2.0 | capacity feasibility interpretation |
| 8 | Stakeholder rights, burden, equity, privacy, and claims | 1.5 | accountability and claim records |
| 9 | Guided charter assembly and peer challenge | 1.0 | revised charter draft |
| 10 | Independent completion, validation, and defense | 1.5 | complete 25-file submission |
| **Total** |  | **15.5** |  |

The source audits use the complete accepted snapshots. Learners may explore the checked-in compressed files and profiles. Faculty reproducing the HHS state extract must supply the exact complete national CSV to `profile_sources.py`.

## 7. Authoritative readings and public clinical sources

### Required public sources

1. CMS Timely and Effective Care - Hospital:
   https://data.cms.gov/provider-data/dataset/yv7e-xc69
2. Complete accepted CMS timely-care CSV:
   https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv
3. CMS Complications and Deaths - Hospital:
   https://data.cms.gov/provider-data/dataset/ynj2-r877
4. Complete accepted CMS complications CSV:
   https://data.cms.gov/provider-data/sites/default/files/resources/6af7c44d77436e5a1caac3ce39a83fe9_1785189947/Complications_and_Deaths-Hospital.csv
5. CMS Complications and Deaths topic explanation:
   https://data.cms.gov/provider-data/topics/hospitals/complications-deaths/
6. CMS measures and current data-collection periods:
   https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods
7. HHS COVID-19 Reported Patient Impact and Hospital Capacity by Facility:
   https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u
8. Complete accepted HHS CSV endpoint:
   https://healthdata.gov/api/views/anag-cw7u/rows.csv?accessType=DOWNLOAD
9. HHS dataset metadata:
   https://healthdata.gov/api/views/anag-cw7u

### Reading purpose

Learners do not read the public data as a leaderboard. They use it to answer:

- What is the published measure called?
- What grain is reported?
- What population and period does the record represent?
- What values are unavailable or suppressed?
- Which measure concept could inform a future local definition?
- What local event fields would still be required?
- What claim remains impossible even after reading the source?

CMS method pages support measure meaning. The CSV releases support exact source auditing. HHS metadata supports field meaning, reporting history, and snapshot identity.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Source course document

The course source is `07-APP-3-Clinical-Performance-and-Improvement.docx`, 26,907 bytes, SHA-256 `084a412054c77169ea065cf15ed3cc7097e412a6017fbb58a260e909d17717e3`. Byte-identical copies appear in both supplied curriculum archives.

### CMS Timely and Effective Care

| Property | Accepted value |
|---|---|
| Dataset ID | `yv7e-xc69` |
| Accepted release date | 2026-08-13 |
| Grain | one facility-measure-period row |
| Rows | 138,084 |
| Columns | 16 |
| Facilities | 4,658 |
| Measures | 30 |
| States or reporting jurisdictions | 56 |
| Raw bytes | 34,150,899 |
| Raw SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |
| Repository artifact | complete deterministic gzip |
| Teaching purpose | measure definition, source support, unavailable values, flow, timeliness, and access concepts |

### CMS Complications and Deaths

| Property | Accepted value |
|---|---|
| Dataset ID | `ynj2-r877` |
| Accepted release date | 2026-08-13 |
| Grain | one facility-measure-period row |
| Rows | 95,800 |
| Columns | 18 |
| Facilities | 4,790 |
| Measures | 20 |
| States or reporting jurisdictions | 56 |
| Raw bytes | 22,963,267 |
| Raw SHA-256 | `26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d` |
| Repository artifact | complete deterministic gzip |
| Teaching purpose | safety, adverse-event, support, comparison-language, and unavailable-value concepts |

### HHS historical facility capacity

| Property | Accepted value |
|---|---|
| Dataset ID | `anag-cw7u` |
| Last update | 2024-05-03 |
| Grain | one facility-week row |
| Rows | 1,045,406 |
| Columns | 128 |
| Facilities | 5,172 |
| Weeks | 226 |
| Date range | 2019-12-29 through 2024-04-21 |
| Corrected false rows | 1,005,914 |
| Corrected true rows | 39,492 |
| Raw bytes | 481,497,539 |
| Raw SHA-256 | `b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f` |
| Repository artifact | all 15,179 Massachusetts rows and 24 decision-relevant columns |
| Teaching purpose | capacity, occupancy, coverage, correction, historical demand, and sentinel handling |

The full 481,497,539-byte HHS binary is not stored in Git. The exact URL, size, row count, column count, date range, facility count, week count, and SHA-256 are stored. The reproduction script refuses to create the Massachusetts artifact unless the supplied full CSV matches every pinned identity fact.

### Rights and data classes

The three sources are public United States government datasets. The package contains public facility-level aggregates and fictional service definitions. It contains no patient-level public records and no real local operational data.

Public access does not remove the need for responsible interpretation. Facility identifiers may remain in the public source artifacts, but they cannot be transferred into the fictional service layer or used for a Module 01 ranking.

## 9. Data dictionary and expected analytic structure

### Immutable source inventory

`data/source-inventory.csv` has one row per evidence layer and these fields:

| Field | Meaning |
|---|---|
| `source_id` | stable accepted source identifier |
| `title` | public dataset or declaration title |
| `publisher` | source authority |
| `grain` | what one row represents |
| `rows` | complete accepted row count |
| `columns` | complete accepted field count |
| `raw_bytes` | byte count before repository compression |
| `raw_sha256` | complete raw-source identity |
| `repository_artifact` | stored or declared teaching artifact |
| `teaching_role` | purpose in the module |
| `claim_limit` | interpretation that remains prohibited |

### Immutable measure-family anchors

`data/measure-family-anchors.csv` records ten facts:

- `EDV`, `OP_18b`, and `OP_22` from timely care;
- `PSI_90`, `PSI_04`, and `PSI_03` from complications; and
- inpatient beds, inpatient beds used, staffed adult ICU beds, and emergency visits from HHS capacity.

Every row includes source support, reported support, unavailable support, period, decision use, and the statement that the value does not describe `CGH-ED-01`.

### Immutable capacity profile

`data/capacity-source-profile.csv` has `CP01` through `CP20`. It records complete national snapshot identity, date coverage, correction status, Massachusetts extract identity, support for four relevant fields, and zero public patient-level rows.

### Unit of flow

`unit-of-flow.csv` has six ordered states:

1. recorded arrival;
2. triage;
3. roomed;
4. first clinician contact;
5. disposition decision; and
6. recorded departure.

Each state records clock status, required future fields, decision use, invalid or missing branch, and owner. The sequence is an instructional contract, not a claim that every emergency service uses the same workflow.

### Future operational table declaration

Module 01 declares but does not populate these Module 02 and later tables:

| Table | Future grain | Primary purpose |
|---|---|---|
| `encounters` | one synthetic emergency encounter | population, entry, exit, disposition, and encounter-level attributes |
| `process-events` | one recorded event per encounter-state-time | clocks, sequence, delay, completion, and missing states |
| `staffing` | one role and operating interval | available labor, skill mix, workload, and overtime |
| `queue-snapshots` | one queue and timestamp | work waiting, work in service, and congestion |
| `safety-events` | one synthetic event | error, near miss, adverse event, harm, detection, and review state |
| `calendar-demand` | one operating interval | arrivals, seasonality, special periods, and forecast features |
| `scenarios` | one predeclared change and evaluation unit | assumptions, resource changes, outcomes, and balancing consequences |
| `known-truth` | one generated parameter or mechanism | synthetic provenance and recovery checks |

No operational result is present in Module 01.

## 10. Worked example and instructor walkthrough

### Starting prompt

An executive says, "The emergency department is too slow. We should add staff."

The instructor asks learners to identify what is missing:

- no bounded service;
- no unit moving through it;
- no entry or exit;
- no population;
- no measure family;
- no evidence about demand or capacity;
- no accountable decision owner;
- no balancing or safety consequence;
- no distinction between public context and local operations; and
- a proposed solution before diagnosis.

### Walkthrough

1. Replace the real-world sounding service with the explicitly fictional `CGH-ED-01` adult emergency service.
2. Define one synthetic adult emergency encounter as the unit of flow.
3. Start the clock at the first valid recorded arrival and stop it at departure after a documented disposition.
4. Record triage, rooming, first clinician contact, disposition, and departure as states whose order can be checked.
5. Separate total visit duration from stage delay.
6. Place left-before-seen in access and balancing, not as proof of cause.
7. Place safety events in their own family with distinct error, near miss, adverse event, and harm concepts.
8. Place staffing hours and overtime in workload and balancing rather than treating staffing as the answer.
9. Use CMS and HHS records to learn how public measures and unavailable values are represented.
10. State that those public values are not observations from `CGH-ED-01`.
11. Assign Module 02 the next action: construct and validate local measure definitions.

### Correct reference interpretation

The module can continue with conditions because the decision, source identities, unit, boundary, measure families, owners, and claim limits are complete. It cannot diagnose delay, identify a bottleneck, recommend staff, compare hospitals, or authorize implementation.

### Source arithmetic learners must explain

- Timely care has 138,084 rows across 30 measure IDs. `OP_18b` has 4,081 reported and 577 unavailable scores, totaling 4,658 facility rows.
- Complications has 95,800 rows across 20 measure IDs. `PSI_90` has 2,908 reported and 1,882 unavailable scores, totaling 4,790 facility rows.
- HHS capacity has 1,045,406 national rows. The repository extract has 15,179 Massachusetts rows. For `previous_day_total_ED_visits_7_day_sum`, 10,909 are reported after blanks and `-999999` are excluded from the reported count, leaving 4,270 unavailable or sentinel rows.

These counts establish source support. They are not performance results for the fictional service.

## 11. Guided practice

### Practice A: decision repair

Learners receive five vague statements such as "reduce wait time" or "improve safety." For each statement they must add:

- service;
- population;
- unit of flow;
- entry;
- exit;
- accountable owner;
- permitted next action; and
- prohibited action.

### Practice B: event-state audit

Learners review encounter-state examples with:

- duplicate arrivals;
- triage before arrival;
- clinician contact before rooming;
- missing disposition;
- departure before arrival;
- transfer with no departure; and
- a completed encounter.

They classify each example as valid, invalid, unresolved, or requiring a named rule. They do not calculate duration from an invalid sequence.

### Practice C: measure-family sorting

Learners sort proposed measures into outcome, process, balancing, safety, demand, capacity, workload, access, and equity. They must explain why one measure can inform more than one decision but still needs one primary role in the release.

### Practice D: source feasibility

Learners answer these questions for each complete source:

1. What does one row represent?
2. What is the complete row count?
3. What is the accepted identity?
4. Which unavailable values appear?
5. Which concept is useful for the future local measure system?
6. Which local fields remain missing?
7. Which claim stays prohibited?

### Practice E: stakeholder challenge

Pairs exchange charters. One learner acts as the decision owner and the other as the patient/access, workforce, safety, or data reviewer. The reviewer must identify one unresolved evidence need, one burden, and one stop condition.

## 12. Independent exercise

The learner independently completes the ten editable records.

### Required decisions

1. Write the readiness decision in one sentence.
2. Name one owner and one permitted next action.
3. Declare the service fictional and disjoint from public facilities.
4. Define the unit of flow.
5. Define entry, exit, clocks, and failure branches.
6. Mark included and excluded service scope.
7. Define at least seven required measure roles.
8. Interpret all three accepted public sources.
9. Preserve missing, unavailable, footnoted, corrected, and sentinel states.
10. Assign stakeholder rights and evidence owners.
11. Mark claims as allowed, conditional, or prohibited.
12. Disclose any AI or agent use.
13. Score readiness and record all gates.
14. Choose one allowed progression value.

### Independent defense questions

- Why is encounter the unit rather than patient, facility, day, or event?
- Which state starts and stops the clock?
- What would make a duration invalid?
- Why does `OP_18b` not define the local clock by itself?
- Why can `OP_22` motivate an access measure but not explain why a person left?
- Why do PSI records not detect a current local safety event?
- Why can a historical capacity field not establish present staffing need?
- Which balancing measure could stop a later scenario?
- Who can require revision?
- What exact evidence gives Module 02 permission to begin?

## 13. Visualization and communication requirements

Module 01 requires communication that clarifies the decision without implying a result.

### Required displays

1. One accessible ordered process table or simple process map showing arrival through departure.
2. One exact source-feasibility table comparing the three public sources by grain, rows, time coverage, role, and claim limit.
3. One accountability table showing decision right, evidence need, burden or power, engagement point, and unresolved question.

### Display rules

- Lead with the decision and why it matters.
- Use exact units and dates.
- Label unavailable and sentinel values plainly.
- Do not use color alone to encode inclusion, exclusion, status, or risk.
- Give every table a descriptive title and column labels.
- Preserve reading order in documents.
- Do not draw a performance trend, control chart, ranking, forecast, or scenario result.
- Do not place a public facility next to `CGH-ED-01` in a way that implies equivalence.

The decision charter begins with what the council needs to decide. Source methods support that decision rather than becoming the story.

## 14. Exact submission package and filenames

The assembled workspace contains exactly 25 files:

```text
.gitattributes
VERSION
assessment.md
data-spec.md
decision-contract.json
profile_sources.py
source-record.yml
validate_workspace.py
release-manifest.csv
data/
  capacity-source-profile.csv
  measure-family-anchors.csv
  source-inventory.csv
  raw/
    Complications_and_Deaths-Hospital.csv.gz
    HHS-Capacity-Massachusetts.csv.gz
    Timely_and_Effective_Care-Hospital.csv.gz
clinical-performance-charter.md
synthetic-service-declaration.md
unit-of-flow.csv
process-boundary.csv
measure-family.csv
source-feasibility-interpretation.md
stakeholder-accountability-map.csv
claim-boundary.csv
ai-use.md
progression-decision.md
```

The 14 immutable files appear in `release-manifest.csv`. The ten learner records remain editable. The manifest itself is generated after the immutable files are copied.

### Build commands

```powershell
cd courses/clinical-performance-improvement/modules/01-clinical-performance-decision
python build_workspace.py --target "$env:TEMP\app3-module01-learner"
python validate_workspace.py "$env:TEMP\app3-module01-learner" --starter
```

### Reference commands

```powershell
python build_workspace.py --target "$env:TEMP\app3-module01-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module01-reference"
```

The builder refuses to overwrite an existing target.

## 15. Rubric and pass conditions

Module 01 uses 20 readiness points. These points do not enter the 100-point course total.

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Decision, owner, and bounded next action | 4 | exact readiness decision, one accountable owner, one Module 02 action, and no clinical action |
| Unit of flow and process boundary | 4 | six ordered states, entry, exit, clock status, failure branches, and explicit exclusions |
| Measure families and source roles | 4 | required roles, unit, denominator or base, public anchor, future local source, decision use, and claim limit |
| Accountability and responsible claims | 4 | stakeholder rights, affected groups, burden, owners, and allowed or prohibited claims |
| Reproducibility and progression | 4 | exact source identities, manifest, AI record, gates, owned conditions, and allowed progression |
| **Total** | **20** | **16 or more plus every noncompensable gate** |

### Noncompensable gates

1. Fictional service declared.
2. One synthetic adult emergency encounter is the unit of flow.
3. Public and local evidence grains remain separate.
4. Three complete public source identities are pinned.
5. Unavailable and sentinel values remain visible.
6. Entry, exit, clocks, and exclusions are defined.
7. Required measure families are represented.
8. Decision owner and next action are named.
9. No bottleneck diagnosis appears.
10. No staffing proposal or clinical action appears.
11. No hospital ranking, causal, or public-to-synthetic linkage claim appears.
12. The package is complete, portable, disclosed, and reproducible.

A readiness score cannot compensate for a failed gate. A condition can remain open only when it has an owner, due point, evidence requirement, and escalation trigger.

## 16. Common errors, failure modes, and instructor interventions

| Error | Why it matters | Instructor response |
|---|---|---|
| "The ED is slow" without a unit or clock | no reproducible performance measure can follow | require entry, exit, unit, and invalid-state rules |
| naming a staffing solution in the problem statement | the answer precedes diagnosis | replace it with the permitted Module 02 construction action |
| treating a public facility as the fictional service | creates false attribution | remove the linkage and restate the synthetic declaration |
| reading `Not Available` as zero | changes missing evidence into a performance result | restore the source value and classify availability |
| reading `-999999` as a measured negative count | converts a sentinel into data | preserve the sentinel and exclude it only from reported support |
| using patient as the grain for facility aggregates | invites patient inference | restate the public facility-measure or facility-week grain |
| using `OP_18b` as the complete local measure specification | public label does not define local event logic | require local entry, exit, exclusions, and source fields in Module 02 |
| calling any safety count "harm" | error, near miss, adverse event, and harm are not interchangeable | require separate concepts and owners |
| leaving burden only to leadership | frontline and patient consequences disappear | add patient/access, workforce, nursing, and equity rights |
| ranking hospitals | the module has no approved comparison design | mark the claim prohibited |
| adding readiness points to course points | corrupts the 40/25/35 assessment plan | keep course points at zero here |
| allowing `continue` with a failed gate | bypasses the readiness contract | change progression to revise or refer |

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

- Tables have descriptive headings and a logical reading order.
- Status is written in text rather than color alone.
- Dates and units are explicit.
- Process states are numbered.
- Acronyms are expanded on first use.
- Source URLs remain complete and usable.
- Plain-language interpretation precedes technical details.

### Equity

The module requires an equity and supported-access measure family but does not invent unsupported subgroup results. Learners must state:

- which subgroup fields could exist in the fictional event model;
- why collection, support, privacy, and governance matter;
- which differences would be meaningful to the decision;
- when sparse support requires aggregation, suppression, revision, or referral; and
- who can stop an unsupported disparity claim.

Aggregate improvement cannot be treated as equitable improvement without supported subgroup evidence. Module 01 records the requirement; later modules test it.

### Privacy

The public files are facility-level aggregates. The future local case is synthetic. Learners may not introduce real patient data, restricted local data, or re-identification attempts. They may not infer patient characteristics from public hospital values.

### Responsible claims

Allowed claims describe source identity, grain, support, measure meaning, fictional-service status, and readiness. Prohibited claims include:

- current local performance;
- named-hospital quality judgment;
- public-to-synthetic equivalence;
- current staffing need;
- causal explanation;
- clinical benefit;
- patient-level experience; and
- implementation authority.

## 18. AI and agent policy, required disclosure, and verification

AI or agents may help:

- explain terminology;
- inspect file structure;
- summarize a public data dictionary;
- suggest missing stakeholders or measure families;
- challenge a decision statement;
- check schema consistency;
- edit prose; and
- run deterministic validation.

AI or agents may not:

- decide the clinical recommendation;
- invent public-source facts;
- treat inaccessible data as inspected;
- link `CGH-ED-01` to a public hospital;
- convert missing or sentinel values into observed results;
- infer patient-level facts;
- authorize staffing, care, or implementation; or
- replace required human review.

`ai-use.md` must record tool and model, date, purpose, prompt or task, data classes shared, files affected, whether output was used or changed, material claim, independent verification, correction or retained action, human owner, and accountability statement.

Material numeric and source claims require deterministic verification against the accepted files. A fluent explanation is not evidence of source inspection.

## 19. Answer key and instructor notes

### Reference answer summary

- Service: `CGH-ED-01`.
- Status: fictional adult emergency service.
- Unit: one synthetic adult emergency encounter.
- Entry: first valid recorded arrival.
- Exit: recorded departure after disposition.
- Decision owner: `CGH-ED-01` clinical performance and improvement council.
- Decision: whether the problem, unit, source evidence, measure families, and accountable action are defined enough for local measure construction.
- Next action: Module 02 measure construction and validation.
- Progression: `continue with conditions`.
- Module 02 permission: `permitted for curriculum construction`.
- Operational diagnosis: prohibited.
- Staffing change: prohibited.
- Clinical action: prohibited.
- Hospital ranking: prohibited.
- Public-to-synthetic linkage: prohibited.

### Required open conditions

1. Instantiate every declared event state.
2. Write exact numerator, denominator, exclusion, and missingness logic.
3. Keep public and synthetic identifiers disjoint.
4. Conserve encounter denominators across every branch.
5. Preserve safety event concepts separately.
6. Define supported subgroup and burden checks.
7. Retain the no-diagnosis and no-action boundary through Module 02.

### Instructor judgment

Accept different wording when it preserves the same decision, service boundary, evidence roles, ownership, and prohibited claims. Do not accept a more detailed answer if that detail silently advances into diagnosis or action.

The HHS full source is intentionally external because the accepted CSV is 481,497,539 bytes. The repository artifact is not a convenience sample: it contains every Massachusetts row and can be reproduced only after complete-source identity validation.

## 20. Runnable acceptance checks for data, code, links, and expected findings

### Source checks

`profile_sources.py` must verify:

- complete CMS timely raw bytes, SHA-256, header, 138,084 rows, 4,658 facilities, 30 measures, and 56 jurisdictions;
- complete CMS complications raw bytes, SHA-256, header, 95,800 rows, 4,790 facilities, 20 measures, and 56 jurisdictions;
- committed HHS Massachusetts gzip header, 15,179 rows, 74 facilities, 214 state weeks, 24 fields, and decompressed SHA-256;
- capacity profile linkage to the complete HHS 1,045,406-row fingerprint; and
- rejection of a changed CMS source.

With all three complete raw CSVs supplied under `--write`, it must also verify:

- exact HHS complete bytes and SHA-256;
- 128 fields;
- 5,172 facilities;
- 226 national weeks;
- 2019-12-29 through 2024-04-21 range;
- 39,492 corrected rows;
- 1,005,914 uncorrected rows; and
- deterministic reproduction of the all-row Massachusetts artifact.

### Builder checks

`build_workspace.py --self-check` must prove:

- 14 immutable manifest rows;
- 10 editable records;
- 25 assembled files;
- deterministic manifests across two independent reference builds;
- explicit learner placeholders; and
- refusal to overwrite an existing target.

### Validator checks

`validate_workspace.py --self-check` must validate complete and starter modes and reject:

- a completed-source mutation;
- a missing required record;
- an invalid progression value;
- a staffing recommendation; and
- an incomplete starter presented as complete.

The reference package must pass 177 complete checks. The starter must pass 133 structural checks.

### Link checks

The full CMS dataset pages, CMS method pages, HHS dataset page, HHS full CSV endpoint, and HHS metadata endpoint must remain present as complete URLs. Link availability is checked at release review; a later upstream update does not silently replace the accepted fingerprints.

### Expected findings

The accepted findings are source and readiness facts only:

- the timely source is complete and contains substantial unavailable support;
- the complications source is complete and contains substantial unavailable support;
- the HHS source is historical, large, corrected in some rows, and contains blank or sentinel values;
- all three sources can orient measure families;
- none describes local `CGH-ED-01` operations;
- the fictional service and process boundary are complete enough for measure construction; and
- progression is conditional and authorizes no operational or clinical action.

## 21. Release status, reviewers, version, and known issues

### Release decision

- Module version: `0.1.0`.
- Commons release: `0.66.0`.
- Status: runnable release candidate.
- Reference readiness score: `20.00 of 20.00`.
- Reference progression: `continue with conditions`.
- Module 02 permission: `permitted for curriculum construction`.
- Course points awarded here: 0.

### Required review coverage before alpha

- APP-3 faculty owner;
- emergency clinician;
- quality and safety;
- operations and workflow;
- nursing and frontline practice;
- patient and access;
- workforce;
- equity and privacy;
- data engineering and measure stewardship;
- accessibility;
- responsible AI; and
- independent instructor.

Joe Joseph, MD, SFHM, is the named clinician for Module 07. His direct participation and final role wording remain pending. Module 01 does not imply his review or endorsement.

### Known issues

- The official APP-3 section and half-term dates remain to be assigned from the academic calendar.
- The HHS full national binary is not stored in Git because it is 481,497,539 bytes; exact reproduction requires reacquiring the pinned accepted source.
- Public source links can later point to newer releases, so accepted fingerprints remain authoritative for this version.
- The future synthetic operational generator, safety-event design, subgroup support, staffing assumptions, and workload language require human review before alpha.
- No local operational result, bottleneck, forecast, scenario, or implementation recommendation exists yet.

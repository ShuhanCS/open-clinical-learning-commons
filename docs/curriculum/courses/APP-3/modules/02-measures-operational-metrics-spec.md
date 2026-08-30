# APP-3 Module 02: Measures and operational metrics

## 1. Module identity, decision, and release boundary

- Module ID: `oclc-app3-02`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Instructional week: 2.
- Student effort: 16.0 hours.
- Submission: 20-point measure and operational metric build.
- Module version: `0.1.0`.
- Commons release: `0.67.0`.
- Package: `courses/clinical-performance-improvement/modules/02-measures-operational-metrics/`.
- Decision: whether measure logic and linked operational tables are valid enough to diagnose performance over time.
- Primary decision owner: `CGH-ED-01 clinical performance and improvement council`.
- Progression decision: `continue`, `continue with conditions`, `revise`, or `refer`.

The module answers a practical question before any process diagnosis begins: can the council trust how each measure was built? A passing release has exact populations, clocks, joins, repairs, unavailable states, refresh rules, and owners. It also preserves enough uncertainty for Module 03 to test variation and bottleneck evidence honestly.

This is a measure release, not an operational recommendation. It cannot name the service bottleneck, attribute cause, recommend staffing, direct clinical care, or authorize implementation.

## 2. Place in the course and prerequisite handoff

Module 01 supplies ten frozen records and seven owned conditions. Module 02 must not reopen the fictional service, public-source boundary, unit of flow, or process scope simply to improve a result.

### Required Module 01 identity

- Service: `CGH-ED-01`.
- Status: fictional adult emergency service.
- Unit of flow: one synthetic adult emergency encounter.
- Entry: first valid recorded arrival.
- Exit: recorded departure after disposition, with declared failure branches.
- Public relationship: no public hospital linkage.
- Decision owner: `CGH-ED-01 clinical performance and improvement council`.
- Module 02 permission: `permitted for curriculum construction`.

### Seven owned handoff conditions

1. Instantiate every declared event state.
2. Write exact numerator, denominator, exclusion, and missingness logic.
3. Keep public and synthetic identifiers disjoint.
4. Conserve encounter denominators across every branch.
5. Preserve safety event concepts separately.
6. Define supported subgroup and burden checks.
7. Retain the no-diagnosis and no-action boundary through Module 02.

`freeze_upstream.py` copies the accepted Module 01 artifacts and writes a deterministic handoff manifest. A changed upstream file must fail validation rather than silently changing the measure release.

## 3. Learning outcomes

By the end of the module, learners can:

1. define a measure with an exact numerator or summary, denominator or population, exclusions, unit, direction, clock, attribution, window, refresh cadence, owner, threshold origin, unavailable state, and interpretation limit;
2. distinguish counts, rates, ratios, durations, snapshots, totals, and diagnostic performance measures;
3. link encounter, event, staffing, queue, safety, and demand tables without changing their grain;
4. validate event order before calculating time;
5. preserve an immutable raw layer while applying declared clean-layer rules;
6. show how each data defect changes at least one measure or invariant;
7. conserve encounters, queue arithmetic, and staffing intervals;
8. separate error, near miss, adverse event, and harm;
9. calculate synthetic trigger sensitivity, incident capture, and specificity from known truth;
10. publish support and unavailable states for every subgroup comparison;
11. use SQL for linked measure logic and Python for independent reproduction;
12. explain what generated operational values do and do not support; and
13. issue a progression decision without crossing into diagnosis or action.

## 4. Concept ownership and boundaries

### Module 02 owns

- operational measure specification;
- numerator, denominator, exclusion, and population logic;
- event-clock eligibility;
- encounter and shift attribution;
- unavailable-state treatment;
- raw-to-clean repair rules;
- linked SQL construction;
- Python reproduction and exact checks;
- cycle time, wait, throughput, queue, utilization, staffing-hour, safety-detection, and subgroup-support measures;
- defect impact records;
- measure release scoring and gates; and
- permission for Module 03 to begin.

### Module 02 extends rather than repeats

- FND-1 descriptive summaries by tying each summary to a clinical-performance decision;
- FND-2 joins and missingness by testing event order, conservation, and unavailable clocks;
- DA-730 rates, denominators, uncertainty, and accessible communication by applying them to linked operational grain; and
- Module 01 measure families by turning family requirements into executable definitions.

### Out of scope

- control-chart selection and limits;
- common-cause or special-cause interpretation;
- bottleneck diagnosis;
- demand forecasting;
- Little's Law inference;
- scenario simulation;
- improvement effect estimation;
- staffing recommendations;
- workflow redesign recommendations;
- clinical action;
- causal claims;
- machine-learning fitting;
- implementation planning; and
- public hospital ranking or linkage.

Module 03 owns variation, safety signals, and bounded bottleneck diagnosis. Later modules own forecasting, scenarios, feasibility, machine learning, and clinician leadership.

## 5. Continuing evidence thread and source authority

### Public concept anchors

Module 01 pins the complete CMS Timely and Effective Care and Complications and Deaths releases and the complete HHS historical capacity identity. Their official dataset pages are:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

https://data.cms.gov/provider-data/dataset/ynj2-r877

https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u

These releases teach how public measures express time, availability, safety, facility grain, and reporting coverage. They do not provide local encounter, event, queue, staffing, or safety-candidate rows for `CGH-ED-01`.

### Local teaching evidence

The linked operational source is generated, not sampled from a public hospital. Its identity is:

| Item | Accepted value |
|---|---|
| Release | `cgh-ed-01-operational-v1` |
| Generator | `generate_operational_release.py` version `0.1.0` |
| Seed | `73002` |
| First arrival date | 2024-01-01 |
| Last arrival date | 2024-12-29 |
| Weeks | 52 |
| Arrival shifts | 1,092 |
| Raw tables | 9 |
| Raw rows | 318,732 |
| Synthetic flag | 1 on every accepted row |

`data/operational-source-manifest.csv` is the accepted source identity. `data/data-dictionary.csv` defines 117 fields across the nine tables. The manifest records row counts, columns, decompressed bytes, decompressed SHA-256, gzip bytes, gzip SHA-256, generator version, seed, and synthetic status.

The generated known-truth file supports curriculum checks. Learners do not use later disclosed bottleneck or scenario truth to construct a favorable result in Module 02.

## 6. Synthetic operational release contract

| Table | Grain | Rows | Module 02 role |
|---|---|---:|---|
| encounters | one raw encounter row plus one seeded duplicate | 43,631 | accepted adult population, dispositions, returns |
| process-events | one recorded state per encounter and time | 250,821 | event order and durations |
| staffing | one synthetic role per arrival shift | 4,368 | valid hours and descriptive ratios |
| queue-snapshots | one service queue per 30-minute interval | 17,520 | queue conservation and length |
| safety-events | one true event or reviewed non-event candidate | 1,274 | detection and capture diagnostics |
| calendar-demand | one arrival shift | 1,092 | accepted arrival reconciliation |
| scenarios | one predeclared scenario without results | 4 | later boundary only |
| known-truth | one generated mechanism or null condition | 10 | validation and later recovery |
| defect-register | one seeded raw defect | 12 | repair audit |

Relationships use stable synthetic identifiers. Encounter IDs connect event and safety rows. Arrival shift IDs connect encounters, staffing, queue, and calendar demand. Person tokens support return linkage but cannot be treated as real identities.

### Required raw-layer properties

- deterministic gzip with a fixed timestamp;
- unchanged accepted raw files;
- explicit synthetic flag;
- no public provider identifier;
- no real patient, clinician, staff, or hospital record;
- declared missing meanings;
- stable source fingerprint; and
- a defect register that names every intentional defect.

### Required clean-layer properties

- one accepted adult encounter per stable encounter ID;
- no public-like service identifier;
- no encounter under age 18;
- no impossible accepted arrival and departure order;
- one stable event per encounter and event type;
- no event or safety orphan;
- conserved queue arithmetic;
- valid nonnegative staffing hours;
- calendar arrivals derived from accepted encounters;
- separate safety classes; and
- scenario results absent.

## 7. Measure specification contract

Every measure row must contain all 17 fields in `measure-specifications.csv`:

1. stable measure ID;
2. plain-language name;
3. family;
4. type;
5. unit;
6. direction;
7. numerator or summary rule;
8. denominator or population;
9. exclusions;
10. event clock;
11. attribution;
12. reporting window;
13. refresh cadence;
14. accountable owner;
15. threshold origin;
16. unavailable state; and
17. interpretation limit.

The accepted reference defines 17 measures:

| ID | Measure | Family | Unit |
|---|---|---|---|
| M01 | Accepted arrivals | demand | encounters |
| M02 | Arrival to triage | access | minutes |
| M03 | Arrival to clinician | access | minutes |
| M04 | Arrival to departure | flow | minutes |
| M05 | Left before seen | balancing | percent |
| M06 | Return within 72 hours | outcome | percent |
| M07 | Process completion | process | percent |
| M08 | Valid event sequence | data quality | percent |
| M09 | Safety event candidate rate | safety | events per 1,000 completed encounters |
| M10 | Trigger sensitivity | safety | percent |
| M11 | Incident capture sensitivity | safety | percent |
| M12 | Completed throughput | flow | encounters |
| M13 | Queue end | flow | encounters waiting |
| M14 | Clinician staff hours per arrival | capacity | hours per encounter |
| M15 | Throughput per clinician hour | capacity | completed encounters per hour |
| M16 | Overtime hours | workforce | hours |
| M17 | Supported access-group stratification | equity | encounters |

A label such as "wait time" is not a measure specification. The learner must state which events start and stop time, which records can enter, which missing states suppress a duration, and who owns the release.

## 8. Event model, clocks, and denominator conservation

The nominal event order is:

1. arrival;
2. triage;
3. roomed;
4. clinician;
5. disposition; and
6. departure.

Not every accepted encounter uses every state. A left-before-seen encounter can end without clinician contact. The clock must be unavailable rather than zero. One seeded encounter has a missing clinician event and remains accepted, producing one invalid full sequence and one explicitly unavailable clinician clock beyond the left-before-seen branch.

The accepted encounter reconciliation is:

```text
39,975 completed encounters
+ 3,653 left before seen
= 43,628 accepted adult encounters
```

The clean layer has 43,627 valid event sequences and 39,974 available clinician times. Duration calculations must never use a negative or invalid clock.

Queue conservation is checked at every 30-minute interval:

```text
queue_end = queue_start + arrivals - exits
```

Staffing records must connect to a declared arrival shift. Actual staff hours cannot be negative. Ratio denominators of zero or unavailable hours return an unavailable measure rather than infinity or zero.

## 9. Defect and repair curriculum

The raw release contains 12 deliberate defects. Each one exercises a different measurement failure.

| ID | Defect | Required clean disposition | Required effect |
|---|---|---|---|
| D001 | duplicate encounter row | deduplicate | accepted denominator changes |
| D002 | missing encounter arrival | recover from unique arrival event | arrival clocks become available |
| D003 | public-like service identifier | quarantine | fictional-service denominator changes |
| D004 | underage encounter | quarantine | adult denominator changes |
| D005 | departure before arrival | recover from unique departure event | visit duration becomes valid |
| D006 | duplicate process event | deduplicate | event count changes |
| D007 | swapped triage and rooming times | repair with declared sequence | event sequence becomes valid |
| D008 | missing clinician event | retain unavailable | clinician-time support decreases |
| D009 | negative queue end | recalculate by conservation | queue becomes valid |
| D010 | negative actual staff hours | reconstruct from declared inputs | staffing ratios become valid |
| D011 | duplicate safety candidate | deduplicate | safety candidate count changes |
| D012 | calendar and encounter arrival mismatch | derive from accepted encounters | shift demand changes |

Raw evidence is never edited. SQL implements the clean rule. `defect-repair-log.csv` names the disposition, measure effect, owner, and status. `outputs/defect-impact.csv` proves the expected raw-to-clean change.

Learners may propose another deterministic clean rule only if it preserves the declared population, explains the decision consequence, and reproduces every required invariant. Convenience is not enough reason to discard a row.

## 10. SQL and Python division of responsibility

SQL owns linked operational logic because the relationships and populations must be visible in one executable sequence.

### SQL 01: clean operational sources

- load accepted raw tables;
- deduplicate stable keys;
- quarantine invalid service and population rows;
- recover only declared clocks;
- retain unavailable states;
- reconstruct queue and staffing values; and
- create indexed clean tables.

### SQL 02: encounter measures

- pivot event types into encounter clocks;
- validate event order;
- calculate supported durations;
- preserve left-before-seen and completed branches;
- attach return and subgroup support; and
- produce one accepted encounter row.

### SQL 03: operational measures

- build shift measures;
- build weekly measures;
- calculate safety diagnostics;
- calculate subgroup support; and
- retain numerators, denominators, and unavailable counts.

### SQL 04: validation and defects

- reconcile raw and clean row counts;
- record all 12 defect effects; and
- run 30 exact query checks.

Python independently loads the nine sources into SQLite, registers a deterministic median aggregate, runs the ordered SQL, writes eight outputs, writes one build report, verifies SHA-256 identities, rejects a nonempty output target, and reproduces the release twice in self-check mode.

This division is intentional. Python does not hide the denominator logic, and SQL does not certify its own output without an independent build path.

## 11. Instructional sequence and 16-hour workload

| Block | Hours | Learner work | Evidence |
|---|---:|---|---|
| Measure purpose and family review | 1.5 | connect Module 01 families to decisions | draft measure list |
| Numerator, denominator, unit, and direction | 2.0 | repair incomplete measure statements | measure specifications |
| Event clocks and linked grain | 2.0 | audit state order and attribution | event validation |
| Raw-to-clean SQL | 3.0 | implement repairs without changing raw data | SQL 01 and defect log |
| Encounter and operational SQL | 3.0 | build encounter, shift, weekly, safety, and subgroup layers | SQL 02 and 03 |
| Python reproduction and failure checks | 2.0 | reproduce outputs and inspect query checks | SQL 04 and build report |
| Interpretation and subgroup support | 1.0 | state findings and claim limits | two interpretation records |
| Scoring, defense, and progression | 1.5 | score gates and defend Module 03 permission | score, gates, AI record, progression |
| **Total** | **16.0** |  |  |

The work is technical throughout. It revisits fundamentals through operational events, denominators, missing states, and linked tables rather than repeating a general statistics sequence.

## 12. Guided practice and independent exercise

### Guided practice A: complete the measure

Learners receive statements such as "reduce wait," "improve safety," and "increase throughput." They add a population, numerator or summary, denominator, unit, clock, direction, unavailable state, owner, and interpretation limit.

### Guided practice B: clock eligibility

Learners classify seven event examples:

- complete ordered encounter;
- left before seen;
- missing clinician event;
- duplicated triage event;
- triage before arrival;
- departure before arrival; and
- disposition with no departure.

They decide whether each record is eligible for arrival-to-triage, arrival-to-clinician, and arrival-to-departure. They do not replace unavailable time with zero.

### Guided practice C: repair audit

For each seeded defect, learners answer:

1. What is visible in raw data?
2. Which clean rule is predeclared?
3. Is the disposition repair, quarantine, deduplicate, or retain unavailable?
4. Which measure or invariant changes?
5. Who owns the rule?
6. What would make the rule unsafe?

### Guided practice D: safety detection

Learners separate generated truth, triggers, incident reports, reviewed non-events, and safety class. They calculate true positives, false positives, sensitivity, capture, and specificity. They explain why incident-report counts are not prevalence.

### Guided practice E: subgroup support

Learners compare eligible counts and unavailable clocks before reading a difference. A group below the declared teaching threshold cannot support the planned comparison without aggregation, suppression, revision, or referral.

### Independent exercise

Learners complete four SQL files and ten learner records. They reproduce every output, explain all 12 defect effects, score the 20-point build, pass 15 gates, and defend one progression value.

Defense questions include:

- Why is the denominator 43,628 rather than 43,631?
- Why does D008 stay in the accepted population?
- Why is a missing clinician clock unavailable rather than zero?
- Which branch conserves completed and left-before-seen encounters?
- Why can trigger sensitivity be calculated here but not transferred to a real hospital?
- What makes a staff-hour ratio descriptive rather than a staffing target?
- Why does subgroup support not prove equity or inequity?
- Which evidence permits Module 03 to begin?
- Which claims remain prohibited after a perfect score?

## 13. Expected findings and responsible interpretation

The accepted reference build produces these exact findings:

| Finding | Accepted value |
|---|---:|
| Accepted encounters | 43,628 |
| Completed encounters | 39,975 |
| Left before seen | 3,653 |
| Valid event sequences | 43,627 |
| Clinician times available | 39,974 |
| Median arrival to triage | 13 minutes |
| Median arrival to clinician | 98 minutes |
| Median arrival to departure | 304 minutes |
| Shift rows | 1,092 |
| Weekly rows | 52 |
| Total overtime | 1,050 hours |
| Maximum conserved queue end | 20 |
| Generated true safety events | 894 |
| Trigger sensitivity | 75.2796 percent |
| Incident capture | 40.0447 percent |
| Trigger specificity | 99.0302 percent |
| Query checks | 30 of 30 pass |

The accepted access-support counts are:

- language support: 6,032 encounters;
- mobility support: 3,498 encounters; and
- standard: 34,098 encounters.

All three clear the teaching threshold of 1,000 accepted encounters. Their generated results can enter Module 03 with denominators and unavailable states attached.

These findings prove construction and support only. A median does not identify a delayed stage. A queue maximum does not identify its cause. Overtime does not prove burden or a staffing need. Trigger performance does not establish real event prevalence. A generated subgroup difference does not prove inequity.

## 14. Exact submission package and filenames

The learner workspace contains exactly 49 files. The reference workspace contains exactly 58 files.

```text
.gitattributes
VERSION
assessment.md
data-spec.md
operational-contract.json
release.json
source-record.yml
generate_operational_release.py
freeze_upstream.py
build_measures.py
build_workspace.py
validate_workspace.py
release-manifest.csv
data/
  data-dictionary.csv
  operational-source-manifest.csv
  raw/
    calendar-demand.csv.gz
    defect-register.csv.gz
    encounters.csv.gz
    known-truth.csv.gz
    process-events.csv.gz
    queue-snapshots.csv.gz
    safety-events.csv.gz
    scenarios.csv.gz
    staffing.csv.gz
upstream/
  module01-handoff-manifest.csv
  module01-decision-contract.json
  clinical-performance-charter.md
  synthetic-service-declaration.md
  unit-of-flow.csv
  process-boundary.csv
  measure-family.csv
  module01-source-inventory.csv
  source-feasibility-interpretation.md
  claim-boundary.csv
  progression-decision.md
sql/
  01-clean-operational-sources.sql
  02-encounter-measures.sql
  03-operational-measures.sql
  04-validation-and-defects.sql
measure-specifications.csv
defect-repair-log.csv
event-validation.md
operational-interpretation.md
subgroup-support-interpretation.md
measure-score.csv
gate-results.csv
ai-use.md
progression-decision.md
reproducibility-check.md
```

The reference adds:

```text
outputs/
  source-reconciliation.csv
  encounter-measures.csv.gz
  shift-metrics.csv
  weekly-metrics.csv
  safety-diagnostics.csv
  subgroup-support.csv
  defect-impact.csv
  query-checks.csv
  build-report.json
```

### Learner build

```powershell
cd courses/clinical-performance-improvement/modules/02-measures-operational-metrics
python build_workspace.py --target "$env:TEMP\app3-module02-learner"
python validate_workspace.py "$env:TEMP\app3-module02-learner" --starter
```

### Reference build

```powershell
python build_workspace.py --target "$env:TEMP\app3-module02-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module02-reference"
```

The builder refuses to overwrite an existing target.

## 15. Rubric and pass conditions

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Measure definitions and denominators | 4 | 17 complete specifications with exact population, clock, unavailable state, owner, and limit |
| Event logic and data repair | 4 | valid event model, immutable raw layer, 12 declared repairs, and conserved encounter branches |
| Operational metric construction | 4 | reproducible encounter, shift, week, queue, staffing, safety, and subgroup outputs |
| Validation and responsible interpretation | 4 | 30 checks pass and prose stops before diagnosis or action |
| Reproducibility and progression | 4 | exact identities, manifests, disclosure, gates, conditions, and allowed progression |
| **Total** | **20** | **16 or more plus all gates** |

### Fifteen noncompensable gates

1. Fictional service and synthetic rows remain explicit.
2. Public and synthetic identifiers remain disjoint.
3. Adult encounter population is exact.
4. Encounter denominators conserve across branches.
5. Required event states and clocks are validated.
6. Every raw defect has a declared effect.
7. Queue arithmetic conserves.
8. Staffing intervals are valid.
9. Safety types remain separate.
10. Safety detection is tested against generated truth.
11. Subgroup support is explicit.
12. SQL owns linked operational logic.
13. Python independently reproduces and checks outputs.
14. No bottleneck, staffing, causal, clinical, or implementation claim appears.
15. The package is complete, portable, disclosed, and reproducible.

One failed gate makes progression `revise` or `refer`, regardless of points.

## 16. Common errors and instructor interventions

| Error | Why it matters | Instructor response |
|---|---|---|
| counting 43,631 raw encounter rows as the adult denominator | duplicates and quarantined rows enter measures | require raw-to-clean reconciliation |
| using patient as the primary grain | a return-linked person is not one encounter | restore encounter grain and explicit return logic |
| replacing missing clinician time with zero | missingness becomes impossible performance | restore unavailable state and support count |
| calculating duration before checking event order | invalid time enters medians | require event validity before duration |
| dropping D008 entirely | denominator changes to hide a data problem | retain the encounter and suppress only unsupported clocks |
| editing a raw defect | destroys the audit trail | restore immutable raw data and apply SQL repair |
| averaging ratios without their bases | shifts receive misleading equal weight | publish numerator and denominator support |
| treating candidate safety events as harm | safety classes and review status collapse | separate class, truth, trigger, report, and review |
| reading incident capture as prevalence | a detection process becomes a clinical rate | restate the synthetic diagnostic question |
| calling staff-hour ratios productivity | description becomes workforce judgment | keep the measure descriptive and owner-reviewed |
| naming a bottleneck from one median | stage and variation evidence are missing | defer diagnosis to Module 03 |
| recommending staff after seeing overtime | no scenario or burden evidence exists | remove the action and preserve the later evaluation boundary |
| interpreting a generated group difference as real inequity | fictional categories become claims about people | restate support and synthetic limits |
| linking CMS or HHS rows to the fictional service | creates false attribution | remove identifiers and link only at concept level |
| passing a failed gate with enough points | corrupts the release contract | require revise or refer |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Plain-language finding comes before implementation detail.
- Every table has a descriptive heading and logical reading order.
- Status is written in text and never encoded by color alone.
- Dates, units, denominators, and unavailable counts are visible.
- Acronyms are expanded on first use.
- CSV and Markdown records remain usable without a visual dashboard.
- Complete URLs are written visibly where public source context matters.

### Equity

The measure system retains access-support categories, eligible counts, unavailable clocks, and a predeclared teaching threshold. Later comparisons must keep those values attached. Aggregate improvement cannot be called equitable improvement when support is missing, sparse, or uneven.

The categories are synthetic service-support states. They do not establish real prevalence, identity, disparity, discrimination, or burden. Human review is required before a real collection or governance design could be proposed.

### Privacy

The package contains no real patient, clinician, workforce, or hospital data. Synthetic person tokens exist only for generated return linkage. Learners may not attach public facilities, local records, real names, restricted data, or re-identification attempts.

### Responsible claims

Allowed claims describe generated source identity, grain, cleaning, measure support, detection performance, reproducibility, and readiness for Module 03. Prohibited claims include:

- public-to-synthetic equivalence;
- real hospital performance;
- real event prevalence;
- real subgroup disparity;
- bottleneck diagnosis;
- causal explanation;
- productivity judgment;
- staffing adequacy or change;
- clinical benefit or action; and
- implementation authority.

## 18. AI and agent policy

AI or agents may help:

- explain a measure field;
- inspect source structure;
- propose validation checks;
- trace SQL joins;
- detect incomplete denominators;
- compare generated outputs;
- edit prose;
- test schemas; and
- run deterministic reproduction.

AI or agents may not:

- invent source facts;
- edit accepted raw evidence;
- decide which inconvenient records to discard;
- link the fictional service to a public hospital;
- replace missing values with favorable values;
- choose a staffing or clinical action;
- infer a bottleneck before Module 03;
- turn generated categories into claims about real people; or
- replace human accountability.

`ai-use.md` records tool and model, date, purpose, task, data classes, files, output disposition, material claim, independent check, correction or retained action, human owner, and accountability statement.

Material numeric claims require exact reproduction. Fluent text is not proof that the source or SQL was inspected.

## 19. Answer key and instructor interpretation

### Reference decisions

- Accepted adult encounters: `43,628`.
- Completed encounters: `39,975`.
- Left before seen: `3,653`.
- Valid event sequences: `43,627`.
- Clinician times available: `39,974`.
- Raw defects: `12`.
- Query checks: `30 of 30 pass`.
- Measure specifications: `17`.
- Score: `20 of 20`.
- Gates: `15 of 15 pass`.
- Progression: `continue with conditions`.
- Module 03 permission: `permitted for curriculum construction`.
- Operational diagnosis: `prohibited`.
- Bottleneck claim: `prohibited`.
- Staffing change: `prohibited`.
- Clinical action: `prohibited`.
- Causal claim: `prohibited`.
- Implementation: `prohibited`.

### Correct interpretation

The release is ready for Module 03 because the populations, event logic, repairs, output support, safety truth comparison, subgroup support, and identities reproduce. It is conditional because variation rules, safety-signal interpretation, candidate stage comparisons, bottleneck reconciliation, and escalation logic do not exist yet.

### Seven open Module 03 conditions

1. Choose valid time and subgroup comparisons before interpretation.
2. Distinguish common-cause variation from a review signal.
3. Test candidate stages before naming a bottleneck.
4. Carry denominators and unavailable clocks into every comparison.
5. Keep staffing measures descriptive until a later scenario test.
6. Keep generated results separate from clinical action.
7. Preserve reproducibility and claim limits in the Week 3 checkpoint.

Accept alternate wording and SQL when they preserve the same identities, denominators, event eligibility, repair effects, outputs, and boundaries.

## 20. Runnable acceptance checks

### Source generator

```powershell
python generate_operational_release.py --self-check
```

It must prove:

- deterministic reproduction across two independent builds;
- nine tables and 318,732 rows;
- exact manifest and gzip identities;
- all rows synthetic;
- overwrite protection; and
- rejection of a mutated source.

### Upstream handoff

```powershell
python freeze_upstream.py --self-check
```

It must prove ten frozen Module 01 files, exact fingerprints, conditional progression, Module 02 permission, and rejection of a changed handoff.

### Measure builder

```powershell
python build_measures.py --self-check
```

It must prove:

- deterministic output reproduction;
- eight output datasets plus one build report;
- 43,628 accepted encounters;
- 30 exact query checks;
- identical committed and regenerated output bytes; and
- refusal to overwrite a nonempty output target.

### Workspace builder

```powershell
python build_workspace.py --self-check
```

It must prove 49 learner files, 58 reference files, 34 learner manifest rows, 43 reference manifest rows, deterministic manifests, explicit learner placeholders, and overwrite protection.

### Workspace validator

```powershell
python validate_workspace.py --self-check
```

The accepted reference passes 215 checks. The starter passes 150 structural checks. Self-check must reject:

1. a mutated raw source;
2. a missing raw table;
3. changed SQL with a wrong expected denominator;
4. a public link added to learner interpretation;
5. a staffing recommendation;
6. an invalid score;
7. an invalid progression value;
8. a missing required record; and
9. an incomplete starter submitted as complete.

### Repository-wide check

`scripts/check-curriculum-specs.ps1` must pass after the course handoff, build ledger, catalog, version, and next-module records are updated.

## 21. Release status, reviewers, known issues, and handoff

### Release status

- Module version: `0.1.0`.
- Commons release: `0.67.0`.
- Status: runnable release candidate.
- Reference score: `20 of 20`.
- Reference gates: `15 of 15 pass`.
- Reference progression: `continue with conditions`.
- Module 03 permission: `permitted for curriculum construction`.
- Course points awarded: 20.

### Human review required before alpha

- APP-3 faculty owner;
- emergency clinician;
- quality and safety reviewer;
- operations and workflow reviewer;
- nursing and frontline reviewer;
- workforce reviewer;
- access and equity reviewer;
- privacy reviewer;
- data engineering and measure stewardship reviewer;
- accessibility reviewer;
- responsible AI reviewer; and
- independent instructor and reproducer.

Joe Joseph, MD, SFHM, is the named clinician for Module 07. Module 02 does not imply his review, participation, or endorsement.

### Known issues

- Official course section and half-term dates remain to be assigned from the academic calendar.
- The synthetic generator, subgroup design, staffing assumptions, safety-event construction, and workload language require human review before alpha.
- Return within 72 hours is zero in this release and must not be presented as a clinical success result.
- Public source pages may later update, so Module 01 fingerprints remain authoritative for accepted public identities.
- Module 03 must declare chart families, signal rules, low-count handling, candidate stage comparisons, and bottleneck evidence before using these measures diagnostically.

### Handoff to Module 03

Module 03 receives the frozen Module 01 handoff, the Module 02 source manifest, four accepted SQL files, 17 measure specifications, 12 repairs, eight outputs, the build report, 20-point score, 15 gates, seven open conditions, AI record, and progression decision.

Module 03 may study variation, safety signals, and candidate process stages. It may not change a denominator, clock, defect rule, subgroup support rule, or source identity merely to create a clearer signal. Any necessary correction must return to Module 02, receive a new version, reproduce, and be accepted before the Week 3 checkpoint.

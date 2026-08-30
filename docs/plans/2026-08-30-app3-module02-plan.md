# APP-3 Module 02 build plan

## Purpose

Module 02 turns the accepted Module 01 decision into a versioned synthetic operational release and a 20-point measure build. It decides whether the linked event and measure logic is valid enough for Module 03 to study performance over time.

The module does not diagnose a bottleneck, recommend staffing, compare hospitals, claim causation, or authorize action.

## Protected Module 01 handoff

The package will freeze these accepted records from Module 01 with exact byte counts and SHA-256 values:

- decision contract;
- clinical performance charter;
- synthetic service declaration;
- unit of flow;
- process boundary;
- measure families;
- source feasibility interpretation;
- claim boundary;
- progression decision; and
- public-source inventory.

The service remains `CGH-ED-01`, an explicitly fictional adult emergency service with no public hospital linkage. The unit of flow remains one synthetic adult emergency encounter.

## Synthetic operational release

- Release ID: `cgh-ed-01-operational-v1`.
- Generator version: `0.1.0`.
- Fixed seed: `73002`.
- Arrival window: 2024-01-01 through 2024-12-29.
- Schedule: 364 days, 52 weeks, and three eight-hour arrival shifts per day.
- Data class: synthetic teaching data only.
- Public facility identifiers: prohibited from the accepted clean layer.

The generator will use a hash-derived deterministic random stream so output does not depend on process order or an external package.

## Required raw tables

| Table | Grain | Required role |
|---|---|---|
| `encounters.csv.gz` | one raw encounter row, plus one seeded duplicate | population, entry, exit, disposition, access support, and 72-hour return logic |
| `process-events.csv.gz` | one recorded event state per encounter and time | arrival, triage, rooming, clinician contact, disposition, departure, and event order |
| `staffing.csv.gz` | one role per shift | scheduled and actual counts, hours, absence, and overtime |
| `queue-snapshots.csv.gz` | one service queue per 30-minute interval | arrivals, service starts, exits without service, queue conservation, and capacity context |
| `safety-events.csv.gz` | one true event or reviewed non-event candidate | error, near miss, adverse event, harm, trigger, incident report, and review status |
| `calendar-demand.csv.gz` | one arrival shift | calendar features and exact arrival demand |
| `scenarios.csv.gz` | one predeclared scenario | future Module 05 assumptions without scenario results |
| `known-truth.csv.gz` | one generated mechanism or null condition | synthetic validation and later teaching checks |
| `defect-register.csv.gz` | one seeded raw defect | affected key, raw effect, repair rule, clean disposition, and affected measure |

Every table will have an explicit synthetic flag, schema entry, row count, raw byte count, raw SHA-256, gzip byte count, gzip SHA-256, and grain.

## Seeded raw defects

The immutable raw layer will contain twelve declared defects:

1. duplicate encounter row;
2. missing encounter arrival recoverable from the arrival event;
3. public-like service identifier that must be quarantined;
4. underage encounter outside the adult population;
5. encounter departure before arrival recoverable from the departure event;
6. duplicate process event;
7. swapped triage and rooming timestamps;
8. missing clinician-contact event that remains unavailable;
9. impossible negative queue value;
10. impossible negative actual staff hours;
11. duplicate safety candidate;
12. shift arrival count that disagrees with encounter arrivals.

The clean layer must never overwrite or delete the raw files. Each repair or quarantine rule must be visible, tested, and connected to at least one measure consequence.

## SQL ownership

SQL will own:

- deduplication and quarantine;
- event repair and state logic;
- encounter eligibility;
- numerator and denominator membership;
- event-clock calculations;
- shift and week attribution;
- queue conservation;
- staffing interval linkage;
- safety surveillance counts; and
- exact metric tables.

The complete reference uses four ordered SQL files. The learner package contains the same filenames with explicit `REPLACE` prompts and no prebuilt outputs.

## Python ownership

Python will independently verify:

- source manifest identity;
- relationship and key integrity;
- event time and state order;
- duplicate inclusion;
- impossible time;
- missing transitions;
- queue conservation;
- staffing intervals and impossible hours;
- safety sensitivity and specificity;
- cycle and wait time;
- throughput;
- utilization;
- queue length;
- supported subgroup denominators;
- output determinism; and
- score and progression rules.

Only the Python standard library and SQLite are required.

## Measure release

The reference measure specification will include at least these families:

- arrival-to-triage time;
- arrival-to-clinician time;
- arrival-to-departure time;
- left-before-seen rate;
- 72-hour unplanned return rate;
- ordered-event completion;
- process-state completion;
- safety event rate;
- incident-report capture sensitivity;
- arrivals per shift;
- completed throughput per shift;
- queue length;
- staffed clinician hours per arrival;
- clinician utilization proxy;
- overtime hours per shift; and
- supported access-group stratification.

Every specification must name the family, type, unit, direction, numerator or summary, denominator or population, exclusions, event clock, attribution, reporting window, refresh cadence, owner, threshold origin, unavailable state, and interpretation limit.

## Reference outputs

The reference build will release:

- a clean-source reconciliation;
- encounter-level measures as deterministic gzip;
- shift-level operational metrics;
- week-level measure inputs for Module 03;
- safety diagnostics;
- subgroup support;
- defect impacts;
- exact query and invariant checks; and
- a machine-readable build report.

Module 02 may report valid numeric measures. It may not interpret a time pattern as common or special cause, identify a bottleneck, or turn an operational measure into a staffing proposal.

## Assessment

The source-authoritative 20 points are split into five four-point criteria:

1. source, service, unit, and denominator integrity;
2. event and time logic;
3. quality, safety, and access measures;
4. flow, capacity, queue, and workforce measures; and
5. reproducibility, claims, and progression.

All noncompensable gates must pass or pass with an owned condition. Module 03 permission is possible only with `continue` or `continue with conditions`.

## Validation and release

The module will include generator, builder, workspace assembler, and validator self-checks. Failure cases must reject a changed raw source, missing table, wrong denominator, bad event order, broken queue conservation, public-to-synthetic linkage, invalid score, prohibited staffing conclusion, invalid progression, incomplete learner record, and existing-target overwrite.

Commons semver will advance from `0.66.0` to `0.67.0` because this is a new runnable module with a continuing course dataset.

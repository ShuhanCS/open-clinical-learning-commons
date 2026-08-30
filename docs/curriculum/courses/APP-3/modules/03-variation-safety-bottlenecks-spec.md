# APP-3 Module 03: Variation, safety signals, and bottlenecks

## 1. Module identity, decision, and release boundary

- Module ID: `oclc-app3-03`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Instructional week: 3.
- Student effort: 16.5 hours.
- Submission: 20-point performance diagnostic and Week 3 handoff.
- Module version: `0.1.0`.
- Commons release: `0.68.0`.
- Package: `courses/clinical-performance-improvement/modules/03-variation-safety-bottlenecks/`.
- Decision: whether the evidence supports one bounded process diagnosis and immediate escalation rule.
- Primary decision owner: `CGH-ED-01 clinical performance and improvement council`.
- Progression decision: `continue`, `continue with conditions`, `revise`, or `refer`.

This module asks learners to do more than find an unusual point. They must decide whether a signal survives review of its measure, baseline, denominator, event clocks, process stage, safety-surveillance channel, queue, staffing exposure, balancing measures, comparison period, and recovery period.

The accepted diagnosis is limited to the fictional teaching release. Module 03 can name a constrained stage and time window. It cannot establish root cause, staffing adequacy, staff productivity, clinical benefit, or implementation authority.

## 2. Place in the course and Week 3 checkpoint

Module 03 completes the first three-week technical block. The Week 3 checkpoint contains:

| Component | Course points | Role |
|---|---:|---|
| Module 01 clinical performance charter | 0 | required readiness gate |
| Module 02 measure and operational metric build | 20 | accepted population, clocks, measures, and linked evidence |
| Module 03 performance diagnostic | 20 | variation, safety, bounded diagnosis, and escalation |
| **Week 3 total** | **40** | **counted once** |

Module 03 does not itself release Module 04. It permits construction of `checkpoints/01-measures-variation-readiness`. The checkpoint must freeze Modules 01 through 03, verify the 40 points and all inherited gates, and issue a separate progression decision before forecasting begins.

### Module 02 prerequisites

- Service: fictional `CGH-ED-01` adult emergency service.
- Accepted encounters: 43,628.
- Completed encounters: 39,975.
- Left before seen: 3,653.
- Valid event sequences: 43,627.
- Clinician times available: 39,974.
- Raw defects: 12 with declared clean-layer effects.
- Measure specifications: 17.
- Query checks: 30 of 30 pass.
- Module 02 score: 20 of 20.
- Module 02 gates: 15 of 15 pass.
- Module 03 permission: `permitted for curriculum construction`.

`freeze_upstream.py` copies 14 accepted Module 02 files and writes a deterministic handoff manifest. Any changed upstream byte fails validation.

## 3. Learning outcomes

By the end of Module 03, learners can:

1. distinguish routine variation, a predeclared statistical signal, a bounded process diagnosis, and a causal explanation;
2. select a p-chart, XmR chart, exact low-count u-chart, or run chart from the measure type and denominator;
3. declare a baseline and evaluation phase before calculating limits;
4. calculate week-specific binomial limits for a proportion;
5. calculate XmR centerlines and limits from a moving range;
6. preserve integer Poisson limits for low-count surveillance with varying exposure;
7. apply three predeclared signal rules and record every occurrence;
8. recognize when the baseline itself is not a verified stable phase;
9. separate known truth, triggers, reports, false positives, reviewed non-events, and safety classes;
10. explain why incident reports cannot estimate event prevalence;
11. map process states, clocks, handoffs, failure branches, and unavailable rework capture;
12. compare stage time across a baseline, target, contemporaneous control, and recovery period;
13. reconcile stage, queue, throughput, staffing exposure, overtime, and balancing evidence;
14. recalculate subgroup support inside the proposed comparison window;
15. write one bounded synthetic process diagnosis without claiming root cause;
16. write one human escalation rule that does not automate action; and
17. prepare an exact 20-point handoff for the 40-point Week 3 checkpoint.

## 4. Concept ownership and boundaries

### Module 03 owns

- phase definition for the diagnostic;
- chart-family selection;
- centerline and control-limit calculation;
- low-count safety limits;
- signal-rule audit;
- baseline-stability review;
- safety-surveillance interpretation;
- process-stage comparison;
- queue, throughput, staffing, and balancing reconciliation;
- bounded bottleneck diagnosis;
- human escalation rule;
- window-specific subgroup support;
- accessible diagnostic figures and exact tables;
- the 20-point Module 03 score; and
- permission to construct the Week 3 checkpoint.

### Module 03 extends rather than repeats

- FND-1 descriptive and relational work by tracing operational measures across states, shifts, and time;
- FND-2 variation and validation by making the baseline, temporal order, and decision consequence explicit;
- DA-730 process-variation communication by judging charts for clinical-performance meaning, not chart mechanics; and
- Modules 01 and 02 by using their frozen service, source, measure, clock, and claim contracts.

DA-730 remains the standalone conceptual visualization course. APP-3 uses visual methods in service of one operational decision. It does not turn this module into another chart catalog.

### Out of scope

- changing a Module 02 denominator, clock, repair, or unavailable state;
- treating a signal as proof of cause;
- adjusting demand for seasonality or calendar effects;
- forecasting demand;
- using Little's Law to set capacity;
- testing a staffing or workflow scenario;
- estimating an improvement effect;
- recommending staff or a schedule;
- routing patients;
- clinical decision making;
- fitting machine learning;
- authorizing a real test; and
- implementing a change.

Module 04 owns seasonal demand forecasting and capacity implications. Module 05 owns scenarios and evaluation. Module 06 owns feasibility, monitoring, and the embedded machine-learning comparison. Module 07 owns clinician leadership and final defense.

## 5. Source authority and frozen handoff

The local analytic evidence remains synthetic. Public CMS and HHS sources orient measure concepts through Modules 01 and 02, but no public row is linked to `CGH-ED-01`.

The inherited public pages remain:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

https://data.cms.gov/provider-data/dataset/ynj2-r877

https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u

Module 03 freezes these 14 Module 02 files:

1. operational contract;
2. release record;
3. operational source manifest;
4. accepted synthetic safety candidates;
5. encounter measures;
6. shift measures;
7. weekly measures;
8. safety diagnostics;
9. subgroup support;
10. query checks;
11. build report;
12. measure specifications;
13. event validation; and
14. progression decision.

The handoff contains 43,628 accepted encounters, 1,092 shifts, 52 weeks, 1,274 raw safety-candidate rows, and 30 passing query checks. Module 03 deduplicates the one declared safety candidate defect by the accepted Module 02 rule and uses only accepted encounter links.

## 6. Analytic phase and chart-selection contract

### Phases

- Baseline: Weeks 1 through 24.
- Evaluation: Weeks 25 through 52.
- Target process window: evening shifts in Weeks 35 through 44.
- Contemporaneous control: day and night shifts in Weeks 35 through 44.
- Recovery: evening shifts in Weeks 45 through 52.

The baseline is declared before signal calculation. It is long enough for a teaching XmR phase, but it is not assumed stable. The signal audit later finds an eight-point high run inside the baseline. Learners must retain that result and call the limits provisional.

### Four chart choices

| ID | Measure | Family | Reason |
|---|---|---|---|
| C01 | weekly left-before-seen percent | p-chart | a weekly proportion with a varying denominator |
| C02 | weekly mean of three shift median arrival-to-clinician values | XmR | one continuous summary enters in time order |
| C03 | weekly incident reports per 1,000 completed encounters | exact Poisson u-chart | low counts and varying exposure require integer count limits |
| C04 | weekly arrivals | run chart | seasonal and calendar structure makes unadjusted control limits inappropriate |

C04 is intentionally not an individuals chart. The release has known winter and weekday demand structure, and Module 04 owns adjustment and forecasting. A control chart that ignores those mechanisms would label predictable calendar variation as process instability.

## 7. Exact control-limit calculations

### C01 p-chart

The baseline center is:

```text
pbar = baseline left-before-seen encounters / baseline accepted encounters
pbar = 8.137669534781974 percent
```

Each week uses its own denominator `n`:

```text
LCL = max(0, pbar - 3 * sqrt(pbar * (1 - pbar) / n))
UCL = min(1, pbar + 3 * sqrt(pbar * (1 - pbar) / n))
```

The calculation uses proportions internally and reports percent.

### C02 XmR chart

For the 24 baseline weekly values:

```text
X center = 97.63695833333334 minutes
mean moving range = 2.6884782608695654 minutes
X lower limit = center - 2.66 * mean moving range = 90.4856061594203
X upper limit = center + 2.66 * mean moving range = 104.78831050724638
moving-range upper limit = 3.267 * mean moving range = 8.78325847826087
```

The weekly X value is a mean of three shift medians. It is not an encounter-level mean and cannot be relabeled as one.

### C03 exact low-count u-chart

The baseline incident-report center is 9.895750648251045 reports per 1,000 completed encounters. For each week:

1. multiply the baseline rate by the weekly completed-encounter exposure to obtain the expected count;
2. take the exact Poisson 0.00135 and 0.99865 count quantiles;
3. preserve those integer count boundaries;
4. divide by the weekly exposure; and
5. report the limits per 1,000.

The lower boundary can remain zero. A normal approximation cannot replace the exact rule in the accepted release.

### C04 run chart

The Weeks 1 through 24 median is 853 arrivals. The chart has no control limits. It can show sequences and temporal shape, but it cannot isolate a seasonal or special-event demand effect.

## 8. Signal rules and exact audit

Three rules are fixed before the evaluation phase is inspected:

- R1: one point outside the declared control limits;
- R2: eight consecutive points strictly above or below the centerline; and
- R3: six consecutive strictly increasing or decreasing points.

The signal point for R2 is the eighth point. The audit preserves the entire maximal run. The signal point for R3 is the sixth point. No R3 signal appears in the accepted release.

The deterministic audit contains nine records:

| ID | Chart | Rule | Signal week | Full span | Direction |
|---|---|---|---:|---|---|
| S001 | C01 | R1 | 44 | Week 44 | high |
| S002 | C01 | R2 | 49 | Weeks 42 through 49 | above |
| S003 | C02 | R2 | 11 | Weeks 4 through 11 | above |
| S004 | C02 | R1 | 26 | Week 26 | low |
| S005 | C02 | R2 | 42 | Weeks 35 through 52 | above |
| S006 | C02 | R1 | 44 | Week 44 | high |
| S007 | C03 | R2 | 40 | Weeks 33 through 42 | below |
| S008 | C04 | R2 | 8 | Weeks 1 through 11 | above |
| S009 | C04 | R2 | 27 | Weeks 20 through 30 | below |

Every signal receives the same initial disposition: review generated context; signal is not proof of cause. None automates action.

## 9. Baseline stability and known-truth review

S003 occurs inside the baseline. That finding matters because an XmR centerline and limits describe a stable phase only when the phase is reasonably stable. Module 03 therefore calls the accepted limits provisional teaching limits.

The independent audit is frozen before generated truth is interpreted. The post-audit truth review records:

- KT04, bounded demand event: not isolated by the unadjusted arrival run chart; seasonal adjustment is deferred to Module 04;
- KT05, added first-clinician delay: recovered by the evaluation high run and stage reconciliation;
- KT06, access-support delay: visible in full-release summaries, while narrow target-window language and mobility comparisons are unsupported;
- KT07, incident undercapture: recovered by class-specific truth, trigger, report, and reviewed-non-event counts; and
- KT08, routine variation: signals outside KT05 remain review prompts rather than generated causes.

This is not a failure of statistical process control. It is the correct lesson: a rule detects a pattern under a declared reference, while source and process review determine what that pattern can mean.

## 10. Safety-surveillance contract

The accepted clean surveillance layer contains 1,273 reviewed candidates:

| Class | Reviewed | Known true | Trigger true positives | Incident true positives | Trigger sensitivity | Incident capture |
|---|---:|---:|---:|---:|---:|---:|
| error | 333 | 333 | 225 | 79 | 67.5676% | 23.7237% |
| near miss | 254 | 254 | 177 | 74 | 69.6850% | 29.1339% |
| adverse event | 217 | 217 | 183 | 131 | 84.3318% | 60.3687% |
| harm | 90 | 90 | 88 | 74 | 97.7778% | 82.2222% |
| reviewed non-event | 379 | 0 | 0 | 0 | unavailable | unavailable |
| **Overall true events** |  | **894** | **673** | **358** | **75.2796%** | **40.0447%** |

The 379 reviewed non-events are trigger false positives. Overall trigger specificity is 99.0302 percent among completed encounters without generated true events.

C03 has no point beyond its exact Poisson limits. S007 is a low run, so it still opens review. Generated truth has no corresponding temporal safety mechanism. The release cannot call the run improved safety.

An incident report is a surveillance observation, not an event-prevalence denominator. A quiet chart never cancels review of a newly identified serious-harm candidate.

## 11. Process map, handoffs, and rework limits

The accepted process has six ordered states:

1. arrival;
2. triage;
3. roomed;
4. clinician;
5. disposition; and
6. departure.

The stage clocks are:

- arrival to triage;
- triage to roomed;
- roomed to clinician;
- clinician to disposition; and
- disposition to departure.

The process map names the accountable role, incoming and outgoing handoff, clock role, failure branch, and diagnostic use for every state.

The source does not directly capture clinical or administrative rework. A duplicate raw event is a declared data defect, not evidence that work was repeated. Learners must mark rework capture unavailable and may not manufacture a rework rate from duplicate rows.

Left-before-seen remains a valid failure branch. It contributes to the accepted encounter denominator but has no clinician or later-stage time. The one additional missing clinician event also remains unavailable.

## 12. Stage comparison and bounded diagnosis

Four comparison contexts are declared before stage results are read:

| Context | Completed encounters | Purpose |
|---|---:|---|
| Weeks 1 through 24 evening | 6,695 | baseline evening process |
| Weeks 35 through 44 evening | 2,620 | target window |
| Weeks 35 through 44 day and night | 4,824 | contemporaneous control |
| Weeks 45 through 52 evening | 2,229 | recovery |

The exact stage medians are:

| Stage | Baseline evening | Target evening | Day/night control | Recovery evening |
|---|---:|---:|---:|---:|
| arrival to triage | 13 | 13 | 12 | 13 |
| triage to roomed | 39 | 38 | 37 | 39 |
| roomed to clinician | 49 | 66 | 44 | 49 |
| clinician to disposition | 192 | 198 | 192 | 195 |
| disposition to departure | 20 | 20 | 20 | 20 |

Roomed-to-clinician has the clearest localized change. It rises 17 minutes above baseline, is 22 minutes above the contemporaneous day and night median, and returns to 49 minutes in recovery.

The accepted bounded diagnosis is:

> In the fictional `CGH-ED-01` release, evening shifts in Weeks 35 through 44 contain a roomed-to-clinician process constraint.

That sentence does not identify why the constraint occurred.

## 13. Bottleneck reconciliation and support limits

The diagnosis must reconcile eight evidence rows:

| Evidence | Baseline evening | Target evening | Day/night control | Recovery evening |
|---|---:|---:|---:|---:|
| roomed-to-clinician median, minutes | 49.0000 | 66.0000 | 44.0000 | 49.0000 |
| arrival-to-clinician shift median, minutes | 100.0000 | 116.0000 | 92.7500 | 99.0000 |
| median mean-queue end | 9.0000 | 9.9688 | 7.1875 | 8.9062 |
| median max-queue end | 11.0000 | 12.0000 | 10.0000 | 11.0000 |
| completed per clinician hour | 1.0244 | 0.9393 | 0.8750 | 0.9637 |
| clinician hours per arrival | 0.8889 | 0.9535 | 1.0435 | 0.9302 |
| left before seen, percent | 8.9859 | 11.2165 | 7.4799 | 9.0575 |
| overtime hours per shift | 0.9881 | 1.1429 | 1.0857 | 0.8214 |

Stage, total delay, queue, balancing, contemporaneous comparison, and recovery support the bounded diagnosis. Throughput is partial evidence because it is lower than baseline but not lower than the day and night control. Staffing exposure and overtime remain descriptive. They do not establish staffing adequacy, burden, productivity, or cause.

### Window-specific subgroup support

Full-release support is available for all three synthetic groups. The target evening window contains:

- language support: 401 encounters, below the 1,000 threshold;
- mobility support: 242 encounters, below the threshold; and
- standard: 2,308 encounters, above the threshold.

Only one group has target-window support, so no cross-group target-window comparison is accepted. Full-release support cannot be borrowed for a narrower period.

## 14. Immediate escalation rule and human authority

The required rule is E01.

- Trigger: a high C02 R1 or R2 clinician-delay signal plus a same-period C01 high signal or documented queue corroboration.
- Reference trigger point: Week 44.
- Reference evidence: C02 R1 high, C02 R2 above, C01 R1 high, and elevated evening queue evidence.
- Action: open human clinical, flow, access, and safety review within one business day.
- Data stop: if source identity, denominator, event clock, or support gate fails, stop interpretation and return to Module 02.
- Safety override: a newly reviewed serious-harm candidate enters immediate safety review regardless of chart status.
- Restart: accepted data repair or human review disposition with owner and date.

E01 opens review. It does not select staff, change a schedule, route a patient, alter care, launch a test, or implement a change. The council remains accountable for disposition.

## 15. Instructional sequence, workload, and submission

### 16.5-hour sequence

| Block | Hours | Learner work | Evidence |
|---|---:|---|---|
| Handoff and decision | 1.0 | verify Module 02 and restate the bounded question | handoff record |
| Process map and stages | 2.0 | map states, handoffs, clocks, failure branches, and rework limits | process map |
| Variation and chart selection | 3.0 | choose four charts and calculate centers and limits | chart selection and variation series |
| Safety surveillance | 2.5 | separate truth, triggers, reports, false positives, and classes | safety interpretation |
| Bottleneck reconciliation | 3.0 | compare stages, queues, throughput, staffing exposure, balancing, and recovery | diagnostic and reconciliation |
| Subgroup and access support | 1.5 | recalculate support in the target window | support interpretation |
| Communication and accessible charts | 1.5 | build exact tables and four accessible SVGs | diagnostic figures |
| Scoring, escalation, and defense | 2.0 | score gates, defend E01, and issue progression | score, gates, AI record, progression |
| **Total** | **16.5** |  |  |

### Learner workspace

The learner workspace contains exactly 41 files:

- 12 immutable module controls;
- 15 upstream files, including the handoff manifest;
- 13 editable learner records; and
- one generated release manifest.

### Reference workspace

The reference contains exactly 54 files. It adds 13 accepted diagnostic outputs and records 40 immutable manifest rows.

### Editable records

1. `process-map.csv`;
2. `chart-selection.csv`;
3. `signal-rules.csv`;
4. `performance-diagnostic.md`;
5. `safety-interpretation.md`;
6. `bottleneck-interpretation.md`;
7. `subgroup-support-interpretation.md`;
8. `escalation-rule.md`;
9. `week3-score.csv`;
10. `gate-results.csv`;
11. `ai-use.md`;
12. `progression-decision.md`; and
13. `reproducibility-check.md`.

## 16. Rubric, gates, and Week 3 accounting

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Chart selection and exact limits | 4 | four justified families, exact baseline, center, limits, exposure, and known limit |
| Signal calculation and phase interpretation | 4 | all nine signals, three rules, baseline instability, and no signal-as-cause claim |
| Safety surveillance and low-count reasoning | 4 | exact Poisson limits, separated classes and channels, undercapture, false positives, and event-level override |
| Process diagnosis and support limits | 4 | process map, stage and control comparison, queue, throughput, staffing, balancing, recovery, and subgroup support |
| Communication, escalation, and reproducibility | 4 | accessible figures, exact tables, human E01, disclosure, deterministic outputs, and progression |
| **Total** | **20** | **16 or more plus all gates** |

### Eighteen noncompensable gates

1. Module 02 identity is frozen.
2. Service remains fictional and synthetic.
3. Baseline and evaluation phases are declared before calculation.
4. Baseline instability is disclosed.
5. Chart families match measure type and denominator.
6. Control limits and centers reproduce exactly.
7. Signal rules are predeclared and auditable.
8. A signal is not treated as proof of cause.
9. Low-count safety limits remain exact.
10. Safety classes and surveillance channels remain separate.
11. Process handoffs and unavailable rework capture are explicit.
12. Bottleneck diagnosis uses multiple evidence families.
13. Root cause and staffing adequacy remain unestablished.
14. Narrow subgroup support is recalculated.
15. Charts and tables are accessible.
16. Escalation remains human and nonclinical.
17. Module 03 score and Week 3 accounting are exact.
18. Package is complete, portable, disclosed, and reproducible.

One failed gate forces `revise` or `refer`, regardless of points.

## 17. Common errors and instructor interventions

| Error | Why it matters | Instructor response |
|---|---|---|
| changing Weeks 1 through 24 after seeing results | creates a favorable post-hoc phase | restore the predeclared baseline |
| calling the baseline stable | S003 contradicts that claim | label the limits provisional |
| using a p-chart without weekly denominators | limits become wrong when exposure varies | show numerator, denominator, and week-specific limits |
| using normal u-chart limits for low reports | integer low-count behavior disappears | restore exact Poisson count quantiles |
| calling S007 improved safety | the chart has no exact breach and truth has no temporal safety mechanism | retain review status and undercapture limits |
| calling incident reports prevalence | reports are an incomplete surveillance channel | compare with known truth and state capture |
| merging error, near miss, adverse event, and harm | clinical meaning and capture differences disappear | restore class-specific rows |
| treating a duplicate event as rework | a data defect becomes a workflow claim | mark rework capture unavailable |
| naming a bottleneck from C02 alone | a weekly summary cannot localize a stage | require stage, queue, control, balancing, and recovery evidence |
| calling lower throughput proof of staffing shortage | the day/night control is lower and hours per arrival are not lower | keep throughput partial and staffing descriptive |
| comparing target-window support groups | two groups are below the threshold | report support and suppress comparison |
| treating generated truth as the analysis | learners can reverse-engineer the intended answer | freeze the independent review before truth disclosure |
| turning E01 into a staffing order | escalation and intervention are different decisions | restore human review and prohibited actions |
| adding Module 01 points | corrupts the source 40-point contract | keep Module 01 as a zero-point gate |
| starting Module 04 immediately | bypasses checkpoint acceptance | build and validate the Week 3 checkpoint first |

## 18. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Plain-language finding precedes technical calculation.
- Every chart has an SVG title and description.
- Signal markers use a square, an `S` label, and text, not color alone.
- Axes state unit and week.
- Process-stage bars include abbreviations and numeric labels.
- Exact CSV tables accompany every figure.
- Tables use descriptive headings and logical reading order.
- Status and progression are written in text.

### Equity and access

Support is a property of a group inside a defined window. Full-release support does not make a target-window comparison valid. The learner must report eligible encounters, unavailable clinician times, left-before-seen numerator and denominator, median support, threshold, and suppression status.

The categories are generated service-support states. They do not establish identity, real prevalence, discrimination, inequity, or cause.

### Privacy

The package contains no real patient, clinician, workforce, or hospital data. Stable synthetic identifiers exist only to preserve linked teaching grain. Learners may not add public provider identifiers, local records, names, restricted data, or re-identification attempts.

### Responsible claims

Allowed claims describe source identity, calculation, signals, surveillance capture, support, stage localization, recovery, and readiness for checkpoint construction.

Prohibited claims include:

- public-to-synthetic equivalence;
- current real-service performance;
- a signal as proof of cause;
- true real-world safety prevalence;
- real subgroup disparity;
- root cause;
- staffing adequacy or productivity;
- staffing, scheduling, or routing change;
- clinical benefit or action;
- causal effect; and
- implementation authority.

## 19. AI, R, and software policy

AI or agents may help:

- explain chart selection;
- inspect phase and denominator logic;
- reproduce centerlines and limits;
- trace signal rules;
- compare stage outputs;
- audit missing support;
- check accessible SVG structure;
- edit prose; and
- run deterministic validation.

AI or agents may not:

- change the baseline after seeing results;
- hide a baseline signal;
- invent a stable phase;
- convert a signal into cause;
- relabel a duplicate as rework;
- invent subgroup support;
- recommend staffing or care;
- authorize implementation; or
- replace human escalation ownership.

`ai-use.md` records tool and model, date, purpose, task, data classes, files, output disposition, material claim, independent verification, correction or retained action, human owner, and accountability statement.

Python is the deterministic release authority. `verify_control_charts.R` uses base R to recompute the p-chart center and XmR values. Learners are expected to read, run, and interpret it. Writing R from scratch is not graded. R is not installed in the construction environment, so an independent R execution remains a pre-alpha review condition.

## 20. Runnable acceptance checks and failure routes

### Upstream handoff

```powershell
python freeze_upstream.py --self-check
```

It must verify 14 exact Module 02 files, reproduce the handoff manifest, confirm 43,628 encounters and 30 passing checks, and reject changed upstream evidence.

### Diagnostic builder

```powershell
python build_diagnostic.py --self-check
```

It must reproduce 13 outputs twice, compare every byte with the committed reference, recover nine signal records and the 66-minute target stage median, and refuse a nonempty output target.

### Workspace builder

```powershell
python build_workspace.py --self-check
```

It must prove 41 learner files, 54 reference files, 27 learner manifest rows, 40 reference manifest rows, deterministic manifests, placeholders, and overwrite protection.

### Workspace validator

```powershell
python validate_workspace.py --self-check
```

The complete reference passes 259 checks. The starter passes 130 structural checks. Self-check rejects:

1. changed Module 02 evidence;
2. missing upstream evidence;
3. changed baseline;
4. wrong chart family;
5. changed control limit;
6. missing exact low-count handling;
7. signal-as-cause language;
8. a staffing recommendation;
9. an unsupported subgroup claim;
10. changed bottleneck stage;
11. wrong score;
12. failed gate;
13. invalid progression;
14. missing required record; and
15. an incomplete starter submitted as complete.

### Base-R check

```powershell
Rscript verify_control_charts.R
```

The expected result is `APP-3 Module 03 base-R control-chart verification passed.` This check must be run independently before alpha.

### Repository gate

`scripts/check-curriculum-specs.ps1` must pass after the course handoff, ledger, checker, catalog, and Commons version are updated.

## 21. Release status, reviewers, known issues, and handoff

### Release status

- Module version: `0.1.0`.
- Commons release: `0.68.0`.
- Status: runnable release candidate.
- Reference score: 20 of 20.
- Reference gates: 18 of 18 pass.
- Reference progression: `continue with conditions`.
- Week 3 checkpoint permission: `permitted for curriculum construction`.
- Module 04 permission: `not yet`.
- Action authorized: no.

### Required human review before alpha

- APP-3 faculty owner;
- emergency clinician;
- quality and safety reviewer;
- statistical process control reviewer;
- operations and workflow reviewer;
- nursing and frontline reviewer;
- workforce reviewer;
- patient and access reviewer;
- equity and privacy reviewer;
- data engineering and measure-stewardship reviewer;
- R reviewer;
- accessibility reviewer;
- responsible AI reviewer; and
- independent instructor and reproducer.

Joe Joseph, MD, SFHM, is the named clinician for Module 07. Module 03 does not imply his review, participation, or endorsement.

### Known issues

- The official APP-3 section and half-term dates remain to be assigned from the academic calendar.
- The Weeks 1 through 24 baseline contains a high run and cannot serve as a live stable control phase.
- The arrival run chart cannot isolate the generated demand event without the seasonal and calendar modeling owned by Module 04.
- Language-support and mobility-support target-window groups remain below the teaching support threshold.
- Rework is not directly captured.
- R execution remains pending in an environment with R installed.
- Synthetic generator, safety construction, process diagnosis, subgroup language, escalation wording, and workload require human review before alpha.

### Handoff to the Week 3 checkpoint

The checkpoint receives:

- the accepted Module 01 decision package;
- the accepted Module 02 20-point measure package;
- the Module 03 20-point performance diagnostic;
- 14 frozen Module 02 inputs;
- 13 deterministic diagnostic outputs;
- four chart contracts;
- three signal rules and nine signal records;
- safety truth, trigger, report, false-positive, reviewed-non-event, and class evidence;
- six process states and five stage comparisons;
- eight bottleneck-reconciliation rows;
- window-specific subgroup support;
- E01 human escalation;
- 18 Module 03 gates;
- eight checkpoint conditions;
- AI disclosure; and
- the progression decision.

The checkpoint must freeze the exact evidence without recalculating a favorable baseline or changing a denominator. It counts Module 02 and Module 03 once, keeps Module 01 as a required zero-point gate, and decides whether Module 04 may begin.

# APP-3 Module 05: Improvement scenarios and evaluation

## 1. Module identity, decision, and release boundary

- Module ID: `oclc-app3-05`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Instructional block: application block after the accepted forecast.
- Source feedback milestone: end of instructional Week 5.
- Cumulative checkpoint: end of instructional Week 6.
- Student effort: 16.0 hours.
- Submission: 25-point forecast, scenario, and evaluation component.
- Course points: 25, counted once.
- Module version: `0.1.0`.
- Commons release: `0.71.0`.
- Package: `courses/clinical-performance-improvement/modules/05-improvement-scenarios-evaluation/`.
- Decision: which baseline, flex-coverage, fast-track, or combined option, if any, deserves feasibility review.
- Primary decision owner: `CGH-ED-01 clinical performance and improvement council`.
- Progression decision: `continue`, `continue with conditions`, `revise`, or `refer`.

The learner must answer a practical question: when the accepted demand forecast and its uncertainty are carried into a guided operations model, does any bounded redesign clear the declared performance, access, workforce, and stress gates? A correct answer may be no. The assignment rewards a defensible decision, not selection of an intervention.

This is a synthetic teaching analysis. It compares assumptions and exposes tradeoffs. It does not predict a realized intervention effect, validate a production simulator, define required staffing, measure productivity, establish safety, establish equitable access, route a real patient, automate a decision, or authorize implementation.

## 2. Place in the course and the Week 6 package

Modules 04 through 06 form the application block after the Week 3 measures and diagnostic checkpoint.

| Unit | Hours | Course points | Application role |
|---|---:|---:|---|
| Module 04 demand forecasting and capacity | 16.5 | 0 | accepted demand and uncertainty gate |
| Module 05 improvement scenarios and evaluation | 16.0 | 25 | scored scenario and evaluation component |
| Module 06 feasibility, monitoring, and embedded ML | 16.0 | 0 | feasibility, monitoring, and ML gates |
| Cumulative Week 6 checkpoint | 48.5 | 25 | one accepted application release |

Module 05 accepts the Module 04 forecast without changing its target, folds, method, or error record. It uses the point forecast, lower and upper values, difficult periods, Week 3 process diagnosis, access evidence, and action limits as scenario inputs. Module 06 later receives the exact scenario decision and may not tune Module 05 after seeing its own results.

The source assessment is due for feedback at the end of Week 5. The 25 points enter the cumulative checkpoint only once at Week 6, after Module 06 supplies its required zero-point gates. A strong Module 06 result cannot repair an altered scenario contract, hidden failed condition, unsupported safety claim, or forced option selection.

## 3. Learning outcomes

By the end of Module 05, learners can:

1. translate a bounded clinical operations question into baseline and redesign scenarios;
2. distinguish a scenario assumption from an observed mechanism or effect;
3. preserve the accepted forecast target, uncertainty, diagnosis, and scenario register;
4. explain the roles of arrivals, preparation, service, routing, priority, staffing, capacity, abandonment, and warm-up;
5. trace one patient and one paired replication through a guided discrete-event model;
6. use common random numbers to make scenario comparisons more precise;
7. validate arrivals, service, routing, priority, capacity, conservation, run identity, and output bounds;
8. compare no change with at least two redesign options on the same simulated inputs;
9. interpret median, tail, abandonment, throughput, utilization, overtime, activation, access, and workforce results together;
10. distinguish a throughput gain from a wait improvement;
11. preserve null, failed, fragile, and tradeoff-bearing conditions;
12. apply a predeclared option rule without selecting the least unfavorable option;
13. state why simulation does not establish a causal effect;
14. design process-control monitoring separately from causal evaluation;
15. audit secular trend, regression to the mean, measurement changes, concurrent interventions, case mix, gaming, contamination, and missing groups;
16. identify prospective safety, return, access, and workforce measures that the model cannot supply;
17. communicate scenario evidence through exact tables, accessible figures, and plain language;
18. document responsible AI use and reproduce the accepted release; and
19. hand Module 06 an exact decision, conditions, failures, measures, and authority boundary.

## 4. Concept ownership and boundaries

### Module 05 owns

- the guided scenario model and its declared assumptions;
- the no-change, flex-coverage, fast-track, and combined option rules;
- five demand, service, and workflow-effect conditions;
- warm-up, measurement, seeds, common random numbers, and replications;
- arrivals, service, route, priority, capacity, conservation, and calibration checks;
- paired option effects and uncertainty summaries;
- median and P90 arrival-to-clinician time;
- arrival-to-departure time, completed throughput, and left before seen;
- clinician utilization, modeled overtime, flex hours, triggers, and activation delay;
- language-support, mobility-support, and standard-group wait evidence;
- failed and fragile condition retention;
- the predeclared selection rule and no-selection outcome;
- prospective evaluation measures and threat audit;
- gaming and unintended-effect review;
- the full 25-point score and 20 noncompensable gates; and
- the exact Module 06 handoff.

### Module 05 revisits rather than repeats

- FND-1 data quality through source identity, row checks, missingness, event order, and conservation;
- FND-2 probability and statistics through stochastic inputs, paired comparisons, quantiles, uncertainty, and decision rules;
- DA-730 visual communication through two decision-focused accessible figures;
- APP-3 Module 02 through accepted measures and operational metric definitions;
- APP-3 Module 03 through the accepted roomed-to-clinician diagnosis, access limits, signal uncertainty, and escalation boundary; and
- APP-3 Module 04 through the accepted forecast, empirical range, error, and difficult periods.

Every applied course revisits fundamentals for a different decision. This module owns scenario reasoning and evaluation, not generic statistics instruction. DA-730 remains the separate concept-first visualization course.

### Out of scope

- changing the accepted service, population, measures, repairs, clocks, diagnosis, or forecast;
- treating public or synthetic missing values as observed;
- fitting or comparing machine learning;
- constructing a production simulation;
- optimizing a real schedule;
- estimating required staff or individual productivity;
- claiming that a model assumption is an observed operational fact;
- interpreting simulated safety or return outcomes;
- using a pre/post mean difference as causal evidence;
- selecting an option after weakening a failed gate;
- clinical decision making;
- automated routing, staffing, or scheduling;
- authorizing a real-world test; and
- implementation.

Module 06 owns feasibility, monitoring design, escalation, fallback, and embedded ML. Module 07 owns clinician leadership, recommendation, and final defense.

## 5. Source authority and frozen handoff

The authoritative analytic handoff is Module 04, `oclc-app3-04` version `0.1.0` at Commons release `0.70.0`. The Module 05 package freezes 29 accepted files plus its handoff manifest.

| Handoff fact | Accepted value |
|---|---:|
| Frozen analytic files | 29 plus manifest |
| Accepted synthetic encounters | 43,628 |
| Completed donor encounters | 39,974 |
| Empirical donor strata | 45 |
| Selected forecast method | seasonal exponential smoothing |
| Point weekly arrivals | 876.924084 |
| Lower weekly arrivals | 805.136639 |
| Upper weekly arrivals | 970.733035 |
| Weekly MAE | 64.678197 arrivals |
| Accepted scenarios | S00 through S03 |
| Scenario known truths | KT09 and KT10 |

The source course is `07-APP-3-Clinical-Performance-and-Improvement.docx`. It assigns 16.0 hours to improvement scenarios and evaluation and places the 25-point forecast, scenario, and evaluation assessment at the end of Week 5 for the Week 6 package.

`freeze_upstream.py` checks every frozen file by path, byte count, and SHA-256. It also verifies the exact forecast release, Week 3 diagnosis, scenario register, known-truth contract, accepted encounter profile, measure specifications, and Module 05 permission. Learners do not repair or silently replace this handoff.

## 6. Decision question and predeclared scenario contract

Before running the model, the learner records:

- decision: which option, if any, deserves feasibility review;
- baseline: S00 no change;
- options: S01 flex coverage, S02 fast track, and S03 combined bounded rule;
- primary condition: C02 point demand;
- stress condition: C04 upper demand with slower service;
- comparison unit: paired replication;
- warm-up: 7 days;
- measurement: 7 days;
- replications: 200 per scenario-condition cell;
- base seed: 7300500;
- primary and secondary measures;
- selection thresholds;
- near-tie rule;
- access and workforce limits;
- outcomes not simulated;
- failed-result retention rule; and
- implementation boundary.

The model uses 1,000 unique workloads: 5 conditions by 200 replications. Each workload is passed unchanged to all four scenarios, producing 4,000 runs. Common random numbers ensure that an option is compared with no change under the same arrivals, acuity, support need, preparation delay, service donor, and abandonment draw.

## 7. Guided model structure and input assumptions

The engine is a bounded discrete-event model written with the Python standard library. Learners configure and interrogate it. They are not required to build a production simulator.

### Time and arrivals

- Each run contains a 7-day warm-up and 7-day measurement period.
- Each day has night, day, and evening eight-hour shifts.
- The accepted 21-shift Week 53 shape distributes expected arrivals.
- Arrivals within each shift follow a homogeneous Poisson process.
- Only measurement-week arrivals enter reported outcomes.

### Patient and service profile

- Acuity and access-support profiles are sampled from 43,628 accepted synthetic encounters.
- Preparation and clinician-to-departure donors come from 39,974 completed encounters.
- Donors are matched by shift, acuity, and access-support group.
- The model uses 20 percent of clinician-to-departure elapsed time as an effective service proxy.
- The 20 percent factor represents intermittent clinician work inside a longer interval. It is not productivity.
- Low-acuity abandonment follows the declared synthetic source mechanism.

### Queue and capacity

- Priority is nonpreemptive and acuity ordered, with acuity 1 highest.
- Base clinician slots are 2 night, 6 day, and 4 evening.
- This schedule is a calibrated teaching assumption, not an observed staffing count.
- The initial 3-night, 7-day, and 5-evening schedule produced a 55-minute median and too little queue response to distinguish options.
- The released schedule was fixed before the accepted output release and keeps point-demand abandonment inside the broad 4 to 15 percent calibration range.

All assumptions appear in `scenario-assumption-register.csv`. A learner may criticize an assumption without silently changing it. A proposed revision becomes a new declared condition and requires a new release.

## 8. Exact scenario rules

| ID | Scenario | Trigger | Resource change | Routing or service change |
|---|---|---|---|---|
| S00 | No change | none | none | none |
| S01 | Flex clinician coverage | accepted shift forecast meets 32 night, 55 day, or 48 evening arrivals | one added synthetic clinician slot for the full eligible shift | none |
| S02 | Fast-track activation | at least 4 waiting patients for 15 minutes | no net added staff | one existing slot prioritizes acuity 4 and 5 with service multiplier 0.70 |
| S03 | Combined bounded rule | forecast eligibility plus the same sustained queue threshold | one added synthetic slot after activation | fast-track rule after activation |

Every support group remains eligible. Support need cannot be used to deny the route. Activation is recorded, and a threshold that does not persist for 15 minutes does not activate. S02 must show zero flex clinician-hours. S03 must satisfy both the forecast and queue rules.

These rules configure synthetic choices. They do not establish that a low-acuity route is clinically appropriate or that a staffing block is available.

## 9. Uncertainty and sensitivity conditions

| ID | Condition | Weekly arrivals | Service multiplier | Fast-track multiplier | Purpose |
|---|---|---:|---:|---:|---|
| C01 | Lower demand | 805.136639 | 1.00 | 0.70 | lower accepted demand bound |
| C02 | Point demand | 876.924084 | 1.00 | 0.70 | primary decision condition |
| C03 | Upper demand | 970.733035 | 1.00 | 0.70 | upper accepted demand bound |
| C04 | Upper demand and slower service | 970.733035 | 1.15 | 0.70 | demand and service stress |
| C05 | Point demand and weak workflow effect | 876.924084 | 1.00 | 0.90 | reduced fast-track benefit |

The accepted release retains all 15 option-condition comparisons. An option is not removed because it performs poorly. A result is marked null or failed when median or P90 wait does not improve, throughput falls by more than 1 percent, or the language-support gap worsens by more than 5 minutes. Partial benefit is distinct from full qualification.

## 10. Model validation, calibration, and conservation

The builder runs 24 release checks:

1. 43,628 accepted encounter profiles;
2. S00 through S03 scenario identity;
3. 45 donor strata;
4. accepted point forecast identity;
5. five conditions;
6. 7-day warm-up;
7. 4,000 runs;
8. 1,000 shared paired seeds;
9. acuity priority;
10. calibrated base capacity;
11. forecast thresholds;
12. fast-track trigger;
13. zero S02 added staff;
14. combined S03 rule;
15. arrival conservation;
16. nonnegative counts and times;
17. unique run identities;
18. broad no-change wait calibration;
19. 4 to 15 percent no-change abandonment calibration;
20. finite standard, language, and mobility results;
21. retained null or failed evidence;
22. unmodeled safety boundary;
23. unmodeled 72-hour return boundary; and
24. valid selection output, including none.

All 24 pass in the reference. Under C02 and S00, median arrival-to-clinician time is 60.035963 minutes, P90 is 136.453267 minutes, and left before seen is 11.914912 percent. High-acuity median wait is 45.084398 minutes and low-acuity median wait is 70.473589 minutes.

Calibration makes a guided model plausible enough to compare assumptions. It does not validate local staffing, individual behavior, a production implementation, or external prediction.

## 11. Paired comparison measures and interpretation

Every scenario-condition cell reports medians across 200 replications for:

- arrivals;
- completed encounters;
- left-before-seen count and percent;
- median arrival-to-clinician time;
- P90 arrival-to-clinician time;
- median arrival-to-departure time;
- clinician utilization;
- modeled overtime;
- flex clinician-hours;
- triggers and activation delay;
- standard, language-support, and mobility-support waits;
- language and mobility gaps relative to standard;
- high- and low-acuity waits;
- maximum waiting queue;
- fast-track completions;
- safety status;
- 72-hour return status; and
- conservation status.

Paired effects subtract the option from no change for wait and abandonment so a positive value favors the option. Throughput change is the paired percentage change from S00. The release also includes 10th and 90th percentiles across paired replications. A gain in one outcome cannot be relabeled as improvement in every outcome.

## 12. Exact reference comparison

### Point-demand scenario results

| Scenario | Median wait | P90 wait | Left before seen | Completed | Flex hours |
|---|---:|---:|---:|---:|---:|
| S00 no change | 60.035963 | 136.453267 | 11.914912% | 772.5 | 0.000000 |
| S01 flex coverage | 58.437408 | 114.495931 | 9.393213% | 795.0 | 40.000000 |
| S02 fast track | 66.508977 | 180.955701 | 5.260214% | 829.0 | 0.000000 |
| S03 combined | 60.000000 | 121.559060 | 8.693199% | 801.0 | 25.220413 |

### Paired option effects at point demand

| Option | Median wait improvement | P90 wait improvement | LBBS improvement | Throughput change | Language-gap worsening |
|---|---:|---:|---:|---:|---:|
| S01 | 1.958703 min | 21.244986 min | 2.518000 pp | 2.874244% | 0.013189 min |
| S02 | -5.803341 min | -41.617987 min | 6.611140 pp | 7.540650% | -0.345440 min |
| S03 | 0.316383 min | 14.547388 min | 3.163164 pp | 3.590432% | 0.031209 min |

S01 improves the tail and abandonment but only modestly changes the median. S02 illustrates why throughput cannot stand in for flow: more patients complete, but median and P90 waits worsen. S03 provides partial benefits but remains below the declared wait thresholds.

Six option-condition rows are null or failed. Under C04, S02 worsens median wait by 86.671644 minutes. That result remains visible.

## 13. Selection rule, tradeoffs, and no-selection result

At C02, an option must satisfy all of these rules:

- median arrival-to-clinician improvement at least 10 minutes;
- P90 arrival-to-clinician improvement at least 15 minutes;
- left-before-seen improvement at least 1 percentage point;
- throughput loss no worse than 1 percent;
- language-support gap worsening no more than 5 minutes;
- positive median-wait improvement under C04; and
- all validation, conservation, and claim-boundary gates pass.

If qualifying options are within 5 minutes on point-demand median improvement, the option with fewer flex hours is preferred. If no option qualifies, the decision is none. The learner may not choose the largest throughput gain, the best single measure, or the least unfavorable result.

Reference decision: `none qualifies for feasibility review`.

- S01 fails the 10-minute median rule.
- S02 fails the median, P90, and stress rules.
- S03 fails the median and P90 rules.

The assignment earns full credit because the no-selection decision follows the contract and preserves tradeoffs. The result may support revision or further evidence collection, not implementation.

## 14. Prospective monitoring and evaluation design

The release defines 12 measures for a later authorized test:

| Domain | Measure | Display or analysis | Boundary |
|---|---|---|---|
| process | weekly median arrival-to-clinician | XmR | monitoring, not causal proof |
| process | P90 arrival-to-clinician | exact table and run chart | preserve tail |
| process | arrival-to-departure | XmR | preserve denominator and clock |
| process | left before seen | p-chart | audit exclusions |
| process | completed throughput | run chart | not a safety proxy |
| workforce | clinician utilization | exact table and run chart | not productivity |
| workforce | overtime hours | run chart | prospectively verify |
| safety | reviewed event candidates | exact Poisson u-chart | reporting completeness required |
| outcome | return within 72 hours | p-chart | follow-up completeness required |
| access | language-support wait gap | exact table and run chart | report support and unavailable states |
| access | mobility-support wait gap | exact table and run chart | report support and unavailable states |
| workforce | interruptions and perceived load | prospective instrument | no accepted baseline yet |

Process-control monitoring asks whether the observed process is changing and whether a signal requires review. Causal evaluation asks whether the option produced the change. Those are different questions. A before-and-after average is not sufficient for the causal question.

Any stronger design must be separately authorized and must specify assignment, eligibility, adoption, crossover, calendar time, case mix, missingness, and concurrent changes. The model can inform expectations, monitoring limits, and stop rules. It cannot supply observed outcomes.

## 15. Evaluation threats, gaming, and unintended effects

The learner audits eight required threats:

1. secular trend in demand or flow;
2. regression to the mean after an unusually poor trigger period;
3. measurement or documentation change;
4. concurrent staffing, workflow, or policy intervention;
5. changing acuity, arrival mode, or support need;
6. gaming of timestamps, routing, exclusions, or denominators;
7. contamination, uneven adoption, or crossover; and
8. missing or unsupported access groups.

The audit names a detection method and response for each threat. The evaluation must also look for displaced work, interruptions, overtime, worsening high-acuity flow, reduced safety reporting, incomplete follow-up, denial of access-support needs, and route use outside eligibility.

When measure production changes, the team pauses interpretation and investigates. It does not treat a favorable dashboard as proof that the care process improved.

## 16. Instructional sequence and 16-hour workload

| Learning segment | Hours | Learner activity | Durable evidence |
|---|---:|---|---|
| 1. Handoff and decision contract | 2.0 | verify forecast, scenario register, decision, and boundaries | assumption register |
| 2. Model tracing and validation | 3.0 | trace one patient and one paired replication; test model structure | scenario validation |
| 3. Scenario comparison | 4.0 | run S00 through S03; interpret paired outcomes | scenario comparison and figures |
| 4. Sensitivity and tradeoffs | 2.5 | compare C01 through C05; retain failures | sensitivity and access/workforce review |
| 5. Evaluation design | 2.5 | specify measures, threats, gaming, and unintended effects | evaluation records |
| 6. Decision, scoring, and handoff | 2.0 | apply rules, score once, verify, and hand off | score, gates, progression, Module 06 handoff |
| Total | 16.0 |  |  |

The instructor first asks learners to trace a paired replication rather than reading the answer table. The main critique asks whether the learner preserved a failed result and separated throughput, wait, safety, access, workforce, and causal claims.

Feedback occurs at the source Week 5 milestone. The work becomes final only when it enters the cumulative Week 6 package with the required Module 06 gates.

## 17. Submission, outputs, and workspace contract

The deterministic builder produces 12 accepted outputs:

1. `input-profile.csv`, 45 rows;
2. `condition-register.csv`, 5 rows;
3. `validation-checks.csv`, 24 rows;
4. `replication-results.csv`, 4,000 rows;
5. `scenario-summary.csv`, 20 rows;
6. `paired-effects.csv`, 15 rows;
7. `sensitivity-review.csv`, 15 rows;
8. `evaluation-measures.csv`, 12 rows;
9. `evaluation-threats.csv`, 8 rows;
10. `scenario-findings.json`;
11. `point-demand-tradeoffs.svg`; and
12. `sensitivity-wait-effects.svg`.

The learner submission contains 14 records:

1. `scenario-assumption-register.csv`;
2. `scenario-validation.md`;
3. `scenario-comparison.md`;
4. `sensitivity-interpretation.md`;
5. `access-workforce-safety-review.md`;
6. `evaluation-design.md`;
7. `evaluation-threat-audit.csv`;
8. `gaming-unintended-effects.md`;
9. `week6-score.csv`;
10. `gate-results.csv`;
11. `module06-handoff.md`;
12. `ai-use.md`;
13. `progression-decision.md`; and
14. `reproducibility-check.md`.

The learner workspace contains 56 files and 41 immutable manifest rows. It includes no accepted scenario outputs and contains explicit placeholders. The reference workspace contains 68 files and 53 manifest rows. The builder refuses an existing target.

## 18. Scoring, gates, and progression

### Point map

| Criterion | Points |
|---|---:|
| Frozen forecast and scenario contract | 3 |
| Model validation and conservation | 5 |
| Scenario comparison | 5 |
| Sensitivity and tradeoffs | 4 |
| Evaluation design and threats | 5 |
| Reproducibility, communication, and responsible AI | 3 |
| Total | 25 |

The reference earns 25 of 25. The score measures the quality of reasoning and evidence, not whether an option wins.

Twenty gates must pass: upstream identity, forecast identity, scenario register, condition register, pairing, time window, run count, priority, capacity and triggers, conservation, nonnegative outputs, calibration, access groups, failed-result retention, safety boundary, return boundary, workforce boundary, causal boundary, implementation boundary, and reproducibility with responsible AI.

Points cannot compensate for a failed gate. The progression record carries the exact 25 points once, all 20 gates, the no-selection decision, failed conditions, and no implementation authority.

Reference progression: `continue with conditions` to Module 06.

## 19. Accessibility, equity, privacy, AI, and software policy

Each SVG has `role="img"`, a title, and a descriptive text alternative. Every plotted value has an exact CSV table. Labels identify scenarios and conditions so interpretation does not rely on color alone. Units, direction, uncertainty, and claim limits remain available in text.

Access review begins with eligibility, event count, missingness, support, and unavailable states. Synthetic differences cannot be turned into traits of real language-support or mobility-support groups. A small modeled gap does not establish equity. A missing or unsupported result is reported as unavailable, not imputed.

The repository contains public aggregate evidence and synthetic encounters only. No protected patient or workforce data enter the model or an external agent. Modeled workload is not employee surveillance.

Agents may explain code, suggest checks, or help draft summaries. They may not alter the accepted forecast, invent values, delete failed runs, select an option, infer unmodeled safety, or authorize implementation. Numeric claims must trace to frozen evidence or deterministic outputs, and the learner remains accountable.

The scenario engine uses the Python standard library. Git records the accepted version. The model deliberately avoids an added simulation dependency because the bounded event queue, checks, and clean-rebuild contract are fully supported without one.

## 20. Runnable acceptance checks and failure routes

From the module directory:

```powershell
python freeze_upstream.py --self-check
python build_scenarios.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

The release check must reproduce 12 output files, 4,000 runs, 20 summaries, 15 paired-effect rows, no selected option, and 6 null or failed sensitivity rows. It must reproduce committed bytes and refuse an existing output target.

The workspace validator rejects at least these failure routes:

- changed upstream evidence;
- wrong score total;
- a failed gate;
- a forced option;
- favorable unmodeled safety language;
- a causal simulation claim;
- implementation authorization;
- hidden failed sensitivity evidence;
- a missing record;
- a changed deterministic output;
- an unfinished reference placeholder; and
- an unsupported progression decision.

Complete validation passes 271 checks, starter validation passes 166 structural checks, and 12 failure routes are rejected. Release review also confirms 24 scenario validations, 18 accepted assumptions, 8 evaluation threats, 20 gates, accessible SVG structure, portable paths, no personal absolute paths, and plain ASCII dashes.

## 21. Release status and Module 06 handoff

Release status: `runnable release candidate`.

The Module 05 release contains:

- exact Module 04 handoff identity;
- 18 accepted assumptions;
- 4,000 deterministic scenario runs;
- 24 passed validation checks;
- 20 scenario-condition summaries;
- 15 paired option effects;
- 6 retained null or failed comparisons;
- 12 prospective measures;
- 8 evaluation threats;
- 25 of 25 course points;
- 20 of 20 gates;
- progression with conditions;
- no selected option; and
- no implementation authority.

Module 06 may assess whether an option can be revised into a credible bounded test, define monitoring and fallback logic, and compare one bounded ML forecast with the accepted transparent method. It may not lower Module 05 thresholds, erase failed evidence, reinterpret simulation as a causal effect, or select an option retrospectively.

The correct next question is not, "Which intervention did the model approve?" It is, "Given that none cleared the declared gates, what additional evidence or revision would make a bounded feasibility decision responsible?"

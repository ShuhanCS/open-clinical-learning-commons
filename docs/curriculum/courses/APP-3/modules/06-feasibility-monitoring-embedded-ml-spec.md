# APP-3 Module 06: Feasibility, monitoring, and embedded machine learning

## 1. Module identity, decision, and release boundary

- Module ID: `oclc-app3-06`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Instructional block: final application block before clinician leadership.
- Source milestone: end of instructional Week 6.
- Student effort: 16.0 hours.
- Application and monitoring: 8.0 hours.
- Embedded machine learning: 8.0 hours.
- Submission: cumulative Week 6 clinical performance package.
- New points in this module: 0.
- Cumulative Week 6 points: 25, counted once from Module 05.
- Module version: `0.1.0`.
- Commons release: `0.72.0`.
- Package: `courses/clinical-performance-improvement/modules/06-feasibility-monitoring-embedded-ml/`.
- Decision: whether any Module 05 option is ready for reconsideration and whether the bounded ML forecast changes the accepted planning input.
- Primary decision owner: `CGH-ED-01 clinical performance and improvement council`.
- Progression decision: `continue`, `continue with conditions`, `revise`, or `refer`.

The learner must turn a no-selection scenario result into a usable leadership package. The correct response is not to force a winner. It is to state what must be revised, what must be monitored, who owns each decision, when leadership should investigate, pause, or roll back, and whether a fixed machine-learning challenger clears every predeclared replacement rule.

This is planning evidence for a fictional clinical service. It does not establish clinical safety, equitable access, causal benefit, required staffing, implementation feasibility, or authority to test, route, schedule, implement, or deploy anything.

## 2. Place in the course and the Week 6 checkpoint

Modules 04 through 06 form the course application block.

| Unit | Hours | Course points | Application role |
|---|---:|---:|---|
| Module 04 demand forecasting and capacity | 16.5 | 0 | transparent demand and uncertainty gate |
| Module 05 improvement scenarios and evaluation | 16.0 | 25 | scored scenario and evaluation component |
| Module 06 feasibility, monitoring, and embedded ML | 16.0 | 0 | feasibility, monitoring, and ML gates |
| Cumulative Week 6 checkpoint | 48.5 | 25 | one accepted application release |

Module 06 accepts the exact Module 04 target, folds, transparent forecast, difficult periods, and Week 53 range. It also accepts the exact Module 05 scenario results, failed conditions, 25-point score, 20 gates, and no-selection decision. It does not rerun Module 05 with new thresholds after seeing feasibility or ML results.

The Week 6 package is complete only when all Module 06 zero-point gates pass. A favorable model result cannot compensate for a forced scenario selection, hidden safety gap, missing access measure, unowned escalation rule, or implementation language.

## 3. Learning outcomes

By the end of Module 06, learners can:

1. preserve a no-selection result instead of selecting the least unfavorable option;
2. distinguish technical promise from implementation readiness;
3. screen redesign options for staffing, scheduling, governance, sustainability, quality, safety, access, and workforce constraints;
4. state a supported disposition for each option;
5. identify evidence needed before a revised option can return for evaluation;
6. translate proposed measures into an accessible monitoring dashboard;
7. define units, denominators, periods, owners, cadence, unavailable states, and claim limits;
8. distinguish investigation, action review, pause review, and rollback review;
9. assign escalation and fallback responsibilities without automating clinical action;
10. explain why a static dashboard design is not a live clinical system;
11. preserve the accepted forecast target, issue time, horizon, folds, and evaluation rows;
12. distinguish features known at issue time from future or uncertain information;
13. explain temporal leakage and training-only preprocessing;
14. fit one fixed gradient-boosted regressor without tuning;
15. compare the challenger and transparent forecast in operational units;
16. interpret MAE, RMSE, bias, WAPE, underforecasting, overforecasting, and weighted cost together;
17. examine difficult folds, subgroups, largest errors, and Week 53 plausibility;
18. apply a predeclared all-rules replacement decision;
19. retain a near miss instead of moving a threshold;
20. explain why feature importance is model allocation rather than causation;
21. document responsible AI use and exact reproducibility; and
22. hand Module 07 an explicit recommendation boundary, open decisions, and accountability map.

## 4. Concept ownership and boundaries

### Module 06 owns

- implementation feasibility screening;
- quality and safety interaction review;
- equity and access review;
- workforce burden review;
- four explicit scenario dispositions;
- 12-measure monitoring design;
- an accessible static dashboard;
- escalation, pause-review, fallback, and rollback-review design;
- monitoring ownership and sustainability;
- one fixed gradient-boosted arrival forecast;
- issue-time feature eligibility;
- rolling temporal evaluation on the accepted 588 rows;
- operational error and difficult-fold review;
- ML failure cases and feature-importance limits;
- the predeclared forecast replacement rule;
- Week 6 score preservation and 22 noncompensable gates; and
- the exact Module 07 handoff.

### Module 06 revisits rather than repeats

- FND-1 through data identity, missingness, source roles, row integrity, and reproducibility;
- FND-2 through prediction error, bias, temporal evaluation, thresholds, and uncertainty;
- DA-730 through an accessible decision dashboard and exact table;
- APP-3 Module 02 through accepted operational measures;
- APP-3 Module 03 through variation, safety undercapture, access support, bottleneck diagnosis, and escalation limits;
- APP-3 Module 04 through forecasting, temporal folds, uncertainty, capacity limits, and failure periods; and
- APP-3 Module 05 through scenario dispositions, evaluation threats, and prospective outcomes.

Every applied course revisits fundamentals for its own decision. This module uses prediction to test whether a planning input should change. It does not become a general machine-learning course, and DA-730 remains the separate concept-first visualization course.

### Out of scope

- weakening Module 05 rules after seeing results;
- selecting S01, S02, or S03 for implementation;
- estimating a causal intervention effect;
- validating a real staffing schedule or clinical pathway;
- creating clinical orders or routing rules;
- declaring a reviewed safety event absent from source data;
- imputing unavailable prospective measures;
- using current target-week outcomes as forecast features;
- using the special-event flag without an accepted issue-time source;
- model tuning, family search, or repeated challenger selection;
- treating feature importance as a mechanism or cause;
- replacing process diagnosis, clinical review, or human ownership with ML;
- live dashboard integration;
- automated alerts or actions;
- testing, implementation, production scoring, or deployment; and
- deciding the final clinician recommendation assigned to Module 07.

## 5. Source authority and frozen handoff

Module 06 freezes selected evidence from two accepted releases.

| Source | Accepted release | Role |
|---|---|---|
| APP-3 Module 04 | `oclc-app3-04@0.1.0+commons.0.70.0` | target, folds, predictions, errors, Week 53 forecast, capacity boundary |
| APP-3 Module 05 | `oclc-app3-05@0.1.0+commons.0.71.0` | scenarios, evaluation, score, gates, no-selection decision |

The accepted analytic facts are:

| Handoff fact | Accepted value |
|---|---:|
| Shift history rows | 1,092 |
| Historical weeks | 52 |
| Rolling folds | 28 |
| Common evaluation rows | 588 |
| Transparent method | seasonal exponential smoothing |
| Transparent MAE | 5.937283 arrivals per shift |
| Transparent RMSE | 7.307180 arrivals per shift |
| Transparent bias | 0.008215 arrivals per shift |
| Transparent WAPE | 15.141268 percent |
| Week 53 point forecast | 876.924084 arrivals |
| Week 53 lower planning value | 805.136639 arrivals |
| Week 53 upper planning value | 970.733035 arrivals |
| Module 05 runs | 4,000 |
| Scenario-condition summaries | 20 |
| Paired option effects | 15 |
| Null or failed comparisons | 6 |
| Module 05 score | 25 of 25 |
| Module 05 gates | 20 of 20 |
| Selected option | none |
| Implementation authority | not authorized |

`freeze_upstream.py` copies the declared source files into the module, records path, bytes, SHA-256, source release, and role, and refuses an existing destination. Verification fails if any frozen byte or accepted fact changes.

## 6. Decision questions and predeclared contracts

The application question is: given the accepted no-selection result, what should leadership retain, revise, stop, monitor, and require before reconsideration?

The ML question is: does one fixed gradient-boosted forecast improve the accepted planning input enough to clear every replacement rule on the exact same temporal evaluation rows?

Both contracts are fixed before fitting the model. Learners may explain limitations or propose a future release. They may not move a threshold, add a feature, tune a parameter, drop a difficult fold, or change an option disposition to obtain a preferred answer.

## 7. Exact scenario dispositions

| Scenario | Disposition | Supported reason | Return condition |
|---|---|---|---|
| S00 no change | retain as monitoring baseline | no redesign qualified under Module 05 | continue monitoring while alternatives are revised |
| S01 flex clinician coverage | revise before reconsideration | improves P90 wait and abandonment but misses the median-wait rule and uses 40.000000 modeled clinician-hours | revise the rule and return through a new scenario contract and all Module 05 gates |
| S02 fast-track activation | stop in current form | worsens median and P90 wait at point demand and under stress | do not reuse without a materially different, clinically reviewed design |
| S03 combined bounded rule | revise before reconsideration | misses both point-demand wait rules and uses 25.220413 modeled flex hours | revise the rule and return through a new scenario contract and all Module 05 gates |

No row says implement, pilot, staff, schedule, or deploy. A revision is a future evidence request, not a conditional authorization.

## 8. Feasibility domains and evidence statuses

Each option is screened across seven domains:

1. staffing availability and role coverage;
2. scheduling and shift fit;
3. clinical governance and scope;
4. quality and safety interaction;
5. equity and access interaction;
6. workforce burden and interruptions; and
7. sustainability, measurement, and ownership.

Each domain receives one of four statuses:

- `supported`: accepted evidence is sufficient for the limited planning claim;
- `requires local evidence`: the question is relevant but the synthetic source cannot answer it;
- `not supported`: accepted evidence contradicts the proposal or a required gate fails; or
- `not applicable`: the domain genuinely does not apply and the reason is recorded.

Unknowns are not scored as favorable. An option cannot become implementation-ready because a required input was unavailable.

## 9. Quality and safety interaction review

The review must ask whether faster flow, higher throughput, new queues, prioritization, handoffs, or added capacity could create harm not represented by the scenario model. It carries forward that reviewed safety-event candidates and 72-hour returns were not simulated.

Required safeguards include:

- immediate clinical review of each safety-event candidate under the declared low-count method;
- follow-up completeness before interpreting 72-hour return rates;
- high-acuity wait monitoring;
- no assumption that lower return or event counts are inherently favorable;
- no routing or scope change without clinical governance; and
- an explicit pause-review path when a safety or high-acuity threshold is crossed.

The record describes questions, measures, owners, and responses. It does not certify safety.

## 10. Equity, access, and workforce review

The access review preserves language-support and mobility-support groups. It reports denominators and unavailable states rather than suppressing small or incomplete groups. A gap more than 5 minutes worse than the standard group triggers pause review, not a conclusion about cause.

The workforce review separates modeled resource use from observed workload. It carries S01's 40.000000 and S03's 25.220413 modeled flex clinician-hours as scenario consequences, not staffing recommendations. Overtime is a planning reference. Interruptions and perceived load require a prospective baseline before any test.

No learner may interpret staff-hours per arrival as individual productivity, infer a staffing level, or treat missing workforce evidence as zero burden.

## 11. Monitoring measure contract

The dashboard carries all 12 accepted Module 05 measures.

| ID | Domain | Measure | Required state |
|---|---|---|---|
| M01 | process | weekly median arrival-to-clinician | simulated planning baseline |
| M02 | process | weekly P90 arrival-to-clinician | simulated planning baseline |
| M03 | outcome | weekly median arrival-to-departure | simulated planning baseline |
| M04 | access | left before seen | simulated planning baseline |
| M05 | flow | completed throughput | simulated planning baseline |
| M06 | capacity | clinician utilization | simulated planning baseline |
| M07 | workforce | overtime hours | simulated planning reference |
| M08 | safety | reviewed safety-event candidates | unavailable prospectively |
| M09 | outcome | return within 72 hours | unavailable prospectively |
| M10 | access | language-support wait gap | simulated planning baseline |
| M11 | access | mobility-support wait gap | simulated planning baseline |
| M12 | workforce | interruptions and perceived workload | unavailable prospectively |

Every measure record contains the unit, direction, display, source period, denominator, owner, cadence, current status, threshold, escalation, unavailable state, and claim limit. An unavailable value is displayed as unavailable, never zero or blank.

## 12. Draft thresholds, escalation, and fallback

| Measure | Draft review threshold | Response level |
|---|---:|---|
| Median arrival-to-clinician | above 70.035963 minutes | investigate |
| P90 arrival-to-clinician | above 151.453267 minutes | investigate |
| Left before seen | above 12.914912 percent | investigate |
| High-acuity median wait | above 60.084398 minutes | pause review |
| Language-support wait gap | above 5 minutes worse | pause review |
| Mobility-support wait gap | above 5 minutes worse | pause review |
| Modeled overtime reference | above 8.715484 hours | investigate |
| Reviewed safety-event candidate | any reviewed candidate | immediate clinical review |
| Return within 72 hours | only after follow-up completeness passes | interpretability gate |
| Interruptions and perceived load | no accepted baseline | baseline required |

These are draft evaluation thresholds derived from accepted planning evidence. They are not statistical control limits, safe staffing values, clinical orders, automatic alert rules, or test-start criteria.

Every escalation record identifies the trigger, confirmer, investigation owner, decision owner, immediate safeguard, fallback state, documentation location, and restart condition. The only available fallback in this release is continued no-change monitoring. A future rollback rule requires an authorized test plan and clinician leadership approval.

## 13. Accessible dashboard contract

The module produces a static HTML dashboard backed exactly by `dashboard-data.csv`. It is a teaching artifact, not a connected operational tool.

The dashboard must:

- use semantic HTML with one `h1` and a logical heading order;
- begin with a visible planning-evidence and no-authorization banner;
- name the fictional service and data period;
- distinguish observed, simulated, and unavailable states with text;
- show each measure's value, unit, status, threshold, owner, and cadence;
- use color only as a secondary cue;
- remain readable at 320 CSS pixels;
- support keyboard reading order;
- include visible focus styles for links;
- include an exact table for all 12 measures;
- avoid motion, scripts, external fonts, and external assets; and
- state that no option or implementation is authorized.

The dashboard is generated as one self-contained HTML file. Its only visualization dependency is native HTML and CSS.

## 14. Machine-learning comparison population

The challenger uses the accepted Module 04 forecasting frame without alteration.

- Target: accepted arrivals per eight-hour shift.
- Issue time: end of the final shift in each completed week.
- Horizon: next 21 shifts over 7 days.
- Initial accepted evaluation issue: end of Week 24.
- Evaluation weeks: 25 through 52.
- Rolling folds: F01 through F28.
- Common evaluation rows: 588.
- Comparator: accepted seasonal exponential smoothing predictions.
- Challenger: one `GradientBoostingRegressor`.
- Random state: 7300600.
- Hyperparameter tuning: prohibited.

Each fold trains only on eligible rows at or before its declared training end week. Both methods are joined by fold ID and exact target shift ID before metrics are calculated.

## 15. Eligible feature and leakage contract

Features must be known at the issue time:

- horizon shift, 1 through 21;
- target week index;
- shift name;
- weekday;
- month;
- known holiday flag;
- arrivals at lags 21, 42, and 63 shifts;
- mean arrivals in the last complete 21-shift week; and
- mean arrivals in the last three complete weeks.

The complete-week means are constant across all 21 targets in a forecast week. No actual value from the target week enters any lag or mean. The first three weeks are ineligible for training because a complete 63-shift history does not exist.

Shift name, weekday, and month are one-hot encoded inside each fold using training rows only. Unknown categories are ignored rather than learned from evaluation data. The special-event flag is excluded because its issue-time knowability is not established. Target outcomes, completed encounters, abandonment, waits, staffing outcomes, future event flags, and post-issue revisions are prohibited.

Leakage checks verify row cutoffs, feature completeness, source weeks, target-week exclusion, preprocessing scope, row identity, and absence of prohibited columns.

## 16. Fixed gradient-boosted model

The model is fixed as follows:

| Parameter | Value |
|---|---|
| Loss | squared error |
| Estimators | 100 |
| Learning rate | 0.05 |
| Maximum depth | 2 |
| Minimum samples per leaf | 15 |
| Maximum features | all eligible features |
| Random state | 7300600 |
| Prediction floor | 0 arrivals |

The supported environment is Python 3.12, NumPy 2.0.2, pandas 3.0.3, and scikit-learn 1.9.0. The builder reports the observed environment and fails when the supported versions are not present. It does not install packages.

Feature importance is reported from one final Week 53 model fitted on all eligible Weeks 1 through 52 rows. Importance is a description of how this fitted model allocated split improvement. It is not a causal estimate, workflow mechanism, or reason to alter care.

## 17. Error measures and operational consequences

For each method, the release reports:

- evaluation rows;
- MAE in arrivals per shift;
- RMSE in arrivals per shift;
- signed bias in arrivals per shift;
- WAPE percent;
- total underforecast arrivals;
- total overforecast arrivals; and
- weighted error cost, with underforecast weight 2 and overforecast weight 1.

Underforecasting may leave too little operational preparation. Overforecasting may direct scarce attention or resources toward demand that does not occur. The weighting is a declared teaching choice, not an estimated financial or clinical cost.

The release also reports fold, shift, weekday, holiday, horizon, and difficult-fold slices, plus the ten largest absolute ML errors. It preserves both favorable and unfavorable results.

## 18. Predeclared model replacement rule

The challenger may replace the transparent forecast input only if all eight rules pass:

1. MAE improves by at least 0.75 arrivals per shift.
2. RMSE does not worsen.
3. WAPE improves by at least 1.00 percentage point.
4. Absolute bias is no more than 1.00 arrival per shift.
5. Weighted error cost improves by at least 5 percent.
6. At least three of F03, F09, F15, and F16 do not worsen by more than 10 percent on MAE.
7. All 588 target rows, cutoffs, feature rules, preprocessing checks, and leakage checks pass.
8. The Week 53 challenger total remains within 805.136639 to 970.733035 arrivals.

The rules are conjunctive. Seven passes and one failure means the challenger does not replace the accepted method. No near-tie tolerance or rounding exception is added after fitting.

## 19. Exact reference ML result

The fixed reference run produces:

| Measure | Transparent | Gradient boosted | Challenger change |
|---|---:|---:|---:|
| MAE | 5.937283 | 5.205494 | 0.731788 lower |
| RMSE | 7.307180 | 6.554934 | 0.752247 lower |
| Bias | 0.008215 | -0.513059 | within 1.00 absolute |
| WAPE | 15.141268% | 13.275060% | 1.866208 percentage points lower |
| Underforecast arrivals | 1743.145980 | 1681.254756 | 61.891224 lower |
| Overforecast arrivals | 1747.976156 | 1379.575834 | 368.400322 lower |
| Weighted error cost | 5234.268116 | 4742.085347 | 9.403087% lower |

The challenger improves RMSE, WAPE, bias bound, weighted cost, and all four difficult folds. Its Week 53 total is 860.277096 arrivals, inside the accepted range. It fails the first rule because its MAE improvement is 0.731788, below 0.750000 by 0.018212 arrivals per shift.

The accepted decision is therefore `retain transparent forecast`. This is a deliberate near-miss teaching result. The threshold is not changed and the challenger is not tuned again.

## 20. ML interpretation and claim limits

The challenger demonstrates that a fixed nonlinear model can improve several historical error measures while still failing a declared replacement rule. That is the decision lesson.

The result does not show that gradient boosting is generally superior, that demand has a causal mechanism captured by the model, that Week 53 will contain 860.277096 arrivals, or that a real service should change staffing. It does not retroactively alter the Module 05 scenarios, because those scenarios were released against the accepted transparent forecast and uncertainty range.

A future challenger release may revise the contract only before seeing new evaluation outcomes. It must use a newly declared holdout period and cannot reuse the 588 rows as fresh confirmation evidence.

## 21. Instructional sequence and 16-hour workload

| Session | Hours | Learner work | Checkpoint |
|---|---:|---|---|
| A. Handoff and dispositions | 1.5 | verify releases, preserve no selection, assign four dispositions | accepted handoff and disposition record |
| B. Feasibility | 2.0 | screen staffing, scheduling, governance, sustainability | feasibility review |
| C. Safety, access, workforce | 2.0 | review unmodeled risks and group effects | three bounded reviews |
| D. Monitoring and escalation | 2.5 | specify 12 measures, thresholds, owners, fallback | dashboard and escalation review |
| E. ML contract and leakage | 2.0 | freeze target, folds, features, parameters, preprocessing | ML contract review |
| F. Fit and compare | 3.0 | run 28 folds and calculate operational errors | model comparison |
| G. Failure cases and Week 53 | 1.5 | inspect slices, large errors, importance, plausibility | failure review |
| H. Decision and handoff | 1.5 | apply all rules, verify gates, prepare Module 07 handoff | Week 6 release |
| Total | 16.0 | 8.0 application and 8.0 ML | 25-point cumulative package |

The instructor reveals the reference output only after learners freeze the decision-change rule. Discussion focuses on why the near miss remains a failure and what leadership can still learn from it.

## 22. Submission and deterministic outputs

The release contains 19 deterministic outputs:

1. `upstream-inventory.csv`;
2. `feasibility-screen.csv`;
3. `monitoring-measures.csv`;
4. `escalation-fallback.csv`;
5. `dashboard-data.csv`;
6. `ml-split-registry.csv`;
7. `ml-predictions.csv`;
8. `model-performance.csv`;
9. `fold-comparison.csv`;
10. `model-error-slices.csv`;
11. `feature-importance.csv`;
12. `failure-cases.csv`;
13. `leakage-tests.csv`;
14. `week53-model-comparison.csv`;
15. `decision-change.csv`;
16. `invariant-checks.csv`;
17. `build-report.json`;
18. `forecast-comparison.svg`; and
19. `monitoring-dashboard.html`.

The learner or reference workspace includes 17 submission records:

1. `feasibility-review.md`;
2. `quality-safety-review.md`;
3. `access-equity-review.md`;
4. `workforce-review.md`;
5. `dashboard-review.md`;
6. `escalation-fallback-review.md`;
7. `monitoring-stewardship.md`;
8. `accountability-map.csv`;
9. `ml-contract-review.md`;
10. `model-comparison.md`;
11. `failure-review.md`;
12. `week6-score.csv`;
13. `gate-results.csv`;
14. `module07-handoff.md`;
15. `ai-use.md`;
16. `progression-decision.md`; and
17. `reproducibility-check.md`.

The builder refuses an existing target. Reference workspaces include immutable outputs and complete records. Learner workspaces contain explicit placeholders and no accepted Module 06 outputs. Both include a sorted SHA-256 release manifest.

## 23. Scoring, gates, and progression

### Point map

| Component | Points available | Points in Module 06 |
|---|---:|---:|
| Module 04 forecast gate | 0 | 0 |
| Module 05 scenario and evaluation | 25 | 0 new points |
| Module 06 application, monitoring, and ML gates | 0 | 0 |
| Cumulative Week 6 package | 25 | 25 counted once |

The 22 noncompensable gates are:

1. exact upstream identity;
2. retained no-selection handoff;
3. four supported scenario dispositions;
4. implementation feasibility evidence;
5. quality and safety boundary;
6. access and equity boundary;
7. workforce burden boundary;
8. all 12 measures specified;
9. accessible bounded dashboard;
10. escalation and fallback ownership;
11. monitoring stewardship and sustainability;
12. exact target, issue time, and horizon;
13. 28 folds and 588 common rows;
14. eligible issue-time features only;
15. training-only categorical preprocessing;
16. one fixed untuned model;
17. operational-unit error reporting;
18. difficult periods and failure cases retained;
19. all eight replacement rules applied;
20. 25 points counted once;
21. no clinical, staffing, testing, implementation, or deployment authority; and
22. reproducibility and responsible AI records complete.

All 22 must pass. The supported reference progression is `continue with conditions`: carry the no-selection decision, retain the transparent forecast, complete clinician leadership review, and do not implement.

## 24. Accessibility, equity, privacy, AI, and software policy

All prose uses plain ASCII dashes and plain language. Tables retain exact values and units. The SVG includes a title, description, text labels, and a non-color distinction. The dashboard meets the static accessibility contract in Section 13.

The source is synthetic and identifies no real patient, clinician, worker, or hospital. Public clinical sources provide definition and historical aggregate context elsewhere in the course, but this module does not link public data to the synthetic records.

Learners record whether AI assisted code, prose, interpretation, or review. AI may help explain or check work, but the learner remains responsible for source identity, leakage prevention, model fitting, errors, option dispositions, limits, and the final decision. AI may not invent unavailable safety, access, or workforce data.

No new package is installed. The release uses Python, NumPy, pandas, scikit-learn, and native HTML/CSS already supported by the course environment.

## 25. Runnable acceptance checks and failure routes

The validator checks exact file sets, manifest identity, upstream hashes, module identity, versions, hours, points, scenario dispositions, measure count, dashboard structure, ML rows, temporal cutoffs, eligible features, model parameters, predictions, metrics, difficult folds, Week 53 values, decision rules, score accounting, gates, progression, claim limits, ASCII dashes, portable paths, and deterministic regeneration.

The self-check assembles and validates one complete reference and one learner starter. It also proves rejection of at least these failures:

- changed upstream evidence;
- forced scenario selection;
- implementation authorization;
- missing feasibility domain;
- unsupported safety claim;
- missing access measure;
- hidden workforce burden;
- inaccessible or unbounded dashboard;
- wrong target rows;
- changed model parameter;
- target-week leakage;
- dropped difficult fold;
- changed decision threshold;
- accepted ML despite a failed rule;
- duplicate Week 6 points;
- failed gate;
- incomplete learner record; and
- unsupported progression decision.

Deterministic regeneration must reproduce every committed output byte for byte.

The accepted reference passes 354 complete checks. The learner starter passes 183 structural checks. The validator rejects all 18 failure routes above.

## 26. Release status and Module 07 handoff

The reference release status is `runnable release candidate`. It carries:

- Module 05 option: none;
- scenario disposition: retain S00, revise S01, stop S02, revise S03;
- Module 05 score: 25 of 25;
- Module 06 gates: 22 of 22;
- accepted forecast: seasonal exponential smoothing;
- ML decision: retain transparent forecast;
- Week 6 cumulative score: 25 points once;
- progression: continue with conditions; and
- implementation authority: not authorized.

Module 07 receives the exact package for clinician leadership and defense. It may decide how to communicate the recommendation, assign further evidence work, or refer an unresolved issue. It may not erase failed evidence, treat the ML challenger as accepted, certify safety, or authorize implementation without a separate governed process.

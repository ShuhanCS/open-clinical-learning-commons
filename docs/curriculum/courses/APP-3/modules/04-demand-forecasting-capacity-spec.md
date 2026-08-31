# APP-3 Module 04: Demand forecasting and capacity

## 1. Module identity, decision, and release boundary

- Module ID: `oclc-app3-04`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Instructional block: application block after the Week 3 checkpoint.
- Student effort: 16.5 hours.
- Submission: required forecasting and capacity gate for the Week 6 package.
- Course points: 0.
- Module version: `0.1.0`.
- Commons release: `0.70.0`.
- Package: `courses/clinical-performance-improvement/modules/04-demand-forecasting-capacity/`.
- Decision: whether one transparent arrival-demand forecast is adequate input for Module 05 scenario construction, and what bounded planning range follows from its observed error.
- Primary decision owner: `CGH-ED-01 clinical performance and improvement council`.
- Progression decision: `continue`, `continue with conditions`, `revise`, or `refer`.

The learner must answer a practical planning question: what can the service reasonably carry forward about next week's arrivals when only information available at the forecast issue time is used? A successful answer names the demand target, cutoff, horizon, eligible history, comparison methods, selection rule, error consequences, failure periods, uncertainty, and capacity limits before it recommends progression.

This is a synthetic teaching analysis. It may support construction of Module 05 improvement scenarios. It does not guarantee demand, establish required staffing, rate productivity, prove equilibrium, diagnose root cause, order a schedule, authorize clinical action, automate a decision, or permit implementation.

## 2. Place in the course and Week 6 package

Checkpoint 01 freezes the first three modules and releases Module 04 with conditions. Modules 04 through 06 form the application block.

| Unit | Course points | Application role |
|---|---:|---|
| Module 04 demand forecasting and capacity | 0 | required transparent forecast and planning-range gate |
| Module 05 improvement scenarios and evaluation | 25 | scored Week 6 component |
| Module 06 feasibility, monitoring, and embedded ML | 0 | required feasibility, monitoring, and ML comparison gates |
| Week 6 total | 25 | counted once at the cumulative checkpoint |

Module 04 accepts the Week 3 evidence without changing it. Module 05 may use the accepted forecast and uncertainty range to configure scenarios. Module 06 later compares one bounded machine-learning forecast with the transparent method on the same target, cutoff, folds, horizon, and evaluation rows.

The module is a noncompensable gate. Its zero-point status means it does not add course points. It does not mean the work is optional. A later score cannot compensate for leakage, an altered forecast contract, hidden error, an unsupported staffing conclusion, or a failed progression boundary.

## 3. Learning outcomes

By the end of Module 04, learners can:

1. define a forecast as a target, unit, decision, issue time, information cutoff, and horizon;
2. distinguish forecast-time information from retrospective error-review information;
3. construct expanding rolling-origin folds without using future observations;
4. explain why random train-test splitting is invalid for this weekly staffing horizon;
5. implement and interpret a last-value benchmark;
6. implement a seasonal-naive benchmark with the correct 21-shift lag;
7. implement bounded additive seasonal exponential smoothing with fixed parameters;
8. compare all methods on identical target rows;
9. select a method with a predeclared primary metric and simplicity tie rule;
10. interpret MAE, RMSE, signed bias, and WAPE in the context of arrival demand;
11. preserve under-forecast and over-forecast consequences separately;
12. identify difficult folds, calendar slices, unsupported slices, and adaptation failures;
13. produce a one-week forecast with an empirical actual-equivalent range;
14. translate arrivals into a historical planning-equivalent range without defining staffing need;
15. use Little's Law only as a bounded consistency check when its assumptions are not met;
16. communicate numeric evidence through accessible tables, figures, and plain language;
17. defend what the forecast permits and prohibits; and
18. hand Module 05 an exact, reproducible, condition-bearing forecast release.

## 4. Concept ownership and boundaries

### Module 04 owns

- the accepted arrival-demand target;
- forecast issue time, cutoff, and one-week horizon;
- the 28 expanding rolling-origin folds;
- last-value and seasonal-naive benchmarks;
- bounded seasonal exponential smoothing;
- common-row method comparison;
- selection rule and tie handling;
- shift, weekday, holiday, special-event, and season error review;
- separate under-forecast and over-forecast totals;
- Week 53 point forecast and empirical range;
- historical planning-equivalent conversion;
- bounded Little's Law consistency checks;
- forecast accessibility review;
- Module 05 handoff; and
- all 18 zero-point progression gates.

### Module 04 revisits rather than repeats

- FND-1 data quality by protecting row order, dates, units, missingness, and release identity;
- FND-2 prediction evaluation by applying time-ordered validation to a clinical operations decision;
- DA-730 visual communication by making units, uncertainty, comparison, and claim limits visible;
- APP-3 Module 02 by using accepted operational measures without redefining them; and
- APP-3 Module 03 by preserving the diagnosed time window, signal uncertainty, safety limits, and action boundary.

DA-730 remains the separate concept-first visualization course. This module uses two simple figures because they help defend a forecast decision. It does not become a chart-design survey.

### Out of scope

- changing the accepted encounter population, repairs, measure definitions, clocks, or Week 3 diagnosis;
- filling unavailable public or synthetic states with invented values;
- random cross-validation;
- tuning smoothing parameters on evaluation results;
- using holiday or special-event truth that would not be known at issue time;
- fitting machine learning;
- simulating a staffing or workflow redesign;
- estimating an intervention effect;
- establishing staffing adequacy or required hours;
- measuring individual clinician productivity;
- claiming queue equilibrium;
- clinical decision making;
- automated staffing, scheduling, or routing;
- authorizing a real-world test; and
- implementation.

Module 05 owns scenario construction and evaluation. Module 06 owns feasibility, monitoring, and the embedded ML comparison. Module 07 owns clinician leadership, recommendation, and final defense.

## 5. Source authority and frozen checkpoint handoff

The authoritative input is Checkpoint 01, `oclc-app3-cp01` version `0.1.0` at Commons release `0.69.0`.

| Handoff fact | Accepted value |
|---|---:|
| Checkpoint candidate files | 137 |
| Candidate manifest bytes | 23,862 |
| Candidate manifest SHA-256 | `9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656` |
| Frozen analytic files | 23 plus handoff manifest |
| Accepted synthetic encounters | 43,628 |
| Consecutive shifts | 1,092 |
| Complete weeks | 52 |
| Week 3 course points | 40 of 40 |
| Module 04 permission | permitted for demand forecasting and capacity analysis |

`freeze_upstream.py` assembles the accepted checkpoint reference, verifies its exact file count and manifest identity, and copies the analytic subset needed for forecasting. The subset includes checkpoint identity and decision records, Module 02 demand and staffing measures, and Module 03 variation, bottleneck, subgroup, and escalation evidence.

`checkpoint-handoff-manifest.csv` records path, source, bytes, SHA-256, release identity, and role for each frozen file. Any missing or changed byte fails validation. The complete 137-row checkpoint candidate manifest remains the chain of custody for accepted files outside the analytic subset.

The principal analytic table is `upstream/shift-metrics.csv`. It has one row per eight-hour shift from 2024-01-01 through 2024-12-29 in fixed night, day, evening order. Every analytic row has `synthetic_flag = 1`.

## 6. Forecast question and predeclared contract

The forecast contract is fixed before a method is fitted.

| Item | Contract |
|---|---|
| Target | accepted arrivals per eight-hour shift |
| Unit | synthetic arrivals per shift |
| Decision | adequacy for Module 05 scenario construction and bounded planning implication |
| Issue time | end of the final shift in each completed week |
| Information cutoff | no observation at or after the first target shift enters that fold fit |
| Horizon | next 21 consecutive shifts |
| Calendar length | seven days |
| Staffing horizon | one planning week |
| Initial training | Weeks 1 through 24, 504 shifts |
| Evaluation | Weeks 25 through 52 |
| Seasonal period | 21 shifts |
| Primary metric | MAE in arrivals per shift |
| Secondary metrics | RMSE, signed bias, and WAPE |
| Tie tolerance | 0.25 arrivals per shift |

The contract makes the forecast reproducible and decision-specific. A daily target would hide within-day staffing patterns. A longer horizon would answer a different planning question. A random split would allow later seasonal and event information to influence an earlier issue date.

Weekday and shift position define the seasonal cycle. Holiday and synthetic special-event fields are kept for retrospective error slices. They are not used as future outcome information. A production forecast could use a genuinely known calendar, but this teaching release does not add a holiday effect because the eligible-history evidence is too small to support one.

## 7. Rolling-origin evaluation and information eligibility

The evaluation has 28 expanding folds. Each fold trains through a completed week and predicts the next 21 shifts.

| Fold element | Rule |
|---|---|
| First origin | train Weeks 1-24, test Week 25 |
| Last origin | train Weeks 1-51, test Week 52 |
| Training update | append the newly observed test week before the next issue |
| Test rows per fold | 21 |
| Evaluation rows per method | 588 |
| Common-row rule | every eligible method predicts every accepted test row |
| Forecast floor | 0 arrivals |

For every fold, the audit records issue shift, issue date, training end week, training rows, test week, test dates, horizon, special-event exposure, actual weekly arrivals, forecast weekly arrivals, signed weekly error, and fold MAE.

Forecast eligibility requires:

1. the exact accepted source order;
2. a complete training history through the issue shift;
3. no future target or event information;
4. exactly 21 nonnegative predictions;
5. the same 588 evaluation rows used by every method;
6. no hidden deletion of difficult periods;
7. no evaluation-driven parameter tuning; and
8. exact preservation of fold identity in the output.

The learner must explain why a method could have run at each issue time. A numerically strong result that violates this eligibility contract is rejected.

## 8. Candidate methods and implementation rules

### Method 1: last value

Repeat the final observed shift arrival count for all 21 forecast horizons. This method is intentionally simple. It tests whether the added seasonal structure earns its complexity.

### Method 2: seasonal naive

Use the arrival count from the prior week for the same weekday and shift. The lag is exactly 21 rows because each day has night, day, and evening shifts. A lag of 7 would compare different shift positions and fails the gate.

### Method 3: seasonal exponential smoothing

Use an additive level and 21-position seasonal state with:

- no trend;
- `alpha = 0.30`;
- `gamma = 0.20`;
- initial level equal to the mean of the first 21 shifts;
- initial seasonal values equal to each first-week observation minus that level;
- recursive level and seasonal updates from the second week onward; and
- a nonnegative forecast floor.

The values of alpha and gamma are fixed. No fold, search, package default, or evaluation result may change them. The implementation uses the Python standard library and has no external runtime dependency.

These methods form a deliberate complexity ladder. The module does not fit autoregression, Prophet, neural networks, gradient boosting, or a production scheduling model. Module 06 owns one bounded ML comparison under the frozen contract.

## 9. Selection rule and operational error

All methods are scored on the same 588 shifts.

- MAE is the primary measure because it reports typical absolute error in arrivals per shift.
- RMSE is secondary and gives more weight to large misses.
- Signed bias shows the average direction of error but can cancel large opposing misses.
- WAPE expresses total absolute error relative to total observed arrivals.
- Under-forecast arrivals sum the magnitude of negative forecast errors.
- Over-forecast arrivals sum positive forecast errors.

The eligible method with the lowest MAE is selected. If any simpler method is within 0.25 arrivals per shift of the best MAE, the simpler method wins in this order: last value, seasonal naive, then smoothing.

Under-forecast and over-forecast errors are never collapsed into one operational consequence. Under-forecasting may create pressure on queues, staff, and access. Over-forecasting may create unused planned capacity or unnecessary cost. The release does not assign money, safety events, or staffing decisions to either direction because the accepted evidence does not identify those causal consequences.

## 10. Exact reference method comparison

Across 588 evaluation shifts per method:

| Method | MAE | RMSE | Bias | WAPE | Under-forecast arrivals | Over-forecast arrivals |
|---|---:|---:|---:|---:|---:|---:|
| Last value | 10.775510 | 13.291345 | -3.391156 | 27.479724% | 4,165.000000 | 2,171.000000 |
| Seasonal naive | 7.095238 | 9.060079 | -0.149660 | 18.094288% | 2,130.000000 | 2,042.000000 |
| Seasonal exponential smoothing | 5.937283 | 7.307180 | 0.008215 | 15.141268% | 1,743.145982 | 1,747.976153 |

Seasonal exponential smoothing is selected. Its MAE is more than 0.25 arrivals below seasonal naive, so the simplicity tie rule does not change the result.

The selected model's near-zero aggregate bias is not evidence of small operational error. It still misses by 5.937283 arrivals per shift on average. Across the 28 weekly folds, mean absolute total error is 64.678197 arrivals. The model is accepted as the best eligible transparent option, not as a guarantee of future arrivals.

## 11. Error slices, difficult periods, and structural change

The selected method is reviewed by shift, weekday, holiday, synthetic special-event status, and season. A slice with fewer than 21 rows is marked not supported.

| Review | Reference result | Interpretation |
|---|---:|---|
| Day-shift MAE | 6.474502 | largest shift MAE |
| Evening-shift MAE | 6.363190 | remains operationally material |
| Night-shift MAE | 4.974155 | smallest shift MAE |
| Special-event MAE | 5.956421 across 126 rows | supported retrospective slice |
| Routine MAE | 5.932063 across 462 rows | similar average absolute error |
| Holiday MAE | 4.004068 across 9 rows | not supported |

The four difficult folds carried into Module 05 are:

- F03, Week 27: the model under-forecasts the start of the special-event window by 151.431012 arrivals for the week;
- F09, Week 33: the highest fold MAE, 8.174933 arrivals per shift, occurs after the special-event window and over-forecasts weekly arrivals by 145.433773;
- F15, Week 39: the model over-forecasts by 152.923903 weekly arrivals; and
- F16, Week 40: the next fold reverses direction and under-forecasts by 146.711332.

The evidence is consistent with difficulty adapting to abrupt shifts and reversals. It does not establish why those shifts occurred. The model must not remove the special-event window, the post-event period, or any high-error fold as noise.

Residual review in this module is descriptive. Learners inspect direction, magnitude, calendar position, repeated failure, and unsupported slices. Formal residual stationarity or independence claims are not required and are not supported by the small number of weekly folds.

## 12. Week 53 forecast and empirical uncertainty

The selected model is refit through Week 52 and issued after the final shift on 2024-12-29. It predicts 21 shifts from 2024-12-30 through 2025-01-05.

- Raw forecast total: 876.924084 arrivals.
- Sum of shift-level half-up rounded forecasts: 878 arrivals.
- Point forecast status: future synthetic planning estimate; actual unavailable.

Uncertainty uses the 28 selected-model weekly total errors. The 10th and 90th percentiles are calculated with linear interpolation on the ordered fold totals. Inverting those errors around the Week 53 forecast gives an empirical actual-equivalent range:

- lower: 805.136639 arrivals;
- upper: 970.733035 arrivals.

This range is a transparent backtest summary, not a calibrated probabilistic prediction interval. It inherits the limited 28-week evaluation history and observed structural changes. Learners must preserve both the point and range. Module 05 must not configure only the point forecast.

Shift-level outputs retain date, shift name, horizon position, raw forecast, rounded planning arrivals, holiday flag, actual-unavailable status, and synthetic flag. Rounding occurs only for presentation. All capacity calculations use the raw total.

## 13. Capacity-planning implication and action boundary

The accepted baseline planning anchor is the median clinician staff-hours per arrival across accepted shifts in Weeks 1 through 24: 0.960000 clinician-hours per arrival.

| Quantity | Value |
|---|---:|
| Week 53 point planning conversion | 841.847121 clinician-hours |
| Lower planning conversion | 772.931174 clinician-hours |
| Upper planning conversion | 931.903714 clinician-hours |
| Baseline weekly clinician-hours minimum | 822 |
| Baseline weekly clinician-hours median | 842 |
| Baseline weekly clinician-hours maximum | 852 |
| Weekly forecast-error conversion | 62.091069 clinician-hours |

The point conversion is close to the historical baseline median, but the uncertainty range extends below the historical minimum and above the historical maximum. That crossing is the central capacity finding. It shows why one point estimate cannot support a staffing order.

The 0.96 factor is a historical planning conversion. It is not:

- a required staffing ratio;
- a safe minimum;
- a productivity standard;
- a causal estimate of hours needed for one arrival;
- evidence that observed staffing was adequate;
- a shift schedule; or
- permission to add or remove clinician hours.

The capacity record may inform Module 05 scenario bounds. A named clinical and operational authority would still need workload, skill mix, breaks, coverage, boarding, acuity, labor rules, safety, access, and workforce evidence before considering a real staffing decision.

## 14. Little's Law consistency check

The module calculates arrival rate per hour multiplied by median arrival-to-clinician hours and compares the product with the accepted mean queue-end snapshot.

| Context | Arrival rate/hour | Median elapsed hours | Product | Mean queue snapshot | Signed gap |
|---|---:|---:|---:|---:|---:|
| Weeks 1-24, all shifts | 5.101935 | 1.625000 | 8.290644 | 8.286086 | 0.004557 |
| Weeks 25-52, all shifts | 4.901573 | 1.616667 | 7.924210 | 7.999681 | -0.075471 |
| Weeks 35-44, evening | 5.269643 | 1.933333 | 10.187976 | 9.702679 | 0.485298 |
| Weeks 45-52, evening | 5.470982 | 1.650000 | 9.027121 | 9.029018 | -0.001897 |

Equilibrium is not established. The arithmetic mixes:

- accepted arrivals as the arrival rate numerator;
- a median elapsed time rather than the required mean time in a common system;
- a sampled mean queue-end state rather than a time-average number in the same system;
- priority classes;
- abandonment;
- blocking and boarding;
- changing capacity;
- nonstationary demand and delay; and
- a stage definition that may not align with the queue snapshot.

The calculation is therefore a bounded consistency check. It may prompt a learner to reconcile units and definitions. It cannot solve for staff, prove that staffing caused a queue, or establish a stable queueing system.

## 15. Instructional sequence and workload

| Learning activity | Hours | Required evidence |
|---|---:|---|
| Inspect checkpoint identity and accepted measures | 1.0 | upstream chain-of-custody note |
| Declare target, decision, cutoff, horizon, and error consequences | 2.0 | forecast plan |
| Build and audit 28 rolling-origin folds | 2.0 | fold audit |
| Fit and interpret last-value and seasonal-naive benchmarks | 2.5 | common-row comparison |
| Fit bounded seasonal exponential smoothing | 2.5 | fixed-parameter comparison |
| Review metrics, error direction, slices, and difficult folds | 2.0 | model and failure review |
| Convert forecast uncertainty and assess Little's Law limits | 2.0 | capacity and queue interpretations |
| Complete accessibility, gates, handoff, reproduction, and defense | 2.5 | final learner records |
| Total | 16.5 | complete Module 04 submission |

The recommended order is contract first, folds second, methods third, interpretation fourth. Instructors should stop a learner who begins model selection before the issue time and eligible history are explicit.

Suggested checkpoints within the module are:

1. contract review before any forecast output;
2. fold review after F01, F03, F09, and F28 are traced by hand;
3. method review before opening the accepted comparison;
4. capacity review before a progression decision; and
5. brief defense using the Week 53 point and range.

## 16. Submission, outputs, and workspace contract

### Learner records

The learner submits 12 records:

1. `forecast-plan.md`;
2. `fold-audit.csv`;
3. `model-comparison.md`;
4. `failure-period-review.md`;
5. `capacity-interpretation.md`;
6. `littles-law-interpretation.md`;
7. `accessible-output-review.md`;
8. `gate-results.csv`;
9. `module05-handoff.md`;
10. `ai-use.md`;
11. `progression-decision.md`; and
12. `reproducibility-check.md`.

### Deterministic reference outputs

`build_forecast.py` creates ten outputs:

| Output | Rows or role |
|---|---|
| `folds.csv` | 28 rolling origins |
| `forecast-predictions.csv` | 1,764 method-fold-shift predictions |
| `error-summary.csv` | 3 method summaries |
| `error-slices.csv` | 17 selected-model slices |
| `week53-forecast.csv` | 21 future shifts |
| `capacity-implication.csv` | 13 planning quantities |
| `littles-law-check.csv` | 4 contexts |
| `forecast-findings.json` | release findings |
| `forecast-error-comparison.svg` | accessible method comparison |
| `week53-demand-forecast.svg` | accessible future-shift forecast |

### Workspace assembly

`build_workspace.py` creates:

- a 49-file learner workspace with 36 immutable manifest rows; or
- a 59-file reference workspace with 46 immutable manifest rows.

The learner workspace excludes the ten accepted outputs and uses explicit `REPLACE` prompts. The reference workspace includes accepted outputs and complete records. The builder refuses to overwrite an existing target and produces a file-level release manifest.

## 17. Gates, scoring, and progression

Module 04 awards zero course points and has 18 noncompensable gates.

| Gate | Required evidence |
|---|---|
| G01 | checkpoint handoff identity |
| G02 | target and decision declared |
| G03 | issue time, cutoff, and horizon declared |
| G04 | no future leakage |
| G05 | 28 common rolling origins |
| G06 | three eligible methods compared |
| G07 | seasonal lag and smoothing values fixed |
| G08 | primary and secondary errors reported |
| G09 | under and over errors separated |
| G10 | failure periods reviewed |
| G11 | calendar slice support retained |
| G12 | Week 53 uncertainty retained |
| G13 | capacity conversion bounded |
| G14 | no staffing recommendation |
| G15 | Little's Law limits retained |
| G16 | accessible outputs reviewed |
| G17 | reproducibility confirmed |
| G18 | Module 05 permission and boundaries explicit |

All 18 gates must pass. The reference decision is `continue with conditions`. Module 05 permission is `permitted for improvement scenario and evaluation construction`.

A `revise` decision returns the learner to the failed record or computation. A `refer` decision is appropriate when the forecast decision requires unavailable operational or clinical authority. No decision may skip a failed gate or change Week 3 evidence inside Module 04.

## 18. Common errors and instructor interventions

| Error | Why it fails | Instructor response |
|---|---|---|
| Start with a model instead of a decision | target and information eligibility become movable | require the forecast plan before code |
| Use a random split | later observations can influence earlier forecasts | rebuild all 28 rolling origins |
| Use lag 7 | compares different shift positions | trace one week of row order and restore lag 21 |
| Tune alpha or gamma on evaluation folds | leaks performance feedback into the method | restore 0.30 and 0.20 and rerun |
| Add future special-event truth | gives the model information unavailable at issue time | remove it from fitting and keep it as an error slice |
| Report only WAPE or bias | hides error in arrivals and opposing misses | add MAE, RMSE, under, and over totals |
| Remove F03 or F09 | hides structural-change failure | restore every accepted fold |
| Treat nine holiday rows as stable | support is too small | mark the holiday slice not supported |
| Turn 0.96 into required staffing | historical conversion is not a need estimate | rewrite as a planning-equivalent range |
| Solve for staff with Little's Law | the fields and assumptions do not form one equilibrium system | state the definition mismatch and prohibit staffing use |
| Carry only the point forecast | suppresses observed weekly uncertainty | carry 805.136639 to 970.733035 into Module 05 |
| Claim a better forecast proves a better intervention | forecast accuracy and scenario effect are different questions | defer intervention comparison to Module 05 |

An instructor should treat an unexpectedly strong method as a leakage prompt, not automatic success. Ask which rows, flags, parameters, and preprocessing states were available at each issue time.

## 19. Accessibility, equity, privacy, AI, and software policy

### Accessibility

Every figure has an SVG title, description, visible units, text labels, and table-first evidence. Method identity does not depend on color. Forecast status distinguishes future estimates from observed values. The plain-language summary gives both the point and range.

### Equity and workforce

This module does not estimate subgroup demand because the accepted target is service-level arrivals and the Week 3 target-window subgroup evidence is limited. A learner may not allocate or withdraw capacity by language, disability, race, ethnicity, payer, or another protected characteristic. Module 05 must examine access and workforce consequences across every scenario.

Capacity language must recognize who may carry workload, who may wait, and who may be excluded by a narrow operating plan. Those questions are carried forward as scenario and feasibility requirements, not answered by the forecast alone.

### Privacy and source boundary

All linked operational rows are synthetic. Public aggregate sources supplied definitions and context in Module 01 but are not linked to the fictional service. Learner records contain no public-to-synthetic identity claim and no personal absolute path.

### AI and software

The release implementation uses the Python standard library. No dependency is added for forecasting, CSV work, quantiles, SVG generation, or validation. `verify_forecast.R` gives an independent base-R calculation of the method metrics and Week 53 total.

The reference AI record states that generative AI was not used as analytic evidence. Any learner AI use must be disclosed with task, input boundary, output role, verification, and rejected suggestions. AI cannot supply a missing source, authorize staffing, repair leakage, or replace the learner's defense.

Rscript is unavailable in the construction environment. The base-R script is committed and named as a required independent check before alpha rather than silently treated as executed.

## 20. Runnable acceptance checks and failure routes

The accepted package runs:

```powershell
python freeze_upstream.py --self-check
python build_forecast.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
Rscript verify_forecast.R
```

The first four commands currently pass. The validator reports:

- complete reference: 255 checks;
- learner starter: 151 checks; and
- 19 rejected mutation or incomplete-submission routes.

The failure routes cover:

1. changed upstream evidence;
2. missing upstream evidence;
3. changed target;
4. missing fold;
5. future leakage;
6. wrong selected method;
7. wrong MAE;
8. hidden error direction;
9. failed gate;
10. missing record;
11. staffing claim;
12. equilibrium claim;
13. unsupported holiday overclaim;
14. changed capacity result;
15. removed Little's Law boundary;
16. invalid progression;
17. staffing authority in the Module 05 handoff;
18. changed deterministic output; and
19. a placeholder submitted as complete.

The upstream, forecast, and workspace builders also verify deterministic identity and refuse existing targets. A clean forecast rebuild must match all ten committed outputs byte for byte.

## 21. Release status, review requirements, and Module 05 handoff

### Release status

- Module package: runnable release candidate.
- Module version: `0.1.0`.
- Commons release: `0.70.0`.
- Reference gates: 18 of 18 pass.
- Course points: 0.
- Progression: `continue with conditions`.
- Module 05 permission: `permitted for improvement scenario and evaluation construction`.
- Staffing recommendation: not authorized.
- Implementation authority: not authorized.

### Required review before alpha

- run `verify_forecast.R` in an environment with Rscript;
- complete independent reproduction of the frozen handoff and ten outputs;
- complete named clinical operations review of the demand target and planning horizon;
- complete named workforce review of the capacity language;
- review the synthetic seasonal and special-event construction;
- review the accessibility of both figures and verbal summary;
- confirm that Module 05 preserves the range and difficult folds; and
- assign the official APP-3 half-term dates from the published academic calendar.

### Known limits

- the history contains only 52 synthetic weeks;
- evaluation has 28 weekly folds;
- the holiday slice has only nine shifts;
- the empirical range is not a calibrated coverage claim;
- the smoothing parameters are fixed for teaching, not optimized for production;
- the planning conversion omits skill mix, acuity, breaks, coverage, boarding, and labor constraints;
- Little's Law assumptions are not established; and
- no real service, patient, clinician, or staffing decision is represented.

### Module 05 handoff

Module 05 receives:

- seasonal exponential smoothing as the accepted transparent method;
- 876.924084 forecast arrivals for Week 53;
- the 805.136639 to 970.733035 empirical arrival range;
- the 772.931174 to 931.903714 historical planning-equivalent clinician-hour range;
- 64.678197 mean absolute weekly arrival error;
- separate under- and over-forecast consequences;
- F03, F09, F15, and F16 as difficult folds;
- the unsupported holiday slice;
- the bounded roomed-to-clinician diagnosis from Week 3;
- no staffing recommendation; and
- no scenario-effect, clinical, automated, or implementation authority.

The next durable unit is APP-3 Module 05, `Improvement scenarios and evaluation`. It must compare no change with at least two redesign scenarios, preserve uncertainty and failed runs, report process, access, safety, workforce, and balancing consequences, and keep scenario evidence separate from real intervention effect.

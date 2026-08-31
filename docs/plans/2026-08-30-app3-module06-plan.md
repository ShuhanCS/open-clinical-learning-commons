# APP-3 Module 06 build plan

## Goal and release boundary

Build `oclc-app3-06`, Feasibility, monitoring, and embedded machine learning, as a 16.0-hour runnable release candidate. The module uses eight hours for application and monitoring and eight hours for one bounded gradient-boosted arrival forecast.

Module 06 adds no course points. It carries the accepted Module 05 score of 25 points into the cumulative Week 6 release exactly once. The first module release is `0.1.0`, and the Commons release target is `0.72.0`.

The release may support Module 07 clinician leadership review. It may not select an option that Module 05 rejected, revise Module 05 thresholds after seeing results, claim a simulated or causal effect, define required staffing, route patients, authorize a test, implement a workflow, or deploy a model.

## Accepted handoff

The release freezes exact evidence from APP-3 Modules 04 and 05:

- transparent forecast method: seasonal exponential smoothing;
- target: accepted arrivals per eight-hour shift;
- horizon: 21 shifts over 7 days;
- evaluation: 28 expanding rolling-origin folds and 588 common target shifts;
- transparent MAE: 5.937283 arrivals per shift;
- transparent RMSE: 7.307180 arrivals per shift;
- Week 53 point forecast: 876.924084 arrivals;
- empirical range: 805.136639 to 970.733035 arrivals;
- Module 05 runs: 4,000;
- Module 05 option-condition summaries: 20;
- Module 05 paired effects: 15;
- Module 05 null or failed comparisons: 6;
- Module 05 score: 25 of 25;
- Module 05 gates: 20 of 20;
- option for feasibility review: none;
- progression: continue with conditions;
- safety and 72-hour return: not simulated; prospective measurement required; and
- implementation authority: not authorized.

The frozen handoff must include the exact Module 04 forecast inputs and results plus the exact Module 05 release, contract, outputs, decision records, evaluation design, score, gates, and progression record. Every file is checked by path, bytes, and SHA-256.

## Source Week 6 ownership

The source Week 6 work owns:

- implementation feasibility;
- quality and safety interactions;
- equity and access effects;
- workforce burden;
- an accessible measurement dashboard;
- escalation and fallback thresholds; and
- monitoring and sustainability.

The new curriculum adds an eight-hour embedded ML comparison. The ML work must use the accepted forecast target, cutoffs, folds, horizon, and evaluation rows. It may challenge or fail to improve the transparent method. It cannot replace process diagnosis, scenario evidence, safety review, access review, human ownership, or the simpler benchmark.

## Application and monitoring decision

Because Module 05 selected no option, Module 06 will not pretend that an implementation proposal exists. It will make four explicit dispositions:

1. S00 no change: retain as the monitoring baseline while evidence is revised.
2. S01 flex coverage: revise before reconsideration because it improves P90 wait and abandonment but misses the median-wait rule and requires 40 modeled clinician-hours.
3. S02 fast track: stop in its current form because it worsens median and P90 waits, including under stress.
4. S03 combined rule: revise before reconsideration because it misses both point-demand wait rules and carries 25.220413 modeled flex hours.

No disposition authorizes implementation. A revised option must return through a new declared scenario contract and the Module 05 gates.

## Monitoring and dashboard contract

The dashboard is a static, accessible design artifact, not a live clinical system. It will show the 12 accepted prospective measures with exact units, owner, cadence, baseline status, escalation rule, and unavailable state. Every visible value has an exact CSV source.

The initial design thresholds are:

- median arrival-to-clinician: investigate above 70.035963 minutes;
- P90 arrival-to-clinician: investigate above 151.453267 minutes;
- left before seen: investigate above 12.914912 percent;
- high-acuity median wait: pause review above 60.084398 minutes;
- language-support or mobility-support wait gap: pause review above 5 minutes worse than standard;
- modeled overtime reference: investigate above 8.715484 hours, which is 10 percent above the no-change median;
- reviewed safety-event candidate: immediate clinical review under the declared exact low-count method;
- 72-hour return: report only when follow-up completeness passes; and
- workforce interruptions and perceived load: collect a baseline before any test.

These are draft evaluation thresholds for leadership review. They do not establish control limits, safe staffing, a clinical order, a test start, or automatic action.

The dashboard must:

- use semantic HTML and a logical heading order;
- provide a visible planning-evidence banner;
- distinguish observed, simulated, and unavailable states;
- identify units, periods, denominators, owners, and review cadence;
- use text in addition to color;
- remain usable at narrow screen widths;
- include an exact table; and
- state that no option and no implementation are authorized.

## Gradient-boosted forecast contract

### Comparison population

- Target: accepted arrivals per eight-hour shift.
- Issue time: end of each completed week.
- Horizon: next 21 shifts.
- Folds: F01 through F28, testing Weeks 25 through 52.
- Common evaluation rows: 588.
- Transparent comparator: accepted seasonal exponential smoothing predictions from Module 04.
- ML family: one `GradientBoostingRegressor` only.
- Random state: 7300600.
- Tuning: prohibited.

### Eligible features

All features must be knowable at the forecast issue time:

- horizon shift from 1 through 21;
- target week index;
- shift name;
- weekday;
- month;
- known holiday flag;
- arrivals at lags 21, 42, and 63 shifts;
- mean over the 21 shifts in the last complete week; and
- mean over the 63 shifts in the last three complete weeks.

The complete-week means are constant across a target week and are calculated only from weeks completed by the issue time. The special-event flag is excluded because the accepted forecast release does not establish that it is knowable at issue time. No value from the target week may enter training or feature construction. Categorical encoding is fit on each training fold only.

### Fixed model

- loss: squared error;
- estimators: 100;
- learning rate: 0.05;
- maximum depth: 2;
- minimum samples per leaf: 15;
- maximum features: all;
- random state: 7300600; and
- nonnegative prediction floor: zero.

The environment is pinned to Python 3.12, NumPy 2.0.2, pandas 3.0.3, and scikit-learn 1.9.0.

## ML evaluation and decision-change rule

Both methods are evaluated on the same 588 rows. The release reports:

- MAE in arrivals per shift;
- RMSE in arrivals per shift;
- signed bias;
- WAPE;
- total under-forecast arrivals;
- total over-forecast arrivals;
- weighted error cost, with under-forecast weight 2 and over-forecast weight 1;
- fold-level MAE and total error;
- shift, weekday, holiday, horizon, and difficult-fold slices;
- feature importance as model allocation only;
- largest absolute errors;
- Week 53 forecast shape and total; and
- leakage and row-identity tests.

ML may replace the transparent forecast input only if every rule passes:

1. MAE improves by at least 0.75 arrivals per shift.
2. RMSE does not worsen.
3. WAPE improves by at least 1.00 percentage point.
4. Absolute bias is no more than 1.00 arrival per shift.
5. Weighted error cost improves by at least 5 percent.
6. At least three of the four accepted difficult folds do not worsen by more than 10 percent on MAE.
7. All 588 target rows, temporal cutoffs, feature-eligibility checks, and leakage tests pass.
8. The Week 53 ML total remains inside the accepted 805.136639 to 970.733035 range.

If any rule fails, the transparent method remains the accepted forecast. Better average error alone is insufficient. Even if all rules pass, the ML result does not retroactively change Module 05 or authorize staffing, a scenario, or implementation. It creates a challenge for a future declared release.

## Required deterministic outputs

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

The builder will refuse an existing target and reproduce committed outputs byte for byte.

## Learner and reference records

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

The reference must be complete. The learner template must contain explicit placeholders and no accepted model output.

## Assessment and gates

Module 06 adds zero points. The Week 6 score remains:

- Module 04 forecast gate: 0 points;
- Module 05 scenario and evaluation component: 25 points;
- Module 06 application, monitoring, and ML gates: 0 points; and
- cumulative Week 6 total: 25 points once.

The release will define 22 noncompensable gates covering upstream identity, the no-selection handoff, four scenario dispositions, safety, access, workforce, dashboard accessibility, escalation, stewardship, common target rows, temporal folds, eligible features, training-only preprocessing, one fixed model, operational errors, failure evidence, ML decision rule, point accounting, implementation boundary, reproducibility, and responsible AI.

## Release handoff

Module 07 may begin only when:

- the exact Module 05 no-selection result is retained;
- all feasibility and monitoring records are complete;
- the dashboard is accessible and bounded;
- the ML comparison uses the accepted rows and cutoffs;
- the ML decision-change rule is applied without retuning;
- the Week 6 total remains 25 points once;
- all 22 gates pass; and
- clinical, staffing, testing, implementation, and deployment authority remain absent.

The next package after Module 06 is the cumulative Week 6 checkpoint, followed by Module 07 clinician leadership and defense.

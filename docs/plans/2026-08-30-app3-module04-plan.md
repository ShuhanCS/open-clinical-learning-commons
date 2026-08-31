# APP-3 Module 04 build plan

## Objective

Build the 16.5-hour APP-3 Module 04 package, `Demand forecasting and capacity`, from the accepted Week 3 checkpoint. The module must forecast synthetic arrival demand with time-ordered validation and translate forecast error into a bounded capacity-planning implication without recommending staffing or claiming that demand is guaranteed.

## Fixed upstream contract

- Upstream checkpoint: `oclc-app3-cp01` version `0.1.0` at Commons release `0.69.0`.
- Candidate files: 137.
- Candidate manifest bytes: 23,862.
- Candidate manifest SHA-256: `9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656`.
- Accepted service: fictional `CGH-ED-01` adult emergency service.
- Accepted demand history: 1,092 consecutive eight-hour shifts across 52 complete weeks.
- Accepted population: 43,628 synthetic encounters.
- Week 3 score: 40 of 40 with all 63 inherited and checkpoint gates passing.
- Module 04 permission: permitted for demand forecasting and capacity analysis.

The module will freeze 23 checkpoint, Module 02, and Module 03 artifacts plus a file-level handoff manifest. The full 137-row checkpoint candidate manifest remains the chain of custody for files not copied into the analytic subset.

## Predeclared forecasting contract

### Target and decision

- Target: accepted arrival count for one eight-hour service shift.
- Unit: synthetic arrivals per shift.
- Issue time: end of the final shift in each completed week.
- Horizon: the next 21 shifts, equal to one seven-day planning week.
- Staffing horizon: one week.
- Decision: whether the accepted transparent forecast is adequate input for Module 05 scenario construction and what planning range it implies.
- Information cutoff: no row at or after the first target shift may enter its fold fit.

### Time-ordered evaluation

- Initial training: Weeks 1 through 24, 504 shifts.
- Evaluation: Weeks 25 through 52.
- Rolling origins: 28 expanding folds.
- Test rows: 21 shifts per fold.
- Evaluation rows: 588 per method.
- Calendar features: weekday and shift position define the 21-shift seasonal cycle. Holiday and synthetic special-event flags are retained for error slices but do not enter a model as future truth.

### Candidate methods

1. Last value: repeat the final observed shift count for all 21 horizons.
2. Seasonal naive: use the previous week's count for the same weekday and shift.
3. Seasonal exponential smoothing: additive level and 21-position seasonal state, no trend, fixed `alpha = 0.30`, fixed `gamma = 0.20`, and a nonnegative floor.

The smoothing parameters are fixed before evaluation. No fold tunes them. The model has no extrapolated trend and no external dependency.

### Selection and error

- Primary metric: mean absolute error in arrivals per shift.
- Secondary metrics: root mean squared error, mean signed error, and weighted absolute percentage error.
- Operational error: under-forecast arrivals and over-forecast arrivals remain separate.
- Tie rule: if MAE differs by less than 0.25 arrivals per shift, select the simpler eligible method in the order last value, seasonal naive, smoothing.
- Eligibility: complete predictions, no future-row use, nonnegative forecasts, exact fold coverage, and no hidden calendar truth.

## Expected reference result

Across 588 evaluation shifts per method:

| Method | MAE | RMSE | Bias | WAPE |
|---|---:|---:|---:|---:|
| Last value | 10.775510 | 13.291345 | -3.391156 | 27.479724% |
| Seasonal naive | 7.095238 | 9.060079 | -0.149660 | 18.094288% |
| Seasonal exponential smoothing | 5.937283 | 7.307180 | 0.008215 | 15.141268% |

Seasonal exponential smoothing is the expected selected method. It improves MAE by more than the 0.25-arrival tie threshold.

## Week 53 planning forecast

The selected method is refit through Week 52 and forecasts the 21 shifts from 2024-12-30 through 2025-01-05.

- Raw forecast total: 876.924084 arrivals.
- Sum of shift-level rounded forecasts: 878 arrivals.
- Empirical 80 percent actual-equivalent range from fold-total error: 805.136639 to 970.733035 arrivals.
- Baseline planning conversion: median Weeks 1 through 24 clinician staff-hours per arrival, 0.96.
- Point planning conversion: 841.847121 clinician-hours.
- Range after the same conversion: 772.931174 to 931.903714 clinician-hours.
- Historical baseline weekly clinician-hours: 822 minimum, 842 median, and 852 maximum.

The range crosses the historical range. The conversion is descriptive and cannot be presented as required staffing, adequate staffing, a schedule, a productivity target, or a causal conclusion.

## Little's Law boundary

The module will compute `arrival rate per hour x median arrival-to-clinician hours` and compare it with accepted mean queue-end snapshots. This is a consistency check only. It mixes a rate with a median elapsed time and sampled queue state, and it is weakened by priority classes, abandonment, nonstationarity, blocking, stage mismatch, and changing capacity.

No Little's Law row may be used to solve for required staff or assert equilibrium.

## Deterministic outputs

`build_forecast.py` will write:

1. `folds.csv`;
2. `forecast-predictions.csv`;
3. `error-summary.csv`;
4. `error-slices.csv`;
5. `week53-forecast.csv`;
6. `capacity-implication.csv`;
7. `littles-law-check.csv`;
8. `forecast-findings.json`;
9. `forecast-error-comparison.svg`; and
10. `week53-demand-forecast.svg`.

The builder will use the Python standard library, produce stable bytes, reject nonempty targets, and verify committed outputs against a clean rebuild.

## Learner and reference records

- `forecast-plan.md`;
- `fold-audit.csv`;
- `model-comparison.md`;
- `failure-period-review.md`;
- `capacity-interpretation.md`;
- `littles-law-interpretation.md`;
- `accessible-output-review.md`;
- `gate-results.csv`;
- `module05-handoff.md`;
- `ai-use.md`;
- `progression-decision.md`; and
- `reproducibility-check.md`.

The package also includes a base-R verification script for learners to read and run. Python remains the release validator because R is not installed in the construction environment.

## Assessment and progression

- Course points awarded here: 0.
- Role: required forecast and capacity gate for the Week 6 application release.
- Noncompensable gates: 18.
- Reference progression: `continue with conditions`.
- Module 05 permission: `permitted for improvement scenario and evaluation construction`.
- Prohibited: staffing recommendation, staffing adequacy, productivity target, guaranteed demand, root cause, clinical action, automation, implementation, scenario effect, or machine learning.

## Validation routes

The validator will check complete and learner workspaces and reject at least:

1. changed upstream evidence;
2. missing upstream evidence;
3. changed target or horizon;
4. future-row leakage;
5. missing fold;
6. wrong seasonal lag;
7. changed smoothing parameter;
8. negative forecast;
9. changed selected method;
10. wrong error value;
11. collapsed under- and over-forecast error;
12. hidden special-event failure slice;
13. changed capacity anchor;
14. staffing recommendation;
15. Little's Law equilibrium claim;
16. failed gate;
17. invalid progression;
18. missing learner record; and
19. incomplete starter submitted as complete.

## Release handoff

- Module version: 0.1.0.
- Commons release target: 0.70.0.
- Specification: `docs/curriculum/courses/APP-3/modules/04-demand-forecasting-capacity-spec.md`.
- Package: `courses/clinical-performance-improvement/modules/04-demand-forecasting-capacity/`.
- Next durable unit: APP-3 Module 05, `Improvement scenarios and evaluation`.

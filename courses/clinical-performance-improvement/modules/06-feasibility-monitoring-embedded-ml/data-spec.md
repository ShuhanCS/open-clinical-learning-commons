# Feasibility, monitoring, and ML data contract

## Accepted upstream

- Module 04: `oclc-app3-04` version `0.1.0`, Commons `0.70.0`.
- Module 05: `oclc-app3-05` version `0.1.0`, Commons `0.71.0`.
- Forecast target: accepted arrivals per eight-hour shift.
- Evaluation: 28 rolling folds, Weeks 25 through 52, and 588 exact target shifts.
- Week 53 forecast: 876.924084 arrivals with range 805.136639 to 970.733035.
- Scenario decision: no option qualifies; implementation is not authorized.
- Week 6 score entering this module: 25 of 25, counted once.

Module 06 does not alter the accepted population, measures, repairs, diagnosis, forecast target, fold cutoffs, transparent predictions, scenario assumptions, simulation results, evaluation design, score, or gates.

## Evidence grain

| Object | Grain |
|---|---|
| Feasibility screen | one scenario and feasibility domain |
| Monitoring measure | one accepted prospective measure |
| Escalation rule | one measure or evidence trigger |
| ML split | one rolling temporal fold |
| ML prediction | one method, fold, and target shift |
| Performance summary | one forecast method across 588 rows |
| Error slice | one method and declared slice |
| Failure case | one retained large ML error |
| Decision rule | one predeclared challenger rule |

## Issue-time features

Eligible inputs are horizon shift, target week, shift name, weekday, month, known holiday flag, arrivals at lags 21, 42, and 63 shifts, mean arrivals in the last complete week, and mean arrivals in the last three complete weeks. Complete-week means are fixed across a target week. Target-week outcomes and the unverified special-event flag are excluded.

Categorical encoding is fit separately on each fold's training rows. The model is one fixed `GradientBoostingRegressor` with no tuning.

## State and claim rules

Dashboard values are labeled `simulated planning baseline`, `simulated planning reference`, or `unavailable prospectively`. Unavailable is never displayed as zero. Thresholds are draft review rules, not control limits or automatic action.

The release may support feasibility questions, monitoring design, and a bounded forecast challenge. It cannot establish a causal effect, clinical benefit, safety, equity, staffing need, production performance, or authority to test, route, schedule, implement, or deploy.

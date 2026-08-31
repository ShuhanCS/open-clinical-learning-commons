# Forecasting data contract

## Upstream identity

- Accepted checkpoint: `oclc-app3-cp01` version `0.1.0` at Commons release `0.69.0`.
- Checkpoint candidate files: 137.
- Frozen analytic handoff: 23 files plus one handoff manifest.
- Service: fictional `CGH-ED-01`.
- Shift rows: 1,092.
- Complete weeks: 52.
- Synthetic flag: 1 on every analytic row.

Module 04 does not change the checkpoint population, source roles, repairs, measures, baseline, signals, safety evidence, bottleneck diagnosis, support rules, or escalation rule.

## Target and fold grain

| Item | Contract |
|---|---|
| Target | accepted arrivals per eight-hour shift |
| Issue time | end of the final shift in a completed week |
| Horizon | next 21 consecutive shifts |
| Initial train | Weeks 1 through 24 |
| Evaluation | Weeks 25 through 52 |
| Folds | 28 expanding origins |
| Rows per fold | 21 |
| Evaluation rows per method | 588 |
| Seasonal lag | 21 shifts |

Holiday and synthetic special-event flags support error slices. They do not enter the forecast as future outcome information.

## Output grains

| Output | Grain |
|---|---|
| `folds.csv` | one rolling origin |
| `forecast-predictions.csv` | one method, fold, and target shift |
| `error-summary.csv` | one method across common evaluation rows |
| `error-slices.csv` | one selected-model calendar or shift slice |
| `week53-forecast.csv` | one future shift and selected forecast |
| `capacity-implication.csv` | one bounded planning quantity |
| `littles-law-check.csv` | one declared historical context |
| `forecast-findings.json` | one release summary |

## Claim boundary

The release may compare transparent forecasts and express error in arrivals and planning-equivalent clinician-hours. It cannot establish staffing need, staffing adequacy, clinician productivity, equilibrium, guaranteed demand, root cause, clinical effect, scenario effect, causal effect, automated action, or implementation authority.

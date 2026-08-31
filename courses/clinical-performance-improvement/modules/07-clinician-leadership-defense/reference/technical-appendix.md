# Technical appendix

## Checkpoint identities

| Unit | Version | Commons | Files | Candidate manifest SHA-256 | Release SHA-256 |
|---|---:|---:|---:|---|---|
| `oclc-app3-cp01` | 0.1.0 | 0.69.0 | 153 | `9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656` | `270b4e49d1c21d8faf7243cd11cef1dddea836d32be551dfe72edac771b31f27` |
| `oclc-app3-cp02` | 0.1.0 | 0.73.0 | 226 | `4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a` | `b8af80b7e07c2eac2aeb0e9206533bfae134f55d69a5df9038a7a9a915c4dd05` |

## Technical performance facts

- Accepted encounters: `43,628`.
- Completed: `39,975`.
- Left before seen: `3,653`.
- Provisional baseline: `Weeks 1 through 24`.
- Signal records: `9`.
- Known true safety events: `894`.
- Trigger true positives: `673`.
- Incident true positives: `358`.
- Trigger false positives: `379`.
- Trigger sensitivity: `75.2796 percent`.
- Incident capture: `40.0447 percent`.
- Trigger specificity: `99.0302 percent`.
- Roomed-to-clinician medians: `49, 66, 44, and 49 minutes`.
- Target-window language-support count: `401, not supported`.
- Target-window mobility-support count: `242, not supported`.
- Root cause: `not established`.

## Forecast facts

- Target: `accepted arrivals per eight-hour shift`.
- Horizon: `21 shifts over 7 days`.
- Folds: `28`.
- Evaluation rows: `588 per method`.
- Accepted method: `seasonal exponential smoothing`.
- MAE: `5.937283`.
- RMSE: `7.307180`.
- Bias: `0.008215`.
- WAPE: `15.141268 percent`.
- Week 53 point: `876.924084`.
- Empirical range: `805.136639 to 970.733035`.
- Little's Law equilibrium: `not established`.
- Staffing recommendation: `not authorized`.

## Scenario and evaluation facts

- Scenarios: `S00 through S03`.
- Conditions: `C01 through C05`.
- Paired runs: `4,000`.
- Summaries: `20`.
- Option effects: `15`.
- Null or failed effects: `6`.
- Selected option: `none`.
- S01 point median improvement: `1.958703 minutes`.
- S01 point P90 improvement: `21.244986 minutes`.
- S02 point median worsening: `5.803341 minutes`.
- S02 point P90 worsening: `41.617987 minutes`.
- S02 stress median worsening: `86.671644 minutes`.
- S03 point median improvement: `0.316383 minutes`.
- S03 point P90 improvement: `14.547388 minutes`.
- Prospective measures: `12`.
- Evaluation threats: `8`.
- Safety and return within 72 hours: `not simulated`.
- Causal effect: `not established by simulation`.

## Feasibility, monitoring, and ML facts

- Feasibility rows: `28`.
- Status counts: `5 supported, 18 requires local evidence, 5 not supported`.
- Dispositions: `S00 retain, S01 revise, S02 stop, S03 revise`.
- Monitoring measures: `12`.
- Prospectively unavailable values: `3`.
- Escalation rules: `10`.
- Automatic actions: `0`.
- Fallback: `continue no-change monitoring`.
- Challenger: `one fixed untuned GradientBoostingRegressor, seed 7300600`.
- Leakage and environment checks: `12 pass`.
- Common rows: `588`.
- Challenger MAE: `5.205494`.
- Challenger RMSE: `6.554934`.
- Challenger Week 53: `860.277096`.
- R01 required MAE improvement: `0.750000`.
- R01 observed MAE improvement: `0.731788`.
- Rules passed: `7 of 8`.
- ML decision: `retain transparent forecast`.

These facts are teaching evidence for a fictional service. They do not establish a real cause, safety result, staffing level, intervention effect, or model utility.

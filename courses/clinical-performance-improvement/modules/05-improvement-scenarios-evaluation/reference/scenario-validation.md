# Scenario validation

- Validation checks: `24 of 24 passed`
- Accepted encounters: `43,628 synthetic encounters`
- Input strata: `45`
- Scenario runs: `4,000`
- Paired seeds: `1,000`
- Conservation: `pass in every run`
- Point-demand no-change median arrival-to-clinician time: `60.035963 minutes`
- Point-demand no-change left-before-seen rate: `11.914912%`
- High-acuity median wait: `45.084398 minutes`
- Low-acuity median wait: `70.473589 minutes`

The model preserves acuity priority, nonnegative values, unique run identities, all three access-support groups, exact safety and return outcome boundaries, and the accepted scenario register. The no-change calibration is broad because this is a guided teaching model. The 2-night, 6-day, and 4-evening slot schedule is not an observed staffing count.

The validation result permits comparison of assumptions. It does not validate a production simulator or predict realized effects.

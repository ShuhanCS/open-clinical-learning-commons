# APP-1 Module 04: Risk adjustment and fair comparison

This module uses the accepted 476-person cohort to compare fixed-horizon outcomes after accounting for four prespecified baseline fields. It releases the expected-outcome model, calibration and bootstrap checks, person-level expected outcomes, exposure-group results, and six synthetic teaching-site comparisons.

## Reference result

- The cohort contains 476 people and 87 first later acute returns by day 335.
- The expected model uses age, any prior acute encounter, prior condition count, and inpatient index status.
- Apparent Brier score is 0.13490621 and apparent ROC AUC is 0.66585409.
- Expected events sum to 87.00000000 in the fitting cohort.
- The any-prior-acute coefficient is unstable in the person bootstrap. Its 95 percent bootstrap interval runs from 0.61109293 to 22.56297423.
- The standardized event rate is 0.19819116 with scheduled follow-up and 0.17721417 without recorded follow-up.
- The secondary adjusted odds ratio for scheduled follow-up is 1.16353250, with a 95 percent interval from 0.67665877 to 2.00072462 and p = 0.58392672.
- All six synthetic sites meet the prespecified minimums and are reported with caution in fixed SITE-A through SITE-F order.

These are synthetic, descriptive results. Apparent model performance is not external validation. The adjusted odds ratio is not a risk ratio, hazard ratio, or causal effect. Site estimates are not grades or rankings. The failed Module 03 proportional-hazards screen remains open.

## Build

```powershell
python build_adjustment.py --self-check
python build_adjustment.py --cohort ../02-longitudinal-cohorts-followup/outputs/analysis-cohort.csv --target <new-output-directory>
python build_workspace.py --target <new-learner-workspace>
python build_workspace.py --target <new-reference-workspace> --reference
python validate_adjustment.py .
```

The supplied R script is a reading route for the same formula. Run it only in the named environment and record whether its results reconcile with the Python reference.

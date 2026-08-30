# Transparent benchmark versus bounded machine learning

## Locked comparison

Both models predict later acute return at the day-30 landmark from exactly four baseline features: age in decades from 40, any prior acute encounter, prior-year condition count, and inpatient index status. The time-ordered training set has 333 people and 70 events. The held-out evaluation set has 143 people and 17 events. The threshold `0.20` and false-negative-to-false-positive teaching cost ratio `3:1` were fixed before evaluation.

Gender, race, ethnicity, teaching site, recorded follow-up, expected probability, outcome fields, and post-landmark fields are prohibited features. Only one ML model was fitted.

## Held-out evidence

| Measure | Transparent GLM | Bounded random forest |
|---|---:|---:|
| Brier score | 0.09609243 | 0.10745654 |
| ROC AUC | 0.66363212 | 0.62371615 |
| Log loss | 0.34684826 | 0.37750998 |
| Calibration intercept | -0.85765595 | -1.04707642 |
| Calibration slope | 0.98604197 | 0.64579740 |
| True negatives | 109 | 77 |
| False positives | 17 | 49 |
| False negatives | 9 | 6 |
| True positives | 8 | 11 |
| People flagged | 25 | 60 |
| Weighted teaching cost | 44 | 67 |

The random forest catches 3 additional events but adds 32 false positives and 35 flags. Its Brier score is worse by `0.01136411`; the paired 95% bootstrap interval is `-0.00489999` to `0.02602160`. Its AUC is lower by `-0.03991597`; the interval is `-0.16059757` to `0.11721522`. The intervals remain uncertain, but there is no supported overall improvement.

## Subgroup and failure boundary

Model metrics are reportable for held-out age 18-44, age 45-64, source-recorded F, source-recorded M, White, and non-Hispanic groups. Other groups fail the minimum evaluation support rule and remain suppressed. These audits cannot certify fairness or justify group-specific thresholds.

- Does ML change the improvement decision: `no`
- Preferred analytic benchmark: `transparent GLM`
- Universal prospective workflow measurement: `required`
- Clinical model deployment: `prohibited`

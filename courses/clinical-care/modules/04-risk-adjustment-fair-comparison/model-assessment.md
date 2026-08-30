# Model assessment

## Apparent performance

- People: `476`
- Events: `87`
- Event prevalence: `0.18277311`
- Brier score: `0.13490621`
- ROC AUC: `0.66585409`
- Log likelihood: `-208.29076775`
- Deviance: `416.58153550`
- Non-intercept parameters: `4`
- Events per non-intercept parameter: `21.75000000`
- Sum of expected events: `87.00000000`

All metrics are apparent results from the same synthetic cohort used to fit the model. They do not establish transportability or deployment performance. The five calibration groups contain 87 observed and 87.00000001 rounded expected events in total. The highest predicted-probability group contains 37 observed and 33.61772427 expected events.

## Coefficients and stability

The expected-model odds ratios are 1.01824451 per ten-year age increment from age 40, 6.45268606 for any prior acute encounter, 1.07830919 per prior condition, and 4.09130751 for an inpatient index encounter. These are apparent synthetic associations, not clinical effects.

All 300 person bootstrap fits succeeded. The age and prior-condition coefficients have same-sign shares of 0.58666667 and 0.66666667. The any-prior-acute coefficient has a bootstrap median of 1.96192904 and a 95 percent interval from 0.61109293 to 22.56297423. That wide upper estimate is a sparse-coefficient stability warning. The field remains in the prespecified model and the warning remains open.

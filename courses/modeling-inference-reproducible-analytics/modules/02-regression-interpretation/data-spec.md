# FND-2 Module 02 data specification

## Immutable Module 01 inputs

| Input | Bytes | SHA-256 |
|---|---:|---|
| `modeling-cohort.csv` | 138503 | `6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332` |
| `split-registry.csv` | 51910 | `05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1` |
| `baseline-metrics.csv` | 306 | `613651013e397beeadc84b17482026ca7cb4674abf61bf521699d79af0a3c9af` |
| `feature-role-contract.csv` | 3766 | `599f29ca612cb5f23aed277c56937af78c488ba952c2926faa94166f33449c83` |

The model build stops on any input change. It does not recalculate the cohort, field roles, temporal split, or baseline.

## Fit partition

All models are fit on `split=train` only. The build reads validation and test rows only to verify that they remain present and excluded from fitting. Module 02 does not calculate validation or test regression evidence.

## Linear case

The outcome is `next_30d_days_after_index_stop`. It is observed for 111 cohort rows: 69 train, 21 validation, and 21 test. Only the 69 training rows are used in `LIN01`.

The 263 blanks represent no recorded different encounter within 30 days under the source definition. They are structural for this conditional outcome and remain blank. They are not zero days and are not imputed.

Declared model:

```text
next_30d_days_after_index_stop = intercept
  + age_at_index
  + prior_365d_encounter_count
  + index_class_inpatient
```

The result describes conditional mean timing among selected training rows with a recorded different encounter. It is not a survival model and does not estimate time to encounter for the full cohort.

## Logistic cases

All logistic models use 224 training rows and 25 positive `acute_return_90d` outcomes.

Training mean age is `46.245535714286`. The centered decade term is:

```text
age_centered_decade = (age_at_index - 46.245535714286) / 10
```

`LOG01`:

```text
logit(P(acute_return_90d = 1)) = intercept
  + age_centered_decade
  + prior_365d_acute_count
  + index_class_inpatient
```

`LOG02` adds `age_centered_decade_sq`.

`LOG03` adds `prior_acute_x_inpatient` to `LOG01`.

The added-term models are training-only interpretation exercises. They do not replace validation-based selection in Module 03.

## Uncertainty

Linear output includes classical t-based and HC3 heteroskedasticity-robust standard errors and intervals. Logistic output includes model-based and HC3 standard errors and odds-ratio intervals. Scenario tables distinguish uncertainty for a conditional mean from an interval for a new linear outcome and distinguish probability uncertainty from individual outcome certainty.

## Sparse-cell contract

Training counts are reported for gender, race, ethnicity, and index class even when a field is not used by the bounded formula. The `other` race category has no training rows; `native` has three rows and no positive outcome. Unsupported category effects cannot be fit, ranked, merged, or interpreted without a new plan.

## Output contract

The release produces 13 CSV evidence tables plus `build-report.json`. All outputs use UTF-8 and LF endings. Generated outputs are never hand-edited.

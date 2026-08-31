# Performance interpretation

## Development

The weighted development prevalence is `0.02916349`. The constant prevalence baseline has weighted Brier score `0.02831298`, log loss `0.13182226`, and ROC AUC `0.50000000`. The transparent model has weighted Brier score `0.02802258`, log loss `0.12642281`, and ROC AUC `0.68292125`.

## Untouched temporal holdout

The 1,806-row holdout contains 97 outcomes. Weighted prevalence is `0.02904272`. The transparent model has weighted mean probability `0.03015261`, Brier score `0.02811126`, log loss `0.12694930`, and ROC AUC `0.68783144`. The 500-replicate teaching interval for AUC is `0.65477394` to `0.71633676`.

## Later transport stress

The 2,086-row transport set contains 75 outcomes. Weighted prevalence is `0.03274014`. The transparent model has weighted mean probability `0.03041245`, Brier score `0.03175435`, log loss `0.14019059`, and ROC AUC `0.68422573`. The teaching interval for AUC is `0.62444634` to `0.73840965`.

## Decision meaning

The model separates some higher and lower historical scores better than a constant baseline. It does not show enough by itself to choose a threshold or infer patient benefit. Similar AUC across the two evaluation partitions does not establish local transport, calibration, workflow usefulness, or safety. Calibration, burden, missed cases, support, and governance remain separate gates.

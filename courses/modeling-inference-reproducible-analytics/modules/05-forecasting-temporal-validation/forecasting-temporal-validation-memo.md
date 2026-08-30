# Forecasting and temporal-validation memo

## Recommendation

Continue the exact pipeline to Module 06 testing with conditions. `HOLT_DAMPED` beats both declared benchmarks on aggregate MAE and RMSE, but the result is public-data teaching evidence, not operational approval.

## Target and folds

The target is weekly total reported COVID-19, influenza, and RSV new admissions in the Massachusetts jurisdiction aggregate. Five expanding-window origins at weeks 74, 78, 82, 86, and 90 each predict four later weeks. The 20 test targets span weeks 75 through 94 and no future row enters a fit.

## Comparison

`HOLT_DAMPED` has MAE 14.99587157 and RMSE 21.07855007 admissions. `LAST` has MAE 28.20000000 and RMSE 39.44363066. `SNAIVE52` has MAE 93.15000000 and RMSE 96.43002644. All three overpredict on average during the released decline; actual-minus-prediction biases are -5.97261489, -22.50000000, and -93.15000000.

The candidate does not dominate every fold. It loses to last-value in F04, with MAE 7.41230761 versus 1.00000000, and only narrowly improves F05, with 12.73106354 versus 13.25000000. Its worst miss is 58.96408576 admissions on 2026-05-23.

## Uncertainty and recognition

The illustrative damped-Holt intervals are extremely wide and are not calibrated. The level ADF p-value is 0.12535568, while the first-difference p-value is 0.00590799. The supplied ARIMA(1,1,1) reading and Ljung-Box p-values of 0.35732989 and 0.32516289 support recognition exercises only; they neither select a model nor prove adequate residual behavior.

## Source and use boundary

The 94 weeks are public aggregates across a changing group of reporting hospitals. Reporting coverage is shown beside errors but never used as a correction weight. The backtest cannot support a complete burden estimate, a single-hospital forecast, staffing, capacity, clinical care, causal explanation, automated refresh, or deployment.

# FND-2 Module 05: Forecasting and temporal validation

This 16-hour module forecasts weekly Massachusetts respiratory admissions from the exact 94-week public CDC NHSN series. It uses five expanding-window, four-week folds; last-value and 52-week seasonal-naive benchmarks; one guided damped-Holt candidate; and an ARIMA(1,1,1) reading kept outside candidate selection.

The candidate has the best aggregate backtest error: MAE 14.99587157 admissions, compared with 28.20000000 for last-value and 93.15000000 for seasonal naive. That result permits Module 06 testing with conditions. It does not support staffing, capacity, care, or deployment.

## Workflow

1. Read `source-record.yml`, `data-spec.md`, `forecast-contract.json`, and `assessment.md`.
2. Confirm the target, cutoff, horizon, and possible use before fitting.
3. Inspect the five folds and benchmark eligibility.
4. Rebuild into a new target: `python build_forecast_evidence.py reproduced-outputs --outputs-only`.
5. Compare all 60 predictions, then aggregate, fold, and horizon errors.
6. Explain candidate failures, reporting coverage, intervals, and the ARIMA boundary.
7. Complete every decision and accountability record.
8. Run `python validate_forecast_evidence.py . --mode submission`.

The 6,208-row source release and 94-row Massachusetts series are public aggregate data already versioned in the Commons. No live download or patient data are required.

Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

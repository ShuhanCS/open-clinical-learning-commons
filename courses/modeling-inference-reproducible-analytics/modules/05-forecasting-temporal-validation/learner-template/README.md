# FND-2 Module 05 learner release

This workspace contains exact copies of the 6,208-row public CDC release, 94-row Massachusetts series, Module 04 handoff, deterministic builder, exact forecast outputs, and the records you must complete.

## Workflow

1. Read the source, data, forecast, and assessment contracts.
2. Define target, cutoff, horizon, refresh, possible decision, and prohibited use.
3. Rebuild with `python build_forecast_evidence.py reproduced-outputs --outputs-only`.
4. Defend all five time folds and both benchmark eligibility decisions.
5. Compare aggregate, fold, horizon, failure, interval, and coverage evidence.
6. Read decomposition, ADF, ARIMA, and residual tables at the declared recognition level.
7. Complete all nine prompted records.
8. Run `python validate_forecast_evidence.py . --mode submission`.

Do not edit source values, folds, predictions, or misses. A required contract change returns for review and versioning.

No artifact permits staffing, capacity, clinical, or deployment use.

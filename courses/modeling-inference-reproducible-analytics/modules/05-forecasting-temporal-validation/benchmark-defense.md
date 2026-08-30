# Benchmark defense

`LAST` is required because a forecast that cannot improve on the most recent observed count has little teaching value as a trend model. It is available at every origin and uses no future information.

`SNAIVE52` tests a plausible yearly seasonal comparison. Every test target has a value exactly 52 weeks earlier within its training range. Eligibility is established from timing before performance is viewed.

`HOLT_DAMPED` is the only guided candidate. It is refit inside each fold and must improve aggregate MAE and RMSE against both benchmarks on the same 20 targets. It passes that rule but loses one fold to last-value, so the result remains conditional.

`ARIMA111` is not a fourth competitor. It is supplied after the model contract as a recognition exercise, with one final-origin fit and no order search. Promoting it would require a new design and version.

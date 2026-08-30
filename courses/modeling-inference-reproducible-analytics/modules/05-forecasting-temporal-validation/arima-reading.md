# ARIMA-family reading

The supplied example fits ARIMA(1,1,1) with drift to weeks 1 through 90 and forecasts weeks 91 through 94. The first difference represents change between adjacent weeks; `ar.L1` reads one autoregressive lag in the differenced process; `ma.L1` reads one moving-average error lag; and `sigma2` is fitted innovation variance.

The level-series ADF p-value is 0.12535568 and the first-difference p-value is 0.00590799. These are diagnostics under assumptions, not automatic evidence that ARIMA(1,1,1) is the correct model.

The four point readings are 14.15958493, 12.01524062, 9.53826688, and 6.97644012 admissions. Their model intervals include implausible negative lower values and are extremely wide. The release retains those outputs to expose model-scale and uncertainty problems; it does not use them operationally.

Ljung-Box p-values are 0.35732989 at lag 4 and 0.32516289 at lag 8. Failure to reject residual autocorrelation is not proof of white noise, correct specification, or useful forecasts. `ARIMA111` remains recognition only.

# Model comparison

All results use the same 28 rolling origins and 588 target shifts per method.

| Method | MAE | RMSE | Bias | WAPE | Under | Over | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| Last value | 10.775510 | 13.291345 | -3.391156 | 27.479724% | 4165.000000 | 2171.000000 | Reject |
| Seasonal naive | 7.095238 | 9.060079 | -0.149660 | 18.094288% | 2130.000000 | 2042.000000 | Reject |
| Seasonal exponential smoothing | 5.937283 | 7.307180 | 0.008215 | 15.141268% | 1743.145982 | 1747.976153 | Select |

- Selected method: `seasonal_exponential_smoothing`
- Selection reason: `lowest eligible MAE beyond the 0.25-arrival tie tolerance`
- Practical meaning: `the selected method reduces average shift error, but still misses about 5.94 arrivals per shift and 64.68 arrivals per week on average`
- Retained warning: `near-zero aggregate bias does not cancel the operational consequences of individual under- and over-forecasts`

The selected method is transparent and bounded. Its performance does not establish future demand, staffing need, or clinical effect.

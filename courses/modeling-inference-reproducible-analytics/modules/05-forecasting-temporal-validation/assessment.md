# Assessment: forecasting and temporal validation

## Submission

Submit one protected package tagged `fnd2-forecast-v0.1.0`. Preserve all source and Module 04 fingerprints, complete every prompted record, rebuild into a new target, validate the package, and defend one allowed Module 06 disposition.

## Required defense

Explain:

1. unit, target, source unit, horizon, cutoff, refresh, decision, and prohibited use;
2. why a random split would leak time;
3. the train and test indexes in all five folds;
4. why test blocks do not overlap;
5. why `LAST` is the minimum benchmark;
6. why `SNAIVE52` is eligible at every target;
7. where each `HOLT_DAMPED` fit occurs;
8. why `ARIMA111` is ineligible for selection;
9. exact aggregate MAE, RMSE, and bias for all eligible methods;
10. why MAPE is secondary at small counts;
11. the candidate's F04 loss and F05 near tie;
12. the worst miss for each model;
13. what positive and negative signed errors mean;
14. why interval coverage is not calibration proof;
15. what the ADF readings do and do not establish;
16. what the Ljung-Box readings do and do not establish;
17. why reporting coverage is context rather than a weight;
18. why the aggregate is not one hospital's process;
19. what triggers forecasting or operations referral; and
20. why aggregate backtest improvement permits testing but not deployment.

## Ten-point Week 6 share

| Criterion | Points |
|---|---:|
| Forecast aim, target, horizon, cutoff, and time-ordered folds | 2.00 |
| Naive benchmarks and exact fold-level predictions | 2.00 |
| Guided model, error metrics, residuals, and comparison | 2.50 |
| Reporting coverage, failure analysis, limits, and recommendation | 2.00 |
| Accessible evidence, reproduction, and responsible agent record | 1.50 |
| Total | 10.00 |

The minimum numeric score is 8.00. Every gate must pass.

## Noncompensable gates

1. Exact full and Massachusetts source fingerprints.
2. All 94 weeks retained in order.
3. Target reconciles to the three reported components.
4. Future rows excluded from each fit.
5. Benchmark eligibility declared before candidate comparison.
6. Candidate compared on identical folds and targets.
7. Errors retain source units and valid denominators.
8. No manual revision of source values or forecast misses.
9. Reporting coverage remains context only.
10. No single-hospital, stable-process, staffing, capacity, clinical, or operational claim.
11. Accessible exact table accompanies the display.
12. ARIMA remains recognition.
13. Reproduction and material AI assistance are recorded.
14. An explicit Module 06 progression disposition is recorded.

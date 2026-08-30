# Forecast display text alternative

The display shows 94 consecutive weekly Massachusetts jurisdiction aggregates from 2024-11-09 through 2026-08-22. Admissions rise into the first winter, decline through spring and summer, rise again during the second winter, and fall sharply toward low counts by summer 2026.

The final backtest origin is week 90, dated 2026-07-25, with an observed target of 15. Weeks 91 through 94 have actual values 22, 21, 37, and 33. Last-value predicts 15 for each. Damped Holt predicts 15.25338692, 15.45609649, 15.61826415, and 15.74799827. The 52-week seasonal-naive values are much higher because the corresponding prior-year weeks occurred earlier in a different part of the reported wave.

Exact values for every model, fold, horizon, actual, error, and reporting percentage are in `outputs/forecast-predictions.csv`. No conclusion depends on line color or position.

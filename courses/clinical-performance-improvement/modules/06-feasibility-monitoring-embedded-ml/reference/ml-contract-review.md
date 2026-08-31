# ML contract review

- Target: `accepted arrivals per eight-hour shift`
- Issue time: `end of the final shift in each completed week`
- Horizon: `21 shifts`
- Folds: `28`
- Common rows: `588`
- Comparator: `seasonal_exponential_smoothing`
- Challenger: `one GradientBoostingRegressor`
- Random state: `7300600`
- Tuning: `prohibited`
- Categorical preprocessing: `fit on each training fold only`
- Special-event flag: `excluded; issue-time knowability not established`
- Leakage checks: `12 of 12 passed`

Eligible features are calendar and shift fields known at issue time, lags 21, 42, and 63, and means from the last one and three complete weeks. No target-week outcome enters a feature. The first three weeks are excluded from training because the 63-shift history is incomplete.

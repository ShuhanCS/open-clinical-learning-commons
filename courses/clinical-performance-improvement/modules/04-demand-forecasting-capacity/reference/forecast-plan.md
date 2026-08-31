# Forecast plan

- Target: `accepted arrivals per eight-hour shift`
- Decision: `whether a transparent one-week demand forecast can support bounded Module 05 scenario construction`
- Issue time: `end of the final shift in each completed week`
- Cutoff: `the issue shift; no later observation is eligible`
- Horizon: `21 consecutive shifts over 7 days`
- Initial training window: `Weeks 1 through 24, 504 shifts`
- Evaluation window: `Weeks 25 through 52`
- Evaluation design: `28 expanding rolling-origin folds with 21 target rows per fold`
- Eligible methods: `last value; seasonal naive at lag 21; additive seasonal exponential smoothing without trend`
- Primary metric: `mean absolute error in arrivals per shift`
- Secondary metrics: `root mean squared error, signed bias, and WAPE`
- Selection rule: `lowest eligible MAE; if methods are within 0.25 arrivals, retain the simpler method`
- Error consequences: `report under-forecast and over-forecast arrivals separately`
- Calendar rule: `holiday and special-event flags are retrospective error slices, not future predictors`
- Action boundary: `the result may enter Module 05; it does not authorize staffing or implementation`

The plan was fixed before fitting. All three methods use the same 588 evaluation shifts. The smoothing parameters are fixed at alpha 0.30 and gamma 0.20, with seasonal period 21, no trend, and a nonnegative floor.

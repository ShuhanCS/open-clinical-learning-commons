# Fixed ML contract review

- Contract status: `frozen before evaluation`.
- Common rows: `7,544`.
- Predictors: `age centered per 10, BMI centered per 5, and female indicator`.
- Target: `observed LBXGH at or above 6.5 percent, not diagnosis`.
- Development cycles: `2013-2014 and 2015-2016`.
- Temporal holdout: `2017-2018, untouched by fitting`.
- Transport stress: `2021-2023, untouched by fitting`.
- Random state: `7400600`.
- Search or tuning: `none`.
- Accepted threshold: `none`.

## Contract decision

One fixed `GradientBoostingClassifier` is fit once with the same target, three predictors, weights, development rows, evaluation rows, missing-input rule, and six candidate thresholds as the accepted transparent model. The challenger replaces the transparent model only if all 11 rules pass. Holdout inspection cannot change model settings, thresholds, intended use, workflow, or authority.

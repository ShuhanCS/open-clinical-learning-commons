# Leakage and interpretability review

- Leakage tests: `12 of 12 pass`.
- Model fits: `one fixed development-only fit`.
- Holdout-guided tuning: `none`.
- Predictor importances: `three global impurity importances sum to 1.00000000`.
- Directional interpretation: `not supplied by impurity importance`.
- Patient-level explanation: `not supplied and not required for this nonproduction teaching comparison`.
- Replacement effect: `interpretability rule R10 passes for the declared global-importance contract, but it grants no clinical use`.

## Review conclusion

The code preserves temporal boundaries, common rows, predictors, target, weights, thresholds, and one fixed model fit. Global feature importance can show which predictors the fitted trees used most, but it does not show direction, causality, reliability for a person, or clinical meaning. The discrimination and subgroup failures independently retain the transparent model.

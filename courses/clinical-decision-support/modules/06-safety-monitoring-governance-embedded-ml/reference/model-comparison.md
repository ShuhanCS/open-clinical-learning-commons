# Model comparison

- Transparent decision: `retain transparent model`.
- Replacement rules: `8 of 11 pass`.
- Failed rules: `R03, R04, and R08`.
- Temporal-holdout AUC difference: `-0.00743486`.
- Transport-stress AUC difference: `-0.01928938`.
- Worst supported subgroup AUC degradation: `0.10385240`.
- Accepted threshold: `none`.
- Clinical authority: `none`.

## Decision

The challenger improves weighted Brier score and meets the calibration and candidate burden rules, but it loses discrimination on both untouched evaluation sets and exceeds the allowed supported subgroup degradation. Because replacement requires every rule, the transparent model remains accepted for this teaching comparison. This decision does not validate either model locally, accept a threshold, or authorize clinical use.

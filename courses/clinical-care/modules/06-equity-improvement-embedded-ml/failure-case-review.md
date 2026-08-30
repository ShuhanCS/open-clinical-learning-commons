# Failure-case review

`outputs/failure-cases.csv` contains every held-out false negative: 9 for the transparent model and 6 for the bounded random forest. It also contains one aggregate false-positive burden row per model: 17 for the transparent model and 49 for the random forest.

The review is deliberately limited to the four eligible baseline features, prediction, and outcome. No clinical story is inferred from a synthetic record.

## What the comparison reveals

The random forest reduces false negatives by 3 but adds 32 false positives. With the fixed educational costs, its total is 67 versus 44. Changing the cost ratio could change that arithmetic, which is why the ratio is labeled a teaching scenario rather than clinical value.

## Failure modes checked

- Leakage: neither model uses outcome, post-landmark, exposure, site, expected-probability, or demographic audit fields.
- Test contamination: the final 143 rows are used only after model, features, threshold, and split are frozen.
- Unsupported subgroup ranking: unsupported metrics are blank, groups are not combined, and all fixed categories remain visible.
- Performance-only recommendation: calibration, confusion counts, workload, support, and failure cases accompany AUC and Brier score.
- Replacement failure: the model does not supplant the transparent benchmark or collection of offer, preference, completion, barrier, and burden states.
- Deployment failure: synthetic retrospective evidence cannot support clinical deployment.

The bounded random forest fails to improve the decision case. Retain the transparent model and move only the prospective workflow proposal to clinician leadership review.

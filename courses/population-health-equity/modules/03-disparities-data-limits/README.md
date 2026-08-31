# APP-5 Module 03: Disparities and data limits

This 16.5-hour module turns the accepted Module 02 measures into a bounded disparity analysis for the fictional `FMA-DP-01` planning review. Learners work with three separate synthetic equity margins, calculate absolute and relative disparities, test two reference choices, audit missing fields and representation, and apply primary and complementary suppression.

The accepted release has 151,715 tract-age-group margin rows, 7,985 field-completeness rows, 32 pairwise comparisons, and six summary disparity results. Its tract-group publication table has 30,343 rows: 19,742 primary suppressions, 1,488 complementary suppressions, and 9,113 publishable synthetic cells. Suppressed values are blank, not zero.

## Verify the accepted evidence

```powershell
python freeze_upstream.py --self-check
python generate_equity_layer.py --self-check
python build_disparities.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

## Build learner and reference workspaces

```powershell
python build_workspace.py --target "$env:TEMP\app5-module03-learner"
python validate_workspace.py "$env:TEMP\app5-module03-learner" --starter

python build_workspace.py --target "$env:TEMP\app5-module03-reference" --reference
python validate_workspace.py "$env:TEMP\app5-module03-reference"
```

The builder refuses to overwrite an existing target. The three equity dimensions are marginal tables, not joint person records, and cannot support intersectional claims. Every result is synthetic. The module may permit construction of the cumulative 40-point Week 3 checkpoint, but it does not authorize Module 04, real disparity claims, mapping, tract ranking, targeting, allocation, intervention, implementation, or deployment.

The durable teaching specification is `docs/curriculum/courses/APP-5/modules/03-disparities-data-limits-spec.md`.

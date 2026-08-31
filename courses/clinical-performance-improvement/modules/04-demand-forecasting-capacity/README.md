# APP-3 Module 04: Demand forecasting and capacity

This 16.5-hour module turns the accepted Week 3 evidence into a transparent one-week arrival forecast and bounded capacity-planning range for the fictional `CGH-ED-01` service. Learners predeclare the target, issue time, cutoff, horizon, folds, methods, selection rule, and error consequences before fitting.

The reference compares last value, seasonal naive, and fixed seasonal exponential smoothing on 28 common rolling origins. Smoothing has the lowest MAE at 5.937283 arrivals per shift. The Week 53 forecast is 876.924084 arrivals, with an empirical actual-equivalent range of 805.136639 to 970.733035. The result may enter Module 05 scenario construction but does not authorize staffing or implementation.

## Verify the accepted evidence

```powershell
python freeze_upstream.py --self-check
python build_forecast.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
Rscript verify_forecast.R
```

The Python checks pass in the construction environment. The base-R check remains required before alpha because Rscript is not installed here.

## Build learner and reference workspaces

```powershell
python build_workspace.py --target "$env:TEMP\app3-module04-learner"
python validate_workspace.py "$env:TEMP\app3-module04-learner" --starter

python build_workspace.py --target "$env:TEMP\app3-module04-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module04-reference"
```

The builder refuses to overwrite an existing target. Module 04 is a required zero-point gate for Module 05. Its durable teaching specification is `docs/curriculum/courses/APP-3/modules/04-demand-forecasting-capacity-spec.md`.

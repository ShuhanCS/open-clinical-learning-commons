# Reproducibility check

- Upstream freeze self-check: `pass`
- Forecast builder self-check: `pass`
- Workspace builder self-check: `pass`
- Workspace validator: `pass`
- Repeated output identity: `pass`
- Existing-target protection: `pass`
- Rolling folds: `28`
- Prediction rows: `1,764`
- Outputs: `10`
- Selected method: `seasonal_exponential_smoothing`
- Week 53 raw forecast: `876.924084 arrivals`
- Independent base R check: `pending before alpha because Rscript is unavailable in this environment`

Reproduction commands:

```text
python freeze_upstream.py --self-check
python build_forecast.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
Rscript verify_forecast.R
```

The Python self-check rebuilds in temporary directories, compares committed bytes, confirms exact metrics and forecast totals, and verifies that existing targets are not overwritten. The R command remains a named release condition rather than a silently omitted check.

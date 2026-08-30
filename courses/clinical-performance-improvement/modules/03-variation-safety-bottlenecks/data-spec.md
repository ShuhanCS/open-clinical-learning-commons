# Diagnostic data contract

## Upstream identity

- Module 02 version: `0.1.0`.
- Commons input release: `0.67.0`.
- Frozen upstream files: 14 plus one handoff manifest.
- Accepted encounters: 43,628.
- Completed encounters: 39,975.
- Weekly rows: 52.
- Shift rows: 1,092.
- Safety candidate raw rows: 1,274.
- Module 02 query checks: 30 of 30 pass.

Module 03 does not change the accepted population, event clocks, repairs, measure definitions, unavailable states, or synthetic-service boundary.

## Phase contract

- Baseline: Weeks 1 through 24.
- Evaluation: Weeks 25 through 52.
- Target process window: evening shifts in Weeks 35 through 44.
- Contemporaneous control: day and night shifts in Weeks 35 through 44.
- Recovery: evening shifts in Weeks 45 through 52.

The baseline is provisional because it contains a predeclared run signal. Its limits support curriculum review, not live operational control.

## Output grains

| Output | Grain | Rows |
|---|---|---:|
| variation-series.csv | one chart and week | 208 |
| control-limits.csv | one chart contract | 4 |
| signal-audit.csv | one predeclared signal occurrence | 9 |
| weekly-safety.csv | one week | 52 |
| safety-surveillance.csv | one overall or safety class | 6 |
| process-stage-comparison.csv | one context and stage | 20 |
| bottleneck-reconciliation.csv | one evidence family | 8 |
| subgroup-window-support.csv | one window and support group | 6 |
| diagnostic-findings.json | one release summary | 1 |

Four SVG files communicate exact results. Every SVG requires a title, description, text labels, and a non-color signal marker.

## Claim boundary

The release may support a bounded synthetic process diagnosis. It cannot establish root cause, current real-service performance, staffing adequacy, staff productivity, real safety prevalence, real disparity, clinical effect, causal effect, or implementation authority.

# Reproducibility check

- Upstream files: `14`
- Upstream encounters: `43,628`
- Upstream query checks: `30 of 30 pass`
- Baseline: `Weeks 1 through 24`
- Evaluation: `Weeks 25 through 52`
- Analytic outputs: `13`
- Variation rows: `208`
- Signal records: `9`
- Stage comparison rows: `20`
- Bottleneck evidence rows: `8`
- Subgroup support rows: `6`
- Module version: `0.1.0`
- Commons release: `0.68.0`
- Result: `pass`
- Owner: `APP-3 analytics owner`

`freeze_upstream.py` verifies the Module 02 handoff. `build_diagnostic.py` reproduces every CSV, JSON, and SVG byte from the accepted upstream files and refuses a nonempty output target. The workspace validator rebuilds the diagnostic in a temporary target and compares all 13 files.

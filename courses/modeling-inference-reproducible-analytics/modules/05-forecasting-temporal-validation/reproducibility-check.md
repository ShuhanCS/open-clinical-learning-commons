# Reproducibility check

- Five upstream fingerprints: pass.
- Public source rows: 6,208 all-jurisdiction and 94 Massachusetts.
- Weekly continuity: 93 of 93 seven-day gaps.
- Target reconciliation: 94 of 94 rows.
- Temporal folds: five, with zero future rows in fit.
- Generated forecast checks: 20 of 20 pass.
- Fresh copied learner workspace: pass.
- Second build: byte-identical generated outputs.
- Existing-target refusal: pass.
- Release, starter, unfinished-submission, and broken-output validator routes: pass.
- Reference environment: Windows 11, Python 3.12.10.

Rebuild without overwriting the reference:

```text
python build_forecast_evidence.py reproduced-outputs --outputs-only
python validate_forecast_evidence.py . --mode submission
```

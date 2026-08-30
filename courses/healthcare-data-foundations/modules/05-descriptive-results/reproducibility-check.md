# Reference reproducibility check

- Date: 2026-08-30.
- Platform: Windows.
- Python: 3.12.10.
- Builder external dependencies: none.
- Notebook dependencies: pandas 3.0.5, JupyterLab 4.6.3, nbclient 0.10.2.
- Source and quality fingerprints verified: pass.
- Builder self-check: pass.
- Validator self-check: pass.
- Six CSV outputs reproduced byte for byte: pass.
- All 18 descriptive checks pass: pass.
- Notebook clean execution: pass.
- Existing target refused: pass.
- Incomplete submission rejected: pass.
- macOS reproduction: pending.
- Linux reproduction: pending.

```powershell
python build_descriptive.py --source data/resolved-analytic-table.csv --quality-results data/quality-rule-results.csv --target <new-output-directory>
python validate_descriptive.py .
```

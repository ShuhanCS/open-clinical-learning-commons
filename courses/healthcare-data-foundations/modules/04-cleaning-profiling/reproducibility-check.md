# Reference reproducibility check

- Date: 2026-08-30.
- Platform: Windows.
- Python: 3.12.10.
- SQLite: 3.49.1.
- Builder external dependencies: none.
- Profiler external dependencies: none.
- Notebook dependencies: pandas 3.0.5, JupyterLab 4.6.3, nbclient 0.10.2.
- Accepted fingerprint verified: pass.
- Fresh defect build reproduced all five data artifacts byte for byte: pass.
- Fresh profile reproduced all six evidence CSV files byte for byte: pass.
- All 28 rule counts reconciled: pass.
- Notebook clean execution: pass.
- Resolved table equals accepted source byte for byte: pass.
- Existing targets refused: pass.
- Incomplete submission rejected: pass.
- macOS reproduction: pending.
- Linux reproduction: pending.

Reference commands:

```powershell
python build_defect_release.py --source ..\03-cohorts-analytic-tables\outputs\analytic-table.csv --target <new-data-directory>
python profile_quality.py --data-dir <new-data-directory> --dictionary ..\03-cohorts-analytic-tables\data-dictionary.csv --target <new-output-directory>
python validate_defect_release.py .
```

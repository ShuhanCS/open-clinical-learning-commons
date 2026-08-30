# Reference reproducibility check

- Date: 2026-08-30.
- Platform: Windows.
- Python: 3.12.10.
- SQLite: 3.49.1.
- External Python dependencies: none.
- Upstream database rebuilt from the pinned archive: pass.
- Upstream database bytes and SHA-256 matched: pass.
- New output target used: pass.
- Builder self-check: pass.
- Validator self-check: pass.
- Four SQL files executed read-only: pass.
- Five output files reproduced byte for byte: pass.
- Nonempty target refused: pass.
- Incomplete package rejected: pass.
- macOS reproduction: pending.
- Linux reproduction: pending.

Reference command:

```powershell
python build_cohort.py --database <module-02-workspace>\data\fnd1_synthea_apr2020.sqlite --target <new-output-directory>
```

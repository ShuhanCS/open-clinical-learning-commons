# Reference reproduction record

- Reproducer: OpenAI Codex technical reference
- Date: 2026-08-30
- Environment: Windows 11 and PowerShell
- Python: 3.12.10
- Module packages: Module 04 and 05 release records preserve their tested numpy, pandas, scipy, scikit-learn, and statsmodels versions; Checkpoint 2 uses the Python standard library only
- Manifest verification: complete reference validator, pass
- Assembler self-check: two reference builds and one learner starter, pass
- Validator self-check: complete, starter, and deliberate failure cases, pass
- Whole-repository curriculum check: pass at Commons 0.46.0
- Independent calculations: 75-row confusion recount and 20-row candidate MAE/RMSE are preserved from Module 06 and rechecked by the checkpoint validator
- Output differences: none in accepted immutable fingerprints
- Return or referral: paired R execution and named independent reproduction remain open before alpha

The checkpoint validates immutable artifacts and independently recomputes selected contract facts. It does not rerun every upstream estimator. A changed immutable artifact returns to its owner and receives a new version.

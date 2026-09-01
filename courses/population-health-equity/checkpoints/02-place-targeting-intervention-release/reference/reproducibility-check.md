# Reproducibility check

- Candidate files: `1,030`.
- Nested immutable rows: `966`.
- Checkpoint files: `1,051`.
- Candidate manifest bytes: `249,511`.
- Candidate manifest SHA-256: `6d403bfb0e4bb6f177400ae97a3b1d89cf968c35b24482f64cea6b927f397f83`.
- External Python dependencies: `0`.
- Point check: `10 + 15 + 0 = 25; the checkpoint adds zero`.
- Gate check: `22 + 26 + 34 + 24 = 106; all pass`.
- Independent reference assembly: `two builds match byte for byte`.
- Learner candidate identity: `matches the reference candidate`.
- Existing-target refusal: `pass`.
- Copied validator: `pass`.
- Changed candidate: `rejected`.
- Changed outer manifest: `rejected`.
- Changed point total: `rejected`.
- Duplicate score: `rejected`.
- Failed checkpoint gate: `rejected`.
- Hidden access or capacity condition: `rejected`.
- Intervention-ready mutation: `rejected`.
- Outcome or effect mutation: `rejected`.
- Accepted-challenger mutation: `rejected`.
- Missing owner mutation: `rejected`.
- Invalid Module 07 permission: `rejected`.
- Implementation or deployment mutation: `rejected`.
- Learner starter submitted as complete: `rejected`.
- Independent reproduction status: `pending before alpha`.

Run from the package root:

```powershell
python build_checkpoint.py --self-check
python validate_checkpoint.py --self-check
```

To assemble a complete reference workspace for inspection:

```powershell
python build_checkpoint.py --target .work/reference --reference
python .work/reference/validate_checkpoint.py .work/reference
```

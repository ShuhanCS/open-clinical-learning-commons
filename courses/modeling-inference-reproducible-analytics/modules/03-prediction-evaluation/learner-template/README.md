# FND-2 Module 03 learner release

This workspace contains the seven fingerprinted Module 01 and 02 inputs, frozen model contract, deterministic builder, validation tool, reference evidence tables, and records you must complete.

## Workflow

1. Read `data-spec.md`, `source-record.yml`, `model-contract.json`, and `assessment.md`.
2. Explain the training, validation, and test roles before fitting.
3. Rebuild into a new target: `python build_prediction_evidence.py reproduced-outputs --outputs-only`.
4. Review the training resampling and transformed features.
5. Apply the validation selection rule without using test results.
6. Explain why the leaked model is ineligible.
7. Defend the validation threshold consequence and lock.
8. Interpret exact test metrics, calibration, confusion counts, and subgroup suppression.
9. Complete all five prompted Markdown records.
10. Run `python validate_prediction_evidence.py . --mode submission`.

Do not change the source files or reference outputs to make the submission pass. If a contract change is necessary, document the return and version decision instead.

No artifact in this workspace permits clinical use or deployment.

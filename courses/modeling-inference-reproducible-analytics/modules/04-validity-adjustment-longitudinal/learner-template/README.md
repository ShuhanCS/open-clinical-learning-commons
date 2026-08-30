# FND-2 Module 04 learner release

This workspace contains nine fingerprinted accepted inputs, three deterministic generated fixtures, a public-safe Synthea selection case, exact model evidence, and the decision records you must complete.

## Workflow

1. Read `source-record.yml`, `data-spec.md`, and `assessment.md`.
2. Classify all five analytic aims before interpreting a model.
3. Rebuild with `python build_validity_evidence.py reproduced-outputs --outputs-only`.
4. Complete the causal screen and narrate the structured DAG.
5. Compare overlap, balance, selection, missingness, and all seven effect estimates.
6. Interpret repeated-measures and survival quantities.
7. Record specialist triggers, accessibility, reproduction, and material AI use.
8. Choose `continue with conditions`, `revise`, or `stop`.
9. Run `python validate_validity_evidence.py . --mode submission`.

Do not edit accepted inputs or reference outputs to make the submission pass. If a design contract must change, document the return and version decision.

No artifact in this workspace permits clinical inference, care, or deployment.

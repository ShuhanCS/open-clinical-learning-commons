# Reproducibility check

- Release build: pass.
- Deterministic seed: `20260830`.
- Accepted upstream fingerprints: pass.
- Generated validity checks: 16 of 16 pass.
- Fresh copied learner workspace: pass in builder self-check.
- Independent rebuild into a second target: byte-identical outputs.
- Existing-target refusal: pass.
- Release, starter, incomplete-submission, and broken-output validator routes: pass.
- Platform used for the reference: Windows 11, Python 3.12.10.
- R status: script supplied; paired R execution awaits a named managed R environment.

Reproduce from a learner workspace with:

```text
python build_validity_evidence.py reproduced-outputs --outputs-only
python validate_validity_evidence.py . --mode submission
```

Do not overwrite `outputs/`. A separate target keeps the accepted reference visible for comparison.

# Reproducibility check

- 13 accepted fingerprints: pass.
- 18 accepted-contract tests: pass.
- Ten seeded failure rejections: pass for intended codes.
- Three independent recalculations: pass.
- Four claim adjudications: complete.
- Seven data-class rules and seven summary gates: pass.
- Copied learner workspace reproduction: pass.
- Existing-target refusal: pass.
- Standard-library runner: pass on Python 3.12.10, Windows 11.

Run `python build_agent_test_evidence.py reproduced-outputs --outputs-only`, then `python validate_agent_test_evidence.py . --mode submission`.

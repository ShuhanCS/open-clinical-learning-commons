# FND-2 Module 06: Agent-assisted modeling and testing

This 16-hour module verifies accepted prediction, validity, and forecasting evidence without refitting it. The standard-library suite fingerprints 13 artifacts, passes 18 accepted-contract tests, rejects ten seeded failures for ten exact reasons, independently recalculates three material results, and adjudicates four agent claims.

## Workflow

1. Read `data-spec.md`, `source-record.yml`, `test-contract.json`, `prompt-constraints.md`, and `assessment.md`.
2. Classify every shared input and write a bounded task plan.
3. Rebuild: `python build_agent_test_evidence.py reproduced-outputs --outputs-only`.
4. Inspect all accepted tests and seeded failure codes.
5. Independently verify a material claim from lower-level evidence.
6. Adjudicate agent claims as accept, modify, reject, or refer.
7. Complete trace, correction, accessibility, AI-use, sign-off, and progression records.
8. Run `python validate_agent_test_evidence.py . --mode submission`.

A passing suite proves only that declared contracts behaved as tested. It does not approve clinical use or deployment.

Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

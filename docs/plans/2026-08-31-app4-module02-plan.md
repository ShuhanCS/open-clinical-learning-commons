# APP-4 Module 02 build plan

## Purpose

Build `oclc-app4-02`, Decision support logic, triggers, and data, as a deterministic runnable release candidate at Module version `0.1.0` and Commons release `0.78.0`.

The module decides whether the fictional `CGH-GIM-01` advisory concept has a complete, testable, nonproduction logic and event-time input contract. It does not fit a model, use real patient data, accept a clinical threshold, fire a clinical alert, or authorize clinical action.

## Fixed course handoff

- Course: APP-4, Data for Clinical Decision Support.
- Week: 2.
- Learner time: 16 hours.
- Course points: 20 of the 40-point Week 3 checkpoint.
- Continuing concept: a nonbinding advisory asking a clinician to consider whether confirmatory HbA1c testing is appropriate.
- Required inheritance: preserve the accepted Module 01 use-case, source, authority, and progression boundaries.
- Permitted progression: hand a complete candidate logic, input, terminology, trace, and synthetic-test contract to Module 03 for historical evidence and threshold evaluation.
- Prohibited progression: model fitting in this module, threshold acceptance, real-patient scoring, clinical alerting, implementation, or deployment.

## Versioned synthetic-source release

Generate a complete synthetic FHIR R4 teaching release from the official Synthea 4.0.0 runnable JAR using a pinned portable Java runtime, fixed random and clinician seeds, fixed reference and end dates, 1,000 Massachusetts adults, a checked configuration, and a captured generation log.

Do not commit the Synthea JAR or Java runtime. Record their official URLs, versions, byte counts, and SHA-256 identities as reproducible build inputs. Commit the complete deterministically compressed generated release, its resource inventory, and its manifest.

A separate deterministic Commons layer assigns the fictional service, encounter decision moment, event-time input state, rule-test fixture, and known truth needed for teaching. It must never copy a public NHANES row or imply that synthetic records validate local prevalence, clinical correctness, workflow fit, or safety.

## Logic and input outputs

- `logic-specification.csv`: ordered candidate branches, nonaction, and human ownership.
- `input-contract.csv`: event-time source, terminology, unit, value-state, staleness, and failure handling.
- `trigger-suppression-matrix.csv`: positive, negative, boundary, missing, stale, inconsistent, duplicate, delayed, terminology-mismatch, version-mismatch, and silent-failure cases.
- `rule-test-cases.csv`: deterministic inputs and expected nonproduction branch traces.
- `rule-test-results.csv`: executable comparison of expected and observed traces.
- `terminology-map.csv`: exact FHIR, LOINC, SNOMED CT, and local teaching identifiers with claim limits.
- `synthetic-release-interpretation.md`: provenance, generation result, limits, and open review conditions.
- `logic-change-control.md`: version, approval, rollback, and invalidation rules.
- `ai-use.md`: tool use, human decisions, and independent checks.
- `progression-decision.md`: bounded Module 03 handoff.

The candidate score threshold remains a named external configuration value. Mock score fixtures may test branch mechanics, but this module cannot estimate, optimize, recommend, or accept a clinical threshold. Module 03 owns evidence-supported threshold analysis and human acceptance.

## Required implementation

- durable 21-section module specification;
- reproducible synthetic generation, normalization, deterministic compression, and committed-release verification;
- deterministic learner and reference workspace builder with immutable manifests;
- executable rule engine limited to nonproduction fixture evaluation;
- validator with complete, starter, copied-workspace, source-mutation, placeholder, trace, threshold-authority, and prohibited-live-use tests;
- assessment, rubric, instructor notes, data specification, decision contract, source record, release record, environment record, semantic version, and generation log;
- course, root README, build-ledger, and central curriculum-validator integration.

## Noncompensable gates

1. The official Synthea executable and Java runtime have exact accepted identities.
2. The complete generated FHIR release has a reproducible manifest, resource counts, bytes, hashes, and zero parse failures.
3. `CGH-GIM-01` and every clinical or workflow row remain explicitly fictional and synthetic.
4. Module 01 use-case, source-role, nonaction, stop-right, and authority boundaries remain unchanged.
5. One workflow hook, decision moment, user, intended support, and nonaction are explicit and testable.
6. Every required input has an event-time availability, terminology, unit, value-state, staleness, and failure contract.
7. Normal, boundary, missing, stale, inconsistent, duplicate, delayed, terminology-mismatch, version-mismatch, and silent-failure cases are executable.
8. Every evaluated fixture produces a deterministic branch trace and expected reason code.
9. Mock scores test mechanics only and cannot be described as predictions, evidence, performance, or clinical recommendations.
10. No model is fit and no clinical threshold is selected or accepted.
11. AI use is disclosed and independently checked.
12. Progression permits Module 03 evidence construction only and preserves every prohibited authority.

## Verification and release

1. Verify or acquire the pinned build inputs, then regenerate the full synthetic release from an empty output directory.
2. Rebuild all inventories, teaching fixtures, and rule-test results twice and require stable identities.
3. Build two reference workspaces and require byte-identical manifests.
4. Build and validate an incomplete learner workspace.
5. Reject changed source bytes, missing evidence, copied answers, placeholders in a complete package, unexpected traces, threshold-acceptance claims, and any live-use or deployment claim.
6. Run the complete curriculum regression.
7. Advance Commons from `0.77.0` to `0.78.0`.
8. Commit, push, and remote-verify Module 02 as one isolated unit.

# APP-4 Module 01 build plan

## Purpose

Build `oclc-app4-01`, Framing a decision support use case, as a deterministic runnable release candidate at Module version `0.1.0` and Commons release `0.77.0`.

The module decides whether the fictional `CGH-GIM-01` advisory concept is bounded and supported well enough to begin logic and input specification in Module 02. It does not fit a model, choose a clinical target or threshold, fire an alert, score a patient, or authorize clinical action.

## Fixed course handoff

- Course: APP-4, Data for Clinical Decision Support.
- Week: 1.
- Learner time: 15.5 hours.
- Course points: 0.
- Week 3 components owned later: Module 02, 20 points; Module 03, 20 points.
- Continuing concept: an advisory card asking a clinician to consider confirmatory HbA1c testing.
- Permitted progression: begin Module 02 logic and input specification for curriculum construction only.
- Prohibited progression: modeling, threshold selection, alert firing, live scoring, clinical use, implementation, or deployment.

## Full public-source release

Acquire all 16 complete official NHANES XPT files named in the APP-4 source record:

- cycles 2013-2014, 2015-2016, 2017-2018, and 2021-2023;
- components DEMO, BMX, DIQ, and GHB for every cycle; and
- no convenience samples or prefiltered downloads.

For every file, record URL, cycle, component, suffix, retrieval date, raw bytes, raw SHA-256, deterministic gzip bytes and SHA-256, rows, columns, `SEQN` uniqueness, duplicate count, field inventory, codebook route, survey-design role, teaching role, and claim limit.

The committed raw layer contains deterministic gzip copies of all 16 complete XPT files. The profiler must refuse a changed, missing, truncated, duplicated, or schema-inconsistent release.

## Source-feasibility outputs

- `data/source-inventory.csv`: one exact row for each of the 16 complete XPT releases.
- `data/field-inventory.csv`: one row for every field in every accepted file.
- `data/cycle-join-profile.csv`: cycle-specific source support and join coverage without defining a final analytic cohort.
- `data/standards-inventory.csv`: CDS Hooks, FHIR R4, Synthea, and ONC SAFER roles and limits.
- `data/raw/*.xpt.gz`: all 16 complete, deterministically compressed releases.

## Learner and reference records

- `cds-use-case-charter.md`
- `user-workflow-action-map.csv`
- `intended-use-boundary.csv`
- `source-feasibility-interpretation.md`
- `public-synthetic-data-role-map.csv`
- `input-availability-inventory.csv`
- `synthetic-generation-contract.md`
- `stakeholder-accountability-map.csv`
- `claim-boundary.csv`
- `ai-use.md`
- `progression-decision.md`

The learner template keeps immutable source evidence and module controls complete while leaving assessed records incomplete. The reference workspace contains one bounded construction answer and preserves all open clinical, survey-methods, interoperability, safety, and governance conditions.

## Required implementation

- durable 21-section module specification;
- deterministic source acquisition, profiling, and committed-release verification;
- deterministic learner/reference workspace builder with an immutable manifest;
- validator with complete, starter, copied-workspace, source-mutation, placeholder, progression, and prohibited-authority tests;
- assessment, rubric, instructor notes, data specification, decision contract, source record, release record, requirements, and semantic version;
- course, root README, build-ledger, and central curriculum-validator integration.

## Noncompensable gates

1. All 16 complete public files have exact accepted identities.
2. All 16 files parse and have unique `SEQN` within file.
3. Cycle identity, component identity, and suffix are consistent.
4. Field and join profiles reproduce exactly.
5. NHANES remains historical survey evidence, not local validation.
6. `CGH-GIM-01` and all future workflow records remain explicitly fictional and synthetic.
7. The user, workflow moment, intended action, nonaction, and prohibited actions are explicit.
8. Clinical and patient consequences, burden, and stop rights have human owners.
9. Public and synthetic data roles are separate.
10. No model, final target, threshold, alert, or clinical recommendation appears early.
11. AI use is disclosed and independently checked.
12. Progression permits Module 02 construction only and preserves every prohibited authority.

## Verification and release

1. Rebuild the committed source profiles from all 16 compressed raw files.
2. Build two reference workspaces and require byte-identical manifests.
3. Build and validate an incomplete learner workspace.
4. Validate the committed reference and learner packages.
5. Reject changed source bytes, missing evidence, copied answers, placeholders in a complete package, invalid progression, and any live-use or deployment claim.
6. Run the complete curriculum regression.
7. Advance Commons from `0.76.0` to `0.77.0`.
8. Commit, push, and remote-verify Module 01 as one isolated unit.

# APP-5 Checkpoint 02 implementation plan

## Purpose

Build the separate APP-5 Week 6 checkpoint as a deterministic release candidate. The checkpoint must freeze the accepted Module 04 place evidence, Module 05 targeting and fairness evidence, and Module 06 intervention, monitoring, accountability, and embedded-ML evidence without recomputing or repairing an upstream result.

## Release identity

- Checkpoint ID: `oclc-app5-cp02`
- Version: `0.1.0`
- Commons release: `0.94.0`
- Package: `courses/population-health-equity/checkpoints/02-place-targeting-intervention-release/`
- Specification: `docs/curriculum/courses/APP-5/checkpoints/02-place-targeting-intervention-release-spec.md`
- Due point: end of instructional Week 6
- Course points: 25

## Accepted inputs

| Module | Complete reference files | Immutable manifest rows | Manifest bytes | Manifest SHA-256 | Points | Gates |
|---|---:|---:|---:|---|---:|---:|
| APP-5 Module 04 | 287 | 271 | 48,575 | `c0300a2eff3fa9ede53eab4723fe7296cad341cf5f6e4e5e76fde25881652629` | 10 | 22 |
| APP-5 Module 05 | 340 | 318 | 62,245 | `54da8bae1c36ae49397b278fc636f2b8e112f55406acbfc57c94a215087818da` | 15 | 26 |
| APP-5 Module 06 | 403 | 377 | 79,357 | `2e9358d65c889e786db474de97e223982a8d238dba64ec283c6dc950ebb89e82` | 0 | 34 |
| Total | 1,030 | 966 |  |  | 25 | 82 |

## Required build

1. Create a standard-library checkpoint assembler that calls the three accepted workspace builders.
2. Refuse an existing destination and require every accepted module identity before copying evidence.
3. Place the exact complete workspaces under `candidate/module-04`, `candidate/module-05`, and `candidate/module-06`.
4. Create a sorted outer manifest with the path, bytes, SHA-256, source module, source version, and role for all 1,030 candidate files.
5. Package 12 parallel learner and reference checkpoint records.
6. Keep the point architecture exact: Module 04 contributes 10 points once, Module 05 contributes 15 points once, Module 06 contributes zero points, and the checkpoint adds zero points.
7. Carry all 82 inherited gates and add 24 checkpoint-integrity gates.
8. Preserve the responsible teaching map, four targeting comparisons, community-review candidate, access and capacity limits, dry-run incidents, six triggers, intervention-not-ready decision, and rejected clustering challenger.
9. Permit Module 07 curriculum construction only for clinician leadership interpretation, recommendation, accountability, and defense.
10. Prohibit real need determination, consent, eligibility, outreach, funding, allocation, community action, service delivery, intervention-effect estimation, implementation, production connection, and deployment.

## Checkpoint records

The learner and reference packages contain the same 12 record names:

1. `README.md`
2. `evidence-index.csv`
3. `place-targeting-intervention-readiness-review.md`
4. `checkpoint-score.csv`
5. `checkpoint-gates.csv`
6. `responsible-claims-audit.md`
7. `checkpoint-defense.md`
8. `reviewer-record.md`
9. `conditions-register.csv`
10. `reproducibility-check.md`
11. `ai-use.md`
12. `progression-decision.md`

## Validation

The validator must verify the complete file inventory, every outer and nested fingerprint, exact module and release identities, the score and gate architecture, accepted place and targeting results, access and burden limits, intervention and monitoring facts, challenger rejection, accountable owners, pending human review, Module 07 boundary, and absent real-world authority.

The self-check must build independent reference and learner packages, run the copied validator, reject learner records submitted as complete, and reject protected mutations to the candidate, point total, gates, intervention readiness, challenger decision, ownership, progression, and authority.

## Integration and release

Update the root and course README files, root `VERSION`, APP-5 course specification, curriculum catalog, build ledger, and central curriculum checker. Run focused checkpoint checks and the relevant APP-5 repository checks. Commit only the checkpoint task files, push `feat/roadmap-course-catalog`, and verify the remote commit before beginning Module 07.

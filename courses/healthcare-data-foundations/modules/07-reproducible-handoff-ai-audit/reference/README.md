# FND-1 reproducible toolkit candidate

## Release identity

- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons
- Candidate version: 0.1.0.
- Required accepted tag: `fnd1-handoff-v0.1.0`.
- Upstream checkpoint: `oclc-fnd1-cp2` version 0.1.0.
- Upstream modules: `oclc-fnd1-04`, `oclc-fnd1-05`, and `oclc-fnd1-06`, each version 0.1.0.
- Package: 90 files with 74 immutable manifest rows.
- Reference status: complete technical fixture; an accepted learner release records its full reviewed commit before tagging.

## Receiver decision

The health-system analytics engineering lead decides whether to accept, condition, revise, or refer this candidate for downstream modeling or applied analysis. Acceptance means the technical synthetic-data foundation is reusable under its conditions. It does not authorize production deployment, clinical approval, or real-patient use.

## Reproduction route

Use Python 3.12.10 and the exact `requirements.txt` pins. Verify the 8,982,431-byte Synthea archive and SHA-256 `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`. Run the accepted Module 02 database builder, Module 03 cohort builder and SQL, Module 04 defect builder and profiler, Module 05 descriptive builder, and Module 06 renderer in order with explicit input and new target paths. Compare every accepted output by byte count and SHA-256, then run `python validation/validate_toolkit.py <toolkit-folder>` from the repository module package.

The source ZIP, generated SQLite database, caches, and virtual environment remain outside the toolkit and Git.

## Evidence map

- Source, schema, and pipeline code: `source-code/` and `requirements.txt`.
- Analytic release: `data/`.
- Quality and retained conditions: `quality/`, `evidence/module-04-stop-fix-proceed.md`, and `documentation/checkpoint2/quality-decision.md`.
- Descriptive evidence: `evidence-tables/` and `documentation/checkpoint2/interpretation-memo.md`.
- Figures and equivalent access: `tables/`, `figures/`, `alt-text/`, `figure-registry.csv`, and `documentation/checkpoint2/accessibility-synthesis.md`.
- Source and assembly provenance: `provenance/` and `documentation/checkpoint2/`.
- Release and AI accountability: root release records, `documentation/ai-audit.md`, and `audit/prompt-log.csv`.
- Decision preparation: `component-score.csv`, `release-checklist.md`, `defense/`, and `review-disposition.md`.

## Conditions and stop rules

D01 through D20 remain resolved and N01 through N08 remain conditions. Exact denominators, synthetic interval meaning, selected-cohort time wording, and every equivalent access route remain required. Named human review and macOS or Linux reproduction remain pending. A changed immutable file, restricted data, hidden dependency, broken access route, unsupported real-world claim, incomplete AI disclosure, or failed defense requires revision or referral.

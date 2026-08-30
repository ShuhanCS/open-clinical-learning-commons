# Reproducibility check

- Accepted candidate files: `160 across Modules 04 through 06`
- Assembled checkpoint files: `174`
- Candidate manifest rows: `160`
- Candidate manifest identity: `recorded in release.json after deterministic assembly`
- Two reference builds: `match byte for byte`
- Learner and reference candidate manifests: `match`
- Existing target result: `rejected`
- Copied-validator result: `pass`
- Candidate mutation result: `rejected`
- Duplicate-score result: `rejected`
- Failed-gate result: `rejected`
- Invalid-progression result: `rejected`
- Independent reproduction: `pending named independent reviewer before alpha`

The builder assembles accepted module workspaces without recomputing their evidence. A changed source workspace, nested manifest, score, gate, or progression value invalidates the checkpoint.

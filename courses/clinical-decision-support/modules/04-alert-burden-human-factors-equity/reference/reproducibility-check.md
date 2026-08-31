# Reproducibility check

- Workflow builder: `python build_workflow.py --self-check`.
- Workspace builder: `python build_workspace.py --self-check`.
- Workspace validator: `python validate_workspace.py --self-check`.
- Python dependencies: standard library only.
- Checkpoint candidate manifest SHA-256: `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`.
- Workflow output-manifest digest: `4ab020f4862fe06ea3c877d7302afa988b7069ce5922ddb2f578841d22838911`.
- Deterministic workflow builds: byte-identical.
- Existing-target behavior: refused.
- Nested immutable rows: 204 verified.
- Workflow invariants: 20 of 20 pass.
- Independent reproduction: required before alpha and not yet signed.

The workflow builder reads accepted gzip, CSV, and JSON files by exact bytes and SHA-256. It does not download, refit, retune, impute, or alter the Week 3 evidence. Deterministic gzip files use a zero modification time.

Reproduction confirms package mechanics. It does not confirm local workflow, burden, usability, equity, safety, clinical validity, implementation readiness, or deployment readiness.

# Reproducibility check

- Python: `3.12.10`
- NumPy: `2.0.2`
- pandas: `3.0.3`
- scikit-learn: `1.9.0`
- Source inputs: `13 exact files verified by size and SHA-256`
- Split: `stratified 70/30 with random_state 20260830`
- Model: `200 trees, depth 3, minimum leaf 25, max_features None, n_jobs 1`
- Determinism: `two builds match byte for byte`
- Mutation check: `changed response input rejected`
- Existing target: `overwrite rejected`
- Outputs: `17 deterministic files`
- Result: `pass`

Run `python build_partnered_improvement_ml.py --self-check`, `python build_workspace.py --self-check`, and `python validate_workspace.py --self-check` from the module or repository environment.

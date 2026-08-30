# Reproducibility check

- Upstream cohort SHA-256: `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`
- Upstream rows and fields: `476 rows, 49 fields`
- Analysis ID: `app1-risk-adjustment-v1`
- Field-role rows: `49`
- Bootstrap: `300 successful fits, 0 failed fits, seed 20260830`
- Python result: `two complete builds match byte for byte`
- Builder overwrite result: `existing target rejected`
- Changed-upstream result: `rejected`
- Changed-field-role result: `rejected`
- Python environment: `Python 3.12 with the versions in environment.yml`
- R status: `script supplied; execution awaits a named managed R environment`

The frozen Python build is the reference. Every released output has fixed rows, fields, bytes, and SHA-256 in the validator. The R route remains pending until a reviewer runs it and reconciles the same model formula and group summaries.

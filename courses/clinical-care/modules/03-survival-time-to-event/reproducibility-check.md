# Reproducibility check

- Upstream cohort SHA-256: `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`
- Upstream rows and fields: `476 rows, 49 fields`
- Analysis ID: `app1-survival-v1`
- Python result: `two complete builds match byte for byte`
- Builder overwrite result: `existing target rejected`
- Changed-upstream result: `rejected`
- Python environment: `Python 3.12 with the versions in environment.yml`
- R status: `script supplied; execution awaits a named managed R environment with the survival package`

The Python build is the frozen reference. The R route is a read-run-interpret exercise and must be recorded as pending until someone runs it in the named environment and reconciles its output.

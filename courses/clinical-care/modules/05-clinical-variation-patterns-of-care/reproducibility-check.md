# Reproducibility check

- Synthea SQLite SHA-256: `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`
- SQLite access: `read-only`
- Analysis cohort SHA-256: `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`
- Expected-outcomes SHA-256: `e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e`
- Analysis ID: `app1-clinical-variation-v1`
- Randomness: `none`
- Python result: `two complete builds match byte for byte`
- Builder overwrite result: `existing target rejected`
- Changed-database result: `rejected`
- Changed-cohort result: `rejected`
- Changed-expected-outcome result: `rejected`
- Changed-contract result: `rejected`
- Python environment: `Python 3.12 with the versions in environment.yml`

The released validator fixes every output's rows, fields, bytes, and SHA-256. It also checks source conservation, support decisions, claim boundaries, the 20-point score, and the four-part Module 06 handoff.

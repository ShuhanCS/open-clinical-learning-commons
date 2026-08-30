# Reproducibility check

- Generator version: `0.1.0`
- Generator seed: `73002`
- Source release: `cgh-ed-01-operational-v1`
- Raw tables: `9`
- Raw rows: `318,732`
- Measure outputs: `8`
- Query checks: `30 of 30 pass`
- Module version: `0.1.0`
- Commons release: `0.67.0`
- Result: `pass`
- Owner: `APP-3 analytics owner`

`generate_operational_release.py`, `freeze_upstream.py`, and `build_measures.py` reproduce the accepted source, handoff, and output identities. The workspace validator independently rebuilds the outputs and compares their SHA-256 fingerprints. The builder refuses to overwrite a nonempty target.

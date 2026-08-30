# Reference version policy

Current checkpoint version: `0.1.0`.

Required checkpoint tag: `fnd1-checkpoint1-v0.1.0`.

## Semantic changes

- Patch: correct a record or validator defect without changing required paths, SQL meaning, or expected output.
- Minor: add compatible evidence or a supported platform while preserving the current contract and bytes.
- Major: change a required path, source release, cohort definition, analytic grain, or field contract incompatibly.

## Version chain

- Module 01: 0.1.0 and `fnd1-setup-v0.1.0`.
- Module 02: 0.1.0.
- Module 03: 0.1.0 and cohort definition 0.1.0.
- Checkpoint 01: 0.1.0.

## Tag evidence

The technical reference records the required tag name. A course release is tagged only after both decision owners review a clean commit and sign `review-disposition.md`.

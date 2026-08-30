# Event validation record

- Service: `CGH-ED-01`
- Release: `cgh-ed-01-operational-v1`
- Accepted encounters: `43,628`
- Valid event sequences: `43,627`
- Invalid retained sequences: `1`
- Clinician times available: `39,974`
- Clinician times unavailable: `3,654`
- Completed encounters: `39,975`
- Left before seen: `3,653`
- Reconciliation: `39,975 + 3,653 = 43,628`
- Query checks: `30 of 30 pass`
- Owner: `CGH-ED-01 data steward`

The accepted clock order is arrival, triage, roomed, clinician, disposition, and departure when those states apply. A left-before-seen encounter can end without clinician contact. D008 stays in the accepted denominator but its clinician duration and full-sequence validity are unavailable. Raw defects stay unchanged in `data/raw`; clean-layer changes are recorded in SQL and `defect-repair-log.csv`.

These checks establish that measures can be calculated. They do not identify a delay source or authorize an operational response.

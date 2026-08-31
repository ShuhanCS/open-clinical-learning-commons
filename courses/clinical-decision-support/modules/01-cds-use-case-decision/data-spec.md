# APP-4 Module 01 data specification

## Public source layer

The immutable public layer contains 16 complete CDC NCHS NHANES XPT files. Each cycle contributes demographics (`DEMO`), body measures (`BMX`), diabetes questionnaire (`DIQ`), and glycohemoglobin (`GHB`). Files join on `SEQN` within the same cycle only.

| Cycle | Role | All-four-component intersection |
|---|---|---:|
| 2013-2014 | development evidence | 6,979 |
| 2015-2016 | development evidence | 6,744 |
| 2017-2018 | temporal holdout | 6,401 |
| 2021-2023 | later-cycle transport stress test | 7,199 |

These intersections describe source support. They are not final analytic cohorts.

## File contracts

`data/source-inventory.csv` has one row per complete XPT file with:

- source ID, cycle, component, and suffix;
- exact data and codebook URLs;
- retrieval date;
- raw filename, bytes, and SHA-256;
- deterministic gzip filename, bytes, and SHA-256;
- rows, columns, unique `SEQN`, and duplicate count; and
- teaching role and claim limit.

`data/field-inventory.csv` has one row per accepted source field with source identity, field order, name, pandas data type, row count, nonmissing count, missing count, distinct nonmissing count, and source role.

`data/cycle-join-profile.csv` has one row per cycle with component rows, pairwise DEMO joins, the all-four intersection, required-field presence, survey-design-field presence, and an interpretation boundary.

`data/standards-inventory.csv` records the accepted CDS Hooks, FHIR R4, Synthea, and ONC SAFER routes, versions, teaching roles, and limits. These standards records contain no protected or clinical data.

## Raw-file policy

All 16 complete XPT files are stored as deterministic gzip files under `data/raw/`. Compression uses an empty embedded filename and an `mtime` of zero. The profiler verifies both the decompressed official identity and the committed gzip identity.

The raw layer is immutable inside a module release. A source refresh requires exact review, a new source inventory, new hashes, regenerated profiles, an explicit semantic-version decision, and revalidation of every downstream package.

## Survey design and missingness

Every DEMO file contains `SDMVPSU`, `SDMVSTRA`, and `WTMEC2YR`. Their presence does not choose a final analysis weight. Module 03 must document the weight and variance decision for every estimate and any combined-cycle analysis.

Missing values remain missing. Questionnaire response codes retain their codebook meaning. No unavailable value becomes zero. A complete `SEQN` join does not imply complete candidate inputs or an observed outcome.

## Data-role boundary

NHANES may support historical prevalence, model development, temporal validation, calibration, threshold, subgroup-support, and later-cycle transport analysis after later module gates pass. It cannot supply the fictional service's workflow, input availability, alert count, interaction, latency, burden, incident, or silent-failure truth.

The future synthetic layer supplies those missing roles. Public participant identities and values cannot be copied into the synthetic service. `CGH-GIM-01` remains fictional.

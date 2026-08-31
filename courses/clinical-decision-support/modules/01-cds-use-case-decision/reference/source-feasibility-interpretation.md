# Source feasibility interpretation

## Accepted release

All 16 complete official NHANES XPT files were acquired on 2026-08-30. The release covers four cycles and four components per cycle. It contains 34,221,200 raw bytes, 145,563 component rows, and 442 source fields. The deterministic repository copies total 3,149,043 gzip bytes.

Every file parses and contains `SEQN`. Each file has a unique `SEQN` with zero duplicates. The four-component intersections are 6,979 for 2013-2014, 6,744 for 2015-2016, 6,401 for 2017-2018, and 7,199 for 2021-2023.

## What is feasible later

The accepted files contain the structural elements needed to consider a later historical evidence build: age and survey design in DEMO, body mass index in BMX, diabetes questionnaire evidence in DIQ, and glycohemoglobin in GHB. `SDMVPSU`, `SDMVSTRA`, and `WTMEC2YR` appear in every DEMO file.

This is source feasibility, not an accepted cohort or model. The exact clinical target, eligibility, exclusions, predictor list, weight treatment, combined-cycle approach, missing-input rule, and threshold remain open.

## Cycle differences

The cycles are not treated as interchangeable. The 2021-2023 DIQ release has 9 fields, while each earlier DIQ release has 54. BMX and DEMO field counts also differ. Module 03 must preserve cycle identity and document every harmonization decision.

The 2013-2014 and 2015-2016 cycles are assigned to development evidence, 2017-2018 to a temporal holdout, and 2021-2023 to a later-cycle transport stress test. That assignment does not claim that one known event caused a difference between cycles.

## What NHANES cannot answer

NHANES cannot establish local `CGH-GIM-01` prevalence, input availability at an encounter, local calibration, workflow fit, card burden, clinician interaction, patient consequence, latency, incident capture, silent failure, prospective utility, or deployment safety. It cannot identify the correct local threshold or authorize testing.

Those roles require a separate synthetic workflow layer for teaching and, outside the course, local governance and evidence.

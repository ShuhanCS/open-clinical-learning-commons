# Data specification

## Frozen handoff

`upstream/module05-reference/` is the complete accepted APP-5 Module 05 reference workspace. `upstream/module05-handoff-manifest.csv` records its frozen identity. Module 06 reads the 1,597-row linked candidate table and the 28 rows selected by the community-review comparison. It does not recompute public measures, geographic evidence, fictional resource rules, consequences, sensitivity tests, points, or gates.

## Fictional monitoring source

`data/raw/fictional-monitoring-dry-run.csv.gz` contains 280 deterministic test records. Source `fma-dp-01-monitoring-dry-run-v1` uses seed `73056` and stable SHA-256 routing. The source does not use public modeled prevalence to generate response, access, scheduling, burden, feedback, objection, incident, escalation, or pause fields.

Every row is a software and governance test. It is not a person, encounter, service, clinical outcome, community statement, or implementation record. Outcomes are intentionally unavailable. `data/synthetic-source-manifest.csv` pins all six source files by row count, byte count, and SHA-256.

## Monitoring measures

`data/monitoring-measures.csv` declares 20 measures before analysis. Each measure has a numerator, denominator, cadence, source, owner, unavailable state, direction, teaching threshold, threshold origin, and human response. Thresholds are classroom triggers. They are not validated clinical or operational standards and cannot start an automatic action.

## Fixed clustering challenger

`data/cluster-feature-contract.csv` fixes nine area-level features. Public prevalence, uncertainty width, and log-transformed adult population remain public context. Capacity, travel, burden, access readiness, and staff readiness remain fictional. Missing features fail the build, and no imputation is allowed.

`data/challenger-variants.csv` fixes KMeans with four clusters, 20 initializations, the Lloyd algorithm, seed `73056`, four alternate seeds, and three scaling challengers. Selection labels are never features. Cluster identity cannot rank, select, exclude, allocate, infer individual traits, determine fairness, replace the transparent rule, or bypass community review.

## Output boundary

The 14 files in `outputs/` are deterministic teaching evidence. Their build report records six monitoring triggers and rejects the clustering challenger under the declared standard. No output estimates intervention effects or supports real-world action.

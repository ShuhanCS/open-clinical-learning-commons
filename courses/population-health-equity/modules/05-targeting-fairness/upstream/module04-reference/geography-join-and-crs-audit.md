# Geography join and coordinate-system audit

## Frozen inputs

The module reads the complete accepted APP-5 Week 3 checkpoint. The 45,547-byte handoff manifest fingerprints 240 files with SHA-256 `db70b4e20a17fbddd2b49f7647dd9ce5bcd064e01af5e7a7e23df9122889914e`.

The assessed measure comes from the frozen Module 02 table: CDC PLACES 2023 modeled crude diabetes prevalence in the 2025 census-tract release. The table has 1,597 rows. It remains separate from the fictional synthetic event evidence.

## Key and join result

The join uses the 11-character tract GEOID without numeric coercion. The geometry contains 1,620 unique keys. The PLACES table contains 1,597 unique keys. The accepted linkage audit contains all 1,620 tract states.

- Matched geometry and PLACES rows: `1,597`.
- Geometry-only rows: `23`.
- PLACES rows without geometry: `0`.
- Linkage disagreements: `0`.
- Geometry-only estimates converted to zero: `0`.

Each geometry-only tract remains in the exact table with map class `unavailable`, support state `unavailable`, and a blank estimate and interval. Gray on the map means unavailable. It does not mean zero prevalence, no residents, no diabetes, low need, or low priority.

## Coordinate systems and area

The source CRS is EPSG 4269. Geometry-area checks and display preparation use EPSG 26986. The map applies a topology-preserving 100-meter display simplification after projection. The source ZIP, geometry audit, keys, joined values, exact table, and areas remain unchanged.

All 32 SQL checks pass. The checks reconcile source rows, unique keys, state and county identity, geometry validity, coordinate systems, projected area, measure identity, intervals, join states, unavailable values, county summaries, classes, support states, and exact output counts.

## Decision

The geometry and exact key join are accepted for one bounded teaching map. This decision does not authorize a spatial point join, address inference, service-area claim, ranking, targeting, eligibility, outreach, funding, allocation, implementation, or deployment.

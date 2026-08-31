# APP-5 Module 04 data specification

## Source boundary

`data/raw/tl_2024_25_tract.zip` is the complete official 2024 TIGER/Line Massachusetts census tract archive. It is public boundary evidence from the U.S. Census Bureau. The archive supplies tract keys and geometry. It does not supply demographic values, clinical events, service access, community identity, priority, eligibility, or authority to act.

`data/source-manifest.csv` fingerprints the archive and every decompressed member. `acquire_geometry.py` verifies the exact URL, 4,506,627-byte archive, SHA-256 `74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4`, and seven expected members before accepting the source.

## Accepted evidence thread

`upstream/checkpoint-reference/` is the complete 240-file APP-5 Week 3 checkpoint reference workspace. Module 04 reads the accepted public PLACES table from `candidate/module-02/outputs/public-modeled-prevalence.csv` and its exact tract linkage audit. It does not recompute or repair checkpoint evidence.

The map measure is CDC PLACES 2023 modeled crude diabetes prevalence from the 2025 census-tract release. It is a modeled public estimate, not observed case data and not the fictional synthetic numerator used elsewhere in APP-5.

## Geometry contract

- Key: 11-character `GEOID`.
- State: FIPS `25` only.
- Rows: 1,620.
- Unique keys: 1,620.
- Counties: 14.
- Source CRS: EPSG 4269.
- Projected area-check CRS: EPSG 26986.
- Geometry types: Polygon or MultiPolygon only.
- Validity: no null, empty, or invalid geometry.
- Join: 1,597 measure matches and 23 geometry-only tracts.
- Unavailable state: a geometry-only tract remains unavailable and never becomes zero.

Projected geometry area is compared with the source `ALAND + AWATER` value. This check tests geometry and projection integrity. It does not replace the source area fields or redefine the tract.

The static teaching map projects the accepted geometry to EPSG 26986 and applies a 100-meter topology-preserving display simplification. This reduces the SVG file size without changing any source file, tract key, joined value, exact table, audit, or analytic result. The complete unsimplified geometry remains in the verified source archive.

## Map classes and support

The map uses declared absolute prevalence classes:

1. less than 5.0%;
2. 5.0% to less than 10.0%;
3. 10.0% to less than 15.0%;
4. 15.0% to less than 20.0%;
5. 20.0% or greater; and
6. unavailable.

The classes do not depend on ranks, quantiles, SVI ranks, or a targeting rule.

The classroom limited-support flag is triggered when the modeled confidence-interval width is at least 4.0 percentage points or the retained PLACES population field is below 500. The flag preserves the exact estimate and interval. It is an instructional review trigger, not a CDC quality designation, clinical threshold, suppression rule, or reason to exclude a tract.

## County teaching summaries

County summaries weight tract modeled prevalence by the retained PLACES population field. They are population-weighted summaries of tract estimates for the aggregation exercise. They are not official county PLACES estimates, observed county rates, service-area measures, causal results, or allocation inputs.

## Output boundary

The deterministic build writes geometry, join, tract, stability, county, aggregation, class, check, SVG, structured-text, and build-report outputs. The complete tract table is the exact nonvisual alternative to the map. No output ranks a tract or labels a place as high need, vulnerable, underserved, deficient, priority, eligible, or targeted.

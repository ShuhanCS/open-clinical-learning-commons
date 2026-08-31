# APP-5 Module 04 build plan

## Purpose

Build APP-5 Module 04, Place-based evidence and geographic reasoning. The module decides whether the accepted population evidence can be communicated geographically without a wrong join, unstable support, ecological inference, inaccessible output, or language that treats a place or its residents as the problem.

The module adds verified geography and one responsible teaching map. It does not rank tracts, define a priority area, target a population, set eligibility, direct outreach, allocate funding, fit a model, estimate an intervention effect, claim a real disparity, represent community agreement, implement, connect to production, or deploy.

## Release identity

- Module ID: `oclc-app5-04`.
- Module version: `0.1.0`.
- Commons release: `0.91.0`.
- Hours: 16.5.
- Course points: 10 toward the separate 25-point Week 6 checkpoint.
- Planned package: `courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/`.
- Planned specification: `docs/curriculum/courses/APP-5/modules/04-place-evidence-geographic-reasoning-spec.md`.
- Decision: can the accepted population evidence be communicated geographically within its source, support, accessibility, and claim limits?

## Accepted upstream handoff

The module builder must call the existing APP-5 Checkpoint 01 builder and request its complete reference workspace. The handoff freezes:

- checkpoint ID `oclc-app5-cp01`, version `0.1.0`, Commons `0.90.0`;
- 240 reference-workspace files;
- 219 candidate files from Modules 01 through 03;
- 177 nested immutable module rows;
- 40 of 40 checkpoint points;
- all 67 inherited and checkpoint gates;
- 1,620 union tracts and 1,597 linked measure tracts;
- the public CDC PLACES modeled diabetes prevalence table;
- the synthetic measure and disparity evidence, unavailable states, suppression, bias, and claim limits; and
- the `continue with conditions` decision that permits bounded Module 04 curriculum construction.

The freeze script fingerprints all 240 checkpoint files in a sorted outer manifest. Module 04 may read accepted evidence but may not repair, recompute, rescore, or reinterpret the checkpoint.

## Public geometry source

Use the complete official 2024 TIGER/Line Massachusetts census tract archive:

- Release page: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html
- State download interface: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?layergroup=Census+Tracts&year=2024
- Direct archive: https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_25_tract.zip
- Archive bytes: `4,506,627`.
- Archive SHA-256: `74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4`.
- Geometry rows: `1,620`.
- Unique tract GEOIDs: `1,620`.
- State FIPS: `25`.
- Counties: `14`.
- Source coordinate system: NAD83 geographic coordinates, EPSG `4269`.
- Geometry types: `1,617` Polygon and `3` MultiPolygon.
- Geometry validity: `1,620` valid, `0` empty, `0` null.

Commit the exact archive as immutable public source evidence. The acquisition script must verify the URL, byte count, SHA-256, ZIP inventory, expected basename, and refusal to overwrite. Geometry validation belongs to the analysis builder.

## Analytic and map contract

Python owns geometry reading, coordinate-system checks, projected area checks, map construction, SVG accessibility metadata, and deterministic output. SQLite owns exact key joins, county summaries, class comparisons, and tabular checks.

The release must:

1. retain all 1,620 geometry tracts;
2. join exactly 1,597 accepted PLACES rows by 11-character tract GEOID;
3. preserve the 23 geometry-only tracts as unavailable rather than zero;
4. reject duplicate, malformed, wrong-state, missing, extra, invalid, empty, or null geometry;
5. verify NAD83 EPSG 4269 and project to Massachusetts Mainland EPSG 26986 for area checks;
6. compare projected geometry area with `ALAND + AWATER` without changing source geometry;
7. keep the public PLACES modeled estimate, interval, population field, release label, and claim limit separate from synthetic evidence;
8. use declared absolute prevalence classes rather than quantile ranks;
9. flag limited small-area support with a predeclared classroom rule while retaining the exact interval and population field;
10. calculate population-weighted tract summaries by county and label them as teaching summaries, not official county PLACES estimates;
11. compare tract classes with county-summary classes to demonstrate aggregation sensitivity without calling either geography correct;
12. produce one deterministic Massachusetts tract SVG map, one complete exact CSV alternative, one structured text alternative, and one context memo; and
13. prohibit priority, need, vulnerability, risk, ranking, targeting, eligibility, outreach, funding, allocation, intervention, implementation, or deployment language.

The assessed map uses the accepted CDC PLACES 2023 modeled crude diabetes prevalence estimates from the 2025 tract release. It is a source-labeled teaching display, not an observed-case map, causal analysis, individual risk estimate, disparity finding, needs assessment, or action rule.

## Required outputs

The deterministic reference build should produce:

1. `source-profile.csv`;
2. `geometry-audit.csv`;
3. `geometry-join-audit.csv`;
4. `tract-map-table.csv`;
5. `small-area-stability.csv`;
6. `county-aggregation.csv`;
7. `aggregation-comparison.csv`;
8. `map-class-summary.csv`;
9. `query-checks.csv`;
10. `responsible-diabetes-prevalence-map.svg`;
11. `map-text-facts.json`; and
12. `build-report.json`.

Every row and output receives an exact schema, row count, byte count, SHA-256, and interpretation boundary in the release record.

## Learner and reference records

Build parallel learner and reference versions of three SQL files and these 12 records:

1. `geometry-source-review.md`;
2. `geography-join-and-crs-audit.md`;
3. `aggregation-and-stability-review.md`;
4. `ecological-contextual-claims-audit.csv`;
5. `responsible-map-specification.md`;
6. `responsible-map-text-alternative.md`;
7. `responsible-map-context-memo.md`;
8. `week6-component-score.csv`;
9. `gate-results.csv`;
10. `progression-decision.md`;
11. `reproducibility-check.md`; and
12. `ai-use.md`.

Learner records use explicit `REPLACE` prompts. Reference records contain exact accepted evidence and no placeholder.

## Assessment and gates

Score the module out of 10:

- source and geometry integrity: 2 points;
- exact join, aggregation, and stability accounting: 3 points;
- responsible accessible map and exact alternative: 3 points; and
- ecological, contextual, reproducibility, and claim-limit reasoning: 2 points.

The numeric passing threshold is 8 of 10. Any noncompensable gate failure overrides the score. Gates cover checkpoint identity, source fingerprint, ZIP inventory, row and key counts, state and county identity, coordinate systems, validity, join accounting, unavailable states, public and synthetic separation, interval and support retention, aggregation labels, no ranks, SVG accessibility, exact and text alternatives, ecological limits, non-stigmatizing language, AI disclosure, deterministic reproduction, and bounded progression.

The reference result should be 10 of 10 with all gates passing and disposition `continue with conditions`. Acceptance permits Module 05 curriculum construction only. It does not make any tract eligible, prioritized, targeted, contacted, funded, or selected.

## Workspace and validation design

Reuse the established applied-course module pattern and installed geospatial libraries. Do not add a custom geometry parser.

- The source acquirer uses the Python standard library.
- The analysis uses GeoPandas, Shapely, PyProj, Matplotlib, and SQLite through GeoPandas and the Python standard library.
- The upstream freezer calls the accepted checkpoint builder.
- The workspace builder refuses an existing target and assembles separate learner and reference workspaces.
- Learner and reference workspaces receive the same immutable source and checkpoint handoff.
- Independent source builds, map builds, and reference workspaces must match byte for byte.

The validator checks exact inventories, fingerprints, data schemas, geometry states, source identities, join accounting, summaries, map structure, accessibility metadata, points, gates, records, AI accountability, and authority. Its self-check must reject changed source bytes, a missing or duplicate tract, wrong CRS, invalid geometry status, changed PLACES estimate, a public and synthetic merge, a geometry-only tract changed to zero, rank or target language, inaccessible map output, incomplete alternatives, changed score, failed gate, copied reference answers, complete-mode learner workspaces, invalid progression, and deployment authority.

## Integration and release gates

Update the APP-5 course specification, course package README, root README, curriculum catalog wording where needed, build ledger, central curriculum checker, and root `VERSION`.

Release only after:

- source acquisition and fingerprint checks;
- checkpoint freeze self-check;
- deterministic analysis and map self-check;
- learner and reference workspace self-check;
- complete and starter validation;
- copied-validator execution;
- protected failure-route rejection;
- focused central curriculum contract;
- catalog integrity, plain-ASCII, personal-path, placeholder, and Git diff checks;
- semver checks;
- Git commit and push; and
- remote branch verification.

The next unit after acceptance is APP-5 Module 05, Targeting and fairness. Module 05 must begin from the frozen Module 04 handoff and may compare fictional transparent rules only. It may not treat the map as an automatic action rule.

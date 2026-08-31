# APP-5 Module 04 instructor notes

## Teaching purpose

This module teaches learners to distrust a polished map until they can defend its source, boundary vintage, key, coordinate system, geometry, join, support, aggregation, accessibility, language, and decision use.

The technical result is intentionally bounded. Learners produce one map, then spend as much time auditing what the map cannot support as they spend drawing it.

## Suggested 16.5-hour sequence

| Activity | Hours | Instructor focus |
|---|---:|---|
| Checkpoint handoff and decision framing | 1.0 | Freeze accepted evidence and restate the authority boundary |
| Official TIGER source acquisition and archive audit | 2.0 | Direct URL, hash, inventory, vintage, source role |
| Geometry, CRS, validity, and projected-area laboratory | 2.0 | EPSG 4269 versus 26986, geometry checks, display generalization |
| Exact tract-key join and unavailable-state laboratory | 2.5 | String keys, full geometry retention, no silent loss or zero fill |
| Small-area support and tract-versus-county aggregation | 2.0 | Interval width, population field, teaching summary, modifiable areal unit problem |
| Responsible map and accessibility studio | 3.0 | Fixed classes, source note, hatching, SVG title and description, exact alternative |
| Ecological claims clinic and context memo | 2.5 | Individual inference, place stigma, community rights, action limits |
| Reproduction, scoring, gates, and defense | 1.5 | Clean build, failure routes, decision, Module 05 handoff |
| Total | 16.5 | |

## Demonstration order

1. Show the direct Census archive URL and verify its fingerprint before opening a map.
2. Print geometry row, key, state, county, CRS, validity, and area-check results.
3. Join the accepted PLACES table and pause on the 23 geometry-only tracts.
4. Ask learners what gray should mean before revealing the unavailable state.
5. Compare a tract display with the county teaching summary and discuss why the question changes.
6. Add hatching and inspect the exact interval rather than calling a flagged estimate bad.
7. Read the map once visually and once from the exact table and text alternative.
8. Rewrite ecological and stigmatizing statements before accepting the map.

## Common errors and interventions

| Error | Instructor response |
|---|---|
| GEOID read as a number | Rebuild it as an 11-character string and rerun the full join audit |
| Geometry-only tract filled with zero | Restore unavailable and ask what evidence would support a numeric value |
| Latitude-longitude area calculation | Require the declared projected CRS and compare with `ALAND + AWATER` |
| Quantile map presented as neutral | Require declared breaks and explain how the data determine quantile membership |
| Darkest color called high need | Separate the modeled estimate from access, capacity, burden, benefit, harm, and community review |
| County summary called official | Rename it and document the population-weighted tract-summary method |
| Hatching called unreliable | Name the classroom rule and retain the exact estimate and interval |
| Map accepted without nonvisual route | Require SVG metadata, exact table, text alternative, and reading order |
| Community described as the problem | Rewrite the statement around data, conditions, missing evidence, accountable actors, and possible system responses |

## Review requirements before alpha

Named reviewers must cover population-health clinical practice, epidemiology, biostatistics, Census and TIGER geography, GIS, PLACES methodology, equity, community engagement, privacy, accessibility, responsible AI, and independent reproduction. Missing geographic, community, accessibility, or independent-reproduction coverage blocks alpha.

## Stop conditions

Stop and refer the release if a source or handoff fingerprint changes, a geometry or join gate fails, an unavailable value becomes zero, the map loses its exact alternative, the language infers individual or community need, an action rule appears, community input is fabricated, or a human reviewer cannot identify who owns the next decision and who can stop it.

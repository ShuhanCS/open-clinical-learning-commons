# Responsible map specification

## Purpose and reader

The map helps APP-5 learners inspect how one accepted public modeled measure appears across 2024 Massachusetts census tract geometry. The intended readers are learners, faculty, GIS reviewers, population-health clinicians, accessibility reviewers, and community reviewers evaluating the teaching release.

The map does not support outreach, case finding, care delivery, needs assessment, priority setting, eligibility, funding, or allocation.

## Data and geography

- Boundary source: 2024 TIGER/Line Massachusetts census tracts.
- Boundary vintage: legal boundaries and names as of January 1, 2024.
- Measure: CDC PLACES modeled crude adult diabetes prevalence.
- Measure year: 2023.
- Measure release: 2025 census-tract release.
- Joined tracts: 1,597.
- Unavailable geometry-only tracts: 23.
- Source CRS: EPSG 4269.
- Display CRS: EPSG 26986.
- Display-only simplification: topology preserving, 100 meters.

## Encoding

Five fixed absolute classes use a light-to-dark sequential blue scale. The breaks are below 5.0%, 5.0% to below 10.0%, 10.0% to below 15.0%, 15.0% to below 20.0%, and 20.0% or greater. Gray means unavailable. Hatching marks the 49 classroom limited-support review tracts.

The classes are not quantiles, ranks, clinical thresholds, quality levels, needs categories, or action groups. County boundaries appear only as orientation lines.

## Accessibility

The SVG has `role="img"`, an accessible title, a structured description, and `aria-labelledby="map-title map-desc"`. Meaning does not depend on color alone: unavailable has a named gray state, support review uses hatching, the legend includes counts, and the package includes a complete exact CSV table and a structured text alternative.

The source note names the measure year, release, modeled-estimate status, absolute classes, unavailable meaning, review-trigger meaning, and action limit. The text alternative supplies a nonvisual reading sequence.

## Claim boundary

The map may be described as a source-labeled display of modeled tract estimates. It cannot be described as observed cases, individual risk, a real disparity, community need, vulnerability, deficit, priority, eligibility, target, outreach list, funding rule, allocation rule, intervention effect, implementation evidence, or production result.

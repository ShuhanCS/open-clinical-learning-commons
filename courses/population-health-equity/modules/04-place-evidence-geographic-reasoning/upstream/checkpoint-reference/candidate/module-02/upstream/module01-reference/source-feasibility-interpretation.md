# Source feasibility interpretation

## Accepted release

The module releases 1,597 PLACES rows and 24 fields, 1,620 ACS rows and 100 fields, and 1,613 SVI rows and 158 fields. The field inventory has 282 rows. The three-source intersection is 1,597 tracts, and the union is 1,620 tracts.

The ACS acquisition verified the complete national B01001 table before extraction: 200,356,282 raw bytes, SHA-256 `1637b18a96881b81e050df1cd3d5ac38a33208b9b69b40e1dbeb3c4e13718f0e`, 616,690 rows, and 99 source fields.

## Join interpretation

Every PLACES diabetes tract has an ACS row and an SVI row. This supports later construction of a declared intersection without implying that the sources share a population, denominator, period, method, or meaning.

SVI contains 16 tracts without a PLACES diabetes row. ACS contains 23 tracts without a PLACES diabetes row and seven tract records without an SVI row. These rows remain visible. Their absence from another source is not a zero and is not evidence that residents, diabetes, or social conditions are absent.

## Source roles

PLACES supplies modeled adult diabetes prevalence and published 95% limits. It does not supply observed diagnoses or local intervention effects. ACS supplies 2020-2024 age-by-sex population estimates and margins. It does not supply diabetes events. SVI supplies 2022 area context and relative ranks. It does not supply individual traits, a longitudinal vulnerability score, causation, or allocation authority.

The different periods remain part of every interpretation. Joining by tract FIPS is technically feasible, but analytic compatibility still requires a declared measure, population, denominator, period, and claim.

## Decision consequence

The public release is feasible for Module 02 curriculum construction with conditions. It is not sufficient to identify a tract for funding or outreach. Rate formulas, age bands, standard population, synthetic numerator design, margin handling, disparity measures, suppression, geometry, local evidence, capacity, and community review remain unresolved.

No public source can establish that a community needs, wants, can access, or would benefit from the fictional intervention. Structured community review is a future required decision step, not an inference from a score.

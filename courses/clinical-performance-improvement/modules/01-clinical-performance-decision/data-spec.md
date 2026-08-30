# APP-3 Module 01 data specification

## Evidence layers

The module keeps three evidence layers separate:

1. Public CMS hospital aggregates define quality, timeliness, and safety measure families.
2. Historical HHS facility-week aggregates show how capacity, occupancy, coverage, and demand fields are represented.
3. The fictional `CGH-ED-01` event model is only declared here. Synthetic encounter and operational rows begin in Module 02.

No public facility is the fictional service. Facility names and identifiers in public files must never be copied into synthetic operational records.

## Complete accepted sources

| Source | Rows | Columns | Raw bytes | Raw SHA-256 | Repository treatment |
|---|---:|---:|---:|---|---|
| CMS Timely and Effective Care | 138,084 | 16 | 34,150,899 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` | complete deterministic gzip |
| CMS Complications and Deaths | 95,800 | 18 | 22,963,267 | `26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d` | complete deterministic gzip |
| HHS facility capacity | 1,045,406 | 128 | 481,497,539 | `b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f` | full snapshot fingerprint plus all-row Massachusetts extract |

The HHS repository extract retains all 15,179 Massachusetts facility-week rows, including inconvenient sentinel and unavailable values, and 24 fields needed to teach source feasibility. `profile_sources.py` can reproduce it only after validating the complete 481,497,539-byte national source.

## Immutable outputs

- `data/source-inventory.csv`: one row per accepted public source and one declaration row for the fictional service.
- `data/measure-family-anchors.csv`: exact support and availability facts for three timely-care measures, three safety measures, and four capacity concepts.
- `data/capacity-source-profile.csv`: complete-source and Massachusetts-extract facts.
- `data/raw/Timely_and_Effective_Care-Hospital.csv.gz`: complete CMS timely-care snapshot.
- `data/raw/Complications_and_Deaths-Hospital.csv.gz`: complete CMS complications snapshot.
- `data/raw/HHS-Capacity-Massachusetts.csv.gz`: deterministic state extract derived only after complete-source validation.

## Editable records

| Record | Grain | Required purpose |
|---|---|---|
| `clinical-performance-charter.md` | one module decision | bind problem, owner, unit, evidence, action, and claim boundary |
| `synthetic-service-declaration.md` | one fictional service | prohibit public-to-synthetic attribution |
| `unit-of-flow.csv` | one event state per row | define how an encounter moves through the service |
| `process-boundary.csv` | one included or excluded boundary per row | prevent scope drift |
| `measure-family.csv` | one measure family per row | map concept, role, grain, denominator, and future owner |
| `source-feasibility-interpretation.md` | one interpretation | explain every immutable source fact and consequence |
| `stakeholder-accountability-map.csv` | one role per row | assign decision rights and review duties |
| `claim-boundary.csv` | one proposed claim per row | mark allowed, conditional, or prohibited use |
| `ai-use.md` | one disclosure | record assistance and human verification |
| `progression-decision.md` | one readiness decision | control entry to Module 02 |

## Missingness and unavailable values

Blank, `Not Available`, `N/A`, `-999999`, footnotes, and coverage fields remain evidence. They may be classified, counted, and explained but not silently converted into observed performance. Module 01 calculates no facility ranking, local rate, forecast, control limit, intervention effect, or staffing requirement.

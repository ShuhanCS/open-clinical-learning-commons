# Data brief

## Source and rights

The toolkit uses the public Synthea April 2020 CSV sample from https://synthea.mitre.org/downloads. The 8,982,431-byte archive SHA-256 is `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`. The source is synthetic and contains no real patient records. The source ZIP and generated SQLite database are verified but not distributed in this toolkit.

## Relational system and analytic grain

The source has 16 CSV tables, 168 fields, and 471,836 rows. Module 02 builds a 177-field SQLite dictionary and relational database. Module 03 selects 1,048 eligible adult acute events and one deterministic index for 374 synthetic adults. The accepted analytic table has 374 rows and 29 fields, with one unique patient and one unique index encounter per row. Its SHA-256 is `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.

## Time and follow-up

Time zero is the selected index encounter. History uses the declared pre-index window. Follow-up begins after index stop. The 30-day next-state rows are 263 no encounter recorded, 92 scheduled care, 4 urgent care, and 15 acute return. Ninety-day flags include 36 acute returns and 8 synthetic deaths. No recorded next encounter is not proof of no care.

## Quality and retained conditions

Module 04 created a separate 379-row teaching defect layer with D01 through D20, 56 issue cases, and 68 manifest changes. All 28 registered rules pass. D01 through D20 are resolved, and the restored table is byte-identical to the accepted table. N01 through N08 remain explicit conditions for structural missingness, extremes, high counts, and small supported results.

## Descriptive evidence

The release has 17 profiles, 12 cross-tab cells, six rates, two unadjusted strata, 27 denominator records, and 18 passing checks. The six rate numerators are 111, 92, 4, 15, 36, and 8, each over 374. Wilson intervals are descriptive arithmetic for the fixed synthetic cohort, not significance tests or real-population estimates.

## Figures and equivalent access

F01 compares accepted and deliberately defective missingness. F02 shows six exact rates and intervals. F03 shows 374 selected indexes across 20 quarters, including 314 emergency and 60 inpatient. Each has PNG, SVG, exact CSV, registry mapping, and structured text. Non-color cues, grayscale, 50-percent width, 200-percent zoom, reading order, and table equivalence are recorded.

## Permitted and prohibited use

Permitted use is public technical education and downstream method development on synthetic data under the retained release conditions. The toolkit supports no real clinical, operational, performance, safety, access, equity, utilization, cost, population, trend, forecast, process-control, effect, or causal conclusion. It is not a production data product or clinical approval.

## Reproduction and version

The copied requirements, database builder, schema, query runner, cohort SQL and builder, quality builders, descriptive builder, and figure renderer identify the accepted pipeline. Reproduction begins from the pinned archive, uses explicit new targets, and compares outputs by bytes and SHA-256. Toolkit candidate version is 0.1.0; the accepted tag is `fnd1-handoff-v0.1.0`.

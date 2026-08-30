# Handoff questions and responses

1. One row in the analytic table represents one selected synthetic person and one unique index encounter. Other tables declare their own grain in the data dictionary, headers, or denominator registry.
2. `source-code/module03/sql/02-index-cohort.sql` selects the deterministic index after adult eligibility. The source flow is 1,171 patients: 690 without an acute event, 107 with only under-18 acute events, and 374 included adults.
3. RT01 through RT06 have numerators 111, 92, 4, 15, 36, and 8, each over 374. Definitions and windows remain in `evidence-tables/rates.csv` and the denominator registry.
4. Duplicate person rows most directly threaten downstream use because they change grain, counts, and rates. D01 detects five seeded duplicate rows and the restored release returns to one row per person.
5. D01 through D20 were corrected in the separate teaching layer and verified against the accepted fingerprint. N01 through N08 were retained and remain visible in quality, descriptive, figure, limitations, and review records.
6. Synthea supports realistic pipeline education without patient records. Its generated synthetic values and selected cohort cannot estimate real care, quality, safety, population, or outcome conditions.
7. Another analyst verifies the source archive, installs exact requirements, runs the copied module builders and SQL in order with new targets, compares every accepted output by bytes and SHA-256, and runs complete toolkit validation.
8. AI helped draft contracts, wording, tests, and documentation. The material structural-missingness claim was checked independently against 374 rows, N03, VP14, and the denominator record. Humans own the final decision.
9. Permitted use is public technical education and downstream method development on synthetic data under the retained conditions. Production and real clinical use are not authorized.
10. A changed immutable file, source or denominator ambiguity, hidden dependency, restricted data, broken access route, incomplete AI audit, unsupported real-world claim, or failed defense stops or revises the release.

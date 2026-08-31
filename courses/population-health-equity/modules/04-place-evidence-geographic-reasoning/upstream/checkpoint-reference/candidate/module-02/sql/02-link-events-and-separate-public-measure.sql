DROP TABLE IF EXISTS linked_synthetic_events;
CREATE TABLE linked_synthetic_events AS
SELECT
    e.synthetic_event_id,
    e.case_id,
    e.tract_fips,
    e.age_band_id,
    e.age_band,
    d.band_order,
    e.period,
    d.denominator_estimate,
    d.denominator_moe90,
    CAST(e.acs_denominator_estimate AS INTEGER) AS generator_denominator_estimate,
    CAST(e.synthetic_event_count AS INTEGER) AS synthetic_event_count,
    CAST(e.generated_probability AS REAL) AS generated_probability,
    CAST(e.fictional_tract_effect AS REAL) AS fictional_tract_effect,
    e.generator_version,
    CAST(e.seed AS INTEGER) AS seed,
    CAST(e.synthetic_flag AS INTEGER) AS synthetic_flag,
    e.numerator_definition,
    e.claim_limit,
    CASE WHEN d.denominator_estimate = CAST(e.acs_denominator_estimate AS INTEGER) THEN 1 ELSE 0 END AS denominator_match
FROM raw_synthetic_events e
JOIN adult_age_denominators d
  ON d.tract_fips = e.tract_fips
 AND d.age_band_id = e.age_band_id
ORDER BY e.tract_fips, d.band_order;

DROP TABLE IF EXISTS public_modeled_prevalence;
CREATE TABLE public_modeled_prevalence AS
SELECT
    locationid AS tract_fips,
    countyfips AS county_fips,
    countyname AS county_name,
    year AS measure_year,
    measureid AS measure_id,
    datavaluetypeid AS data_value_type_id,
    CAST(data_value AS REAL) AS modeled_crude_prevalence_percent,
    CAST(low_confidence_limit AS REAL) AS modeled_low_confidence_limit,
    CAST(high_confidence_limit AS REAL) AS modeled_high_confidence_limit,
    CAST(totalpop18plus AS INTEGER) AS places_adult_population_field,
    'CDC PLACES 2025 census-tract release' AS source_release,
    'modeled small-area prevalence' AS estimate_type,
    'separate public evidence; not observed cases and not the synthetic numerator' AS claim_limit
FROM raw_places
ORDER BY locationid;

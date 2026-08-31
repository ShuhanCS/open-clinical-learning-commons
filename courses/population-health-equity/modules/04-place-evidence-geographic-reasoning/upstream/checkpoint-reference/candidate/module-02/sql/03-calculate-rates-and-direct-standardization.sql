DROP TABLE IF EXISTS standard_population;
CREATE TABLE standard_population AS
WITH totals AS (
    SELECT
        d.age_band_id,
        d.age_band,
        d.band_order,
        SUM(d.denominator_estimate) AS standard_population,
        SUM(e.synthetic_event_count) AS statewide_synthetic_events
    FROM adult_age_denominators d
    JOIN linked_synthetic_events e
      ON e.tract_fips = d.tract_fips
     AND e.age_band_id = d.age_band_id
    GROUP BY d.age_band_id, d.age_band, d.band_order
), overall AS (
    SELECT SUM(standard_population) AS adult_standard_population FROM totals
)
SELECT
    t.age_band_id,
    t.age_band,
    t.band_order,
    t.standard_population,
    ROUND(1.0 * t.standard_population / o.adult_standard_population, 10) AS standard_weight,
    t.statewide_synthetic_events,
    ROUND(100000.0 * t.statewide_synthetic_events / t.standard_population, 8) AS statewide_synthetic_rate_per_100k,
    'ACS 2020-2024 B01001 adult population across all 1,597 matched tracts' AS standard_source,
    'synthetic 2024 event period' AS event_period,
    'one common teaching standard; not a real risk or allocation standard' AS claim_limit
FROM totals t
CROSS JOIN overall o
ORDER BY t.band_order;

DROP TABLE IF EXISTS age_specific_rates;
CREATE TABLE age_specific_rates AS
SELECT
    e.tract_fips,
    e.age_band_id,
    e.age_band,
    e.band_order,
    e.period,
    e.synthetic_event_count,
    e.denominator_estimate,
    e.denominator_moe90,
    100000 AS rate_multiplier,
    CASE WHEN e.denominator_estimate > 0 THEN ROUND(100000.0 * e.synthetic_event_count / e.denominator_estimate, 8) END AS age_specific_rate_per_100k,
    CASE WHEN e.denominator_estimate > 0 THEN ROUND(WILSON_LOW(e.synthetic_event_count, e.denominator_estimate, 100000.0), 8) END AS rate_low_95,
    CASE WHEN e.denominator_estimate > 0 THEN ROUND(WILSON_HIGH(e.synthetic_event_count, e.denominator_estimate, 100000.0), 8) END AS rate_high_95,
    CASE WHEN e.denominator_estimate = 0 THEN 'unavailable_zero_denominator' ELSE 'available' END AS availability_state,
    CASE
        WHEN e.denominator_estimate = 0 THEN 'unavailable'
        WHEN e.denominator_estimate < 50 THEN 'review_small_denominator'
        ELSE 'supported_for_module02_calculation'
    END AS support_state,
    'synthetic planning-need event divided by ACS age-band estimate' AS measure_definition,
    'teaching rate only; not a diagnosis, observed local rate, eligibility result, or allocation signal' AS claim_limit
FROM linked_synthetic_events e
ORDER BY e.tract_fips, e.band_order;

DROP TABLE IF EXISTS tract_rate_summary;
CREATE TABLE tract_rate_summary AS
WITH joined AS (
    SELECT
        r.*,
        s.standard_weight,
        CASE WHEN r.denominator_estimate > 0
             THEN s.standard_weight * (1.0 * r.synthetic_event_count / r.denominator_estimate)
        END AS weighted_proportion,
        CASE WHEN r.denominator_estimate > 0
             THEN s.standard_weight * s.standard_weight
                * (1.0 * r.synthetic_event_count / r.denominator_estimate)
                * (1.0 - 1.0 * r.synthetic_event_count / r.denominator_estimate)
                / r.denominator_estimate
        END AS weighted_variance
    FROM age_specific_rates r
    JOIN standard_population s ON s.age_band_id = r.age_band_id
), summarized AS (
    SELECT
        tract_fips,
        SUM(synthetic_event_count) AS synthetic_event_count,
        SUM(denominator_estimate) AS adult_denominator_estimate,
        ROUND(SQRT(SUM(denominator_moe90 * denominator_moe90)), 3) AS adult_denominator_moe90,
        SUM(CASE WHEN denominator_estimate > 0 THEN 1 ELSE 0 END) AS positive_denominator_age_bands,
        MIN(denominator_estimate) AS minimum_age_band_denominator,
        SUM(CASE WHEN denominator_estimate = 0 THEN 1 ELSE 0 END) AS zero_denominator_age_bands,
        SUM(weighted_proportion) AS direct_proportion,
        SUM(weighted_variance) AS direct_variance
    FROM joined
    GROUP BY tract_fips
)
SELECT
    tract_fips,
    synthetic_event_count,
    adult_denominator_estimate,
    adult_denominator_moe90,
    100000 AS rate_multiplier,
    ROUND(100000.0 * synthetic_event_count / adult_denominator_estimate, 8) AS crude_rate_per_100k,
    ROUND(WILSON_LOW(synthetic_event_count, adult_denominator_estimate, 100000.0), 8) AS crude_rate_low_95,
    ROUND(WILSON_HIGH(synthetic_event_count, adult_denominator_estimate, 100000.0), 8) AS crude_rate_high_95,
    positive_denominator_age_bands,
    minimum_age_band_denominator,
    CASE WHEN zero_denominator_age_bands = 0 THEN ROUND(100000.0 * direct_proportion, 8) END AS direct_standardized_rate_per_100k,
    CASE WHEN zero_denominator_age_bands = 0 THEN ROUND(MAX(0.0, 100000.0 * direct_proportion - 1.96 * 100000.0 * SQRT(direct_variance)), 8) END AS direct_rate_low_95,
    CASE WHEN zero_denominator_age_bands = 0 THEN ROUND(MIN(100000.0, 100000.0 * direct_proportion + 1.96 * 100000.0 * SQRT(direct_variance)), 8) END AS direct_rate_high_95,
    CASE
        WHEN zero_denominator_age_bands > 0 THEN 'direct_unavailable_zero_denominator'
        WHEN minimum_age_band_denominator < 50 THEN 'review_small_age_denominator'
        ELSE 'complete_for_module02'
    END AS direct_support_state,
    CASE WHEN minimum_age_band_denominator < 50 THEN 'yes' ELSE 'no' END AS guided_indirect_required,
    'direct rate is a relative teaching index under one common standard age distribution' AS claim_limit
FROM summarized
ORDER BY tract_fips;

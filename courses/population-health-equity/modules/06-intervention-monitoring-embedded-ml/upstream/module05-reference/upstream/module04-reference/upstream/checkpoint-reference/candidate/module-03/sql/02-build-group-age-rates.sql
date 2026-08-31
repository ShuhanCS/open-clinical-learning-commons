DROP TABLE IF EXISTS group_age_rates;
CREATE TABLE group_age_rates AS
WITH reported AS (
    SELECT
        m.equity_dimension,
        m.dimension_label,
        m.group_id,
        m.group_label,
        m.group_order,
        c.missing_group,
        c.primary_reference,
        m.age_band_id,
        m.age_band,
        m.band_order,
        SUM(m.population_count) AS population_count,
        SUM(m.synthetic_event_count) AS synthetic_event_count
    FROM equity_margins AS m
    JOIN group_contract AS c
      ON c.equity_dimension = m.equity_dimension
     AND c.group_id = m.group_id
    GROUP BY m.equity_dimension, m.dimension_label, m.group_id, m.group_label,
             m.group_order, c.missing_group, c.primary_reference,
             m.age_band_id, m.age_band, m.band_order
), overall_reported AS (
    SELECT
        m.equity_dimension,
        m.dimension_label,
        'overall_reported' AS group_id,
        'Overall reported population' AS group_label,
        999 AS group_order,
        0 AS missing_group,
        0 AS primary_reference,
        m.age_band_id,
        m.age_band,
        m.band_order,
        SUM(m.population_count) AS population_count,
        SUM(m.synthetic_event_count) AS synthetic_event_count
    FROM equity_margins AS m
    JOIN group_contract AS c
      ON c.equity_dimension = m.equity_dimension
     AND c.group_id = m.group_id
    WHERE c.missing_group = 0
    GROUP BY m.equity_dimension, m.dimension_label, m.age_band_id, m.age_band, m.band_order
), combined AS (
    SELECT * FROM reported
    UNION ALL
    SELECT * FROM overall_reported
)
SELECT
    equity_dimension,
    dimension_label,
    group_id,
    group_label,
    group_order,
    missing_group,
    primary_reference,
    age_band_id,
    age_band,
    band_order,
    population_count,
    synthetic_event_count,
    100000 AS rate_multiplier,
    CASE WHEN population_count > 0 THEN 100000.0 * synthetic_event_count / population_count END AS age_specific_rate_per_100k,
    CASE WHEN population_count > 0 THEN WILSON_LOW(synthetic_event_count, population_count, 100000.0) END AS rate_low_95,
    CASE WHEN population_count > 0 THEN WILSON_HIGH(synthetic_event_count, population_count, 100000.0) END AS rate_high_95,
    CASE WHEN population_count > 0 THEN 'available' ELSE 'unavailable_zero_denominator' END AS availability_state,
    'synthetic marginal rate; not an observed group rate, biological comparison, eligibility result, or allocation signal' AS claim_limit
FROM combined
ORDER BY equity_dimension, group_order, band_order;

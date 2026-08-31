DROP TABLE IF EXISTS standardized_group_rates;
CREATE TABLE standardized_group_rates AS
WITH calculated AS (
    SELECT
        g.equity_dimension,
        g.dimension_label,
        g.group_id,
        g.group_label,
        g.group_order,
        g.missing_group,
        g.primary_reference,
        SUM(g.population_count) AS population_count,
        SUM(g.synthetic_event_count) AS synthetic_event_count,
        COUNT(*) AS age_bands,
        SUM(CASE WHEN g.population_count > 0 THEN 1 ELSE 0 END) AS positive_age_bands,
        SUM(CAST(s.standard_weight AS REAL) * g.age_specific_rate_per_100k) AS direct_standardized_rate_per_100k,
        SUM(
            CAST(s.standard_weight AS REAL) * CAST(s.standard_weight AS REAL)
            * (1.0 * g.synthetic_event_count / g.population_count)
            * (1.0 - 1.0 * g.synthetic_event_count / g.population_count)
            / g.population_count * 100000.0 * 100000.0
        ) AS direct_variance
    FROM group_age_rates AS g
    JOIN raw_standard_population AS s USING (age_band_id)
    GROUP BY g.equity_dimension, g.dimension_label, g.group_id, g.group_label,
             g.group_order, g.missing_group, g.primary_reference
)
SELECT
    equity_dimension,
    dimension_label,
    group_id,
    group_label,
    group_order,
    missing_group,
    primary_reference,
    population_count,
    synthetic_event_count,
    age_bands,
    positive_age_bands,
    direct_standardized_rate_per_100k,
    MAX(0.0, direct_standardized_rate_per_100k - 1.959963984540054 * SQRT(direct_variance)) AS direct_rate_low_95,
    direct_standardized_rate_per_100k + 1.959963984540054 * SQRT(direct_variance) AS direct_rate_high_95,
    CASE
        WHEN group_id = 'overall_reported' THEN 'overall_reported_reference'
        WHEN missing_group = 1 THEN 'missingness_audit_only'
        WHEN synthetic_event_count < 16 THEN 'unavailable_small_event_count'
        WHEN positive_age_bands < 5 THEN 'unavailable_age_support'
        ELSE 'supported_for_synthetic_comparison'
    END AS support_state,
    'direct standardization uses the accepted five-band Module 02 teaching population; synthetic comparison only' AS claim_limit
FROM calculated
ORDER BY equity_dimension, group_order;

DROP TABLE IF EXISTS disparity_comparisons;
CREATE TABLE disparity_comparisons AS
WITH primary_refs AS (
    SELECT
        g.equity_dimension,
        'predeclared_group' AS reference_choice,
        g.group_id AS reference_group_id,
        g.group_label AS reference_group_label,
        g.direct_standardized_rate_per_100k AS reference_rate,
        g.direct_rate_low_95 AS reference_low,
        g.direct_rate_high_95 AS reference_high,
        'predeclared large reported group; not a claim that the group is a norm or ideal' AS reference_rationale
    FROM standardized_group_rates AS g
    WHERE g.primary_reference = 1
), overall_refs AS (
    SELECT
        g.equity_dimension,
        'overall_reported' AS reference_choice,
        g.group_id AS reference_group_id,
        g.group_label AS reference_group_label,
        g.direct_standardized_rate_per_100k AS reference_rate,
        g.direct_rate_low_95 AS reference_low,
        g.direct_rate_high_95 AS reference_high,
        'all reported synthetic groups combined; missing group excluded' AS reference_rationale
    FROM standardized_group_rates AS g
    WHERE g.group_id = 'overall_reported'
), refs AS (
    SELECT * FROM primary_refs
    UNION ALL
    SELECT * FROM overall_refs
)
SELECT
    g.equity_dimension,
    g.dimension_label,
    g.group_id,
    g.group_label,
    r.reference_choice,
    r.reference_group_id,
    r.reference_group_label,
    g.direct_standardized_rate_per_100k AS group_rate_per_100k,
    r.reference_rate AS reference_rate_per_100k,
    g.direct_standardized_rate_per_100k - r.reference_rate AS rate_difference_per_100k,
    CASE WHEN r.reference_rate > 0 THEN g.direct_standardized_rate_per_100k / r.reference_rate END AS rate_ratio,
    g.direct_rate_low_95 - r.reference_high AS rate_difference_low_95,
    g.direct_rate_high_95 - r.reference_low AS rate_difference_high_95,
    CASE WHEN r.reference_high > 0 THEN g.direct_rate_low_95 / r.reference_high END AS rate_ratio_low_95,
    CASE WHEN r.reference_low > 0 THEN g.direct_rate_high_95 / r.reference_low END AS rate_ratio_high_95,
    r.reference_rationale,
    CASE WHEN g.support_state = 'supported_for_synthetic_comparison' THEN 'supported' ELSE 'unavailable' END AS comparison_state,
    'absolute and relative synthetic disparity measures can change direction or magnitude with the reference choice' AS interpretation_limit
FROM standardized_group_rates AS g
JOIN refs AS r USING (equity_dimension)
WHERE g.group_id <> 'overall_reported'
  AND g.missing_group = 0
ORDER BY g.equity_dimension, r.reference_choice, g.group_order;

DROP TABLE IF EXISTS summary_disparities;
CREATE TABLE summary_disparities AS
SELECT
    equity_dimension,
    dimension_label,
    reference_choice,
    reference_group_id,
    reference_group_label,
    COUNT(*) AS comparison_groups,
    AVG(ABS(rate_difference_per_100k)) AS summary_absolute_rate_difference_per_100k,
    AVG(CASE WHEN rate_ratio >= 1.0 THEN rate_ratio ELSE 1.0 / rate_ratio END) AS summary_rate_ratio,
    MAX(group_rate_per_100k) - MIN(group_rate_per_100k) AS maximal_rate_difference_per_100k,
    MAX(group_rate_per_100k) / MIN(group_rate_per_100k) AS maximal_rate_ratio,
    'unweighted teaching summary across supported reported groups; inspect pairwise results and group support before interpretation' AS interpretation_limit
FROM disparity_comparisons
WHERE comparison_state = 'supported'
  AND NOT (reference_choice = 'predeclared_group' AND group_id = reference_group_id)
GROUP BY equity_dimension, dimension_label, reference_choice, reference_group_id, reference_group_label
ORDER BY equity_dimension, reference_choice;

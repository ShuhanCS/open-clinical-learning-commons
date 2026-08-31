DROP TABLE IF EXISTS missingness_audit;
CREATE TABLE missingness_audit AS
WITH unpivoted AS (
    SELECT 'race' AS field_id, SUM(synthetic_event_count) AS eligible_records, SUM(race_missing_count) AS missing_records FROM field_completeness
    UNION ALL SELECT 'ethnicity', SUM(synthetic_event_count), SUM(ethnicity_missing_count) FROM field_completeness
    UNION ALL SELECT 'primary_language', SUM(synthetic_event_count), SUM(primary_language_missing_count) FROM field_completeness
    UNION ALL SELECT 'disability_status', SUM(synthetic_event_count), SUM(disability_status_missing_count) FROM field_completeness
    UNION ALL SELECT 'tract_geography', SUM(synthetic_event_count), SUM(tract_geography_missing_count) FROM field_completeness
)
SELECT
    field_id,
    eligible_records,
    missing_records,
    100.0 * missing_records / eligible_records AS missing_percent,
    CASE WHEN field_id = 'tract_geography' THEN 'conditioned_on_linked_analytic_universe' ELSE 'generated_missingness_present' END AS capture_state,
    CASE WHEN field_id = 'tract_geography' THEN 'zero missingness follows the accepted tract-linked input and does not measure records excluded before linkage' ELSE 'generated field completeness describes the synthetic event layer only' END AS interpretation_limit
FROM unpivoted
ORDER BY CASE field_id WHEN 'race' THEN 1 WHEN 'ethnicity' THEN 2 WHEN 'primary_language' THEN 3 WHEN 'disability_status' THEN 4 ELSE 5 END;

DROP TABLE IF EXISTS representation_audit;
CREATE TABLE representation_audit AS
SELECT
    g.equity_dimension,
    g.dimension_label,
    g.group_id,
    g.group_label,
    g.missing_group,
    g.population_count,
    g.synthetic_event_count,
    1.0 * g.population_count / SUM(g.population_count) OVER (PARTITION BY g.equity_dimension) AS population_share,
    1.0 * g.synthetic_event_count / SUM(g.synthetic_event_count) OVER (PARTITION BY g.equity_dimension) AS event_share,
    g.support_state,
    CASE WHEN g.missing_group = 1 THEN 'missing_group_retained_for_audit' ELSE 'reported_group_retained_without_merging' END AS representation_state,
    'separate synthetic margins cannot support intersectional or person-level representation claims' AS interpretation_limit
FROM standardized_group_rates AS g
WHERE g.group_id <> 'overall_reported'
ORDER BY g.equity_dimension, g.group_order;

DROP TABLE IF EXISTS tract_group_base;
CREATE TABLE tract_group_base AS
SELECT
    m.tract_fips,
    m.equity_dimension,
    m.dimension_label,
    m.group_id,
    m.group_label,
    m.group_order,
    c.missing_group,
    SUM(m.population_count) AS population_count,
    SUM(m.synthetic_event_count) AS synthetic_event_count
FROM equity_margins AS m
JOIN group_contract AS c
  ON c.equity_dimension = m.equity_dimension
 AND c.group_id = m.group_id
GROUP BY m.tract_fips, m.equity_dimension, m.dimension_label, m.group_id,
         m.group_label, m.group_order, c.missing_group;

DROP TABLE IF EXISTS tract_group_suppression;
CREATE TABLE tract_group_suppression AS
WITH primary_state AS (
    SELECT
        *,
        CASE WHEN synthetic_event_count < 16 OR population_count < 100 THEN 1 ELSE 0 END AS primary_suppressed
    FROM tract_group_base
), ranked AS (
    SELECT
        *,
        SUM(primary_suppressed) OVER (PARTITION BY tract_fips, equity_dimension) AS primary_suppressed_cells,
        ROW_NUMBER() OVER (
            PARTITION BY tract_fips, equity_dimension
            ORDER BY CASE WHEN primary_suppressed = 0 THEN 0 ELSE 1 END,
                     synthetic_event_count, population_count, group_order
        ) AS complementary_rank
    FROM primary_state
)
SELECT
    *,
    CASE WHEN primary_suppressed = 0 AND primary_suppressed_cells = 1 AND complementary_rank = 1 THEN 1 ELSE 0 END AS complementary_suppressed
FROM ranked;

DROP TABLE IF EXISTS published_tract_group_rates;
CREATE TABLE published_tract_group_rates AS
SELECT
    tract_fips,
    equity_dimension,
    dimension_label,
    group_id,
    group_label,
    missing_group,
    CASE
        WHEN primary_suppressed = 1 THEN 'primary_suppressed'
        WHEN complementary_suppressed = 1 THEN 'complementary_suppressed'
        ELSE 'publishable'
    END AS support_state,
    CASE
        WHEN primary_suppressed = 1 AND synthetic_event_count < 16 AND population_count < 100 THEN 'event_count_below_16_and_denominator_below_100'
        WHEN primary_suppressed = 1 AND synthetic_event_count < 16 THEN 'event_count_below_16'
        WHEN primary_suppressed = 1 THEN 'denominator_below_100'
        WHEN complementary_suppressed = 1 THEN 'complementary_nonreconstruction_protection'
        ELSE ''
    END AS suppression_reason,
    CASE WHEN primary_suppressed = 0 AND complementary_suppressed = 0 THEN population_count END AS published_population_count,
    CASE WHEN primary_suppressed = 0 AND complementary_suppressed = 0 THEN synthetic_event_count END AS published_synthetic_event_count,
    CASE WHEN primary_suppressed = 0 AND complementary_suppressed = 0 THEN 100000.0 * synthetic_event_count / population_count END AS published_crude_rate_per_100k,
    CASE WHEN primary_suppressed = 0 AND complementary_suppressed = 0 THEN WILSON_LOW(synthetic_event_count, population_count, 100000.0) END AS published_rate_low_95,
    CASE WHEN primary_suppressed = 0 AND complementary_suppressed = 0 THEN WILSON_HIGH(synthetic_event_count, population_count, 100000.0) END AS published_rate_high_95,
    'suppressed values are unavailable, not zero; no tract total is published in this table' AS publication_limit
FROM tract_group_suppression
ORDER BY tract_fips, equity_dimension, group_order;

DROP TABLE IF EXISTS complementary_suppression_audit;
CREATE TABLE complementary_suppression_audit AS
SELECT
    tract_fips,
    equity_dimension,
    COUNT(*) AS group_rows,
    SUM(primary_suppressed) AS primary_suppressed_cells,
    SUM(complementary_suppressed) AS complementary_suppressed_cells,
    SUM(primary_suppressed + complementary_suppressed) AS total_suppressed_cells,
    CASE
        WHEN SUM(primary_suppressed) = 0 AND SUM(complementary_suppressed) = 0 THEN 'pass'
        WHEN SUM(primary_suppressed) = 1 AND SUM(complementary_suppressed) = 1 THEN 'pass'
        WHEN SUM(primary_suppressed) >= 2 AND SUM(complementary_suppressed) = 0 THEN 'pass'
        ELSE 'fail'
    END AS status,
    'at least two cells are withheld when exactly one primary cell would otherwise be recoverable' AS rule
FROM tract_group_suppression
GROUP BY tract_fips, equity_dimension
ORDER BY tract_fips, equity_dimension;

DROP TABLE IF EXISTS bias_register;
CREATE TABLE bias_register (
    bias_id TEXT, bias_family TEXT, mechanism TEXT, evidence_in_release TEXT,
    likely_direction TEXT, mitigation_or_limit TEXT, owner TEXT, status TEXT
);
INSERT INTO bias_register VALUES
('B01', 'selection', 'analytic universe requires an accepted tract link', 'tract geography missingness is zero by construction', 'unknown; excluded records are not observed', 'state the conditioned universe and do not claim complete capture', 'data steward', 'open'),
('B02', 'selection', 'synthetic planning-need events are generated from accepted denominators', 'fixed generator probabilities and tract effects', 'set by generator rather than observed need', 'limit every result to the fictional teaching release', 'population-health clinical reviewer', 'open'),
('B03', 'linkage', 'only the 1,597 three-source intersection enters group analysis', '23 ACS-only union tracts remain outside the measure intersection', 'may change area coverage', 'retain the full 1,620-tract union audit and exclusions', 'data steward', 'open'),
('B04', 'measurement', 'combined race and ethnicity groups are generated marginal categories', 'separate group contract and synthetic flag', 'cannot represent self-identification or within-group diversity', 'no biological, person-level, or real demographic interpretation', 'race and ethnicity standards reviewer', 'open'),
('B05', 'measurement', 'language and disability are generated marginal fields', 'fixed shares, multipliers, and missing groups', 'cannot represent access need or lived experience', 'require language-access and disability review before alpha', 'accessibility reviewer', 'open'),
('B06', 'measurement', 'three equity dimensions are separate margins', 'margin_only equals one for every source row', 'joint and intersectional patterns are unknowable', 'prohibit cross-margin joins and intersectional claims', 'equity reviewer', 'open'),
('B07', 'uncertainty', 'group intervals omit ACS covariance and generator uncertainty', 'binomial teaching intervals around generated counts', 'intervals are narrower than full uncertainty', 'carry the Module 02 denominator and margin limits', 'biostatistics reviewer', 'open'),
('B08', 'suppression', 'small generated tract-group cells are withheld', 'event threshold 16 denominator threshold 100 and complementary suppression', 'published local detail is reduced', 'retain unavailable states and do not reconstruct or impute', 'privacy reviewer', 'open');

DROP TABLE IF EXISTS query_checks;
CREATE TABLE query_checks AS
SELECT 'Q01' AS check_id, 'equity margin rows' AS check_name, CAST((SELECT COUNT(*) FROM equity_margins) AS TEXT) AS observed_value, '151715' AS expected_value, CASE WHEN (SELECT COUNT(*) FROM equity_margins) = 151715 THEN 'pass' ELSE 'fail' END AS status
UNION ALL SELECT 'Q02', 'group contract rows', CAST((SELECT COUNT(*) FROM group_contract) AS TEXT), '19', CASE WHEN (SELECT COUNT(*) FROM group_contract) = 19 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q03', 'equity dimensions', CAST((SELECT COUNT(DISTINCT equity_dimension) FROM group_contract) AS TEXT), '3', CASE WHEN (SELECT COUNT(DISTINCT equity_dimension) FROM group_contract) = 3 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q04', 'tract age dimension keys', CAST((SELECT COUNT(*) FROM (SELECT tract_fips, age_band_id, equity_dimension FROM equity_margins GROUP BY tract_fips, age_band_id, equity_dimension)) AS TEXT), '23955', CASE WHEN (SELECT COUNT(*) FROM (SELECT tract_fips, age_band_id, equity_dimension FROM equity_margins GROUP BY tract_fips, age_band_id, equity_dimension)) = 23955 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q05', 'population total across three margins', CAST((SELECT SUM(population_count) FROM equity_margins) AS TEXT), '17039304', CASE WHEN (SELECT SUM(population_count) FROM equity_margins) = 17039304 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q06', 'event total across three margins', CAST((SELECT SUM(synthetic_event_count) FROM equity_margins) AS TEXT), '850842', CASE WHEN (SELECT SUM(synthetic_event_count) FROM equity_margins) = 850842 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q07', 'field completeness rows', CAST((SELECT COUNT(*) FROM field_completeness) AS TEXT), '7985', CASE WHEN (SELECT COUNT(*) FROM field_completeness) = 7985 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q08', 'group age rates', CAST((SELECT COUNT(*) FROM group_age_rates) AS TEXT), '110', CASE WHEN (SELECT COUNT(*) FROM group_age_rates) = 110 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q09', 'standardized group rates', CAST((SELECT COUNT(*) FROM standardized_group_rates) AS TEXT), '22', CASE WHEN (SELECT COUNT(*) FROM standardized_group_rates) = 22 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q10', 'pairwise disparity comparisons', CAST((SELECT COUNT(*) FROM disparity_comparisons) AS TEXT), '32', CASE WHEN (SELECT COUNT(*) FROM disparity_comparisons) = 32 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q11', 'summary disparity rows', CAST((SELECT COUNT(*) FROM summary_disparities) AS TEXT), '6', CASE WHEN (SELECT COUNT(*) FROM summary_disparities) = 6 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q12', 'missingness audit rows', CAST((SELECT COUNT(*) FROM missingness_audit) AS TEXT), '5', CASE WHEN (SELECT COUNT(*) FROM missingness_audit) = 5 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q13', 'representation audit rows', CAST((SELECT COUNT(*) FROM representation_audit) AS TEXT), '19', CASE WHEN (SELECT COUNT(*) FROM representation_audit) = 19 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q14', 'published tract group rows', CAST((SELECT COUNT(*) FROM published_tract_group_rates) AS TEXT), '30343', CASE WHEN (SELECT COUNT(*) FROM published_tract_group_rates) = 30343 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q15', 'suppression audit rows', CAST((SELECT COUNT(*) FROM complementary_suppression_audit) AS TEXT), '4791', CASE WHEN (SELECT COUNT(*) FROM complementary_suppression_audit) = 4791 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q16', 'bias register rows', CAST((SELECT COUNT(*) FROM bias_register) AS TEXT), '8', CASE WHEN (SELECT COUNT(*) FROM bias_register) = 8 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q17', 'source reconciliation rows', CAST((SELECT COUNT(*) FROM source_reconciliation) AS TEXT), '12', CASE WHEN (SELECT COUNT(*) FROM source_reconciliation) = 12 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q18', 'failed source reconciliation checks', CAST((SELECT COUNT(*) FROM source_reconciliation WHERE status <> 'pass') AS TEXT), '0', CASE WHEN (SELECT COUNT(*) FROM source_reconciliation WHERE status <> 'pass') = 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q19', 'overall reported references', CAST((SELECT COUNT(*) FROM standardized_group_rates WHERE group_id = 'overall_reported') AS TEXT), '3', CASE WHEN (SELECT COUNT(*) FROM standardized_group_rates WHERE group_id = 'overall_reported') = 3 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q20', 'predeclared group references', CAST((SELECT COUNT(*) FROM standardized_group_rates WHERE primary_reference = 1) AS TEXT), '3', CASE WHEN (SELECT COUNT(*) FROM standardized_group_rates WHERE primary_reference = 1) = 3 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q21', 'missing group rates', CAST((SELECT COUNT(*) FROM standardized_group_rates WHERE missing_group = 1) AS TEXT), '3', CASE WHEN (SELECT COUNT(*) FROM standardized_group_rates WHERE missing_group = 1) = 3 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q22', 'predeclared reference comparisons', CAST((SELECT COUNT(*) FROM disparity_comparisons WHERE reference_choice = 'predeclared_group') AS TEXT), '16', CASE WHEN (SELECT COUNT(*) FROM disparity_comparisons WHERE reference_choice = 'predeclared_group') = 16 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q23', 'overall reference comparisons', CAST((SELECT COUNT(*) FROM disparity_comparisons WHERE reference_choice = 'overall_reported') AS TEXT), '16', CASE WHEN (SELECT COUNT(*) FROM disparity_comparisons WHERE reference_choice = 'overall_reported') = 16 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q24', 'supported reported groups', CAST((SELECT COUNT(*) FROM standardized_group_rates WHERE support_state = 'supported_for_synthetic_comparison') AS TEXT), '16', CASE WHEN (SELECT COUNT(*) FROM standardized_group_rates WHERE support_state = 'supported_for_synthetic_comparison') = 16 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q25', 'failed suppression audits', CAST((SELECT COUNT(*) FROM complementary_suppression_audit WHERE status <> 'pass') AS TEXT), '0', CASE WHEN (SELECT COUNT(*) FROM complementary_suppression_audit WHERE status <> 'pass') = 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q26', 'published rows missing values', CAST((SELECT COUNT(*) FROM published_tract_group_rates WHERE support_state = 'publishable' AND (published_population_count IS NULL OR published_synthetic_event_count IS NULL OR published_crude_rate_per_100k IS NULL)) AS TEXT), '0', CASE WHEN (SELECT COUNT(*) FROM published_tract_group_rates WHERE support_state = 'publishable' AND (published_population_count IS NULL OR published_synthetic_event_count IS NULL OR published_crude_rate_per_100k IS NULL)) = 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q27', 'suppressed rows exposing values', CAST((SELECT COUNT(*) FROM published_tract_group_rates WHERE support_state <> 'publishable' AND (published_population_count IS NOT NULL OR published_synthetic_event_count IS NOT NULL OR published_crude_rate_per_100k IS NOT NULL OR published_rate_low_95 IS NOT NULL OR published_rate_high_95 IS NOT NULL)) AS TEXT), '0', CASE WHEN (SELECT COUNT(*) FROM published_tract_group_rates WHERE support_state <> 'publishable' AND (published_population_count IS NOT NULL OR published_synthetic_event_count IS NOT NULL OR published_crude_rate_per_100k IS NOT NULL OR published_rate_low_95 IS NOT NULL OR published_rate_high_95 IS NOT NULL)) = 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q28', 'tract total rows in published table', CAST((SELECT COUNT(*) FROM published_tract_group_rates WHERE group_id LIKE '%total%') AS TEXT), '0', CASE WHEN (SELECT COUNT(*) FROM published_tract_group_rates WHERE group_id LIKE '%total%') = 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q29', 'race missingness present', CAST((SELECT CASE WHEN missing_records > 0 THEN 1 ELSE 0 END FROM missingness_audit WHERE field_id = 'race') AS TEXT), '1', CASE WHEN (SELECT missing_records FROM missingness_audit WHERE field_id = 'race') > 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q30', 'ethnicity missingness present', CAST((SELECT CASE WHEN missing_records > 0 THEN 1 ELSE 0 END FROM missingness_audit WHERE field_id = 'ethnicity') AS TEXT), '1', CASE WHEN (SELECT missing_records FROM missingness_audit WHERE field_id = 'ethnicity') > 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q31', 'language missingness present', CAST((SELECT CASE WHEN missing_records > 0 THEN 1 ELSE 0 END FROM missingness_audit WHERE field_id = 'primary_language') AS TEXT), '1', CASE WHEN (SELECT missing_records FROM missingness_audit WHERE field_id = 'primary_language') > 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q32', 'disability missingness present', CAST((SELECT CASE WHEN missing_records > 0 THEN 1 ELSE 0 END FROM missingness_audit WHERE field_id = 'disability_status') AS TEXT), '1', CASE WHEN (SELECT missing_records FROM missingness_audit WHERE field_id = 'disability_status') > 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q33', 'conditioned geography missingness', CAST((SELECT missing_records FROM missingness_audit WHERE field_id = 'tract_geography') AS TEXT), '0', CASE WHEN (SELECT missing_records FROM missingness_audit WHERE field_id = 'tract_geography') = 0 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q34', 'margin-only source rows', CAST((SELECT SUM(margin_only) FROM equity_margins) AS TEXT), '151715', CASE WHEN (SELECT SUM(margin_only) FROM equity_margins) = 151715 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q35', 'synthetic source flags', CAST((SELECT SUM(synthetic_flag) FROM equity_margins) AS TEXT), '151715', CASE WHEN (SELECT SUM(synthetic_flag) FROM equity_margins) = 151715 THEN 'pass' ELSE 'fail' END
UNION ALL SELECT 'Q36', 'standard population weights', CAST(ROUND((SELECT SUM(CAST(standard_weight AS REAL)) FROM raw_standard_population), 9) AS TEXT), '1.0', CASE WHEN ABS((SELECT SUM(CAST(standard_weight AS REAL)) FROM raw_standard_population) - 1.0) < 0.000000001 THEN 'pass' ELSE 'fail' END;

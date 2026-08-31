DROP TABLE IF EXISTS equity_margins;
CREATE TABLE equity_margins AS
SELECT
    equity_margin_id,
    case_id,
    tract_fips,
    age_band_id,
    age_band,
    CAST(band_order AS INTEGER) AS band_order,
    period,
    equity_dimension,
    dimension_label,
    group_id,
    group_label,
    CAST(group_order AS INTEGER) AS group_order,
    CAST(population_count AS INTEGER) AS population_count,
    CAST(synthetic_event_count AS INTEGER) AS synthetic_event_count,
    CAST(base_share AS REAL) AS base_share,
    CAST(risk_multiplier AS REAL) AS risk_multiplier,
    generator_version,
    CAST(seed AS INTEGER) AS seed,
    CAST(synthetic_flag AS INTEGER) AS synthetic_flag,
    CAST(margin_only AS INTEGER) AS margin_only,
    claim_limit
FROM raw_equity_margins;

DROP TABLE IF EXISTS field_completeness;
CREATE TABLE field_completeness AS
SELECT
    completeness_id,
    case_id,
    tract_fips,
    age_band_id,
    age_band,
    CAST(band_order AS INTEGER) AS band_order,
    period,
    CAST(synthetic_event_count AS INTEGER) AS synthetic_event_count,
    CAST(race_missing_count AS INTEGER) AS race_missing_count,
    CAST(ethnicity_missing_count AS INTEGER) AS ethnicity_missing_count,
    CAST(primary_language_missing_count AS INTEGER) AS primary_language_missing_count,
    CAST(disability_status_missing_count AS INTEGER) AS disability_status_missing_count,
    CAST(tract_geography_missing_count AS INTEGER) AS tract_geography_missing_count,
    generator_version,
    CAST(seed AS INTEGER) AS seed,
    CAST(synthetic_flag AS INTEGER) AS synthetic_flag,
    analytic_universe,
    claim_limit
FROM raw_field_completeness;

DROP TABLE IF EXISTS group_contract;
CREATE TABLE group_contract AS
SELECT
    equity_dimension,
    dimension_label,
    group_id,
    group_label,
    CAST(group_order AS INTEGER) AS group_order,
    CAST(base_share AS REAL) AS base_share,
    CAST(risk_multiplier AS REAL) AS risk_multiplier,
    CAST(missing_group AS INTEGER) AS missing_group,
    CAST(primary_reference AS INTEGER) AS primary_reference,
    analysis_role,
    claim_limit
FROM raw_group_contract;

DROP TABLE IF EXISTS source_reconciliation;
CREATE TABLE source_reconciliation AS
SELECT 'SR01' AS check_id, 'synthetic equity margin rows' AS item,
       CAST((SELECT COUNT(*) FROM equity_margins) AS TEXT) AS observed_value,
       '151715' AS expected_value,
       CASE WHEN (SELECT COUNT(*) FROM equity_margins) = 151715 THEN 'pass' ELSE 'fail' END AS status,
       'complete generated tract-age-dimension-group margin release' AS interpretation
UNION ALL SELECT 'SR02', 'synthetic field completeness rows', CAST((SELECT COUNT(*) FROM field_completeness) AS TEXT), '7985', CASE WHEN (SELECT COUNT(*) FROM field_completeness) = 7985 THEN 'pass' ELSE 'fail' END, 'one generated completeness row per accepted tract-age row'
UNION ALL SELECT 'SR03', 'equity group contract rows', CAST((SELECT COUNT(*) FROM group_contract) AS TEXT), '19', CASE WHEN (SELECT COUNT(*) FROM group_contract) = 19 THEN 'pass' ELSE 'fail' END, 'three separate marginal dimensions'
UNION ALL SELECT 'SR04', 'race and ethnicity population total', CAST((SELECT SUM(population_count) FROM equity_margins WHERE equity_dimension = 'race_ethnicity') AS TEXT), '5679768', CASE WHEN (SELECT SUM(population_count) FROM equity_margins WHERE equity_dimension = 'race_ethnicity') = 5679768 THEN 'pass' ELSE 'fail' END, 'reconciles to accepted adult denominator'
UNION ALL SELECT 'SR05', 'race and ethnicity event total', CAST((SELECT SUM(synthetic_event_count) FROM equity_margins WHERE equity_dimension = 'race_ethnicity') AS TEXT), '283614', CASE WHEN (SELECT SUM(synthetic_event_count) FROM equity_margins WHERE equity_dimension = 'race_ethnicity') = 283614 THEN 'pass' ELSE 'fail' END, 'reconciles to accepted generated numerator'
UNION ALL SELECT 'SR06', 'primary language population total', CAST((SELECT SUM(population_count) FROM equity_margins WHERE equity_dimension = 'primary_language') AS TEXT), '5679768', CASE WHEN (SELECT SUM(population_count) FROM equity_margins WHERE equity_dimension = 'primary_language') = 5679768 THEN 'pass' ELSE 'fail' END, 'reconciles to accepted adult denominator'
UNION ALL SELECT 'SR07', 'primary language event total', CAST((SELECT SUM(synthetic_event_count) FROM equity_margins WHERE equity_dimension = 'primary_language') AS TEXT), '283614', CASE WHEN (SELECT SUM(synthetic_event_count) FROM equity_margins WHERE equity_dimension = 'primary_language') = 283614 THEN 'pass' ELSE 'fail' END, 'reconciles to accepted generated numerator'
UNION ALL SELECT 'SR08', 'disability status population total', CAST((SELECT SUM(population_count) FROM equity_margins WHERE equity_dimension = 'disability_status') AS TEXT), '5679768', CASE WHEN (SELECT SUM(population_count) FROM equity_margins WHERE equity_dimension = 'disability_status') = 5679768 THEN 'pass' ELSE 'fail' END, 'reconciles to accepted adult denominator'
UNION ALL SELECT 'SR09', 'disability status event total', CAST((SELECT SUM(synthetic_event_count) FROM equity_margins WHERE equity_dimension = 'disability_status') AS TEXT), '283614', CASE WHEN (SELECT SUM(synthetic_event_count) FROM equity_margins WHERE equity_dimension = 'disability_status') = 283614 THEN 'pass' ELSE 'fail' END, 'reconciles to accepted generated numerator'
UNION ALL SELECT 'SR10', 'frozen Module 02 denominator total', CAST((SELECT SUM(CAST(denominator_estimate AS INTEGER)) FROM raw_upstream_denominators) AS TEXT), '5679768', CASE WHEN (SELECT SUM(CAST(denominator_estimate AS INTEGER)) FROM raw_upstream_denominators) = 5679768 THEN 'pass' ELSE 'fail' END, 'accepted Module 02 denominator preserved'
UNION ALL SELECT 'SR11', 'frozen Module 02 event total', CAST((SELECT SUM(CAST(synthetic_event_count AS INTEGER)) FROM raw_upstream_events) AS TEXT), '283614', CASE WHEN (SELECT SUM(CAST(synthetic_event_count AS INTEGER)) FROM raw_upstream_events) = 283614 THEN 'pass' ELSE 'fail' END, 'accepted Module 02 numerator preserved'
UNION ALL SELECT 'SR12', 'margin-only flags', CAST((SELECT SUM(margin_only) FROM equity_margins) AS TEXT), '151715', CASE WHEN (SELECT SUM(margin_only) FROM equity_margins) = 151715 THEN 'pass' ELSE 'fail' END, 'separate dimensions cannot be crossed into person records';

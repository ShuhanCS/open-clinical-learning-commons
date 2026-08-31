DROP TABLE IF EXISTS indirect_standardization;
CREATE TABLE indirect_standardization AS
WITH expected_by_age AS (
    SELECT
        d.tract_fips,
        d.age_band_id,
        d.denominator_estimate,
        e.synthetic_event_count,
        s.statewide_synthetic_rate_per_100k,
        d.denominator_estimate * s.statewide_synthetic_rate_per_100k / 100000.0 AS expected_synthetic_events
    FROM adult_age_denominators d
    JOIN linked_synthetic_events e
      ON e.tract_fips = d.tract_fips
     AND e.age_band_id = d.age_band_id
    JOIN standard_population s ON s.age_band_id = d.age_band_id
), summarized AS (
    SELECT
        tract_fips,
        SUM(synthetic_event_count) AS synthetic_event_count,
        ROUND(SUM(expected_synthetic_events), 8) AS expected_synthetic_events,
        MIN(denominator_estimate) AS minimum_age_band_denominator
    FROM expected_by_age
    GROUP BY tract_fips
)
SELECT
    tract_fips,
    synthetic_event_count,
    expected_synthetic_events,
    ROUND(1.0 * synthetic_event_count / expected_synthetic_events, 8) AS standardized_event_ratio,
    ROUND(RATIO_LOW(synthetic_event_count, expected_synthetic_events), 8) AS ratio_low_95,
    ROUND(RATIO_HIGH(synthetic_event_count, expected_synthetic_events), 8) AS ratio_high_95,
    CASE WHEN minimum_age_band_denominator < 50 THEN 'required_for_guided_sparse-support_exercise' ELSE 'available_as_secondary_check' END AS indirect_role,
    'ratio compares a synthetic count with an expected synthetic count under statewide synthetic age rates' AS measure_definition,
    'not directly comparable across tracts as a common-standard rate and not a real excess-case claim' AS claim_limit
FROM summarized
ORDER BY tract_fips;

DROP TABLE IF EXISTS source_reconciliation;
CREATE TABLE source_reconciliation AS
SELECT 'SR01' AS check_id, 'ACS tract rows' AS item, COUNT(*) AS observed_value, 1620 AS expected_value, CASE WHEN COUNT(*) = 1620 THEN 'pass' ELSE 'fail' END AS status, 'complete accepted Massachusetts B01001 release' AS interpretation FROM raw_acs_b01001
UNION ALL SELECT 'SR02', 'PLACES diabetes tract rows', COUNT(*), 1597, CASE WHEN COUNT(*) = 1597 THEN 'pass' ELSE 'fail' END, 'complete accepted Massachusetts DIABETES extract' FROM raw_places
UNION ALL SELECT 'SR03', 'SVI tract rows', COUNT(*), 1613, CASE WHEN COUNT(*) = 1613 THEN 'pass' ELSE 'fail' END, 'complete accepted Massachusetts SVI tract release' FROM raw_svi
UNION ALL SELECT 'SR04', 'three-source intersection', SUM(three_source_intersection), 1597, CASE WHEN SUM(three_source_intersection) = 1597 THEN 'pass' ELSE 'fail' END, 'every measure tract is present in all three accepted sources' FROM tract_linkage_audit
UNION ALL SELECT 'SR05', 'union tracts', COUNT(*), 1620, CASE WHEN COUNT(*) = 1620 THEN 'pass' ELSE 'fail' END, 'unmatched public-source states remain visible' FROM tract_linkage_audit
UNION ALL SELECT 'SR06', 'age-band denominator rows', COUNT(*), 7985, CASE WHEN COUNT(*) = 7985 THEN 'pass' ELSE 'fail' END, '1,597 tracts times five declared adult age bands' FROM adult_age_denominators
UNION ALL SELECT 'SR07', 'synthetic event rows', COUNT(*), 7985, CASE WHEN COUNT(*) = 7985 THEN 'pass' ELSE 'fail' END, 'one generated tract-age-period row per denominator' FROM linked_synthetic_events
UNION ALL SELECT 'SR08', 'public modeled prevalence rows', COUNT(*), 1597, CASE WHEN COUNT(*) = 1597 THEN 'pass' ELSE 'fail' END, 'public modeled prevalence stays separate from synthetic events' FROM public_modeled_prevalence
ORDER BY check_id;

DROP TABLE IF EXISTS query_checks;
CREATE TABLE query_checks AS
SELECT 'Q01' AS check_id, 'tract linkage rows' AS check_name, CAST((SELECT COUNT(*) FROM tract_linkage_audit) AS TEXT) AS observed_value, '1620' AS expected_value
UNION ALL SELECT 'Q02', 'three-source eligible tracts', CAST((SELECT SUM(measure_eligible) FROM tract_linkage_audit) AS TEXT), '1597'
UNION ALL SELECT 'Q03', 'unexpected linkage states', CAST((SELECT COUNT(*) FROM tract_linkage_audit WHERE unmatched_state = 'unexpected source-presence state') AS TEXT), '0'
UNION ALL SELECT 'Q04', 'ACS and SVI tracts without PLACES', CAST((SELECT COUNT(*) FROM tract_linkage_audit WHERE acs_present = 1 AND svi_present = 1 AND places_present = 0) AS TEXT), '16'
UNION ALL SELECT 'Q05', 'ACS-only tracts', CAST((SELECT COUNT(*) FROM tract_linkage_audit WHERE acs_present = 1 AND svi_present = 0 AND places_present = 0) AS TEXT), '7'
UNION ALL SELECT 'Q06', 'age-band denominator rows', CAST((SELECT COUNT(*) FROM adult_age_denominators) AS TEXT), '7985'
UNION ALL SELECT 'Q07', 'declared age bands', CAST((SELECT COUNT(DISTINCT age_band_id) FROM adult_age_denominators) AS TEXT), '5'
UNION ALL SELECT 'Q08', 'adult denominator total', CAST((SELECT SUM(denominator_estimate) FROM adult_age_denominators) AS TEXT), '5679768'
UNION ALL SELECT 'Q09', 'zero age-band denominators', CAST((SELECT COUNT(*) FROM adult_age_denominators WHERE denominator_estimate = 0) AS TEXT), '41'
UNION ALL SELECT 'Q10', 'negative age-band denominators', CAST((SELECT COUNT(*) FROM adult_age_denominators WHERE denominator_estimate < 0) AS TEXT), '0'
UNION ALL SELECT 'Q11', 'synthetic event rows', CAST((SELECT COUNT(*) FROM linked_synthetic_events) AS TEXT), '7985'
UNION ALL SELECT 'Q12', 'synthetic tract count', CAST((SELECT COUNT(DISTINCT tract_fips) FROM linked_synthetic_events) AS TEXT), '1597'
UNION ALL SELECT 'Q13', 'synthetic event total', CAST((SELECT SUM(synthetic_event_count) FROM linked_synthetic_events) AS TEXT), '283614'
UNION ALL SELECT 'Q14', 'denominator mismatches', CAST((SELECT COUNT(*) FROM linked_synthetic_events WHERE denominator_match <> 1) AS TEXT), '0'
UNION ALL SELECT 'Q15', 'invalid synthetic counts', CAST((SELECT COUNT(*) FROM linked_synthetic_events WHERE synthetic_event_count < 0 OR synthetic_event_count > denominator_estimate) AS TEXT), '0'
UNION ALL SELECT 'Q16', 'non-synthetic rows', CAST((SELECT COUNT(*) FROM linked_synthetic_events WHERE synthetic_flag <> 1) AS TEXT), '0'
UNION ALL SELECT 'Q17', 'wrong synthetic periods', CAST((SELECT COUNT(*) FROM linked_synthetic_events WHERE period <> '2024') AS TEXT), '0'
UNION ALL SELECT 'Q18', 'standard population rows', CAST((SELECT COUNT(*) FROM standard_population) AS TEXT), '5'
UNION ALL SELECT 'Q19', 'standard weight sum', printf('%.10f', (SELECT SUM(standard_weight) FROM standard_population)), '1.0000000000'
UNION ALL SELECT 'Q20', 'standard population total', CAST((SELECT SUM(standard_population) FROM standard_population) AS TEXT), '5679768'
UNION ALL SELECT 'Q21', 'age-specific rate rows', CAST((SELECT COUNT(*) FROM age_specific_rates) AS TEXT), '7985'
UNION ALL SELECT 'Q22', 'available age-specific rates', CAST((SELECT COUNT(*) FROM age_specific_rates WHERE availability_state = 'available') AS TEXT), '7944'
UNION ALL SELECT 'Q23', 'tract rate summaries', CAST((SELECT COUNT(*) FROM tract_rate_summary) AS TEXT), '1597'
UNION ALL SELECT 'Q24', 'direct rates available', CAST((SELECT COUNT(*) FROM tract_rate_summary WHERE direct_standardized_rate_per_100k IS NOT NULL) AS TEXT), '1576'
UNION ALL SELECT 'Q25', 'direct rates unavailable', CAST((SELECT COUNT(*) FROM tract_rate_summary WHERE direct_standardized_rate_per_100k IS NULL) AS TEXT), '21'
UNION ALL SELECT 'Q26', 'guided indirect required tracts', CAST((SELECT COUNT(*) FROM tract_rate_summary WHERE guided_indirect_required = 'yes') AS TEXT), '80'
UNION ALL SELECT 'Q27', 'indirect rows', CAST((SELECT COUNT(*) FROM indirect_standardization) AS TEXT), '1597'
UNION ALL SELECT 'Q28', 'nonpositive expected synthetic events', CAST((SELECT COUNT(*) FROM indirect_standardization WHERE expected_synthetic_events <= 0) AS TEXT), '0'
UNION ALL SELECT 'Q29', 'public modeled prevalence rows', CAST((SELECT COUNT(*) FROM public_modeled_prevalence) AS TEXT), '1597'
UNION ALL SELECT 'Q30', 'failed source reconciliation rows', CAST((SELECT COUNT(*) FROM source_reconciliation WHERE status <> 'pass') AS TEXT), '0';

ALTER TABLE query_checks ADD COLUMN status TEXT;
UPDATE query_checks SET status = CASE WHEN observed_value = expected_value THEN 'pass' ELSE 'fail' END;

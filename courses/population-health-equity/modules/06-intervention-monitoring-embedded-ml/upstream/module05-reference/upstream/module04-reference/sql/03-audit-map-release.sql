DROP TABLE IF EXISTS map_class_definitions;
CREATE TABLE map_class_definitions (
    class_order INTEGER PRIMARY KEY,
    map_class TEXT NOT NULL
);
INSERT INTO map_class_definitions VALUES
    (1, 'less than 5.0%'),
    (2, '5.0% to less than 10.0%'),
    (3, '10.0% to less than 15.0%'),
    (4, '15.0% to less than 20.0%'),
    (5, '20.0% or greater'),
    (6, 'unavailable');

DROP TABLE IF EXISTS map_class_summary;
CREATE TABLE map_class_summary AS
SELECT
    d.class_order,
    d.map_class,
    COUNT(t.tract_fips) AS tract_count,
    SUM(CASE WHEN t.support_state = 'limited_support_review' THEN 1 ELSE 0 END) AS limited_support_tracts,
    SUM(COALESCE(t.places_adult_population_field, 0)) AS retained_places_population,
    'absolute display class; not a rank, priority, target, or eligibility group' AS interpretation_limit
FROM map_class_definitions d
LEFT JOIN tract_map_table t ON t.map_class = d.map_class
GROUP BY d.class_order, d.map_class
ORDER BY d.class_order;

DROP TABLE IF EXISTS query_checks;
CREATE TABLE query_checks AS
SELECT 'Q01' check_id, 'geometry rows' check_name, '1620' expected, CAST(COUNT(*) AS TEXT) actual,
       CASE WHEN COUNT(*) = 1620 THEN 'pass' ELSE 'fail' END status FROM raw_geometry
UNION ALL SELECT 'Q02', 'unique geometry keys', '1620', CAST(COUNT(DISTINCT tract_fips) AS TEXT),
       CASE WHEN COUNT(DISTINCT tract_fips) = 1620 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q03', 'Massachusetts state only', '25', MIN(state_fips),
       CASE WHEN COUNT(DISTINCT state_fips) = 1 AND MIN(state_fips) = '25' THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q04', 'county count', '14', CAST(COUNT(DISTINCT county_fips) AS TEXT),
       CASE WHEN COUNT(DISTINCT county_fips) = 14 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q05', 'valid geometry rows', '1620', CAST(SUM(is_valid) AS TEXT),
       CASE WHEN SUM(is_valid) = 1620 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q06', 'null geometry rows', '0', CAST(SUM(is_null) AS TEXT),
       CASE WHEN SUM(is_null) = 0 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q07', 'empty geometry rows', '0', CAST(SUM(is_empty) AS TEXT),
       CASE WHEN SUM(is_empty) = 0 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q08', 'accepted geometry types', '0 invalid', CAST(SUM(CASE WHEN geometry_type NOT IN ('Polygon','MultiPolygon') THEN 1 ELSE 0 END) AS TEXT),
       CASE WHEN SUM(CASE WHEN geometry_type NOT IN ('Polygon','MultiPolygon') THEN 1 ELSE 0 END) = 0 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q09', 'maximum projected area relative difference', '<0.001', printf('%.10f', MAX(CAST(area_relative_difference AS REAL))),
       CASE WHEN MAX(CAST(area_relative_difference AS REAL)) < 0.001 THEN 'pass' ELSE 'fail' END FROM raw_geometry
UNION ALL SELECT 'Q10', 'accepted PLACES rows', '1597', CAST(COUNT(*) AS TEXT),
       CASE WHEN COUNT(*) = 1597 THEN 'pass' ELSE 'fail' END FROM raw_places
UNION ALL SELECT 'Q11', 'accepted linkage audit rows', '1620', CAST(COUNT(*) AS TEXT),
       CASE WHEN COUNT(*) = 1620 THEN 'pass' ELSE 'fail' END FROM raw_linkage_audit
UNION ALL SELECT 'Q12', 'matched measure tracts', '1597', CAST(SUM(join_state = 'matched_measure') AS TEXT),
       CASE WHEN SUM(join_state = 'matched_measure') = 1597 THEN 'pass' ELSE 'fail' END FROM geometry_join_audit
UNION ALL SELECT 'Q13', 'geometry-only unavailable tracts', '23', CAST(SUM(join_state = 'geometry_only_unavailable') AS TEXT),
       CASE WHEN SUM(join_state = 'geometry_only_unavailable') = 23 THEN 'pass' ELSE 'fail' END FROM geometry_join_audit
UNION ALL SELECT 'Q14', 'linkage disagreements', '0', CAST(SUM(join_state = 'linkage_disagreement') AS TEXT),
       CASE WHEN SUM(join_state = 'linkage_disagreement') = 0 THEN 'pass' ELSE 'fail' END FROM geometry_join_audit
UNION ALL SELECT 'Q15', 'unavailable rows retain null estimate', '23', CAST(SUM(map_class = 'unavailable' AND modeled_crude_prevalence_percent IS NULL) AS TEXT),
       CASE WHEN SUM(map_class = 'unavailable' AND modeled_crude_prevalence_percent IS NULL) = 23 THEN 'pass' ELSE 'fail' END FROM tract_map_table
UNION ALL SELECT 'Q16', 'mapped public estimates', '1597', CAST(SUM(modeled_crude_prevalence_percent IS NOT NULL) AS TEXT),
       CASE WHEN SUM(modeled_crude_prevalence_percent IS NOT NULL) = 1597 THEN 'pass' ELSE 'fail' END FROM tract_map_table
UNION ALL SELECT 'Q17', 'measure year', '2023', CAST(MIN(CAST(measure_year AS INTEGER)) AS TEXT),
       CASE WHEN MIN(CAST(measure_year AS INTEGER)) = 2023 AND MAX(CAST(measure_year AS INTEGER)) = 2023 THEN 'pass' ELSE 'fail' END FROM tract_map_table WHERE measure_year IS NOT NULL
UNION ALL SELECT 'Q18', 'measure identity', 'DIABETES', MIN(measure_id),
       CASE WHEN COUNT(DISTINCT measure_id) = 1 AND MIN(measure_id) = 'DIABETES' THEN 'pass' ELSE 'fail' END FROM tract_map_table WHERE measure_id IS NOT NULL
UNION ALL SELECT 'Q19', 'source release identity', 'CDC PLACES 2025 census-tract release', MIN(source_release),
       CASE WHEN COUNT(DISTINCT source_release) = 1 AND MIN(source_release) = 'CDC PLACES 2025 census-tract release' THEN 'pass' ELSE 'fail' END FROM tract_map_table WHERE source_release IS NOT NULL
UNION ALL SELECT 'Q20', 'ordered confidence limits', '0 invalid', CAST(SUM(NOT (modeled_low_confidence_limit <= modeled_crude_prevalence_percent AND modeled_crude_prevalence_percent <= modeled_high_confidence_limit)) AS TEXT),
       CASE WHEN SUM(NOT (modeled_low_confidence_limit <= modeled_crude_prevalence_percent AND modeled_crude_prevalence_percent <= modeled_high_confidence_limit)) = 0 THEN 'pass' ELSE 'fail' END FROM tract_map_table WHERE modeled_crude_prevalence_percent IS NOT NULL
UNION ALL SELECT 'Q21', 'county teaching summaries', '14', CAST(COUNT(*) AS TEXT),
       CASE WHEN COUNT(*) = 14 THEN 'pass' ELSE 'fail' END FROM county_aggregation
UNION ALL SELECT 'Q22', 'aggregation comparison rows', '1597', CAST(COUNT(*) AS TEXT),
       CASE WHEN COUNT(*) = 1597 THEN 'pass' ELSE 'fail' END FROM aggregation_comparison
UNION ALL SELECT 'Q23', 'map class rows', '6', CAST(COUNT(*) AS TEXT),
       CASE WHEN COUNT(*) = 6 THEN 'pass' ELSE 'fail' END FROM map_class_summary
UNION ALL SELECT 'Q24', 'map class tract reconciliation', '1620', CAST(SUM(tract_count) AS TEXT),
       CASE WHEN SUM(tract_count) = 1620 THEN 'pass' ELSE 'fail' END FROM map_class_summary
UNION ALL SELECT 'Q25', 'stability rows', '1597', CAST(COUNT(*) AS TEXT),
       CASE WHEN COUNT(*) = 1597 THEN 'pass' ELSE 'fail' END FROM small_area_stability
UNION ALL SELECT 'Q26', 'limited-support review is populated', '>0', CAST(SUM(support_state = 'limited_support_review') AS TEXT),
       CASE WHEN SUM(support_state = 'limited_support_review') > 0 THEN 'pass' ELSE 'fail' END FROM tract_map_table
UNION ALL SELECT 'Q27', 'supported display state is populated', '>0', CAST(SUM(support_state = 'supported_for_teaching_display') AS TEXT),
       CASE WHEN SUM(support_state = 'supported_for_teaching_display') > 0 THEN 'pass' ELSE 'fail' END FROM tract_map_table
UNION ALL SELECT 'Q28', 'aggregation changes at least one display class', '>0', CAST(SUM(class_changes_after_aggregation) AS TEXT),
       CASE WHEN SUM(class_changes_after_aggregation) > 0 THEN 'pass' ELSE 'fail' END FROM aggregation_comparison
UNION ALL SELECT 'Q29', 'county names are complete', '0 missing', CAST(SUM(county_name IS NULL OR county_name = '') AS TEXT),
       CASE WHEN SUM(county_name IS NULL OR county_name = '') = 0 THEN 'pass' ELSE 'fail' END FROM county_aggregation
UNION ALL SELECT 'Q30', 'retained PLACES population', '5663670', CAST(SUM(places_adult_population_field) AS TEXT),
       CASE WHEN SUM(places_adult_population_field) = 5663670 THEN 'pass' ELSE 'fail' END FROM tract_map_table
UNION ALL SELECT 'Q31', 'public estimate range', '0.7 to 30.5', printf('%.1f to %.1f', MIN(modeled_crude_prevalence_percent), MAX(modeled_crude_prevalence_percent)),
       CASE WHEN MIN(modeled_crude_prevalence_percent) = 0.7 AND MAX(modeled_crude_prevalence_percent) = 30.5 THEN 'pass' ELSE 'fail' END FROM tract_map_table
UNION ALL SELECT 'Q32', 'one public claim limit', '1', CAST(COUNT(DISTINCT claim_limit) AS TEXT),
       CASE WHEN COUNT(DISTINCT claim_limit) = 1 THEN 'pass' ELSE 'fail' END FROM tract_map_table WHERE modeled_crude_prevalence_percent IS NOT NULL
ORDER BY check_id;

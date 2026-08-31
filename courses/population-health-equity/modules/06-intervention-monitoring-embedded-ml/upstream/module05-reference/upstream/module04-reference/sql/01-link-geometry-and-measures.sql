DROP TABLE IF EXISTS geometry_join_audit;
CREATE TABLE geometry_join_audit AS
SELECT
    g.tract_fips,
    g.state_fips,
    g.county_fips,
    g.tract_code,
    g.tract_name,
    g.geometry_type,
    g.is_valid,
    g.is_empty,
    g.is_null,
    g.aland_sq_m,
    g.awater_sq_m,
    g.projected_area_sq_m,
    g.area_relative_difference,
    CASE WHEN p.tract_fips IS NULL THEN 0 ELSE 1 END AS places_present,
    CAST(a.places_present AS INTEGER) AS accepted_places_present,
    CASE
        WHEN p.tract_fips IS NOT NULL AND CAST(a.places_present AS INTEGER) = 1 THEN 'matched_measure'
        WHEN p.tract_fips IS NULL AND CAST(a.places_present AS INTEGER) = 0 THEN 'geometry_only_unavailable'
        ELSE 'linkage_disagreement'
    END AS join_state
FROM raw_geometry g
LEFT JOIN raw_places p USING (tract_fips)
LEFT JOIN raw_linkage_audit a USING (tract_fips)
ORDER BY g.tract_fips;

DROP TABLE IF EXISTS tract_map_table;
CREATE TABLE tract_map_table AS
SELECT
    g.tract_fips,
    g.county_fips,
    p.county_name,
    p.measure_year,
    p.measure_id,
    p.data_value_type_id,
    CAST(p.modeled_crude_prevalence_percent AS REAL) AS modeled_crude_prevalence_percent,
    CAST(p.modeled_low_confidence_limit AS REAL) AS modeled_low_confidence_limit,
    CAST(p.modeled_high_confidence_limit AS REAL) AS modeled_high_confidence_limit,
    CASE
        WHEN p.tract_fips IS NULL THEN NULL
        ELSE CAST(p.modeled_high_confidence_limit AS REAL) - CAST(p.modeled_low_confidence_limit AS REAL)
    END AS interval_width_percentage_points,
    CAST(p.places_adult_population_field AS INTEGER) AS places_adult_population_field,
    p.source_release,
    p.estimate_type,
    CASE
        WHEN p.tract_fips IS NULL THEN 'unavailable'
        WHEN CAST(p.modeled_crude_prevalence_percent AS REAL) < 5.0 THEN 'less than 5.0%'
        WHEN CAST(p.modeled_crude_prevalence_percent AS REAL) < 10.0 THEN '5.0% to less than 10.0%'
        WHEN CAST(p.modeled_crude_prevalence_percent AS REAL) < 15.0 THEN '10.0% to less than 15.0%'
        WHEN CAST(p.modeled_crude_prevalence_percent AS REAL) < 20.0 THEN '15.0% to less than 20.0%'
        ELSE '20.0% or greater'
    END AS map_class,
    CASE
        WHEN p.tract_fips IS NULL THEN 'unavailable'
        WHEN CAST(p.modeled_high_confidence_limit AS REAL) - CAST(p.modeled_low_confidence_limit AS REAL) >= 4.0
          OR CAST(p.places_adult_population_field AS INTEGER) < 500 THEN 'limited_support_review'
        ELSE 'supported_for_teaching_display'
    END AS support_state,
    CASE
        WHEN p.tract_fips IS NULL THEN 'no accepted PLACES row; retain unavailable state'
        ELSE 'public modeled small-area estimate; not observed cases, individual risk, a disparity, or an action rule'
    END AS claim_limit
FROM raw_geometry g
LEFT JOIN raw_places p USING (tract_fips)
ORDER BY g.tract_fips;

DROP TABLE IF EXISTS small_area_stability;
CREATE TABLE small_area_stability AS
SELECT
    tract_fips,
    county_fips,
    county_name,
    modeled_crude_prevalence_percent,
    modeled_low_confidence_limit,
    modeled_high_confidence_limit,
    interval_width_percentage_points,
    places_adult_population_field,
    support_state,
    CASE
        WHEN interval_width_percentage_points >= 4.0 AND places_adult_population_field < 500
            THEN 'interval width and retained population trigger review'
        WHEN interval_width_percentage_points >= 4.0
            THEN 'interval width triggers review'
        WHEN places_adult_population_field < 500
            THEN 'retained population triggers review'
        ELSE 'no classroom review trigger'
    END AS review_reason,
    'classroom review flag only; not a CDC quality designation, suppression rule, or exclusion rule' AS interpretation_limit
FROM tract_map_table
WHERE modeled_crude_prevalence_percent IS NOT NULL
ORDER BY tract_fips;

DROP TABLE IF EXISTS county_aggregation;
CREATE TABLE county_aggregation AS
WITH geometry_counts AS (
    SELECT county_fips, COUNT(*) AS tract_geometry_count
    FROM raw_geometry
    GROUP BY county_fips
), measure_summary AS (
    SELECT
        county_fips,
        MAX(county_name) AS county_name,
        COUNT(*) AS tracts_with_measure,
        SUM(places_adult_population_field) AS places_adult_population,
        SUM(modeled_crude_prevalence_percent * places_adult_population_field)
          / SUM(places_adult_population_field) AS weighted_modeled_prevalence_percent,
        MIN(modeled_crude_prevalence_percent) AS minimum_tract_prevalence_percent,
        MAX(modeled_crude_prevalence_percent) AS maximum_tract_prevalence_percent
    FROM tract_map_table
    WHERE modeled_crude_prevalence_percent IS NOT NULL
    GROUP BY county_fips
)
SELECT
    m.county_fips,
    m.county_name,
    g.tract_geometry_count,
    m.tracts_with_measure,
    g.tract_geometry_count - m.tracts_with_measure AS geometry_only_tracts,
    m.places_adult_population,
    m.weighted_modeled_prevalence_percent,
    m.minimum_tract_prevalence_percent,
    m.maximum_tract_prevalence_percent,
    m.maximum_tract_prevalence_percent - m.minimum_tract_prevalence_percent AS within_county_range_percentage_points,
    CASE
        WHEN m.weighted_modeled_prevalence_percent < 5.0 THEN 'less than 5.0%'
        WHEN m.weighted_modeled_prevalence_percent < 10.0 THEN '5.0% to less than 10.0%'
        WHEN m.weighted_modeled_prevalence_percent < 15.0 THEN '10.0% to less than 15.0%'
        WHEN m.weighted_modeled_prevalence_percent < 20.0 THEN '15.0% to less than 20.0%'
        ELSE '20.0% or greater'
    END AS county_summary_class,
    'population-weighted tract teaching summary; not an official county PLACES estimate' AS summary_type,
    'aggregation changes the question and can hide within-county variation; no rank, target, or action follows' AS claim_limit
FROM measure_summary m
JOIN geometry_counts g USING (county_fips)
ORDER BY m.county_fips;

DROP TABLE IF EXISTS aggregation_comparison;
CREATE TABLE aggregation_comparison AS
SELECT
    t.tract_fips,
    t.county_fips,
    t.county_name,
    t.modeled_crude_prevalence_percent AS tract_modeled_prevalence_percent,
    t.map_class AS tract_map_class,
    c.weighted_modeled_prevalence_percent AS county_weighted_tract_summary_percent,
    c.county_summary_class,
    ABS(t.modeled_crude_prevalence_percent - c.weighted_modeled_prevalence_percent) AS absolute_difference_percentage_points,
    CASE WHEN t.map_class = c.county_summary_class THEN 0 ELSE 1 END AS class_changes_after_aggregation,
    'tract and county summaries answer different area-level questions; neither supports individual inference' AS interpretation_limit
FROM tract_map_table t
JOIN county_aggregation c USING (county_fips)
WHERE t.modeled_crude_prevalence_percent IS NOT NULL
ORDER BY t.tract_fips;

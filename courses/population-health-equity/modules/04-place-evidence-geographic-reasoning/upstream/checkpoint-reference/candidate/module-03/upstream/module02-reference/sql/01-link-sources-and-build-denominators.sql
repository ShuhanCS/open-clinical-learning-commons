DROP TABLE IF EXISTS tract_linkage_audit;
CREATE TABLE tract_linkage_audit AS
WITH tract_union AS (
    SELECT tract_fips FROM raw_acs_b01001
    UNION
    SELECT locationid FROM raw_places
    UNION
    SELECT FIPS FROM raw_svi
)
SELECT
    u.tract_fips,
    CASE WHEN a.tract_fips IS NULL THEN 0 ELSE 1 END AS acs_present,
    CASE WHEN p.locationid IS NULL THEN 0 ELSE 1 END AS places_present,
    CASE WHEN s.FIPS IS NULL THEN 0 ELSE 1 END AS svi_present,
    CASE WHEN a.tract_fips IS NOT NULL AND p.locationid IS NOT NULL AND s.FIPS IS NOT NULL THEN 1 ELSE 0 END AS three_source_intersection,
    CASE WHEN a.tract_fips IS NOT NULL AND p.locationid IS NOT NULL AND s.FIPS IS NOT NULL THEN 1 ELSE 0 END AS measure_eligible,
    CASE
        WHEN a.tract_fips IS NOT NULL AND p.locationid IS NOT NULL AND s.FIPS IS NOT NULL THEN 'complete three-source intersection'
        WHEN a.tract_fips IS NOT NULL AND p.locationid IS NULL AND s.FIPS IS NOT NULL THEN 'ACS and SVI; no PLACES diabetes row'
        WHEN a.tract_fips IS NOT NULL AND p.locationid IS NULL AND s.FIPS IS NULL THEN 'ACS only; no PLACES or SVI row'
        ELSE 'unexpected source-presence state'
    END AS unmatched_state
FROM tract_union u
LEFT JOIN raw_acs_b01001 a ON a.tract_fips = u.tract_fips
LEFT JOIN raw_places p ON p.locationid = u.tract_fips
LEFT JOIN raw_svi s ON s.FIPS = u.tract_fips
ORDER BY u.tract_fips;

DROP TABLE IF EXISTS adult_age_denominators;
CREATE TABLE adult_age_denominators AS
SELECT
    c.tract_fips,
    c.age_band_id,
    c.age_band,
    c.band_order,
    SUM(c.estimate) AS denominator_estimate,
    ROUND(SQRT(
        SUM(CASE WHEN c.estimate <> 0 THEN c.moe * c.moe ELSE 0 END)
        + COALESCE(MAX(CASE WHEN c.estimate = 0 THEN c.moe * c.moe ELSE NULL END), 0)
    ), 3) AS denominator_moe90,
    COUNT(*) AS source_cell_count,
    SUM(CASE WHEN c.estimate = 0 THEN 1 ELSE 0 END) AS zero_source_cells,
    'ACS 2020-2024 B01001' AS denominator_source,
    '2020-2024 five-year estimate' AS source_period,
    'Massachusetts census tract' AS geography,
    'RSS of nonzero-cell MOEs plus the largest zero-estimate-cell MOE' AS moe_method,
    'Approximate 90 percent MOE; component covariance is not included' AS moe_limit
FROM raw_acs_age_cells c
JOIN tract_linkage_audit l
    ON l.tract_fips = c.tract_fips
   AND l.measure_eligible = 1
GROUP BY c.tract_fips, c.age_band_id, c.age_band, c.band_order
ORDER BY c.tract_fips, c.band_order;

CREATE UNIQUE INDEX IF NOT EXISTS candidate_release_tract_key ON candidate_release(tract_fips);
CREATE INDEX IF NOT EXISTS candidate_release_county_key ON candidate_release(county_fips);

DROP VIEW IF EXISTS candidate_source_separation;
CREATE VIEW candidate_source_separation AS
SELECT
    COUNT(*) AS candidate_rows,
    COUNT(DISTINCT tract_fips) AS unique_tracts,
    COUNT(DISTINCT public_source_release) AS public_releases,
    COUNT(DISTINCT synthetic_source_id) AS synthetic_releases,
    SUM(synthetic_flag = 1) AS synthetic_rows,
    SUM(public_evidence_role = 'accepted public modeled area-level estimate') AS public_role_rows
FROM candidate_release;

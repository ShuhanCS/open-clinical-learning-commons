CREATE UNIQUE INDEX IF NOT EXISTS candidate_tract_key ON candidate_release(tract_fips);
CREATE UNIQUE INDEX IF NOT EXISTS dry_run_test_key ON monitoring_dry_run(fictional_test_id);

DROP VIEW IF EXISTS selected_candidate;
CREATE VIEW selected_candidate AS
SELECT * FROM rule_assignments
WHERE rule_id = 'community_review' AND selected = 1;

DROP VIEW IF EXISTS dry_run_reconciliation;
CREATE VIEW dry_run_reconciliation AS
SELECT
    s.tract_fips,
    s.allocated_places AS expected_fictional_places,
    COUNT(d.fictional_test_id) AS dry_run_records,
    SUM(d.offer_test_state = 'processed') AS processed_offer_tests,
    SUM(d.offer_test_state = 'held_for_readiness') AS held_for_readiness_tests,
    SUM(d.outcome_available = 'yes') AS outcome_records,
    CASE WHEN COUNT(d.fictional_test_id) = s.allocated_places THEN 'yes' ELSE 'no' END AS reconciled
FROM selected_candidate s
LEFT JOIN monitoring_dry_run d USING (tract_fips)
GROUP BY s.tract_fips, s.allocated_places;

SELECT COUNT(*) AS selected_tracts, SUM(expected_fictional_places) AS fictional_places,
       SUM(dry_run_records) AS dry_run_records, SUM(reconciled = 'yes') AS reconciled_tracts,
       SUM(outcome_records) AS outcome_records
FROM dry_run_reconciliation;

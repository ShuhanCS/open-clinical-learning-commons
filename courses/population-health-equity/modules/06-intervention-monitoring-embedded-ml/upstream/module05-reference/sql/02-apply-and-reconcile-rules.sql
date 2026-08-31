CREATE INDEX IF NOT EXISTS assignment_rule_key ON rule_assignments(rule_id);
CREATE UNIQUE INDEX IF NOT EXISTS assignment_rule_tract_key ON rule_assignments(rule_id, tract_fips);

DROP VIEW IF EXISTS rule_reconciliation;
CREATE VIEW rule_reconciliation AS
SELECT
    rule_id,
    COUNT(*) AS candidate_rows,
    SUM(selected) AS selected_tracts,
    SUM(allocated_places) AS allocated_places,
    COUNT(DISTINCT CASE WHEN selected = 1 THEN county_fips END) AS selected_counties,
    SUM(selected = 1 AND support_state = 'limited_support_review') AS selected_limited_support,
    SUM(selected = 1 AND fictional_capacity_places < 10) AS selected_below_capacity,
    SUM(selected = 1 AND automatic_action != 0) AS automatic_actions
FROM rule_assignments
GROUP BY rule_id;

CREATE INDEX IF NOT EXISTS county_rule_key ON county_concentration(rule_id, county_fips);
CREATE INDEX IF NOT EXISTS group_rule_key ON group_consequences(rule_id, equity_dimension, group_id);
CREATE INDEX IF NOT EXISTS sensitivity_rule_key ON sensitivity_results(rule_id, variant_id);

DROP VIEW IF EXISTS selected_consequence_audit;
CREATE VIEW selected_consequence_audit AS
SELECT
    rule_id,
    SUM(selected) AS selected_tracts,
    SUM(selected = 1 AND fictional_travel_minutes >= 60) AS high_travel,
    SUM(selected = 1 AND fictional_delivery_burden_score >= 4) AS high_burden,
    SUM(selected = 1 AND fictional_language_access_ready = 0) AS language_access_gaps,
    SUM(selected = 1 AND fictional_disability_access_ready = 0) AS disability_access_gaps,
    SUM(selected = 1 AND fictional_objection_state = 'unresolved_objection') AS unresolved_objections
FROM rule_assignments
GROUP BY rule_id;

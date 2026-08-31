DROP VIEW IF EXISTS monitoring_release_audit;
CREATE VIEW monitoring_release_audit AS
SELECT
    COUNT(*) AS measures,
    SUM(denominator > 0) AS measures_with_denominators,
    SUM(result = 'triggered') AS review_triggers,
    SUM(automatic_action != 'no') AS automatic_actions
FROM monitoring_results;

DROP VIEW IF EXISTS incident_release_audit;
CREATE VIEW incident_release_audit AS
SELECT
    SUM(incident_test_state != 'none') AS incidents,
    SUM(incident_test_state != 'none' AND escalation_test_route != 'none') AS incidents_with_routes,
    SUM(objection_test_state != 'none') AS objections,
    SUM(objection_test_state != 'none' AND pause_test_triggered = 'yes') AS paused_objections
FROM monitoring_dry_run;

SELECT * FROM monitoring_release_audit;
SELECT * FROM incident_release_audit;

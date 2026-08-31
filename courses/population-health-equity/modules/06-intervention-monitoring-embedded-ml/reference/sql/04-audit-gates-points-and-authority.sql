DROP VIEW IF EXISTS module06_release_audit;
CREATE VIEW module06_release_audit AS
SELECT
    (SELECT COUNT(*) FROM week6_gate_results) AS gates,
    (SELECT SUM(status = 'pass') FROM week6_gate_results) AS gates_passed,
    (SELECT SUM(status != 'pass') FROM week6_gate_results) AS gate_failures,
    (SELECT SUM(automatic_action != 'no') FROM monitoring_results) AS automatic_monitoring_actions,
    (SELECT SUM(cluster_used_to_change_selection != 'no') FROM cluster_assignments) AS cluster_selection_changes,
    (SELECT SUM(outcome_available = 'yes') FROM monitoring_dry_run) AS outcome_records,
    10 AS module04_points_carried,
    15 AS module05_points_carried,
    0 AS module06_points_added,
    25 AS week6_checkpoint_points;

SELECT *,
       CASE WHEN gates = 34 AND gates_passed = 34 AND gate_failures = 0
                  AND automatic_monitoring_actions = 0 AND cluster_selection_changes = 0
                  AND outcome_records = 0 AND module04_points_carried + module05_points_carried
                      + module06_points_added = week6_checkpoint_points
            THEN 'permit checkpoint construction with no real-world authority'
            ELSE 'stop' END AS progression
FROM module06_release_audit;

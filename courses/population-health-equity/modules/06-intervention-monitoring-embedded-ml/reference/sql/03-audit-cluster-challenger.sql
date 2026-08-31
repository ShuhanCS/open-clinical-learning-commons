CREATE UNIQUE INDEX IF NOT EXISTS cluster_assignment_tract_key ON cluster_assignments(tract_fips);

DROP VIEW IF EXISTS cluster_support_audit;
CREATE VIEW cluster_support_audit AS
SELECT cluster_id, COUNT(*) AS tracts,
       SUM(community_review_selected = 'yes') AS selected_tracts,
       SUM(cluster_used_to_change_selection != 'no') AS changed_selections,
       SUM(automatic_action != 'no') AS automatic_actions
FROM cluster_assignments
GROUP BY cluster_id;

DROP VIEW IF EXISTS challenger_decision;
CREATE VIEW challenger_decision AS
SELECT
    MIN(CASE WHEN variant_type = 'seed' THEN adjusted_rand_vs_base END) AS alternate_seed_minimum_ari,
    MAX(scaling_variant_median_ari) AS scaling_variant_median_ari,
    MIN(challenger_stable_for_bounded_questions) AS accepted_use,
    MIN(challenger_use) AS challenger_use
FROM challenger_stability;

SELECT * FROM cluster_support_audit ORDER BY cluster_id;
SELECT * FROM challenger_decision;
SELECT COUNT(*) AS selected_rows, COUNT(DISTINCT cluster_id) AS selected_clusters,
       SUM(selection_preserved = 'yes') AS preserved_rows
FROM selected_tract_cluster_review;

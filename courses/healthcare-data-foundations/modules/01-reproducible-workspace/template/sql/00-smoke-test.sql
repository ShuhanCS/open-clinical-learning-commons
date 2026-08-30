DROP TABLE IF EXISTS workspace_smoke;

CREATE TABLE workspace_smoke (
    record_id TEXT PRIMARY KEY,
    source_label TEXT NOT NULL,
    event_count INTEGER NOT NULL CHECK (event_count >= 0)
);

SELECT
    COUNT(*) AS row_count,
    SUM(event_count) AS event_count_total,
    MIN(event_count) AS event_count_minimum,
    MAX(event_count) AS event_count_maximum
FROM workspace_smoke;

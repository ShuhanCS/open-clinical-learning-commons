-- Exact cohort facts used to reconcile event, patient, exclusion, and index counts.
WITH acute_period_events AS (
    SELECT
        e.patient AS patient_id,
        e.id AS encounter_id,
        e.start AS encounter_start,
        e.encounterclass,
        CAST(substr(e.start, 1, 4) AS INTEGER)
          - CAST(substr(p.birthdate, 1, 4) AS INTEGER)
          - (substr(e.start, 6, 5) < substr(p.birthdate, 6, 5)) AS age_at_event
    FROM encounters AS e
    JOIN patients AS p ON p.id = e.patient
    WHERE e.encounterclass IN ('emergency', 'inpatient')
      AND e.start >= '2015-01-01T00:00:00Z'
      AND e.start < '2020-01-01T00:00:00Z'
),
eligible_events AS (
    SELECT * FROM acute_period_events WHERE age_at_event >= 18
),
ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY patient_id
            ORDER BY encounter_start, encounter_id
        ) AS event_rank
    FROM eligible_events
),
facts(check_id, check_name, observed_value, expected_value) AS (
    SELECT 1, 'source patients', (SELECT COUNT(*) FROM patients), 1171
    UNION ALL SELECT 2, 'source encounters', (SELECT COUNT(*) FROM encounters), 53346
    UNION ALL SELECT 3, 'acute events in index period', (SELECT COUNT(*) FROM acute_period_events), 1243
    UNION ALL SELECT 4, 'emergency events in index period', (SELECT COUNT(*) FROM acute_period_events WHERE encounterclass = 'emergency'), 687
    UNION ALL SELECT 5, 'inpatient events in index period', (SELECT COUNT(*) FROM acute_period_events WHERE encounterclass = 'inpatient'), 556
    UNION ALL SELECT 6, 'patients with any acute event', (SELECT COUNT(DISTINCT patient_id) FROM acute_period_events), 481
    UNION ALL SELECT 7, 'patients without an acute event', (SELECT COUNT(*) FROM patients) - (SELECT COUNT(DISTINCT patient_id) FROM acute_period_events), 690
    UNION ALL SELECT 8, 'patients with only under-18 acute events', (SELECT COUNT(DISTINCT patient_id) FROM acute_period_events) - (SELECT COUNT(DISTINCT patient_id) FROM eligible_events), 107
    UNION ALL SELECT 9, 'adult eligible events', (SELECT COUNT(*) FROM eligible_events), 1048
    UNION ALL SELECT 10, 'included adult patients', (SELECT COUNT(*) FROM ranked WHERE event_rank = 1), 374
    UNION ALL SELECT 11, 'eligible non-index events', (SELECT COUNT(*) FROM ranked WHERE event_rank > 1), 674
    UNION ALL SELECT 12, 'unique included patients', (SELECT COUNT(DISTINCT patient_id) FROM ranked WHERE event_rank = 1), 374
    UNION ALL SELECT 13, 'unique index encounters', (SELECT COUNT(DISTINCT encounter_id) FROM ranked WHERE event_rank = 1), 374
    UNION ALL SELECT 14, 'emergency index encounters', (SELECT COUNT(*) FROM ranked WHERE event_rank = 1 AND encounterclass = 'emergency'), 314
    UNION ALL SELECT 15, 'inpatient index encounters', (SELECT COUNT(*) FROM ranked WHERE event_rank = 1 AND encounterclass = 'inpatient'), 60
    UNION ALL SELECT 16, 'flow conservation', 690 + 107 + (SELECT COUNT(*) FROM ranked WHERE event_rank = 1), 1171
)
SELECT
    check_id,
    check_name,
    observed_value,
    expected_value,
    CASE WHEN observed_value = expected_value THEN 'pass' ELSE 'fail' END AS status
FROM facts
ORDER BY check_id;

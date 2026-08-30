-- One row per included patient with separate history and follow-up summaries.
WITH eligible_events AS (
    SELECT
        p.id AS patient_id,
        p.birthdate AS birth_date,
        p.deathdate AS death_date,
        p.gender,
        p.race,
        p.ethnicity,
        e.id AS index_encounter_id,
        e.start AS index_start,
        e.stop AS index_stop,
        e.encounterclass AS index_class,
        e.code AS index_code,
        e.description AS index_description,
        e.reasoncode AS index_reason_code,
        e.reasondescription AS index_reason_description,
        CAST(substr(e.start, 1, 4) AS INTEGER)
          - CAST(substr(p.birthdate, 1, 4) AS INTEGER)
          - (substr(e.start, 6, 5) < substr(p.birthdate, 6, 5)) AS age_at_index
    FROM encounters AS e
    JOIN patients AS p ON p.id = e.patient
    WHERE e.encounterclass IN ('emergency', 'inpatient')
      AND e.start >= '2015-01-01T00:00:00Z'
      AND e.start < '2020-01-01T00:00:00Z'
),
ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY patient_id
            ORDER BY index_start, index_encounter_id
        ) AS event_rank
    FROM eligible_events
    WHERE age_at_index >= 18
),
index_cohort AS (
    SELECT *
    FROM ranked
    WHERE event_rank = 1
),
encounter_history AS (
    SELECT
        i.patient_id,
        COUNT(e.id) AS prior_365d_encounter_count,
        SUM(CASE WHEN e.encounterclass IN ('emergency', 'inpatient') THEN 1 ELSE 0 END) AS prior_365d_acute_count
    FROM index_cohort AS i
    LEFT JOIN encounters AS e
      ON e.patient = i.patient_id
     AND julianday(e.start) >= julianday(i.index_start) - 365
     AND julianday(e.start) < julianday(i.index_start)
    GROUP BY i.patient_id
),
condition_history AS (
    SELECT
        i.patient_id,
        COUNT(c.source_row_number) AS prior_365d_condition_count
    FROM index_cohort AS i
    LEFT JOIN conditions AS c
      ON c.patient = i.patient_id
     AND julianday(c.start) >= julianday(i.index_start) - 365
     AND julianday(c.start) < julianday(i.index_start)
    GROUP BY i.patient_id
),
medication_history AS (
    SELECT
        i.patient_id,
        COUNT(m.source_row_number) AS prior_365d_medication_count
    FROM index_cohort AS i
    LEFT JOIN medications AS m
      ON m.patient = i.patient_id
     AND julianday(m.start) >= julianday(i.index_start) - 365
     AND julianday(m.start) < julianday(i.index_start)
    GROUP BY i.patient_id
),
next_encounters AS (
    SELECT
        i.patient_id,
        e.id AS next_encounter_id,
        e.start AS next_start,
        e.encounterclass AS next_class,
        ROW_NUMBER() OVER (
            PARTITION BY i.patient_id
            ORDER BY e.start, e.id
        ) AS next_rank
    FROM index_cohort AS i
    JOIN encounters AS e
      ON e.patient = i.patient_id
     AND e.id <> i.index_encounter_id
     AND julianday(e.start) > julianday(i.index_stop)
     AND julianday(e.start) <= julianday(i.index_stop) + 30
),
first_next AS (
    SELECT patient_id, next_encounter_id, next_start, next_class
    FROM next_encounters
    WHERE next_rank = 1
),
acute_returns AS (
    SELECT
        i.patient_id,
        MAX(CASE WHEN e.id IS NOT NULL THEN 1 ELSE 0 END) AS acute_return_90d
    FROM index_cohort AS i
    LEFT JOIN encounters AS e
      ON e.patient = i.patient_id
     AND e.id <> i.index_encounter_id
     AND e.encounterclass IN ('emergency', 'inpatient')
     AND julianday(e.start) > julianday(i.index_stop)
     AND julianday(e.start) <= julianday(i.index_stop) + 90
    GROUP BY i.patient_id
),
source_coverage AS (
    SELECT MAX(julianday(start)) AS maximum_encounter_day
    FROM encounters
)
SELECT
    i.patient_id,
    i.birth_date,
    i.death_date,
    i.age_at_index,
    i.gender,
    i.race,
    i.ethnicity,
    i.index_encounter_id,
    i.index_start,
    i.index_stop,
    i.index_class,
    i.index_code,
    i.index_description,
    i.index_reason_code,
    i.index_reason_description,
    h.prior_365d_encounter_count,
    h.prior_365d_acute_count,
    c.prior_365d_condition_count,
    m.prior_365d_medication_count,
    CASE
        WHEN n.next_encounter_id IS NULL THEN 'No encounter recorded'
        WHEN n.next_class IN ('ambulatory', 'outpatient', 'wellness') THEN 'Scheduled care'
        WHEN n.next_class = 'urgentcare' THEN 'Urgent care'
        WHEN n.next_class IN ('emergency', 'inpatient') THEN 'Acute return'
        ELSE 'Other recorded encounter'
    END AS next_30d_state,
    n.next_encounter_id AS next_30d_encounter_id,
    n.next_start AS next_30d_start,
    CASE
        WHEN n.next_start IS NULL THEN NULL
        ELSE ROUND(julianday(n.next_start) - julianday(i.index_stop), 6)
    END AS next_30d_days_after_index_stop,
    a.acute_return_90d,
    CASE
        WHEN i.death_date IS NOT NULL
         AND julianday(i.death_date) > julianday(i.index_stop)
         AND julianday(i.death_date) <= julianday(i.index_stop) + 90
        THEN 1 ELSE 0
    END AS death_90d,
    CASE
        WHEN i.death_date IS NOT NULL
         AND julianday(i.death_date) > julianday(i.index_stop)
         AND julianday(i.death_date) <= julianday(i.index_stop) + 90
        THEN 'Death'
        WHEN a.acute_return_90d = 1 THEN 'Acute return'
        ELSE 'No acute return recorded'
    END AS endpoint_90d,
    CASE WHEN s.maximum_encounter_day >= julianday(i.index_stop) + 90 THEN 1 ELSE 0 END AS followup_90d_complete,
    'synthea-csv-apr2020' AS source_release,
    '0.1.0' AS cohort_definition_version
FROM index_cohort AS i
JOIN encounter_history AS h ON h.patient_id = i.patient_id
JOIN condition_history AS c ON c.patient_id = i.patient_id
JOIN medication_history AS m ON m.patient_id = i.patient_id
LEFT JOIN first_next AS n ON n.patient_id = i.patient_id
JOIN acute_returns AS a ON a.patient_id = i.patient_id
CROSS JOIN source_coverage AS s
ORDER BY i.patient_id;

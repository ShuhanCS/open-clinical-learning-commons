-- One deterministic first eligible acute event per adult patient.
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
)
SELECT
    patient_id,
    birth_date,
    death_date,
    age_at_index,
    gender,
    race,
    ethnicity,
    index_encounter_id,
    index_start,
    index_stop,
    index_class,
    index_code,
    index_description,
    index_reason_code,
    index_reason_description
FROM ranked
WHERE event_rank = 1
ORDER BY patient_id;

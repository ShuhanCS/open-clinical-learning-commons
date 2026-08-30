-- Adult emergency and inpatient events in the declared index period.
WITH acute_period_events AS (
    SELECT
        p.id AS patient_id,
        p.birthdate AS birth_date,
        p.deathdate AS death_date,
        p.gender,
        p.race,
        p.ethnicity,
        e.id AS eligible_encounter_id,
        e.start AS eligible_start,
        e.stop AS eligible_stop,
        e.encounterclass AS eligible_class,
        e.code AS eligible_code,
        e.description AS eligible_description,
        e.reasoncode AS eligible_reason_code,
        e.reasondescription AS eligible_reason_description,
        CAST(substr(e.start, 1, 4) AS INTEGER)
          - CAST(substr(p.birthdate, 1, 4) AS INTEGER)
          - (substr(e.start, 6, 5) < substr(p.birthdate, 6, 5)) AS age_at_event
    FROM encounters AS e
    JOIN patients AS p ON p.id = e.patient
    WHERE e.encounterclass IN ('emergency', 'inpatient')
      AND e.start >= '2015-01-01T00:00:00Z'
      AND e.start < '2020-01-01T00:00:00Z'
)
SELECT
    patient_id,
    birth_date,
    death_date,
    age_at_event,
    gender,
    race,
    ethnicity,
    eligible_encounter_id,
    eligible_start,
    eligible_stop,
    eligible_class,
    eligible_code,
    eligible_description,
    eligible_reason_code,
    eligible_reason_description
FROM acute_period_events
WHERE age_at_event >= 18
ORDER BY patient_id, eligible_start, eligible_encounter_id;

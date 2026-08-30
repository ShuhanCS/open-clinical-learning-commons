-- APP-1 Module 02: every source event relevant to index, exposure, branches, and outcome.
WITH eligible AS (
  SELECT
    e.*,
    p.birthdate,
    p.deathdate,
    CAST(strftime('%Y', e.start) AS INTEGER)
      - CAST(strftime('%Y', p.birthdate) AS INTEGER)
      - CASE WHEN strftime('%m-%d', e.start) < strftime('%m-%d', p.birthdate) THEN 1 ELSE 0 END AS age_at_index
  FROM encounters e
  JOIN patients p ON p.id = e.patient
  WHERE e.encounterclass IN ('emergency', 'inpatient')
    AND e.start >= '2010-01-01T00:00:00Z'
    AND e.start < '2019-04-01T00:00:00Z'
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY patient ORDER BY start, id) AS index_rank
  FROM eligible
  WHERE age_at_index >= 18
), cohort AS (
  SELECT * FROM ranked WHERE index_rank = 1
), classified_encounters AS (
  SELECT
    c.patient AS patient_id,
    CASE
      WHEN julianday(e.start) <= julianday(c.stop) + 30
        AND e.encounterclass IN ('ambulatory', 'outpatient', 'wellness') THEN 'scheduled_followup'
      WHEN julianday(e.start) <= julianday(c.stop) + 30
        AND e.encounterclass IN ('emergency', 'inpatient') THEN 'early_acute_return'
      ELSE 'later_acute_return'
    END AS event_role,
    e.id AS event_id,
    e.start AS event_start,
    e.stop AS event_stop,
    e.encounterclass,
    ROUND(julianday(e.start) - julianday(c.stop), 8) AS days_from_discharge,
    'timestamp' AS timing_precision,
    'encounters' AS source_table
  FROM cohort c
  JOIN encounters e ON e.patient = c.patient
  WHERE julianday(e.start) > julianday(c.stop)
    AND julianday(e.start) <= julianday(c.stop) + 365
    AND (
      (julianday(e.start) <= julianday(c.stop) + 30
        AND e.encounterclass IN ('ambulatory', 'outpatient', 'wellness', 'emergency', 'inpatient'))
      OR
      (julianday(e.start) > julianday(c.stop) + 30
        AND e.encounterclass IN ('emergency', 'inpatient'))
    )
), ranked_encounters AS (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY patient_id, event_role ORDER BY event_start, event_id) AS role_rank
  FROM classified_encounters
), audit AS (
  SELECT
    patient AS patient_id,
    'index_encounter' AS event_role,
    id AS event_id,
    start AS event_start,
    stop AS event_stop,
    encounterclass,
    0.0 AS days_from_discharge,
    'timestamp' AS timing_precision,
    'encounters' AS source_table,
    1 AS selected_for_analysis,
    'first eligible adult acute encounter' AS selection_rule
  FROM cohort
  UNION ALL
  SELECT
    patient_id,
    event_role,
    event_id,
    event_start,
    event_stop,
    encounterclass,
    days_from_discharge,
    timing_precision,
    source_table,
    CASE WHEN role_rank = 1 THEN 1 ELSE 0 END,
    CASE WHEN role_rank = 1 THEN 'first event in role window' ELSE 'retained audit event after first' END
  FROM ranked_encounters
  UNION ALL
  SELECT
    patient AS patient_id,
    CASE
      WHEN date(deathdate) <= date(stop) THEN 'index_death'
      WHEN date(deathdate) <= date(stop, '+30 day') THEN 'early_death'
      ELSE 'later_death'
    END AS event_role,
    'death:' || patient AS event_id,
    deathdate AS event_start,
    '' AS event_stop,
    '' AS encounterclass,
    ROUND(julianday(date(deathdate)) - julianday(date(stop)), 8) AS days_from_discharge,
    'date' AS timing_precision,
    'patients' AS source_table,
    1 AS selected_for_analysis,
    'only recorded death date' AS selection_rule
  FROM cohort
  WHERE deathdate IS NOT NULL
    AND date(deathdate) <= date(stop, '+365 day')
)
SELECT * FROM audit
ORDER BY patient_id, event_start, event_role, event_id;

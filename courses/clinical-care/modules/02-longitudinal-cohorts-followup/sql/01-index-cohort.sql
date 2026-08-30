-- APP-1 Module 02: one deterministic adult acute-care index per synthetic person.
WITH eligible AS (
  SELECT
    e.id,
    e.start,
    e.stop,
    e.patient,
    e.organization,
    e.encounterclass,
    p.birthdate,
    p.deathdate,
    p.gender,
    p.race,
    p.ethnicity,
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
)
SELECT
  patient AS patient_id,
  id AS index_encounter_id,
  start AS index_start,
  stop AS index_stop,
  encounterclass AS index_encounter_class,
  organization AS source_organization_id,
  age_at_index,
  gender,
  race,
  ethnicity,
  (
    SELECT COUNT(*) FROM encounters h
    WHERE h.patient = ranked.patient
      AND julianday(h.start) >= julianday(ranked.start) - 365
      AND julianday(h.start) < julianday(ranked.start)
  ) AS prior_365d_encounter_count,
  (
    SELECT COUNT(*) FROM encounters h
    WHERE h.patient = ranked.patient
      AND h.encounterclass IN ('emergency', 'inpatient')
      AND julianday(h.start) >= julianday(ranked.start) - 365
      AND julianday(h.start) < julianday(ranked.start)
  ) AS prior_365d_acute_count,
  (
    SELECT COUNT(*) FROM conditions c
    WHERE c.patient = ranked.patient
      AND julianday(c.start) >= julianday(ranked.start) - 365
      AND julianday(c.start) < julianday(ranked.start)
  ) AS prior_365d_condition_count,
  (SELECT COUNT(*) FROM conditions c WHERE c.encounter = ranked.id) AS index_condition_count,
  (SELECT COUNT(*) FROM procedures p WHERE p.encounter = ranked.id) AS index_procedure_count
FROM ranked
WHERE index_rank = 1
ORDER BY patient_id;

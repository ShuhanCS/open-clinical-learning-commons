-- APP-1 Module 02: one longitudinal record for every initial synthetic person.
WITH eligible AS (
  SELECT
    e.*,
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
), cohort AS (
  SELECT * FROM ranked WHERE index_rank = 1
), timed AS (
  SELECT
    c.*,
    (SELECT COUNT(*) FROM encounters h WHERE h.patient = c.patient AND julianday(h.start) >= julianday(c.start) - 365 AND julianday(h.start) < julianday(c.start)) AS prior_365d_encounter_count,
    (SELECT COUNT(*) FROM encounters h WHERE h.patient = c.patient AND h.encounterclass IN ('emergency', 'inpatient') AND julianday(h.start) >= julianday(c.start) - 365 AND julianday(h.start) < julianday(c.start)) AS prior_365d_acute_count,
    (SELECT COUNT(*) FROM conditions d WHERE d.patient = c.patient AND julianday(d.start) >= julianday(c.start) - 365 AND julianday(d.start) < julianday(c.start)) AS prior_365d_condition_count,
    CASE WHEN c.deathdate IS NOT NULL AND date(c.deathdate) <= date(c.stop) THEN 1 ELSE 0 END AS index_death_flag,
    CASE WHEN c.deathdate IS NOT NULL AND date(c.deathdate) > date(c.stop) AND date(c.deathdate) <= date(c.stop, '+30 day') THEN 1 ELSE 0 END AS early_death_flag,
    (SELECT a.id FROM encounters a WHERE a.patient = c.patient AND julianday(a.start) > julianday(c.stop) AND julianday(a.start) <= julianday(c.stop) + 30 AND a.encounterclass IN ('emergency', 'inpatient') ORDER BY a.start, a.id LIMIT 1) AS first_early_acute_id,
    (SELECT a.start FROM encounters a WHERE a.patient = c.patient AND julianday(a.start) > julianday(c.stop) AND julianday(a.start) <= julianday(c.stop) + 30 AND a.encounterclass IN ('emergency', 'inpatient') ORDER BY a.start, a.id LIMIT 1) AS first_early_acute_start,
    (SELECT f.id FROM encounters f WHERE f.patient = c.patient AND julianday(f.start) > julianday(c.stop) AND julianday(f.start) <= julianday(c.stop) + 30 AND f.encounterclass IN ('ambulatory', 'outpatient', 'wellness') ORDER BY f.start, f.id LIMIT 1) AS first_followup_id,
    (SELECT f.start FROM encounters f WHERE f.patient = c.patient AND julianday(f.start) > julianday(c.stop) AND julianday(f.start) <= julianday(c.stop) + 30 AND f.encounterclass IN ('ambulatory', 'outpatient', 'wellness') ORDER BY f.start, f.id LIMIT 1) AS first_followup_start,
    (SELECT a.id FROM encounters a WHERE a.patient = c.patient AND julianday(a.start) > julianday(c.stop) + 30 AND julianday(a.start) <= julianday(c.stop) + 365 AND a.encounterclass IN ('emergency', 'inpatient') ORDER BY a.start, a.id LIMIT 1) AS first_later_acute_id,
    (SELECT a.start FROM encounters a WHERE a.patient = c.patient AND julianday(a.start) > julianday(c.stop) + 30 AND julianday(a.start) <= julianday(c.stop) + 365 AND a.encounterclass IN ('emergency', 'inpatient') ORDER BY a.start, a.id LIMIT 1) AS first_later_acute_start
  FROM cohort c
), classified AS (
  SELECT *,
    CASE WHEN first_early_acute_id IS NOT NULL THEN 1 ELSE 0 END AS early_acute_return_flag,
    CASE WHEN first_followup_id IS NOT NULL THEN 1 ELSE 0 END AS scheduled_followup_flag,
    CASE WHEN index_death_flag = 0 AND early_death_flag = 0 AND first_early_acute_id IS NULL THEN 1 ELSE 0 END AS landmark_eligible_flag,
    CASE
      WHEN index_death_flag = 1 THEN 'index_death'
      WHEN early_death_flag = 1 THEN 'early_death'
      WHEN first_early_acute_id IS NOT NULL THEN 'early_acute_return'
      ELSE ''
    END AS landmark_exclusion_reason,
    CASE WHEN deathdate IS NOT NULL AND date(deathdate) > date(stop, '+30 day') AND date(deathdate) <= date(stop, '+365 day') THEN 1 ELSE 0 END AS later_death_flag,
    CASE WHEN deathdate IS NOT NULL AND date(deathdate) > date(stop, '+30 day') AND date(deathdate) <= date(stop, '+365 day') AND (first_later_acute_start IS NULL OR julianday(date(deathdate)) <= julianday(first_later_acute_start)) THEN 1 ELSE 0 END AS later_death_before_event_flag
  FROM timed
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
  prior_365d_encounter_count,
  prior_365d_acute_count,
  prior_365d_condition_count,
  index_death_flag,
  CASE WHEN index_death_flag = 1 THEN deathdate ELSE '' END AS index_death_date,
  early_death_flag,
  CASE WHEN early_death_flag = 1 THEN deathdate ELSE '' END AS early_death_date,
  early_acute_return_flag,
  COALESCE(first_early_acute_id, '') AS first_early_acute_id,
  COALESCE(first_early_acute_start, '') AS first_early_acute_start,
  CASE WHEN first_early_acute_start IS NOT NULL THEN ROUND(julianday(first_early_acute_start) - julianday(stop), 8) ELSE '' END AS first_early_acute_days,
  scheduled_followup_flag,
  COALESCE(first_followup_id, '') AS first_followup_id,
  COALESCE(first_followup_start, '') AS first_followup_start,
  CASE WHEN first_followup_start IS NOT NULL THEN ROUND(julianday(first_followup_start) - julianday(stop), 8) ELSE '' END AS first_followup_days,
  landmark_eligible_flag,
  landmark_exclusion_reason,
  CASE WHEN landmark_eligible_flag = 1 THEN strftime('%Y-%m-%dT%H:%M:%SZ', datetime(stop, '+30 day')) ELSE '' END AS landmark_datetime,
  CASE WHEN landmark_eligible_flag = 1 THEN scheduled_followup_flag ELSE '' END AS landmark_exposure,
  CASE WHEN landmark_eligible_flag = 1 AND first_later_acute_start IS NOT NULL AND later_death_before_event_flag = 0 THEN 1 ELSE 0 END AS later_acute_return_flag,
  CASE WHEN landmark_eligible_flag = 1 AND first_later_acute_start IS NOT NULL AND later_death_before_event_flag = 0 THEN first_later_acute_id ELSE '' END AS first_later_acute_id,
  CASE WHEN landmark_eligible_flag = 1 AND first_later_acute_start IS NOT NULL AND later_death_before_event_flag = 0 THEN first_later_acute_start ELSE '' END AS first_later_acute_start,
  CASE WHEN landmark_eligible_flag = 1 AND first_later_acute_start IS NOT NULL AND later_death_before_event_flag = 0 THEN ROUND(julianday(first_later_acute_start) - julianday(stop), 8) ELSE '' END AS first_later_acute_days_from_discharge,
  later_death_flag,
  CASE WHEN later_death_flag = 1 THEN deathdate ELSE '' END AS later_death_date,
  later_death_before_event_flag,
  CASE WHEN landmark_eligible_flag = 1 AND first_later_acute_start IS NOT NULL AND later_death_before_event_flag = 0 THEN 1 ELSE 0 END AS event_indicator,
  CASE
    WHEN landmark_eligible_flag = 0 THEN ''
    WHEN later_death_before_event_flag = 1 THEN ROUND(julianday(date(deathdate)) - julianday(stop) - 30, 8)
    WHEN first_later_acute_start IS NOT NULL THEN ROUND(julianday(first_later_acute_start) - julianday(stop) - 30, 8)
    ELSE 335.0
  END AS observed_time_days,
  CASE
    WHEN landmark_eligible_flag = 0 THEN ''
    WHEN later_death_before_event_flag = 1 THEN 'competing_death'
    WHEN first_later_acute_start IS NOT NULL THEN 'event'
    ELSE 'administrative_end'
  END AS censor_reason,
  strftime('%Y-%m-%dT%H:%M:%SZ', datetime(stop, '+365 day')) AS administrative_end_datetime
FROM classified
ORDER BY patient_id;

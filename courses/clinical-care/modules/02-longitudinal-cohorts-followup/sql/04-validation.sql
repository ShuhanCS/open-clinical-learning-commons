-- APP-1 Module 02: exact source, cohort, timing, and conservation checks.
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
), pathway AS (
  SELECT
    c.*,
    CASE WHEN c.deathdate IS NOT NULL AND date(c.deathdate) <= date(c.stop) THEN 1 ELSE 0 END AS index_death,
    CASE WHEN c.deathdate IS NOT NULL AND date(c.deathdate) > date(c.stop) AND date(c.deathdate) <= date(c.stop, '+30 day') THEN 1 ELSE 0 END AS early_death,
    (SELECT a.start FROM encounters a WHERE a.patient = c.patient AND julianday(a.start) > julianday(c.stop) AND julianday(a.start) <= julianday(c.stop) + 30 AND a.encounterclass IN ('emergency', 'inpatient') ORDER BY a.start, a.id LIMIT 1) AS early_acute_start,
    (SELECT f.start FROM encounters f WHERE f.patient = c.patient AND julianday(f.start) > julianday(c.stop) AND julianday(f.start) <= julianday(c.stop) + 30 AND f.encounterclass IN ('ambulatory', 'outpatient', 'wellness') ORDER BY f.start, f.id LIMIT 1) AS followup_start,
    (SELECT a.start FROM encounters a WHERE a.patient = c.patient AND julianday(a.start) > julianday(c.stop) + 30 AND julianday(a.start) <= julianday(c.stop) + 365 AND a.encounterclass IN ('emergency', 'inpatient') ORDER BY a.start, a.id LIMIT 1) AS later_acute_start
  FROM cohort c
), classified AS (
  SELECT *,
    CASE WHEN early_acute_start IS NOT NULL THEN 1 ELSE 0 END AS early_acute,
    CASE WHEN followup_start IS NOT NULL THEN 1 ELSE 0 END AS followup,
    CASE WHEN index_death = 0 AND early_death = 0 AND early_acute_start IS NULL THEN 1 ELSE 0 END AS landmark_eligible,
    CASE WHEN deathdate IS NOT NULL AND date(deathdate) > date(stop, '+30 day') AND date(deathdate) <= date(stop, '+365 day') THEN 1 ELSE 0 END AS later_death,
    CASE WHEN deathdate IS NOT NULL AND date(deathdate) > date(stop, '+30 day') AND date(deathdate) <= date(stop, '+365 day') AND (later_acute_start IS NULL OR julianday(date(deathdate)) <= julianday(later_acute_start)) THEN 1 ELSE 0 END AS later_death_before_event
  FROM pathway
), facts AS (
  SELECT 'source people' AS check_name, (SELECT COUNT(*) FROM patients) AS observed_value
  UNION ALL SELECT 'source encounters', (SELECT COUNT(*) FROM encounters)
  UNION ALL SELECT 'initial cohort', COUNT(*) FROM classified
  UNION ALL SELECT 'unique initial patients', COUNT(DISTINCT patient) FROM classified
  UNION ALL SELECT 'index emergency', SUM(encounterclass = 'emergency') FROM classified
  UNION ALL SELECT 'index inpatient', SUM(encounterclass = 'inpatient') FROM classified
  UNION ALL SELECT 'index deaths', SUM(index_death) FROM classified
  UNION ALL SELECT 'early deaths', SUM(early_death) FROM classified
  UNION ALL SELECT 'early acute returns', SUM(early_acute) FROM classified
  UNION ALL SELECT 'branch overlaps', SUM((index_death + early_death + early_acute) > 1) FROM classified
  UNION ALL SELECT 'landmark eligible', SUM(landmark_eligible) FROM classified
  UNION ALL SELECT 'scheduled followup', SUM(CASE WHEN landmark_eligible = 1 THEN followup ELSE 0 END) FROM classified
  UNION ALL SELECT 'no scheduled followup', SUM(CASE WHEN landmark_eligible = 1 THEN 1 - followup ELSE 0 END) FROM classified
  UNION ALL SELECT 'later acute returns', SUM(CASE WHEN landmark_eligible = 1 AND later_acute_start IS NOT NULL AND later_death_before_event = 0 THEN 1 ELSE 0 END) FROM classified
  UNION ALL SELECT 'exposed later acute returns', SUM(CASE WHEN landmark_eligible = 1 AND followup = 1 AND later_acute_start IS NOT NULL AND later_death_before_event = 0 THEN 1 ELSE 0 END) FROM classified
  UNION ALL SELECT 'unexposed later acute returns', SUM(CASE WHEN landmark_eligible = 1 AND followup = 0 AND later_acute_start IS NOT NULL AND later_death_before_event = 0 THEN 1 ELSE 0 END) FROM classified
  UNION ALL SELECT 'administrative censored', SUM(CASE WHEN landmark_eligible = 1 AND later_acute_start IS NULL AND later_death_before_event = 0 THEN 1 ELSE 0 END) FROM classified
  UNION ALL SELECT 'competing death censored', SUM(CASE WHEN landmark_eligible = 1 AND later_death_before_event = 1 THEN 1 ELSE 0 END) FROM classified
  UNION ALL SELECT 'later deaths recognized', SUM(CASE WHEN landmark_eligible = 1 THEN later_death ELSE 0 END) FROM classified
  UNION ALL SELECT 'source organizations', COUNT(DISTINCT CASE WHEN landmark_eligible = 1 THEN organization END) FROM classified
  UNION ALL SELECT 'invalid index order', SUM(julianday(stop) < julianday(start)) FROM classified
  UNION ALL SELECT 'invalid followup time', SUM(followup_start IS NOT NULL AND (julianday(followup_start) <= julianday(stop) OR julianday(followup_start) > julianday(stop) + 30)) FROM classified
  UNION ALL SELECT 'invalid early acute time', SUM(early_acute_start IS NOT NULL AND (julianday(early_acute_start) <= julianday(stop) OR julianday(early_acute_start) > julianday(stop) + 30)) FROM classified
  UNION ALL SELECT 'invalid later acute time', SUM(later_acute_start IS NOT NULL AND (julianday(later_acute_start) <= julianday(stop) + 30 OR julianday(later_acute_start) > julianday(stop) + 365)) FROM classified
  UNION ALL SELECT 'landmark conservation', SUM(index_death) + SUM(early_death) + SUM(early_acute) + SUM(landmark_eligible) FROM classified
  UNION ALL SELECT 'outcome conservation', SUM(CASE WHEN landmark_eligible = 1 AND later_acute_start IS NOT NULL AND later_death_before_event = 0 THEN 1 ELSE 0 END) + SUM(CASE WHEN landmark_eligible = 1 AND later_acute_start IS NULL AND later_death_before_event = 0 THEN 1 ELSE 0 END) + SUM(CASE WHEN landmark_eligible = 1 AND later_death_before_event = 1 THEN 1 ELSE 0 END) FROM classified
)
SELECT check_name, observed_value FROM facts ORDER BY check_name;

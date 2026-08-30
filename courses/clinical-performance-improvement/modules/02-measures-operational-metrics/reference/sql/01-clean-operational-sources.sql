CREATE INDEX IF NOT EXISTS raw_process_event_id_idx ON raw_process_events(event_id);
CREATE INDEX IF NOT EXISTS raw_process_encounter_type_idx ON raw_process_events(encounter_id, event_type);
CREATE INDEX IF NOT EXISTS raw_encounter_id_idx ON raw_encounters(encounter_id);
CREATE INDEX IF NOT EXISTS raw_safety_candidate_idx ON raw_safety_events(candidate_id);

DROP TABLE IF EXISTS event_dedup;
CREATE TABLE event_dedup AS
SELECT event_id, encounter_id, service_id, event_type, event_at,
       CAST(event_sequence AS INTEGER) AS event_sequence,
       source_row_status, defect_flag, CAST(synthetic_flag AS INTEGER) AS synthetic_flag
FROM raw_process_events AS source
WHERE rowid = (
  SELECT MIN(candidate.rowid)
  FROM raw_process_events AS candidate
  WHERE candidate.event_id = source.event_id
);

CREATE INDEX IF NOT EXISTS event_dedup_encounter_type_idx ON event_dedup(encounter_id, event_type);

DROP TABLE IF EXISTS event_repaired;
CREATE TABLE event_repaired AS
SELECT event_id, encounter_id, service_id, event_type,
       CASE
         WHEN defect_flag = 'D007' AND event_type = 'triage' THEN (
           SELECT roomed.event_at FROM event_dedup AS roomed
           WHERE roomed.encounter_id = event_dedup.encounter_id AND roomed.event_type = 'roomed'
         )
         WHEN defect_flag = 'D007' AND event_type = 'roomed' THEN (
           SELECT triage.event_at FROM event_dedup AS triage
           WHERE triage.encounter_id = event_dedup.encounter_id AND triage.event_type = 'triage'
         )
         ELSE event_at
       END AS event_at,
       event_sequence, source_row_status, defect_flag, synthetic_flag
FROM event_dedup;

CREATE INDEX IF NOT EXISTS event_repaired_encounter_type_idx ON event_repaired(encounter_id, event_type);

DROP TABLE IF EXISTS encounter_dedup;
CREATE TABLE encounter_dedup AS
SELECT *
FROM raw_encounters AS source
WHERE rowid = (
  SELECT MIN(candidate.rowid)
  FROM raw_encounters AS candidate
  WHERE candidate.encounter_id = source.encounter_id
);

DROP TABLE IF EXISTS clean_encounters;
CREATE TABLE clean_encounters AS
WITH event_clock AS (
  SELECT encounter_id,
         MAX(CASE WHEN event_type = 'arrival' THEN event_at END) AS event_arrival_at,
         MAX(CASE WHEN event_type = 'departure' THEN event_at END) AS event_departure_at
  FROM event_repaired
  GROUP BY encounter_id
), repaired AS (
  SELECT encounter.encounter_id, encounter.person_id, encounter.service_id,
         encounter.arrival_shift_id,
         COALESCE(NULLIF(encounter.arrival_at, ''), event_clock.event_arrival_at) AS arrival_at,
         CAST(encounter.age_years AS INTEGER) AS age_years,
         CAST(encounter.acuity AS INTEGER) AS acuity,
         encounter.arrival_mode, encounter.access_support_group, encounter.disposition,
         CASE
           WHEN encounter.departure_at = '' OR julianday(encounter.departure_at) < julianday(COALESCE(NULLIF(encounter.arrival_at, ''), event_clock.event_arrival_at))
             THEN event_clock.event_departure_at
           ELSE encounter.departure_at
         END AS departure_at,
         CAST(encounter.left_before_seen_flag AS INTEGER) AS left_before_seen_flag,
         encounter.return_to_encounter_id,
         CAST(encounter.return_within_72h_flag AS INTEGER) AS return_within_72h_flag,
         encounter.source_row_status, encounter.defect_flag,
         CAST(encounter.synthetic_flag AS INTEGER) AS synthetic_flag
  FROM encounter_dedup AS encounter
  LEFT JOIN event_clock USING (encounter_id)
)
SELECT *
FROM repaired
WHERE service_id = 'CGH-ED-01'
  AND age_years >= 18
  AND arrival_at IS NOT NULL AND arrival_at <> ''
  AND departure_at IS NOT NULL AND departure_at <> ''
  AND julianday(departure_at) >= julianday(arrival_at);

CREATE UNIQUE INDEX IF NOT EXISTS clean_encounter_id_idx ON clean_encounters(encounter_id);

DROP TABLE IF EXISTS clean_process_events;
CREATE TABLE clean_process_events AS
SELECT event.*
FROM event_repaired AS event
JOIN clean_encounters USING (encounter_id)
WHERE event.service_id = 'CGH-ED-01';

CREATE UNIQUE INDEX IF NOT EXISTS clean_process_event_id_idx ON clean_process_events(event_id);
CREATE INDEX IF NOT EXISTS clean_process_encounter_type_idx ON clean_process_events(encounter_id, event_type);

DROP TABLE IF EXISTS clean_staffing;
CREATE TABLE clean_staffing AS
SELECT staffing_id, service_id, shift_id, shift_start, role,
       CAST(scheduled_count AS INTEGER) AS scheduled_count,
       CAST(actual_count AS INTEGER) AS actual_count,
       CAST(shift_hours AS REAL) AS shift_hours,
       CAST(scheduled_staff_hours AS REAL) AS scheduled_staff_hours,
       CASE
         WHEN defect_flag = 'D010' THEN CAST(actual_count AS REAL) * CAST(shift_hours AS REAL) + CAST(overtime_hours AS REAL)
         ELSE CAST(actual_staff_hours AS REAL)
       END AS actual_staff_hours,
       CAST(overtime_hours AS REAL) AS overtime_hours,
       CAST(absence_hours AS REAL) AS absence_hours,
       source_row_status, defect_flag, CAST(synthetic_flag AS INTEGER) AS synthetic_flag
FROM raw_staffing
WHERE service_id = 'CGH-ED-01';

DROP TABLE IF EXISTS clean_queue_snapshots;
CREATE TABLE clean_queue_snapshots AS
SELECT snapshot_id, service_id, interval_start, interval_end, shift_id,
       CAST(queue_start AS INTEGER) AS queue_start,
       CAST(arrivals AS INTEGER) AS arrivals,
       CAST(service_starts AS INTEGER) AS service_starts,
       CAST(exits_without_service AS INTEGER) AS exits_without_service,
       CAST(queue_start AS INTEGER) + CAST(arrivals AS INTEGER) - CAST(service_starts AS INTEGER) - CAST(exits_without_service AS INTEGER) AS queue_end,
       CAST(clinician_count AS INTEGER) AS clinician_count,
       CAST(staffed_clinician_hours_interval AS REAL) AS staffed_clinician_hours_interval,
       CAST(occupancy_proxy AS REAL) AS occupancy_proxy,
       source_row_status, defect_flag, CAST(synthetic_flag AS INTEGER) AS synthetic_flag
FROM raw_queue_snapshots
WHERE service_id = 'CGH-ED-01';

DROP TABLE IF EXISTS clean_safety_events;
CREATE TABLE clean_safety_events AS
SELECT candidate_id, candidate.encounter_id, candidate.service_id, candidate.event_at,
       candidate.event_class, CAST(candidate.known_true_event_flag AS INTEGER) AS known_true_event_flag,
       CAST(candidate.trigger_flag AS INTEGER) AS trigger_flag,
       CAST(candidate.incident_report_flag AS INTEGER) AS incident_report_flag,
       candidate.review_status, candidate.severity, candidate.source_row_status,
       candidate.defect_flag, CAST(candidate.synthetic_flag AS INTEGER) AS synthetic_flag
FROM raw_safety_events AS candidate
JOIN clean_encounters USING (encounter_id)
WHERE candidate.rowid = (
  SELECT MIN(other.rowid)
  FROM raw_safety_events AS other
  WHERE other.candidate_id = candidate.candidate_id
)
  AND candidate.service_id = 'CGH-ED-01';

DROP TABLE IF EXISTS clean_calendar_demand;
CREATE TABLE clean_calendar_demand AS
WITH accepted_arrivals AS (
  SELECT arrival_shift_id AS shift_id, COUNT(*) AS arrival_count
  FROM clean_encounters
  GROUP BY arrival_shift_id
)
SELECT calendar.shift_id, calendar.date, calendar.shift_name, calendar.shift_start,
       calendar.day_of_week, CAST(calendar.week_index AS INTEGER) AS week_index,
       calendar.season, CAST(calendar.holiday_flag AS INTEGER) AS holiday_flag,
       CAST(calendar.synthetic_special_event_flag AS INTEGER) AS synthetic_special_event_flag,
       COALESCE(accepted_arrivals.arrival_count, 0) AS arrival_count,
       calendar.source_row_status, calendar.defect_flag,
       CAST(calendar.synthetic_flag AS INTEGER) AS synthetic_flag
FROM raw_calendar_demand AS calendar
LEFT JOIN accepted_arrivals USING (shift_id);

DROP TABLE IF EXISTS clean_scenarios;
CREATE TABLE clean_scenarios AS SELECT * FROM raw_scenarios WHERE synthetic_flag = '1';
DROP TABLE IF EXISTS clean_known_truth;
CREATE TABLE clean_known_truth AS SELECT * FROM raw_known_truth WHERE synthetic_flag = '1';
DROP TABLE IF EXISTS clean_defect_register;
CREATE TABLE clean_defect_register AS SELECT * FROM raw_defect_register WHERE synthetic_flag = '1';

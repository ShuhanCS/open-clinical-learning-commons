DROP TABLE IF EXISTS encounter_measures;
CREATE TABLE encounter_measures AS
WITH event_pivot AS (
  SELECT encounter_id,
         MAX(CASE WHEN event_type = 'arrival' THEN event_at END) AS arrival_event_at,
         MAX(CASE WHEN event_type = 'triage' THEN event_at END) AS triage_at,
         MAX(CASE WHEN event_type = 'roomed' THEN event_at END) AS roomed_at,
         MAX(CASE WHEN event_type = 'clinician' THEN event_at END) AS clinician_at,
         MAX(CASE WHEN event_type = 'disposition' THEN event_at END) AS disposition_at,
         MAX(CASE WHEN event_type = 'departure' THEN event_at END) AS departure_event_at,
         COUNT(*) AS recorded_event_count
  FROM clean_process_events
  GROUP BY encounter_id
)
SELECT encounter.encounter_id, encounter.person_id, encounter.service_id,
       encounter.arrival_shift_id, calendar.date AS arrival_date,
       calendar.shift_name, calendar.week_index, encounter.arrival_at,
       event_pivot.triage_at, event_pivot.roomed_at, event_pivot.clinician_at,
       event_pivot.disposition_at, encounter.departure_at,
       encounter.age_years, encounter.acuity, encounter.arrival_mode,
       encounter.access_support_group, encounter.disposition,
       encounter.left_before_seen_flag, encounter.return_to_encounter_id,
       encounter.return_within_72h_flag, event_pivot.recorded_event_count,
       CASE WHEN event_pivot.triage_at IS NOT NULL THEN 1 ELSE 0 END AS triage_available_flag,
       CASE WHEN event_pivot.clinician_at IS NOT NULL THEN 1 ELSE 0 END AS clinician_available_flag,
       CASE
         WHEN encounter.left_before_seen_flag = 1
           AND event_pivot.arrival_event_at IS NOT NULL
           AND event_pivot.triage_at IS NOT NULL
           AND event_pivot.departure_event_at IS NOT NULL
           AND julianday(event_pivot.arrival_event_at) <= julianday(event_pivot.triage_at)
           AND julianday(event_pivot.triage_at) <= julianday(event_pivot.departure_event_at)
           THEN 1
         WHEN encounter.left_before_seen_flag = 0
           AND event_pivot.arrival_event_at IS NOT NULL
           AND event_pivot.triage_at IS NOT NULL
           AND event_pivot.roomed_at IS NOT NULL
           AND event_pivot.clinician_at IS NOT NULL
           AND event_pivot.disposition_at IS NOT NULL
           AND event_pivot.departure_event_at IS NOT NULL
           AND julianday(event_pivot.arrival_event_at) <= julianday(event_pivot.triage_at)
           AND julianday(event_pivot.triage_at) <= julianday(event_pivot.roomed_at)
           AND julianday(event_pivot.roomed_at) <= julianday(event_pivot.clinician_at)
           AND julianday(event_pivot.clinician_at) <= julianday(event_pivot.disposition_at)
           AND julianday(event_pivot.disposition_at) <= julianday(event_pivot.departure_event_at)
           THEN 1
         ELSE 0
       END AS valid_event_sequence_flag,
       ROUND((julianday(event_pivot.triage_at) - julianday(encounter.arrival_at)) * 1440.0, 3) AS arrival_to_triage_minutes,
       CASE WHEN event_pivot.clinician_at IS NOT NULL
         THEN ROUND((julianday(event_pivot.clinician_at) - julianday(encounter.arrival_at)) * 1440.0, 3)
       END AS arrival_to_clinician_minutes,
       ROUND((julianday(encounter.departure_at) - julianday(encounter.arrival_at)) * 1440.0, 3) AS arrival_to_departure_minutes,
       CASE WHEN encounter.left_before_seen_flag = 0 THEN 1 ELSE 0 END AS completed_flag,
       1 AS eligible_adult_encounter_flag,
       encounter.source_row_status, encounter.defect_flag, encounter.synthetic_flag
FROM clean_encounters AS encounter
JOIN event_pivot USING (encounter_id)
JOIN clean_calendar_demand AS calendar ON calendar.shift_id = encounter.arrival_shift_id;

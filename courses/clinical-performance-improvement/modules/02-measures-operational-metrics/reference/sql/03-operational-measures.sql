DROP TABLE IF EXISTS shift_metrics;
CREATE TABLE shift_metrics AS
WITH encounter_summary AS (
  SELECT arrival_shift_id AS shift_id,
         COUNT(*) AS arrivals,
         SUM(completed_flag) AS completed_encounters,
         SUM(left_before_seen_flag) AS left_before_seen,
         SUM(return_within_72h_flag) AS return_within_72h,
         SUM(valid_event_sequence_flag) AS valid_event_sequences,
         SUM(clinician_available_flag) AS clinician_time_available,
         median(arrival_to_triage_minutes) AS median_arrival_to_triage_minutes,
         median(arrival_to_clinician_minutes) AS median_arrival_to_clinician_minutes,
         median(arrival_to_departure_minutes) AS median_arrival_to_departure_minutes
  FROM encounter_measures
  GROUP BY arrival_shift_id
), staff_summary AS (
  SELECT shift_id,
         SUM(CASE WHEN role IN ('physician', 'advanced_practice_clinician') THEN actual_staff_hours ELSE 0 END) AS clinician_staff_hours,
         SUM(actual_staff_hours) AS total_staff_hours,
         SUM(overtime_hours) AS overtime_hours,
         SUM(absence_hours) AS absence_hours
  FROM clean_staffing
  GROUP BY shift_id
), queue_summary AS (
  SELECT shift_id, AVG(queue_end) AS mean_queue_end, MAX(queue_end) AS max_queue_end,
         median(queue_end) AS median_queue_end,
         SUM(staffed_clinician_hours_interval) AS queue_clinician_hours
  FROM clean_queue_snapshots
  GROUP BY shift_id
)
SELECT calendar.shift_id, calendar.date, calendar.shift_name, calendar.week_index,
       encounter.arrivals, encounter.completed_encounters, encounter.left_before_seen,
       ROUND(100.0 * encounter.left_before_seen / encounter.arrivals, 4) AS left_before_seen_percent,
       encounter.return_within_72h,
       ROUND(100.0 * encounter.return_within_72h / NULLIF(encounter.completed_encounters, 0), 4) AS return_within_72h_percent,
       encounter.valid_event_sequences,
       ROUND(100.0 * encounter.valid_event_sequences / encounter.arrivals, 4) AS valid_event_sequence_percent,
       encounter.clinician_time_available,
       encounter.median_arrival_to_triage_minutes,
       encounter.median_arrival_to_clinician_minutes,
       encounter.median_arrival_to_departure_minutes,
       staff.clinician_staff_hours, staff.total_staff_hours, staff.overtime_hours, staff.absence_hours,
       ROUND(staff.clinician_staff_hours / encounter.arrivals, 4) AS clinician_staff_hours_per_arrival,
       ROUND(encounter.completed_encounters / NULLIF(staff.clinician_staff_hours, 0), 4) AS completed_encounters_per_clinician_hour,
       ROUND(queue.mean_queue_end, 4) AS mean_queue_end, queue.max_queue_end,
       queue.median_queue_end, queue.queue_clinician_hours,
       calendar.holiday_flag, calendar.synthetic_special_event_flag,
       1 AS synthetic_flag
FROM clean_calendar_demand AS calendar
JOIN encounter_summary AS encounter USING (shift_id)
JOIN staff_summary AS staff USING (shift_id)
JOIN queue_summary AS queue USING (shift_id)
ORDER BY calendar.shift_start;

DROP TABLE IF EXISTS weekly_metrics;
CREATE TABLE weekly_metrics AS
SELECT week_index,
       MIN(date) AS week_start_date, MAX(date) AS week_end_date,
       SUM(arrivals) AS arrivals, SUM(completed_encounters) AS completed_encounters,
       SUM(left_before_seen) AS left_before_seen,
       ROUND(100.0 * SUM(left_before_seen) / SUM(arrivals), 4) AS left_before_seen_percent,
       SUM(return_within_72h) AS return_within_72h,
       ROUND(100.0 * SUM(return_within_72h) / NULLIF(SUM(completed_encounters), 0), 4) AS return_within_72h_percent,
       ROUND(AVG(median_arrival_to_triage_minutes), 3) AS shift_median_arrival_to_triage_mean,
       ROUND(AVG(median_arrival_to_clinician_minutes), 3) AS shift_median_arrival_to_clinician_mean,
       ROUND(AVG(median_arrival_to_departure_minutes), 3) AS shift_median_arrival_to_departure_mean,
       ROUND(SUM(completed_encounters) / SUM(clinician_staff_hours), 4) AS completed_encounters_per_clinician_hour,
       ROUND(SUM(overtime_hours), 3) AS overtime_hours,
       ROUND(AVG(mean_queue_end), 4) AS mean_queue_end,
       MAX(max_queue_end) AS max_queue_end,
       SUM(synthetic_special_event_flag) AS special_event_shifts,
       1 AS synthetic_flag
FROM shift_metrics
GROUP BY week_index
ORDER BY week_index;

DROP TABLE IF EXISTS safety_diagnostics;
CREATE TABLE safety_diagnostics AS
WITH classes(event_class) AS (
  VALUES ('overall'), ('error'), ('near_miss'), ('adverse_event'), ('harm')
), eligible AS (
  SELECT SUM(completed_flag) AS completed_encounters FROM encounter_measures
), counts AS (
  SELECT event_class,
         SUM(known_true_event_flag) AS known_true_events,
         SUM(CASE WHEN known_true_event_flag = 1 AND trigger_flag = 1 THEN 1 ELSE 0 END) AS trigger_true_positives,
         SUM(CASE WHEN known_true_event_flag = 1 AND incident_report_flag = 1 THEN 1 ELSE 0 END) AS incident_true_positives
  FROM clean_safety_events
  GROUP BY event_class
), overall AS (
  SELECT SUM(known_true_event_flag) AS known_true_events,
         SUM(CASE WHEN known_true_event_flag = 1 AND trigger_flag = 1 THEN 1 ELSE 0 END) AS trigger_true_positives,
         SUM(CASE WHEN known_true_event_flag = 1 AND incident_report_flag = 1 THEN 1 ELSE 0 END) AS incident_true_positives,
         SUM(CASE WHEN known_true_event_flag = 0 AND trigger_flag = 1 THEN 1 ELSE 0 END) AS trigger_false_positives
  FROM clean_safety_events
)
SELECT class.event_class,
       eligible.completed_encounters,
       CASE WHEN class.event_class = 'overall' THEN overall.known_true_events ELSE COALESCE(counts.known_true_events, 0) END AS known_true_events,
       CASE WHEN class.event_class = 'overall' THEN overall.trigger_true_positives ELSE COALESCE(counts.trigger_true_positives, 0) END AS trigger_true_positives,
       CASE WHEN class.event_class = 'overall' THEN overall.incident_true_positives ELSE COALESCE(counts.incident_true_positives, 0) END AS incident_true_positives,
       CASE WHEN class.event_class = 'overall' THEN overall.trigger_false_positives ELSE 0 END AS trigger_false_positives,
       ROUND(100.0 * (CASE WHEN class.event_class = 'overall' THEN overall.trigger_true_positives ELSE COALESCE(counts.trigger_true_positives, 0) END) /
             NULLIF((CASE WHEN class.event_class = 'overall' THEN overall.known_true_events ELSE COALESCE(counts.known_true_events, 0) END), 0), 4) AS trigger_sensitivity_percent,
       ROUND(100.0 * (CASE WHEN class.event_class = 'overall' THEN overall.incident_true_positives ELSE COALESCE(counts.incident_true_positives, 0) END) /
             NULLIF((CASE WHEN class.event_class = 'overall' THEN overall.known_true_events ELSE COALESCE(counts.known_true_events, 0) END), 0), 4) AS incident_capture_percent,
       CASE WHEN class.event_class = 'overall'
         THEN ROUND(100.0 * ((eligible.completed_encounters - overall.known_true_events) - overall.trigger_false_positives) /
                    NULLIF((eligible.completed_encounters - overall.known_true_events), 0), 4)
       END AS trigger_specificity_percent,
       1 AS synthetic_flag
FROM classes AS class
CROSS JOIN eligible
LEFT JOIN counts ON counts.event_class = class.event_class
CROSS JOIN overall;

DROP TABLE IF EXISTS subgroup_support;
CREATE TABLE subgroup_support AS
SELECT access_support_group,
       COUNT(*) AS eligible_encounters,
       SUM(clinician_available_flag) AS clinician_time_available,
       SUM(left_before_seen_flag) AS left_before_seen,
       ROUND(100.0 * SUM(left_before_seen_flag) / COUNT(*), 4) AS left_before_seen_percent,
       SUM(return_within_72h_flag) AS return_within_72h,
       ROUND(100.0 * SUM(return_within_72h_flag) / NULLIF(SUM(completed_flag), 0), 4) AS return_within_72h_percent,
       median(arrival_to_clinician_minutes) AS median_arrival_to_clinician_minutes,
       median(arrival_to_departure_minutes) AS median_arrival_to_departure_minutes,
       SUM(CASE WHEN arrival_to_clinician_minutes IS NULL THEN 1 ELSE 0 END) AS clinician_time_unavailable,
       1 AS synthetic_flag
FROM encounter_measures
GROUP BY access_support_group
ORDER BY access_support_group;

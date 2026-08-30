DROP TABLE IF EXISTS source_reconciliation;
CREATE TABLE source_reconciliation AS
SELECT 'encounters' AS table_name, (SELECT COUNT(*) FROM raw_encounters) AS raw_rows, (SELECT COUNT(*) FROM clean_encounters) AS clean_rows, 'deduplicate repair and quarantine' AS disposition
UNION ALL SELECT 'process-events', (SELECT COUNT(*) FROM raw_process_events), (SELECT COUNT(*) FROM clean_process_events), 'deduplicate repair and eligible encounter join'
UNION ALL SELECT 'staffing', (SELECT COUNT(*) FROM raw_staffing), (SELECT COUNT(*) FROM clean_staffing), 'repair impossible hours'
UNION ALL SELECT 'queue-snapshots', (SELECT COUNT(*) FROM raw_queue_snapshots), (SELECT COUNT(*) FROM clean_queue_snapshots), 'recalculate queue end'
UNION ALL SELECT 'safety-events', (SELECT COUNT(*) FROM raw_safety_events), (SELECT COUNT(*) FROM clean_safety_events), 'deduplicate and eligible encounter join'
UNION ALL SELECT 'calendar-demand', (SELECT COUNT(*) FROM raw_calendar_demand), (SELECT COUNT(*) FROM clean_calendar_demand), 'derive demand from accepted encounters'
UNION ALL SELECT 'scenarios', (SELECT COUNT(*) FROM raw_scenarios), (SELECT COUNT(*) FROM clean_scenarios), 'unchanged declaration'
UNION ALL SELECT 'known-truth', (SELECT COUNT(*) FROM raw_known_truth), (SELECT COUNT(*) FROM clean_known_truth), 'unchanged generated truth'
UNION ALL SELECT 'defect-register', (SELECT COUNT(*) FROM raw_defect_register), (SELECT COUNT(*) FROM clean_defect_register), 'unchanged audit record';

DROP TABLE IF EXISTS defect_impact;
CREATE TABLE defect_impact AS
SELECT 'D001' AS defect_id, 'duplicate encounter row' AS defect,
       (SELECT COUNT(*) FROM raw_encounters WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D001')) AS raw_value,
       (SELECT COUNT(*) FROM clean_encounters WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D001')) AS clean_value,
       '2 raw rows become 1 accepted encounter' AS expected_result
UNION ALL SELECT 'D002', 'missing encounter arrival',
       (SELECT COUNT(*) FROM raw_encounters WHERE defect_flag = 'D002' AND arrival_at = ''),
       (SELECT COUNT(*) FROM clean_encounters WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D002') AND arrival_at <> ''),
       '1 blank raw arrival becomes 1 repaired arrival'
UNION ALL SELECT 'D003', 'public-like service identifier',
       (SELECT COUNT(*) FROM raw_encounters WHERE defect_flag = 'D003'),
       (SELECT COUNT(*) FROM clean_encounters WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D003')),
       '1 invalid raw encounter becomes 0 accepted encounters'
UNION ALL SELECT 'D004', 'underage encounter',
       (SELECT COUNT(*) FROM raw_encounters WHERE defect_flag = 'D004' AND CAST(age_years AS INTEGER) < 18),
       (SELECT COUNT(*) FROM clean_encounters WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D004')),
       '1 outside-population row becomes 0 accepted encounters'
UNION ALL SELECT 'D005', 'departure before arrival',
       (SELECT COUNT(*) FROM raw_encounters WHERE defect_flag = 'D005' AND julianday(departure_at) < julianday(arrival_at)),
       (SELECT COUNT(*) FROM clean_encounters WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D005') AND julianday(departure_at) >= julianday(arrival_at)),
       '1 impossible raw clock becomes 1 repaired clock'
UNION ALL SELECT 'D006', 'duplicate process event',
       (SELECT COUNT(*) FROM raw_process_events WHERE event_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D006')),
       (SELECT COUNT(*) FROM clean_process_events WHERE event_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D006')),
       '2 raw rows become 1 accepted event'
UNION ALL SELECT 'D007', 'swapped triage and rooming times',
       (SELECT COUNT(*) FROM raw_process_events WHERE defect_flag = 'D007'),
       (SELECT valid_event_sequence_flag FROM encounter_measures WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D007')),
       '2 affected raw events yield 1 valid accepted sequence'
UNION ALL SELECT 'D008', 'missing clinician event',
       (SELECT COUNT(*) FROM raw_process_events WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D008') AND event_type = 'clinician'),
       (SELECT clinician_available_flag FROM encounter_measures WHERE encounter_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D008')),
       '0 raw clinician events remain 0 available clinician times'
UNION ALL SELECT 'D009', 'negative queue end',
       (SELECT COUNT(*) FROM raw_queue_snapshots WHERE defect_flag = 'D009' AND CAST(queue_end AS INTEGER) < 0),
       (SELECT COUNT(*) FROM clean_queue_snapshots WHERE defect_flag = 'D009' AND queue_end >= 0),
       '1 impossible raw queue becomes 1 conserved queue row'
UNION ALL SELECT 'D010', 'negative actual staff hours',
       (SELECT COUNT(*) FROM raw_staffing WHERE defect_flag = 'D010' AND CAST(actual_staff_hours AS REAL) < 0),
       (SELECT COUNT(*) FROM clean_staffing WHERE defect_flag = 'D010' AND actual_staff_hours >= 0),
       '1 impossible raw staffing row becomes 1 repaired row'
UNION ALL SELECT 'D011', 'duplicate safety candidate',
       (SELECT COUNT(*) FROM raw_safety_events WHERE candidate_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D011')),
       (SELECT COUNT(*) FROM clean_safety_events WHERE candidate_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D011')),
       '2 raw rows become 1 accepted safety candidate'
UNION ALL SELECT 'D012', 'calendar and encounter arrival mismatch',
       (SELECT CAST(arrival_count AS INTEGER) FROM raw_calendar_demand WHERE shift_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D012')),
       (SELECT arrival_count FROM clean_calendar_demand WHERE shift_id = (SELECT affected_key FROM clean_defect_register WHERE defect_id = 'D012')),
       'raw count is five above accepted encounter-derived demand';

DROP TABLE IF EXISTS query_checks;
CREATE TABLE query_checks AS
SELECT 'Q01' AS check_id, 'raw encounter rows' AS check_name, (SELECT COUNT(*) FROM raw_encounters) AS observed_value, 43631 AS expected_value
UNION ALL SELECT 'Q02', 'clean adult encounters', (SELECT COUNT(*) FROM clean_encounters), 43628
UNION ALL SELECT 'Q03', 'clean encounter duplicate keys', (SELECT COUNT(*) - COUNT(DISTINCT encounter_id) FROM clean_encounters), 0
UNION ALL SELECT 'Q04', 'clean public-like service identifiers', (SELECT COUNT(*) FROM clean_encounters WHERE service_id <> 'CGH-ED-01'), 0
UNION ALL SELECT 'Q05', 'clean underage encounters', (SELECT COUNT(*) FROM clean_encounters WHERE age_years < 18), 0
UNION ALL SELECT 'Q06', 'clean impossible encounter clocks', (SELECT COUNT(*) FROM clean_encounters WHERE julianday(departure_at) < julianday(arrival_at)), 0
UNION ALL SELECT 'Q07', 'raw process-event rows', (SELECT COUNT(*) FROM raw_process_events), 250821
UNION ALL SELECT 'Q08', 'clean process-event duplicate keys', (SELECT COUNT(*) - COUNT(DISTINCT event_id) FROM clean_process_events), 0
UNION ALL SELECT 'Q09', 'clean event orphans', (SELECT COUNT(*) FROM clean_process_events AS event LEFT JOIN clean_encounters USING (encounter_id) WHERE clean_encounters.encounter_id IS NULL), 0
UNION ALL SELECT 'Q10', 'invalid accepted event sequences', (SELECT COUNT(*) FROM encounter_measures WHERE valid_event_sequence_flag = 0), 1
UNION ALL SELECT 'Q11', 'missing clinician times retained', (SELECT COUNT(*) FROM encounter_measures WHERE clinician_available_flag = 0 AND left_before_seen_flag = 0), 1
UNION ALL SELECT 'Q12', 'negative arrival-to-triage times', (SELECT COUNT(*) FROM encounter_measures WHERE arrival_to_triage_minutes < 0), 0
UNION ALL SELECT 'Q13', 'negative arrival-to-clinician times', (SELECT COUNT(*) FROM encounter_measures WHERE arrival_to_clinician_minutes < 0), 0
UNION ALL SELECT 'Q14', 'negative arrival-to-departure times', (SELECT COUNT(*) FROM encounter_measures WHERE arrival_to_departure_minutes < 0), 0
UNION ALL SELECT 'Q15', 'clean negative queue ends', (SELECT COUNT(*) FROM clean_queue_snapshots WHERE queue_end < 0), 0
UNION ALL SELECT 'Q16', 'queue conservation failures', (SELECT COUNT(*) FROM clean_queue_snapshots WHERE queue_end <> queue_start + arrivals - service_starts - exits_without_service), 0
UNION ALL SELECT 'Q17', 'clean negative actual staff hours', (SELECT COUNT(*) FROM clean_staffing WHERE actual_staff_hours < 0), 0
UNION ALL SELECT 'Q18', 'staffing shift orphans', (SELECT COUNT(*) FROM clean_staffing AS staff LEFT JOIN clean_calendar_demand AS calendar USING (shift_id) WHERE calendar.shift_id IS NULL), 0
UNION ALL SELECT 'Q19', 'calendar shifts', (SELECT COUNT(*) FROM clean_calendar_demand), 1092
UNION ALL SELECT 'Q20', 'calendar arrival mismatches', (SELECT COUNT(*) FROM clean_calendar_demand AS calendar LEFT JOIN (SELECT arrival_shift_id AS shift_id, COUNT(*) AS arrivals FROM clean_encounters GROUP BY arrival_shift_id) AS encounter USING (shift_id) WHERE calendar.arrival_count <> encounter.arrivals), 0
UNION ALL SELECT 'Q21', 'weekly metric rows', (SELECT COUNT(*) FROM weekly_metrics), 52
UNION ALL SELECT 'Q22', 'shift metric rows', (SELECT COUNT(*) FROM shift_metrics), 1092
UNION ALL SELECT 'Q23', 'safety duplicate keys', (SELECT COUNT(*) - COUNT(DISTINCT candidate_id) FROM clean_safety_events), 0
UNION ALL SELECT 'Q24', 'safety event orphans', (SELECT COUNT(*) FROM clean_safety_events AS safety LEFT JOIN clean_encounters USING (encounter_id) WHERE clean_encounters.encounter_id IS NULL), 0
UNION ALL SELECT 'Q25', 'subgroup support rows', (SELECT COUNT(*) FROM subgroup_support), 3
UNION ALL SELECT 'Q26', 'subgroups below 1000 encounters', (SELECT COUNT(*) FROM subgroup_support WHERE eligible_encounters < 1000), 0
UNION ALL SELECT 'Q27', 'seeded defect rows', (SELECT COUNT(*) FROM clean_defect_register), 12
UNION ALL SELECT 'Q28', 'defect impact rows', (SELECT COUNT(*) FROM defect_impact), 12
UNION ALL SELECT 'Q29', 'synthetic flags not equal to one in clean encounters', (SELECT COUNT(*) FROM clean_encounters WHERE synthetic_flag <> 1), 0
UNION ALL SELECT 'Q30', 'scenario results present', (SELECT COUNT(*) FROM clean_scenarios WHERE results_status <> 'not run in Module 02'), 0;

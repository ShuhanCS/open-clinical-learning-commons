-- query: table-inventory
SELECT table_name, source_rows, source_columns
FROM source_table_manifest
ORDER BY table_name;

-- query: encounter-class-counts
SELECT encounterclass, COUNT(*) AS encounter_count
FROM encounters
GROUP BY encounterclass
ORDER BY encounter_count DESC, encounterclass;

-- query: observation-linkage
SELECT
    type,
    CASE WHEN encounter IS NULL THEN 'no encounter reference' ELSE 'linked encounter' END AS encounter_linkage,
    COUNT(*) AS observation_count
FROM observations
GROUP BY type, encounter_linkage
ORDER BY type, encounter_linkage;

-- query: selected-patient-timeline
WITH selected_patient AS (
    SELECT patient
    FROM encounters
    GROUP BY patient
    ORDER BY COUNT(*) DESC, patient
    LIMIT 1
)
SELECT encounter_id, start, stop, encounterclass, code, description
FROM v_encounters_core
WHERE patient_id = (SELECT patient FROM selected_patient)
ORDER BY start, encounter_id
LIMIT 25;

-- query: numeric-observation-sample
SELECT source_row_number, date, patient_id, encounter_id, code, description, value, units
FROM v_observations_core
WHERE type = 'numeric' AND units IS NOT NULL
ORDER BY patient_id, date, code, source_row_number
LIMIT 25;

PRAGMA foreign_keys = ON;

CREATE TABLE patients (
    id TEXT PRIMARY KEY,
    birthdate TEXT NOT NULL,
    deathdate TEXT,
    ssn TEXT,
    drivers TEXT,
    passport TEXT,
    prefix TEXT,
    first TEXT,
    last TEXT,
    suffix TEXT,
    maiden TEXT,
    marital TEXT,
    race TEXT NOT NULL,
    ethnicity TEXT NOT NULL,
    gender TEXT NOT NULL,
    birthplace TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    county TEXT,
    zip TEXT,
    lat REAL,
    lon REAL,
    healthcare_expenses REAL,
    healthcare_coverage REAL
);

CREATE TABLE organizations (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    lat REAL,
    lon REAL,
    phone TEXT,
    revenue REAL,
    utilization INTEGER
);

CREATE TABLE providers (
    id TEXT PRIMARY KEY,
    organization TEXT NOT NULL REFERENCES organizations(id),
    name TEXT,
    gender TEXT,
    speciality TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    lat REAL,
    lon REAL,
    utilization INTEGER
);

CREATE TABLE payers (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state_headquartered TEXT,
    zip TEXT,
    phone TEXT,
    amount_covered REAL,
    amount_uncovered REAL,
    revenue REAL,
    covered_encounters INTEGER,
    uncovered_encounters INTEGER,
    covered_medications INTEGER,
    uncovered_medications INTEGER,
    covered_procedures INTEGER,
    uncovered_procedures INTEGER,
    covered_immunizations INTEGER,
    uncovered_immunizations INTEGER,
    unique_customers INTEGER,
    qols_avg REAL,
    member_months INTEGER
);

CREATE TABLE encounters (
    id TEXT PRIMARY KEY,
    start TEXT NOT NULL,
    stop TEXT NOT NULL,
    patient TEXT NOT NULL REFERENCES patients(id),
    organization TEXT NOT NULL REFERENCES organizations(id),
    provider TEXT NOT NULL REFERENCES providers(id),
    payer TEXT NOT NULL REFERENCES payers(id),
    encounterclass TEXT NOT NULL,
    code TEXT NOT NULL,
    description TEXT,
    base_encounter_cost REAL,
    total_claim_cost REAL,
    payer_coverage REAL,
    reasoncode TEXT,
    reasondescription TEXT
);

CREATE TABLE allergies (
    source_row_number INTEGER PRIMARY KEY,
    start TEXT NOT NULL,
    stop TEXT,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT
);

CREATE TABLE careplans (
    id TEXT PRIMARY KEY,
    start TEXT NOT NULL,
    stop TEXT,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    reasoncode TEXT,
    reasondescription TEXT
);

CREATE TABLE conditions (
    source_row_number INTEGER PRIMARY KEY,
    start TEXT NOT NULL,
    stop TEXT,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT
);

CREATE TABLE devices (
    source_row_number INTEGER PRIMARY KEY,
    start TEXT NOT NULL,
    stop TEXT,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    udi TEXT
);

CREATE TABLE imaging_studies (
    id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    bodysite_code TEXT,
    bodysite_description TEXT,
    modality_code TEXT,
    modality_description TEXT,
    sop_code TEXT,
    sop_description TEXT
);

CREATE TABLE immunizations (
    source_row_number INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    base_cost REAL
);

CREATE TABLE medications (
    source_row_number INTEGER PRIMARY KEY,
    start TEXT NOT NULL,
    stop TEXT,
    patient TEXT NOT NULL REFERENCES patients(id),
    payer TEXT NOT NULL REFERENCES payers(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    base_cost REAL,
    payer_coverage REAL,
    dispenses INTEGER,
    totalcost REAL,
    reasoncode TEXT,
    reasondescription TEXT
);

CREATE TABLE observations (
    source_row_number INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    value TEXT,
    units TEXT,
    type TEXT NOT NULL CHECK (type IN ('numeric', 'text'))
);

CREATE TABLE payer_transitions (
    source_row_number INTEGER PRIMARY KEY,
    patient TEXT NOT NULL REFERENCES patients(id),
    start_year INTEGER NOT NULL,
    end_year INTEGER NOT NULL,
    payer TEXT NOT NULL REFERENCES payers(id),
    ownership TEXT
);

CREATE TABLE procedures (
    source_row_number INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    base_cost REAL,
    reasoncode TEXT,
    reasondescription TEXT
);

CREATE TABLE supplies (
    source_row_number INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    patient TEXT NOT NULL REFERENCES patients(id),
    encounter TEXT NOT NULL REFERENCES encounters(id),
    code TEXT NOT NULL,
    description TEXT,
    quantity INTEGER
);

CREATE TABLE source_table_manifest (
    table_name TEXT PRIMARY KEY,
    archive_path TEXT NOT NULL,
    source_bytes INTEGER NOT NULL,
    source_rows INTEGER NOT NULL,
    source_columns INTEGER NOT NULL,
    source_sha256 TEXT NOT NULL
);

CREATE INDEX encounters_patient_start_idx ON encounters(patient, start);
CREATE INDEX observations_patient_date_idx ON observations(patient, date);
CREATE INDEX observations_encounter_idx ON observations(encounter);
CREATE INDEX conditions_patient_start_idx ON conditions(patient, start);
CREATE INDEX medications_patient_start_idx ON medications(patient, start);
CREATE INDEX procedures_patient_date_idx ON procedures(patient, date);

CREATE VIEW v_patients_minimal AS
SELECT id AS patient_id, birthdate, deathdate, marital, race, ethnicity, gender, state, county
FROM patients;

CREATE VIEW v_encounters_core AS
SELECT id AS encounter_id, start, stop, patient AS patient_id, encounterclass, code, description, reasoncode, reasondescription
FROM encounters;

CREATE VIEW v_observations_core AS
SELECT source_row_number, date, patient AS patient_id, encounter AS encounter_id, code, description, value, units, type
FROM observations;

# Reference transformation record

## Inputs

- Accepted Module 03 analytic table: 374 rows, 29 fields, 121,787 bytes.
- Accepted SHA-256: `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- Cohort-definition version: 0.1.0.

## Defect-layer build

1. Verify the accepted bytes, hash, shape, patient grain, and field contract.
2. Copy the accepted table without alteration.
3. Select distinct synthetic patients in stable input order for D01 through D20.
4. Apply the registered teaching changes and record each original and defective value.
5. Append five exact duplicate rows.
6. Write the defective CSV, 68-row manifest, 28-rule registry, and SQLite inspection database.

## Profiling and resolution

1. Count rows and distinct people before field profiling.
2. Profile all 29 fields and compare accepted with defective missingness.
3. Detect D01 through D20 and N01 through N08 independently.
4. Write aligned rule results, risk log, and resolution log.
5. Resolve seeded defects by rebuilding from the accepted source.
6. Preserve natural source characteristics as documented conditions.
7. Verify the resolved file matches the accepted file byte for byte.

No accepted source value is edited in place. No optional value is imputed. No extreme accepted value or small group is deleted.

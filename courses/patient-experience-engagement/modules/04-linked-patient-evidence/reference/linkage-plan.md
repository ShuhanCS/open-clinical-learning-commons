# Linkage plan

- Decision: `whether patient-reported, access, communication, digital-service, and service-use evidence can be linked with aligned denominators and bounded interpretation`
- Person grain: `one accepted adult inpatient target person`
- Event grains: `one inpatient stay, emergency visit, outpatient visit, or office-based visit per source row`
- Internal link key: `DUPERSID from the official public-use files`
- Released identity: `sequential LINK and EVENT teaching identifiers; no direct public-use person or event ID`
- Related-event rule: `preserve reciprocal links for the 855 emergency-inpatient pairs and do not call them unrelated encounters`
- Period rule: `retain the 12 inpatient stays that begin in 2023 and continue into the 2024 event file`
- Weight rule: `PERWT24F for person estimates with VARSTR and VARPSU; do not sum repeated event-row weights to count unique people`
- Stop rule: `stop if a source fingerprint, checkpoint identity, link total, person-event reconciliation, denominator, design field, data class, or claim boundary fails`

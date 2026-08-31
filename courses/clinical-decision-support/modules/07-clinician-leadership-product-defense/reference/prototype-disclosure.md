# Prototype disclosure

- Prototype: `APP4-M05-LOCAL-SANDBOX-2026-08-31-v1`.
- Runtime: local and nonnetworked.
- Design: `panel-t003`, passive contextual mechanics fixture.
- Threshold: `0.03000000`, unaccepted sandbox fixture.
- Accepted threshold: `none`.
- Cases: `31`.
- Prefetch resources: `184`.
- Responses: `31`.
- Trace events: `61`.
- Inherited failure modes: `17`.
- Silent failures detected: `1`.
- Accessibility defects blocked: `1`.
- Network listener or client: `none`.
- Clinical suggestion, order, or action route: `none`.

The resources and messages are FHIR R4 and CDS Hooks-shaped teaching artifacts. They have not passed a clinical interoperability or conformance review. A test passes when the observed local behavior matches the declared expected behavior, including a visible stop or blocked result. Passing tests do not prove safety, usability, local validity, or utility.

The silent failure is a received request with no response, no terminal trace, and no human notice. It is found by reconciling independent request, response, terminal-trace, and notice ledgers. It does not estimate a clinical failure rate.

The malformed-card fixture remains blocked. Module 07 may require its repair in a future revision, but it may not alter the frozen candidate or waive the defect.

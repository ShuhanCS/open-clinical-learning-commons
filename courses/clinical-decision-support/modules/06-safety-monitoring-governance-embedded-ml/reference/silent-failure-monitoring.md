# Silent-failure monitoring

- Definition: `a received request with no response, no terminal trace, and no human notice`.
- Independent ledgers: `request, response, terminal trace, and human notice`.
- Trigger: `one or more reconciled silent failures`.
- Owner: `patient-safety owner`.
- Cadence: `daily and after every declared test run`.
- Unavailable state: `report reconciliation unavailable and stop the affected evaluation`.
- Human action: `verify all four ledgers, preserve the event, escalate, and investigate`.
- Rate claim: `none; the seeded event does not estimate a clinical silent-failure rate`.

## Reconciliation

The request ledger supplies the denominator. Response, terminal-trace, and notice ledgers are joined independently by request identity. A request present in the first ledger and absent from all three remaining ledgers is counted once. The service log cannot substitute for this reconciliation because the seeded failure disappears after receipt.

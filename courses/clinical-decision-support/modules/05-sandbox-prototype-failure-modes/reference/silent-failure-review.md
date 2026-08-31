# Silent-failure review

## Declared case

`M05-F15` uses the seeded `drop_after_receive` route. The request ledger records receipt. The response body is absent, the service produces no terminal trace, and no human notice appears.

## Detection rule

A silent failure exists when all four statements are true:

1. the request ledger shows receipt;
2. the response body is absent;
3. the terminal trace is absent; and
4. the human notice is absent.

The visibility audit applies the rule to all 31 cases and detects exactly one silent failure. These independent ledgers prevent the audit from treating HTTP status, a request log, or a response envelope by itself as proof of delivery.

## Contrast with visible failure

`M05-F13` returns a visible 503 service failure. `M05-F14` returns a visible 504 timeout. Both have a terminal trace and human notice. They are failures, but they are not silent.

## Required Module 06 control

Module 06 must define a reconciliation measure with request, response, terminal, and notice counts; an owner; cadence; trigger origin; escalation; fallback; stop rule; and unavailable state. The control cannot rely on the service log alone.

## Authority

This seeded case does not estimate a clinical silent-failure rate or authorize silent-mode evaluation. It proves only that the curriculum detector recognizes the declared local fixture.

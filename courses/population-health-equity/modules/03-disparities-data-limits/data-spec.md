# Data specification

## Accepted upstream

The module freezes the complete 72-file Module 02 reference workspace, its 57-row nested manifest, and the accepted Module 02 release record. The outer 73-row handoff manifest has SHA-256 `f5e84b251143edeb65b68d816a57492755083d8bc57c73e6bdaede381b933ef1`.

The handoff preserves 5,679,768 adult denominator units, 283,614 generated events, all public-source identities, all age-specific and standardized measures, every unavailable state, and every Module 02 limit.

## Synthetic equity margins

Release `fma-dp-01-equity-v1` uses generator version `0.1.0` and seed `73053`. It contains 151,715 rows across three separate dimensions:

- combined race and ethnicity: nine groups, including a missing group;
- primary language: seven groups, including a missing group; and
- disability status: three groups, including a missing group.

Each dimension independently sums to the accepted 5,679,768 denominator and 283,614 event total. The dimensions are margins. They cannot be joined to construct intersectional or person-level records. The group labels and values are fictional teaching data, not Massachusetts demographic estimates.

## Field completeness

The 7,985-row field-completeness table retains the accepted tract-age grain and generated event total. It records 6,000 missing race values, 7,578 missing ethnicity values, 5,314 missing primary-language values, 8,376 missing disability-status values, and zero missing tract-geography values.

The geography result is conditioned on the accepted linked analytic universe. It does not show whether records without usable geography were excluded before that universe was formed.

## Suppression

A tract-group cell is primarily suppressed when its generated event count is below 16 or its denominator is below 100. When exactly one cell in a tract-dimension table meets the primary rule, the smallest remaining supported cell is also suppressed. Published suppressed rows keep the key, state, and reason while counts, rates, and intervals remain blank.

This is a teaching policy informed by CDC presentation practice. It is not a universal disclosure, legal, surveillance, or clinical rule.

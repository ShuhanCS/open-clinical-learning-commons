# Suppression policy

- Primary event threshold: `16` generated events.
- Primary denominator threshold: `100` generated population units.
- Complementary rule: when exactly one tract-dimension cell is primarily suppressed, suppress the smallest remaining supported cell by event count, denominator, and fixed group order.
- Published tract-group rows: `30,343`.
- Primary suppressed cells: `19,742`.
- Complementary suppressed cells: `1,488`.
- Publishable cells: `9,113`.
- Suppression audit rows: `4,791`.
- Failed suppression audits: `0`.

Every suppressed row retains its tract, dimension, group, support state, and reason. Population count, event count, rate, and interval remain blank. A blank is unavailable, not zero. The publication table contains no tract-dimension total from which a withheld cell can be recovered by subtraction.

The raw teaching source is synthetic and open. This policy tests responsible presentation behavior; it does not claim to protect real confidential records or replace an agency disclosure review.

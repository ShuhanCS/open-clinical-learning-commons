# Scenario comparison

- Primary condition: `C02 point demand`
- Decision: `none qualifies for feasibility review`
- Decision rule: `all six predeclared rules must pass`

| Option | Median wait change | P90 wait change | LBBS change | Throughput change | Flex hours | Result |
|---|---:|---:|---:|---:|---:|---|
| S01 flex coverage | 1.958703 min better | 21.244986 min better | 2.518000 pp better | 2.874244% higher | 40.000000 | fails 10-minute median rule |
| S02 fast track | 5.803341 min worse | 41.617987 min worse | 6.611140 pp better | 7.540650% higher | 0.000000 | fails median, P90, and stress rules |
| S03 combined | 0.316383 min better | 14.547388 min better | 3.163164 pp better | 3.590432% higher | 25.220413 | fails median and P90 rules |

S01 improves the tail and abandonment but does not clear the median-wait gate. S02 exposes a real tradeoff inside the model: prioritizing a fast lane raises completion while worsening waiting time. S03 does not clear the predeclared thresholds. The correct decision is no change, not selection of the least unfavorable option.

These paired synthetic effects are assumption tests. They do not prove that flex coverage, fast track, or a combined rule will work in practice.

# Little's Law interpretation

| Context | Arrival rate per hour | Median arrival-to-clinician hours | Product | Mean queue-end snapshot | Gap |
|---|---:|---:|---:|---:|---:|
| Weeks 1-24, all shifts | 5.101935 | 1.625000 | 8.290644 | 8.286086 | 0.004557 |
| Weeks 25-52, all shifts | 4.901573 | 1.616667 | 7.924210 | 7.999681 | -0.075471 |
| Weeks 35-44, evening | 5.269643 | 1.933333 | 10.187976 | 9.702679 | 0.485298 |
| Weeks 45-52, evening | 5.470982 | 1.650000 | 9.027121 | 9.029018 | -0.001897 |

- Equilibrium status: `not established`
- Permitted use: `bounded consistency check only`
- Staffing use: `prohibited`

The arithmetic is close in three contexts, but the fields do not form a common stationary queue system. Lambda uses accepted arrivals, W is a median arrival-to-clinician elapsed time, and L is a mean queue-end snapshot. Priority, abandonment, blocking, changing capacity, and nonstationarity remain outside the equality. The check cannot solve for required staff or prove that the diagnosed stage caused the queue pattern.

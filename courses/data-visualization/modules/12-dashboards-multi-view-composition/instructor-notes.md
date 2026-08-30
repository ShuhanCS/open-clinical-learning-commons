# Module 12 instructor notes

## Teaching purpose

The module teaches dashboard restraint. A dashboard is not a collection of charts. It is a small decision system with a named audience, defined measures, visible freshness, owned thresholds, and actions.

The reference case deliberately uses historical public aggregate reporting. Learners must discover that the first dashboard action is to obtain current local data.

## Eight-and-a-half-hour plan

| Time | Activity |
|---|---|
| 0:00-0:35 | Audience, decision, owner, and action boundary. |
| 0:35-1:15 | Dashboard versus report, scorecard, and analysis page. |
| 1:15-2:00 | Measure dictionary and source-window audit. |
| 2:00-2:40 | Threshold ownership, alert states, and stale-data behavior. |
| 2:40-3:25 | Trace CMS source, teaching table, and selected hospital. |
| 3:25-4:20 | Run and inspect the five-view reference dashboard. |
| 4:20-5:10 | Critique C1 through C3. |
| 5:10-7:05 | Independent or scaffolded build. |
| 7:05-7:50 | Exact table, text alternative, and decision note. |
| 7:50-8:30 | Peer view-purpose audit and checkpoint handoff. |

## Opening question

Ask: What decision becomes easier after looking at this dashboard?

If the answer is vague, the dashboard is not ready. A monitoring surface that only helps the audience know more is still a report unless it supports a repeated task or action.

## Reference decision

The emergency department quality director decides whether to open a local definition and current-data review for the public OP-22 signal.

The supported answer is yes, because:

- Anna Jaques Hospital reports 23 percent;
- 23 is the highest observed value among 53 reported Massachusetts hospitals;
- the descriptive Massachusetts median is 3 percent;
- the mock teaching trigger is 10 percent; and
- the first action is validation and current local data.

The answer is not that current care is poor.

## Measured answers

| Question | Answer |
|---|---:|
| Complete CMS rows | 138,084 |
| Massachusetts selected rows | 186 |
| Massachusetts hospitals | 62 |
| Measures per hospital | 3 |
| EDV reported categories | 53 |
| OP_18b reported hospitals | 54 |
| OP_18b state median | 211.5 minutes |
| OP_18b state range | 113 to 336 minutes |
| Selected OP_18b | 188 minutes |
| Selected OP_18b sample | 422 |
| Selected OP_18b unfavorable rank | 45 |
| OP_18b mock trigger | 240 minutes, not crossed |
| OP_22 reported hospitals | 53 |
| OP_22 state median | 3 percent |
| OP_22 state range | 0 to 23 percent |
| Selected OP_22 | 23 percent |
| Selected OP_22 denominator | 19,211 |
| Selected OP_22 unfavorable rank | 1 |
| OP_22 mock trigger | 10 percent, crossed |
| OP_18b lag at release | 317 days |
| OP_22 lag at release | 590 days |

## Why Anna Jaques Hospital

The hospital provides a clear teaching case:

- CMS volume category is low;
- OP_22 is an observed peer extreme;
- OP_18b does not cross the mock trigger;
- the two measures do not tell one simple performance story; and
- both public values are historical by the release date.

The selection is for curriculum clarity, not public criticism.

## Five-view key

### View 1: alert

Answers: What needs attention and what should happen immediately?

It shows OP-22, state median, mock trigger, and validation action.

### View 2: freshness

Answers: Can the public value support current operational action?

It cannot. The view states both periods and lag.

### View 3: OP-22 peers

Answers: Where is the public score within reported Massachusetts hospital values?

The view is descriptive. It does not adjust for uncertainty, volume, case mix, or multiple comparison.

### View 4: OP-18b peers

Answers: Does another public ED measure show the same alert pattern?

No. The value is 188 minutes, below the descriptive state median and below the mock 240-minute trigger.

### View 5: action sequence

Answers: Who does what next?

The order prevents a jump from historical public aggregate to intervention.

## Why the units stay separate

OP-22 is a percent. OP_18b is a median number of minutes. They also use different reporting windows. A shared scale would manufacture comparability.

The two views may share layout, typography, and annotation conventions. They must not share a numeric axis.

## Threshold lesson

Thresholds need:

- a measure definition;
- a value and operator;
- a source or policy origin;
- an owner;
- an action;
- a review cadence;
- exception handling; and
- retirement or revision rules.

The course thresholds are mock QI charter assumptions. Learners lose credit if they call them CMS thresholds.

## Freshness lesson

A dashboard should define what happens when data are stale:

- show the period and release date;
- do not label the value current;
- suppress operational recommendations;
- identify the current local source needed; and
- assign a data owner.

Freshness is a decision property, not a cosmetic timestamp.

## Critique key

### C1: KPI wall

Eighteen equally prominent values have no hierarchy, owner, exception, or action. Repair by starting from the decision, keeping one alert and only the views needed to interpret and act.

### C2: mixed units and windows

Percent, minutes, and another percent have been converted to an invented common score. The title calls them current even though the windows differ. Restore original units and dates, then decide whether the measures belong together.

### C3: decorative widgets

The radial shapes show undefined composite percentages. There is no denominator, threshold owner, or action. Replace them with direct values and a decision path or remove them.

## Questions to ask learners

1. Who opens this dashboard?
2. What repeated task are they doing?
3. What is the one alert?
4. Who owns the trigger?
5. What action follows the alert?
6. Which view can be removed?
7. What happens when data are stale?
8. Why are the peer medians not benchmarks?
9. Why are OP-22 and OP-18b separate?
10. What current local source is needed?
11. What would make this an operational dashboard?
12. What evidence could support an intervention-effect claim?

## Common learner errors

### Calling the dashboard real-time

Require reporting-window and release-lag labels. Public reporting cadence does not become real-time because it appears on a dashboard.

### Treating the state median as a target

The median describes the observed reported hospitals. It does not establish acceptable performance.

### Using red and green alone

Require alert words, direct values, line types, and text actions. Color may support hierarchy but cannot carry status alone.

### Hiding unavailable facilities

The source release keeps all 62 facilities for each measure. Peer plots state their numeric reported count.

### Adding filters without a task

A filter is justified only when a named user needs to narrow a view to answer the decision. Decorative interactivity is removed.

### Adding every useful chart

The module caps the dashboard at five views. Additional analysis belongs in a linked detail report, not on the monitoring surface.

## Accessibility review

Check that:

- one alert is visually and verbally dominant;
- status is expressed in words;
- all values have units;
- peer references are labeled directly;
- dotted and dashed lines have text labels;
- reading order is clear;
- exact values are available in a table;
- the text alternative preserves view order and action; and
- no information depends on hover.

## Equity and action language

Do not blame patients for leaving before being seen. A real review should examine arrival patterns, wait communication, triage, language access, disability access, staffing, capacity, and other system conditions.

The public file does not support subgroup analysis. Do not imply that the value describes every patient group equally.

## AHRQ guidance use

The module links to AHRQ guidance about clear quality displays and dashboard practice. The linked dashboard PDF carries third-party copyright language, so the package does not reproduce it. Use the public page as background and teach the Commons contract directly.

## Human review roles before alpha

- emergency department quality clinician or leader;
- CMS measure and source reviewer;
- dashboard and information designer;
- equity and action-language reviewer;
- accessibility reviewer; and
- independent instructor.

## Checkpoint 2 handoff

Checkpoint 2 should require selected evidence from Modules 07 through 12, not six disconnected assignments. Learners submit:

- an accessible figure;
- a temporal or process figure;
- a multi-group comparison;
- a place or structural view;
- the Module 12 dashboard;
- exact tables and source records;
- a view-purpose audit;
- a critique repair; and
- a decision brief.

## Handoff to Module 13

Module 13 selects one analysis from the portfolio and reshapes it for two audiences. The measure definition, data values, uncertainty, source, and action boundary must remain stable even when titles, annotations, sequence, and explanatory depth change.

# Module 11 instructor notes

## Teaching purpose

This module is about defining structure before selecting a special chart. Learners should leave able to say exactly what a node, edge, ribbon, branch, area, count, and denominator mean.

The alluvial figure is not the learning outcome. The outcome is a defensible structure that conserves its unit and serves a decision.

## Eight-hour plan

| Time | Activity |
|---|---|
| 0:00-0:35 | Decision, action boundary, and synthetic-data contract. |
| 0:35-1:20 | Cohort, index event, observation windows, and one-person rule. |
| 1:20-2:05 | Nodes, edges, paths, direction, weights, and denominator audit. |
| 2:05-2:45 | Flow, matrix, composition, hierarchy, and network selection. |
| 2:45-3:25 | Trace source rows through cohort and edge releases. |
| 3:25-4:20 | Run and inspect the reference lab. |
| 4:20-5:10 | Critique C1 through C3. |
| 5:10-6:50 | Independent or scaffolded build. |
| 6:50-7:30 | Decision note, exact table, and text alternative. |
| 7:30-8:00 | Peer conservation audit and Module 12 handoff. |

## Opening question

Ask: What exactly moves through this picture?

Do not accept patient, visit, percentage, and money as interchangeable answers. The unit must remain stable through a conserved flow.

## Measured reference answers

| Question | Answer |
|---|---:|
| Source patients | 1,171 |
| Source encounters | 53,346 |
| Eligible adult cohort | 374 |
| Emergency index | 314 |
| Inpatient index | 60 |
| No encounter recorded within 30 days | 263 |
| Scheduled care within 30 days | 92 |
| Urgent care within 30 days | 4 |
| Acute return as first state within 30 days | 15 |
| Any acute return within 90 days | 36 |
| Death within 90 days | 8 |
| Full-cohort acute-return percentage | 9.6% |
| Reference screen path | Inpatient -> No encounter recorded |
| Reference path denominator | 38 |
| Reference path acute-return count | 6 |
| Reference path acute-return percentage | 15.8% |

## Why the reference path is selected

The declared teaching screen requires at least 20 patients and a path percentage above the cohort percentage. Only the inpatient-to-no-encounter-recorded path meets both conditions.

The action is a definition audit. The simulated team should inspect whether the cohort, encounter grouping, data boundaries, and absence definition behave as intended. The screen does not establish poor care, preventable return, or a valid benchmark.

## Cohort walk-through

Have learners trace one row through four tables:

1. Find the patient in the patient source selection.
2. Sort that patient's encounters by start time.
3. Confirm the first adult emergency or inpatient event in the window.
4. Find the first encounter after index stop and within 30 days.
5. Search 90 days for an acute return.
6. Check the death date.
7. Confirm the mutually exclusive endpoint.
8. Confirm the aggregate edge counts conserve the patient.

This trace is more important than learning a Sankey package.

## Structure selection guide

| Decision question | Preferred starting structure | Main risk |
|---|---|---|
| Where do conserved people move across a few states? | Alluvial flow plus exact table | Double counting or hidden attrition. |
| Which origin-destination cells are large or unusual? | Adjacency or transition matrix | Missing direction or denominator. |
| What share of each group ends in each state? | 100% stacked bar | Hidden group denominator. |
| How are nested categories divided? | Tree or indented table | Ambiguous parent-child membership. |
| How is volume partitioned among many categories? | Treemap only when exact comparison is secondary | Area misread as a rate. |
| Which entities are connected? | Filtered node-link view | Hairball, undefined edge, or false social meaning. |

## Why the flow and matrix both remain

The flow shows the complete sequence and conservation. The matrix makes the denominator direction and sparse combinations easier to read. Neither is redundant because the tasks differ.

The composition view answers a third question: how endpoint shares differ within emergency and inpatient index groups. Its denominator resets within each bar and must be stated.

## Critique key

### C1: changing denominator flow

The displayed 84%, 69%, and 30% do not share a denominator. A viewer may treat them as cohort retention because the bars resemble a funnel. Repair by showing counts from one initial denominator or by labeling every denominator and abandoning the funnel when the stages are not nested.

### C2: hairball network

The diagram provides no node definition, edge definition, direction, weight, time interval, or task. A matrix or ranked edge list is usually better for lookup and comparison. A node-link view becomes defensible only after the learner names a path-finding, neighborhood, bridge, or topology task and filters accordingly.

### C3: treemap conflict

Area represents volume while color and labels represent rate. The largest service has the lowest rate, but its area dominates. Repair with coordinated volume and rate charts or an ordered dot plot with volume labels.

## Questions to ask learners

1. What is the unit in every ribbon?
2. Can one person enter two index classes?
3. What is the denominator of 15.8%?
4. Why are 15 first acute returns not the same as 36 ninety-day acute returns?
5. What does death precedence change?
6. Does no encounter recorded mean no care?
7. What task does the flow solve better than the matrix?
8. What task does the matrix solve better?
9. When would a treemap be acceptable?
10. What must be known before drawing a real referral network?

## Common learner errors

### Counting encounters instead of people

Require a one-row-per-person cohort before visualization. Ask learners to prove uniqueness of `patient_id`.

### Starting follow-up at index start

The reference window begins after index stop. Starting at index start can count concurrent records as follow-up.

### Treating every later event as a new ribbon

The thirty-day state uses the first qualifying later encounter. The ninety-day acute indicator is a separate outcome field.

### Dropping absence

If people without a recorded next encounter disappear, the flow no longer conserves the cohort. Absence must be an explicit state.

### Encoding percentage as ribbon width

Ribbon width is a patient count. Rates appear in exact views with their denominators.

### Reading simulated output as evidence

Require the phrase synthetic or simulated in the title, subtitle, caption, decision note, and accessible alternative where the audience could otherwise mistake the result.

## Accessibility review

Check that:

- every node has text and count;
- index classes differ by labels as well as color;
- small ribbons do not carry essential text;
- the table contains exact values;
- the matrix labels every cell;
- the text alternative states the sequence and result;
- color contrast is adequate; and
- reading order follows the stages.

## Equity discussion

Race, ethnicity, and sex are present for context but are not used in the reference decision screen. Do not ask learners to make subgroup claims from small synthetic cells. A thoughtful extension may audit whether cohort definitions create differential missingness, but it must preserve cell sizes and keep the synthetic-data boundary.

## Optional ClinicalTrials.gov extension

Use https://clinicaltrials.gov/data-api/about-api to build a sponsor-condition-site relationship table. Require learners to define:

- node types;
- whether an edge means sponsorship, site participation, or condition assignment;
- direction;
- study status and date window;
- multi-arm or multi-site counting; and
- whether a matrix is better than a node-link diagram.

This is an extension, not a substitute for the conserved core cohort.

## Review roles before alpha

- transitions-of-care clinician or quality leader;
- Synthea source expert;
- flow and network visualization reviewer;
- equity and language reviewer;
- accessibility reviewer; and
- independent instructor.

## Handoff to Module 12

Module 12 should not simply place all three Module 11 figures on one screen. It must name a monitoring audience, retain only views tied to actions, define refresh cadence and thresholds, and preserve the cohort and denominator dictionary.

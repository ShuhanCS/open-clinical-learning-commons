# Pathway display and structured alternative

## Observed source-record pathway

The accepted cohort contains 476 landmark-eligible synthetic people. A qualifying scheduled-follow-up record is present by day 30 for 129 and absent for 347.

Among the 129 with a qualifying record, 25 have a later acute return and 104 do not. Among the 347 without a qualifying record, 62 have a later acute return and 285 do not. These branches are record patterns, not effects of follow-up.

Exact nodes are in `outputs/pathway-nodes.csv`; exact edges are in `outputs/pathway-edges.csv`.

## What is not observed

The retrospective source does not show whether follow-up was offered, wanted, accepted, scheduled before discharge, completed, inaccessible, unwanted, burdensome, or clinically appropriate. It also does not identify a reason when no qualifying record appears.

## Prospective collection path

For every eligible discharge, the proposed workflow records:

1. whether an offer was made;
2. the person's preference and acceptance or decline;
3. the appointment status before discharge, including capacity barriers and safe escalation; and
4. completion, cancellation, barriers, and reported burden.

In `outputs/pathway-figure.svg`, observed nodes use solid blue borders. Proposed data states use dashed green borders and say `not observed`. The words and border patterns carry the distinction without relying on color.

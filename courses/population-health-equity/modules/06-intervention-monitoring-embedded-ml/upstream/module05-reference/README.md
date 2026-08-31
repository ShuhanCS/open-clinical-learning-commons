# APP-5 Module 05: Targeting and fairness

This module asks a narrow question: which, if any, transparent fictional targeting rule is responsible enough to enter an intervention plan?

The release compares four rules under the same classroom constraint. Each rule receives 280 fictional program places, divided into 28 ten-place awards, across the same 1,597 accepted tract rows. The public CDC PLACES estimates remain modeled area-level context. Capacity, access, staff, review, objection, burden, and resource conditions are generated teaching data.

The four rules produce sharply different results. The equal geographic rule reaches all 14 counties but carries many access and burden gaps. The need-based rule reaches seven counties and selects 26 rows with the classroom support-review flag. The capacity-aware rule has the strongest fictional delivery capacity but reaches eight counties and retains one objection. The community-review rule reaches 11 counties and passes the declared review, access, objection, and capacity filters, but it still has travel, staff, and burden concerns.

The reference carries the community-review rule into Module 06 as the least unacceptable fictional planning candidate. That is not a real allocation decision. Real need, consent, priority, eligibility, outreach, funding, allocation, community action, service delivery, implementation, production connection, and deployment remain prohibited.

## Build the release

```powershell
$env:PYTHONDONTWRITEBYTECODE = "1"
python freeze_upstream.py
python generate_fictional_planning.py --verify
python build_targeting_fairness.py --verify
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Create a learner workspace:

```powershell
python build_workspace.py --target <new-folder>
python <new-folder>/validate_workspace.py <new-folder> --mode learner
```

Create the complete reference workspace:

```powershell
python build_workspace.py --target <new-folder> --reference
python <new-folder>/validate_workspace.py <new-folder>
```

The builder refuses to overwrite an existing target. Learner records contain `REPLACE` prompts. Reference records contain the accepted evidence and must not be distributed as learner answers.

## Assessment

The module contributes 15 points to the separate 25-point Week 6 checkpoint. A score of 12 is required, and all 26 noncompensable gates must pass. Module 06 construction may begin only from an accepted frozen handoff.

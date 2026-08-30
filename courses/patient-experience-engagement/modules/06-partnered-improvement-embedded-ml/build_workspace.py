"""Materialize and assemble APP-2 Module 06 learner or reference workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
import textwrap
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_FILES = (
    "upstream-inventory.csv", "analysis-checks.csv", "improvement-evidence.csv",
    "partner-question-register.csv", "transparent-weight-cells.csv", "split-registry.csv",
    "model-predictions.csv", "model-performance.csv", "calibration-bins.csv",
    "threshold-errors.csv", "response-weight-diagnostics.csv", "estimate-recovery.csv",
    "subgroup-model-audit.csv", "feature-importance.csv", "failure-cases.csv",
    "invariant-checks.csv", "build-report.json",
)
CONTROL_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "module06-contract.json",
    "feature-contract.csv", "partner-contract.csv", "environment.yml", "assessment.md",
    "build_partnered_improvement_ml.py", "build_workspace.py", "validate_workspace.py",
)
WORK_FILES = (
    "README.md", "engagement-status.md", "patient-partner-session.md",
    "interpretation-disagreement.csv", "improvement-brief.md", "driver-diagram.csv",
    "workflow.csv", "measure-registry.csv", "burden-access-review.md",
    "feedback-accountability.md", "ml-comparison.md", "failure-case-review.md",
    "responsible-claims.md", "reproducibility-check.md", "ai-use.md",
    "gate-results.csv", "progression-decision.md",
)
IMMUTABLE_FILES = CONTROL_FILES + tuple(f"outputs/{name}" for name in OUTPUT_FILES)


def clean(text: str) -> str:
    return textwrap.dedent(text).lstrip().replace("\r\n", "\n")


REFERENCE = {
    "README.md": """
        # APP-2 Module 06 reference workspace

        This 16-hour module uses eight hours for patient partnership and improvement design and eight hours for a bounded response-model comparison. Start with `engagement-status.md` and `patient-partner-session.md`. Then complete the improvement records before interpreting the model outputs.

        The reference partnership record is a simulated curriculum example. It contains no real patient or caregiver statement and cannot satisfy the alpha requirement for a named partner. All response outcomes are synthetic. Comment text is excluded from model training.

        The technical question is whether a bounded random forest materially changes the response-adjustment decision compared with the training-only cell-weight benchmark. The answer is recorded in `ml-comparison.md`. Module 06 adds no points. Its 24 gates are required for the cumulative 45-point Week 6 release.
    """,
    "engagement-status.md": """
        # Engagement status

        - Record type: `simulated curriculum reference, not actual patient engagement`
        - Named patient or caregiver partner: `pending before alpha`
        - Actual patient or caregiver statements in this package: `0`
        - Compensation agreement: `example terms only; direct agreement pending`
        - Decision rights: `example permits adding questions, revising language, narrowing, deferring, or stopping the proposal`
        - Access review: `language, format, disability, technology, proxy, scheduling, and non-digital options included for direct review`
        - Privacy and recording: `recording off by default; direct consent required`
        - Attribution: `no public attribution without direct permission`
        - Disagreement: `retained without forced consensus`
        - Final record review: `direct partner review pending before alpha`

        Construction may use this simulation to test the learning workflow. An actual session must replace simulated interpretations before alpha use.
    """,
    "patient-partner-session.md": """
        # Patient-partner session

        ## Purpose

        Review what the accepted evidence can and cannot say before deciding whether an accessible discharge-information and feedback workflow is worth leadership review.

        ## Reference format

        This is a 90-minute simulated curriculum session. Materials are sent one week ahead in plain-language digital and print-ready formats. The agenda allows breaks and does not require video, a portal, or recorded participation.

        ## Evidence reviewed

        The packet includes the 1,255-record target and response flow, Module 04 access and communication evidence, Module 05 group support and suppressed cells, the two lower-income teaching contrasts, synthetic comment themes, the channel audit, and the list of unmeasured constructs.

        ## Decision rights

        The simulated partner role may add a question, reject wording, require another access option, narrow the proposal, defer it, or stop it. The team owns technical corrections. The partner role owns the acceptability of patient-facing language and whether the record fairly represents the discussion.

        ## Outcome

        The simulated record supports leadership review with conditions. It changes the proposal from a digital follow-up concept to a universal choice among phone, mail, web, interpreter-supported, proxy-supported, and no-contact options. It adds burden, unwanted contact, return of results, and stop measures. This is a curriculum result, not an actual partner decision.
    """,
    "interpretation-disagreement.csv": """
        record_id,evidence,simulated_partner_interpretation,team_interpretation,disagreement,revision,owner,status,data_class
        D01,lower-income delayed-cost contrast,cost may also come from transport time phone service or unpaid caregiving,the source records delayed care because of cost only,yes,ask about several cost sources and do not claim mechanism,improvement lead,resolved in simulation,simulated_reference
        D02,lower-income telehealth contrast,lower use does not tell us whether telehealth was unavailable unwanted or unsuitable,the source records linked event use only,no,keep non-digital options and list mechanism as unknown,methods lead,resolved in simulation,simulated_reference
        D03,provider-language estimate,an apparently high percentage can hide people who never reached the denominator,the estimate has only 45 valid records,yes,show denominator and limited support before percentage,survey lead,resolved in simulation,simulated_reference
        D04,synthetic comment themes,theme counts can make invented examples sound like patient priorities,the corpus only teaches coding,no,remove priority language and label every theme count synthetic,qualitative lead,resolved in simulation,simulated_reference
        D05,follow-up contact,a response goal could pressure people who do not want contact,the initial concept assumed a follow-up offer,yes,record no-contact choice and unwanted-contact balancing measure,workflow lead,resolved in simulation,simulated_reference
        D06,digital channel,a web option can become a digital requirement even when alternatives are listed,the team planned several channels,yes,make phone and mail operational pathways rather than exceptions,access lead,resolved in simulation,simulated_reference
        D07,Q22 and Q23,yes answers do not show that information was timely understandable or usable,the items record whether information was given,no,add prospective clarity and burden questions without altering official items,measurement lead,resolved in simulation,simulated_reference
        D08,return of results,collecting feedback without showing what changed repeats the burden,the team planned an internal review,yes,add a dated patient-facing response and advisory-group review,accountability owner,resolved in simulation,simulated_reference
    """,
    "improvement-brief.md": """
        # Improvement brief

        - Decision: `advance a bounded universal-offer proposal to Checkpoint 02 and Module 07 with conditions`
        - Aim: `test whether an accessible discharge-information and feedback workflow can improve reported understanding without adding avoidable burden`
        - Population: `all eligible discharges in a future local test; no model-selected group`
        - Change: `record language, channel, format, proxy, and contact choice; check warning-sign and help-source understanding; offer several follow-up routes; return aggregate findings`
        - Evidence status: `public-derived and synthetic teaching evidence supports questions and design work, not expected benefit`
        - Patient-partner status: `simulated reference only; actual named partner review required before alpha`
        - Access alternatives: `phone, mail, web, interpreter-supported, proxy-supported, accessible format, and no contact`
        - Stop rule: `stop or redesign if access alternatives are unavailable, unwanted contact rises, burden exceeds the agreed limit, safety routing fails, support rules fail, or actual partners reject the proposal`
        - Prohibited: `fielding, patient targeting, official HCAHPS reporting, clinical action, implementation, and model deployment`

        The proposal retains unchanged Q22 and Q23 for teaching measurement. Any local clarity or burden question is a prospective improvement measure and cannot be called validated without separate evidence.
    """,
    "driver-diagram.csv": """
        row_id,level,parent,statement,measure_link,simulated_partner_note,status
        DD01,aim,none,Improve understandable discharge information without adding avoidable burden,M07 and M10,understanding and burden must move together,proposed
        DD02,primary driver,DD01,Patient choice and decision rights,M02 and M11,no-contact is a valid choice,required
        DD03,primary driver,DD01,Understandable warning-sign and help-source information,M04 and M07,information must be usable when tired or worried,required
        DD04,primary driver,DD01,Language and communication access,M03 and M09,do not infer language need from a category,required
        DD05,primary driver,DD01,Reliable workflow ownership,M01 and M05,a choice without an owner is not an option,required
        DD06,primary driver,DD01,Feedback and accountability,M12,patients should see what changed,required
        DD07,secondary driver,DD02,Consent and contact preference at each contact,M02 and M11,avoid pressure to respond,required
        DD08,secondary driver,DD03,Plain-language teach-back with decline option,M04,do not turn teach-back into a compliance test,required
        DD09,secondary driver,DD04,Phone mail web interpreter proxy and accessible formats,M03 and M09,alternatives must work in practice,required
        DD10,secondary driver,DD05,Named owner and safe escalation route,M05 and M13,record failures instead of hiding them,required
        DD11,candidate change,DD07,Preference record with no-contact choice,M02 and M11,review wording with actual partners,pending alpha review
        DD12,candidate change,DD08,Unchanged discharge content plus understanding check,M04 and M07,keep official items separate,proposed
        DD13,candidate change,DD09,Parallel non-digital contact paths,M03 and M09,do not make web the default,pending capacity review
        DD14,candidate change,DD10,Dated patient-facing results and revision log,M12,feedback must close the loop,proposed
    """,
    "workflow.csv": """
        step_id,step,owner,timing,input,output,access_alternative,failure_mode,failure_response,stop_rule
        W01,identify eligible discharge,discharge team,before discharge,eligibility rule,eligibility record,manual review,wrong exclusion,correct record and audit rule,repeated identity errors
        W02,offer participation,trained staff,before discharge,eligibility record,offer or no-offer reason,interpreter or proxy-supported offer,offer not made,record reason and review capacity,systematic missing offers
        W03,record preferences,trained staff,before contact,patient choice,language channel format proxy and no-contact choices,phone mail web accessible format,choice inferred,delete inference and ask directly,inference cannot be prevented
        W04,confirm contact consent,trained staff,before follow-up,contact choice,consent status,no-contact choice,pressure or unclear consent,stop contact and correct process,consent failure
        W05,review discharge information,clinical discharge owner,before discharge,unchanged discharge content,content delivered or declined,interpreter and accessible format,content unavailable,use safe existing escalation route,unsafe or inaccurate content
        W06,check understanding,trained staff,before discharge,warning-sign and help-source content,completed declined or unable status,proxy or interpreter-supported check,check becomes a test,stop and retrain staff,repeated coercive use
        W07,route question,clinical owner,before discharge,unresolved question,documented safe route,phone or in-person route,incorrect advice route,use approved escalation and incident review,safety routing failure
        W08,make follow-up attempt,feedback team,agreed time,consent and channel choice,attempt status,chosen non-digital route,wrong channel or unwanted contact,stop contact and record event,unwanted-contact limit crossed
        W09,collect feedback,feedback team,agreed time,attempt and consent,response or nonresponse,plain-language phone mail or web,burden or inaccessible form,offer alternative or end contact,burden limit crossed
        W10,monitor missing voice,analyst,weekly,opportunities responses and missing items,response dashboard,suppressed accessible table,unsupported group display,blank estimate and review process,support rule failure
        W11,review with patient advisory group,accountability owner,monthly,bounded aggregate evidence,interpretation disagreement and revision record,accessible meeting and asynchronous review,partner access unmet,reschedule with required support,partner terms unmet
        W12,return results,accountability owner,within agreed interval,approved aggregate record,patient-facing response,print phone web and accessible formats,no visible change or explanation,record owner date and reason,repeated failure to return results
    """,
    "measure-registry.csv": """
        measure_id,type,name,numerator,denominator,exclusions,timing,owner,source,stratification,missingness_rule,interpretation,failure_response
        M01,implementation,workflow availability,eligible discharges with workflow available,all eligible discharges,documented rule exclusions,weekly,implementation owner,prospective workflow record,none,missing status stays missing,availability is not use or benefit,review staffing and access capacity
        M02,process,universal offer,eligible discharges with offer recorded,all eligible discharges,none,weekly,workflow owner,prospective offer record,prespecified groups if supported,no record is not an offer,offer measures reach not preference,review missed offers
        M03,process,access preference recorded,people with language channel format proxy and contact choices recorded,people offered participation,declines remain in denominator,weekly,access owner,prospective preference record,prespecified groups if supported,do not infer missing preference,documentation is not access quality,repair collection process
        M04,process,understanding check,people completing or declining the check,people receiving discharge information,clinical exemption documented,weekly,discharge owner,prospective workflow record,prespecified groups if supported,unable and missing remain separate,completion is not understanding,review workflow and burden
        M05,process,safe question routing,unresolved questions with approved route documented,all unresolved questions,none,weekly,clinical owner,prospective escalation record,none,missing route is a safety failure,routing is not resolution,stop unsafe route and investigate
        M06,response,feedback return,completed feedback responses,all consented follow-up opportunities,withdrawn consent excluded with count,weekly,feedback owner,prospective response record,channel and supported groups,total nonresponse stays visible,response is not representativeness,review coverage and alternatives
        M07,outcome,Q22 yes,item-answering yes responses,item-answering yes plus no,not applicable under item rule,reporting cycle,survey lead,unchanged accepted item,separate supported groups,item missingness reported separately,teaching result is not official adjusted HCAHPS,review measure and response process
        M08,outcome,Q23 yes,item-answering yes responses,item-answering yes plus no,not applicable under item rule,reporting cycle,survey lead,unchanged accepted item,separate supported groups,item missingness reported separately,teaching result is not official adjusted HCAHPS,review measure and response process
        M09,access,operational alternatives,offers with requested channel language and format available,offers requesting an alternative,no request excluded with count,weekly,access owner,prospective service record,prespecified groups if supported,unavailable is not missing,availability is not acceptability,repair or stop unavailable pathway
        M10,balancing,reported burden,respondents reporting burden above agreed limit,people answering burden item,item refusal remains visible,weekly,patient-experience owner,prospective unvalidated burden item,channel and supported groups,item missingness reported,local item is not a validated scale,revise workflow with partners
        M11,balancing,unwanted contact,contacts marked unwanted or against preference,all follow-up contacts,none,weekly,privacy owner,prospective contact log,channel and supported groups,missing preference is a process failure,one event requires review,stop contact and investigate
        M12,accountability,results returned on time,review cycles with dated patient-facing response,all completed review cycles,none,monthly,accountability owner,feedback return log,none,missing date fails measure,return may include no change with reason,assign owner and correction date
        M13,safety,failed escalation,questions with incorrect delayed or missing safe route,all questions requiring escalation,none,immediate,clinical safety owner,incident record,none,missing resolution remains open,not an outcome attribution,stop unsafe process and review
        M14,balancing,staff time,minutes spent on workflow steps,completed workflow opportunities,none,weekly,operations owner,time sample,role and channel,missing sample count reported,time does not measure patient value,adjust staffing or workflow
    """,
    "burden-access-review.md": """
        # Burden and access review

        - Language: `ask directly; offer interpreter and translated material; do not infer need from other-language field`
        - Disability access: `offer large text, screen-reader-ready text, captioned or relay-supported contact, plain language, proxy support, and breaks according to direct need`
        - Channel: `phone, mail, web, in-person support when available, and no contact are first-class choices`
        - Cost: `ask about phone, data, transport, time, caregiving, interpreter, and lost-work burden without assuming a mechanism`
        - Technology: `no portal account, smartphone, video, or broadband requirement`
        - Proxy: `record patient permission and the proxy role; do not assume proxy access is harmless or preferred`
        - Privacy: `confirm safe channel and message detail before contact; recording remains off without direct consent`
        - Cognitive load: `short materials, one decision at a time, plain wording, optional pause, and decline without penalty`
        - Missing voice: `report total nonresponse and item missingness; unsupported group estimates stay blank`
        - Stop condition: `stop or redesign when a required alternative is unavailable or burden and unwanted-contact limits are crossed`

        These are proposal requirements from a simulated review. Actual partners must confirm which options matter and how burden should be measured before alpha.
    """,
    "feedback-accountability.md": """
        # Feedback and accountability

        The improvement owner prepares a bounded aggregate summary after each review cycle. It shows opportunities, responses, item missingness, supported group evidence, suppressed cells, burden, unwanted contact, safety routing, and open disagreements. It does not publish synthetic comments as patient voice or expose small groups.

        A patient advisory group reviews the summary in an accessible format. The team records each requested change, owner, due date, disposition, and reason. Within the agreed interval, patients receive a plain-language response through print, phone, web, and accessible formats. The response says what changed, what did not change, why, and what remains open.

        Failure to return results on time is a measured accountability failure. Repeated failure stops progression until ownership and capacity are repaired.
    """,
    "ml-comparison.md": """
        # Transparent versus ML response adjustment

        - Population: `1,255 accepted frame records with 878 training and 377 evaluation rows`
        - Held-out response: `235 respondents and 142 nonrespondents`
        - Eligible fields: `age_band, other_language_at_home, and income_group for both methods`
        - Transparent method: `training-only base-weighted response cells with factors from 1.0 through 3.0`
        - ML method: `one bounded random forest with prespecified settings and training base weights`
        - Transparent Brier score: `0.22962545`
        - ML Brier score: `0.23135127`
        - ML minus transparent Brier: `0.00172582`
        - Transparent AUC: `0.54335192`
        - ML AUC: `0.53869891`
        - Transparent weighted teaching error cost: `227`
        - ML weighted teaching error cost: `225`
        - Transparent adjusted composite absolute bias: `2.48289986 percentage points`
        - ML adjusted composite absolute bias: `2.39922466 percentage points`
        - Composite improvement: `0.08367520 percentage points`
        - Weight stability: `both pass`
        - Decision: `ML does not change the response-adjustment decision because the composite improvement is below 0.50 percentage points`

        The small error-cost advantage does not override the prespecified rule or the worse Brier and AUC values. The transparent benchmark remains the teaching adjustment. Neither method repairs item nonresponse or omitted selection fields, and neither may be used for patient targeting.
    """,
    "failure-case-review.md": """
        # Failure-case review

        The generated review contains 22 held-out rows with a threshold disagreement, a factor-cap hit, or a factor difference of at least 0.50. Each record is a synthetic response case and carries no clinical story.

        The transparent benchmark has 88 false positives and 51 false negatives at the fixed 0.60 threshold. The random forest has 85 false positives and 55 false negatives. Three evaluation respondents receive a transparent factor of 3.0; the ML factors do not reach the cap.

        The model uses the same three fields as the transparent response cells. It intentionally omits assigned mode, health status, proxy status, and the synthetic item truth used by the known generator. Residual bias is therefore expected. Adding those fields after reviewing held-out results would violate the feature contract.

        Unsupported subgroup metrics stay blank for the missing-language, uninsured, Asian, and other-or-multiple-race rows. These blanks do not prove equal performance. They record insufficient support.

        No error pattern permits comment-text modeling, group-specific contact, patient targeting, official reporting, fielding, or deployment.
    """,
    "responsible-claims.md": """
        # Responsible claims

        The package may state that one prespecified random forest did not materially change the held-out synthetic response-adjustment decision. It may report exact calibration, error, weight, and known-truth recovery results with their teaching boundaries.

        It may not state that either method is fair, clinically useful, field ready, official, or suitable for targeting. The group audit is descriptive and support-limited. Race, insurance, and other audit fields are not model predictors.

        The improvement evidence supports a question and a proposed workflow, not proof of benefit. The Module 05 comments and this module's partner record are simulated. They cannot be described as patient testimony or actual engagement.

        Actual patient or caregiver review, named methods and accessibility reviews, local workflow evidence, capacity review, governance, and leadership authorization remain required before any test. Model deployment remains prohibited.
    """,
    "reproducibility-check.md": """
        # Reproducibility check

        - Python: `3.12.10`
        - NumPy: `2.0.2`
        - pandas: `3.0.3`
        - scikit-learn: `1.9.0`
        - Source inputs: `13 exact files verified by size and SHA-256`
        - Split: `stratified 70/30 with random_state 20260830`
        - Model: `200 trees, depth 3, minimum leaf 25, max_features None, n_jobs 1`
        - Determinism: `two builds match byte for byte`
        - Mutation check: `changed response input rejected`
        - Existing target: `overwrite rejected`
        - Outputs: `17 deterministic files`
        - Result: `pass`

        Run `python build_partnered_improvement_ml.py --self-check`, `python build_workspace.py --self-check`, and `python validate_workspace.py --self-check` from the module or repository environment.
    """,
    "ai-use.md": """
        # AI use

        OpenAI Codex helped draft the specification, deterministic build, simulated reference records, and validation controls. The random forest is the only machine-learning model in the analysis. No model reads comment text.

        Human review remains required for patient-partner interpretation, qualitative coding, group claims, accessibility, language access, privacy, clinical safety, governance, and any progression decision. The simulated partnership record is not human patient review.

        AI output cannot authorize fielding, contact, targeting, official reporting, clinical action, implementation, or deployment.
    """,
    "gate-results.csv": """
        gate_id,gate,evidence,status,condition
        G01,accepted upstream identities,upstream-inventory.csv,pass,none
        G02,one-to-one frame identities,analysis-checks.csv CHK04,pass,none
        G03,data classes separated,source-record.yml and engagement-status.md,pass,retain labels
        G04,simulation not actual engagement,engagement-status.md,pass,named actual partner required before alpha
        G05,partnership terms complete,partner-contract.csv,pass,direct agreement required before alpha
        G06,interpretation and disagreement recorded,interpretation-disagreement.csv,pass,replace simulation before alpha
        G07,no proof-of-inequity or cause claim,responsible-claims.md,pass,named equity review pending
        G08,support and suppression retained,subgroup-model-audit.csv,pass,unsupported metrics stay blank
        G09,synthetic comments bounded,responsible-claims.md,pass,human qualitative review pending
        G10,improvement package complete,driver-diagram.csv workflow.csv and measure-registry.csv,pass,local capacity review pending
        G11,no retrospective proxy for prospective field,workflow.csv,pass,prospective collection required
        G12,comment text and prohibited predictors excluded,feature-contract.csv,pass,none
        G13,same fields and split,module06-contract.json and split-registry.csv,pass,none
        G14,training-only preprocessing,module06-contract.json and build script,pass,independent model review pending
        G15,one bounded ML model,module06-contract.json,pass,no model search
        G16,calibration errors costs and weights complete,calibration-bins.csv threshold-errors.csv and response-weight-diagnostics.csv,pass,none
        G17,known-truth recovery complete,estimate-recovery.csv,pass,item nonresponse remains
        G18,subgroup support enforced,subgroup-model-audit.csv,pass,no merging or ranking
        G19,failure cases reviewed,failure-case-review.md and failure-cases.csv,pass,none
        G20,prespecified ML decision used,ml-comparison.md,pass,ML does not change decision
        G21,ML does not replace people or transparent method,ml-comparison.md and engagement-status.md,pass,actual partnership pending
        G22,prohibited uses retained,responsible-claims.md,pass,fielding and deployment prohibited
        G23,workspace reproduces,reproducibility-check.md,pass,independent reproduction pending
        G24,points and progression consistent,progression-decision.md,pass,Checkpoint 02 must carry 25 plus 20 once
    """,
    "progression-decision.md": """
        # Progression decision

        - Module 04 score: `25.00 of 25.00, carried into the Week 6 checkpoint exactly once`
        - Module 05 score: `20.00 of 20.00, carried into the Week 6 checkpoint exactly once`
        - Module 06 points: `0`
        - Module 06 gates: `24 of 24 pass for curriculum construction`
        - Week 6 score: `45.00 of 45.00`
        - Progression: `continue with conditions`
        - Checkpoint 02 permission: `permitted for cumulative assembly`
        - ML changes response-adjustment decision: `no`
        - Teaching adjustment: `retain transparent benchmark`
        - Patient-partner status: `simulated reference only; named actual partner review required before alpha`
        - Continuing conditions: `named faculty, patient or caregiver, survey, qualitative, health-services data, equity, accessibility, language-access, privacy, responsible-AI, clinical, governance, model, and independent reproduction reviews`
        - Comment-text machine learning: `prohibited`
        - Patient targeting and group ranking: `prohibited`
        - Official reporting, fielding, clinical action, implementation, and model deployment: `prohibited`
    """,
}


TEMPLATE = {
    "README.md": "# APP-2 Module 06 learner workspace\n\nREPLACE: identify your team roles, schedule, and order of work. State that Module 06 adds no points and that every gate is required.\n",
    "engagement-status.md": "# Engagement status\n\nREPLACE: record the partner role, compensation, access, privacy, decision rights, disagreement, attribution, and review status. Do not present a simulation as actual engagement.\n",
    "patient-partner-session.md": "# Patient-partner session\n\nREPLACE: document purpose, materials, access, evidence reviewed, decisions, disagreements, revisions, and final partner review.\n",
    "interpretation-disagreement.csv": "record_id,evidence,partner_interpretation,team_interpretation,disagreement,revision,owner,status,data_class\nREPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE\n",
    "improvement-brief.md": "# Improvement brief\n\nREPLACE: state the decision, aim, population, bounded change, evidence limits, access alternatives, burden rule, feedback route, and stop rule.\n",
    "driver-diagram.csv": "row_id,level,parent,statement,measure_link,partner_note,status\nREPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE\n",
    "workflow.csv": "step_id,step,owner,timing,input,output,access_alternative,failure_mode,failure_response,stop_rule\nREPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE\n",
    "measure-registry.csv": "measure_id,type,name,numerator,denominator,exclusions,timing,owner,source,stratification,missingness_rule,interpretation,failure_response\nREPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE,REPLACE\n",
    "burden-access-review.md": "# Burden and access review\n\nREPLACE: review language, disability access, channel, cost, technology, proxy, privacy, cognitive load, missing voice, and stop conditions.\n",
    "feedback-accountability.md": "# Feedback and accountability\n\nREPLACE: name what returns to patients, in which formats, by what date, who owns it, how disagreement is retained, and what happens if the team does not respond.\n",
    "ml-comparison.md": "# Transparent versus ML response adjustment\n\nREPLACE: compare the same fields and held-out rows using Brier, AUC, log loss, calibration, errors, costs, weights, known-truth recovery, and the prespecified decision rule.\n",
    "failure-case-review.md": "# Failure-case review\n\nREPLACE: review threshold disagreements, factor caps, omitted generator fields, residual bias, item nonresponse, support blanks, leakage, targeting, and deployment limits.\n",
    "responsible-claims.md": "# Responsible claims\n\nREPLACE: separate supported teaching claims from prohibited claims about patient voice, inequity, fairness, official reporting, fielding, targeting, implementation, and deployment.\n",
    "reproducibility-check.md": "# Reproducibility check\n\nREPLACE: record environment, source checks, split, model settings, commands, deterministic results, mutation rejection, and unresolved reproduction issues.\n",
    "ai-use.md": "# AI use\n\nREPLACE: record every AI-assisted task, input class, human review, prohibited use, and whether any model accessed comment text.\n",
    "gate-results.csv": "gate_id,gate,evidence,status,condition\nREPLACE,REPLACE,REPLACE,REPLACE,REPLACE\n",
    "progression-decision.md": "# Progression decision\n\nREPLACE: record the 25 plus 20 point carry once, all 24 gates, ML decision, partnership status, conditions, prohibited uses, and Checkpoint 02 disposition.\n",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def materialize() -> dict[str, object]:
    reference = MODULE_ROOT / "reference"
    template = MODULE_ROOT / "template"
    if reference.exists() or template.exists():
        raise FileExistsError("Refusing to overwrite existing reference or template records")
    if set(REFERENCE) != set(WORK_FILES) or set(TEMPLATE) != set(WORK_FILES):
        raise ValueError("Record dictionaries do not match workspace contract")
    reference.mkdir()
    template.mkdir()
    for name in WORK_FILES:
        (reference / name).write_text(clean(REFERENCE[name]), encoding="utf-8", newline="\n")
        (template / name).write_text(clean(TEMPLATE[name]), encoding="utf-8", newline="\n")
    return {"status": "pass", "reference_records": len(REFERENCE), "template_records": len(TEMPLATE)}


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = MODULE_ROOT / ("reference" if reference else "template")
    missing = [name for name in IMMUTABLE_FILES if not (MODULE_ROOT / name).is_file()]
    missing += [name for name in WORK_FILES if not (record_root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in IMMUTABLE_FILES:
        source = MODULE_ROOT / relative
        copy(source, target, relative)
        role = "immutable source model assessment or executable control"
        if relative.startswith("outputs/"):
            role = "immutable partnered-improvement and response-model evidence"
        manifest.append({"relative_path": relative, "bytes": source.stat().st_size, "sha256": sha256(source), "role": role})
    for relative in WORK_FILES:
        copy(record_root / relative, target, relative)
    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("relative_path", "bytes", "sha256", "role"), lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    if len(manifest) != 28 or files != 46:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module06-workspace-") as temp_dir:
        root = Path(temp_dir)
        first, second, learner = root / "first", root / "second", root / "learner"
        one = assemble(first, reference=True)
        two = assemble(second, reference=True)
        starter = assemble(learner)
        assert one == two
        assert all(path.read_bytes() == (second / path.relative_to(first)).read_bytes() for path in first.rglob("*") if path.is_file())
        assert one["assembled_files"] == starter["assembled_files"] == 46
        assert "REPLACE" not in (first / "ml-comparison.md").read_text(encoding="utf-8")
        assert "REPLACE" in (learner / "ml-comparison.md").read_text(encoding="utf-8")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace assembler overwrote an existing target")
    print("APP-2 Module 06 workspace self-check passed: deterministic 28-row manifests and 46-file assemblies.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--materialize-records", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.materialize_records:
            print(json.dumps(materialize(), indent=2))
            return
        if args.self_check:
            self_check()
            return
        if not args.target:
            parser.error("--target is required")
        print(json.dumps(assemble(args.target, reference=args.reference), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Assembly failed: {error}\n")


if __name__ == "__main__":
    main()

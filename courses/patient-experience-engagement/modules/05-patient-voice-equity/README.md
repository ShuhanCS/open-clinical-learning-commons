# APP-2 Module 05: Patient voice, group differences, and equity

This 16-hour module asks which patient-voice and group-difference findings are ready for patient-partner co-design. It uses the accepted 1,255-person MEPS-derived teaching table, 28,455 linked events, and a fully synthetic 420-comment corpus. No comment is patient testimony.

## What you will do

You will define the comment opportunity, code a fixed audit sample, calculate agreement, adjudicate disagreement, test a transparent assisted-coding rule, review survey-weighted group comparisons, suppress unsupported estimates, and write a 20-point equity and patient-voice memo.

The four public group dimensions are language spoken at home, income group, insurance coverage, and race and ethnicity. The four measures are delayed care because of cost, difficult after-hours contact, involvement in decisions, and any linked telehealth event. A recorded difference can raise an equity question. It does not prove inequity, cause, preference, or a group trait.

## Build and check the evidence

```powershell
python build_patient_voice.py --verify-committed
python build_patient_voice.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Build a learner workspace:

```powershell
python build_workspace.py --target <new-directory>
python validate_workspace.py <new-directory> --learner
```

Build the completed reference:

```powershell
python build_workspace.py --target <new-directory> --reference
python validate_workspace.py <new-directory>
```

Each command refuses to overwrite an existing target.

## Source boundary

The five immutable handoff files total 5,297,691 bytes. Their source inventory points to all 25 official AHRQ MEPS HC-256 and HC-254D through HC-254G files retained by Module 04. The generated comments, collection channels, access offers, coder records, and return process are synthetic teaching data.

The module has no portal-access or portal-preference measure. Machine learning remains in Module 06. No package authorizes clinical action, patient targeting, group ranking, causal inference, or implementation.

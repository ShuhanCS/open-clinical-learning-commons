"""Build APP-2 Module 05 synthetic patient-voice and public group evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable


MODULE_ROOT = Path(__file__).resolve().parent
UPSTREAM_ROOT = MODULE_ROOT / "data" / "upstream"
SEED = "oclc-app2-05-v1"
THEMES = (
    "communication_clarity", "medication_help", "warning_signs", "access_after_hours",
    "cost_barrier", "digital_channel", "respect_involvement", "other_or_unclear",
)
THEME_COUNTS = {
    "communication_clarity": 76,
    "medication_help": 58,
    "warning_signs": 54,
    "access_after_hours": 52,
    "cost_barrier": 42,
    "digital_channel": 38,
    "respect_involvement": 60,
    "other_or_unclear": 40,
}
UPSTREAM_RULES = {
    "module04-release.json": (5063, "de31b805351946d644dccc5125deffdffdb993470fbdd74670278c2ca6e7e1d0"),
    "module04-linked-persons.csv": (476048, "3605f17995f4f3020572dd23ac008a17db9ca78980d15d6a2faadb1efd5e8f24"),
    "module04-linked-events.csv": (4808211, "16cbb65d1dc0925f4257c73b574617803f05feacbebba134fec3396dd5788997"),
    "module04-source-inventory.csv": (6596, "63060f9773f38c1ff2d72a51b2d6561725d6263685f7eda7f67a0cf5649988b7"),
    "module04-denominator-registry.csv": (1773, "7263d5c2b4add3eef5493f9c499e711b70f2f31edf90ef649fa56d4a5f61d4de"),
}
THEME_LABELS = {
    "communication_clarity": "Communication clarity",
    "medication_help": "Medication help",
    "warning_signs": "Warning signs",
    "access_after_hours": "Access after hours",
    "cost_barrier": "Cost barrier",
    "digital_channel": "Digital channel",
    "respect_involvement": "Respect and involvement",
    "other_or_unclear": "Other or unclear",
}
CODEBOOK = {
    "communication_clarity": ("clarity or consistency of the discharge explanation", "medicine timing, warning signs, or access as the main issue", "instructions; explanation; written plan"),
    "medication_help": ("understanding medicine names, changes, timing, or purpose", "cost alone or general communication without medicine content", "medicine; medication"),
    "warning_signs": ("symptoms or changes that should lead to a call or urgent help", "general follow-up access without a symptom cue", "warning signs; symptoms; urgent"),
    "access_after_hours": ("finding help outside regular hours", "digital format or routine appointment scheduling alone", "after regular hours; evening; weekend"),
    "cost_barrier": ("cost, affordability, or a lower-cost option", "insurance category without a stated cost concern", "cost; lower-cost"),
    "digital_channel": ("video, online, device, or phone-versus-digital format", "general telephone access without a digital format question", "video; online; digital; device"),
    "respect_involvement": ("being heard, included, or involved in the plan", "clarity alone without involvement", "choose; listened; included"),
    "other_or_unclear": ("a comment without enough information for another theme", "any comment with a clear primary theme", "no qualifying phrase"),
}
TEMPLATES = {
    "communication_clarity": (
        "The instructions used clear words, but I still had one question about care at home.",
        "I wanted a shorter explanation of the plan before leaving.",
        "The written plan and spoken explanation did not match for me.",
    ),
    "medication_help": (
        "I needed more help understanding when to take each medicine.",
        "The medicine list was hard to follow after I got home.",
        "I knew which medicines changed, but not why.",
    ),
    "warning_signs": (
        "I was not sure which warning signs meant I should call for help.",
        "I wanted clearer guidance about symptoms that need urgent attention.",
        "The plan did not say when a change should lead me to call.",
    ),
    "access_after_hours": (
        "I did not know who to contact after regular hours.",
        "It was hard to find help during the evening or weekend.",
        "The plan named a phone number but did not explain when it was available.",
    ),
    "cost_barrier": (
        "The cost of the recommended follow-up made the plan harder to carry out.",
        "I had questions about what the visit or medicine would cost.",
        "The plan did not include a lower-cost option.",
    ),
    "digital_channel": (
        "The video visit worked, but I still needed a phone option.",
        "I could not tell whether the follow-up was online, by phone, or in person.",
        "The digital instructions were difficult to use on my device.",
    ),
    "respect_involvement": (
        "I wanted more time to ask questions and help choose the plan.",
        "The team listened to my concern before explaining the next step.",
        "I did not feel included when the plan changed.",
    ),
    "other_or_unclear": (
        "I have one more question about the next step.",
        "Part of the visit was helpful and part was confusing.",
        "I am not sure which part of the process this comment belongs to.",
    ),
}
KEYWORDS = {
    "communication_clarity": ("instructions", "explanation", "written plan"),
    "medication_help": ("medicine", "medication"),
    "warning_signs": ("warning signs", "symptoms", "urgent"),
    "access_after_hours": ("after regular hours", "evening", "weekend"),
    "cost_barrier": ("cost", "lower-cost"),
    "digital_channel": ("video", "online", "digital", "device"),
    "respect_involvement": ("choose", "listened", "included"),
}
GROUPS = {
    "other_language_at_home": ("no", "yes", "missing or inapplicable"),
    "income_group": ("middle or high income", "lower income"),
    "insurance_coverage": ("any private insurance", "public insurance only", "uninsured"),
    "race_ethnicity": (
        "non-Hispanic White only", "Hispanic", "non-Hispanic Black only",
        "non-Hispanic Asian only", "non-Hispanic other or multiple races",
    ),
}
REFERENCES = {
    "other_language_at_home": "no",
    "income_group": "middle or high income",
    "insurance_coverage": "any private insurance",
    "race_ethnicity": "non-Hispanic White only",
}
MEASURES = {
    "delayed_for_cost": (
        "delayed_medical_care_for_cost", {"yes", "no"}, lambda row: row["delayed_medical_care_for_cost"] == "yes"
    ),
    "after_hours_difficult": (
        "after_hours_contact", {"very_difficult", "somewhat_difficult", "not_too_difficult", "not_at_all_difficult"},
        lambda row: row["after_hours_contact"] in {"very_difficult", "somewhat_difficult"},
    ),
    "involved_usually_always": (
        "involved_in_decisions", {"never", "sometimes", "usually", "always"},
        lambda row: row["involved_in_decisions"] in {"usually", "always"},
    ),
    "any_telehealth_event": (
        "any_telehealth_event", {"yes", "no"}, lambda row: row["any_telehealth_event"] == "yes"
    ),
}
GENERATED_FILES = (
    "data/synthetic/comment-opportunities.csv", "data/synthetic/synthetic-comments.csv",
    "data/synthetic/double-coding-sample.csv",
    "instructor/comment-truth.csv", "instructor/double-coded-comments.csv",
    "instructor/assisted-comment-labels.csv", "outputs/source-profile.csv",
    "outputs/comment-codebook.csv", "outputs/comment-flow.csv", "outputs/agreement-summary.csv",
    "outputs/assisted-classification-audit.csv", "outputs/theme-summary.csv",
    "outputs/comment-examples.csv", "outputs/group-support.csv", "outputs/group-estimates.csv",
    "outputs/group-contrasts.csv", "outputs/channel-exclusion-audit.csv",
    "outputs/invariant-checks.csv", "build-report.json",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_unit(*parts: object) -> float:
    token = "|".join([SEED, *(str(part) for part in parts)]).encode("utf-8")
    return int.from_bytes(hashlib.sha256(token).digest()[:8], "big") / float((1 << 64) - 1)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: tuple[str, ...] | list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: float, digits: int = 8) -> str:
    return f"{value:.{digits}f}"


def verify_upstream() -> int:
    total = 0
    for name, (expected_bytes, expected_hash) in UPSTREAM_RULES.items():
        path = UPSTREAM_ROOT / name
        if not path.is_file() or path.stat().st_size != expected_bytes or sha256(path) != expected_hash:
            raise ValueError(f"Accepted Module 04 handoff changed: {name}")
        total += path.stat().st_size
    release = json.loads((UPSTREAM_ROOT / "module04-release.json").read_text(encoding="utf-8"))
    if release["module"]["id"] != "oclc-app2-04" or release["module"]["version"] != "0.1.0":
        raise ValueError("Module 04 release identity changed")
    if release["package"]["manifest_sha256"] != "bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8":
        raise ValueError("Module 04 manifest identity changed")
    if release["progression"]["module05_permission"] != "permitted for patient-voice and equity analysis":
        raise ValueError("Module 04 does not permit Module 05")
    return total


def build_opportunities(people: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    respondents = sorted((row for row in people if row["response_status"] == "respondent"), key=lambda row: row["link_person_id"])
    if len(respondents) != 782:
        raise ValueError("Accepted synthetic respondent count changed")
    opportunities: list[dict[str, object]] = []
    for index, person in enumerate(respondents, 1):
        person_id = person["link_person_id"]
        channel_value = stable_unit(person_id, "channel")
        channel = "mail" if channel_value < 0.43 else "web" if channel_value < 0.77 else "phone"
        language = person["other_language_at_home"]
        if language == "yes":
            language_support = "offered" if stable_unit(person_id, "language-support") < 0.62 else "not_offered"
        else:
            language_support = "not_applicable"
        accessible = "offered" if stable_unit(person_id, "accessible-format") < 0.25 else "not_offered"
        score = stable_unit(person_id, "return")
        score += {"mail": 0.0, "web": 0.08, "phone": 0.03}[channel]
        if language == "yes":
            score += 0.10 if language_support == "offered" else -0.12
        if accessible == "offered":
            score += 0.03
        if person["income_group"] == "lower income":
            score -= 0.04
        opportunities.append({
            "opportunity_id": f"OPPORTUNITY-{index:04d}",
            "link_person_id": person_id,
            "data_class": "synthetic_comment_opportunity_linked_to_public_derived_meps",
            "assigned_channel": channel,
            "language_support_offer": language_support,
            "accessible_format_offer": accessible,
            "synthetic_selection_score": fmt(score),
            "comment_returned": "no",
            "comment_id": "",
        })
    selected = {row["link_person_id"] for row in sorted(opportunities, key=lambda row: (-float(row["synthetic_selection_score"]), str(row["link_person_id"])))[:420]}
    returned = [row for row in opportunities if row["link_person_id"] in selected]
    returned.sort(key=lambda row: str(row["link_person_id"]))
    comment_id_by_person = {row["link_person_id"]: f"COMMENT-{index:04d}" for index, row in enumerate(returned, 1)}
    for row in opportunities:
        if row["link_person_id"] in selected:
            row["comment_returned"] = "yes"
            row["comment_id"] = comment_id_by_person[row["link_person_id"]]

    theme_pool: list[tuple[str, int]] = []
    for theme in THEMES:
        theme_pool.extend((theme, index) for index in range(THEME_COUNTS[theme]))
    theme_pool.sort(key=lambda item: stable_unit("theme-slot", item[0], item[1]))
    ambiguous_people = {
        row["link_person_id"]
        for row in sorted(returned, key=lambda row: stable_unit(row["link_person_id"], "secondary"))[:84]
    }
    secondary_first_people = {
        person_id
        for person_id in sorted(ambiguous_people, key=lambda value: stable_unit(value, "secondary-first"))[:42]
    }
    comments: list[dict[str, object]] = []
    truth: list[dict[str, object]] = []
    for opportunity, (primary, _) in zip(returned, theme_pool):
        person_id = str(opportunity["link_person_id"])
        primary_index = int(stable_unit(person_id, "primary-template") * len(TEMPLATES[primary])) % len(TEMPLATES[primary])
        secondary = ""
        secondary_index = -1
        if person_id in ambiguous_people:
            alternatives = [theme for theme in THEMES if theme != primary]
            secondary = alternatives[int(stable_unit(person_id, "secondary-theme") * len(alternatives)) % len(alternatives)]
            secondary_index = int(stable_unit(person_id, "secondary-template") * len(TEMPLATES[secondary])) % len(TEMPLATES[secondary])
        sentences = [TEMPLATES[primary][primary_index]]
        if secondary:
            secondary_sentence = TEMPLATES[secondary][secondary_index]
            sentences = [secondary_sentence, *sentences] if person_id in secondary_first_people else [*sentences, secondary_sentence]
        comments.append({
            "comment_id": opportunity["comment_id"],
            "link_person_id": person_id,
            "data_class": "fully_synthetic_comment_linked_to_public_derived_meps",
            "assigned_channel": opportunity["assigned_channel"],
            "language_support_offer": opportunity["language_support_offer"],
            "accessible_format_offer": opportunity["accessible_format_offer"],
            "comment_language": "synthetic English",
            "comment_text": " ".join(sentences),
        })
        truth.append({
            "comment_id": opportunity["comment_id"],
            "primary_theme": primary,
            "secondary_theme": secondary,
            "ambiguous": "yes" if secondary else "no",
            "secondary_text_first": "yes" if person_id in secondary_first_people else "no",
            "primary_template_id": f"{primary}-T{primary_index + 1}",
            "secondary_template_id": f"{secondary}-T{secondary_index + 1}" if secondary else "",
            "generation_rule": "fixed synthetic theme allocation and phrase templates; no observed patient text",
        })
    return opportunities, comments, truth


def alternate_theme(primary: str, offset: int) -> str:
    return THEMES[(THEMES.index(primary) + offset) % len(THEMES)]


def build_double_coding(truth: list[dict[str, object]]) -> list[dict[str, object]]:
    by_theme: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in truth:
        by_theme[str(row["primary_theme"])].append(row)
    coded: list[dict[str, object]] = []
    for theme in THEMES:
        sample = sorted(by_theme[theme], key=lambda row: stable_unit(row["comment_id"], "double-code"))[:15]
        if len(sample) != 15:
            raise ValueError(f"Theme lacks 15 comments for double coding: {theme}")
        for position, row in enumerate(sample):
            coder_a = theme if position not in {0, 10} else alternate_theme(theme, 1)
            if position == 0:
                coder_b = alternate_theme(theme, 1)
            elif position in {7, 14}:
                coder_b = alternate_theme(theme, 2)
            else:
                coder_b = theme
            coded.append({
                "comment_id": row["comment_id"],
                "sample_theme_stratum": theme,
                "coder_a_theme": coder_a,
                "coder_b_theme": coder_b,
                "agreement": "yes" if coder_a == coder_b else "no",
                "adjudicated_theme": theme,
                "adjudication_reason": "both training coders agreed" if coder_a == coder_b == theme else "reference adjudication restored the fixed synthetic truth",
                "record_class": "simulated training coder record; not completed human alpha review",
            })
    return sorted(coded, key=lambda row: str(row["comment_id"]))


def kappa(labels_a: list[str], labels_b: list[str], categories: tuple[str, ...]) -> float:
    if len(labels_a) != len(labels_b) or not labels_a:
        raise ValueError("Kappa requires two nonempty equal-length label lists")
    observed = sum(a == b for a, b in zip(labels_a, labels_b)) / len(labels_a)
    count_a, count_b = Counter(labels_a), Counter(labels_b)
    expected = sum(count_a[category] * count_b[category] for category in categories) / (len(labels_a) ** 2)
    return (observed - expected) / (1.0 - expected) if expected < 1.0 else 1.0


def agreement_summary(coded: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    labels_a = [str(row["coder_a_theme"]) for row in coded]
    labels_b = [str(row["coder_b_theme"]) for row in coded]
    agreements = sum(a == b for a, b in zip(labels_a, labels_b))
    rows.append({
        "scope": "overall_eight_theme", "records": len(coded), "agreements": agreements,
        "percent_agreement": fmt(100 * agreements / len(coded)), "cohens_kappa": fmt(kappa(labels_a, labels_b, THEMES)),
        "interpretation": "agreement describes the simulated training exercise; it does not validate the codebook",
    })
    for theme in THEMES:
        binary_a = ["theme" if value == theme else "other" for value in labels_a]
        binary_b = ["theme" if value == theme else "other" for value in labels_b]
        same = sum(a == b for a, b in zip(binary_a, binary_b))
        rows.append({
            "scope": theme, "records": len(coded), "agreements": same,
            "percent_agreement": fmt(100 * same / len(coded)),
            "cohens_kappa": fmt(kappa(binary_a, binary_b, ("theme", "other"))),
            "interpretation": "binary theme-versus-other diagnostic for codebook review",
        })
    return rows


def classify(text: str) -> tuple[str, str]:
    lowered = text.lower()
    matches: list[tuple[int, str, str]] = []
    for theme, phrases in KEYWORDS.items():
        for phrase in phrases:
            position = lowered.find(phrase)
            if position >= 0:
                matches.append((position, theme, phrase))
    if not matches:
        return "other_or_unclear", "no match"
    position, theme, phrase = min(matches, key=lambda item: (item[0], THEMES.index(item[1]), item[2]))
    return theme, f"first matched phrase at character {position}: {phrase}"


def build_assisted(comments: list[dict[str, object]], truth: list[dict[str, object]], coded: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    truth_map = {str(row["comment_id"]): row for row in truth}
    benchmark_ids = {str(row["comment_id"]) for row in coded}
    labels: list[dict[str, object]] = []
    for comment in comments:
        comment_id = str(comment["comment_id"])
        predicted, matched = classify(str(comment["comment_text"]))
        truth_row = truth_map[comment_id]
        labels.append({
            "comment_id": comment_id,
            "benchmark_sample": "yes" if comment_id in benchmark_ids else "no",
            "adjudicated_or_instructor_truth": truth_row["primary_theme"],
            "assisted_theme": predicted,
            "matched_rule": matched,
            "correct": "yes" if predicted == truth_row["primary_theme"] else "no",
            "human_review_required": "yes",
        })
    benchmark = [row for row in labels if row["benchmark_sample"] == "yes"]
    audit: list[dict[str, object]] = []
    recalls: list[float] = []
    for theme in THEMES:
        truth_n = sum(row["adjudicated_or_instructor_truth"] == theme for row in benchmark)
        predicted_n = sum(row["assisted_theme"] == theme for row in benchmark)
        true_positive = sum(row["adjudicated_or_instructor_truth"] == theme and row["assisted_theme"] == theme for row in benchmark)
        recall = true_positive / truth_n if truth_n else 0.0
        precision = true_positive / predicted_n if predicted_n else 0.0
        recalls.append(recall)
        audit.append({
            "scope": theme, "benchmark_n": len(benchmark), "truth_n": truth_n,
            "predicted_n": predicted_n, "true_positive": true_positive,
            "recall": fmt(recall), "precision": fmt(precision), "accuracy": "",
            "human_review_rule": "every suggested label requires human acceptance change or rejection",
        })
    correct = sum(row["correct"] == "yes" for row in benchmark)
    audit.insert(0, {
        "scope": "overall", "benchmark_n": len(benchmark), "truth_n": len(benchmark),
        "predicted_n": len(benchmark), "true_positive": correct, "recall": fmt(sum(recalls) / len(recalls)),
        "precision": "", "accuracy": fmt(correct / len(benchmark)),
        "human_review_rule": "macro recall and accuracy are diagnostics; human review is required and autonomous coding is prohibited",
    })
    return labels, audit


def survey_estimate(people: list[dict[str, str]], group_field: str, group_value: str, measure: str) -> dict[str, object]:
    source_field, valid_values, positive_test = MEASURES[measure]
    design = [row for row in people if float(row["base_person_weight"]) > 0]
    domain = [row for row in design if row[group_field] == group_value and row[source_field] in valid_values]
    positives = sum(bool(positive_test(row)) for row in domain)
    negatives = len(domain) - positives
    psus = len({(row["variance_stratum"], row["variance_psu"]) for row in domain})
    supported = len(domain) >= 50 and positives >= 10 and negatives >= 10 and psus >= 2
    reason = "reportable_teaching_support" if supported else "; ".join(
        reason for condition, reason in (
            (len(domain) < 50, "valid n below 50"),
            (positives < 10, "positive n below 10"),
            (negatives < 10, "negative n below 10"),
            (psus < 2, "fewer than two contributing PSUs"),
        ) if condition
    )
    result: dict[str, object] = {
        "dimension": group_field, "group": group_value, "reference_group": REFERENCES[group_field],
        "measure": measure, "valid_n": len(domain), "positive_n": positives, "negative_n": negatives,
        "contributing_psus": psus, "weighted_denominator": "", "weighted_percent": "",
        "survey_se_pp": "", "ci95_low_percent": "", "ci95_high_percent": "",
        "support_status": "supported" if supported else "suppressed", "support_reason": reason,
    }
    if not supported:
        return result
    total_weight = sum(float(row["base_person_weight"]) for row in domain)
    estimate = sum(float(row["base_person_weight"]) * int(bool(positive_test(row))) for row in domain) / total_weight
    cluster: dict[tuple[str, str], float] = defaultdict(float)
    strata: dict[str, set[str]] = defaultdict(set)
    for row in design:
        key = (row["variance_stratum"], row["variance_psu"])
        strata[key[0]].add(key[1])
        contribution = 0.0
        if row[group_field] == group_value and row[source_field] in valid_values:
            contribution = float(row["base_person_weight"]) * (int(bool(positive_test(row))) - estimate)
        cluster[key] += contribution
    variance_total = 0.0
    for stratum, stratum_psus in strata.items():
        values = [cluster[(stratum, psu)] for psu in sorted(stratum_psus)]
        if len(values) > 1:
            mean_value = sum(values) / len(values)
            variance_total += len(values) / (len(values) - 1) * sum((value - mean_value) ** 2 for value in values)
    se = math.sqrt(max(variance_total, 0.0)) / total_weight
    result.update({
        "weighted_denominator": fmt(total_weight, 6), "weighted_percent": fmt(100 * estimate),
        "survey_se_pp": fmt(100 * se), "ci95_low_percent": fmt(max(0.0, 100 * (estimate - 1.96 * se))),
        "ci95_high_percent": fmt(min(100.0, 100 * (estimate + 1.96 * se))),
    })
    return result


def survey_contrast(people: list[dict[str, str]], estimate_rows: dict[tuple[str, str, str], dict[str, object]], dimension: str, group: str, measure: str) -> dict[str, object]:
    reference = REFERENCES[dimension]
    current = estimate_rows[(dimension, group, measure)]
    baseline = estimate_rows[(dimension, reference, measure)]
    result: dict[str, object] = {
        "dimension": dimension, "group": group, "reference_group": reference, "measure": measure,
        "group_n": current["valid_n"], "reference_n": baseline["valid_n"], "difference_pp": "",
        "survey_se_pp": "", "ci95_low_pp": "", "ci95_high_pp": "", "support_status": "suppressed",
        "support_reason": "group or reference estimate is unsupported",
    }
    if current["support_status"] != "supported" or baseline["support_status"] != "supported":
        return result
    source_field, valid_values, positive_test = MEASURES[measure]
    design = [row for row in people if float(row["base_person_weight"]) > 0]
    group_rows = [row for row in design if row[dimension] == group and row[source_field] in valid_values]
    reference_rows = [row for row in design if row[dimension] == reference and row[source_field] in valid_values]
    group_weight = sum(float(row["base_person_weight"]) for row in group_rows)
    reference_weight = sum(float(row["base_person_weight"]) for row in reference_rows)
    group_mean = float(current["weighted_percent"]) / 100.0
    reference_mean = float(baseline["weighted_percent"]) / 100.0
    cluster: dict[tuple[str, str], float] = defaultdict(float)
    strata: dict[str, set[str]] = defaultdict(set)
    for row in design:
        key = (row["variance_stratum"], row["variance_psu"])
        strata[key[0]].add(key[1])
        contribution = 0.0
        if row[dimension] == group and row[source_field] in valid_values:
            contribution += float(row["base_person_weight"]) * (int(bool(positive_test(row))) - group_mean) / group_weight
        if row[dimension] == reference and row[source_field] in valid_values:
            contribution -= float(row["base_person_weight"]) * (int(bool(positive_test(row))) - reference_mean) / reference_weight
        cluster[key] += contribution
    variance = 0.0
    for stratum, stratum_psus in strata.items():
        values = [cluster[(stratum, psu)] for psu in sorted(stratum_psus)]
        if len(values) > 1:
            mean_value = sum(values) / len(values)
            variance += len(values) / (len(values) - 1) * sum((value - mean_value) ** 2 for value in values)
    difference = 100 * (group_mean - reference_mean)
    se = 100 * math.sqrt(max(variance, 0.0))
    result.update({
        "difference_pp": fmt(difference), "survey_se_pp": fmt(se),
        "ci95_low_pp": fmt(difference - 1.96 * se), "ci95_high_pp": fmt(difference + 1.96 * se),
        "support_status": "supported", "support_reason": "descriptive exploratory contrast; not proof of inequity or cause",
    })
    return result


def build(output_root: Path = MODULE_ROOT) -> dict[str, object]:
    output_root = output_root.resolve()
    if output_root != MODULE_ROOT and output_root.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)
    upstream_bytes = verify_upstream()
    people = read_csv(UPSTREAM_ROOT / "module04-linked-persons.csv")
    events = read_csv(UPSTREAM_ROOT / "module04-linked-events.csv")
    if len(people) != 1255 or len(events) != 28455:
        raise ValueError("Accepted Module 04 target counts changed")
    if any("DUPERSID" in row or "EVNTIDX" in row for row in [*people[:1], *events[:1]]):
        raise ValueError("Direct MEPS identifiers entered the Module 05 handoff")
    telehealth_people = {row["link_person_id"] for row in events if row["telehealth_status"] == "yes"}
    for person in people:
        person["any_telehealth_event"] = "yes" if person["link_person_id"] in telehealth_people else "no"

    opportunities, comments, truth = build_opportunities(people)
    coded = build_double_coding(truth)
    agreement = agreement_summary(coded)
    assisted_labels, assisted_audit = build_assisted(comments, truth, coded)

    write_csv(output_root / "data/synthetic/comment-opportunities.csv", tuple(opportunities[0]), opportunities)
    write_csv(output_root / "data/synthetic/synthetic-comments.csv", tuple(comments[0]), comments)
    comment_by_id = {str(row["comment_id"]): row for row in comments}
    coding_sample = [
        {
            "comment_id": row["comment_id"],
            "assigned_channel": comment_by_id[str(row["comment_id"])]["assigned_channel"],
            "synthetic_comment_text": comment_by_id[str(row["comment_id"])]["comment_text"],
            "coder_a_theme": "",
            "coder_b_theme": "",
            "adjudicated_theme": "",
        }
        for row in coded
    ]
    write_csv(output_root / "data/synthetic/double-coding-sample.csv", tuple(coding_sample[0]), coding_sample)
    write_csv(output_root / "instructor/comment-truth.csv", tuple(truth[0]), truth)
    write_csv(output_root / "instructor/double-coded-comments.csv", tuple(coded[0]), coded)
    write_csv(output_root / "instructor/assisted-comment-labels.csv", tuple(assisted_labels[0]), assisted_labels)

    profile = [
        {"metric": "upstream_files", "value": 5, "unit": "files", "evidence": "fingerprinted Module 04 handoff"},
        {"metric": "upstream_bytes", "value": upstream_bytes, "unit": "bytes", "evidence": "fingerprinted Module 04 handoff"},
        {"metric": "official_meps_source_files_referenced", "value": 25, "unit": "files", "evidence": "accepted Module 04 source inventory"},
        {"metric": "accepted_people", "value": len(people), "unit": "people", "evidence": "public-derived MEPS teaching table"},
        {"metric": "accepted_events", "value": len(events), "unit": "events", "evidence": "public-derived MEPS teaching table"},
        {"metric": "synthetic_comment_opportunities", "value": len(opportunities), "unit": "opportunities", "evidence": "deterministic procedural layer"},
        {"metric": "synthetic_comments_received", "value": len(comments), "unit": "comments", "evidence": "fully synthetic English teaching text"},
        {"metric": "double_coded_comments", "value": len(coded), "unit": "comments", "evidence": "simulated training coder records"},
        {"metric": "themes", "value": len(THEMES), "unit": "themes", "evidence": "fixed codebook"},
        {"metric": "ambiguous_comments", "value": sum(row["ambiguous"] == "yes" for row in truth), "unit": "comments", "evidence": "fixed synthetic truth"},
        {"metric": "public_group_dimensions", "value": len(GROUPS), "unit": "dimensions", "evidence": "prespecified contract"},
        {"metric": "public_group_measures", "value": len(MEASURES), "unit": "measures", "evidence": "prespecified contract"},
        {"metric": "portal_preference_denominator", "value": 0, "unit": "people", "evidence": "accepted unavailable denominator"},
        {"metric": "external_python_dependencies", "value": 0, "unit": "packages", "evidence": "Python standard library only"},
    ]
    write_csv(output_root / "outputs/source-profile.csv", ("metric", "value", "unit", "evidence"), profile)
    codebook = [
        {"theme": theme, "label": THEME_LABELS[theme], "include": CODEBOOK[theme][0], "exclude": CODEBOOK[theme][1], "anchor_language": CODEBOOK[theme][2], "coding_rule": "one primary theme; optional secondary theme; adjudicate unclear records"}
        for theme in THEMES
    ]
    write_csv(output_root / "outputs/comment-codebook.csv", tuple(codebook[0]), codebook)

    people_by_id = {row["link_person_id"]: row for row in people}
    flow: list[dict[str, object]] = []
    flow_specs = [
        ("overall", "all opportunities", lambda row: True),
        *(("assigned_channel", value, lambda row, value=value: row["assigned_channel"] == value) for value in ("mail", "web", "phone")),
        *(("language_support_offer", value, lambda row, value=value: row["language_support_offer"] == value) for value in ("offered", "not_offered", "not_applicable")),
        *(("accessible_format_offer", value, lambda row, value=value: row["accessible_format_offer"] == value) for value in ("offered", "not_offered")),
    ]
    for dimension, value, test in flow_specs:
        subset = [row for row in opportunities if test(row)]
        returns = sum(row["comment_returned"] == "yes" for row in subset)
        flow.append({
            "dimension": dimension, "value": value, "opportunities": len(subset), "comments_received": returns,
            "return_percent": fmt(100 * returns / len(subset)) if subset else "",
            "data_class": "synthetic procedural counts", "claim_limit": "not a real response rate access estimate or channel preference",
        })
    write_csv(output_root / "outputs/comment-flow.csv", tuple(flow[0]), flow)
    write_csv(output_root / "outputs/agreement-summary.csv", tuple(agreement[0]), agreement)
    write_csv(output_root / "outputs/assisted-classification-audit.csv", tuple(assisted_audit[0]), assisted_audit)

    theme_counts = Counter(str(row["primary_theme"]) for row in truth)
    theme_summary = [
        {"theme": theme, "received_comments": theme_counts[theme], "share_of_received_synthetic_comments": fmt(100 * theme_counts[theme] / len(truth)), "denominator": len(truth), "claim_limit": "share of synthetic received comments only; not prevalence sentiment or saturation"}
        for theme in THEMES
    ]
    write_csv(output_root / "outputs/theme-summary.csv", tuple(theme_summary[0]), theme_summary)
    comment_map = comment_by_id
    examples: list[dict[str, object]] = []
    for theme in THEMES:
        selected = sorted((row for row in truth if row["primary_theme"] == theme), key=lambda row: stable_unit(row["comment_id"], "example"))[:2]
        for row in selected:
            comment = comment_map[str(row["comment_id"])]
            examples.append({
                "theme": theme, "comment_id": row["comment_id"], "assigned_channel": comment["assigned_channel"],
                "secondary_theme": row["secondary_theme"], "synthetic_example_text": comment["comment_text"],
                "example_status": "generated teaching text; never present as patient testimony",
            })
    write_csv(output_root / "outputs/comment-examples.csv", tuple(examples[0]), examples)

    group_support: list[dict[str, object]] = []
    estimate_list: list[dict[str, object]] = []
    for dimension, groups in GROUPS.items():
        for group in groups:
            group_rows = [row for row in people if row[dimension] == group]
            psus = len({(row["variance_stratum"], row["variance_psu"]) for row in group_rows})
            group_support.append({
                "dimension": dimension, "group": group, "reference_group": REFERENCES[dimension],
                "total_people": len(group_rows), "contributing_psus": psus,
                "group_status": "eligible_for_measure_specific_review" if len(group_rows) >= 50 and psus >= 2 else "small_group_retained",
                "claim_limit": "source category is not a biological explanation risk score or proof of inequity",
            })
            for measure in MEASURES:
                estimate_list.append(survey_estimate(people, dimension, group, measure))
    write_csv(output_root / "outputs/group-support.csv", tuple(group_support[0]), group_support)
    write_csv(output_root / "outputs/group-estimates.csv", tuple(estimate_list[0]), estimate_list)
    estimate_map = {(str(row["dimension"]), str(row["group"]), str(row["measure"])): row for row in estimate_list}
    contrasts: list[dict[str, object]] = []
    for dimension, groups in GROUPS.items():
        for group in groups:
            if group == REFERENCES[dimension]:
                continue
            for measure in MEASURES:
                contrasts.append(survey_contrast(people, estimate_map, dimension, group, measure))
    write_csv(output_root / "outputs/group-contrasts.csv", tuple(contrasts[0]), contrasts)

    exclusion: list[dict[str, object]] = []
    for dimension, groups in GROUPS.items():
        for group in groups:
            subset = [row for row in opportunities if people_by_id[str(row["link_person_id"])][dimension] == group]
            received = sum(row["comment_returned"] == "yes" for row in subset)
            exclusion.append({
                "dimension": dimension, "group": group, "opportunities": len(subset), "comments_received": received,
                "return_percent": fmt(100 * received / len(subset)) if subset else "",
                "data_class": "synthetic procedural opportunity linked to public-derived group field",
                "claim_limit": "designed coverage exercise; not observed access trust preference or inequity",
            })
    write_csv(output_root / "outputs/channel-exclusion-audit.csv", tuple(exclusion[0]), exclusion)

    supported_estimates = sum(row["support_status"] == "supported" for row in estimate_list)
    supported_contrasts = sum(row["support_status"] == "supported" for row in contrasts)
    overall_agreement = agreement[0]
    overall_assisted = assisted_audit[0]
    invariants = [
        ("I01", "upstream file count", len(UPSTREAM_RULES), 5),
        ("I02", "upstream bytes", upstream_bytes, 5297691),
        ("I03", "accepted person rows", len(people), 1255),
        ("I04", "accepted event rows", len(events), 28455),
        ("I05", "synthetic respondent opportunities", len(opportunities), 782),
        ("I06", "synthetic received comments", len(comments), 420),
        ("I07", "unique comment IDs", len({row["comment_id"] for row in comments}), 420),
        ("I08", "real patient text rows", 0, 0),
        ("I09", "codebook themes", len(codebook), 8),
        ("I10", "theme allocation total", sum(theme_counts.values()), 420),
        ("I11", "ambiguous comment rows", sum(row["ambiguous"] == "yes" for row in truth), 84),
        ("I12", "secondary-text-first rows", sum(row["secondary_text_first"] == "yes" for row in truth), 42),
        ("I13", "double-coded rows", len(coded), 120),
        ("I14", "double-coded rows per theme", min(Counter(row["sample_theme_stratum"] for row in coded).values()), 15),
        ("I15", "coder agreements", int(overall_agreement["agreements"]), 96),
        ("I16", "adjudicated rows", sum(bool(row["adjudicated_theme"]) for row in coded), 120),
        ("I17", "assisted benchmark rows", int(overall_assisted["benchmark_n"]), 120),
        ("I18", "assisted human-review-required rows", sum(row["human_review_required"] == "yes" for row in assisted_labels), 420),
        ("I19", "comment examples", len(examples), 16),
        ("I20", "group dimensions", len(GROUPS), 4),
        ("I21", "group measures", len(MEASURES), 4),
        ("I22", "group support rows", len(group_support), 13),
        ("I23", "group estimate rows", len(estimate_list), 52),
        ("I24", "group contrast rows", len(contrasts), 36),
        ("I25", "portal preference denominator", 0, 0),
        ("I26", "direct source identifier fields released", 0, 0),
        ("I27", "external Python dependencies", 0, 0),
        ("I28", "theme counts match fixed allocation", theme_counts == Counter(THEME_COUNTS), True),
    ]
    invariant_rows = [
        {"check_id": check_id, "invariant": label, "actual": actual, "expected": expected, "status": "pass" if actual == expected else "fail"}
        for check_id, label, actual, expected in invariants
    ]
    write_csv(output_root / "outputs/invariant-checks.csv", tuple(invariant_rows[0]), invariant_rows)
    if any(row["status"] != "pass" for row in invariant_rows):
        raise ValueError("One or more Module 05 invariants failed")

    evidence_paths = [output_root / relative for relative in GENERATED_FILES if relative != "build-report.json"]
    report = {
        "schema_version": "1.0.0", "status": "pass", "seed": SEED,
        "upstream": {"files": 5, "bytes": upstream_bytes, "people": len(people), "events": len(events)},
        "synthetic_comments": {
            "opportunities": len(opportunities), "received": len(comments), "themes": len(THEMES),
            "ambiguous": 84, "double_coded": len(coded), "coder_agreements": int(overall_agreement["agreements"]),
            "percent_agreement": overall_agreement["percent_agreement"], "cohens_kappa": overall_agreement["cohens_kappa"],
            "assisted_benchmark_accuracy": overall_assisted["accuracy"], "real_patient_text_rows": 0,
        },
        "group_review": {
            "dimensions": len(GROUPS), "measures": len(MEASURES), "support_rows": len(group_support),
            "estimate_rows": len(estimate_list), "supported_estimates": supported_estimates,
            "contrast_rows": len(contrasts), "supported_contrasts": supported_contrasts,
        },
        "generated_evidence": {
            "files_excluding_report": len(evidence_paths),
            "bytes_excluding_report": sum(path.stat().st_size for path in evidence_paths),
            "invariants_passed": len(invariant_rows), "invariants_failed": 0,
        },
    }
    (output_root / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    generated_sha256 = {relative: sha256(output_root / relative) for relative in GENERATED_FILES}
    return {"report": report, "generated_sha256": generated_sha256}


def verify_committed() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module05-verify-") as temp_dir:
        candidate = Path(temp_dir) / "build"
        rebuilt = build(candidate)
        for relative, digest in rebuilt["generated_sha256"].items():
            committed = MODULE_ROOT / relative
            if not committed.is_file() or sha256(committed) != digest:
                raise ValueError(f"Committed evidence differs from clean build: {relative}")
    print("APP-2 Module 05 committed evidence matches a clean rebuild.")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module05-build-") as temp_dir:
        root = Path(temp_dir)
        first, second = root / "first", root / "second"
        one, two = build(first), build(second)
        assert one == two
        assert one["report"]["synthetic_comments"]["received"] == 420
        assert one["report"]["synthetic_comments"]["coder_agreements"] == 96
        assert one["report"]["group_review"]["estimate_rows"] == 52
        try:
            build(first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder overwrote an existing target")
    print("APP-2 Module 05 evidence builder self-check passed: 782 opportunities, 420 synthetic comments, 120 double-coded records, and 28 invariants.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=MODULE_ROOT)
    parser.add_argument("--verify-committed", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.verify_committed:
            verify_committed()
        elif args.self_check:
            self_check()
        else:
            result = build(args.output_root)
            print(json.dumps(result["report"], indent=2))
    except (OSError, ValueError, KeyError, json.JSONDecodeError, csv.Error) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()

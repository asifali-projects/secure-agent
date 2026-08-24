from dataclasses import dataclass


@dataclass
class RiskAssessment:
    score: int
    level: str


def assess(
    *,
    prompt_injection: bool = False,
    jailbreak: bool = False,
    privileged_request: bool = False,
    destructive_action: bool = False,
) -> RiskAssessment:

    score = 0

    if prompt_injection:
        score += 70

    if jailbreak:
        score += 80

    if privileged_request:
        score += 60

    if destructive_action:
        score += 90

    score = min(score, 100)

    if score >= 80:
        level = "critical"

    elif score >= 60:
        level = "high"

    elif score >= 30:
        level = "medium"

    else:
        level = "low"

    return RiskAssessment(
        score=score,
        level=level,
    )
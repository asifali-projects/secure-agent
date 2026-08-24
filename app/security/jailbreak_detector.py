JAILBREAK_PATTERNS = [
    "dan mode",
    "do anything now",
    "developer mode",
    "god mode",
    "no restrictions",
    "without restrictions",
    "ignore safety",
    "disable safety",
    "disable guardrails",
    "bypass policy",
]


def detect_jailbreak(text: str) -> bool:

    normalized = text.lower()

    return any(
        pattern in normalized
        for pattern in JAILBREAK_PATTERNS
    )
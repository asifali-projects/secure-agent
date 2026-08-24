import re


INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"disregard\s+(all\s+)?previous",
    r"forget\s+(all\s+)?previous",
    r"override\s+(the\s+)?system",
    r"override\s+(the\s+)?developer",
    r"reveal\s+(the\s+)?system\s+prompt",
    r"show\s+(me\s+)?the\s+system\s+prompt",
    r"print\s+(the\s+)?system\s+message",
    r"developer\s+message",
    r"hidden\s+instructions",
    r"bypass\s+(security|guardrail|policy)",
]


def detect_prompt_injection(text: str) -> bool:
    return any(
        re.search(
            pattern,
            text,
            flags=re.IGNORECASE,
        )
        for pattern in INJECTION_PATTERNS
    )
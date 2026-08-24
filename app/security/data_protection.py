import re


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@"
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def redact_email(text: str) -> str:
    return EMAIL_PATTERN.sub(
        "[REDACTED_EMAIL]",
        text,
    )


def protect(text: str) -> str:
    return redact_email(text)
import re

from app.core.config import settings
from app.core.exceptions import OutputSecurityError


SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9_-]{20,}",
    r"(?i)api[_-]?key\s*[:=]\s*\S+",
    r"(?i)secret\s*[:=]\s*\S+",
    r"(?i)password\s*[:=]\s*\S+",
    r"(?i)authorization\s*:\s*bearer\s+\S+",
]


class OutputGuard:

    def validate(self, text: str) -> str:

        if len(text) > settings.max_output_chars:
            raise OutputSecurityError(
                "Model output exceeds maximum size"
            )

        for pattern in SECRET_PATTERNS:

            if re.search(pattern, text):
                raise OutputSecurityError(
                    "Sensitive information detected in model output"
                )

        return text
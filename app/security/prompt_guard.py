from app.core.config import settings
from app.core.exceptions import InputSecurityError

from app.security.injection_detector import (
    detect_prompt_injection,
)

from app.security.jailbreak_detector import (
    detect_jailbreak,
)


class PromptGuard:

    def validate(self, text: str) -> None:

        if not text:
            raise InputSecurityError(
                "Prompt cannot be empty"
            )

        if len(text) > settings.max_input_chars:
            raise InputSecurityError(
                "Prompt exceeds maximum allowed size"
            )

        if detect_prompt_injection(text):
            raise InputSecurityError(
                "Prompt injection detected"
            )

        if detect_jailbreak(text):
            raise InputSecurityError(
                "Jailbreak attempt detected"
            )
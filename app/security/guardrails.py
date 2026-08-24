from app.security.prompt_guard import PromptGuard
from app.security.output_guard import OutputGuard


class GuardrailPipeline:

    def __init__(self):
        self.prompt_guard = PromptGuard()
        self.output_guard = OutputGuard()

    def validate_input(self, text: str) -> None:
        self.prompt_guard.validate(text)

    def validate_output(self, text: str) -> str:
        return self.output_guard.validate(text)

    def sanitize_retrieved_content(
        self,
        text: str,
    ) -> str:

        # Retrieved documents are DATA, never instructions.
        return (
            text
            .replace("\x00", "")
            .strip()
        )
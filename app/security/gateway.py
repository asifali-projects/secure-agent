from app.auth.models import User
from app.security.prompt_guard import PromptGuard
from app.security.output_guard import OutputGuard


class SecurityGateway:

    def __init__(self) -> None:

        self.prompt_guard = PromptGuard()
        self.output_guard = OutputGuard()

    def validate_input(
        self,
        user: User,
        prompt: str,
    ) -> None:

        self.prompt_guard.validate(prompt)

    def validate_output(
        self,
        user: User,
        output: str,
    ) -> str:

        return self.output_guard.validate(output)
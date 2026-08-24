from nemoguardrails import RailsConfig, LLMRails

from app.core.config import settings


class NemoGuard:

    def __init__(self) -> None:
        config = RailsConfig.from_path(
            settings.nemo_config_path
        )

        self.rails = LLMRails(config)

    async def generate(
        self,
        messages: list[dict[str, str]],
    ) -> str:

        response = await self.rails.generate_async(
            messages=messages
        )

        return response["content"]
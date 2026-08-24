from app.agent.state import AgentState
from app.core.config import settings
from app.core.exceptions import SecurityViolation


class AgentExecutor:

    def validate_step(
        self,
        state: AgentState,
    ) -> None:

        if state.steps >= settings.max_agent_steps:
            raise SecurityViolation(
                "Maximum agent steps exceeded"
            )

        if state.tool_calls >= settings.max_tool_calls:
            raise SecurityViolation(
                "Maximum tool calls exceeded"
            )

        state.steps += 1
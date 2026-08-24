from dataclasses import dataclass, field


@dataclass
class AgentState:
    user_id: str
    tenant_id: str
    conversation_id: str
    user_input: str

    steps: int = 0
    tool_calls: int = 0

    retrieved_documents: list[dict] = field(
        default_factory=list
    )

    tool_results: list[dict] = field(
        default_factory=list
    )

    final_answer: str | None = None

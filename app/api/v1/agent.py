from uuid import uuid4

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.agent.agent import SecureAgent
from app.auth.dependencies import get_current_user
from app.auth.models import User


router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)

agent = SecureAgent()


class AgentRequest(BaseModel):

    prompt: str = Field(
        min_length=1,
        max_length=12000,
    )

    conversation_id: str | None = None


class AgentResponse(BaseModel):

    conversation_id: str
    answer: str


@router.post(
    "/chat",
    response_model=AgentResponse,
)
async def chat(
    request: AgentRequest,
    user: User = Depends(get_current_user),
):

    conversation_id = (
        request.conversation_id
        or str(uuid4())
    )

    answer = await agent.run(
        user=user,
        prompt=request.prompt,
        conversation_id=conversation_id,
    )

    return AgentResponse(
        conversation_id=conversation_id,
        answer=answer,
    )
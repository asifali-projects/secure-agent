from app.auth.models import User
from app.tools.permissions import authorize_tool
from app.tools.registry import get_tool


class ToolGateway:

    async def execute(
        self,
        user: User,
        tool_name: str,
        arguments: dict,
    ):

        authorize_tool(
            user,
            tool_name,
        )

        tool = get_tool(tool_name)

        if not tool:
            raise PermissionError(
                "Tool does not exist"
            )

        return await tool(**arguments)
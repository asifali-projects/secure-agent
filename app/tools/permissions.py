from app.auth.models import User
from app.core.exceptions import ToolAuthorizationError


TOOL_ROLES = {
    "search_documents": {
        "analyst",
        "admin",
    },
    "get_time": {
        "analyst",
        "admin",
    },
    "delete_document": {
        "admin",
    },
}


def authorize_tool(
    user: User,
    tool_name: str,
) -> None:

    allowed_roles = TOOL_ROLES.get(
        tool_name
    )

    if not allowed_roles:
        raise ToolAuthorizationError(
            "Unknown tool"
        )

    if not any(
        role in allowed_roles
        for role in user.roles
    ):
        raise ToolAuthorizationError(
            f"Tool '{tool_name}' is not authorized"
        )
from app.auth.models import User
from app.core.exceptions import AuthorizationError


def require_roles(
    user: User,
    *required_roles: str,
) -> None:

    if not any(
        role in user.roles
        for role in required_roles
    ):
        raise AuthorizationError(
            "Required role is missing"
        )


def has_role(
    user: User,
    role: str,
) -> bool:
    return role in user.roles
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.jwt import decode_access_token
from app.auth.models import User
from app.core.exceptions import AuthenticationError


security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> User:

    if not credentials:
        raise AuthenticationError(
            "Authentication required"
        )

    try:
        payload = decode_access_token(
            credentials.credentials
        )

        return User(
            id=payload["sub"],
            email=payload["email"],
            tenant_id=payload["tenant_id"],
            roles=payload.get("roles", []),
        )

    except Exception as exc:
        raise AuthenticationError(
            "Invalid or expired access token"
        ) from exc
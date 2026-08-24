from datetime import datetime, timedelta, timezone

import jwt

from app.auth.models import User
from app.core.config import settings


def create_access_token(user: User) -> str:
    now = datetime.now(timezone.utc)

    payload = {
        "sub": user.id,
        "email": user.email,
        "tenant_id": user.tenant_id,
        "roles": user.roles,
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
        "iat": now,
        "exp": now + timedelta(
            minutes=settings.jwt_expire_minutes
        ),
    }

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.jwt_secret,
        algorithms=[settings.jwt_algorithm],
        issuer=settings.jwt_issuer,
        audience=settings.jwt_audience,
    )
from fastapi import APIRouter, HTTPException

from app.auth.jwt import create_access_token
from app.auth.models import (
    LoginRequest,
    TokenResponse,
)
from app.auth.service import authenticate
from app.core.config import settings


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    payload: LoginRequest,
):

    user = authenticate(
        payload.email,
        payload.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_access_token(user)

    return TokenResponse(
        access_token=token,
        expires_in=settings.jwt_expire_minutes * 60,
    )
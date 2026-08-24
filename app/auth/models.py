from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: str
    email: EmailStr
    tenant_id: str
    roles: list[str] = Field(default_factory=list)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=256)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
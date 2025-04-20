from pydantic import BaseModel
from src.schemas.user import UserCreate


class LoginRequest(UserCreate):
    pass


class RegisterRequest(UserCreate):
    pass


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class RegisterResponse(LoginResponse):
    pass


class RefreshRequest(BaseModel):
    refresh_token: str

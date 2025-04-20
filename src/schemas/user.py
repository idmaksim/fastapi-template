from datetime import datetime
from pydantic import BaseModel, EmailStr

from src.schemas.media import MediaResponse


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: str
    created_at: datetime
    avatar: MediaResponse | None

    class Config:
        from_attributes = True

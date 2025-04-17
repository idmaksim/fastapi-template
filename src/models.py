from datetime import datetime

from cuid2 import cuid_wrapper
from pydantic import BaseModel, Field
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

cuid_generator = cuid_wrapper()


class PaginationModel(BaseModel):
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=0)


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=cuid_generator)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

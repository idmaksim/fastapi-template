from datetime import datetime

from cuid2 import cuid_wrapper
from pydantic import BaseModel, Field
from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.types.media_types import MediaType

cuid_generator = cuid_wrapper()


class PaginationModel(BaseModel):
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=0)


class Media(Base):
    __tablename__ = "medias"

    id: Mapped[str] = mapped_column(primary_key=True, default=cuid_generator)
    type: Mapped[MediaType] = mapped_column(Enum(MediaType))
    url: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user: Mapped["User"] = relationship(back_populates="avatar")


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=cuid_generator)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    avatar_id: Mapped[str] = mapped_column(ForeignKey("medias.id"), nullable=True)
    avatar: Mapped["Media"] = relationship(back_populates="user")

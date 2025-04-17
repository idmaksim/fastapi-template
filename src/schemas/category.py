import datetime
from typing import TYPE_CHECKING, List, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from src.schemas.item import ItemResponse


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class CategoryWithItems(CategoryResponse):
    items: List["ItemResponse"]

    class Config:
        from_attributes = True

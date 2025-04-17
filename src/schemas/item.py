from datetime import datetime

from pydantic import BaseModel

from .category import CategoryResponse


class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
    category_id: int


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda dt: dt.isoformat()}


class ItemWithCategoryResponse(ItemBase):
    id: int
    created_at: datetime
    category: CategoryResponse

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda dt: dt.isoformat()}

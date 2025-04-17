from typing import List
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.dependencies.item_dependency import ItemServiceDep
from src.dependencies.pagination_dependency import PaginationDep
from src.schemas.item import ItemCreate, ItemWithCategoryResponse

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/items/", response_model=ItemWithCategoryResponse)
async def create_item(item: ItemCreate, service: ItemServiceDep):
    return await service.create_item(item)


@router.get("/items/", response_model=List[ItemWithCategoryResponse])
@cache(expire=60)
async def read_items(pagination: PaginationDep, service: ItemServiceDep):
    return await service.read_items(pagination)


@router.get("/items/{item_id}", response_model=ItemWithCategoryResponse)
@cache(expire=60)
async def read_item(item_id: int, service: ItemServiceDep):
    return await service.read_item(item_id)

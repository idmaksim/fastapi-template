from typing import List

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.dependencies.category_dependency import CategoryServiceDep
from src.dependencies.pagination_dependency import PaginationDep
from src.schemas.category import CategoryCreate, CategoryResponse
from src.schemas.item import ItemWithCategoryResponse

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/categories/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, service: CategoryServiceDep):
    return await service.create_category(category)


@router.get("/categories/", response_model=List[CategoryResponse])
@cache(expire=60)
async def read_categories(pagination: PaginationDep, service: CategoryServiceDep):
    return await service.read_categories(pagination)


@router.get(
    "/categories/{category_id}/items/", response_model=List[ItemWithCategoryResponse]
)
@cache(expire=60)
async def read_category_items(category_id: int, service: CategoryServiceDep):
    return await service.read_category_items(category_id)

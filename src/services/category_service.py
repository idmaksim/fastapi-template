from typing import List

from fastapi import HTTPException
from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import src.models as models
from src.dependencies.session_dependency import SessionDep
from src.schemas.category import CategoryCreate, CategoryResponse
from src.schemas.item import ItemWithCategoryResponse


class CategoryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def ensure_category_exists(self, category_id: int) -> bool:
        query = select(exists().where(models.Category.id == category_id))
        result = await self.db.execute(query)
        category_exists = result.scalar()

        if not category_exists:
            raise HTTPException(
                status_code=404, detail=f"Category with id {category_id} not found"
            )

    async def create_category(self, category: CategoryCreate) -> CategoryResponse:
        db_category = models.Category(**category.model_dump())
        self.db.add(db_category)
        await self.db.commit()
        await self.db.refresh(db_category)
        return db_category

    async def read_categories(
        self, pagination: models.PaginationModel
    ) -> List[CategoryResponse]:
        query = (
            select(models.Category)
            .options(selectinload(models.Category.items))
            .offset(pagination.skip)
            .limit(pagination.limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all()

    async def read_category_items(
        self, category_id: int
    ) -> List[ItemWithCategoryResponse]:
        query = (
            select(models.Item)
            .options(selectinload(models.Item.category))
            .filter(models.Category.id == category_id)
        )
        result = await self.db.execute(query)
        items = result.scalars().all()
        if not items:
            raise HTTPException(
                status_code=404,
                detail=f"Category with id {category_id} not found or has no items",
            )
        return items


async def get_category_service(db: SessionDep) -> CategoryService:
    return CategoryService(db)

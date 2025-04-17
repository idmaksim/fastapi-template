from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import src.models as models
from src.dependencies.category_dependency import CategoryServiceDep
from src.dependencies.session_dependency import SessionDep
from src.schemas.item import ItemCreate, ItemResponse
from src.services.category_service import CategoryService


class ItemService:
    def __init__(self, db: AsyncSession, category_service: CategoryService):
        self.db = db
        self.category_service = category_service

    async def read_item(self, item_id: int) -> ItemResponse:
        query = (
            select(models.Item)
            .options(selectinload(models.Item.category))
            .filter(models.Item.id == item_id)
        )

        result = await self.db.execute(query)
        item = result.scalar_one_or_none()

        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    async def read_items(self, pagination: models.PaginationModel):
        query = (
            select(models.Item)
            .options(selectinload(models.Item.category))
            .offset(pagination.skip)
            .limit(pagination.limit)
        )

        result = await self.db.execute(query)
        response = result.scalars().all()
        return response

    async def create_item(self, item: ItemCreate) -> ItemResponse:
        await self.category_service.ensure_category_exists(item.category_id)

        try:
            db_item = models.Item(**item.model_dump())
            self.db.add(db_item)

            await self.db.commit()
            await self.db.refresh(db_item, attribute_names=["category"])

            return db_item

        except Exception as e:
            await self.db.rollback()
            raise HTTPException(
                status_code=500, detail=f"Failed to create item: {str(e)}"
            )


def get_item_service(
    db: SessionDep, category_service: CategoryServiceDep
) -> ItemService:
    return ItemService(db, category_service)

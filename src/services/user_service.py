from fastapi import HTTPException
from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.password_service import hash_password
import src.models as models
from src.dependencies.session_dependency import SessionAnnotatedDep
from src.schemas.user import UserCreate
from src.logger import logger
from sqlalchemy.orm import selectinload


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, id: str) -> models.User:
        logger.info("Getting user by id")
        query = (
            select(models.User)
            .options(selectinload(models.User.avatar))
            .where(models.User.id == id)
        )
        result = await self.db.execute(query)
        user = result.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def get_user_by_email(self, email: str) -> models.User:
        logger.info("Getting user by email")
        query = select(models.User).where(models.User.email == email)
        result = await self.db.execute(query)
        user = result.scalar_one_or_none()
        if user is None:
            logger.error("User not found")
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def ensure_not_exists_by_email(self, email: str) -> None:
        logger.info("Ensuring user does not exist by email")
        query = select(exists(models.User).where(models.User.email == email))
        result = await self.db.execute(query)
        user_exists = result.scalar_one()
        if user_exists:
            logger.error("User already exists")
            raise HTTPException(status_code=409, detail="User already exists")

    async def create_user(self, user: UserCreate) -> models.User:
        logger.info("Creating user")
        await self.ensure_not_exists_by_email(user.email)
        hashed_password = await hash_password(user.password)
        db_user = models.User(
            email=user.email,
            password=hashed_password,
        )
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user


async def get_user_service(db: SessionAnnotatedDep) -> UserService:
    return UserService(db)

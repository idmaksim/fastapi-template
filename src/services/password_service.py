from passlib.context import CryptContext

from src.logger import logger

context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=4)


async def hash_password(password: str) -> str:
    logger.info("Hashing password")
    return context.hash(password)


async def verify_password(password: str, hashed_password: str) -> bool:
    logger.info("Verifying password")
    return context.verify(password, hashed_password)

from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=4)


async def hash_password(password: str) -> str:
    return context.hash(password)


async def verify_password(password: str, hashed_password: str) -> bool:
    return context.verify(password, hashed_password)

from fastapi import APIRouter

from src.env import CACHE_TTL
from src.dependencies.jwt_dependencies import CurrentUser
from src.schemas.user import UserResponse
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
@cache(expire=CACHE_TTL)
async def get_me(user: CurrentUser):
    return user

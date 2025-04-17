from fastapi import APIRouter

from src.dependencies.auth_dependency import AuthServiceDep
from src.schemas.auth import LoginRequest, RegisterRequest


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(credentials: LoginRequest, auth_service: AuthServiceDep):
    return await auth_service.login(credentials)


@router.post("/register")
async def register(credentials: RegisterRequest, auth_service: AuthServiceDep):
    return await auth_service.register(credentials)

from fastapi import APIRouter

from src.dependencies.auth_dependency import AuthServiceDep
from src.schemas.auth import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
)


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
async def login(credentials: LoginRequest, auth_service: AuthServiceDep):
    return await auth_service.login(credentials)


@router.post("/register", response_model=RegisterResponse)
async def register(credentials: RegisterRequest, auth_service: AuthServiceDep):
    return await auth_service.register(credentials)

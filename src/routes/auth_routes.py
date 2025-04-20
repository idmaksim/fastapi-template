from fastapi import APIRouter

from src.dependencies.auth_dependencies import AuthServiceDep
from src.schemas.auth import (
    LoginRequest,
    LoginResponse,
    RefreshRequest,
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


@router.post("/refresh", response_model=LoginResponse)
async def refresh(refresh_token_request: RefreshRequest, auth_service: AuthServiceDep):
    return await auth_service.validate_refresh_token(
        refresh_token_request.refresh_token
    )

from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.dependencies.auth_dependencies import AuthServiceAnnotatedDep
from src.dependencies.user_dependency import UserServiceAnnotatedDep
from src.types.jwt_sub import JWTSub
from src.logger import logger

security = HTTPBearer(auto_error=False)

INVALID_TOKEN_EXCEPTION = HTTPException(
    status_code=401,
    detail="Invalid authentication token",
    headers={"WWW-Authenticate": "Bearer"},
)


async def required_jwt(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    auth_service: AuthServiceAnnotatedDep,
) -> JWTSub:
    try:
        logger.info("Validating access token")
        return await auth_service.validate_access_token(credentials.credentials)
    except Exception:
        logger.warning("Failed to validate JWT token")
        raise INVALID_TOKEN_EXCEPTION


async def get_current_user_token(
    user_service: UserServiceAnnotatedDep,
    jwt_sub: JWTSub = Depends(required_jwt),
) -> JWTSub:
    try:
        logger.info("Getting current user token")
        return await user_service.get_by_id(jwt_sub.id)
    except Exception:
        logger.warning(f"Failed to get user with id {jwt_sub.id}")
        raise INVALID_TOKEN_EXCEPTION


JwtAnnotatedDep = Annotated[JWTSub, Depends(required_jwt)]
JwtDep = Depends(required_jwt)
CurrentUser = Annotated[JWTSub, Depends(get_current_user_token)]

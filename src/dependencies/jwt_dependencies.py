from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.dependencies.user_dependency import UserServiceDep
from src.dependencies.auth_dependency import AuthServiceDep
from src.types.jwt_sub import JWTSub
from jose import jwt

security = HTTPBearer()


async def get_current_user_token(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    auth_service: AuthServiceDep,
    user_service: UserServiceDep,
) -> JWTSub:
    try:
        jwt_sub = await auth_service.validate_access_token(credentials.credentials)
        return await user_service.get_by_id(jwt_sub.id)
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )


CurrentUser = Annotated[JWTSub, Depends(get_current_user_token)]

from datetime import datetime, timedelta
from src.env import ACCESS_TOKEN_SECRET, REFRESH_TOKEN_SECRET
from src.dependencies.user_dependency import UserServiceDep
from src.schemas.auth import LoginRequest, RegisterRequest
from src.services.user_service import UserService
from jose import jwt
import asyncio

from src.types.jwt_sub import JWTSub


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def login(self, body: LoginRequest) -> bool:
        user = await self.user_service.get_user_by_email(body.email)
        if not user:
            return False
        # if not verify_password(password, user.password):
        # return False
        return True

    async def register(self, body: RegisterRequest) -> dict[str, str]:
        user = await self.user_service.create_user(body)
        jwt_sub = JWTSub(id=user.id)

        access_token, refresh_token = await asyncio.gather(
            self.get_access_token(jwt_sub), self.get_refresh_token(jwt_sub)
        )

        return {"access_token": access_token, "refresh_token": refresh_token}

    async def get_access_token(self, data: JWTSub) -> str:
        return jwt.encode(
            claims=dict(
                **data.model_dump(),
                iat=datetime.now(),
                exp=datetime.now() + timedelta(minutes=15),
            ),
            key=ACCESS_TOKEN_SECRET,
            algorithm="HS256",
        )

    async def get_refresh_token(self, data: JWTSub) -> str:
        return jwt.encode(
            claims=dict(
                **data.model_dump(),
                iat=datetime.now(),
                exp=datetime.now() + timedelta(days=7),
            ),
            key=REFRESH_TOKEN_SECRET,
            algorithm="HS256",
        )


async def get_auth_service(user_service: UserServiceDep) -> AuthService:
    return AuthService(user_service)

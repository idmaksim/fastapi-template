from typing import Annotated

from fastapi import Depends

from src.services.user_service import UserService, get_user_service

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

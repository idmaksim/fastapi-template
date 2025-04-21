from typing import Annotated

from fastapi import Depends

from src.services.user_service import UserService, get_user_service


UserServiceAnnotatedDep = Annotated[UserService, Depends(get_user_service)]

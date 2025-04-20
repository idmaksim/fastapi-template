from typing import Annotated

from fastapi import Depends

from src.services.auth_service import AuthService, get_auth_service


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]

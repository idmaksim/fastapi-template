from typing import Annotated

from fastapi import Depends

from src.services.auth_service import AuthService, get_auth_service


AuthServiceAnnotatedDep = Annotated[AuthService, Depends(get_auth_service)]

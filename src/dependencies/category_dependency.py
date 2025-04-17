from typing import Annotated

from fastapi import Depends

from src.services.category_service import CategoryService, get_category_service

CategoryServiceDep = Annotated[CategoryService, Depends(get_category_service)]

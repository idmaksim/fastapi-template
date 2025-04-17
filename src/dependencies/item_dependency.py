from typing import Annotated

from fastapi import Depends

from src.services.item_service import ItemService, get_item_service

ItemServiceDep = Annotated[ItemService, Depends(get_item_service)]

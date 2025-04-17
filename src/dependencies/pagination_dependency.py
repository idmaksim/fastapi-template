from typing import Annotated

from fastapi import Query

from src.models import PaginationModel

PaginationDep = Annotated[PaginationModel, Query()]

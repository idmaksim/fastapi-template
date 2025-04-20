from pydantic import BaseModel

from src.types.media_types import MediaType


class MediaResponse(BaseModel):
    id: str
    type: MediaType
    url: str

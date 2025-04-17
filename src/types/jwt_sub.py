from pydantic import BaseModel


class JWTSub(BaseModel):
    id: str

    class Config:
        from_attributes = True

from pydantic import BaseModel


class JWTSub(BaseModel):
    id: int

    class Config:
        from_attributes = True

from datetime import datetime

from pydantic import BaseModel


class BlockCreateSchema(BaseModel):
    data: str
    data_sign: str


class BlockSignSchema(BaseModel):
    signature: str


class BlockRetrieveSchema(BlockCreateSchema):
    index: int
    timestamp: datetime
    previous_hash: str
    sign: str | None

    class Config:
        orm_mode = True

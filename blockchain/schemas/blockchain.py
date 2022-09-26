from datetime import datetime

from pydantic import BaseModel


class BlockCreateSchema(BaseModel):
    data: str
    data_signature: str


class BlockSignSchema(BaseModel):
    signature: str


class BlockRetrieveSchema(BlockCreateSchema):
    index: int
    timestamp: datetime
    proof: int
    previous_hash: str

    class Config:
        orm_mode = True

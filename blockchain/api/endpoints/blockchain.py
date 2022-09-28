from fastapi import APIRouter

from schemas.blockchain import BlockRetrieveSchema, BlockCreateSchema, BlockSignSchema
from services.blockchain import BlockService

router = APIRouter()


@router.get("/", response_model=list[BlockRetrieveSchema])
async def get_blockchain():
    return await BlockService().get_all()


@router.post("/")
async def create_block(block: BlockCreateSchema):
    return await BlockService().create_block(block_data=block)


@router.get("/{id}/hash/")
async def get_block(id: int):
    return await BlockService().get_block_hash(id)


@router.patch("/{id}/close/")
async def close_block(id: int, block: BlockSignSchema):
    return await BlockService().close_block(block_index=id, data=block)


@router.get("/integrity/")
async def check_blockchain_integrity():
    return await BlockService().verify_blockchain()

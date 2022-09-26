from fastapi import APIRouter

from schemas.blockchain import BlockRetrieveSchema
from services.blockchain import BlockService

router = APIRouter()


@router.get("/all/", response_model=list[BlockRetrieveSchema])
async def get_blockchain():
    return BlockService().get_all()

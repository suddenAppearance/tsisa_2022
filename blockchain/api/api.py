from fastapi import APIRouter
from api.endpoints.blockchain import router as blockchain_router

router = APIRouter()

router.include_router(blockchain_router, tags=['blockchain'])

import binascii
import json

from cryptography.hazmat.primitives.hashes import Hash, SHA256
from fastapi import HTTPException

from models import Block
from repositories.blockchain import BlockRepository
from schemas.blockchain import BlockCreateSchema, BlockRetrieveSchema, BlockSignSchema


class BlockService:
    def __init__(self):
        self.repository = BlockRepository()

    @staticmethod
    def _calculate_hash(data: str) -> str:
        hasher = Hash(SHA256())
        hasher.update(data.encode())
        digest = hasher.finalize()
        return binascii.hexlify(digest).decode()

    async def create_block(self, block_data: BlockCreateSchema) -> BlockRetrieveSchema:
        if not (block := await self.repository.get_last()):
            previous_hash = 'Initial block'
        else:
            previous_hash = await self.get_block_hash(block.index)
        block = Block(data=block_data.data, data_sign=block_data.data_sign, previous_hash=previous_hash)
        return BlockRetrieveSchema.from_orm(await self.repository.save(block))

    async def get_block_hash(self, block_index: int) -> str:
        if not (block := await self.repository.get_block_by_id(block_index)):
            raise HTTPException(status_code=404, detail="No such block")

        block_data = {
            "data": block.data,
            "data_sign": block.data_sign,
            "previous_hash": block.previous_hash
        }
        return self._calculate_hash(json.dumps(block_data, sort_keys=True))

    async def close_block(self, block_index: int, data: BlockSignSchema) -> BlockRetrieveSchema:
        if not (block := await self.repository.get_open_block_by_index(block_index)):
            raise HTTPException(status_code=404, detail="No such block")

        block.sign = data.signature
        return BlockRetrieveSchema.from_orm(await self.repository.save(block))

    async def get_all(self) -> list[BlockRetrieveSchema]:
        return [BlockRetrieveSchema.from_orm(block) for block in await self.repository.get_all()]

    async def verify_blockchain(self) -> bool:
        blockchain = await self.repository.get_all()
        if not blockchain:
            return True
        prev_hash = await self.get_block_hash(blockchain[0].index)
        for block in blockchain[1:]:
            if prev_hash != block.previous_hash:
                return False
            prev_hash = await self.get_block_hash(block.index)
        return True

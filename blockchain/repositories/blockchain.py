from sqlalchemy import select, func

from models import Block
from repositories.base import BaseRepository


class BlockRepository(BaseRepository):
    async def create(self, block: Block) -> Block:
        return await self.save(block)

    async def get_first(self) -> Block | None:
        statement = select(Block).filter(Block.sign.is_not(None)).limit(1).order_by(Block.index)
        return await self.one_or_none(statement)

    async def get_open_block_by_index(self, index: int) -> Block | None:
        statement = select(Block).filter(Block.index == index, Block.sign.is_(None))
        return await self.one_or_none(statement)

    async def get_block_by_id(self, index: int) -> Block | None:
        statement = select(Block).filter(Block.index == index)
        return await self.one_or_none(statement)

    async def get_last(self) -> Block | None:
        statement = select(Block).filter(Block.sign.is_not(None)).limit(1).order_by(Block.index.desc())
        return await self.one_or_none(statement)

    async def get_all(self) -> list[Block]:
        statement = select(Block).filter(Block.sign.is_not(None)).order_by(Block.index)
        return await self.all(statement)

    async def count(self) -> int:
        statement = select(func.count(Block.index)).filter(Block.sign.is_not(None))
        return (await self.execute(statement)).scalar_one()

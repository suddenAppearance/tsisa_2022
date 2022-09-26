import abc
import logging
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select, Update, Delete

from models.base import create_async_session

logger = logging.getLogger("api")

T = TypeVar("T")


def transaction_block(func):
    async def wrapper(self, *args, **kwargs):
        async with create_async_session() as session:
            self.session = session
            result = await func(self, *args, **kwargs)
            await self.session.commit()
            return result

    return wrapper


class BaseRepository(abc.ABC, Generic[T]):
    session: AsyncSession

    @transaction_block
    async def save(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    @transaction_block
    async def batch_save(self, objs: list):
        self.session.add_all(objs)

    @transaction_block
    async def one_or_none(self, statement):
        return (await self.session.execute(statement)).scalars().one_or_none()

    @transaction_block
    async def all(self, statement: Select):
        return (await self.session.execute(statement)).scalars().all()

    @transaction_block
    async def execute(self, statement: Select | Update | Delete):
        return await self.session.execute(statement)

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from core import settings

Base = declarative_base()
async_engine = create_async_engine(settings.ASYNC_DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)

create_async_session = sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)
create_session = sessionmaker(bind=engine, expire_on_commit=False)

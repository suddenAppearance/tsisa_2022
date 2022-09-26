from sqlalchemy import Column, BigInteger, DateTime, func, Text, Integer, String

from models.base import Base


class Block(Base):
    __tablename__ = 'block'

    index = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    data = Column(Text, nullable=False)
    previous_hash = Column(String)
    sign = Column(String)
    data_sign = Column(String)

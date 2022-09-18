import os
import random

from sqlalchemy import create_engine, BigInteger, Column, String, ForeignKey, Integer, Float, select
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine("postgresql://balance901:Sa_901_dkj;@89.108.115.118:5432/balance901")
create_session = sessionmaker(bind=engine, expire_on_commit=False)


class Company(Base):
    __tablename__ = 'company'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    company_owner = Column(String)
    code = Column(String)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(dict(filter(lambda s: not s[0].startswith("_"), self.__dict__.items())))


class CompanyRequirement(Base):
    __tablename__ = 'company_requirement'

    id = Column(BigInteger, primary_key=True)
    company_id = Column(ForeignKey("company.id"))
    product_id = Column(ForeignKey("product.id"))
    count_product = Column(Integer)

    company = relationship("Company", backref="company_requirements")
    product = relationship("Product", backref="company_requirements")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(dict(filter(lambda s: not s[0].startswith("_"), self.__dict__.items())))


class ConsumerRequirementBase(Base):
    __tablename__ = 'consumer_requirement_base'

    id = Column(BigInteger, primary_key=True)
    product_id = Column(ForeignKey("product.id"))
    count_product = Column(Integer)
    consumer_name = Column(String)

    product = relationship("Product", backref="comsumer_requirements")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(dict(filter(lambda s: not s[0].startswith("_"), self.__dict__.items())))


class Product(Base):
    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    company_id = Column(ForeignKey("company.id"))
    price = Column(Float)

    company = relationship("Company", backref="product")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(dict(filter(lambda s: not s[0].startswith("_"), self.__dict__.items())))


class UserSelect(Base):
    __tablename__ = 'user_select'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    selected_company = Column(String)


session = create_session()

product_ids = session.execute(select(Product.id).filter(Product.company_id == 2)).scalars().all()

for product_id in product_ids:
    for i in range(random.randint(0, 3)):
        session.add(ConsumerRequirementBase(
            product_id=product_id,
            count_product=random.randint(10, 30),
            consumer_name=["Вася Пупкин", "Иван Иванов", "Акакий Акакиевич"][i]
        ))

session.commit()

from sqlalchemy import Column, Integer, String,DateTime
from database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    bridge_id = Column(String)
    authentication_token = Column(String)
    machine_id = Column(String, unique=True)
    bearer_token = Column(String)


class Auth(Base):
    __tablename__ = "auth"
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    authentication_token = Column(String)


class Discount(Base):
    __tablename__ = "discount"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name_of_company = Column(String)
    discount_product_name = Column(String)
    discount_price = Column(String)
    normal_price = Column(String)
    discount_percentage = Column(String)
    discount_product_url = Column(String)
    discount_product_image_url = Column(String)
    discount_timestamp = Column(DateTime(timezone=True), default=func.now())

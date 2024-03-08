from itertools import product
from sqlalchemy import Column, Integer, String, Sequence, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from ..database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    firstName = Column(String(255))
    lastName = Column(String(255))
    password = Column(String)
    gender = Column(String(255), default='null')
    email = Column(String(255), default='null')
    phone = Column(String(255))
    location = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    role = Column(String(255), default="user")
    plan = Column(String(255), default="free")
    plan_expire_date = Column(DateTime(timezone=True), server_default=func.now())
    verified = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)
    others = Column(JSON, default='null')

class Verify(Base):
    __tablename__ = "verify"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer)
    code = Column(String(255), default='0000')
    used = Column(Boolean, default=False)
    datetime = Column(DateTime(timezone=True), server_default=func.now())


class UserPlants(Base):
    __tablename__ = "userplants"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, default=3)
    date = Column(DateTime(timezone=True), server_default=func.now())
    imgurl = Column(String)
    lable = Column(JSON)
    disease = Column(String)
    details = Column(JSON)
    deleted = Column(Boolean, default=False)


class DembeghaPost(Base):
    __tablename__ = "dembegha"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    img = Column(String)
    detail = Column(String)
    price_range = Column(String)
    location =  Column(String)
    user_id = Column(String)
    product_name = Column(String)
    catagory = Column(String)


class BaleSuqOffer(Base):
    __tablename__ = "balesuqoffer"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    poster_id = Column(String)
    post_id = Column(String)
    location = Column(String)
    price = Column(String)
    offerer_id = Column(String)
    offerer_name = Column(String)
    details = Column(String)




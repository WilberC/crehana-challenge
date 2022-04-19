from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Geo(Base):
    __tablename__ = "geo"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(String)
    lng = Column(String)
    addresses = relationship("Address", back_populates="geo")


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)
    geo_id = Column(Integer, ForeignKey("geo.id"))
    geo = relationship("Geo", back_populates="addresses")
    users = relationship("User", back_populates="address")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    catchPhrase = Column(String)
    bs = Column(String)
    companies = relationship("User", back_populates="company")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    address_id = Column(Integer, ForeignKey("addresses.id"))
    address = relationship("Address", back_populates="users")
    phone = Column(String)
    website = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="companies")
    posts = relationship("Post", back_populates="user")

from .db_config import DATABASE_URL

from sqlalchemy import create_engine, Integer, String, DECIMAL, Column, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine(DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(255), nullable=False, unique=True)

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(255), nullable=False)
    unit_abbreviation = Column(String(10), nullable=False, unique=True)

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String(255), nullable=False)
    location_type = Column(String(30), nullable=False)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(30), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    default_unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    default_quantity = Column(Integer, nullable=False)
    average_price = Column(DECIMAL(10,2), nullable=False)
    notes = Column(String(255))

    category = relationship("Category")
    default_unit = relationship("Unit")

class Grocery(Base):
    __tablename__ = "groceries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_id = Column(Integer, ForeignKey("units.id", ondelete="CASCADE"), nullable=False)
    bought_date = Column(DateTime)
    expiration_date = Column(DateTime)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="CASCADE"), nullable=False)
    is_consumed = Column(Boolean, nullable=False)
    notes = Column(String(255))

    product = relationship("Product")
    unit = relationship("Unit")
    location = relationship("Location")

class Item(Base):
    __tablename__ = "shopping_list"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit = Column(String)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    added_time = Column(DateTime, default=func.now())
    purchased = Column(Boolean, nullable=False, default=False,)
    purchased_time = Column(DateTime)
    removed = Column(Boolean, nullable=False, default=False)

    product = relationship("Product")
    unit = relationship("Unit")

Base.metadata.create_all(engine)


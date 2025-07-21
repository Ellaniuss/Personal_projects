'''
I have to fix relationships in orm_models tables and then I can try new_item.py with adding new item into Category table
'''


from .db_config import DATABASE_URL

from sqlalchemy import create_engine, Integer, String, Float, Column, Date, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, foreign

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class Grocery(Base):
    __tablename__ = "groceries"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.item_id"), ondelete="CASCADE", nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_id = Column(Integer, ForeignKey("units.unit_id"), ondelete="CASCADE", nullable=False)
    bought_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=True)
    location_id = Column(Integer, ForeignKey("locations.location_id"), ondelete="CASCADE", nullable=False)
    is_consumed = Column(Boolean, nullable=False)
    notes = Column(String(255))

    product = relationship("Product", back_populates="groceries")
    unit = relationship("Unit", back_populates="groceries")
    locations = relationship("Location", back_populates="groceries")



class Product(Base):
    __tablename__ = "products"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), nullable=False)
    category_id = Column(String(30), ForeignKey("categories.category_id"), nullable=False)
    default_unit_id = Column(Integer, ForeignKey("units.unit_id"), nullable=False)
    default_quantity = Column(Integer, nullable=False)
    average_price = Column(Float, nullable=False)
    notes = Column(String(255))

    groceries = relationship("Grocery", back_populates="products")
    category = relationship("Category", back_populates="products")
    deafult_unit = relationship("Unit", back_populates="products")

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(255), nullable=False)

    products = relationship("Product", back_populates="categories")

class Location(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String(255), nullable=False)
    location_type = Column(String(30), nullable=False)

    groceries = relationship("Grocery", back_populates="locations")

class Unit(Base):
    __tablename__ = "units"
    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(255), nullable=False)
    unit_abbreviation = Column(String(10), nullable=False)

    products = relationship("Product", back_populates="units")
    groceries = relationship("Grocery", back_populates="unit")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# new_item = Item(name='Bread', quantity=1, place='Shelf')


# session.add(new_item)
session.commit()


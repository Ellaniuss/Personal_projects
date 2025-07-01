from db_config import DATABASE_URL

from sqlalchemy import create_engine, Integer, String, Float, Column, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, foreign

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class Grocery(Base):
    __tablename__ = "groceries"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, foreign_key=True)
    quantity = Column(Integer, nullable=False)
    unit_id = Column(Integer, nullable=False)
    bought_date = Column(Date, nullable=False)
    sold_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=True)
    location_id = Column(String(30)
    is_consumed = Column(Boolean, nullable=False)
    notes = Column(Text)
    product = relationship("Product", back_populates="groceries")
    unit = relationship("Unit", back_populates="groceries_unit")
    location = relationship("Location", back_populates="groceries")

class Product(Base):
    __tablename__ = "products"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), nullable=False)
    category_id = Column(String(30), ForeignKey("categories.category_id") nullable=False)
    default_unit_id = Column(Integer, ForeignKey("units.unit_id"), nullable=False)
    default_quantity = Column(Integer, nullable=False)
    average_price = Column(Float, nullable=False)
    notes = Column(Text)

    category = relationship("Category", back_populates="products")
    default_unit = relationship("Unit", back_populates="product_default_unit")
    groceries = relationship("Grocery", back_populates="product")

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(255), nullable=False)

    products = relationship("Product", back_populates="category")

class Location(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String(255), nullable=False)
    location_type = Column(String(30), nullable=False)

    groceries = relationship("Grocery", back_populates="location")

class Unit(Base):
    __tablename__ = "units"
    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(255), nullable=False)
    unit_abbreviation = Column(String(10), nullable=False)

    product_default_unit = relationship("Product", back_populates="default_unit")
    groceries_unit = relationship("Grocery", back_populates="unit")








Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# new_item = Item(name='Bread', quantity=1, place='Shelf')


session.add(new_item)
session.commit()


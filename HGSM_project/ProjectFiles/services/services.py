from ProjectFiles.database.db_config import DATABASE_URL
from ProjectFiles.database.orm_models import Base, Category, engine

from sqlalchemy import create_engine, Integer,String, Column
from sqlalchemy.orm import declarative_base,sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_category = Category(category_name="frozen")

session.add(new_category)
session.commit()

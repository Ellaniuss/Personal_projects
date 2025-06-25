from db_config import DATABASE_URL

from sqlalchemy import create_engine, Integer, String, Float, Column, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class Item(Base):
    __tablename__ = "groceries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(Date)
    place = Column(String(30))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


new_item = Item(name='Bread', quantity=1, place='Shelf')


session.add(new_item)
session.commit()


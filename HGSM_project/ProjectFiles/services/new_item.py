'''
I have to fix relationships in orm_models tables and then I can try new_item.py with adding new item into Category table
'''

from ProjectFiles.database.db_config import DATABASE_URL
from ProjectFiles.database.orm_models import Base, Category, engine

from sqlalchemy import create_engine, Integer,String, Column
from sqlalchemy.orm import declarative_base,sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base.metadata.create_all(bind=engine)

class CategoryService:
    def __init__(self, db_session_factory):
        self.db_session_factory = db_session_factory

    def add_category(self, category_name: str) -> Category:
        with self.db_session_factory() as session:
            new_category = Category(category_name = category_name)
            session.add(new_category)
            session.commit()
            session.refresh(new_category)
            print(f"Successfully added category: {new_category}")



if __name__ == "__main__":
    category_service = CategoryService(SessionLocal)
    print("Attempting to add categories...")

    temp_category_name = input("New category name to add:   ")
    added_category = category_service.add_category(category_name=temp_category_name)
    print("\nFinished adding categories.")
    print(f"You added: {added_category.category_name} with ID: {added_category.category_id}")


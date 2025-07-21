from ProjectFiles.database.db_config import DATABASE_URL
from ProjectFiles.database.orm_models import Base, Category, engine

from sqlalchemy import create_engine, Integer,String, Column
from sqlalchemy.orm import declarative_base,sessionmaker

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)

class CategoryService:
    def __init__(self, session_creator):
        self.session_creator = session_creator

    def add_category(self, category_name: str):
        with self.session_creator() as session:
            duplicate = session.query(Category).filter_by(category_name=category_name).first()
            if duplicate:
                print(f"Category '{category_name}' already exists.")
                return duplicate

            new_category = Category(category_name=category_name)
            session.add(new_category)
            session.commit()
            session.refresh(new_category)
            print(f"Successfully added category: {new_category.category_name}")
            return new_category

    def remove_category(self, category_id: int):
        with self.session_creator() as session:
            category = session.get(Category, category_id)
            if not category:
                print(f"Category with ID {category_id} not found")
                return False
            session.delete(category)
            session.commit()
            print(f"Successfully removed category with ID {category_id}")
            return True

class ShoppingListService:
    pass




if __name__ == "__main__":
    choice = int(input("Choose from action you like to perform: 1. Add category, 2. Remove category \n ___choice number___:  "))
    if choice == 1:
        print("Add new category")
        category_name = input("Enter category name:  ")
        added_category = CategoryService(SessionLocal).add_category(category_name)
        if added_category:
            print(f"Category {added_category.category_name} was added to the table categories.")
        else:
            print("Failed")
    elif choice == 2:
        print("Remove existing category")
        category_id = int(input("Enter category ID for removal: "))
        removed_category = CategoryService(SessionLocal).remove_category(category_id)
        if removed_category:
            print(f"Category was successfully removed from the table")
        else:
            print("Failed")

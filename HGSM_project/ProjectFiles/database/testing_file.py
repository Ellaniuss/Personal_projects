from sqlalchemy import create_engine, text, Table, MetaData, Column, Integer, String, ForeignKey

from db_config import DATABASE_URL

'''
The start of any SQLAlchemy application is an object called the Engine.
The engine is typically a global object created just once for a particular database server.
The main argument to create_engine is a string URL - mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
    - three important facts: 
        a) type of database (mariadb as dialect)
        b) DBAPI as third party driver (mariadbconnector) 
        c) database location, URL
    In our code this is all setup in script db_config.py
'''

engine = create_engine(DATABASE_URL, echo=True)
# creating table with text() construct using engine.connect(). In this case we need .commit() method to execute
# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE IF NOT EXISTS testing_table (x INT, y INT)"))
#     conn.execute(
#         text("INSERT INTO testing_table (x, y) VALUES (:x, :y)"),
#         [{"x":1, "y":1}, {"x":2, "y":2}]
#     )
#     conn.commit()

# with engine.begin() as conn:    # engine.begin() automatically commits or rollback in case of error = no need for .commit()
#     conn.execute(
#        text("INSERT INTO testing_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
#      )
# fetching rows with result() object

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x,y FROM testing_table"))
#     for row in result:
#         print(f"x: {row.x}, y: {row.y}")
#
# with engine.begin() as conn:
#     conn.execute(text("DROP TABLE testing_table "))

# metadata_obj = MetaData()
#
# testing_table = Table(
#     "testing_table1",
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(30)),
#     Column('quantity', Integer)
# )
# testing_table2 = Table(
#     "testing_table2",
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('name_id', ForeignKey('testing_table1.id'), nullable=False),
#     Column('date', String(30), nullable=False)
# )
#
# metadata_obj.create_all(engine)

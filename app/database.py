from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#For database (Postgre)
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# #The purpose of this loop is to continuosly run until successfully connect to the Database
# while True:

# #PostgreSQL Database
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi-PythonAPIDevelopment-project1', user='postgres', password='Vamvam04.', cursor_factory=RealDictCursor)    
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to the database failed")
#         print("Error: ", error)
#         time.sleep(2)
import os
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# .env values
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_APPNAME = os.getenv("DB_APPNAME", "app")

SQLALCHEMY_DATABASE_URL = (f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=45, pool_recycle=3600
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas exitosamente.")
    except SQLAlchemyError as e:
        print(f"Error al crear las tablas: {str(e)}")
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os

load_dotenv()

db_url = os.getenv("DB_URL","postgresql://postgres:1234@localhost:5432/stock_tracker")

engine = create_engine(db_url)

class Base(DeclarativeBase):
    pass
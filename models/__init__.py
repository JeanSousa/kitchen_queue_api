from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# import model elements
from models.base import BaseModel
from models.product import Product

db_path = '/database'

# Check if directory exists, then create database
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Sqlite access url 
db_url = f"sqlite:///{db_path}/db.sqlite"

# Create database connection engine with disable query logs
engine = create_engine(db_url, echo=False)

# Instantiate a section creator with the database
Session = sessionmaker(bind=engine)

# Create database if not exists
if not database_exists(engine.url):
    create_database(engine.url)

# Create database tables if not exists
Base.metadata.create_all(engine)
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from models import BaseModel

class Product(BaseModel):
    __tablename__ = 'product'

    id = Column("pk_product", Integer, primary_key=True)
    name = Column(String(200), unique=True)
    value = Column(Float)

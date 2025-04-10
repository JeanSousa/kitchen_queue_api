from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from models.base import BaseModel

class Product(BaseModel):
    __tablename__ = 'product'

    id = Column("pk_product", Integer, primary_key=True)
    name = Column(String(200), unique=True)
    value = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime

from models.base import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    """Table definition."""
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)
    value = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    def __init__(self, name, value):
        """
        Create a product

        Arguments:
            name: product name.
            value: expected value for the product.
        """
        self.name = name 
        self.value = value 

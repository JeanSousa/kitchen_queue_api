from datetime import datetime 
from sqlalchemy import Column, Integer, ForeignKey, DateTime

from models.base import BaseModel


class OrderProduct(BaseModel):
    __tablename__ = 'order_products'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    def __init__(self, order_id, product_id, amount):
        """
        Create an order with products

        Arguments:
            order_id: order id.
            product_id: product id.
            amount: item amount of order.
        """
        self.order_id = order_id
        self.product_id = product_id
        self.amount = amount



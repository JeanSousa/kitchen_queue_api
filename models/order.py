from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum as SqlEnum

from models.base import BaseModel

class OrderStatusEnum(str, Enum):
    IN_QUEUE = "NA_FILA"
    PREPARING = "PREPARANDO"
    READY = "PRONTO"

class Order(BaseModel):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True) 
    table_number = Column(Integer)
    observation = Column(String(200))
    status = Column(
        SqlEnum(OrderStatusEnum, name='order_status_enum'),
        nullable=False,
        default=OrderStatusEnum.IN_QUEUE
    )
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    def __init__(self, table_number, observation, status):
        """
        Create an order

        Arguments:
            table_number: table number of an order.
            status: status of an order.
        """
        self.table_number = table_number
        self.observation = observation
        self.status = status


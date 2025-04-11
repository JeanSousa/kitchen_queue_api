from enum import Enum
from pydantic import BaseModel, Field
from typing import List

from models import Order

class OrderStatusEnum(str, Enum):
    IN_QUEUE = "NA_FILA"
    PREPARING = "PREPARANDO"
    READY = "PRONTO"

class OrderSchema(BaseModel):
    """ Defines how a new order to be inserted should be represented
    """
    table_number: int = 1
    observation: str = "observação"
    status: OrderStatusEnum = "NA_FILA"

class OrderViewSchema(BaseModel):
    """ Defines how a new order to be returned should be represented
    """
    id: int
    table_number: int 
    observation: str 
    status: str
    created_at: str 
    updated_at: str 
    deleted_at: str

class OrderPathSchema(BaseModel):
    order_id: int = Field(..., description="ID do pedido da Url")

class OrderListViewSchema(BaseModel):
    """ Defines how an order listing will be returned.
    """
    orders: List[OrderViewSchema]

class OrderDelSchema(BaseModel):
    """ Defines how an order deleted will be returned.
    """
    message: str 
    table_number: int

def orders_presentation(orders: List[Order]):
    """ Return an order presentation defined by
        OrderViewSchema.
    """
    result = []
    for order in orders:
        result.append({
            "id": order.id,
            "table_number": order.table_number,
            "observation": order.observation,
            "status": order.status,
            "created_at": order.created_at,
            "updated_at": order.updated_at,
            "deleted_at": order.deleted_at
        })

    return {"orders": result}

def order_presentation(order: Order):
    """ Return a order list presentation defined by
        OrderViewSchema.
    """
    return {
        "id": order.id,
        "table_number": order.table_number,
        "observation": order.observation,
        "status": order.status,
        "created_at": order.created_at,
        "updated_at": order.updated_at,
        "deleted_at": order.deleted_at
    }

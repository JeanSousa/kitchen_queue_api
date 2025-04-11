from pydantic import BaseModel, Field
from typing import List

from models import OrderProduct

class OrderProductSchema(BaseModel):
    """ Defines how a new order_product to be inserted should be represented
    """
    order_id: int = 1
    product_id: int = 1
    amount: int = 1


class OrderProductPathSchema(BaseModel):
    order_product_id: int = Field(..., description="ID do pedido da Url")


class OrderProductViewSchema(BaseModel):
    """ Defines how a new order_product to be returned should be represented
    """
    id: int = 1
    order_id: int = 1
    product_id: int = 1
    amount: int = 1


class OrderProductListViewSchema(BaseModel):
    """ Defines how a order products listing will be returned.
    """
    order_products: List[OrderProductViewSchema]


def order_products_presentation(order_products: List[OrderProduct]):
    """ Return an order product presentation defined by
        OrderProductViewSchema.
    """
    result = []
    for order_product in order_products:
        result.append({
            "id": order_product.id,
            "order_id": order_product.order_id,
            "product_id": order_product.product_id,
            "amount": order_product.amount,
            "created_at": order_product.created_at,
            "updated_at": order_product.updated_at,
            "deleted_at": order_product.deleted_at
        })

    return {"order_products": result}


def order_product_presentation(order_product: OrderProduct):
    """ Return an order_product presentation defined by
        OrderProductViewSchema.
    """
    return {
        "id": order_product.id,
        "order_id": order_product.order_id,
        "product_id": order_product.product_id,
        "amount": order_product.amount,
        "created_at": order_product.created_at,
        "updated_at": order_product.updated_at,
        "deleted_at": order_product.deleted_at
    }
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
    order_product_id: int = Field(..., description="ID do vinculo do produto ao pedido da Url")


class OrderProductPathOrderIdSchema(BaseModel):
    order_id: int = Field(..., description="ID do pedido")


class OrderProductViewSchema(BaseModel):
    """ Defines how a new order_product to be returned should be represented
    """
    id: int 
    order_id: int 
    product_id: int 
    amount: int 
    created_at: str
    updated_at: str 
    deleted_at: str


class OrderProductListViewSchema(BaseModel):
    """ Defines how a order products listing will be returned.
    """
    order_products: List[OrderProductViewSchema]


class ProductInOrderSchema(BaseModel):
    """ Product within an order with quantity
    """
    product_id: int
    name: str
    value: float
    amount: int

class OrderWithProductsViewSchema(BaseModel):
    """ Define an order with your products
    """
    order_id: int
    table_number: int
    observation: str
    status: str
    created_at: str 
    updated_at: str 
    deleted_at: str
    products: List[ProductInOrderSchema]

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
    """ Return an order_products presentation defined by
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

    
def order_product_by_order_presentation(order_products: list[OrderProduct]):
    return {
        "order_id": order_products[0].order.id,
        "table_number": order_products[0].order.table_number,
        "observation": order_products[0].order.observation,
        "status": order_products[0].order.status,
        "status": order_products[0].order.created_at,
        "status": order_products[0].order.updated_at,
        "status": order_products[0].order.deleted_at,
        "products": [
            {
                "product_id": op.product.id,
                "name": op.product.name,
                "value": op.product.value,
                "amount": op.amount
            }
            for op in order_products
        ]
    }
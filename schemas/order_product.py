from pydantic import BaseModel

class OrderProductSchema(BaseModel):
    """ Defines how a new order_product to be inserted should be represented
    """
    order_id: int = 1
    product_id: int = 1
    amount: int = 1



class OrderProductViewSchema(BaseModel):
    """ Defines how a new order_product to be returned should be represented
    """
    id: int = 1
    order_id: int = 1
    product_id: int = 1
    amount: int = 1


from pydantic import BaseModel, Field
from typing import List

from models import Product

class ProductSchema(BaseModel):
    """ Defines how a new product to be inserted should be represented
    """
    name: str = "Nome do produto"
    value: float = 0

class ProductViewSchema(BaseModel):
    """ Defines how a new product to be returned should be represented
    """
    id: int
    name: str 
    value: float
    created_at: str 
    updated_at: str 
    deleted_at: str

class ProductPathSchema(BaseModel):
    product_id: int = Field(..., description="ID do produto na URL")


class ProductsListViewSchema(BaseModel):
    """ Defines how a product listing will be returned.
    """
    products: List[ProductViewSchema]

class ProductDelSchema(BaseModel):
    """ Defines how a product deleted will be returned.
    """
    message: str 
    name: str


def products_presentation(products: List[Product]):
    """ Return an product presentation defined by
        ProductViewSchema.
    """
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "value": product.value,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "deleted_at": product.deleted_at
        })

    return {"products": result}

def product_presentation(product: Product):
    """ Return an product list presentation defined by
        ProductViewSchema.
    """
    return {
        "id": product.id,
        "nome": product.name,
        "valor": product.value,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "deleted_at": product.deleted_at
    }
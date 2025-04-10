from pydantic import BaseModel, Field
from typing import List

from models import Product

class ProductSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    name: str = "Nome do produto"
    value: float = 0

class ProductViewSchema(BaseModel):
    """ Define como um novo produto a ser retornado deve ser representado
    """
    id: int
    name: str 
    value: float
    created_at: str 
    updated_at: str 
    deleted_at: str

class ProdutoPathSchema(BaseModel):
    product_id: int = Field(..., description="ID do produto na URL")


# class ProductListSchema(BaseModel):
#     products:List[Product]


def products_presentation(products: List[Product]):
    """ Retorna an product presentation defined by
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
    return {
        "id": product.id,
        "nome": product.name,
        "valor": product.value,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "deleted_at": product.deleted_at
    }
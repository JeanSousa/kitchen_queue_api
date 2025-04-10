from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    name: str = "Coca cola zero 365ml"
    value: float = 2.99

class ProductSchemaResponse(BaseModel):
    """ Define como um novo produto a ser retornado deve ser representado
    """
    name: str 
    value: float

class ProdutoPathSchema(BaseModel):
    product_id: int = Field(..., description="ID do produto na URL")


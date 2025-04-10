from pydantic import BaseModel
from server import product_tag
from . import api_blueprint 

class ProductResponse(BaseModel):
    id: int
    name: str



@api_blueprint.get('/products/<int:product_id>', tags=[product_tag], responses={"200": ProductResponse})
def get(product_id):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    return {"id": product_id, "name": "coca cola"}, 200

# @api_blueprint.get('/products')
# def get_all():
#     return { 'product': []}, 200

# @api_blueprint.post('/products')
# def create():
#     return { 'product': []}, 201

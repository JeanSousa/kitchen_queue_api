from pydantic import BaseModel, Field

from server import product_tag
from schemas import ProductSchema, ProductSchemaResponse, ProdutoPathSchema
from . import api_blueprint 


@api_blueprint.post('/produtos', tags=[product_tag], responses={"201": ProductSchemaResponse})
def add(form: ProductSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação de um produto.
    """
    return { "name": "Coca cola", "value": 2.65}, 201

@api_blueprint.get('/products/<int:product_id>', tags=[product_tag], responses={"200": ProductSchemaResponse})
def get(path: ProdutoPathSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    return {"id": path.product_id, "name": "coca cola"}, 200

# @api_blueprint.get('/products')
# def get_all():
#     return { 'product': []}, 200

# @api_blueprint.post('/products')
# def create():
#     return { 'product': []}, 201

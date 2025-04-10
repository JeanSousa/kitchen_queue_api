from pydantic import BaseModel, Field
from server import product_tag
from . import api_blueprint 

# PASSAR ESSA PARTE PARA OS SCHEMAS, TERMINAR O FLUXO DE UM POST ATE O BANCO DE DADOS
class ProductResponse(BaseModel):
    id: int
    name: str

class ProdutoPathSchema(BaseModel):
    product_id: int = Field(..., description="ID do produto na URL")



@api_blueprint.get('/products/<int:product_id>', tags=[product_tag], responses={"200": ProductResponse})
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

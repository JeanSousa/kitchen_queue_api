from sqlalchemy.exc import IntegrityError

from schemas.product import *
from schemas.error import ErrorSchema
from . import api_blueprint 
from models import Session, Product
from server import product_tag


@api_blueprint.post('/products', tags=[product_tag], 
    responses={"201": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add(form: ProductSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação de um produto.
    """
    product = Product(name=form.name, value=form.value)
    
    try:
        session = Session()
        session.add(product)
        session.commit()
        return product_presentation(product)
    except IntegrityError as e:
        # case product already exists
        errorMessage = "Produto já existe na base de dados"
        return { "message": errorMessage }, 409
    except Exception as e:
        # unknow error
        errorMessage = "Não foi possivel salvar o item, por favor tente novamente mais tarde"
        return { "message": errorMessage}, 400 
    
@api_blueprint.get('/products', tags=[product_tag], responses={"200": ProductsListViewSchema})
def get_all():
    """Busca todos os produtos da base de dados

    Retorna uma representação dos produtos.
    """
    session = Session()
    products = Product.get_all_active(session)
    return products_presentation(products)

# @api_blueprint.get('/products/<int:product_id>', tags=[product_tag], responses={"200": ProductViewSchema})
# def get(path: ProductPathSchema):
#     """Adiciona um novo Produto à base de dados

#     Retorna uma representação dos produtos e comentários associados.
#     """
#     return {"id": path.product_id, "name": "coca cola"}, 200


# @api_blueprint.post('/products')
# def create():
#     return { 'product': []}, 201

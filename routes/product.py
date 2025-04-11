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
        error_message = "Produto já existe na base de dados"
        return { "message": error_message }, 409
    
    except Exception as e:
        # unknow error
        error_message = "Não foi possivel salvar o item, por favor tente novamente mais tarde"
        return { "message": error_message}, 400 
    

@api_blueprint.get('/products', tags=[product_tag], 
    responses={"200": ProductsListViewSchema, "400": ErrorSchema})
def get_all():
    """Busca todos os produtos da base de dados

    Retorna uma representação dos produtos.
    """
    try:
        session = Session()
        products = Product.get_all_active(session)

        if not products:
            return {"produtos": []}, 200
    
        return products_presentation(products)
    
    except Exception as e:
        error_message = "Não foi possível buscar os itens, por favor tente novamente mais tarde"
        return { "message": error_message}, 400


@api_blueprint.get('/products/<int:product_id>', tags=[product_tag], 
    responses={"200": ProductViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def get_by_id(path: ProductPathSchema):
    """Busca um produto na base de dados

    Retorna uma representação de um produto.
    """
    try:
        session = Session()
        product = Product.get_by_id(session, path.product_id)

        if not product:
            error_message = "Produto não encontrado na base de dados"
            return { "message": error_message }, 404

        return product_presentation(product), 200
    except Exception as e: 
        error_message = "Não foi possível buscar o item, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.put('/products/<int:product_id>', tags=[product_tag],
    responses={"200": ProductViewSchema, "401": ErrorSchema, "400": ErrorSchema})
def update_by_id(path: ProductPathSchema, form: ProductSchema):
    """Atualiza um produto na base de dados

    Retorna uma representação de um produto.
    """
    try:
        session = Session()
        product = Product.get_by_id(session, path.product_id)

        if not product:
            error_message = "Produto não encontrado na base de dados"
            return { "message": error_message }, 404
        
        product.name = form.name 
        product.value = form.value 
        session.commit()
    except Exception as e:
        error_message = "Não foi possível atualizar o item, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    
    return product_presentation(product), 200


@api_blueprint.delete('/products/<int:product_id>', tags=[product_tag],
    responses={"200": ProductDelSchema, "401": ErrorSchema, "400": ErrorSchema})
def delete_by_id(path: ProductPathSchema):
    """Deleta um produto na base de dados

    Retorna o nome do produto deletado.
    """
    try:
        session = Session()
        product = Product.get_by_id(session, path.product_id)

        if not product:
            error_message = "Produto não encontrado na base de dados"
            return { "message": error_message }, 404

        product.soft_delete()
        session.commit()
        return { "message" : "Produto deletado com sucesso", "name": product.name }, 200  
    except Exception as e:
        error_message = "Não foi possível deletar o item, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
        


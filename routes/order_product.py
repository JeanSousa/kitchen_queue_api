from schemas.order_product import *
from schemas.error import ErrorSchema
from . import api_blueprint 
from models import Session, OrderProduct
from server import order_products_tag 


@api_blueprint.post('/order-products', tags=[order_products_tag],
    responses={"201": OrderProductViewSchema, "400": ErrorSchema})
def add_order_product(form: OrderProductSchema): 
    """Vincula um produto a um pedido

    Retorna uma representação de um pedido.
    """
    order_products = OrderProduct(
        order_id=form.order_id, 
        product_id=form.product_id,
        amount = form.amount
    )

    try:
        session = Session()
        session.add(order_products)
        session.commit()
        return order_product_presentation(order_products), 201
    except Exception as e:
        # unknow error
        error_message = "Não foi possivel salvar os produtos, por favor tente novamente mais tarde"
        return { "message": error_message}, 400 
    

@api_blueprint.get('/order-products', tags=[order_products_tag], 
    responses={"200": OrderProductListViewSchema, "400": ErrorSchema})
def get_all_orders_products():
    """Busca todos os vinculos de pedidos e produtos

    Retorna uma representação dos vinculos de pedidos e produtos.
    """
    try:
        session = Session()
        order_products = OrderProduct.get_all_active(session)

        if not order_products:
            return {"order_products": []}, 200
    
        return order_products_presentation(order_products), 200
    
    except Exception as e:
        # unknow error
        error_message = "Não foi possível buscar os pedidos, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.get('/order-products/<int:order_product_id>', tags=[order_products_tag], 
    responses={"200": OrderProductViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def get_order_product_by_id(path: OrderProductPathSchema):
    """Busca um vinculo de um produto ao pedido na base de dados

    Retorna uma representação de um vinculo de um produto ao pedido.
    """
    try:
        session = Session()
        order_product = OrderProduct.get_by_id(session, path.order_product_id)

        if not order_product:
            error_message = "Pedido não encontrado na base de dados"
            return { "message": error_message }, 404

        return order_product_presentation(order_product), 200
    except Exception as e: 
        error_message = "Não foi possível buscar o pedido, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.put('/order-products/<int:order_product_id>', tags=[order_products_tag],
    responses={"200": OrderProductViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_order_product_by_id(path: OrderProductPathSchema, form: OrderProductSchema):
    """Atualiza o vinculo de um produto ao pedido na base de dados

    Retorna uma representação de um vinculo de um produto ao pedido.
    """
    try:
        session = Session()
        order_product = OrderProduct.get_by_id(session, path.order_product_id)

        if not order_product:
            error_message = "Vinculo não encontrado na base de dados"
            return { "message": error_message }, 404
        
        order_product.order_id = form.order_id 
        order_product.product_id = form.product_id 
        order_product.amount = form.amount

        session.commit()
        return order_product_presentation(order_product), 200
    except Exception as e:
        error_message = "Não foi possível atualizar o vinculo, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.delete('/orders-products/<int:order_product_id>', tags=[order_products_tag],
    responses={"200": {}, "404": ErrorSchema, "400": ErrorSchema})
def delete_order_product_by_id(path: OrderProductPathSchema):
    """Deleta o vinculo de um produto ao pedido na base de dados

    Retorna o id de um vinculo.
    """
    try:
        session = Session()
        order_product = OrderProduct.get_by_id(session, path.order_product_id)

        if not order_product:
            error_message = "Vinculo não encontrado na base de dados"
            return { "message": error_message }, 404

        order_product.soft_delete()
        session.commit()
        return { "message" : "Vinculo deletado com sucesso", "order_product_id": order_product.id }, 200  
    except Exception as e:
        error_message = "Não foi possível deletar o pedido, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.get('/order-products/products/<int:order_id>', tags=[order_products_tag])
def get_products_by_order_id(path: OrderProductPathOrderIdSchema):
    """Busca os produtos de um pedido

    Retorno sem conteudo.
    """
    # PAREI AQUI IMPLEMENTANDO A BUSCA DE PRODUTOS PELO ID DO PEDIDO
    session = Session()
    order_products = session.query(OrderProduct).filter_by(order_id=path.order_id,deleted_at=None).all() 

    # ISSO TO USANDO PRA PRINTAR POQUE A CLASSE NÃO POSSUI UM METODO __repr__ OU __str__ NA MODEL
    # VERIFICAR POQUE QUANDO USO O METODO DE PRESENTATION DA CERTO
    for op in order_products:
        print(op.__dict__)

    return {}
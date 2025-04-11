from schemas.order_product import *
from schemas.error import ErrorSchema
from . import api_blueprint 
from models import Session, OrderProduct
from server import order_products_tag 


@api_blueprint.post('/order-products', tags=[order_products_tag],
    responses={"200": OrderProductViewSchema, "400": ErrorSchema})
def add_order_product(form: OrderProductSchema): 
    """Adiciona um novo pedido à base de dados

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
    """Busca todos os produtos do pedido da base de dados

    Retorna uma representação dos produtos de um pedido.
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
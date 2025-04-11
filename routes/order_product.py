from schemas.order_product import *
from schemas.error import ErrorSchema
from . import api_blueprint 
from models import Session, OrderProduct
from server import orders_products_tag 


@api_blueprint.post('/orders-products', tags=[orders_products_tag],
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
        return {}, 201
    except Exception as e:
        # unknow error
        error_message = "Não foi possivel salvar os produtos, por favor tente novamente mais tarde"
        return { "message": error_message}, 400 
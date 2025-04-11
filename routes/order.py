from schemas.order import *
from schemas.error import ErrorSchema
from . import api_blueprint 
from models import Session, Order
from server import order_tag

@api_blueprint.post('/orders', tags=[order_tag],
    responses={"200": OrderViewSchema, "400": ErrorSchema})
def add_order(form: OrderSchema):
    """Adiciona um novo pedido à base de dados

    Retorna uma representação de um pedido.
    """
    order = Order(
        table_number=form.table_number, 
        observation=form.observation,
        status = form.status
    )

    try:
        session = Session()
        session.add(order)
        session.commit()
        return order_presentation(order), 200
    except Exception as e:
        # unknow error
        error_message = "Não foi possivel salvar o pedido, por favor tente novamente mais tarde"
        return { "message": error_message}, 400 

@api_blueprint.get('/orders', tags=[order_tag], responses={"400": ErrorSchema})
def get_all_orders():
    """Busca todos os pedidos da base de dados

    Retorna uma representação dos pedidos.
    """
    try:
        session = Session()
        orders = Order.get_all_active(session)

        if not orders:
            return {"orders": []}, 200
    
        return orders_presentation(orders), 200
    
    except Exception as e:
        # unknow error
        error_message = "Não foi possível buscar os pedidos, por favor tente novamente mais tarde"
        return { "message": error_message}, 400

@api_blueprint.get('/orders/<int:order_id>', tags=[order_tag], 
    responses={"200": OrderViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def get_order_by_id(path: OrderPathSchema):
    """Busca um pedido na base de dados

    Retorna uma representação de um pedido.
    """
    try:
        session = Session()
        order = Order.get_by_id(session, path.order_id)

        if not order:
            error_message = "Pedido não encontrado na base de dados"
            return { "message": error_message }, 404

        return order_presentation(order), 200
    except Exception as e: 
        error_message = "Não foi possível buscar o pedido, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.put('/orders/<int:order_id>', tags=[order_tag],
    responses={"200": OrderViewSchema, "401": ErrorSchema, "400": ErrorSchema})
def update_order_by_id(path: OrderPathSchema, form: OrderSchema):
    """Atualiza um pedido na base de dados

    Retorna uma representação de um pedido.
    """
    try:
        session = Session()
        order = Order.get_by_id(session, path.order_id)

        if not order:
            error_message = "Pedido não encontrado na base de dados"
            return { "message": error_message }, 404
        
        order.table_number = form.table_number 
        order.observation = form.observation 
        order.status = form.status

        session.commit()
        return order_presentation(order), 200
    except Exception as e:
        error_message = "Não foi possível atualizar o pedido, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
    

@api_blueprint.delete('/orders/<int:order_id>', tags=[order_tag],
    responses={"200": OrderDelSchema, "401": ErrorSchema, "400": ErrorSchema})
def delete_order_by_id(path: OrderPathSchema):
    """Deleta um pedido na base de dados

    Retorna o nome do pedido deletado.
    """
    try:
        session = Session()
        order = Order.get_by_id(session, path.order_id)

        if not order:
            error_message = "Pedido não encontrado na base de dados"
            return { "message": error_message }, 404

        order.soft_delete()
        session.commit()
        return { "message" : "Pedido deletado com sucesso", "table_number": order.table_number }, 200  
    except Exception as e:
        print(e)
        error_message = "Não foi possível deletar o pedido, por favor tente novamente mais tarde"
        return { "message": error_message}, 400
from sqlalchemy.exc import IntegrityError

from schemas.error import ErrorSchema
from . import api_blueprint 
from models import Session, Order
from server import order_tag

@api_blueprint.post('/orders', tags=[order_tag])
def add_order():
    return {}, 200
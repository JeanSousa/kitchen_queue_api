from enum import Enum
from pydantic import BaseModel, Field
from typing import List

from models import Order

class OrderStatusEnum(str, Enum):
    IN_QUEUE = "NA_FILA"
    PREPARING = "PREPARANDO"
    READY = "PRONTO"

class OrderSchema(BaseModel):
    """ Defines how a new order to be inserted should be represented
    """
    table_number: int = 1
    observation: str = "observação"
    status: OrderStatusEnum = "NA_FILA"



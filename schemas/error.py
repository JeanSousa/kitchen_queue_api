from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """ Defines how an error should be represented
    """
    message: str

# as_declarative transform BaseModel in declarative base from sqlalchemy, 
# declarative_attr allow define atributes like __tablename__
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from sqlalchemy import Column, DateTime
from datetime import datetime


# Override declarative base
@as_declarative()
class BaseModel:
    """Base class for all SQLAlchemy models.

    This class defines common attributes such as:
    - `created_at`: timestamp for when the record was created
    - `updated_at`: timestamp for the last update
    - `deleted_at`: timestamp for soft deletion

    It also provides utility methods like:
    - `soft_delete()`: performs a soft delete on the record
    - `get_all_active()`: retrieves all records that are not soft-deleted
    """
    id: int 

    #define default value to tablename
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()

    @classmethod
    def get_all_active(cls, session):
        return session.query(cls).filter(cls.deleted_at == None).all()
    

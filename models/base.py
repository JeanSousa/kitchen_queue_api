# as_declarative transform BaseModel in declarative base from sqlalchemy, 
# declarative_attr allow define atributes like __tablename__
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from sqlalchemy.inspection import inspect
from datetime import datetime


@as_declarative()
class BaseModel:
    """Base class for all SQLAlchemy models.

    This class override declarative base class and provides utility methods like:
    - `soft_delete()`: performs a soft delete on the record
    - `get_all_active()`: retrieves all records that are not soft-deleted
    """
    id: int 

    @declared_attr
    def __tablename__(cls):
        """Define default value to tablename."""
        return cls.__name__.lower()

    def soft_delete(self):
        """Set soft delete timestamp manually on child class."""
        if hasattr(self, "deleted_at"):
            self.deleted_at = datetime.now()

    @classmethod
    def get_all_active(cls, session):
        """Return all records that are not soft-deleted."""
        if hasattr(cls, "deleted_at"):
            return session.query(cls).filter(cls.deleted_at == None).all()
        return session.query(cls).all()

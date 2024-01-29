"""Base clase declaration"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):

    def __init__(self):
        """initialize base class"""
        date = datetime.now()
        id = uuid4()


base = Base()
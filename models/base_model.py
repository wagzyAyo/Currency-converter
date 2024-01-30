"""Base clase declaration"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from dotenv import load_dotenv
import os
import requests

base = declarative_base
load_dotenv()
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

class Base(base):
    __tablename__ = 'currency_data'



    def __init__(self):
        """initialize base class"""
        self.date = datetime.now()
        self.id = uuid4()
        endpoint = os.getenv('endpoint')
        self.data = requests.get(endpoint).json()

base = Base()
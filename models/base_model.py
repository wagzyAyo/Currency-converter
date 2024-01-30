"""Base clase declaration"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
import requests
import json

base = declarative_base()
load_dotenv()
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

class CurrencyData(base):
    __tablename__ = 'currency_data'
    id = Column(String, primary_key=True, default=str(uuid4()))
    date = Column(DateTime, default=datetime.now())
    endpoint = os.getenv('endpoint')
    data = Column(String, default=json.dumps(requests.get(endpoint).json()))


# Create tables in the database
base.metadata.create_all(engine)

# Create a session to interact with the database
session = Session(engine)

# Create an instance of CurrencyData
currency_instance = CurrencyData()

# Add the instance to the session and commit changes
session.add(currency_instance)
session.commit()
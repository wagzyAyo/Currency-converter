from pymongo import MongoClient
import requests
from dotenv import load_dotenv
import os

def get_database():
    load_dotenv()
    endpoint = os.getenv('endpoint')

    client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

    data_collection = client.data_collection

    currency_data = data_collection.currency_data

    result = requests.get(endpoint).json()
    currency_data.insert_one(result)

    for data in currency_data.find():
        print(data)


get_database()
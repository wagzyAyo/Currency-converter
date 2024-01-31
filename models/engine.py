from pymongo import MongoClient
import requests
from dotenv import load_dotenv
import os

def get_database():
    load_dotenv()
    try:
        endpoint = os.getenv('endpoint')

        client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

        data_collection = client.data_collection

        currency_data = data_collection.currency_data

        result = requests.get(endpoint).json()
        currency_data.insert_one(result)
    except Exception as e:
        try:
            endpoint2 = os.getenv('endpoint2')
            result = requests.get(endpoint2).json()
            currency_data.insert_one(result)
        except Exception as e:
            return
    finally:
        for data in currency_data.find():
            print(data)
        client.close()


get_database()
from dotenv import load_dotenv
import requests
from pymongo import MongoClient
import os
import schedule
import time

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

data_collection = client.data_collection

currency_data = data_collection.currency_data

def get_database():
    load_dotenv()
    try:
        endpoint = os.getenv('endpoint')

        result = requests.get(endpoint)
        if result.status_code != 200:
            endpoint = os.getenv('endpoint2')
            result = requests.get(endpoint)
        result = result.json()
        currency_data.insert_one(result)
    except Exception as e:
        return
    finally:
        #for data in currency_data.find():
        #    print(data)
        #for data in currency_data.find():
        #    print(data)
        client.close()

schedule.every().day.at("04:00").do(get_database)

schedule.every().day.at("12:00").do(get_database)

schedule.every().day.at("21:00").do(get_database)

while True:
    schedule.run_pending()
    time.sleep(1)
    
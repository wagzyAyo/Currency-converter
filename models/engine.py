from dotenv import load_dotenv
import requests
from pymongo import MongoClient
import os
import schedule
import time
from pytz import timezone
from datetime import datetime


load_dotenv()
uri = os.getenv('uri')
client = MongoClient(uri)

def connect_db():
   
    data_collection = client.data_collection

    currency_data = data_collection.currency_data
    return currency_data

currency_data = connect_db()

def convert_to_wat(time_str, time_zone):
    """Convert a spcified 
    time zone to west Africa
    (WAT) time
    """
    source_tz= timezone(time_zone)
    local_time = source_tz.localize(datetime.strptime(time_str, '%H:%M'))
    wat_time = local_time.astimezone(timezone('Africa/Lagos'))
    return wat_time

def get_database():
    """Get data from external 
    API and insert to database
    """
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

wat_4 = convert_to_wat('13:39', 'Africa/Lagos')
schedule.every().day.at(str(wat_4.strftime('%H:%M'))).do(get_database)

wat_12 = convert_to_wat('12:00', 'Africa/Lagos')
schedule.every().day.at(str(wat_12.strftime('%H:%M'))).do(get_database)

wat_21 = convert_to_wat('21:00', 'Africa/Lagos')
schedule.every().day.at(str(wat_21.strftime('%H:%M'))).do(get_database)

while True:
    schedule.run_pending()
    time.sleep(1)
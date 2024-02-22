from decimal import Decimal
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import schedule
from pytz import timezone
import requests
import time
from datetime import datetime


load_dotenv()


uri = os.getenv('uri')
client = MongoClient(uri)
def connect_db():
    '''connects to db'''
    data_collection = client.data_collection

    currency_data = data_collection.currency_data
    return currency_data

def data():
    """Get the last data in database"""
    all_data = connect_db()
    return  all_data.find_one({}, sort=[('_id', -1)])

def get_recent_data():
    """Get recent data on schedule from database"""
    while True:
        latest_data = data()
        time.sleep(60)
        return latest_data

response = get_recent_data()

#Convert currency
def convert(from_c, to_c, amount):
   '''Handle currency conversion rates'''
   if from_c in response['rates'] and to_c in response['rates']:
      if amount > 0:
         rate_from = Decimal(response['rates'][from_c])
         rate_to = Decimal(response['rates'][to_c])
         
         convert_amount = (Decimal(amount) / rate_from) * rate_to
         convert_amount = round(convert_amount, 2)
         return convert_amount
      raise ZeroDivisionError("value must be greater than 0")
   
   raise KeyError("Invalid currency")



#calculate unit
def unit_per(from_c, to_c, amount, result):
   '''Calculates the unites per conversion'''
   if amount > 0:
      rate_from = Decimal(response['rates'][from_c])
      rate_to = Decimal(response['rates'][to_c])
      unit_to = round(result / int(amount), 4)
      if unit_to > 0:
         unit_to = round(unit_to, 2)
      return f'1{from_c} = {unit_to}{to_c}'
   raise ZeroDivisionError("Value must be greater than 0")



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
        print(result)
        currency_data.insert_one(result)
    except Exception as e:
        return
    finally:
        print(result)

def run_db():
    wat_4 = convert_to_wat('04:00', 'Africa/Lagos')
    schedule.every().day.at(str(wat_4.strftime('%H:%M'))).do(get_database)

    wat_12 = convert_to_wat('12:00', 'Africa/Lagos')
    schedule.every().day.at(str(wat_12.strftime('%H:%M'))).do(get_database)

    wat_21 = convert_to_wat('21:00', 'Africa/Lagos')
    schedule.every().day.at(str(wat_21.strftime('%H:%M'))).do(get_database)

    while True:
        schedule.run_pending()
        time.sleep(1)
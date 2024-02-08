from decimal import Decimal
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
endpoint = os.getenv('endpoint2')

uri = os.getenv('uri')
client = MongoClient(uri)
def connect_db():
    '''connects to db'''
    data_collection = client.data_collection

    currency_data = data_collection.currency_data
    return currency_data

all_data = connect_db()
response = all_data.find_one({}, sort=[('timestamp', -1)])
#print(response)

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
   
   raise ValueError("Invalid currency")



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
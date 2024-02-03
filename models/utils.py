from decimal import Decimal
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import ssl

load_dotenv()
#endpoint = os.getenv('endpoint')
password = os.getenv('db_password')

uri = os.getenv('uri')
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
client = MongoClient(uri, ssl=True, ssl_context=ssl_context)

data_collection = client.data_collection

currency_data = data_collection.currency_data

#response = requests.get(endpoint).json()
response = currency_data.find_one({}, sort=[('timestamp', -1)])
print(response)

#Convert currency
def convert(from_c, to_c, amount):
   '''Handle currency conversion rates'''
   try:
      if from_c in response['rates'] and to_c in response['rates']:
         rate_from = Decimal(response['rates'][from_c])
         rate_to = Decimal(response['rates'][to_c])
         
         convert_amount = (Decimal(amount) / rate_from) * rate_to
         convert_amount = round(convert_amount, 2)
         
         return convert_amount
      else:
         return('Invalid conversion')
   except Exception as e:
      return f'Error: {str(e)}'
   

#TEST   
#from_conv = input("Convert from : ").upper()
#to_conv = input('Convert to : ').upper()
#amount = input("Amount to convert : ").upper()
# test
#result = convert(from_conv,to_conv,amount)
#print(f'The conversion is {result}')



#calculate unit
def unit_per(from_c, to_c, amount, result):
   '''Calculates the unites per conversion'''
   rate_from = Decimal(response['rates'][from_c])
   rate_to = Decimal(response['rates'][to_c])
   unit_to = round(result / int(amount), 4)
   if unit_to > 0:
      unit_to = round(unit_to, 2)
   return f'1{from_c} = {unit_to}{to_c}'
   
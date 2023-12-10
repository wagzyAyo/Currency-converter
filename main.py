from flask import Flask, render_template
import requests
import os
from decimal import Decimal
from dotenv import load_dotenv
from datetime import datetime


app = Flask(__name__)
load_dotenv()






endpoint = os.getenv('endpoint')

response = requests.get(endpoint).json()
print(response)

def convert(from_c, to_c, amount):
   '''Handle currency conversion rates'''
   try:
    
    if from_c in response['rates'] and to_c in response['rates']:
        #rate = response['rates'][to_c]
        #converted_amount = rate * int(amount)
        #converted_amount = round(converted_amount, 2)
        #return converted_amount
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
   
from_conv = input("Convert from : ").upper()
to_conv = input('Convert to : ').upper()
amount = input("Amount to convert : ").upper()
# test
result = convert(from_conv,to_conv,amount)
print(f'The conversion is {result}')


## Get current year
year = datetime.now().year
print(year)


def unit_per(from_c, to_c, amount):
   '''Calculates the unites per conversion'''
   rate_from = Decimal(response['rates'][from_c])
   rate_to = Decimal(response['rates'][to_c])
   unit_to = round(result / int(amount), 4)
   return f'Rate: 1{from_c} = {unit_to}{to_c}'
   

unit_result = unit_per(from_conv, to_conv, amount)
print(unit_result)

@app.route('/')
def home():
    return render_template('index.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)

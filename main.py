from flask import Flask, render_template
import requests
import os
from decimal import Decimal
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()






endpoint = os.getenv('endpoint')



def convert(from_c, to_c, amount):
   '''Handle currency conversion rates'''
   try:
    response = requests.get(endpoint).json()
    print(response)
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
   

result = convert(from_c = input("Convert from : ").upper(),
   to_c = input('Convert to : ').upper(),
   amount = input("Amount to convert : ").upper())
print(f'The conversion is {result}')



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

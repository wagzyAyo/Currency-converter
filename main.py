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
        from_rate = Decimal(response['rates'][from_c])
        to_rate = Decimal(response['rates'][to_c])
        print(from_rate)
        print(to_rate)
        
        convert_amount = round((Decimal(amount) ) * to_rate / from_rate, 2)
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

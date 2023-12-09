from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()






endpoint = os.getenv('endpoint')



def convert(from_c, to_c, amount):
   '''Handle currency conversion rates'''
   try:
    response = requests.get(endpoint).json()
    print(response)
    if from_c == response['base']:
        rate = response['rates'][to_c]
        converted_amount = rate * int(amount)
        return converted_amount
    else:
        return('Invalid conversion')
   except Exception as e:
      return f'Error: {str(e)}'
   

result = convert(from_c = input("Convert from : ").upper(),
   to_c = input('Convert to : ').upper(),
   amount = input("Amount to convert : ").upper())
print(result)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

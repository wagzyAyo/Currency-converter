from flask import Flask, render_template
import os
from decimal import Decimal
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,SelectField
from wtforms.validators import DataRequired
from models.currency_list import currency_list
from models.img import currency_map, get_img_url
from api.convert import Bp
from api.hello import simple_dict
from models.utils import convert, unit_per

#print(currency_list)

app = Flask(__name__)
app.secret_key = os.getenv('token')
app.register_blueprint(Bp, url_prefix='/api/convert')
app.register_blueprint(simple_dict, url_prefix='/api/hello')


#class form
class Form(FlaskForm):
   #country_image1 = StringField(render_kw={'readonly': True})
   select= SelectField(validators=[DataRequired()], choices=[(currency_code, currency_code) for currency_code in currency_list])
   amount = FloatField(validators=[DataRequired()], render_kw={'class': 'small_input'})
   #country_image2 = StringField(render_kw={'readonly': True})
   convert_to = SelectField(validators=[DataRequired()], choices=[(currency_code, currency_code) for currency_code in currency_list])
   converted_amount = StringField(render_kw={'readonly' : True, 'class': 'small_input'})




#endpoint = os.getenv('endpoint')

#response = requests.get(endpoint).json()
#print(response)


#Convert currency
#def convert(from_c, to_c, amount):
   '''Handle currency conversion rates'''
  # try:
  #    if from_c in response['rates'] and to_c in response['rates']:
  #       rate_from = Decimal(response['rates'][from_c])
   #      rate_to = Decimal(response['rates'][to_c])
         
   #      convert_amount = (Decimal(amount) / rate_from) * rate_to
    #     convert_amount = round(convert_amount, 2)
         
   #      return convert_amount
   #   else:
   #      return('Invalid conversion')
   #except Exception as e:
   #   return f'Error: {str(e)}'
   

#TEST   
#from_conv = input("Convert from : ").upper()
#to_conv = input('Convert to : ').upper()
#amount = input("Amount to convert : ").upper()
# test
#result = convert(from_conv,to_conv,amount)
#print(f'The conversion is {result}')


## Get current year
year = datetime.now().year
#print(year)

#calculate unit
#def unit_per(from_c, to_c, amount, result):
#   '''Calculates the unites per conversion'''
#  rate_from = Decimal(response['rates'][from_c])
#   rate_to = Decimal(response['rates'][to_c])
#   unit_to = round(result / int(amount), 4)
#   if unit_to > 0:
#      unit_to = round(unit_to, 2)
#   return f'1{from_c} = {unit_to}{to_c}'
   

#unit_result = unit_per(from_conv, to_conv, amount)
#print(unit_result)

#   App routes


#Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()

    if form.validate_on_submit():
       convert_from = form.select.data
       amount_from = form.amount.data
       convert_to = form.convert_to.data
       #Set country image base on selected country image code
       #form.country_image1.data = get_img_url(convert_from)
       #form.country_image2.data = get_img_url(convert_to)

       converted_amont = convert(convert_from, convert_to, amount_from)
       unit = unit_per(convert_from, convert_to, amount_from, converted_amont)

       form.converted_amount.data = converted_amont
       return render_template('index.html', year=year, 
                           form=form, convert_from=convert_from, convert_to=convert_to ,
                           amount_from=amount_from, unit=unit, converted_amount=converted_amont)
    
    return render_template('index.html', year=year, 
                           form=form)


#about route
@app.route('/about')
def about():
   return render_template('about.html')


#privacy route
@app.route('/privacypolicy')
def privacypolicy():
   return render_template('privacy.html')


if __name__ == '__main__':
    app.run(debug=True)

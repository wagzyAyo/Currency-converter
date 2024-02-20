# Currency-converter
Welcome to the Currency Converter App repository! This project aims to provide users with a convenient and efficient solution for currency conversion needs, leveraging the power of Flask as the backend web framework and React Native for mobile app development.

<b> Features:</b>
<br>
 Real-time Exchange Rates: 
 Stay updated with the latest exchange rates from around the world, ensuring accurate and reliable currency conversions.

 Intuitive Interface: 
 Experience a sleek and intuitive user interface designed for effortless navigation and enhanced usability across devices.

 API for Developers: 
 Provide developers with access to currency conversion data through our API, allowing them to integrate real-time exchange rates into their applications and services 
 seamlessly.

#Usage 
<b>With API</b>


``` bash
http://currencyconverter.com.ng/api/convert/{CurrencyToConvert}/{currencyConvertingTO}/{amount}
```
in this example lets use 
CurrencyToConvert as USD(United state dollars)
CurrencyConvertingTo as NGN(Nigerian naira)
Amount as 100

Example response 

``` json
{
"Unit_per1": "1USD = 1500.50NGN",
"amount_to_convert": 100,
"convert_from": "USD",
"convert_to": "NGN",
"converted_amount": "150049.76"
}
```



# Helpful Resources:

https://flask.palletsprojects.com/en/3.0.x/<br>
https://reactnative.dev/docs/getting-started<br>
https://github.com/facebook/react-native<br>
https://www.mongodb.com/languages/python<br>
https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb<br>
https://docs.python.org/3/library/unittest.html


# Currency converter mobile App repo

https://github.com/wagzyAyo/currency_converter_app

# Link to website
www.currencyconverter.com.ng

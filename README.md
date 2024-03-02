# Currency-converter

![alt text](C-1.png)

<video controls src="converter.mp4" title="Title"></video>

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



# Usage 

<b>With API</b>


``` bash
http://currencyconverter.com.ng/api/convert/{CurrencyToConvert}/{currencyConvertingTO}/{amount}
```
in this example lets use 
CurrencyToConvert as USD(United state dollars)
CurrencyConvertingTo as NGN(Nigerian naira)
Amount as 100

<b>Example response </b>

``` json
{
"Unit_per1": "1USD = 1500.50NGN",
"amount_to_convert": 100,
"convert_from": "USD",
"convert_to": "NGN",
"converted_amount": "150049.76"
}
```

<b>Get recent rate</b>

``` bash
http://currencyconverter.com.ng/api/currencybase

```

<b>Example response</b>

``` json
{
"_id": "65e1c35384cd7f622bab26f1",
"base": "EUR",
"date": "2024-03-01",
"rates": {
"AED": 3.973414,
"AFN": 78.940206,
"ALL": 103.978253,
"AMD": 439.975444,
"ANG": 1.952192,
"AOA": 900.077589,
"ARS": 911.143659,
"AUD": 1.662817,
"AWG": 1.947283,
"AZN": 1.841479,
"BAM": 1.955237,
"BBD": 2.187143,
"BDT": 118.875797,
"BGN": 1.957117,
"BHD": 0.40782,
"BIF": 3095.138079,
"BMD": 1.081824,
"BND": 1.457094,
"BOB": 7.484881,
"BRL": 5.375471,
"BSD": 1.083273,
"BTC": 0.000017478151,
"BTN": 89.79158,
"BWP": 14.940875,
"BYN": 3.544459,
"BYR": 21203.745274,
"BZD": 2.183443,
"CAD": 1.468609,
"CDF": 2991.242534,
"CHF": 0.957391,
"CLF": 0.03782,
"CLP": 1043.570156,
"CNY": 7.787617,
"COP": 4249.436099,
"CRC": 554.58401,
"CUC": 1.081824,
"CUP": 28.668329,
"CVE": 110.233793,
"CZK": 25.322272,
"DJF": 192.899655,
"DKK": 7.454323,
"DOP": 63.566705,
"DZD": 145.823395,
"EGP": 33.428892,
"ERN": 16.227356,
"ETB": 61.146311,
"EUR": 1,
"FJD": 2.43221,
"FKP": 0.856377,
"GBP": 0.85569,
"GEL": 2.866843,
"GGP": 0.856377,
"GHS": 13.702121,
"GIP": 0.856377,
"GMD": 73.536986,
"GNF": 9308.665902,
"GTQ": 8.453607,
"GYD": 226.605848,
"HKD": 8.469144,
"HNL": 26.750405,
"HRK": 7.605324,
"HTG": 143.610008,
"HUF": 393.610431,
"IDR": 17020.332877,
"ILS": 3.850373,
"IMP": 0.856377,
"INR": 89.657386,
"IQD": 1417.792074,
"IRR": 45469.051573,
"ISK": 149.496908,
"JEP": 0.856377,
"JMD": 168.974659,
"JOD": 0.767001,
"JPY": 162.701908,
"KES": 158.483633,
"KGS": 96.714828,
"KHR": 4408.772264,
"KMF": 492.933043,
"KPW": 973.545967,
"KRW": 1443.975414,
"KWD": 0.332942,
"KYD": 0.90264,
"KZT": 488.729383,
"LAK": 22613.270474,
"LBP": 97002.712053,
"LKR": 335.463481,
"LRD": 207.281234,
"LSL": 20.759978,
"LTL": 3.194345,
"LVL": 0.654384,
"LYD": 5.232906,
"MAD": 10.946001,
"MDL": 19.259972,
"MGA": 4892.976642,
"MKD": 61.66711,
"MMK": 2274.724245,
"MNT": 3671.954864,
"MOP": 8.731488,
"MRU": 43.166465,
"MUR": 49.536508,
"MVR": 16.657817,
"MWK": 1823.518614,
"MXN": 18.421724,
"MYR": 5.13437,
"MZN": 68.693778,
"NAD": 20.759978,
"NGN": 1749.903814,
"NIO": 39.868529,
"NOK": 11.424529,
"NPR": 143.67695,
"NZD": 1.77457,
"OMR": 0.41644,
"PAB": 1.083093,
"PEN": 4.112379,
"PGK": 4.130964,
"PHP": 60.634071,
"PKR": 299.652228,
"PLN": 4.314545,
"PYG": 7906.346401,
"QAR": 3.938377,
"RON": 4.969247,
"RSD": 117.189642,
"RUB": 98.987948,
"RWF": 1382.410871,
"SAR": 4.05722,
"SBD": 9.184225,
"SCR": 14.690983,
"SDG": 650.176251,
"SEK": 11.182071,
"SGD": 1.456389,
"SHP": 1.365208,
"SLE": 24.552142,
"SLL": 21366.018979,
"SOS": 618.271294,
"SRD": 38.195413,
"STD": 22391.567193,
"SVC": 9.477273,
"SYP": 14064.941066,
"SZL": 20.834642,
"THB": 38.82503,
"TJS": 11.871239,
"TMT": 3.786383,
"TND": 3.381785,
"TOP": 2.567114,
"TRY": 33.90355,
"TTD": 7.350885,
"TWD": 34.225983,
"TZS": 2758.650237,
"UAH": 41.187386,
"UGX": 4253.795761,
"USD": 1.081824,
"UYU": 42.427989,
"UZS": 13536.167945,
"VEF": 3900232.941461,
"VES": 38.973284,
"VND": 26672.364272,
"VUV": 130.3526,
"WST": 2.980038,
"XAF": 655.819836,
"XAG": 0.047618,
"XAU": 0.000526,
"XCD": 2.923683,
"XDR": 0.816229,
"XOF": 655.819836,
"XPF": 119.331742,
"YER": 270.780189,
"ZAR": 20.734771,
"ZMK": 9737.711957,
"ZMW": 25.536659,
"ZWL": 348.346802
},
"success": true,
"timestamp": 1709294403
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

# Link to website app
www.currencyconverter.com.ng

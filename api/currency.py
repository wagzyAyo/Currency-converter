from flask import Blueprint, jsonify
from models.country_code import countries_and_currency_codes

simple_dict = Blueprint('simple_dict', __name__)

@simple_dict.route('/')
def get_currency_code():
    return jsonify(countries_and_currency_codes)
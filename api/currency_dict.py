from flask import Blueprint, jsonify
from models.utils import response

currency_data = Blueprint('currency_data', __name__)

@currency_data.route('/')
def indxex():
    response['_id'] = str(response['_id'])
    return jsonify(response)
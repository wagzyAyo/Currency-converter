from flask import Blueprint, jsonify
from models.utils import convert, unit_per
from decimal import Decimal

Bp = Blueprint('Bp', __name__)

@Bp.route('/<convert_from>/<convert_to>/<int:amount>')
def convert_api(convert_from, convert_to, amount):
    convert_from = convert_from
    convert_to = convert_to
    amount = int(amount)
    convert_result = convert(convert_from, convert_to, amount)
    unit_result = unit_per(convert_from, convert_to, amount, convert_result)
    return jsonify({'convert_from': convert_from,
             'convert_to': convert_to,
             'amount_to_convert': amount,
             'converted_amount': Decimal(convert_result),
             'Unit_per1': unit_result
             })
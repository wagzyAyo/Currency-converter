from flask import Blueprint
from main import convert, unit_per

Bp = Blueprint('Bp', __name__, url_prefix="/api/convert")

@Bp.route('/')
def convert(convert_from, convert_to, amount):
    convert_from = int(convert_from)
    convert_to = int(convert_to)
    amount = int(amount)
    convert_result = convert(convert_from, convert_to, amount)
    unit_result = unit_per(convert_from, convert_to, amount)
    return ({'convert_from': convert_from,
             'convert_to': convert_to,
             'amount_to_convert': amount,
             'converted_amount': convert_result,
             'Unit_per1': unit_result
             })

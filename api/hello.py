from flask import Blueprint

simple_dict = Blueprint('simple_dict', __name__)

@simple_dict.route('/')
def say_hello():
    return {'say': 'Hello world'}
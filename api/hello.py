from flask import Blueprint
import json

simple_dict = Blueprint('simple_dict', __name__)

@simple_dict.route('/')
def say_hello():
    return json.dumps({'say': 'Hello world'})
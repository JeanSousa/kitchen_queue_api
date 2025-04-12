from flask import redirect

from . import api_blueprint 

@api_blueprint.route('/', methods=['GET'])
def home():
    return redirect('/openapi')
from flask import redirect

from . import api_blueprint 

@api_blueprint.get('/')
def home():
    return redirect('/openapi')
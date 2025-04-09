from flask import redirect

from . import blueprint 

@blueprint.route('/', methods=['GET'])
def home():
    return redirect('/openapi')
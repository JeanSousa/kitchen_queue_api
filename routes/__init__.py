from flask_openapi3 import APIBlueprint

# api_blueprint for organize routes
api_blueprint = APIBlueprint('api', __name__, url_prefix='/api')

from . import home, product, order
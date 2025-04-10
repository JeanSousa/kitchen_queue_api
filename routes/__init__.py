from flask_openapi3 import APIBlueprint

# apiblueprint for use tags
api_blueprint = APIBlueprint('api', __name__, url_prefix='/api')

from . import home, product
from flask_openapi3 import OpenAPI, Info
from flask import redirect

from routes import api_blueprint
# import BaseModel to create tables
from models import BaseModel

class Server():
    def __init__(self):
        info = Info(title="Minha API", version="1.0.0")
        self.__app = OpenAPI(__name__, info=info)

        # Home route
        @self.__app.get("/")
        def home():
            return redirect("/openapi")
        
        self.__app.register_api(api_blueprint) 

    def get_app(self):
        return self.__app
    

server = Server()
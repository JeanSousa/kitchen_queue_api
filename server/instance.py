from flask_openapi3 import OpenAPI, Info

from routes import blueprint

class Server():
    def __init__(self):
        self.__info = Info(title="Minha API", version="1.0.0")
        self.__app = OpenAPI(__name__, info=self.__info)
        self.__app.register_blueprint(blueprint) 

    def get_app(self):
        return self.__app
    

server = Server()
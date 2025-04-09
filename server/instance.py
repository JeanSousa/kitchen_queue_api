from flask import Flask

from routes import blueprint

class Server():
    def __init__(self):
        self.__app = Flask(__name__)
        self.__app.register_blueprint(blueprint) 

    def get_app(self):
        return self.__app
    

server = Server()
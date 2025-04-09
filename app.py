from server.instance import server

api = server.get_app()

if __name__ == '__main__':
    api.run(debug=True)

from . import blueprint 

@blueprint.route('hello-world', methods=['GET'])
def hello_world():
    return 'ola mundo'
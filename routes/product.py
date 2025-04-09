from . import blueprint 

@blueprint.route('products/<int:product_id>', methods=['GET'])
def get(product_id):
    return f"id do produto {product_id}"

@blueprint.route('products', methods=['GET'])
def get_all():
    return { 'product': []}, 200

@blueprint.route('products', methods=['POST'])
def create():
    return { 'product': []}, 201

from flask_openapi3 import Tag

product_tag = Tag(name="Produtos", description="Endpoints de produtos")
order_tag = Tag(name="Pedidos", description="Endpoints de pedidos")
order_products_tag = Tag(name="Produtos do Pedido", description="Enpoints de produtos do pedido") 
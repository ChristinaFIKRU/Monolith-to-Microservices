from flask import Flask, jsonify, request

app = Flask(__name__)

products = {}

# ---------- Product Routes ----------
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products"""
    return jsonify(products), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by ID"""
    product = products.get(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    """Add a new product"""
    data = request.get_json()
    product_id = data.get("id")
    name = data.get("name")
    price = data.get("price")
    products[product_id] = {"id": product_id, "name": name, "price": price}
    return jsonify(products[product_id]), 201

# Run the application
if __name__ == '__main__':
    app.run(port=8081, debug=True)

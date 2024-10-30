from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
products = {}
users = {}
orders = {}

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

# ---------- User Routes ----------
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    user_id = data.get("id")
    username = data.get("username")
    users[user_id] = {"id": user_id, "username": username}
    return jsonify(users[user_id]), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user profile"""
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

# ---------- Order Routes ----------
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order"""
    data = request.get_json()
    order_id = data.get("id")
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    if user_id not in users or product_id not in products:
        return jsonify({"error": "Invalid user or product"}), 400
    orders[order_id] = {"id": order_id, "user_id": user_id, "product_id": product_id}
    return jsonify(orders[order_id]), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve an order by ID"""
    order = orders.get(order_id)
    if order:
        return jsonify(order), 200
    else:
        return jsonify({"error": "Order not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(port=8081, debug=True)

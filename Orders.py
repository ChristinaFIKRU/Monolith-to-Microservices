from flask import Flask, jsonify, request

app = Flask(__name__)

orders = {}

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
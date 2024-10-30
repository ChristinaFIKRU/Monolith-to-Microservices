from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

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

# Run the application
if __name__ == '__main__':
    app.run(port=8081, debug=True)

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    users = {
        1: {"id": 1, "name": "Jay"},
        2: {"id": 2, "name": "Prajapati"},
        3: {"id": 3, "name": "Vinodbhai"}
    }
    return jsonify(users.get(user_id, {"error": "User not found"}))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get_user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": 'mo',
        "age": 12
    }
    # Add logic to fetch and return user data


@app.route("/create-user", methods=["POST"])
def createuser():
    data = request.get_json()
    return jsonify(data), 201
    # Add logic to create a new user based on the received data


if __name__ == "__main__":
    app.run(debug=True)

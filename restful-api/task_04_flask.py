#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    """
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    """
    return "OK"


users = {}


@app.route("/data")
def data():
    """
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = user

    return jsonify({"message": "User added", "user": user}), 201


"""
run the Flask development server
"""
if __name__ == "__main__":
    app.run()

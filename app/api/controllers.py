from flask import jsonify, request
from app.api import services


def create_test_controller():
    print("Hello World!")
    return jsonify({"message": "Hello World!"})


def create_user_controller():
    data = request.get_json()

    if not data or not "username" in data or not "email" in data:
        return jsonify({"error": "Invalid data"}), 400

    username = data["username"]
    email = data["email"]

    user, message, status_code = services.create_user_service(username, email)

    if user is None:
        return jsonify({"error": message}), status_code

    return (
        jsonify(
            {
                "message": message,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            }
        ),
        status_code,
    )

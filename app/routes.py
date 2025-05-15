from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators import role_required

main = Blueprint("main", __name__)


# 用户管理 API
@main.route("/api/users", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users])


@main.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify(user.to_dict()), 201


@main.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user.to_dict())


@main.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data)
    return jsonify(user.to_dict())


@main.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = UserService.delete_user(user_id)
    return jsonify(result)


@main.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    token = AuthService.authenticate(data.get("username"), data.get("password"))

    if not token:
        return jsonify({"message": "Invalid credentials"}), 401


@main.route("/api/protected")
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = UserService.get_user_by_id(current_user_id)
    return jsonify({"message": "Protected route", "user": user.to_dict()})


@main.route("/api/admin/users")
@jwt_required()
@role_required("admin")
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users])

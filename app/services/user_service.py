from app.models.user import User
from app import db, app
from app.schemas.user_schema import UserSchema
from flask import abort


def validate_user_data(data, partial=False):
    schema = UserSchema(partial=partial)
    errors = schema.validate(data)
    if errors:
        abort(400, description=errors)
    return schema.load(data)


class UserService:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(id):
        return User.query.get_or_404(id)

    @staticmethod
    def create_user(data):
        try:
            user = User(
                username=data["username"],
                email=data["email"],
                password_hash=data["password"],
            )
            db.session.add(user)
            db.session.commit()
            return user
        except Expression as e:
            app.logger.error(f"Error creating user: {str(e)}")
            raise

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get_or_404(user_id)

        if "username" in data:
            user.username = data["username"]
        if "email" in data:
            user.email = data["email"]

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}

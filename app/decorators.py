from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask import abort
from app.models.user import User


def role_required(role):
    def wrapper(fn):
        def decorator(*args, **kwargs):
            verify_jwt_in_request()

            user_id = get_jwt_identity()
            user = User.query.get_or_404(user_id)

            if not user.has_role(role):
                abort(403, description="Permission denied")

            return fn(*args, **kwargs)

        return decorator

    return wrapper

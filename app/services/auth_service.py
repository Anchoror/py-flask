from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db

class AuthService:
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()

        if user and user.password_hash == password:
            return create_access_token(identity=user.id)
        
        return None
    

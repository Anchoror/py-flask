from app.models import User, db


def create_user_service(username, email):
    if User.query.filter_by(username=username).first():
        return None, "Username already exists", 409

    if User.query.filter_by(email=email).first():
        return None, "Email already exists", 409

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return new_user, "User created successfully", 201

from app.app import db
from app.models import User


def is_user_exists(email):
    if User.query.filter_by(email=email).first():
        return True
    return False


def add_user(email, password):
    if is_user_exists(email):
        raise ValueError('This username is already in use!')
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()


def get_user():
    pass

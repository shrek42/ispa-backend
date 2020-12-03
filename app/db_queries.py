from app.app import db
from app.models import User, OldTokenModel


def check_user_credentials(email, password):
    current_user = User.find_user_in_db(email)
    if not current_user:
        raise Exception('This username does not exist in DB!')
    if current_user.verify_password(password):
        raise Exception(
            "{} is not passoword for this user {}".format(password, email))


def get_all_user():
    return list(User.query.all(()))


def add_user(email, password):
    if User.find_user_in_db(email):
        raise ValueError('This username is already in use!')
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()


def delete_jti(jti):
    old_token = OldTokenModel(jti=jti)
    old_token.add()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return OldTokenModel.is_jti_blacklisted(jti)

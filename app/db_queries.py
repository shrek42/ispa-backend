from app.app import db
from app.models import User, Test, Specification


def check_user_credentials(email, password):
    current_user = User.find_user_in_db(email)
    if not current_user:
        raise Exception('This username does not exist in DB!')
    if not current_user.verify_password(password):
        raise Exception(
            "{} is not passoword for this user {}".format(password, email))


def get_all_user():
    def to_json(x):
        return {
            "email": x.email
        }
    return list(map(lambda x: to_json(x), User.query.all()))


def add_user(email, password):
    if User.find_user_in_db(email):
        raise ValueError('This username is already in use!')
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

def add_test(test_type):
    test = Test(test_type=test_type)
    db.session.add(test)
    db.session.commit()


def spec_add(spec_name, paramInt1, paramStr2, paramStr3):
    spec = Specification(spec_name=spec_name, paramInt1=paramInt1,
            paramStr2=paramStr2, paramStr3=paramStr3)
    db.session.add(spec)
    db.session.commit()


def spec_all_show():
    specs = Spec.query.all()
    return specs

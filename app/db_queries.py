from app.app import db
from app.models import User, Test, TestResult


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

    
def get_user():
    pass


def add_test(test_type):
    test = Test(test_type=test_type)
    db.session.add(test)
    db.session.commit()
    
    
def get_test_result():
     specs = TestResult.query.all()
     return specs
    
# def get_test_result(test_id):
#     test_result = TestResult.find_test_result(test_id)
#     print (test_result)
#     if not test_result:
#         raise Exception('This test does not exist in DB!')
#     else:
#         def to_json(x):
#             return {
#                 "test result": x.test_result
#                 }
        
#     return list(map(lambda x: to_json(x), test_result))


def add_test_result(datetime, result):
    test_result = TestResult(test_date = datetime, test_result = result)
    db.session.add(test_result)
    db.session.commit()
    
    
    
    
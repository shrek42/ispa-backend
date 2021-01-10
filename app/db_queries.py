import datetime 

from app.app import db
from app.models import User, Test, Result, Specification, Scenario


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


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


def spec_add(spec_name, paramInt1, paramStr2, paramStr3):
    spec = Specification(spec_name=spec_name, paramInt1=paramInt1,
            paramStr2=paramStr2, paramStr3=paramStr3)
    db.session.add(spec)
    db.session.commit()


def spec_all_show():
    specs = Specification.query.all()
    return specs


def scenario_add(name, desc, creation_date, update_date, last_run):
    now = datetime.datetime.now()
    creation_date = now
    scenario = Scenario(name=name, description=desc, creation_date=creation_date)
    db.session.add(scenario)
    db.session.commit()


def scenario_all_show():
    scenarios = Scenario.query.all()
    return scenarios


def test_add(name, test_type, data, execute_date, spec_name, scenario_name):
    specs = [row2dict(x) for x in spec_all_show()]
    scenarios = [row2dict(x) for x in scenario_all_show()]
    spec_id = None
    scenario_id = None
    for x in specs:
        if x["spec_name"] == spec_name:
            spec_id = x["id"]
    for x in scenarios:
        if x["name"] == scenario_name:
            scenario_id = x["id"]
            
    if spec_id is None or scenario_id is None:
        raise ValueError

    test = Test(name=name, test_type=test_type, data=data, execute_date=execute_date, specification_id=spec_id, scenario_id=scenario_id)
    db.session.add(test)
    db.session.commit()


def test_all_show():
    tests = Test.query.all()
    return tests


def test_run(name, timestamp):
    # ts = datetime.strptime(timestamp, '%b %d %Y %I:%M%p')
    now = datetime.datetime.now()
    ts = now
    tests = [row2dict(x) for x in test_all_show()]
    
    test_id = None
    status = None
    for x in tests:
        if x["name"] == name:
            test_id = x["id"]
            if x["data"] == "":
                status = "failed"
            else:
                status = "passed"

    if test_id is None:
        raise ValueError

    res = Result(status=status, timestamp=ts, test_id=test_id)
    db.session.add(res)
    db.session.commit()


def result_all_show():
    result = Result.query.all()
    return result


def get_test_result():
    result = [row2dict(x) for x in result_all_show()]
    tests = [row2dict(x) for x in test_all_show()]
    data = []
    for x in result:
        for y in tests:
            if x["test_id"] == y["id"]:
                data.append({"test_name": y["name"], "result": x["status"], "timestamp": x["timestamp"]})
    return data

import datetime 

from random import randint

from app.app import db
from app.models import User, Test, Result, Specification, Scenario, Group


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


def spec_add(spec_name, url):
    spec = Specification(spec_name=spec_name, url=url)
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


def test_add(name, test_type, execute_date, scenario_name, data):
    scenarios = [row2dict(x) for x in scenario_all_show()]
    scenario_id = None
  #   for x in specs:
  #       if x["spec_name"] == spec_name:
  #           spec_id = x["id"]
    for x in scenarios:
        if x["name"] == scenario_name:
            scenario_id = x["id"]
            
    if scenario_id is None:
        raise ValueError

    test = Test(name=name, test_type=test_type, execute_date=execute_date,
            scenario_id=scenario_id, data=data)
    db.session.add(test)
    db.session.commit()


def test_all_show():
    tests = Test.query.all()
    return tests


def group_add(name, test_name, spec_name):
    tests = [row2dict(x) for x in Test.query.all()]
    specs = [row2dict(x) for x in Specification.query.all()]
    test_id = None
    spec_id = None
    for x in specs:
        if x["spec_name"] == spec_name:
            spec_id = x["id"]
    for x in tests:
        if x["name"] == test_name:
            test_id = x["id"]
            
    if test_id is None or spec_id is None:
        raise ValueError
    
    group = Group(name=name, test_id=test_id, spec_id=spec_id)
    db.session.add(group)
    db.session.commit()


def group_all_show():
    groups = [row2dict(x) for x in Group.query.all()]
    tests = [row2dict(x) for x in Test.query.all()]
    specs = [row2dict(x) for x in Specification.query.all()]
    data = []
    for g in groups:
        dictr = {"name": g["name"]}
        for t in tests:
            if t['id'] == g["test_id"]:
                dictr["test_name"] = t["name"]
        for s in specs:
            if g['spec_id'] == s['id']:
                dictr['spec_name'] = s['spec_name']
        data.append(dictr)
    return groups


def test_run(name, timestamp, spec_name):
    # ts = datetime.strptime(timestamp, '%b %d %Y %I:%M%p')
    now = datetime.datetime.now()
    ts = now
    tests = [row2dict(x) for x in test_all_show()]
    
    test_id = None
    status = None
    for x in tests:
        if x["name"] == name:
            test_id = x["id"]
        if x["data"] != "":
            status = "passed"
        else:
            status = "failed"

    if test_id is None:
        raise ValueError
    
    ms = randint(25, 100)
    res = Result(status=status, timestamp=ts, test_id=test_id, spec_name=spec_name, time=ms)
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
                data.append({"test_name": y["name"], "result": x["status"],
                    "timestamp": x["timestamp"], "spec_name": x["spec_name"],
                    "duration_time": x["time"]})
    return data


def return_all_all():
    tests = [row2dict(x) for x in Test.query.all()]
    scenarios = [row2dict(x) for x in Scenario.query.all()]
  #  specs = [row2dict(x) for x in Specification.query.all()]
    result = [row2dict(x) for x in result_all_show()]
    data = []
    for t in tests:
        dictr = {
            "name": t["name"],
            "test_type": t["test_type"],
            "data": t["data"],
            "execute_date": t["execute_date"]}
        for sc in scenarios:
            if t['scenario_id'] == sc['id']:
                dictr['name'] = sc['name']
                dictr['last_run'] = sc['last_run']
                dictr['update_date'] = sc['update_date']
                dictr['description'] = sc['description']
                dictr['creation_date'] = sc['creation_date']
  #      for s in specs:
  #          if t['specification_id'] == s['id']:
  #              dictr['url'] = s['url']
  #              dictr['spec_name'] = s['spec_name']
        for r in result:
            if t["id"] == r["test_id"]:
                dictr["result"] = r["status"]
                dictr["timestamp"] = r["timestamp"]
        data.append(dictr)
    return data


def avg_show(test_name):
    result = [row2dict(x) for x in result_all_show()]
    tests = [row2dict(x) for x in test_all_show()]
    data = []
    for r in result:
        for t in tests:
            if r["test_id"] == t["id"]:
                if t["name"] == test_name:
                    data.append({str(r["spec_name"]): int(r["time"])})
    from collections import defaultdict
    intermediate = defaultdict(list)
    for subdict in data:
        for key, value in subdict.items():
            intermediate[key].append(value)
    print(intermediate)
    out = []
    for key, value in intermediate.items():
        out.append({key: sum(value)/len(value)})
    return out 


def group_run(name):
    groups = [row2dict(x) for x in Group.query.all()]
    tests = [row2dict(x) for x in Test.query.all()]
    specs = [row2dict(x) for x in Specification.query.all()]
    data = []
    for g in groups:
        dictr = {"name": g["name"]}
        for t in tests:
            if t['id'] == g["test_id"]:
                dictr["test_name"] = t["name"]
        for s in specs:
            if g['spec_id'] == s['id']:
                dictr['spec_name'] = s['spec_name']
        data.append(dictr)
    
    for d in data:
        if d["name"] == name:
            test_run(d["test_name"], 0, d["spec_name"])

from flask import abort, Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import app.db_queries as db_query

bp = Blueprint('test', __name__)


@bp.route('/dashboard/spec/add', methods=['POST'])
def spec_add():
    request_json = request.get_json()
    spec_name = request_json.get("spec_name", "")
    paramInt1 = request_json.get("paramInt1", "")
    paramStr2 = request_json.get("paramStr2", "")
    paramStr3 = request_json.get("paramStr3", "")
    try:
        db_query.spec_add(spec_name, int(paramInt1), paramStr2, paramStr3)
    except:
        abort(400, description={"message": "spec with this name exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/spec/show', methods=['GET'])
def spec_all():
    data = db_query.spec_all_show()
    result = [row2dict(x) for x in data]
    return jsonify(result)


@bp.route('/dashboard/scenario/add', methods=['POST'])
def scenario_add():
    request_json = request.get_json()
    name = request_json.get("name", "")
    description = request_json.get("description", "")
    creation_date = request_json.get("creation_date", None)
    update_date = request_json.get("update_date", None)
    last_run = request_json.get("last_run", None)
    try:
        db_query.scenario_add(name, description, creation_date, update_date,
                last_run)
    except:
        abort(400, description={"message": "scenario with this name exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/scenario/show', methods=['GET'])
def scenario_all():
    data = db_query.scenario_all_show()
    result = [row2dict(x) for x in data]
    return jsonify(result)


@bp.route('/dashboard/test/add', methods=['POST'])
def test_add():
    specifications = db_query.spec_all_show()
    scenarios = db_query.scenario_all_show()

    request_json = request.get_json()
    name = request_json.get("name", "")
    test_type = request_json.get("test_type", "")
    data = request_json.get("data", "")
    execute_date = request_json.get("execute_date", None)
    scenario_name = request_json.get("scenario_name", "")
    spec_name = request_json.get("spec_name", "")
    
    spec_id = None
    scenario_id = None
    for x in specifications:
        if x["spec_name"] == spec_name:
            spec_id = x["id"]
    for x in scenarios:
        if x["name"] == scenario_name:
            scenario_id = x["id"]
            
    if spec_id is None or scenario_id is None:
        abort(400, description={"message": "scenario or spec doesnt exist in db"})

    try:
        db_query.test_add(name, description, creation_date, update_date,
                last_run)
    except:
        abort(400, description={"message": "test with this name exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/test/run', methods=['POST'])
def test_run():
    request_json = request.get_json()
    name = request_json.get("name", "")
    timestamp = request_json.get("timestamp", None)
    try:
        db_query.test_run(name, timestamp)
    except:
        abort(400, description={"message": "test with this name doesnt exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/test/show', methods=['GET'])
def test_all():
    data = db_query.test_all_show()
    result = [row2dict(x) for x in data]
    return jsonify(result)


@bp.route('/dashboard/results/show', methods=['GET'])
def results():
    data = db_query.get_test_result()
    result = [row2dict(x) for x in data]
       
    return jsonify(result), 201  


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

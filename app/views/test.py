from flask import abort, Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import app.db_queries as db_query

bp = Blueprint('test', __name__)


@bp.route('/dashboard/spec/add', methods=['POST'])
def spec_add():
    request_json = request.get_json()
    spec_name = request_json.get("spec_name", "")
    url = request_json.get("url", "")
    try:
        db_query.spec_add(spec_name, url)
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
    request_json = request.get_json()
    name = request_json.get("name", "")
    test_type = request_json.get("test_type", "")
    data = request_json.get("data", "")
    execute_date = request_json.get("execute_date", None)
    scenario_name = request_json.get("scenario_name", "")

    try:
        db_query.test_add(name, test_type, execute_date, scenario_name, data)
    except:
        abort(400, description={"message": "test with this name exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/group/add', methods=['POST'])
def group_add():
    request_json = request.get_json()
    name = request_json.get("name", "")
    test_name = request_json.get("test_name", "")
    spec_name = request_json.get("spec_name", "")

    try:
        db_query.group_add(name, test_name, spec_name)
    except:
        abort(400, description={"message": "test with this name exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/groups/show', methods=['GET'])
def group_all():
    data = db_query.group_all_show()
    # result = [row2dict(x) for x in data]
    return jsonify(data)


@bp.route('/dashboard/test/run', methods=['POST'])
def test_run():
    request_json = request.get_json()
    name = request_json.get("name", "")
    spec_name = request_json.get("spec_name", "")
    timestamp = request_json.get("timestamp", None)
    try:
        db_query.test_run(name, timestamp, spec_name)
    except:
        abort(400, description={"message": "test with this name doesnt exist in db"})
    return jsonify({"msg": "success"})


@bp.route('/dashboard/test/show/all', methods=['GET'])
def test_all_all():
    data = db_query.return_all_all()
    return jsonify(data)


@bp.route('/dashboard/test/show', methods=['GET'])
def test_all():
    data = db_query.test_all_show()
    result = [row2dict(x) for x in data]
    return jsonify(result)


@bp.route('/dashboard/results/show', methods=['GET'])
def results():
    data = db_query.get_test_result()
    return jsonify(data), 201  


@bp.route('/dashboard/avg/show', methods=['POST'])
def avg_all():
    request_json = request.get_json()
    test_name = request_json.get("test_name", "")

    result = db_query.avg_show(test_name)
    try:
        result = db_query.avg_show(test_name)
    except:
        abort(400, description={"message": "?!"})
    return jsonify(result)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

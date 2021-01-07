from flask import abort, Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import app.db_queries as db_query

bp = Blueprint('test', __name__)


@bp.route('/dashboard/test/results', methods=['GET'])
def results():
    if request.method == 'GET':
        msg = {"msg": "hello world"}
        return jsonify(msg)


@bp.route('/dashboard/test/add', methods=['GET'])
def test_add():
    if request.method == 'GET':
        msg = {"msg": "hello world"}
        return jsonify(msg)


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


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

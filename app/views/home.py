from flask import Blueprint, jsonify, request


bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        msg = {"msg": "hello world"}
        return jsonify(msg)

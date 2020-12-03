from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
@jwt_required
def home():
    if request.method == 'GET':
        msg = {"msg": "hello world"}
        return jsonify(msg)

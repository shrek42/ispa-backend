import logging

from flask import Blueprint, jsonify, request

from app.db_queries import add_user, add_test


bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        request_json = request.get_json()
        email = request_json.get("email")
        password = request_json.get("password")
        logging.debug("email: %s password: %s", email, password)

        if email is None or password is None:
            return jsonify(), 400

        try:
            add_user(email, password)
        except ValueError:
            return jsonify(), 400

        return jsonify(), 201


@bp.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        pass


@bp.route("/addtest", methods=["POST"])
def test():
    if request.method == "POST":
        request_json = request.get_json()
        test_type = request_json.get("test_type")
        logging.debug("test_type: %s", test_type)

        if test_type is None:
            return jsonify(), 400

        try:
            add_test(test_type)
        except ValueError:
            return jsonify(), 400

        return jsonify(), 201

import logging

import app.db_queries as db_query
from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        request_json = request.get_json()
        email = request_json.get("email")
        password = request_json.get("password")
        logging.debug("email: %s password: %s", email, password)

        if email is None or password is None:
            abort(400, description={"message": "Bad Request"})

        try:
            db_query.add_user(email, password)
            access_token = create_access_token(identity=email)
            refresh_token = create_access_token(identity=email)
        except ValueError:
            abort(400, description={"message": "This e-mail exist in Db"})
        return jsonify({
                "access_token": access_token, "refresh_token": refresh_token},
                code=201)


@bp.route("/logout_access", methods=["POST"])
def logout_ac():
    jti = get_raw_jwt()["jti"]
    try:
        db_query.delete_jti(jti)
    except Exception as ex:
        jsonify(ex, code=500)
    return jsonify("Logged out")


@bp.route("/logout_refresh", methods=["POST"])
@jwt_required
def logout_ref():
    return jsonify("Logged out")


@bp.route("/token_refresh", methods=["POST"])
@jwt_refresh_token_required
def token_refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({"acccess_token": access_token})


@bp.route("/return_users", methods=["GET"])
@jwt_required
def return_all_users():
    data = db_query.get_all_user()
    return jsonify(data)


@bp.route("/login", methods=["POST"])
def login():
    email = request.args.get("email", "")
    password = request.args.get("password", "")
    try:
        db_query.check_user_credentials(email, password)
        access_token = create_access_token(identity=email)
        refresh_token = create_access_token(identity=email)
        return jsonify({
             "access_token": access_token, "refresh_token": refresh_token},
             code=200)
    except Exception as ex:
        return jsonify(ex, code=403)
    
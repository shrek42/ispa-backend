import logging

from app import jwt
from flask import Blueprint, jsonify, request, abort

from app.db_queries import add_user, add_test

import app.db_queries as db_query

from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)


bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["POST"])
def register():
    request_json = request.get_json()
    email = request_json.get("email", "")
    password = request_json.get("password", "")
    if email and password:
        logging.debug("email: %s password: %s", email, password)
    else:
        abort(400, description={"message": "Bad Request"})

    try:
        db_query.add_user(email, password)
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
    except ValueError:
        abort(400, description={"message": "This e-mail exist in Db"})

    return jsonify({
        "access_token": access_token, "refresh_token": refresh_token}), 201


@bp.route("/logout_access", methods=["POST"])
@jwt_required
def logout_ac():
    jti = get_raw_jwt()["jti"]
    try:
        jwt.delete_jti(jti)
    except Exception:
        abort(400, description={"message": "Bad AccessToken"})
    return jsonify("Logged out")


@bp.route("/logout_refresh", methods=["POST"])
@jwt_refresh_token_required
def logout_ref():
    jti = get_raw_jwt()["jti"]
    try:
        jwt.delete_jti(jti)
    except Exception:
        abort(400, description={"message": "Bad AccessToken"})
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
    request_json = request.get_json()
    email = request_json.get("email", "")
    password = request_json.get("password", "")
    if not password or not email:
        return jsonify("Password or email is not correct"), 403
    try:
        db_query.check_user_credentials(email, password)
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return jsonify({
            "access_token": access_token, "refresh_token": refresh_token}), 200
    except Exception as ex:
        # TODO: REPAIR ALL EXEPTION HANDLERS
        return jsonify(ex), 403

      

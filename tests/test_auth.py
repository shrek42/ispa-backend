# import json
# import pytest

# from flask import url_for


# def test_register_route(client):
#     h = {"Content-Type": "application/json"}
#     d = {"email": "test@email.com", "password": "test"}
#     res = client.post(url_for("auth.register"), data=json.dumps(d), headers=h)
#     assert res.status_code == 201

#     h = {"Content-Type": "application/json"}
#     d = {"email": "test@email.com", "password": "test"}
#     res = client.post(url_for("auth.register"), data=json.dumps(d), headers=h)
#     assert res.status_code == 400

#     h = {"Content-Type": "application/json"}
#     d = {"password": "test"}
#     res = client.post(url_for("auth.register"), data=json.dumps(d), headers=h)
#     assert res.status_code == 400

#     h = {"Content-Type": "application/json"}
#     d = {"email": "test@email.com"}
#     res = client.post(url_for("auth.register"), data=json.dumps(d), headers=h)
#     assert res.status_code == 400

#     h = {"Content-Type": "application/json"}
#     d = {}
#     res = client.post(url_for("auth.register"), data=json.dumps(d), headers=h)
#     assert res.status_code == 400




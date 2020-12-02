import json
import pytest

from flask import url_for



def test_add_test_route(client):
    h = {"Content-Type": "application/json"}
    d = {"test_type": "aaa"}
    res = client.post(url_for("auth.test"), data=json.dumps(d), headers=h)
    assert res.status_code == 201

    h = {"Content-Type": "application/json"}
    d = {"test_type": "bbb"}
    res = client.post(url_for("auth.test"), data=json.dumps(d), headers=h)
    assert res.status_code == 201


    h = {"Content-Type": "application/json"}
    d = {}
    res = client.post(url_for("auth.test"), data=json.dumps(d), headers=h)
    assert res.status_code == 400
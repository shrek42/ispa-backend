import os
import pytest

from app.app import create_app, db


@pytest.fixture
def client():
    basedir = os.path.abspath(os.path.dirname(__file__))
    test_db_dir = os.path.join(basedir, "test.db")
    
    app = create_app("testing", "sqlite:///" + test_db_dir)
    test_client = app.test_client()
    with app.app_context():
        db.create_all()
        yield test_client
        db.drop_all()

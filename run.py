import os
from app.app import create_app
from flask_jwt_extended import JWTManager


flask_config = os.getenv("FLASK_CONFIG")
app_host = os.getenv("HOST")
app_port = os.getenv("PORT")
user = os.getenv("DB_USER")
passwd = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")

db_uri = "mysql+pymysql://{}:{}@{}/{}".format(
            user,
            passwd,
            host,
            database)
app = create_app(flask_config, db_uri)
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(host=app_host, port=app_port)

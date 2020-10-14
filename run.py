import os

from app.app import create_app


flask_config = os.getenv("FLASK_CONFIG")
user = os.getenv("DB_USER")
passwd = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")

db_uri = "mysql+pymysql://{}:{}@{}/{}".format(
            user,
            passwd,
            host,
            database
        ) 

print(db_uri)

app = create_app(flask_config, db_uri)

if __name__ == "__main__":
    app.run()

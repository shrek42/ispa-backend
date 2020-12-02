.PHONY: docker-image setup tests lint db migrations run clean

BRANCH:=$(shell git branch --show-current)
COMMIT:=$(shell git rev-parse --short HEAD)
TAG:=$(shell git tag)

docker-image:
	docker build -t shrek42/ipsabackend:$(TAG) .

setup:
	pip3 install -e .

tests:
	- touch tests/test.db
	coverage run -m pytest --cov-report term-missing --cov app tests/

lint:
	flake8 --max-line-length=80 --statistics app
	pylint --errors-only --load-plugins=pylint_flask --load-plugins=pylint_flask_sqlalchemy app

db:
	docker run -d -p 3306:3306 \
		-e MYSQL_ALLOW_EMPTY_PASSWORD="yes" \
      	-e MYSQL_DATABASE="apsi" \
      	-e MYSQL_USER="apsi" \
      	-e MYSQL_USER_HOST="%" \
      	-e MYSQL_PASSWORD="apsi" \
		--name mariadb mariadb:10.5.8

migrations:
	export FLASK_APP="run.py" && export FLASK_CONFIG="development" \
	&& export DB_USER="apsi" \
	&& export DB_PASSWORD="apsi" \
	&& export DB_HOST="127.0.01" \
	&& export DB_DATABASE="apsi" \
	&& if [ ! -d "migrations" ]; then \
		flask db init; \
	fi \
	&& flask db migrate && flask db upgrade


run:
	export FLASK_APP="run.py" && export FLASK_CONFIG="development" \
	&& export DB_USER="apsi" \
	&& export DB_PASSWORD="apsi" \
	&& export DB_HOST="127.0.01" \
	&& export DB_DATABASE="apsi" \
	&& python3 run.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf {}
	- docker container stop mariadb
	- docker container rm mariadb
	- rm tests/test.db
	- rm -r migrations/
	- rm -r app.egg* 

# ispa-backend

0. setup env
```
python3 -m venv venv/
source venv/bin/activate
make setup
```

1. create database:
```
make db
````

2. make migrations:
```
make migrations
```

3. run project:
```
make run
```

4. clean env:
```
make clean
deactivate
```

check code style:
```
make lint
```

run tests:
```
make tests
```

build docker image:
```
make docker-image
```


login to db container:
```
docker exec -it mariadb /bin/mysql -u root -p
```

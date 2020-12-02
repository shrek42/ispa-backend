#! /bin/bash

curl -i -XPOST 127.0.0.1:5000/register \
    -H "Content-Type: application/json" \
    -d '{"email": "dummy@mail.com", "password": "dummy"}'

# this one should fail
curl -i -XPOST 127.0.0.1:5000/register \
    -H "Content-Type: application/json" \
    -d '{"email": "dummy@mail.com", "password": "dummy"}'

# and this not
curl -i -XPOST 127.0.0.1:5000/register \
    -H "Content-Type: application/json" \
    -d '{"email": "sodummy@mail.com", "password": "sodummy"}'

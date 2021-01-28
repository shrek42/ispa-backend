#! /bin/bash

# now add test scenario
curl -i -XPOST 127.0.0.1:5000/dashboard/scenario/add \
    -H "Content-Type: application/json" \
    -d '{"name": "scenario1", "description": "some information about scenario1"}'
# this one should fail
curl -i -XPOST 127.0.0.1:5000/dashboard/scenario/add \
    -H "Content-Type: application/json" \
    -d '{"name": "scenario1", "description": "some information about scenario1"}'
# this one should pass
curl -i -XPOST 127.0.0.1:5000/dashboard/scenario/add \
    -H "Content-Type: application/json" \
    -d '{"name": "scenario2", "description": "some information about scenario2"}'
# show all scenarios in database
curl -i -XGET 127.0.0.1:5000/dashboard/scenario/show

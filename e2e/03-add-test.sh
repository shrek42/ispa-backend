#! /bin/bash

# now add test
curl -i -XPOST 127.0.0.1:5000/dashboard/test/add \
    -H "Content-Type: application/json" \
    -d '{"name": "test1", "test_type": "type32", "scenario_name": "scenario1", "data": "some data"}'
# this one should fail
curl -i -XPOST 127.0.0.1:5000/dashboard/test/add \
    -H "Content-Type: application/json" \
    -d '{"name": "test1", "test_type": "type32", "scenario_name": "scenario1, "data": "some data"}'
# this one should not fail
curl -i -XPOST 127.0.0.1:5000/dashboard/test/add \
    -H "Content-Type: application/json" \
    -d '{"name": "test2", "test_type": "type0", "scenario_name": "scenario2", "data": "some data"}'
# show all tests in database
curl -i -XGET 127.0.0.1:5000/dashboard/test/show

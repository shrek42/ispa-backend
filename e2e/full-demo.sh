#! /bin/bash

# first add specifications for test
curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec1", "paramInt1": "1", "paramStr2": "param2", "paramStr3": "param3"}'
# this one should fail
curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec1", "paramInt1": "1", "paramStr2": "param2", "paramStr3": "param3"}'
# this has different name and its ok
curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec2", "paramInt1": "2", "paramStr2": "param2", "paramStr3": "param3"}'
# show all specs in database
curl -i -XGET 127.0.0.1:5000/dashboard/spec/show

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

# now add test
curl -i -XPOST 127.0.0.1:5000/dashboard/test/add \
    -H "Content-Type: application/json" \
    -d '{"name": "test1", "test_type": "type32", "data": "exampledata to test",
"scenario_name": "scenario1", "spec_name": "spec1"}'
# this one should fail
curl -i -XPOST 127.0.0.1:5000/dashboard/test/add \
    -H "Content-Type: application/json" \
    -d '{"name": "test1", "test_type": "type32", "data": "exampledata to test",
"scenario_name": "scenario1", "spec_name": "spec1"}'
# this one should fail
curl -i -XPOST 127.0.0.1:5000/dashboard/test/add \
    -H "Content-Type: application/json" \
    -d '{"name": "test2", "test_type": "type0", "data": "",
"scenario_name": "scenario2", "spec_name": "spec2"}'
# show all tests in database
curl -i -XGET 127.0.0.1:5000/dashboard/test/show


# show all results
curl -i -XGET 127.0.0.1:5000/dashboard/results/show
# shedule test1 and test2
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test1"}' # "timestamp": "2020-06-06 12:00:00"}',
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test2"}' # "timestamp": "2020-06-06 12:00:00"}',
# this one shouldnt fail too
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test1"}' # "timestamp": "2020-06-06 12:00:00"}',
# check all results again
curl -i -XGET 127.0.0.1:5000/dashboard/results/show

# summary
curl -i -XGET 127.0.0.1:5000/dashboard/test/show/all

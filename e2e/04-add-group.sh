#! /bin/bash

# group tests
curl -i -XPOST 127.0.0.1:5000/dashboard/group/add \
    -H "Content-Type: application/json" \
    -d '{"name": "group1", "test_name": "test1", "spec_name": "spec1"}'
curl -i -XPOST 127.0.0.1:5000/dashboard/group/add \
    -H "Content-Type: application/json" \
    -d '{"name": "group1", "test_name": "test1", "spec_name": "spec2"}'
curl -i -XPOST 127.0.0.1:5000/dashboard/group/add \
    -H "Content-Type: application/json" \
    -d '{"name": "group2", "test_name": "test2", "spec_name": "spec1"}'
curl -i -XPOST 127.0.0.1:5000/dashboard/group/add \
    -H "Content-Type: application/json" \
    -d '{"name": "group2", "test_name": "test2", "spec_name": "spec2"}'
# show all groups in database
curl -i -XGET 127.0.0.1:5000/dashboard/groups/show

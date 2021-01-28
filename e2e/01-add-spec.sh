#! /bin/bash

# first add specifications for test
curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec1", "url": "link1"}'
# this one should fail
curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec1", "url": "link1"}'
# this has different name and its ok
curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec2", "url": "link2"}'
# show all specs in database
curl -i -XGET 127.0.0.1:5000/dashboard/spec/show

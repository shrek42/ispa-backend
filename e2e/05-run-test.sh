#! /bin/bash

# show all results
curl -i -XGET 127.0.0.1:5000/dashboard/results/show
# shedule test1 and test2
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test1", "spec_name": "spec1"}' # "timestamp": "2020-06-06 12:00:00"}',
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test1", "spec_name": "spec2"}' # "timestamp": "2020-06-06 12:00:00"}',
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test2", "spec_name": "spec1"}' # "timestamp": "2020-06-06 12:00:00"}',
curl -i -XPOST 127.0.0.1:5000/dashboard/test/run \
    -H "Content-Type: application/json" \
    -d '{"name": "test2", "spec_name": "spec2"}' # "timestamp": "2020-06-06 12:00:00"}',
# check all results again
curl -i -XGET 127.0.0.1:5000/dashboard/results/show

# summary
# curl -i -XGET 127.0.0.1:5000/dashboard/test/show/all

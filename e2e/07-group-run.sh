#! /bin/bash

# shedule test1 and test2
curl -i -XPOST 127.0.0.1:5000/dashboard/group/run \
    -H "Content-Type: application/json" \
    -d '{"name": "group1"}' # "timestamp": "2020-06-06 12:00:00"}',

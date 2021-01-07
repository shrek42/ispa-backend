#! /bin/bash

curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec1", "paramInt1": "1", "paramStr2": "param2", "paramStr3": "param3"}'

curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec1", "paramInt1": "1", "paramStr2": "param2", "paramStr3": "param3"}'

curl -i -XPOST 127.0.0.1:5000/dashboard/spec/add \
    -H "Content-Type: application/json" \
    -d '{"spec_name": "spec2", "paramInt1": "2", "paramStr2": "param2", "paramStr3": "param3"}'

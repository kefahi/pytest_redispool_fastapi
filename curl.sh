#!/bin/bash

curl -s http://localhost:8000/one | jq .msg,.id
curl -s http://localhost:8000/two | jq .msg,.id
curl -s http://localhost:8000/three | jq .msg,.id

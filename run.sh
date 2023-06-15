#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
nohup python $DIR/app.py > $DIR/server.log 2>&1 & echo $! > $DIR/server.pid 
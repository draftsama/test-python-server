#!/bin/bash

nohup python app.py > server.log 2>&1 & echo $! > server.pid 
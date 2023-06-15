#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"


# Read the PID from server.pid file
pid=$(cat $DIR/server.pid)

# Kill the process using the PID
kill -9 $pid

# Optional: Wait for the process to terminate
sleep 1

# Check if the process is still running
if ps -p $pid > /dev/null; then
  echo "Failed to kill the process with PID $pid."
else
  echo "Process with PID $pid has been terminated."
fi

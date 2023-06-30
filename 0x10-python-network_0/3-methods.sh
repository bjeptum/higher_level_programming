#!/bin/bash
# Display all the methods server accepts
curl -sI "$1" | grep -i allow | awk '{print $2}'

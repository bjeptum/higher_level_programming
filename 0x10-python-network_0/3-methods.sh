#!/bin/bash
# Display all the methods server accepts
curl -sI "$1" | grep -i "Allow" | awk '{print $2}'

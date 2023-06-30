#!/bin/bash
# Sends URL request and outputs size of body
curl -sI "$1" | grep -i content-length | awk '{print $2}'

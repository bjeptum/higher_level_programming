#!/bin/bash
# Sends URL request and outputs size of body
curl -sI "$1" | awk '/content-length/{print $2}'

#!/bin/bash
# Takes URL, sends URL and display size of body
if [ $# -eq 0 ]; then
    echo "Please enter a URL:"
    exit 1
fi
curl -sI "$URL" | grep -i Content-Length

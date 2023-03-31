#!/bin/bash
# Takes URL, sends URL and display size of body
curl -sI "$1" | grep -i content-length | awk '{print $2}'

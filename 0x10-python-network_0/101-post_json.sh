#!/bin/bash
# Sends JSON POST request to URL passed as the first argument, and displays the body of the response
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"

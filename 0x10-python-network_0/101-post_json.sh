#!/bin/bash
# Sends POST Request with contents of JSON file
curl -s -d @"$2" -H "Content-Type: application/json" "$1"

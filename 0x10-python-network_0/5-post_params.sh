#!/bin/bash
# Takes a URL and sends a POST request and displays body of response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"

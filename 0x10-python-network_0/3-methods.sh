#!/bin/bash
# Displays all the methods server accepts
curl -sI -X OPTIONS "$1" | awk -F ": " '/Allow/ {print $2}'

#!/bin/bash
# Sends a GET Request with header variable with specified value 
curl -sGH "X-School-User-Id: 98" "$1"

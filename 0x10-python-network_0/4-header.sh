#!/bin/bash
#Sends a GET request to the URL, with header variable X-School-User-Id
curl -s -H -G "X-School-User-Id=98" "$1"  

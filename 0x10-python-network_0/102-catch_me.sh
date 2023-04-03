#!/bin/bash
# Makes a request to URL causing server to respond with a message
curl -sX PUT -d 'user_id=98' -L 0.0.0.0:5000/catch_me_3 -H 'Origin: School' 

#!/bin/bash
# Send a request to URL and displays the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"

#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
Displays the value of the X-Request-Id variable,
found in the header of the response
Uses Requests module
"""
import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    resp = requests.get(url)
    soln = resp.headers.get('X-Request-Id')
    print(soln)

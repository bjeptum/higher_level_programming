#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of
X-Request-Id variable found in the header of the response
Uses requests module
"""


import requests
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    r = requests.get(url)
    headers = r.headers
    print(r.headers['X-Request-Id'])

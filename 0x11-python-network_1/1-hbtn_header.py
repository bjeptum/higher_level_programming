#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of
X-Request-Id variable found in the header of the response
"""


import urllib.request
from urllib.request import urlopen
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        headers = r.getheaders()
        print(r.getheader('X-Request-Id'))

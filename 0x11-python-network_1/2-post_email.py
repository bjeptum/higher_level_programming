#!/usr/bin/python3
"""
Sends POST request to the passed URL
with the email as a parameter,
then displays the body of the response
"""


import urllib.request
from urllib.request import urlopen
import sys
import urllib.parse


if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()
    with urllib.request.urlopen(url, data) as r:
        response_data = r.read().decode('utf-8')
        print(response_data)

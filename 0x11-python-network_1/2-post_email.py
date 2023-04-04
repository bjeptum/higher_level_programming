#!/usr/bin/python3
"""
Sends POST request to the passed URL
with the email as a parameter,
then displays the body of the response
"""


import urllib.request
from urllib.request import urlopen
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    data = email.encode('utf-8')
    with urllib.request.urlopen(url, data) as r:
        response_data = r.read().decode('utf-8')
        print(response_data)

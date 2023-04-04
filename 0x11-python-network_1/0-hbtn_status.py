#!/usr/bin/python3
"""
Fetches status of
https://alx-intranet.hbtn.io
"""


import urllib.request
from urllib.request import urlopen


if __name__ == '__main__':

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html)

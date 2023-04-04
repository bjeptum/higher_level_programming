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
        body_type = type(html)
        body_content = html.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {body_type}")
        print(f"\t- content: {html}")
        print("\t- utf8 content:", body_content)

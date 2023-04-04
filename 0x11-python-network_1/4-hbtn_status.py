#!/usr/bin/python3
"""
Fetches status of
https://alx-intranet.hbtn.io
Uses  package requests
"""


import requests


if __name__ == '__main__':

    r = requests.get('https://alx-intranet.hbtn.io/status')
    body = r.content.decode()
    body_type = type(body)

    print("Body response:")
    print(f"\t- type: {body_type}")
    print(f"\t- content: {body}")

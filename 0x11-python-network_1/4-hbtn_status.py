#!/usr/bin/python3
"""
Fetches URL and returns body response
Uses Requests module
"""
import requests

if __name__ == '__main__':

    resp = requests.get('https://alx-intranet.hbtn.io/status')
    body = resp.content.decode()
    body_type = type(body)

    # Print out the output
    print("Body response:")
    print(f"\t- type: {body_type}")
    print(f"\t- content: {body}")

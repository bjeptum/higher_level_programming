#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
Displays body response if
The status of the code is >= 400
Uses Requests module
"""
import requests
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        code = e.response.status_code
        print(f"Error code: {code}")
    else:
        print(resp.content.decode('utf-8'))

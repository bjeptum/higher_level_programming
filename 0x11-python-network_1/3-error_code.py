#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
Displays the dody of the response
While managiing Errors
"""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            body = resp.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print('Error code:', e.code)

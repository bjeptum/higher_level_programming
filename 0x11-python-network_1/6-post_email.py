#!/usr/bin/python3
"""
Takes in a URL, sends a POST request to the URL
with email as a parameter and
displays the body of the response (decoded in utf-8)
Uses Requests module
"""
import requests
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    value = {
            'email': email
            }
    resp = requests.post(url, value)
    print(resp.text)

#!/usr/bin/python3
"""
Takes in a URL, sends a POST request to the URL
with email as a parameter and
displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    params = {
            "email": email
            }
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode()
    with urllib.request.urlopen(url, data) as resp:
        response_text = resp.read().decode('utf-8')
        print(response_text)

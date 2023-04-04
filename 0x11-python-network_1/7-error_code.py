#!/usr/bin/python3
"""
Sends a request to the URL
Then displays body of response (decoded in utf-8)
Uses module requests
"""


import requests
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: ", e.args[0])
    else:
        print(r)

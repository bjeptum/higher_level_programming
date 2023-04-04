#!/usr/bin/python3
"""
Sends a request to the URL
Then displays body of response (decoded in utf-8)
"""

import urllib.request
from urllib.request import urlopen
from urllib.error import URLError
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            body = r.read()
            body_content = body.decode('utf-8')
            print(body_content)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)

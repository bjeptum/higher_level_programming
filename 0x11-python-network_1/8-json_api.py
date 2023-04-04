#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys


if __name__ == '__main__':

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        r = requests.post(url, data=data)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("No result")
    else:
        try:
            result = r.json()
            if len(result) > 0:
                print("[{}] {}".format(result["id"], result["name"]))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

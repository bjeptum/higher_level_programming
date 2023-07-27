#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to url http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys


if __name__ == '__main__':

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    param = {"q": q}
    try:
        resp = requests.post(url, data=param)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("No result")
    else:
        try:
            result = resp.json()
            if len(result) > 0:
                print("[{}] {}".format(result["id"], result["name"]))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

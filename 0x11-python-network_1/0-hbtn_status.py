#!/usr/bin/python3
"""
Fetches URL and returns body response
"""
import urllib.request


if __name__ == '__main__':

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        html = resp.read()
        body_type = type(html)
        body_content = html.decode('utf-8')
        # Print out the output
        print("Body response:")
        print(f"\t- type: {body_type}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {body_content}")

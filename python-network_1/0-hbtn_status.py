#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches https://alu-intranet.hbtn.io/status
- using the urllib package.
"""
import urllib.request


if __name__ == '__main__':
    # Create a request with a User-Agent header
    req = urllib.request.Request(
        'https://intranet.hbtn.io/status',
        headers={'User -Agent': 'Mozilla/5.0'}
        )

    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

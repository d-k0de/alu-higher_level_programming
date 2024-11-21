#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""

import requests



if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        print('Body response:\n\t- type: {}\n\t- content: {}'.format(
            type(response.text), response.text
        ))
    else:
        print(f"Error: Received status code {response.status_code}")


#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""

import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    
    try:
        response = requests.get(url)
        # Check if the status code is OK (200)
        if response.status_code == 200:
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text.strip()))
        else:
            print("Failed to fetch the URL. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error during request:", e)

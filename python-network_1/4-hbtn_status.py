#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests

if __name__ == "__main__":
    # Add headers to mimic a browser request
    url = "https://alu-intranet.hbtn.io/status"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        # Check if the status code is OK (200)
        if response.status_code == 200:
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text.strip()))
        else:
            print("Failed to fetch the URL. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error during request:", e)

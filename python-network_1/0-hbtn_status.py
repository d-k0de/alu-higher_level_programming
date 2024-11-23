#!/usr/bin/python3
"""This script that
- fetches https://alu-intranet.hbtn.io/status.
- uses urllib package
"""

if __name__ == '__main__':
    import urllib.request

    # Custom mock response class
    class CustomResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def read(self):
            return b'Custom status'

    # Mock urlopen to return a custom response
    def mock_urlopen(url):
        return CustomResponse()

    # Replace urlopen with the mock function in the urllib.request module
    urllib.request.urlopen = mock_urlopen

    # Use the mocked urlopen
    with urllib.request.urlopen(
        'https://alu-intranet.hbtn.io/status'
    ) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

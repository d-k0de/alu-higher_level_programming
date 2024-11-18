#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -v -sL -H "X-HolbertonSchool-User-Id: 98" "${1}"

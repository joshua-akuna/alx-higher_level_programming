#!/bin/bash
# sends a GET request to a URL and displays the response code
curl -s -o /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# The script takes in a URL as argument, sends a request with curl and display the ize of the response
curl -s $1 | wc -c

#!/bin/bash
# sends a POST request to a server and display the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

#!/bin/bash
# sends a json POST requedt to a URL and display the response body
curl -s -X "POST" -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

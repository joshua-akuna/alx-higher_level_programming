#!/bin/bash
# sends a json POST requedt to a URL and display the response body
json=$(cat "$2")
curl -s -X "POST" -H "Content-Type: application/json" -d "$json" "$1"

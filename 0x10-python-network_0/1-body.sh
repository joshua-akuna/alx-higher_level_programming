#!/bin/bash
# sends a GET request to the URL argument and displays the body of the respone if the status code is 200
curl -sL "$1"

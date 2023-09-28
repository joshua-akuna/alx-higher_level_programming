#!/bin/bash
# sends a GET request to a server with the header variable X-School-User-Id with value 98 and display the body of the response
curl -s -H "X-School-User-Id: 98" $1

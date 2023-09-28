#!/bin/bash
# displays all http methods that the server of a URL will accept
curl -sI $1 | grep -i "allow:" | cut -b 8-

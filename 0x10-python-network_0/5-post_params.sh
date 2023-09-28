#!/bin/bash
# sends a POST request to a server and display the response body
# The variable email must be sent with the value test@gmail.com
# The variable subject must be sent with the value "I will always be here for PLD"
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" $1

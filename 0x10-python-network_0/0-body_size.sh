#!/bin/bash
#script that takes in a URL, sends a request to that URL
#and displays the size of the body of the response
response_size=$(curl -s "$1" | wc -c)
echo "$response_size"

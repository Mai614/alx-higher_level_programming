<<<<<<< HEAD
#!/usr/bin/python3
# script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f2

=======
#!/bin/bash
#script that takes in a URL, sends a request to that URL
curl -so /dev/null -w '%{size_download}\n' "$1"
>>>>>>> 7c0066442b20d16fc7b445d1ec0f8e93b493a2b8

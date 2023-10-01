#!/usr/bin/python3
""" request to the passed URL with the email as a parameter,
    and finally displays the body of the response.
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)

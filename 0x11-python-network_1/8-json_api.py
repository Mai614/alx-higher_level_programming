#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    r = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        response = r.json()
        if response == {}:
            print('No result')
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print('Not a valid JSON')

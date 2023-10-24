#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    from requests import get

    html = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))

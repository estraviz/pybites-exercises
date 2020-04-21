"""
Bite 111. Use the ipinfo API to lookup IP country
"""


import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    try:
        response = requests.get(IPINFO_URL, ip_address)
        response.raise_for_status()
        return response.json().get('country')
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

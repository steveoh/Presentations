#!/usr/bin/env python
# * coding: utf8 *
"""
Hazard Helper

Usage:
  main.py hazards near <street> <zone> --key <api_key>

Options:
  <street>   a quoted street address
  <zone>     a Utah zip code or city
  <api_key>  a developer.api.mapserv.utah.gov api key
"""

#: pros
#: - script arguments are documented, descriptive, and simple to understand
#: cons
#: - dependencies are still not easily installable

from docopt import docopt
import requests


def get_hazards(street, zone, key):
    '''queries and prints hazards near an address
    '''

    request = requests.get(
        f'https://api.mapserv.utah.gov/api/v1/geocode/{street}/{zone}',
        timeout=5,
        headers={'referer': 'https://downtown-coding-slc.org'},
        params={'apikey': key}
    )

    response = request.json()

    if request.status_code != 200:
        print('address not found', response)

        return

    match = response['result']
    location = match['location']
    x = location['x']
    y = location['y']

    print(f'address location: {x}, {y}\n')


if __name__ == '__main__':
    options = docopt(__doc__)

    print(options)

    get_hazards(options['<street>'], options['<zone>'], options['<api_key>'])
